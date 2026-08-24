#!/usr/bin/env python3
"""
Remove 6 bare asterisk debris lines from Arc6-03.
Lines: 75, 434, 556, 561, 610, 1047 (1-based)
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-03.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

debris_lines = [75, 434, 556, 561, 610, 1047]
debris_0based = [l - 1 for l in debris_lines]

# Verify
for idx in debris_0based:
    if idx < len(lines):
        print(f"Removing line {idx+1}: {lines[idx].strip()[:100]}")

# Remove from bottom up
for idx in sorted(debris_0based, reverse=True):
    del lines[idx]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nDone. File now has {len(lines)} lines.")