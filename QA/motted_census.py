# -*- coding: utf-8 -*-
"""Census: Motted vs Mottled across corpus scopes (evidence for ratification)."""
import re, glob, collections

scopes = [
    ('RAW dictation', 'content/story/raw/*.md'),
    ('UMBRELLA published', 'content/story/chapter-0*.md'),
    ('SPLITS published', 'content/story/chapters/chapter-arc*.md'),
    ('DOCS bestiary/world', 'content/bestiary.md'),
    ('DOCS bestiary/world', 'content/world.md'),
    ('DOCS bestiary/world', 'content/world/*.md'),
    ('DOCS creatures', 'content/creatures/**/*.md'),
    ('DOCS places', 'content/places/*.md'),
]
res = collections.defaultdict(collections.Counter)
for name, pat in scopes:
    for f in glob.glob(pat, recursive=True):
        s = open(f, encoding='utf-8').read()
        res[name]['Motted'] += len(re.findall(r'Motted', s))
        res[name]['Mottled'] += len(re.findall(r'Mottled', s))
for k, v in res.items():
    print(f"{k}: Motted={v['Motted']}  Mottled={v['Mottled']}")
