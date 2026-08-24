with open('chapter-arc6-04.md', 'r') as f:
    lines = f.readlines()

# Check around line 525-530
for i in range(520, 540):
    if i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith('*') or 'saber' in stripped.lower() or 'tide wolf' in stripped.lower():
            print(f"Line {i+1}: {stripped[:150]}")