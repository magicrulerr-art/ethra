with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for asterisk-wrapped directive/beat lines
import re
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    # Look for lines that start with * and contain directive/beat language
    if line.lstrip().startswith('*') and any(kw in line.lower() for kw in ['let', 'next scene', 'follow', 'see yvaria', 'brutes', 'worse', 'council worked']):
        print(f'{i}: {line.rstrip()}')