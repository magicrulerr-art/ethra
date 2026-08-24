# -*- coding: utf-8 -*-
"""Find the extra 'Humman' in splits vs umbrella."""
import io, sys, re, os, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters")
UMB = os.path.join(BASE, "content", "story", "chapter-04.md")
split_lines = []
for c in range(1, 7):
    p = os.path.join(CH, "chapter-arc4-%02d.md" % c)
    for i, l in enumerate(open(p, encoding="utf-8").read().split("\n"), 1):
        split_lines.append(l)
umb_lines = open(UMB, encoding="utf-8").read().split("\n")
print("split total lines:", len(split_lines), "umbrella lines:", len(umb_lines))
# find Humman-bearing lines in splits that have no counterpart in umbrella
umb_set = collections.Counter(l.strip() for l in umb_lines if "Humman" in l)
for idx, l in enumerate(split_lines, 1):
    if "Humman" in l:
        key = l.strip()
        if umb_set.get(key, 0) == 0:
            print("UNMATCHED split line %d: %s" % (idx, l[:160]))
        else:
            umb_set[key] -= 1
