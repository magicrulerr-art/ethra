# -*- coding: utf-8 -*-
"""diet_audit.py — list static/images files no static ref or runtime
picker/probe touches (superseded art candidates)."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rep = json.load(open(os.path.join(ROOT, 'tools', 'linkcheck.json'), encoding='utf-8'))
used = set(rep['existing_refs'])
for d in rep['dynamic_probes']:
    for p in d.get('paths', []):
        used.add(p)

img = 'static/images'
unused = []
for f in sorted(os.listdir(os.path.join(ROOT, img))):
    p = img + '/' + f
    if p not in used and os.path.isfile(os.path.join(ROOT, p)):
        unused.append((p, os.path.getsize(os.path.join(ROOT, p))))
tot = sum(s for _, s in unused)
print('unreferenced files:', len(unused), ' total: %.1fMB' % (tot / 1e6))
for p, s in unused:
    print('  %-55s %6.2fMB' % (p, s / 1e6))
