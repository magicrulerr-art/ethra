import re, io, sys, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
files = ["chapter-arc%d-%02d.md" % (a, c) for a in (1, 2) for c in range(1, 7)]
CH = "ethra_site/content/story/chapters/"

print("### HUM VARIANTS PER CHAPTER (case-insensitive exact forms) ###")
grand = collections.Counter()
for f in files:
    txt = re.sub(r"<[^>]+>", "", open(CH + f, encoding="utf-8").read())
    c = collections.Counter(m.group(0) for m in re.finditer(r"\b[Hh]u+m+ans?\b", txt))
    grand.update(c)
    print(f, dict(sorted(c.items())))
print("GRAND:", dict(sorted(grand.items())))

print("\n### KING/KING PER CHAPTER ###")
for f in files:
    txt = re.sub(r"<[^>]+>", "", open(CH + f, encoding="utf-8").read())
    cap = len(re.findall(r"\bKing\b", txt))
    low = len(re.findall(r"\bking\b", txt))
    print(f, "King=%d king=%d" % (cap, low))

print("\n### REPORTED REPETITIONS ###")
def count_phrase(f, pat):
    txt = re.sub(r"<[^>]+>", "", open(CH + f, encoding="utf-8").read())
    return len(re.findall(pat, txt, re.I))
print("arc2-03 'Bright Paw capital' (incl heading):", count_phrase("chapter-arc2-03.md", r"bright paw capital"))
print("arc2-06 'She stepped closer':", count_phrase("chapter-arc2-06.md", r"she stepped closer"))
print("arc2-06 'Sylara' (any):", count_phrase("chapter-arc2-06.md", r"sylara"))
print("arc2-06 'She raised':", count_phrase("chapter-arc2-06.md", r"she raised"))
print("arc2-06 'She raised the Petal-Shell':", count_phrase("chapter-arc2-06.md", r"she raised the petal-shell"))

print("\n### 'hummans' canon check across non-arc1/2 corpus ###")
import glob, os
canon_h = canon_hu = 0
for p in glob.glob("ethra_site/content/**/*.md", recursive=True):
    bn = os.path.basename(p)
    if bn.startswith("chapter-arc1-") or bn.startswith("chapter-arc2-"):
        continue
    txt = open(p, encoding="utf-8", errors="ignore").read()
    canon_h += len(re.findall(r"\bHummans?\b", txt))
    canon_hu += len(re.findall(r"\bhumans?\b", txt, re.I)) - len(re.findall(r"\bhummans?\b", txt, re.I))
print("Rest of corpus: 'Humman(s)' (canon)=%d, plain 'human(s)'=%d" % (canon_h, canon_hu))
