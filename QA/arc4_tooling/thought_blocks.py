# -*- coding: utf-8 -*-
"""Thought-block inventory: asterisk thoughts vs single-quote thoughts."""
import io, sys, re, glob, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p in sorted(glob.glob(os.path.join(BASE, "content", "story", "chapters", "chapter-arc4-*.md"))):
    D = open(p, encoding="utf-8").read().split("\n")
    tb = []
    for i, l in enumerate(D, 1):
        if "thought-block" in l:
            star = "*" in l
            sq = "'" in l
            tb.append((i, star, sq))
    print(os.path.basename(p), "thought-blocks:", len(tb))
    for i, star, sq in tb:
        print("   L%d asterisk=%s singlequote=%s" % (i, star, sq))
