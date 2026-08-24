with open('chapter-arc6-05.md', 'r') as f:
    lines = f.readlines()

# Check line 799 and surrounding
for i in range(795, 810):
    if i < len(lines):
        print(f"Line {i+1}: {lines[i].rstrip()}")