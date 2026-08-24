with open('chapter-arc6-02.md', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('*') and not stripped.startswith('**'):
        print(f"Line {i+1}: {stripped[:150]}")