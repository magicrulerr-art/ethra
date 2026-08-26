# -*- coding: utf-8 -*-
"""Script B2: chapter-04.md — vary 7 of 12 Sylva aura 'flickered gently' tics."""
import pathlib

P = pathlib.Path('ethra_site/content/story/chapter-04.md')
t = P.read_text(encoding='utf-8')
assert t.count("flickered gently") == 14

# (unique anchor including following text, replacement of the aura sentence only)
EDITS = [
    # occ 2 — beside-throne approval beat
    ("Sylva's silver aura flickered gently in the shadows beside the throne, and her ancient eyes held",
     "Sylva's silver aura pulsed, soft and low, in the shadows beside the throne, and her ancient eyes held"),
    # occ 3 — Motted Paws will serve
    ("Sylva's silver aura flickered gently. <span class=\"speech\">\"The Motted Paws will serve",
     "Sylva's silver aura shimmered faintly. <span class=\"speech\">\"The Motted Paws will serve"),
    # occ 4 — declined beat
    ("Sylva's silver aura flickered gently. She had been declined",
     "A slow flicker passed through Sylva's silver aura. She had been declined"),
    # occ 5 — grand vizier
    ("Sylva's silver aura flickered gently. <span class=\"speech\">\"The grand vizier will hold",
     "Sylva's silver aura stirred. <span class=\"speech\">\"The grand vizier will hold"),
    # occ 9 — Seris asks for much
    ("Sylva's silver aura flickered gently. \"You ask for much, Ambassador",
     "Sylva's silver aura dimmed, then steadied. \"You ask for much, Ambassador"),
    # occ 11 — Lena / you will not fail
    ("Sylva's silver aura flickered gently. \"You will not fail. You are too stubborn",
     "Sylva's silver aura pulsed gently. \"You will not fail. You are too stubborn"),
    # occ 13 — intelligence network
    ("Sylva's silver aura flickered gently. <span class=\"speech\">\"The intelligence network is working",
     "Sylva's silver aura rippled once. <span class=\"speech\">\"The intelligence network is working"),
]

for old, new in EDITS:
    assert t.count(old) == 1, f"anchor not unique: {old[:60]}"
    t = t.replace(old, new)

remaining = t.count("flickered gently")
assert remaining == 7, f"expected 7 remaining, got {remaining}"
P.write_text(t, encoding='utf-8')
print("Script B2 DONE: 14 ->", remaining, "(keep: occ1, 7, 8, 10, 14 Sylva + 2 Ajani green-fire)")
