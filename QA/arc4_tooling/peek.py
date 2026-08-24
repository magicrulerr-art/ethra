# -*- coding: utf-8 -*-
"""peek.py FILE START END [START END ...] — print exact lines (read-only)."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
path = sys.argv[1]
d = open(path, encoding="utf-8").read().split("\n")
args = sys.argv[2:]
pairs = [(int(args[i]), int(args[i+1])) for i in range(0, len(args), 2)]
for a, b in pairs:
    print("--- %s L%d-%d ---" % (path, a, b))
    for i in range(a-1, min(b, len(d))):
        print("%5d| %s" % (i+1, d[i][:260]))
