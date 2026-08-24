# -*- coding: utf-8 -*-
"""Arc IV final tally — adapted from QA/final_tally.py.
Hum variants + king/King census per chapter and in the umbrella; corpus canon check."""
import re, io, sys, os, collections, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CH = os.path.join(BASE, "content", "story", "chapters") + os.sep
UMBRELLA = os.path.join(BASE, "content", "story", "chapter-04.md")
files = ["chapter-arc4-%02d.md" % c for c in range(1, 7)]

def detag(s): return re.sub(r"<[^>]+>", "", s)

print("### HUM VARIANTS PER CHAPTER (case-sensitive exact forms) ###")
grand = collections.Counter()
for f in files:
    txt = detag(open(CH + f, encoding="utf-8").read())
    c = collections.Counter(m.group(0) for m in re.finditer(r"\b[Hh]u+m+ans?\b", txt))
    grand.update(c)
    print(f, dict(sorted(c.items())))
print("SPLITS GRAND:", dict(sorted(grand.items())))

txt = detag(open(UMBRELLA, encoding="utf-8").read())
c = collections.Counter(m.group(0) for m in re.finditer(r"\b[Hh]u+m+ans?\b", txt))
print("UMBRELLA chapter-04.md:", dict(sorted(c.items())))

print("\n### KING/KING PER CHAPTER + UMBRELLA ###")
for f in files:
    txt = detag(open(CH + f, encoding="utf-8").read())
    cap = len(re.findall(r"\bKing\b", txt)); low = len(re.findall(r"\bking\b", txt))
    print(f, "King=%d king=%d" % (cap, low))
txt = detag(open(UMBRELLA, encoding="utf-8").read())
print("UMBRELLA", "King=%d king=%d" % (len(re.findall(r"\bKing\b", txt)), len(re.findall(r"\bking\b", txt))))

print("\n### KING CAPITALIZED CONTEXT CHECK (umbrella) — any 'king Ajani/Uthgard' lowercase? ###")
for i, l in enumerate(open(UMBRELLA, encoding="utf-8").read().split("\n"), 1):
    t = detag(l)
    for m in re.finditer(r"\bking (?:Ajani|Uthgard)", t):
        print("L%d %s" % (i, t.strip()[:120]))

print("\n### CORPUS CANON CHECK (all story md, incl. umbrella + splits + other arcs) ###")
canon_h = canon_hu = 0
for p in glob.glob(os.path.join(BASE, "content", "**", "*.md"), recursive=True):
    txt = open(p, encoding="utf-8", errors="ignore").read()
    canon_h += len(re.findall(r"\bHummans?\b", txt))
    canon_hu += len(re.findall(r"\bhumans?\b", txt, re.I)) - len(re.findall(r"\bhummans?\b", txt, re.I))
print("Corpus: 'Humman(s)' (canon)=%d, plain 'human(s)'=%d" % (canon_h, canon_hu))

print("\n### EM DASH TOTALS ###")
for f in files:
    txt = detag(open(CH + f, encoding="utf-8").read())
    print(f, "em=%d en=%d" % (txt.count("\u2014"), txt.count("\u2013")))
txt = detag(open(UMBRELLA, encoding="utf-8").read())
print("UMBRELLA", "em=%d en=%d" % (txt.count("\u2014"), txt.count("\u2013")))
