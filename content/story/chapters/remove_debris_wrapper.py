#!/usr/bin/env python3
"""
Remove debris dialogue-block wrapper at lines 798-800 (1-based).
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-05.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove lines 798-800 (1-based) -> indices 797-799
start, end = 797, 799
print("Removing:")
for i in range(start, end + 1):
    print(f"  L{i+1}: {lines[i].rstrip()}")

del lines[start:end+1]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nDone. File now has {len(lines)} lines.")

# Verify
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(793, 810):
    if i < len(lines):
        print(f"  L{i+1}: {lines[i].rstrip()}")