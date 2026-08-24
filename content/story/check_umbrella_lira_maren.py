with open('chapter-06.md', 'r') as f:
    content = f.read()

lines = content.splitlines(keepends=True)
for i, line in enumerate(lines):
    if 'Lira' in line and 'Maren' in line:
        print(f"Line {i+1}: {line.strip()[:150]}")
    if ('Lira' in line or 'Maren' in line) and ('sibling' in line.lower() or 'friction' in line.lower() or 'argu' in line.lower()):
        print(f"Line {i+1}: {line.strip()[:150]}")