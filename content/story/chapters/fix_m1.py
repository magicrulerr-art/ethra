#!/usr/bin/env python3
"""
Fix M1: Replace all Humman variants (Humman, Hummans, Humman's) with Human variants.
"""

import re

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all variants
# Humman -> Human
# Hummans -> Humans
# Humman's -> Human's
# Humman- -> Human- (if any)

original = content
content = re.sub(r'\bHumman\b', 'Human', content)
content = re.sub(r'\bHummans\b', 'Humans', content)
content = re.sub(r'\bHumman\'s\b', "Human's", content)
content = re.sub(r'\bHumman-', 'Human-', content)

if content != original:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replacements made.")
else:
    print("No changes needed.")

# Verify
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

humman_found = []
for i, line in enumerate(lines):
    if 'Humman' in line:
        humman_found.append((i+1, line.strip()[:100]))

if humman_found:
    print(f"Remaining Humman ({len(humman_found)}):")
    for ln, txt in humman_found:
        print(f"  Line {ln}: {txt}")
else:
    print("PASS: No 'Humman' variants remain")