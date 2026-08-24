# -*- coding: utf-8 -*-
"""Locate specific meta/debris strings in the umbrella chapter-04.md."""
import io, sys, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UMB = os.path.join(BASE, "content", "story", "chapter-04.md")
pats = [
    "You can start wherever you see fit",
    "lets start then",
    "continue the vignettes",
    "are we ready to continue",
    "emotional engine",
    "reveals a deep understanding of character voice",
    "In Chapter Three",
    "retroactively establish her",
    "revised backstory is grounded",
    "The Fire Beetles fill a crucial gap",
    "evolutionary arms race you have described",
    "walking exposition",
    "audience surrogate",
    "Kira has been carrying that bag",
    "Kira's outburst is not merely disappointment",
    "will be the most telling moment",
    "I have only one small note",
    "Here.s how that could play",
    "Let me rewrite",
    "Version A",
    "Version B",
    "Underground Training Halls",
    "The Cosmic Structure of Ethra",
    "The Chapter.s Cadence",
    "What This Reveals About the Speaker",
    "performing competence",
    "let us see her in class with tutors",
    "feedback?",
]
D = open(UMB, encoding="utf-8").read().split("\n")
for p in pats:
    hits = [i + 1 for i, l in enumerate(D) if re.search(p, l)]
    print("%-52s %s" % (p, hits if hits else "NONE"))
