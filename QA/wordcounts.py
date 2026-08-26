import re, glob, pathlib
tot = {}
for f in sorted(glob.glob('ethra_site/content/story/chapters/chapter-arc[1-4]-*.md')):
    t = pathlib.Path(f).read_text(encoding='utf-8')
    t = re.sub(r'<[^>]+>', ' ', t)
    n = len(t.split())
    arc = pathlib.Path(f).name.split('-')[1]
    tot[arc] = tot.get(arc, 0) + n
    print(f"{pathlib.Path(f).name}: {n:,} words")
print()
for a, n in sorted(tot.items()):
    print(f"{a}: {n:,} words total")
print(f"GRAND TOTAL arcs I-IV: {sum(tot.values()):,} words")
