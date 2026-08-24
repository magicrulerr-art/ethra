with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check lines 120-130
for i in range(119, 130):
    print(f'{i+1}: {repr(lines[i])}')