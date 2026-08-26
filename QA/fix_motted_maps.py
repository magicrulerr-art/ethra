# -*- coding: utf-8 -*-
"""Align derived map JSONs + linkcheck inventory with MOTTED ratification."""
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
jobs = [
    ('static/maps/cultures_v2.json', [('Mottled Paw Wengari', 'Motted Paw Wengari')]),
    ('static/maps/states_v2.json', [('Mottled March', 'Motted March')]),
    ('static/maps/burgs_v2.json', [('Mottled Crossing', 'Motted Crossing')]),
    ('tools/linkcheck.json', [
        ('static/images/mottled-paw.png', 'static/images/motted-paw.png'),
        ('static/images/mottled-paw.webp', 'static/images/motted-paw.webp'),
        ('static/images/mottled-paw.jpg', 'static/images/motted-paw.jpg'),
    ]),
]
for rel, pairs in jobs:
    p = BASE / rel
    s = p.read_text(encoding='utf-8')
    report = []
    for old, new in pairs:
        n = s.count(old)
        s = s.replace(old, new)
        report.append(f"{old!r}x{n}")
    p.write_text(s, encoding='utf-8')
    print(f"{rel}: {', '.join(report)}")
