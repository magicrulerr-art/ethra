with open('chapter-arc6-04.md', 'r') as f:
    content = f.read()

lines = content.splitlines(keepends=True)
for i, line in enumerate(lines):
    if 'Dinner' in line or 'dinner' in line.lower():
        if 'Ivan' in line or 'Kira' in line or 'Anastasia' in line:
            print(f"Line {i+1}: {line.strip()[:150]}")
    if 'Anastasia' in line:
        print(f"Line {i+1}: {line.strip()[:150]}")