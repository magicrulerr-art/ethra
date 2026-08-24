with open(r'content\story\chapters\chapter-arc6-02.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'arc6-02: {len(lines)} lines')
for i, line in enumerate(lines, 1):
    if line.lstrip().startswith('*') and not line.lstrip().startswith('**'):
        print(f'  {i}: {line.rstrip()[:100]}')