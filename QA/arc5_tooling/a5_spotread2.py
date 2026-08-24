# -*- coding: utf-8 -*-
"""Spot-read ranges for duplicate-block canon designation. Read-only."""
import io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters")
REQ = [
    ("chapter-arc5-01.md", 70, 90), ("chapter-arc5-01.md", 140, 160),
    ("chapter-arc5-01.md", 225, 245), ("chapter-arc5-01.md", 275, 300),
    ("chapter-arc5-01.md", 355, 380),
    ("chapter-arc5-03.md", 45, 60), ("chapter-arc5-03.md", 85, 100),
    ("chapter-arc5-03.md", 118, 128),
    ("chapter-arc5-06.md", 125, 140), ("chapter-arc5-06.md", 155, 170),
    ("chapter-arc5-06.md", 178, 195),
    ("chapter-arc5-07.md", 55, 95),
    ("chapter-arc5-07.md", 55, 95),
    ("chapter-arc5-08.md", 1, 21),
    ("chapter-arc5-11.md", 158, 175), ("chapter-arc5-11.md", 199, 230),
    ("chapter-arc5-15.md", 14, 34), ("chapter-arc5-15.md", 36, 62),
    ("chapter-arc5-16.md", 25, 60), ("chapter-arc5-16.md", 66, 105),
    ("chapter-arc5-18.md", 45, 65), ("chapter-arc5-18.md", 80, 105),
    ("chapter-arc5-19.md", 36, 82),
]
cache = {}
for fname, a, b in REQ:
    if fname not in cache:
        cache[fname] = open(os.path.join(CH, fname), encoding="utf-8").read().split("\n")
    lines = cache[fname]
    print("=" * 100)
    print("%s  L%d-%d" % (fname, a, b))
    for ln in range(a, min(b, len(lines)) + 1):
        print("L%-4d| %s" % (ln, lines[ln - 1][:400]))
