#!/usr/bin/env python3
"""
Remove debris line 342 from Arc6-05.
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-05.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

idx = 341  # 0-based
if idx < len(lines):
    print(f"Removing line 342: {lines[idx].strip()[:100]}")
    del lines[idx]
else:
    print("Line out of bounds")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Done. File now has {len(lines)} lines.")