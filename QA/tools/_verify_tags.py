import glob, re
res_tot = 0
patterns = ['granddaughter', "Sun's Mercy", 'Honorary General', 'conjured from nothing',
            'the correct resolution', 'the correct conclusion', 'Every other day',
            'Ajani says his voice booming']
for f in sorted(glob.glob('content/story/chapters/chapter-arc*.md')):
    t = open(f, encoding='utf-8').read()
    for p in patterns:
        if p in t:
            print('RESIDUE', repr(p), '->', f.split(chr(92))[-1]); res_tot += 1
print('residue total:', res_tot)

print()
print('== maid rename (Mara) / envoy (Mira) in arc3 & arc4 ==')
for f in sorted(glob.glob('content/story/chapters/chapter-arc3-*.md')) + sorted(glob.glob('content/story/chapters/chapter-arc4-*.md')):
    t = open(f, encoding='utf-8').read()
    if 'Mara' in t or 'Mira' in t:
        print(' ', f.split(chr(92))[-1], 'Mara', t.count('Mara'), 'Mira', t.count('Mira'))

print()
print('== Tamsin title in arc6 ==')
for f in sorted(glob.glob('content/story/chapters/chapter-arc6-*.md')):
    t = open(f, encoding='utf-8').read()
    if 'Knight of the Wengari' in t or 'Mira' in t:
        print(' ', f.split(chr(92))[-1], 'KnightWengari', t.count('Knight of the Wengari'), 'Mira', t.count('Mira'))