with open('chapter-06.md', 'r') as f:
    lines = f.readlines()

# Find Lira appearances in umbrella
for i, line in enumerate(lines):
    if 'Lira' in line:
        print(f"Line {i+1}: {line.strip()[:150]}")