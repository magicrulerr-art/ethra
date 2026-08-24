#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ethra Arc IV lint — adapted from QA/lint_chapters.py (Arc I-II battery).
Read-only. Scans content/story/chapters/chapter-arc4-01..06.md.
Outputs QA/arc4_tooling/lint_results_arc4.json + readable summary to stdout.
"""
import re, os, json, collections

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))          # .../QA/arc4_tooling
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))              # .../ethra_site
CHDIR = os.path.join(BASE, "content", "story", "chapters")
FILES = ["chapter-arc4-%02d.md" % c for c in range(1, 7)]

TAG_RE = re.compile(r"<[^>]+>")

CONTRACTIONS = [
    "wasnt", "cant", "dont", "wont", "thats", "ive", "ill", "id", "im",
    "whos", "didnt", "couldnt", "wouldnt", "shouldnt", "isnt", "arent",
    "youre", "theyre", "weve", "youve", "hasnt", "havent", "doesnt",
    "hed", "shes", "hes", "lets", "mustnt", "wheres", "heres", "theres",
    "yall", "hadnt", "mightnt", "neednt", "couldve", "wouldve", "shouldve",
    "mustve", "mightve", "oughta", "gonna", "wanna", "aint", "hell",
]

results = {}
para_index = collections.defaultdict(list)   # norm -> [(file, para_no, line, text)]
sent_index = collections.defaultdict(list)   # norm -> [(file, line, raw)]

def strip_tags(line):
    return TAG_RE.sub("", line)

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

for fname in FILES:
    path = os.path.join(CHDIR, fname)
    with open(path, encoding="utf-8") as fh:
        raw_lines = fh.read().split("\n")

    r = {
        "file": fname,
        "n_lines": len(raw_lines),
        "contractions": collections.defaultdict(list),
        "lowercase_i": [],
        "double_quote_odd_lines": [],
        "single_quote_odd_lines": [],
        "curly_double": {"open": 0, "close": 0},
        "curly_single": {"open": 0, "close": 0},
        "ascii_double": 0,
        "ascii_single": 0,
        "em_dash_odd_lines": [],
        "em_dash_total": 0,
        "en_dash_total": 0,
        "hbar_total": 0,
        "hyphen_dialogue_lines": [],
        "hum_variants": collections.defaultdict(list),
        "king_hits": [],
    }

    for i, raw in enumerate(raw_lines, 1):
        txt = strip_tags(raw)
        if not txt.strip():
            continue

        for w in CONTRACTIONS:
            for m in re.finditer(r"\b%s\b" % w, txt, re.IGNORECASE):
                r["contractions"][w].append((i, norm(txt)))

        for m in re.finditer(r"\bi\b", txt):
            r["lowercase_i"].append((i, norm(txt)))

        r["ascii_double"] += txt.count('"')
        r["ascii_single"] += txt.count("'")
        r["curly_double"]["open"] += txt.count("\u201c")
        r["curly_double"]["close"] += txt.count("\u201d")
        r["curly_single"]["open"] += txt.count("\u2018")
        r["curly_single"]["close"] += txt.count("\u2019")
        if txt.count('"') % 2 == 1:
            r["double_quote_odd_lines"].append((i, norm(txt)))
        if txt.count("'") % 2 == 1:
            r["single_quote_odd_lines"].append((i, norm(txt)))
        cd = txt.count("\u201c") - txt.count("\u201d")
        if cd != 0:
            r["double_quote_odd_lines"].append((i, "[curly d=%+d] %s" % (cd, norm(txt))))
        cs = txt.count("\u2018") - txt.count("\u2019")
        if cs > 0:
            r["single_quote_odd_lines"].append((i, "[curly s=%+d] %s" % (cs, norm(txt))))

        em = txt.count("\u2014")
        r["em_dash_total"] += em
        r["en_dash_total"] += txt.count("\u2013")
        r["hbar_total"] += txt.count("\u2015")
        if em % 2 == 1:
            r["em_dash_odd_lines"].append((i, em, norm(txt)))
        if re.match(r"^\s*(--|-\s)", txt) or txt.lstrip().startswith("\u2014"):
            r["hyphen_dialogue_lines"].append((i, norm(txt)))

        for m in re.finditer(r"\b[Hh]u+m+ans?\b", txt):
            r["hum_variants"][m.group(0)].append((i, norm(txt)))

        for m in re.finditer(r"\b[Kk]ings?\b", txt):
            r["king_hits"].append((i, norm(txt)))

    para_no = 0
    para_start_line = 1
    buf = []
    def flush(line_no):
        global para_no
        if buf:
            para_no += 1
            text = " ".join(norm(strip_tags(b)) for b in buf if norm(strip_tags(b)))
            if text:
                key = re.sub(r"\s+", " ", text.lower())
                para_index[key].append((fname, para_no, para_start_line, text))
                for s in re.split(r"(?<=[.!?])\s+", text):
                    s2 = norm(s)
                    if len(s2) >= 35:
                        sent_index[re.sub(r"\s+", " ", s2.lower())].append((fname, line_no, s2))
            buf.clear()
    for i, raw in enumerate(raw_lines, 1):
        if raw.strip() == "":
            flush(i)
        else:
            if not buf:
                para_start_line = i
            buf.append(raw)
    flush(len(raw_lines) + 1)

    r["contractions"] = dict(r["contractions"])
    r["hum_variants"] = dict(r["hum_variants"])
    results[fname] = r

dup_paras = {k: v for k, v in para_index.items() if len(v) >= 2 and len(k) >= 35}
dup_sents = {k: v for k, v in sent_index.items() if len(v) >= 2}

out = {
    "per_file": results,
    "duplicate_paragraphs": dup_paras,
    "duplicate_sentences": dup_sents,
}
os.makedirs(TOOL_DIR, exist_ok=True)
with open(os.path.join(TOOL_DIR, "lint_results_arc4.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)

# ---- summary to stdout ----
print("=== CONTRACTIONS MISSING APOSTROPHE ===")
for f in FILES:
    r = results[f]
    tot = sum(len(v) for v in r["contractions"].values())
    if tot:
        print("%s: %d hits" % (f, tot))
        for w in sorted(r["contractions"]):
            for ln, ctx in r["contractions"][w]:
                print("   L%d [%s] %s" % (ln, w, ctx[:150]))
print("\n=== LOWERCASE STANDALONE i ===")
for f in FILES:
    r = results[f]
    if r["lowercase_i"]:
        print("%s: %d hits" % (f, len(r["lowercase_i"])))
        for ln, ctx in r["lowercase_i"][:60]:
            print("   L%d %s" % (ln, ctx[:150]))
print("\n=== QUOTE INVENTORY (per chapter) ===")
for f in FILES:
    r = results[f]
    print("%s: ascii\"=%d ascii'=%d curlyOpen\"=%d curlyClose\"=%d curlyOpen'=%d curlyClose'=%d" % (
        f, r["ascii_double"], r["ascii_single"],
        r["curly_double"]["open"], r["curly_double"]["close"],
        r["curly_single"]["open"], r["curly_single"]["close"]))
print("\n=== LINES WITH ODD ASCII-DOUBLE-QUOTE COUNT ===")
for f in FILES:
    for ln, ctx in results[f]["double_quote_odd_lines"]:
        print("%s L%d %s" % (f, ln, ctx[:160]))
print("\n=== LINES WITH ODD ASCII-SINGLE-QUOTE COUNT ===")
for f in FILES:
    for ln, ctx in results[f]["single_quote_odd_lines"]:
        print("%s L%d %s" % (f, ln, ctx[:160]))
print("\n=== EM DASHES ===")
for f in FILES:
    r = results[f]
    print("%s: em=%d en=%d hbar=%d oddLines=%d" % (
        f, r["em_dash_total"], r["en_dash_total"], r["hbar_total"], len(r["em_dash_odd_lines"])))
    for ln, n, ctx in r["em_dash_odd_lines"]:
        print("   ODD(%d) L%d %s" % (n, ln, ctx[:160]))
    for ln, ctx in r["hyphen_dialogue_lines"]:
        print("   HYPHEN-START L%d %s" % (ln, ctx[:160]))
print("\n=== HUM VARIANTS ===")
for f in FILES:
    r = results[f]
    if r["hum_variants"]:
        counts = {w: len(v) for w, v in sorted(r["hum_variants"].items())}
        print("%s: %s" % (f, counts))
        for w in sorted(r["hum_variants"]):
            if w not in ("Humman", "Hummans"):  # deviations only
                for ln, ctx in r["hum_variants"][w]:
                    print("   L%d [%s] %s" % (ln, w, ctx[:150]))
print("\n=== KING/KING ===")
for f in FILES:
    r = results[f]
    if r["king_hits"]:
        print("%s: %d hits" % (f, len(r["king_hits"])))
        for ln, ctx in r["king_hits"]:
            print("   L%d %s" % (ln, ctx[:170]))
print("\n=== DUPLICATE PARAGRAPHS (>=2 occurrences, len>=35) ===")
for k, v in sorted(dup_paras.items(), key=lambda kv: -len(kv[1])):
    print("x%d @ %s :: %s" % (len(v), "; ".join("%s p%d L%d" % (a, b, c) for a, b, c, _ in v), k[:180]))
print("\n=== DUPLICATE SENTENCES (>=2 occurrences, len>=35) ===")
for k, v in sorted(dup_sents.items(), key=lambda kv: -len(kv[1])):
    print("x%d @ %s :: %s" % (len(v), "; ".join("%s L%d" % (a, b) for a, b, _ in v), k[:180]))
