# -*- coding: utf-8 -*-
import io, json, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
d = json.load(open("a5_lint_results.json", encoding="utf-8"))
bad = []
tot = 0
for f, r in d["per_file"].items():
    for ln, ctx in r["king_hits"]:
        tot += 1
        for m in re.finditer(r"\bking\b", ctx):
            pre = ctx[max(0, m.start() - 16):m.start()]
            if not re.search(r"(the|a|an|my|his|her|their|our|your|this|that|one|no|some|every|any)\s*$", pre, re.I):
                bad.append((f, ln, pre + "[king]" + ctx[m.end():m.end() + 24]))
print("total king/King hit-lines:", tot)
print("suspicious lowercase 'king' lacking obvious determiner:", len(bad))
for b in bad:
    print(b[0], "L%d" % b[1], repr(b[2]))
