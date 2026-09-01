"""Excise unauthorized gift montage from chapter-04.md (Ainz ruling 2026-09-01).
Marker-based: find exact start/end strings, cut the span, insert one bridging line."""
import io, sys

F = 'content/story/chapter-04.md'
START = 'The capital stirred with the arrival of foreign delegations.'
END = '"We will be worthy, my king. We will climb."'
BRIDGE = 'Three weeks passed.'

t = io.open(F, encoding='utf-8').read()
i = t.find(START)
assert i != -1, 'start marker not found'
j = t.find(END, i)
assert j != -1, 'end marker not found'
j += len(END)

before = t[:i].rstrip()
after = t[j:].lstrip()
assert after.startswith('Lena knelt beside the pool'), 'unexpected text after montage: ' + after[:60]

new = before + '\n\n' + BRIDGE + '\n\n' + after
io.open(F, 'w', encoding='utf-8', newline='\n').write(new)

import re
print('cut chars:', j - i)
print('montage residue — obsidian dagger:', len(re.findall(r'(?i)obsidian dagger', new)),
      '| spore:', len(re.findall(r'(?i)\bspore\b', new)),
      '| Sylara:', len(re.findall(r'Sylara', new)),
      '| private ceremony:', len(re.findall(r'(?i)private ceremon', new)),
      '| Veylar came first:', len(re.findall(r'The Veylar came first', new)),
      '| barding (kept refs):', len(re.findall(r'(?i)ceremonial barding', new)))
print('bridge present:', BRIDGE in new)
print('new length:', len(new))
