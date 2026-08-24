# -*- coding: utf-8 -*-
"""Repair double-encoded UTF-8 in templates/index.html, add favicon link,
bump css cache-buster. Writes bytes directly — no editor round-trip."""
import sys

P = 'templates/index.html'
txt = open(P, encoding='utf-8').read()

def undouble(s):
    out = bytearray()
    for ch in s:
        o = ord(ch)
        if o < 0x100:
            out.append(o)
        else:
            out += ch.encode('cp1252')   # raises if truly unmappable
    return out.decode('utf-8')

fixed = undouble(txt)

# sanity: the repaired text must contain the intended glyphs
for glyph in ['✦', '—', '·', '↩', '…', '═']:
    assert glyph in fixed, 'missing glyph after repair: ' + glyph
assert 'â€' not in fixed and 'Â·' not in fixed and 'â†' not in fixed

# favicon (was missing entirely)
if 'rel="icon"' not in fixed:
    anchor = '<meta charset="UTF-8">'
    assert anchor in fixed
    fixed = fixed.replace(
        anchor,
        anchor + '\n<link rel="icon" type="image/svg+xml" href="/static/favicon.svg">\n'
        '<link rel="apple-touch-icon" href="/static/favicon.svg">',
        1)

# cache-buster for the motif CSS
assert 'ethra_core.css?v=28' in fixed
fixed = fixed.replace('ethra_core.css?v=28', 'ethra_core.css?v=29')

open(P, 'w', encoding='utf-8', newline='').write(fixed)
print('repaired + favicon + v29')
