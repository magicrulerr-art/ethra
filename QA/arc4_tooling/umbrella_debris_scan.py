# -*- coding: utf-8 -*-
"""Arc IV umbrella draft-debris scanner (chapter-04.md, 3,668 lines).
Grep-style scans ONLY; writes QA/arc4_tooling/umbrella_debris.txt. Read-only.
Scans: meta markers, Version A/B, Corrected, Montage, pass1/2/3 markers,
author planning prose, heading inventory, duplicated headings, duplicated
paragraph blocks (normalized whitespace, >=35 chars)."""
import re, os, collections

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
UMB = os.path.join(BASE, "content", "story", "chapter-04.md")
lines = open(UMB, encoding="utf-8").read().split("\n")

out = open(os.path.join(TOOL_DIR, "umbrella_debris.txt"), "w", encoding="utf-8")
def P(*a): out.write(" ".join(str(x) for x in a) + "\n")

P("UMBRELLA:", UMB); P("LINES:", len(lines)); P("=" * 90)

# ---- 1. meta / author-voice markers ----
P("--- META / AUTHOR-VOICE MARKERS ---")
markers = [
    (r"^\s*Let me\b", "let-me"),
    (r"\bHere is the correction\b", "here-is-correction"),
    (r"\bHere is the corrected\b", "here-is-corrected"),
    (r"\bI'll rewrite\b", "ill-rewrite"),
    (r"\bLet me rewrite\b", "let-me-rewrite"),
    (r"\bLet me narrate\b", "let-me-narrate"),
    (r"\bVersion A\b", "version-a"),
    (r"\bVersion B\b", "version-b"),
    (r"\bMontage\b", "montage"),
    (r"\bCorrected\b", "corrected"),
    (r"\bcorrection\b", "correction-word"),
    (r"\bpass\s*[123]\b", "pass-marker"),
    (r"\bPASS\s*[123]\b", "pass-marker-cap"),
    (r"\bshould be grounded\b", "craft-note-grounded"),
    (r"\bperfectly calibrated\b", "craft-calibrated"),
    (r"\bIt also fits the\b", "craft-also-fits"),
    (r"\bcraft note\b", "craft-note"),
    (r"\bI think this\b", "author-think"),
    (r"\bLet's keep\b", "lets-keep"),
    (r"\bLet me check\b", "let-me-check"),
    (r"\bNow,? let\b", "now-let"),
]
seen = set()
for i, l in enumerate(lines, 1):
    for rx, label in markers:
        if re.search(rx, l, re.I):
            if i not in seen:
                P("L%-5d [%s] %s" % (i, label, l.strip()[:150]))
                seen.add(i)

# ---- 2. heading inventory (markdown # lines and standalone bold lines) ----
P(); P("--- HEADING INVENTORY (markdown # and bold-only lines) ---")
head_locs = collections.defaultdict(list)
for i, l in enumerate(lines, 1):
    s = l.strip()
    if re.match(r"^#{1,6}\s", s):
        P("L%-5d [md] %s" % (i, s[:120]))
        head_locs[s.lower()].append(i)
    elif re.match(r"^\*\*[^*]+\*\*\s*$", s):
        P("L%-5d [bold] %s" % (i, s[:120]))
        head_locs[s.lower()].append(i)

P(); P("--- DUPLICATED HEADINGS ---")
dups = {k: v for k, v in head_locs.items() if len(v) >= 2}
if not dups:
    P("none")
for k, v in sorted(dups.items()):
    P("x%d lines %s :: %s" % (len(v), v, k[:120]))

# ---- 3. duplicated paragraph blocks ----
P(); P("--- DUPLICATED PARAGRAPH BLOCKS (>=35 chars, normalized) ---")
para_index = collections.defaultdict(list)
para_start = None
buf = []
def flush(end_line):
    global buf, para_start
    if buf:
        text = " ".join(re.sub(r"\s+", " ", b).strip() for b in buf)
        text = text.strip()
        if len(text) >= 35:
            key = re.sub(r"\s+", " ", text.lower())
            para_index[key].append((para_start, end_line - 1, text))
        buf = []
for i, l in enumerate(lines, 1):
    if l.strip() == "":
        flush(i)
        para_start = None
    else:
        if para_start is None:
            para_start = i
        buf.append(l.strip())
flush(len(lines) + 1)
anydup = False
for k, v in sorted(para_index.items(), key=lambda kv: -len(kv[1])):
    if len(v) >= 2:
        anydup = True
        P("x%d @ %s" % (len(v), "; ".join("L%d-%d" % (a, b) for a, b, _ in v)))
        P("      %s" % v[0][2][:220])
if not anydup:
    P("none")

# ---- 4. duplicated long sentences (cross-paragraph) ----
P(); P("--- DUPLICATED SENTENCES (>=45 chars) ---")
sent_index = collections.defaultdict(list)
for i, l in enumerate(lines, 1):
    for s in re.split(r"(?<=[.!?])\s+", re.sub(r"<[^>]+>", "", l)):
        s2 = re.sub(r"\s+", " ", s).strip()
        if len(s2) >= 45:
            sent_index[re.sub(r"\s+", " ", s2.lower())].append(i)
anyd = False
for k, v in sorted(sent_index.items(), key=lambda kv: -len(kv[1])):
    if len(v) >= 2 and len(set(v)) >= 2:
        anyd = True
        P("x%d lines %s :: %s" % (len(v), sorted(set(v)), k[:180]))
if not anyd:
    P("none")

# ---- 5. stray structural anomalies: consecutive identical lines, HTML comment blocks ----
P(); P("--- HTML COMMENTS / STRAY TAGS ---")
for i, l in enumerate(lines, 1):
    if "<!--" in l or "-->" in l:
        P("L%-5d [comment] %s" % (i, l.strip()[:150]))

out.close()
print("done")
