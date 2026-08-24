with open('chapter-arc6-04.md', 'r') as f:
    lines = f.readlines()

# Check the converted blocks
for i in range(523, 538):
    if i < len(lines):
        print(f"Line {i+1}: {lines[i].rstrip()}")