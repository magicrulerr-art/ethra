#!/usr/bin/env python3
"""
Remove the 3 remaining bare asterisk debris lines from chapter-arc6-01.md split.
Lines (1-based) from search: 427, 789, 881
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lines to remove (1-based, convert to 0-based)
# These are bare asterisk lines, not in wrappers
debris_lines_1based = [427, 789, 881]
debris_lines_0based = [l - 1 for l in debris_lines_1based]

# Verify content
for idx in debris_lines_0based:
    if idx < len(lines):
        print(f"Removing line {idx+1}: {lines[idx].strip()[:100]}")
    else:
        print(f"WARNING: Line {idx+1} out of bounds")

# Remove from bottom up
for idx in sorted(debris_lines_0based, reverse=True):
    del lines[idx]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Done. File now has {len(lines)} lines.")