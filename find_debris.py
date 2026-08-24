with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if any(marker in line for marker in ['DRAFT-BEAT', 'DRAFT-LINE', 'DRAFT-HYBRID', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-BLOCK', 'SCAFFOLD-BLOCK', 'PLANNING-BLOCK', 'DUP-', 'CORRECTIONS-']):
        print(f'{i}: {line.rstrip()}')