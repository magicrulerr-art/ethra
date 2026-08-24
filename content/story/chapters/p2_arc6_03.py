#!/usr/bin/env python3
"""
P2 Mechanical Mapping for Arc6-03:
- M1: Humman -> Human (all variants)
- M2: King -> king (standalone)
- M4: debris -> wreckage in 350-400 line band
"""

import re

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-03.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# M1: Humman variants
original = content
content = re.sub(r'\bHumman\b', 'Human', content)
content = re.sub(r'\bHummans\b', 'Humans', content)
content = re.sub(r'\bHumman\'s\b', "Human's", content)
content = re.sub(r'\bHumman-', 'Human-', content)
m1_count = len(re.findall(r'\bHumman\b', original)) + len(re.findall(r'\bHummans\b', original))
print(f"M1: ~{m1_count} Humman replacements")

# M2: standalone King -> king
king_matches = list(re.finditer(r'\bKing\b(?![a-z])', content))
m2_count = 0
for match in king_matches:
    context = content[max(0, match.start()-20):match.end()+20]
    if 'Ice King' not in context and 'Shadow King' not in context:
        m2_count += 1
print(f"M2: {m2_count} standalone King to fix")

def replace_king(match):
    context = content[max(0, match.start()-20):match.end()+20]
    if 'Ice King' in context or 'Shadow King' in context:
        return match.group(0)
    return 'king'

content = re.sub(r'\bKing\b(?![a-z])', replace_king, content)

# M4: debris -> wreckage in 350-400
lines = content.splitlines(keepends=True)
m4_count = 0
for i in range(349, min(400, len(lines))):
    if 'debris' in lines[i].lower():
        print(f"  M4 line {i+1}: {lines[i].strip()[:100]}")
        lines[i] = re.sub(r'\bdebris\b', 'wreckage', lines[i], flags=re.IGNORECASE)
        m4_count += 1
print(f"M4: {m4_count} debris replacements")

content = ''.join(lines)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("P2 complete.")