with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Search for debris patterns
debris_patterns = ['*Let', '*You can', 'DRAFT-', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-BLOCK', 'SCAFFOLD-BLOCK', 'PLANNING-BLOCK', 'DUP-', 'CORRECTIONS-', 'DRAFT-BEAT', 'DRAFT-LINE', 'DRAFT-HYBRID', 'DRAFT-CITATION', 'DRAFT-PROCLAMATION']
for i, line in enumerate(lines, 1):
    for pattern in debris_patterns:
        if pattern in line:
            print(f'{i}: {line.rstrip()}')
            break