with open('chapter-arc6-01.md', 'r') as f:
    lines = f.readlines()

# Find asterisk lines that are NOT headers (**Header**) and NOT debris
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('*') and not stripped.startswith('**'):
        print(f"Line {i+1}: {stripped[:150]}")