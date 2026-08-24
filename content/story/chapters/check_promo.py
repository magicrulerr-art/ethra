with open('chapter-arc6-02.md', 'r') as f:
    content = f.read()

# Search for promotion speech
lines = content.splitlines(keepends=True)
for i, line in enumerate(lines):
    if 'promot' in line.lower() and ('general' in line.lower() or 'legion' in line.lower() or 'two star' in line.lower()):
        print(f"Line {i+1}: {line.strip()[:150]}")

# Also check arc6-01 for promotion speech
with open('chapter-arc6-01.md', 'r') as f:
    content1 = f.read()
lines1 = content1.splitlines(keepends=True)
print("\n=== Arc6-01 promotion speech ===")
for i, line in enumerate(lines1):
    if 'promot' in line.lower() and ('general' in line.lower() or 'legion' in line.lower() or 'two star' in line.lower()):
        print(f"Line {i+1}: {line.strip()[:150]}")