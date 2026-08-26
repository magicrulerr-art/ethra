# -*- coding: utf-8 -*-
"""D5 adjudication (2026-08-25, Ainz delegated judgment to Mare):
lowercase 'humman(s)' in published prose is drift, not style — normalize
to capitalized 'Humman(s)' (canon race name, always capitalized like
Wengari/Pyrinae/Veylar/Threx). Applied to Arc IV + Arc VI umbrellas only.
Raw ledger (content/story/raw/) untouched — verbatim dictation record.
"""
import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
targets = [
    BASE / 'content' / 'story' / 'chapter-04.md',
    BASE / 'content' / 'story' / 'chapter-06.md',
]

pat = re.compile(r'\bhumman(s?)\b')  # case-sensitive: lowercase only
total = 0
for t in targets:
    s = t.read_text(encoding='utf-8')
    new, n = pat.subn(lambda m: 'Humman' + m.group(1), s)
    if n:
        t.write_text(new, encoding='utf-8')
        print(f"{t.name}: {n} normalized")
        total += n
    else:
        print(f"{t.name}: none found")
print(f"TOTAL: {total}")

# Verify zero lowercase remain in published content (excl. raw/ and .bak)
left = 0
for f in (BASE / 'content' / 'story').glob('*.md'):
    left += len(pat.findall(f.read_text(encoding='utf-8')))
for f in (BASE / 'content' / 'story' / 'chapters').glob('chapter-arc*.md'):
    left += len(pat.findall(f.read_text(encoding='utf-8')))
print(f"remaining lowercase in umbrellas+splits: {left} (splits go to 0 after regenerate)")
