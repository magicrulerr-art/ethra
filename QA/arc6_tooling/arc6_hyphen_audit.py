#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arc VI — ASCII hyphen audit v2: tally unique word-word compounds + special roles. Read-only."""
import re, io, sys, os, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CH = os.path.join(BASE, "content", "story", "chapters")
files = ["chapter-arc6-%02d.md" % c for c in range(1, 6)]
out = open(os.path.join(TOOL_DIR, "arc6_hyphen_audit.txt"), "w", encoding="utf-8")
def p(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")
TAG = re.compile(r"<[^>]+>")
compounds = collections.Counter()
comp_locs = collections.defaultdict(list)
spaced = []
trailing = []
dash_role = []  # hyphen between independent words (sentence-level, em-dash role)
for f in files:
    lines = open(os.path.join(CH, f), encoding="utf-8").read().split("\n")
    for ln, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        if "-" not in t:
            continue
        for m in re.finditer(r"-", t):
            a = m.start(); b = m.end()
            before = t[:a]; after = t[b:]
            if before.endswith(" ") or after.startswith(" "):
                spaced.append((f, ln, t[max(0,a-40):b+40].strip()))
                continue
            mb = re.search(r"([A-Za-z']+)$", before)
            ma = re.match(r"([A-Za-z']+)", after)
            if mb and ma:
                comp = (mb.group(1) + "-" + ma.group(1)).lower()
                compounds[comp] += 1
                if len(comp_locs[comp]) < 3:
                    comp_locs[comp].append("%s L%d" % (f, ln))
            elif mb and not ma:
                trailing.append((f, ln, t[max(0,a-60):a]))
p("=== SPACED HYPHENS (space before/after '-') ===")
for f, ln, ctx in spaced:
    p("  %s L%-4d %s" % (f, ln, ctx[:130]))
p("\n=== TRAILING HYPHENS (word ends with '-' and line/segment ends) ===")
for f, ln, ctx in trailing:
    p("  %s L%-4d ...%s-" % (f, ln, ctx))
p("\n=== UNIQUE word-word COMPOUNDS (count x locations) ===")
for comp, n in sorted(compounds.items(), key=lambda kv: (-kv[1], kv[0])):
    p("  x%-3d %-28s %s" % (n, comp, ", ".join(comp_locs[comp])))
out.close()
print("written")
