import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
files = ["chapter-arc%d-%02d.md" % (a, c) for a in (1, 2) for c in range(1, 7)]
out = open("ethra_site/QA/quote_pair_check.txt", "w", encoding="utf-8")
def p(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")
TAG = re.compile(r"<[^>]+>")
MIDWORD = re.compile(r"([A-Za-z])'([A-Za-z])")
for f in files:
    lines = open("ethra_site/content/story/chapters/" + f, encoding="utf-8").read().split("\n")
    p("=" * 78); p(f)
    # 1) double-quote walk across the whole file
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
    # 2) single quotes with possessive/contraction mid-word apostrophes removed
    for ln, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        t2 = MIDWORD.sub(r"\1?\2", t)  # neutralize mid-word apostrophes (L'vat, isn't, father's)
        n = t2.count("'")
        if n % 2 == 1:
            p("  SQ-ODD(%d) L%d: %s" % (n, ln, t.strip()[:150]))
    # 3) asterisk balance (thought blocks) — per line odd count, and cross-line walk
    ast_open = False; ast_ln = 0
    for ln, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        n = t.count("*")
        for _ in range(n):
            ast_open = not ast_open
        if n % 2 == 1 and not ast_open and False:
            pass
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
