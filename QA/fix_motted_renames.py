# -*- coding: utf-8 -*-
"""Rename mottled-paw assets + creature file -> motted-paw (ratification).
Pure renames; content already text-aligned by fix_motted_ratification.py.
"""
import os, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
renames = [
    ('static/images/mottled-paw.png',  'static/images/motted-paw.png'),
    ('static/images/mottled-paw.webp', 'static/images/motted-paw.webp'),
    ('static/images/mottled-paw.jpg',  'static/images/motted-paw.jpg'),
    ('content/creatures/rune-belt/mottled-paw.md', 'content/creatures/rune-belt/motted-paw.md'),
]
for src, dst in renames:
    s, d = BASE / src, BASE / dst
    if not s.exists():
        print(f"SKIP (missing src): {src}")
        continue
    if d.exists():
        print(f"SKIP (dst exists): {dst}")
        continue
    os.rename(s, d)
    print(f"renamed: {src} -> {dst}  (exists={d.exists()})")

# verify none of the old names remain
for src, _ in renames:
    print(f"old gone? {src}: {not (BASE/src).exists()}")
