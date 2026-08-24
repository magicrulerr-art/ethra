for fname in ['chapter-arc6-02.md', 'chapter-arc6-03.md', 'chapter-arc6-04.md', 'chapter-arc6-05.md']:
    with open(f'content\\story\\chapters\\{fname}', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'=== {fname} ===')
    for i, line in enumerate(lines, 1):
        if any(marker in line for marker in ['DRAFT-', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-BLOCK', 'SCAFFOLD-BLOCK', 'PLANNING-BLOCK', 'DUP-', 'CORRECTIONS-']):
            print(f'  {i}: {line.rstrip()}')