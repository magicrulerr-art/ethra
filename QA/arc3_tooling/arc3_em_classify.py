import re, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters") + os.sep
files = ["chapter-arc3-%02d.md" % c for c in range(1, 6)]
EM = "\u2014"; Q = '"'
# Canon (ratified D1): speech cutoff; paired parenthetical; single dash introducing an
# elaboration that runs to sentence end. Any other dash = defect.
# Odd-count lines: classify the LAST (unpaired) dash:
#  - CUT: dash directly before closing quote (legit speech cutoff)
#  - TAIL: dash introduces elaboration running to end of line (legit single dash)
#  - OPEN-MID: dash mid-clause with significant text continuing past next sentence stop
#    (suspect unclosed parenthetical)
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
