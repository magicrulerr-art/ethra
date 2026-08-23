# -*- coding: utf-8 -*-
"""diet_archive.py — move superseded art into static/images/_archive/.
Keep-set rule: highest -vN per chapter cover, map-supercontinent v2,
the active arc5-med probe hit per chapter, all docs for kept art."""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'static', 'images')
ARC = os.path.join(IMG, '_archive')
os.makedirs(ARC, exist_ok=True)

moved = []
def mv(name):
    src = os.path.join(IMG, name)
    if os.path.exists(src):
        shutil.move(src, os.path.join(ARC, name))
        moved.append(name)
    else:
        print('!! absent:', name)

# v0 covers superseded by -v2 / -v8
for ch in ('01', '04', '05'):
    for ext in ('png', 'jpg', 'webp'):
        mv('chapter-arc4-%s.%s' % (ch, ext))
# arc5 ch11: keep v101 only
for v in (1, 2, 3, 4, 5, 99, 100):
    for ext in ('png', 'jpg', 'webp'):
        mv('chapter-arc5-11-v%d.%s' % (v, ext))
# map: keep v2
for v in (1, 3, 4):
    mv('map-supercontinent-v%d.png' % v)
for doc in ('map-supercontinent-v1-PROMPT-RECORD.md',
            'map-supercontinent-v3-PROMPT-RECORD.md',
            'map-supercontinent-v4-PROMPT-RECORD.md',
            'map-supercontinent-v4-VISUAL-AUDIT.md'):
    mv(doc)
# windows redirect junk
mv('$null')

print('moved %d files -> static/images/_archive/' % len(moved))
for m in moved:
    print('  ', m)
