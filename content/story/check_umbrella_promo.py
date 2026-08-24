with open('chapter-06.md', 'r') as f:
    content = f.read()

import re
lines = content.splitlines(keepends=True)
for i, line in enumerate(lines):
    if 'promot' in line.lower() and ('two star' in line.lower() or 'legion' in line.lower() or 'four to' in line.lower()):
        print(f"Line {i+1}: {line.strip()[:200]}")