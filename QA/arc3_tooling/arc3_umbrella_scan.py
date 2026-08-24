#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arc III umbrella draft-debris scan. Read-only.
Targets content/story/chapter-03.md ONLY. Detects:
  - meta/author markers (Let me, Here is the correction, Corrected, Version A/B, Montage,
    Lore Confirmed, Rewrite, craft-note phrasing)
  - bold scaffold headings (** ... **) and duplicates thereof
  - duplicated paragraphs (normalized, >=35 chars)
  - duplicated scene-heading lines
Outputs QA/arc3_tooling/arc3_umbrella_scan.txt
"""
import re, os, collections

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UMB = os.path.join(BASE, "content", "story", "chapter-03.md")
TAG_RE = re.compile(r"<[^>]+>")
raw_lines = open(UMB, encoding="utf-8").read().split("\n")

here = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(here, "arc3_umbrella_scan.txt"), "w", encoding="utf-8")
def P(*a): out.write(" ".join(str(x) for x in a) + "\n")

def strip_tags(s): return TAG_RE.sub("", s)
def norm(s): return re.sub(r"\s+", " ", s).strip()

P("UMBRELLA chapter-03.md — %d lines" % len(raw_lines))
P("=" * 90)

# ---- 1. meta markers ----
P("--- META / AUTHOR-VOICE MARKERS ---")
markers = [
    (r"^\s*Let me\b", "Let me..."),
    (r"^Here is the\b", "Here is the..."),
    (r"\bHere is the correction\b", "Here is the correction"),
    (r"\bCorrected\b", "Corrected"),
    (r"\bVersion A\b|\bVersion B\b", "Version A/B"),
    (r"\bThe Montage\b|\bMontage,?\s*Corrected\b", "Montage"),
    (r"\bLore Confirmed\b", "Lore Confirmed"),
    (r"\bRewrite[ds]?\b", "Rewrite"),
    (r"\bI need to\b|\bI want to\b|\bI'll now\b|\bLet's\b\s*rewrite", "author-voice planning"),
    (r"\bcraft note\b|\bauthor'?s? note\b", "craft/author note"),
    (r"\bshould be grounded\b|\bIt also fits\b", "craft analysis"),
    (r"\btake [AB]\b|\bTake [AB]\b", "take A/B"),
    (r"\boption [AB]\b|\bOption [AB]\b", "option A/B"),
    (r"\b\(note\b|\bNote:\b|\bNOTE\b", "note:"),
    (r"\bTODO\b|\bFIXME\b|\bTBD\b", "TODO/FIXME/TBD"),
]
for i, raw in enumerate(raw_lines, 1):
    t = strip_tags(raw).strip()
    if not t:
        continue
    for pat, label in markers:
        if re.search(pat, t, re.I):
            P("L%-5d [%s] %s" % (i, label, t[:160]))
            break

# ---- 2. bold headings inventory ----
P("")
P("--- BOLD HEADINGS (all '**...**' lines) ---")
heads = collections.defaultdict(list)
for i, raw in enumerate(raw_lines, 1):
    t = raw.strip()
    if t.startswith("**") and t.endswith("**") and len(t) > 4:
        heads[t].append(i)
for h, ls in sorted(heads.items(), key=lambda kv: kv[1][0]):
    dup = "  <<DUPLICATE x%d>>" % len(ls) if len(ls) > 1 else ""
    P("L%s %s%s" % (",".join(map(str, ls)), h[:120], dup))

# ---- 3. H1/H2/H3 headings ----
P("")
P("--- MARKDOWN HEADINGS (# lines) ---")
for i, raw in enumerate(raw_lines, 1):
    if raw.startswith("#"):
        P("L%-5d %s" % (i, raw.strip()[:120]))

# ---- 4. duplicated paragraphs (normalized, len>=35) ----
P("")
P("--- DUPLICATE PARAGRAPHS (normalized, len>=35, >=2 occurrences) ---")
para_index = collections.defaultdict(list)
buf = []; start = 1
def flush():
    global buf
    if buf:
        text = " ".join(norm(strip_tags(b)) for b in buf if norm(strip_tags(b)))
        if text:
            key = re.sub(r"\s+", " ", text.lower())
            para_index[key].append((start, text))
    buf = []
for i, raw in enumerate(raw_lines, 1):
    if raw.strip() == "":
        flush()
    else:
        if not buf: start = i
        buf.append(raw)
flush()
ndup = 0
for k, v in sorted(para_index.items(), key=lambda kv: kv[1][0][0]):
    if len(v) >= 2 and len(k) >= 35:
        ndup += 1
        P("x%d @ L%s :: %s" % (len(v), ",".join(str(a) for a, _ in v), v[0][1][:200]))
P("TOTAL duplicated paragraph groups: %d" % ndup)

# ---- 5. duplicated sentences (len>=35) ----
P("")
P("--- DUPLICATE SENTENCES (normalized, len>=35, >=2 occurrences) ---")
sent_index = collections.defaultdict(list)
for (start, text) in sum(([(s, t) for s, t in v] for v in para_index.values()), []):
    pass
sent_para = []
buf2 = []
def flush2(i):
    global buf2
    if buf2:
        text = " ".join(norm(strip_tags(b)) for b in buf2 if norm(strip_tags(b)))
        if text: sent_para.append((i, text))
    buf2 = []
for i, raw in enumerate(raw_lines, 1):
    if raw.strip() == "": flush2(i)
    else: buf2.append(raw)
flush2(len(raw_lines)+1)
for (ln, text) in sent_para:
    for s in re.split(r"(?<=[.!?])\s+", text):
        s2 = norm(s)
        if len(s2) >= 35:
            sent_index[re.sub(r"\s+", " ", s2.lower())].append(ln)
nsent = 0
for k, v in sorted(sent_index.items(), key=lambda kv: kv[1][0]):
    if len(v) >= 2:
        nsent += 1
        if nsent <= 120:
            P("x%d @ L%s :: %s" % (len(v), ",".join(map(str, v)), k[:180]))
P("TOTAL duplicated sentence groups: %d" % nsent)

out.close()
print("done; groups written to arc3_umbrella_scan.txt")
