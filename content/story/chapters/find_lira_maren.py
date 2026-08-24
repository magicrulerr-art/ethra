with open('chapter-arc6-03.md', 'r') as f:
    lines = f.readlines()

# Find all Lira and Maren appearances
for i, line in enumerate(lines):
    if 'Lira' in line or 'Maren' in line:
        print(f"Line {i+1}: {line.strip()[:150]}")