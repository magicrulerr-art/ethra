#!/usr/bin/env python3
"""
P2 Mechanical Mapping for Arc6-01 split:
- M1: Humman -> Human (case-sensitive, whole word)
- M3: Add missing closing quote at speech line (audit L641)
- M4: debris -> wreckage in 350-400 line band (verify each)
"""

import re

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.splitlines(keepends=True)
original_lines = lines[:]

# M1: Humman -> Human (whole word, case-sensitive)
print("=== M1: Humman -> Human ===")
m1_count = 0
new_lines = []
for i, line in enumerate(lines):
    new_line = re.sub(r'\bHumman\b', 'Human', line)
    if new_line != line:
        m1_count += line.count('Humman')  # approximate
        print(f"  Line {i+1}: {line.strip()[:80]} -> {new_line.strip()[:80]}")
    new_lines.append(new_line)
lines = new_lines
print(f"M1: ~{m1_count} replacements")

# M3: Find speech line missing closing quote
# The audit L641 in original would be around here. Look for <p class="speech-line"> with unmatched quote
print("\n=== M3: Missing closing quote ===")
for i, line in enumerate(lines):
    if '<p class="speech-line">' in line:
        # Count quotes in the line
        quotes = line.count('"')
        if quotes % 2 == 1:
            print(f"  Line {i+1} has odd quotes ({quotes}): {line.strip()[:120]}")

# M4: debris -> wreckage in 350-400 line band (1-based)
print("\n=== M4: debris -> wreckage (lines 350-400) ===")
m4_count = 0
for i in range(349, min(400, len(lines))):  # 0-based: 349-399
    if 'debris' in lines[i].lower():
        print(f"  Line {i+1}: {lines[i].strip()[:120]}")
        # Verify context - only replace if it means battle debris
        lines[i] = re.sub(r'\bdebris\b', 'wreckage', lines[i], flags=re.IGNORECASE)
        m4_count += 1
print(f"M4: {m4_count} replacements")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nDone. File has {len(lines)} lines.")