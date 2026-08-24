with open('chapter-arc6-04.md', 'r') as f:
    lines = f.readlines()

for i in range(523, 540):
    if i < len(lines):
        print(f"Line {i+1}: {lines[i].rstrip()}")