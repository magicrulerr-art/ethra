# -*- coding: utf-8 -*-
"""MOTTED ratification (2026-08-25, delegated by Ainz to Mare).
Corpus evidence: raw dictation ledger uses 'Motted' EXCLUSIVELY (0
'Mottled' in raw/); published story uses 'Mottled' exactly once
(arc5-11, Cefiro's reveal). Ratified canon: the family is the MOTTED
Paws (jaguars, Rune Belt). This script aligns all doc-side text.
Asset/file renames done separately via git mv.
"""
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
files = [
    'content/bestiary.md',
    'content/world.md',
    'content/world/geography.md',
    'content/creatures/rune-belt/mottled-paw.md',
    'content/creatures/rune-belt/shadow-paw.md',
    'content/creatures/rune-belt/stripe-paw.md',
    'content/creatures/rune-belt/wengari.md',
    'content/creatures/umbral-ring/snow-paws.md',
    'content/places/riversong.md',
    'content/story/chapter-05.md',
]
total = 0
for rel in files:
    p = BASE / rel
    s = p.read_text(encoding='utf-8')
    n1 = s.count('Mottled')
    s = s.replace('Mottled', 'Motted')          # case-sensitive: keeps 'dusk-mottling'
    n2 = s.count('mottled-paw')
    s = s.replace('mottled-paw', 'motted-paw')
    if n1 or n2:
        p.write_text(s, encoding='utf-8')
        print(f"{rel}: Mottled->{n1}, mottled-paw->{n2}")
        total += n1 + n2
    else:
        print(f"{rel}: clean")
print(f"TOTAL replacements: {total}")
