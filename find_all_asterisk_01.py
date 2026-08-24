with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find all lines with *...* pattern (not **bold**)
import re
for i, line in enumerate(lines, 1):
    # Look for asterisk-wrapped content that's not markdown bold
    matches = re.finditer(r'(?<!\*)\*([^*\n]+)\*(?!\*)', line)
    for m in matches:
        print(f'{i}: {line.rstrip()}')
        break