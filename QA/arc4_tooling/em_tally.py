# -*- coding: utf-8 -*-
"""Tally em_classify_arc4.txt categories per file."""
import collections, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "em_classify_arc4.txt")
d = open(p, encoding="utf-8").read().split("\n")
f = ""
tot = collections.Counter()
per = collections.defaultdict(collections.Counter)
for l in d:
    if l.startswith("=" * 10):
        continue
    if l.strip() and not l.startswith("  "):
        f = l.strip()
        continue
    if l.startswith("  L"):
        cat = l.split("[")[1].split("]")[0]
        tot[cat] += 1
        per[f][cat] += 1
print("TOTAL:", dict(tot))
for k in per:
    print(k, dict(per[k]))
