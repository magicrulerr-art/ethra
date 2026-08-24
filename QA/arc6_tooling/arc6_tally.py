#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arc VI — final tally: hum variants + king/King contexts per chapter (adapted from QA/final_tally.py). Read-only."""
import re, io, sys, os, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CH = os.path.join(BASE, "content", "story", "chapters")
files = ["chapter-arc6-%02d.md" % c for c in range(1, 6)]
out = open(os.path.join(TOOL_DIR, "arc6_tally.txt"), "w", encoding="utf-8")
def p(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")

def txt_of(f):
    return re.sub(r"<[^>]+>", "", open(os.path.join(CH, f), encoding="utf-8").read())

p("### HUM VARIANTS PER CHAPTER (case-sensitive exact forms) ###")
grand = collections.Counter()
for f in files:
    c = collections.Counter(m.group(0) for m in re.finditer(r"\b[Hh]u+m+ans?\b", txt_of(f)))
    grand.update(c)
    p(f, dict(sorted(c.items())))
p("GRAND:", dict(sorted(grand.items())))

p("\n### KING/KING PER CHAPTER ###")
for f in files:
    t = txt_of(f)
    cap = len(re.findall(r"\bKing\b", t))
    low = len(re.findall(r"\bking\b", t))
    p(f, "King=%d king=%d" % (cap, low))

p("\n### 'King' CAPITALIZED CONTEXTS (all) ###")
for f in files:
    for ln, l in enumerate(open(os.path.join(CH, f), encoding="utf-8").read().split("\n"), 1):
        t = re.sub(r"<[^>]+>", "", l)
        for m in re.finditer(r"\bKing\b", t):
            a = max(0, m.start()-30); b = min(len(t), m.end()+30)
            p("%s L%-4d ...%s..." % (f, ln, t[a:b].replace("\n", " ")))

p("\n### lowercase 'king' before a Name (potential canon violations) ###")
for f in files:
    for ln, l in enumerate(open(os.path.join(CH, f), encoding="utf-8").read().split("\n"), 1):
        t = re.sub(r"<[^>]+>", "", l)
        for m in re.finditer(r"\bking [A-Z][a-z]+", t):
            p("%s L%-4d ...%s..." % (f, ln, t[max(0,m.start()-25):m.end()+25].replace("\n"," ")))

p("\n### capitalized 'King' with determiner (potential canon violations: 'the King', 'my King', 'a King', 'his King') ###")
for f in files:
    for ln, l in enumerate(open(os.path.join(CH, f), encoding="utf-8").read().split("\n"), 1):
        t = re.sub(r"<[^>]+>", "", l)
        for m in re.finditer(r"\b(the|my|a|an|his|her|their|our|your|this|that|old|young) King\b", t):
            p("%s L%-4d ...%s..." % (f, ln, t[max(0,m.start()-25):m.end()+35].replace("\n"," ")))
out.close()
print("written: arc6_tally.txt")
