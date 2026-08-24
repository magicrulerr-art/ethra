with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Search for lines that start with * but are not markdown headers (**)
for i, line in enumerate(lines, 1):
    stripped = line.lstrip()
    if stripped.startswith('*') and not stripped.startswith('**'):
        print(f'{i}: {line.rstrip()}')