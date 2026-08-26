# -*- coding: utf-8 -*-
"""Refresh the chapter SHA-256 integrity baseline (chapters legitimately
changed since 08-24: Styxiancus retcon, D5 Humman-case normalization,
Motted ratification in arc5-11 Cefiro line)."""
import hashlib, glob, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
lines = []
for f in sorted(glob.glob(str(BASE / 'content/story/chapters/chapter-arc*.md'))):
    h = hashlib.sha256(open(f, 'rb').read()).hexdigest().upper()
    lines.append(f"{h}  {pathlib.Path(f).name}")
out = BASE / 'QA/chapter_hashes_baseline_2026-08-25.txt'
out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f"{len(lines)} hashes written to {out.name}")
