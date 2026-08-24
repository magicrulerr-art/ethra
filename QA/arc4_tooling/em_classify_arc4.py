# -*- coding: utf-8 -*-
"""Arc IV em-dash classifier — adapted from QA/em_classify.py.
Classifies the LAST dash on each odd-count line: CUT / TAIL / OPEN-MID."""
import re, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CH = os.path.join(BASE, "content", "story", "chapters") + os.sep
files = ["chapter-arc4-%02d.md" % c for c in range(1, 7)]
EM = "\u2014"; Q = '"'
for f in files:
    lines = open(CH + f, encoding="utf-8").read().split("\n")
    print("=" * 70); print(f)
    for ln, l in enumerate(lines, 1):
        t = re.sub(r"<[^>]+>", "", l)
        n = t.count(EM)
        if n % 2 == 0:
            continue
        if re.search(Q + EM + r"\s*$|" + EM + Q, t):
            cat = "CUT(speech)"
        else:
            idx = t.rfind(EM)
            after = t[idx+1:].strip()
            if re.search(r"[.!?]\s+\S", after):
                cat = "OPEN-MID(suspect)"
            elif len(after) == 0:
                cat = "TAIL(empty)"
            else:
                cat = "TAIL(elab)"
        print("  L%-4d [%-16s] %s" % (ln, cat, t.strip()[:120]))
