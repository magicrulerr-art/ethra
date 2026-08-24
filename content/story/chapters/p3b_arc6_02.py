#!/usr/bin/env python3
"""
P3b: Convert asterisk-thoughts to single quotes in Arc6-02.
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-02.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Convert *text* to 'text' for narrative asterisk lines (not headers **)
# Pattern: lines that are entirely *... (with optional whitespace)
import re

def replace_asterisk_thoughts(match):
    line = match.group(0)
    # Don't convert **Header** markdown
    if line.strip().startswith('**'):
        return line
    # Convert *text* to 'text'
    # Handle multiline: * at start of line, * at end of line
    stripped = line.strip()
    if stripped.startswith('*') and stripped.endswith('*') and not stripped.startswith('**'):
        # Single line asterisk thought
        inner = stripped[1:-1]
        return line.replace(stripped, f"'{inner}'")
    return line

# Process line by line
lines = content.splitlines(keepends=True)
new_lines = []
count = 0
for line in lines:
    stripped = line.strip()
    if stripped.startswith('*') and stripped.endswith('*') and not stripped.startswith('**'):
        inner = stripped[1:-1]
        # Preserve leading/trailing whitespace
        leading = line[:len(line) - len(line.lstrip())]
        trailing = line[len(line.rstrip()):]
        new_line = leading + f"'{inner}'" + trailing
        new_lines.append(new_line)
        print(f"Converted: {stripped[:80]} -> '{inner[:80]}'")
        count += 1
    else:
        new_lines.append(line)

content = ''.join(new_lines)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nConverted {count} asterisk-thoughts to single quotes.")