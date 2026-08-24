import re, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
CH = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters" + os.sep
UMB = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-03.md"
EM = "\u2014"
files = [("chapter-arc3-%02d.md" % c, CH + "chapter-arc3-%02d.md" % c) for c in range(1, 6)]
files.append(("UMBRELLA chapter-03.md", UMB))
for name, path in files:
    lines = open(path, encoding="utf-8").read().split("\n")
    n_led = n_dd = n_ah = n_en = 0
    for i, l in enumerate(lines, 1):
        t = re.sub(r"<[^>]+>", "", l)
        s = t.rstrip()
        if s.endswith(EM):
            n_led += 1
            print("%s L%-5d LINE-END-DASH: ...%s" % (name, i, s[-90:]))
        if EM + EM in t or EM + " " + EM in t:
            n_dd += 1
            print("%s L%-5d DOUBLE/SPACED-DASH: ...%s" % (name, i, t.strip()[:120]))
        if re.search(r"--+", t):
            n_ah += 1
            print("%s L%-5d ASCII-HYPHEN-RUN: %s" % (name, i, t.strip()[:120]))
        if "\u2013" in t:
            n_en += 1
            print("%s L%-5d EN-DASH: %s" % (name, i, t.strip()[:120]))
    print("%s: line-end=%d doubled=%d ascii-run=%d en=%d" % (name, n_led, n_dd, n_ah, n_en))
