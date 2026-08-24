import re, io, sys, os, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters") + os.sep
files = ["chapter-arc3-%02d.md" % c for c in range(1, 6)]

print("### HUM VARIANTS PER CHAPTER (case-sensitive exact forms) ###")
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

print("\n### ARC3 REPETITION PHRASES ###")
def count_phrase(f, pat):
    txt = re.sub(r"<[^>]+>", "", open(CH + f, encoding="utf-8").read())
    return len(re.findall(pat, txt, re.I))
probes = [r"fire feet", r"tyrant cycle", r"the arena", r"she stepped closer",
          r"he raised", r"she raised", r"the spear", r"aura", r"low hum"]
for f in files:
    row = ", ".join("%s=%d" % (p.replace("\\",""), count_phrase(f, p)) for p in probes)
    print(f, row)

print("\n### UMBRELLA chapter-03.md census ###")
u = open(os.path.join(BASE, "content", "story", "chapter-03.md"), encoding="utf-8").read()
print("lines:", len(u.split("\n")), "chars:", len(u))
print("Humman(s):", len(re.findall(r"\bHummans?\b", u)), "| human(s) any-case:", len(re.findall(r"\bhumans?\b", u, re.I)))
print("King:", len(re.findall(r"\bKing\b", u)), "king:", len(re.findall(r"\bking\b", u)))
print("em dashes:", u.count("\u2014"))
print("asterisk lines:", sum(1 for l in u.split("\n") if "*" in l))
