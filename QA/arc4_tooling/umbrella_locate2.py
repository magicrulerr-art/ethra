# -*- coding: utf-8 -*-
"""Map key arc4-01/02 boundary strings to umbrella line numbers."""
import io, sys, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UMB = os.path.join(BASE, "content", "story", "chapter-04.md")
pats = [
    "Then the Shadow Paws will propos",
    "Here is a comprehensive summary",
    "Zara was the first to speak",
    "The Shadow Paws also accept",
    "She had been declined",
    "She will be ready",
    "The Chapter.s Cadence",
    "The Motted Paws . The Silent Halls",
    "Nefere entered the Great Hall",
    "The Hummans are honored by the king",
]
D = open(UMB, encoding="utf-8").read().split("\n")
for p in pats:
    hits = [i + 1 for i, l in enumerate(D) if re.search(p, l)]
    print("%-45s %s" % (p, hits if hits else "NONE"))
