import re, io, sys, os, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
CH = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters" + os.sep
UMB = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-03.md"
files = ["chapter-arc3-%02d.md" % c for c in range(1, 6)]
TAG = re.compile(r"<[^>]+>")

print("### ALL LINES CONTAINING ASTERISK (splits) ###")
for f in files:
    lines = open(CH + f, encoding="utf-8").read().split("\n")
    for i, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        if "*" in t:
            print("%s L%-4d (%d*) %s" % (f, i, t.count("*"), t.strip()[:170]))

print("\n### UMBRELLA HUM VARIANTS (case-sensitive exact forms) ###")
u = open(UMB, encoding="utf-8").read()
c = collections.Counter(m.group(0) for m in re.finditer(r"\b[Hh]u+m+ans?\b", u))
print(dict(sorted(c.items())))

print("\n### GENERIC 'the King' (capital K after determiner) in splits ###")
for f in files:
    txt = TAG.sub("", open(CH + f, encoding="utf-8").read())
    for m in re.finditer(r"\b(the|a|an|our|my|your|his|their) King\b", txt):
        print(f, m.group(0))

print("\n### DIRECT-ADDRESS CHECK: 'my king' vs 'My king' sentence starts ###")
for f in files:
    lines = open(CH + f, encoding="utf-8").read().split("\n")
    for i, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        for m in re.finditer(r"\b[Kk]ing\b", t):
            a = max(0, m.start() - 14)
            pre = t[a:m.start()].lower()
            if pre.endswith("my ") and m.group(0) == "King":
                print("%s L%d My-KING: %s" % (f, i, t[max(0, m.start()-20):m.start()+12][:60]))
