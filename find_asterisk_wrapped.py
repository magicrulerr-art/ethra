with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Search for lines containing asterisk-wrapped content *...*
import re
for i, line in enumerate(lines, 1):
    # Look for *text* pattern (not **bold**)
    if re.search(r'(?<!\*)\*[^*]+\*(?!\*)', line):
        print(f'{i}: {line.rstrip()}')