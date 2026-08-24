# -*- coding: utf-8 -*-
"""Arc IV quote-pair walker — adapted from QA/quote_pair_check.py."""
import re, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CH = os.path.join(BASE, "content", "story", "chapters") + os.sep
files = ["chapter-arc4-%02d.md" % c for c in range(1, 7)]
out = open(os.path.join(TOOL_DIR, "quote_pair_check_arc4.txt"), "w", encoding="utf-8")
def p(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")
TAG = re.compile(r"<[^>]+>")
MIDWORD = re.compile(r"([A-Za-z])'([A-Za-z])")
for f in files:
    lines = open(CH + f, encoding="utf-8").read().split("\n")
    p("=" * 78); p(f)
    open_state = False; open_ln = 0
    for ln, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        for ch in t:
            if ch == '"':
                if not open_state:
                    open_state = True; open_ln = ln
                else:
                    open_state = False
        if open_state and l.strip() == "":
            p("  DQ-OPEN-ACROSS-BLANK: opened L%d still open at blank L%d" % (open_ln, ln))
    if open_state:
        p("  DQ-UNBALANCED-AT-EOF: opened L%d" % open_ln)
    else:
        p("  DQ: balanced across whole file")
    for ln, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        t2 = MIDWORD.sub(r"\1?\2", t)
        n = t2.count("'")
        if n % 2 == 1:
            p("  SQ-ODD(%d) L%d: %s" % (n, ln, t.strip()[:150]))
    ast_open = False; ast_ln = 0
    for ln, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        n = t.count("*")
        for _ in range(n):
            ast_open = not ast_open
        if ast_open and l.strip() == "":
            p("  AST-OPEN-ACROSS-BLANK: opened L%d still open at blank L%d" % (ast_ln, ln))
        if n % 2 == 1:
            if ast_ln == 0 or not ast_open:
                ast_ln = ln
            p("  AST-ODD L%d (state now %s): %s" % (ln, "OPEN" if ast_open else "closed", t.strip()[:150]))
    if ast_open:
        p("  AST-UNBALANCED-AT-EOF: opened L%d" % ast_ln)
    else:
        p("  AST: balanced across whole file")
out.close()
