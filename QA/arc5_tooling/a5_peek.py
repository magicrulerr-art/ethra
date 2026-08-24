# -*- coding: utf-8 -*-
"""Head/tail peek of all 22 arc5 split files (boundary pre-inspection). Read-only."""
import io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # ethra_site
CH = os.path.join(BASE, "content", "story", "chapters")
out = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "a5_peek.txt"), "w", encoding="utf-8")
def P(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")
for c in range(1, 23):
    f = "chapter-arc5-%02d.md" % c
    lines = open(os.path.join(CH, f), encoding="utf-8").read().split("\n")
    P("=" * 90)
    P("%s  (%d lines)" % (f, len(lines)))
    P("--- HEAD (first 6 non-empty-ish) ---")
    for i, l in enumerate(lines[:8], 1):
        P("  L%-4d %s" % (i, repr(l[:170])))
    P("--- TAIL (last 5) ---")
    for i, l in enumerate(lines[-5:], len(lines) - 4):
        P("  L%-4d %s" % (i, repr(l[:170])))
out.close()
print("done")
