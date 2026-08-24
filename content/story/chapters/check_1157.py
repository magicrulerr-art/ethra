with open('chapter-arc6-05.md', 'r') as f:
    lines = f.readlines()

for i in range(1153, 1165):
    if i < len(lines):
        print(f"Line {i+1}: {lines[i].rstrip()}")