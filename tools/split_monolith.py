# -*- coding: utf-8 -*-
"""split_monolith.py — P2a: extract the four inline blocks from
templates/index.html into static/css + static/js, replacing them with
cache-busted link/script tags at the exact same positions (same order,
same synchronous timing). Run once; idempotence NOT guaranteed."""
import io, os, sys

ROOT = os.path.join(os.path.dirname(__file__), '..')
TPL = os.path.join(ROOT, 'templates', 'index.html')

with io.open(TPL, encoding='utf-8') as f:
    lines = f.read().split('\n')

def block(a, b):  # 1-based inclusive
    return '\n'.join(lines[a-1:b])

css1 = block(11, 1725)
css2 = block(1732, 1928)
js1 = block(2076, 2825)
js2 = block(2829, 3187)

# sanity: boundaries are exactly the tag lines
assert lines[9].strip() == '<style>', lines[9]
assert lines[1725].strip() == '</style>', lines[1725]
assert lines[1730].strip() == '<style>', lines[1730]
assert lines[1928].strip() == '</style>', lines[1928]
assert lines[2074].strip() == '<script>', lines[2074]
assert lines[2825].strip() == '</script>', lines[2825]
assert lines[2827].strip() == '<script>', lines[2827]
assert lines[3187].strip() == '</script>', lines[3187]
# no jinja inside the extracted blocks
for name, blk in (('css1', css1), ('css2', css2), ('js1', js1), ('js2', js2)):
    assert '{{' not in blk and '{%' not in blk, name

out = {
    'static/css/ethra_core.css': css1,
    'static/css/ethra_story.css': css2,
    'static/js/ethra_core.js': js1,
    'static/js/ethra_story.js': js2,
}
for rel, text in out.items():
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text + '\n')
    print('wrote %s (%d lines)' % (rel, text.count('\n') + 1))

# rebuild the template with tags in place
V = '24'
new = []
i = 0  # 0-based
def emit_tags(which):
    if which == 1:
        new.append('<link rel="stylesheet" href="/static/css/ethra_core.css?v=%s">' % V)
    elif which == 2:
        new.append('<link rel="stylesheet" href="/static/css/ethra_story.css?v=%s">' % V)
    elif which == 3:
        new.append('<script src="/static/js/ethra_core.js?v=%s"></script>' % V)
    elif which == 4:
        new.append('<script src="/static/js/ethra_story.js?v=%s"></script>' % V)

# line numbers (1-based) -> 0-based indices
spans = [(10, 1725, 1), (1731, 1928, 2), (2075, 2825, 3), (2828, 3187, 4)]
skip = {}
for a, b, w in spans:
    for n in range(a, b + 1):
        skip[n] = w

for n in range(1, len(lines) + 1):
    if n in skip:
        if n == [a for a, b, w in spans if skip[n] == w][0]:
            emit_tags(skip[n])
        continue
    new.append(lines[n-1])

with io.open(TPL, 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(new))
print('template now %d lines (was %d)' % (len(new), len(lines)))
