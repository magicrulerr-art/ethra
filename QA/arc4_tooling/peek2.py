# -*- coding: utf-8 -*-
"""peek2.py FILE START END [W] — compact line view, W chars wide (default 100)."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
path = sys.argv[1]; a = int(sys.argv[2]); b = int(sys.argv[3])
w = int(sys.argv[4]) if len(sys.argv) > 4 else 100
d = open(path, encoding="utf-8").read().split("\n")
for i in range(a-1, min(b, len(d))):
    print("%5d| %s" % (i+1, d[i][:w]))
