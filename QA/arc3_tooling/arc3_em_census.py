import re, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters") + os.sep
files = ["chapter-arc3-%02d.md" % c for c in range(1, 6)]
EM = "\u2014"; Q = '"'
tot = inter = odd = oddres = 0
for f in files:
    lines = open(CH + f, encoding="utf-8").read().split("\n")
    fe = fi = fo = fr = 0
    for l in lines:
        t = re.sub(r"<[^>]+>", "", l)
        n = t.count(EM)
        fe += n
        fi += len(re.findall(Q + EM + "|" + EM + Q, t))
        if n % 2 == 1:
            fo += 1
            if not re.search(Q + EM + r"\s*$|" + EM + Q, t):
                fr += 1
    print("%s: em_total=%d quote_adjacent=%d odd_lines=%d odd_non_speech=%d" % (f, fe, fi, fo, fr))
    tot += fe; inter += fi; odd += fo; oddres += fr
print("TOTAL: em=%d quote_adjacent=%d odd_lines=%d odd_non_speech=%d" % (tot, inter, odd, oddres))
