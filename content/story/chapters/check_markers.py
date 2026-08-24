with open('chapter-arc6-01.md', 'r') as f:
    lines = f.readlines()

markers = ['DRAFT-', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-', 'SCAFFOLD', 'PLANNING', 'DUP-', 'CORRECTIONS-', 'Humman', 'King']
for marker in markers:
    for i, line in enumerate(lines):
        if marker in line:
            print(f'{marker} at line {i+1}: {line.strip()[:100]}')