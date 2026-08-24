#!/usr/bin/env python3
"""
Remove debris asterisk lines from Arc6-04, convert golden text asterisk lines to single quotes.
Debris: 146, 315, 1101
Golden text (convert * to '): 528, 536
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-04.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# First, convert golden text lines (528, 536) from *text* to 'text'
golden_indices = [527, 535]  # 0-based
for idx in golden_indices:
    if idx < len(lines):
        stripped = lines[idx].strip()
        if stripped.startswith('*') and stripped.endswith('*'):
            inner = stripped[1:-1]
            leading = lines[idx][:len(lines[idx]) - len(lines[idx].lstrip())]
            trailing = lines[idx][len(lines[idx].rstrip()):]
            lines[idx] = leading + f"'{inner}'" + trailing
            print(f"Converted golden text line {idx+1}: '{inner[:80]}'")

# Then remove debris lines (146, 315, 1101) - adjust for 0-based and line shifts
# Since we're not adding/removing lines yet, indices are still valid
debris_indices = [145, 314, 1100]  # 0-based
for idx in sorted(debris_indices, reverse=True):
    if idx < len(lines):
        print(f"Removing debris line {idx+1}: {lines[idx].strip()[:100]}")
        del lines[idx]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nDone. File now has {len(lines)} lines.")