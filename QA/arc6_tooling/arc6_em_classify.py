#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arc VI — em-dash census + CUT/TAIL/OPEN-MID classification (adapted from QA/em_census.py + QA/em_classify.py). Read-only."""
import re, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CH = os.path.join(BASE, "content", "story", "chapters")
files = ["chapter-arc6-%02d.md" % c for c in range(1, 6)]
EM = "\u2014"; Q = '"'
out = open(os.path.join(TOOL_DIR, "arc6_em_classify.txt"), "w", encoding="utf-8")
def p(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")
tot = inter = odd = oddres = 0
cats_all = []
for f in files:
    lines = open(os.path.join(CH, f), encoding="utf-8").read().split("\n")
    fe = fi = fo = fr = 0
    p("=" * 70); p(f)
    for ln, l in enumerate(lines, 1):
        t = re.sub(r"<[^>]+>", "", l)
        n = t.count(EM)
        fe += n
        fi += len(re.findall(Q + EM + "|" + EM + Q, t))
        if n % 2 == 1:
            fo += 1
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
            if cat != "CUT(speech)":
                fr += 1
            cats_all.append((f, ln, cat))
            p("  L%-4d [%-16s] %s" % (ln, cat, t.strip()[:120]))
    p("  SUBTOTAL: em_total=%d quote_adjacent=%d odd_lines=%d non_cut=%d" % (fe, fi, fo, fr))
    tot += fe; inter += fi; odd += fo; oddres += fr
p("=" * 70)
p("TOTAL: em=%d quote_adjacent=%d odd_lines=%d non_cut=%d" % (tot, inter, odd, oddres))
import collections
p("BY CATEGORY:", dict(collections.Counter(c for _, _, c in cats_all)))
out.close()
