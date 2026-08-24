import re, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
CH = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters"
UMB = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-03.md"
files = ["chapter-arc3-%02d.md" % c for c in range(1, 6)]
TAG = re.compile(r"<[^>]+>")

probes = [
    ("PYRANEI", r"PYRANEI"),
    ("STEMMED", r"\bSTEMMED\b"),
    ("ESPECTACULAR", r"ESPECTACULAR"),
    ("fhe", r"\bfhe\b"),
    ("wenfari", r"\bwenfari\b", re.I),
    ("definetly", r"\bdefinetl?y\b", re.I),
    ("RISED", r"\bRISED\b"),
    ("loose (the crown)", r"\bloose\b", re.I),
    ("gauge (eyes)", r"\bgauge\b", re.I),
    ("Faint (feint?)", r"\bFaint\b"),
    ("FRIEND'S", r"FRIEND'S"),
    ("therye", r"\btherye\b", re.I),
    ("dual blade", r"\bdual blade", re.I),
    ("DESER", r"\bDESER\b"),
    ("t'vat lowercase", r"\bt'vat\b"),
    ("'1)' numbered rule", r"\b1\)"),
    ("'2)' numbered rule", r"\b2\)"),
    ("styx lowercase", r"\bstyx\b"),
    ("wengari lowercase", r"\bwengari\b"),
    ("solen lowercase", r"\bsolen\b"),
    ("striped paws lowercase", r"\bstriped paws\b"),
    ("veylar lowercase", r"\bveylar\b"),
    ("pyrinae lowercase", r"\bpyrinae\b"),
    ("threx lowercase", r"\bthrex\b"),
    ("kyrie", r"\bkyrie\b", re.I),
    ("gratious", r"\bgratious\b", re.I),
    ("payed", r"\bpayed\b", re.I),
    ("assasins", r"\bassasins?\b", re.I),
    ("three thousands", r"\bthree thousands\b", re.I),
    ("Raise and eyebrow", r"Raise and eyebrow"),
    ("dessert", r"\bdessert\b", re.I),
    ("wanning", r"\bwanning\b", re.I),
    ("handt", r"\bhandt\b", re.I),
    ("producy", r"\bproducy\b", re.I),
    ("my father son", r"my father son", re.I),
    ("appropiate", r"\bappropiate\b", re.I),
]

for f in files + [os.path.basename(UMB)]:
    path = os.path.join(CH, f) if f.startswith("chapter-arc3") else UMB
    lines = open(path, encoding="utf-8").read().split("\n")
    print("=" * 80); print(f)
    for probe in probes:
        label, pat = probe[0], probe[1]
        flags = probe[2] if len(probe) > 2 else 0
        hits = []
        for i, raw in enumerate(lines, 1):
            t = TAG.sub("", raw)
            for m in re.finditer(pat, t, flags):
                hits.append(i)
        if hits:
            print("  %-22s x%-3d lines %s" % (label, len(hits), hits[:20]))
