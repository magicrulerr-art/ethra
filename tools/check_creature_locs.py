"""One-shot check: every JSON creature slug has a matching file, and the
file's biome directory matches the JSON biome."""
import os
import json

d = json.load(open('static/data/map-coordinates.json', encoding='utf-8'))
locs = {}
for b in os.listdir('content/creatures'):
    p = os.path.join('content/creatures', b)
    if os.path.isdir(p):
        for f in os.listdir(p):
            if f.endswith('.md'):
                locs[f[:-3]] = b

missing = []
for c in d['creatures']:
    s = c['slug']
    if s not in locs:
        missing.append(s)
    elif locs[s] != c['biome']:
        print('BIOME MISMATCH:', s, 'json:', c['biome'], 'file dir:', locs[s])
print('missing files:', missing)
print('total json creatures:', len(d['creatures']))
print('total creature files:', len(locs))
