# -*- coding: utf-8 -*-
"""Spot-read exact lines from arc5 splits for verification. Read-only."""
import io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters")
REQ = {
    "chapter-arc5-02.md": [11, 29],
    "chapter-arc5-05.md": [19],
    "chapter-arc5-06.md": [135, 136, 137, 161, 162, 163, 190],
    "chapter-arc5-07.md": list(range(60, 73)),
    "chapter-arc5-09.md": [3, 4, 5],
    "chapter-arc5-11.md": [25, 194, 218, 225, 226],
    "chapter-arc5-12.md": [43, 44, 45],
    "chapter-arc5-13.md": [29, 30, 31, 32, 33],
    "chapter-arc5-15.md": list(range(3, 14)) + [33, 34, 35],
    "chapter-arc5-16.md": list(range(60, 70)) + list(range(105, 112)),
    "chapter-arc5-18.md": list(range(3, 8)),
    "chapter-arc5-19.md": list(range(3, 8)) + [40, 41, 42, 43, 78, 79, 80],
    "chapter-arc5-22.md": list(range(3, 8)),
}
for fname in sorted(REQ):
    lines = open(os.path.join(CH, fname), encoding="utf-8").read().split("\n")
    print("=" * 100)
    print(fname)
    for ln in REQ[fname]:
        if 1 <= ln <= len(lines):
            print("L%-4d| %s" % (ln, lines[ln - 1]))
