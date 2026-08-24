#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crossed * / ' delimiter detection — Arc V (adapted from QA/delimiter_cross_check.py).
Read-only. Output: QA/arc5_tooling/a5_cross.txt"""
import re, io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a5_cross.txt")
files = ["chapter-arc5-%02d.md" % c for c in range(1, 23)]
out = open(OUT, "w", encoding="utf-8")
def p(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")
TAG = re.compile(r"<[^>]+>")
MIDWORD = re.compile(r"([A-Za-z])'([A-Za-z])")
total = 0
for f in files:
    lines = open(os.path.join(CH, f), encoding="utf-8").read().split("\n")
    hits = []
    for ln, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        if "*" not in t and "'" not in t:
            continue
        t2 = MIDWORD.sub(lambda m: m.group(1) + "\x00" + m.group(2), t)
        stack = []
        crossed = False
        for ch in t2:
            if ch in "*'":
                if stack and stack[-1] == ch:
                    stack.pop()
                elif stack and stack[-1] != ch:
                    crossed = True
                    stack.pop()
                else:
                    stack.append(ch)
        if crossed or stack:
            hits.append((ln, "CROSSED" if crossed else ("OPEN(%s)" % "".join(stack)), t.strip()))
    p("=" * 78); p(f)
    if not hits:
        p("  clean")
    for ln, kind, txt in hits:
        total += 1
        p("  L%-4d [%s] %s" % (ln, kind, txt[:220]))
p("=" * 78)
p("TOTAL flagged lines: %d" % total)
out.close()
