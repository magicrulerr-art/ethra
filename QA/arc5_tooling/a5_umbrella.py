#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Umbrella chapter-05.md draft-debris scanner (NEW). Read-only.
Grep-style marker scan + heading inventory + duplicate paragraph sweep +
split-anchor context. Output: QA/arc5_tooling/a5_umbrella.txt"""
import re, io, os, json, sys, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STORY = os.path.join(BASE, "content", "story")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a5_umbrella.txt")
out = open(OUT, "w", encoding="utf-8")
def P(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")

content = open(os.path.join(STORY, "chapter-05.md"), encoding="utf-8").read()
lines = content.split("\n")
P("UMBRELLA: content/story/chapter-05.md  (%d bytes, %d lines)" % (len(content.encode('utf-8')), len(lines)))

arcs = json.load(open(os.path.join(STORY, "arcs.json"), encoding="utf-8"))["arcs"]
anchors = arcs["5"]["split_anchors"]
anchor_set = set(anchors)
def split_of(ln):
    # which split chapter does umbrella line ln fall into
    idx = 0
    for a in anchors:
        if ln >= a:
            idx += 1
        else:
            break
    return idx + 1

P("\n=== 1. HEADING INVENTORY (all # lines) ===")
for i, l in enumerate(lines, 1):
    if re.match(r"^#{1,6}\s", l):
        P("L%-5d [ch%02d] %s" % (i, split_of(i), l.strip()[:140]))

P("\n=== 2. BOLD SCAFFOLD LINES (**...** alone on line) ===")
for i, l in enumerate(lines, 1):
    if re.match(r"^\s*\*\*[^*]+\*\*\s*$", l):
        P("L%-5d [ch%02d] %s" % (i, split_of(i), l.strip()[:140]))

P("\n=== 3. META / AUTHOR-VOICE MARKERS ===")
markers = [
    ("let_me", r"^\s*Let me\b", re.I),
    ("here_is_the", r"\bHere is the\b", re.I),
    ("version_ab", r"\bVersion [AB12]\b", 0),
    ("corrected", r"\bcorrect(?:ed|ion)\b", re.I),
    ("montage", r"\bmontage\b", re.I),
    ("rewrite", r"\brewrit\w+\b", re.I),
    ("draft", r"\bdraft\b", re.I),
    ("take2", r"\b(?:second|2nd) take\b|\btake [AB2]\b", re.I),
    ("i_need_to", r"^\s*I need to\b", 0),
    ("okay_wait", r"^\s*(Okay|Wait|Hmm|Actually|No,)\b", 0),
    ("scaffold_ts", r"^\s*\*\*\d{2}:\d{2}\b", 0),
    ("note_to_self", r"\bnote to self\b|\bauthor'?s note\b", re.I),
    ("scene:", r"^\s*Scene\s*[:\d]", re.I),
]
for i, l in enumerate(lines, 1):
    for label, pat, fl in markers:
        if re.search(pat, l, fl):
            P("L%-5d [ch%02d] [%s] %s" % (i, split_of(i), label, l.strip()[:150]))
            break

P("\n=== 4. DRAFT-INSTRUCTION PROSE (present-tense stage direction suspects) ===")
for i, l in enumerate(lines, 1):
    t = re.sub(r"<[^>]+>", "", l)
    if re.search(r"\b(?:yells?|says|tores|chants?|visibily)\b", t, re.I) or re.search(r"!{3,}", t):
        P("L%-5d [ch%02d] %s" % (i, split_of(i), t.strip()[:170]))

P("\n=== 5. TIMESTAMP / FORMULAIC OPENERS (dup-scene-heading suspects) ===")
ts_open = collections.defaultdict(list)
for i, l in enumerate(lines, 1):
    t = l.strip()
    if re.match(r"^(It was|At) \d{1,2}:\d{2}\b", t):
        key = re.sub(r"\s+", " ", t.lower())[:80]
        ts_open[key].append(i)
for k, v in ts_open.items():
    if len(v) >= 2:
        P("x%d  %s  -> lines %s (chapters %s)" % (len(v), k[:70], v, [split_of(x) for x in v]))
P("(singletons omitted; %d distinct formulaic openers total)" % len(ts_open))

P("\n=== 6. DUPLICATE PARAGRAPHS (normalized, len>=35, >=2 occurrences) ===")
para_index = collections.defaultdict(list)
buf = []; start = 1
def flush(ln):
    global buf
    if buf:
        text = " ".join(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", b)).strip() for b in buf)
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) >= 35:
            para_index[text.lower()].append((start, text))
    buf = []
for i, l in enumerate(lines, 1):
    if l.strip() == "":
        flush(i)
    else:
        if not buf:
            start = i
        buf.append(l)
flush(len(lines) + 1)
ndup = 0
for k, v in sorted(para_index.items(), key=lambda kv: -len(kv[1])):
    if len(v) >= 2:
        ndup += 1
        P("x%d @ %s [chapters %s]" % (len(v), "; ".join("L%d" % a for a, _ in v), [split_of(a) for a, _ in v]))
        P("      %s" % v[0][1][:220])
P("(%d duplicated paragraph groups)" % ndup)

P("\n=== 7. SPLIT-ANCHOR CONTEXT (umbrella line at each anchor; chapter starts there) ===")
for j, a in enumerate(anchors, 2):
    ctx_before = lines[a - 2].strip()[:90] if a - 2 >= 0 else ""
    ctx_at = lines[a - 1].strip()[:90] if a - 1 < len(lines) else ""
    P("anchor L%-5d -> ch%02d start | prev line: %s" % (a, j, repr(ctx_before)))
    P("                  | anchor line: %s" % repr(ctx_at))
out.close()
print("done -> a5_umbrella.txt")
