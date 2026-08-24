# -*- coding: utf-8 -*-
"""Cross-reference check: is take A's 'sealed letter' beat referenced downstream?"""
import io, sys, re, os, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
files = sorted(glob.glob(os.path.join(BASE, "content", "story", "chapters", "chapter-arc4-0[3-6].md")))
files += [os.path.join(BASE, "content", "story", "chapter-04.md"),
          os.path.join(BASE, "content", "story", "chapter-05.md")]
for p in files:
    D = open(p, encoding="utf-8").read().split("\n")
    hits = [(i + 1, l.strip()[:110]) for i, l in enumerate(D)
            if re.search(r"sealed letter|sealed scroll|the letter", l, re.I)]
    print(os.path.basename(p), len(hits))
    for h in hits[:8]:
        print("   L%d %s" % h)
