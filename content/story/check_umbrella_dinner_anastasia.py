with open('chapter-06.md', 'r') as f:
    content = f.read()

# Search for Dinner V2 / Anastasia V3
import re
lines = content.splitlines(keepends=True)
for i, line in enumerate(lines):
    if 'Dinner V2' in line or 'Anastasia V3' in line or 'dinner' in line.lower() and 'ivan' in line.lower() and 'kira' in line.lower():
        print(f"Line {i+1}: {line.strip()[:200]}")
    if 'Anastasia' in line and ('armor' in line.lower() or 'craft' in line.lower() or 'protection' in line.lower()):
        print(f"Line {i+1}: {line.strip()[:200]}")