# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
lines = open("a5_pass2.txt", encoding="utf-8").read().split("\n")
f = None; sec = None
for l in lines:
    if l.startswith("FILE:"):
        f = l.split()[1]; sec = None
    elif l.startswith("--- "):
        sec = l.strip("- ").strip()
    elif sec == "TYPO SWEEP" and l.startswith("L"):
        print("%-24s %s" % (f, l))
