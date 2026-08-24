import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
files = ["chapter-arc%d-%02d.md" % (a, c) for a in (1, 2) for c in range(1, 7)]
EM = "\u2014"; Q = '"'
# For each line with odd em count and not a speech-cut, classify the LAST (unpaired) dash:
#  - CUT: dash directly before closing quote  (legit)
#  - TAIL: dash introduces elaboration running to end of line/sentence (usually legit single dash)
#  - OPEN-MID: dash in middle of clause with significant text after it AND before the sentence's next
#    strong stop — i.e., looks like an opened-but-unclosed parenthetical
for f in files:
    lines = open("ethra_site/content/story/chapters/" + f, encoding="utf-8").read().split("\n")
    print("=" * 70); print(f)
    for ln, l in enumerate(lines, 1):
        t = re.sub(r"<[^>]+>", "", l)
        n = t.count(EM)
        if n % 2 == 0:
            continue
        if re.search(Q + EM + r"\s*$|" + EM + Q, t):
            cat = "CUT(speech)"
        else:
            # find last dash position; how much non-space text follows it?
            idx = t.rfind(EM)
            after = t[idx+1:].strip()
            before = t[:idx].strip()
            # if after-text contains a sentence-ending period before the line end, suspect
            if re.search(r"[.!?]\s+\S", after):
                cat = "OPEN-MID(suspect)"
            elif len(after) == 0:
                cat = "TAIL(empty)"
            else:
                cat = "TAIL(elab)"
        print("  L%-4d [%-16s] %s" % (ln, cat, t.strip()[:120]))
