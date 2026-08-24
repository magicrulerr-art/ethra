with open('chapter-arc6-01.md', 'r') as f:
    lines = f.readlines()

# Check for "King" (uppercase) that should be "king"
for i, line in enumerate(lines):
    if 'King' in line and 'Ice King' not in line and 'Shadow King' not in line and 'king' not in line.lower().replace('ice king', '').replace('shadow king', ''):
        # Simple check - look for standalone King
        import re
        if re.search(r'\bKing\b(?![a-z])', line):
            print(f'King at line {i+1}: {line.strip()[:120]}')