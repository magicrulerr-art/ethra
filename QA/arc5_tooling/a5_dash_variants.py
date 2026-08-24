# -*- coding: utf-8 -*-
import io, json, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
d = json.load(open("a5_lint_results.json", encoding="utf-8"))
tot = {"em": 0, "en": 0, "hbar": 0}
for f, r in d["per_file"].items():
    tot["em"] += r["em_dash_total"]; tot["en"] += r["en_dash_total"]; tot["hbar"] += r["hbar_total"]
    if r["en_dash_total"] or r["hbar_total"] or r["hyphen_dialogue_lines"]:
        print(f, "en=%d hbar=%d hyphenStart=%d" % (r["en_dash_total"], r["hbar_total"], len(r["hyphen_dialogue_lines"])))
        for ln, ctx in r["hyphen_dialogue_lines"]:
            print("   HYPHEN L%d %s" % (ln, ctx[:120]))
print("TOTALS: em=%(em)d en=%(en)d hbar=%(hbar)d" % tot)
