#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Final tally — Arc V (adapted from QA/final_tally.py). Read-only."""
import re, io, os, sys, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters")
files = ["chapter-arc5-%02d.md" % c for c in range(1, 23)]
TAG = re.compile(r"<[^>]+>")

print("### HUM VARIANTS PER CHAPTER (exact case forms) ###")
grand = collections.Counter()
for f in files:
    txt = TAG.sub("", open(os.path.join(CH, f), encoding="utf-8").read())
    c = collections.Counter(m.group(0) for m in re.finditer(r"\b[Hh]u+m+ans?\b", txt))
    grand.update(c)
    print(f, dict(sorted(c.items())))
print("GRAND:", dict(sorted(grand.items())))

print("\n### KING/KING PER CHAPTER ###")
for f in files:
    txt = TAG.sub("", open(os.path.join(CH, f), encoding="utf-8").read())
    cap = len(re.findall(r"\bKing\b", txt))
    low = len(re.findall(r"\bking\b", txt))
    print(f, "King=%d king=%d" % (cap, low))

print("\n### ARC5-SPECIFIC CENSUS ###")
def cnt(pat, flags=re.I):
    tot = 0
    per = {}
    for f in files:
        txt = TAG.sub("", open(os.path.join(CH, f), encoding="utf-8").read())
        n = len(re.findall(pat, txt, flags))
        per[f] = n
        tot += n
    return tot, {k: v for k, v in per.items() if v}
for label, pat, fl in [
    ("'Bright Mane' (two words)", r"\bBright Mane\b", 0),
    ("'Brightmane' (one word)", r"\bBrightmane\b", 0),
    ("boilerplate 'It was X ... reign of'", r"in the first year of the reign of", re.I),
    ("draft verb 'yells'", r"\byells?\b", re.I),
    ("draft verb 'says' (present-tense instruction)", r"\b(?:Ajani|Nefere|M'rak) says\b", 0),
    ("'FIRE THE RAY'", r"FIRE THE RAY", 0),
    ("excess bangs !!!!", r"!{3,}", 0),
    ("'the black thing'", r"the black thing", re.I),
    ("Woh mount", r"\bWohs?\b", 0),
    ("Tide Wolf(s)", r"\bTide Wolfs?\b|\bTide Wolves\b", 0),
]:
    tot, per = cnt(pat, fl)
    print("%-52s total=%d  %s" % (label, tot, per if per else ""))

print("\n### 'Humman(s)' canon check across non-arc5 corpus ###")
import glob
canon_h = plain_h = 0
for p in glob.glob(os.path.join(BASE, "content", "**", "*.md"), recursive=True):
    bn = os.path.basename(p)
    if bn.startswith("chapter-arc5-"):
        continue
    txt = open(p, encoding="utf-8", errors="ignore").read()
    canon_h += len(re.findall(r"\bHummans?\b", txt))
    plain_h += len(re.findall(r"\bhumans?\b", txt, re.I)) - len(re.findall(r"\bhummans?\b", txt, re.I))
print("Rest of corpus: 'Humman(s)' (canon)=%d, plain 'human(s)'=%d" % (canon_h, plain_h))
