# -*- coding: utf-8 -*-
"""Find paragraphs (>=25 words) that appear more than once within the same
chapter — the direct 'reader reads the same scene twice' pacing defect."""
import re, glob, pathlib

def norm(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\s+', ' ', s).lower().strip(' .')
    return s

for f in sorted(glob.glob('ethra_site/content/story/chapters/chapter-arc[1-4]-*.md')):
    text = pathlib.Path(f).read_text(encoding='utf-8')
    # paragraphs: split on blank lines; also break dialogue divs into their <p> blocks
    chunks = []
    for blk in re.split(r'\n\s*\n', text):
        blk = blk.strip()
        if not blk:
            continue
        for p in re.findall(r'<p[^>]*>(.*?)</p>', blk, re.S):
            chunks.append(p)
        plain = re.sub(r'<[^>]+>', ' ', blk)
        if plain.strip() and '<p' not in blk:
            chunks.append(plain)
    seen = {}
    for c in chunks:
        n = norm(c)
        w = len(n.split())
        if w >= 25:
            seen.setdefault(n, []).append(c)
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    if dupes:
        print(f"\n=== {pathlib.Path(f).name} ===")
        for k, v in dupes.items():
            print(f"  [{len(v)}x, {len(k.split())}w] {k[:110]}...")
