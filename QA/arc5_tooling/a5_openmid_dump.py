# -*- coding: utf-8 -*-
"""Dump all OPEN-MID(suspect) lines with full text for manual review. Read-only."""
import io, os, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a5_openmid_review.txt")
files = ["chapter-arc5-%02d.md" % c for c in range(1, 23)]
EM = "\u2014"; Q = '"'
out = open(OUT, "w", encoding="utf-8")
n = 0
for f in files:
    lines = open(os.path.join(CH, f), encoding="utf-8").read().split("\n")
    for ln, l in enumerate(lines, 1):
        t = re.sub(r"<[^>]+>", "", l)
        if t.count(EM) % 2 == 0:
            continue
        if re.search(Q + EM + r"\s*$|" + EM + Q, t):
            continue
        idx = t.rfind(EM)
        after = t[idx + 1:].strip()
        if re.search(r"[.!?]\s+\S", after):
            n += 1
            seg_before = t[max(0, idx - 70):idx]
            out.write("%s L%d\n  BEFORE: ...%s\n  DASH>%s\n\n" % (f, ln, seg_before, after[:230]))
out.close()
print("OPEN-MID lines dumped:", n)
