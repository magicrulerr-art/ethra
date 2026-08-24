#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Em-dash CUT/TAIL/OPEN-MID classification — Arc V (adapted from QA/em_classify.py).
Read-only. Output: QA/arc5_tooling/a5_em_classify.txt"""
import re, io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a5_em_classify.txt")
files = ["chapter-arc5-%02d.md" % c for c in range(1, 23)]
EM = "\u2014"; Q = '"'
out = open(OUT, "w", encoding="utf-8")
def P(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")
cats = {"CUT(speech)": 0, "TAIL(elab)": 0, "TAIL(empty)": 0, "OPEN-MID(suspect)": 0}
for f in files:
    lines = open(os.path.join(CH, f), encoding="utf-8").read().split("\n")
    P("=" * 70); P(f)
    for ln, l in enumerate(lines, 1):
        t = re.sub(r"<[^>]+>", "", l)
        n = t.count(EM)
        if n % 2 == 0:
            continue
        if re.search(Q + EM + r"\s*$|" + EM + Q, t):
            cat = "CUT(speech)"
        else:
            idx = t.rfind(EM)
            after = t[idx+1:].strip()
            if re.search(r"[.!?]\s+\S", after):
                cat = "OPEN-MID(suspect)"
            elif len(after) == 0:
                cat = "TAIL(empty)"
            else:
                cat = "TAIL(elab)"
        cats[cat] += 1
        P("  L%-4d [%-16s] %s" % (ln, cat, t.strip()[:130]))
P("=" * 70)
P("CATEGORY TOTALS:", cats)
out.close()
