# -*- coding: utf-8 -*-
"""List all markdown heading lines in umbrella + check sub-chapter heading variants."""
import io, sys, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UMB = os.path.join(BASE, "content", "story", "chapter-04.md")
D = open(UMB, encoding="utf-8").read().split("\n")
for i, l in enumerate(D, 1):
    if re.match(r"^#{1,6}\s", l) or re.search(r"\b(The Gifts|Aftermath|Bureaucracy|The Caravans|The Pyrinae Accord|The Humman Delegation)\b", l):
        print("%5d| %s" % (i, l[:130]))
