# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
lines = open("a5_pass2.txt", encoding="utf-8").read().split("\n")
f = None; sec = None; buf = []
for l in lines:
    if l.startswith("FILE:"):
        f = l.split()[1]
    elif l.startswith("--- "):
        sec = l
    elif sec and "CAPITALIZED CONTEXTS" in sec and l.startswith("L"):
        buf.append("%-24s %s" % (f, l))
print(len(buf), "capitalized 'King' hits:")
print("\n".join(buf))
# also lowercase king-before-name check section
f = None; sec = None; buf2 = []
for l in lines:
    if l.startswith("FILE:"):
        f = l.split()[1]
    elif l.startswith("--- "):
        sec = l
    elif sec and "lowercase-before-name" in sec and l.startswith("L"):
        buf2.append("%-24s %s" % (f, l))
print()
print(len(buf2), "lowercase 'king <Name>' hits:")
print("\n".join(buf2))
