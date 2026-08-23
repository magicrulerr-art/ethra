"""One-shot migration: add map-pin frontmatter to creature files.

Reads static/data/map-coordinates.json and prepends a YAML-lite
frontmatter block (name/kind/x_pct/y_pct/subtitle?/image_full?) to each
matching content/creatures/<biome>/<slug>.md. Idempotent: files that
already start with '---' are skipped. The JSON stays as override source.
"""
import json
import os

COORDS = os.path.join('static', 'data', 'map-coordinates.json')
ROOT = os.path.join('content', 'creatures')

data = json.load(open(COORDS, encoding='utf-8'))

changed, skipped, missing = 0, 0, []
for c in data['creatures']:
    path = os.path.join(ROOT, c['biome'], c['slug'] + '.md')
    if not os.path.isfile(path):
        missing.append(path)
        continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    if text.startswith('---'):
        skipped += 1
        continue
    lines = ['---', f"name: {c['name']}", f"kind: {c.get('kind', 'creature')}",
             f"x_pct: {c['x_pct']}", f"y_pct: {c['y_pct']}"]
    if c.get('subtitle'):
        lines.append(f"subtitle: {c['subtitle']}")
    if c.get('image_full'):
        lines.append(f"image_full: {c['image_full']}")
    lines.append('---')
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(lines) + '\n' + text)
    changed += 1

print(f'changed={changed} skipped(already had frontmatter)={skipped}')
print('missing files:', missing)
