with open('chapter-arc6-05.md', 'r') as f:
    content = f.read()

# Search for Tamsin Golden Claw
import re
lines = content.splitlines(keepends=True)
for i, line in enumerate(lines):
    if 'Tamsin' in line and ('Golden' in line or 'Claw' in line or 'golden' in line.lower() or 'claw' in line.lower()):
        print(f"Tamsin line {i+1}: {line.strip()[:150]}")
    if 'Nikolai' in line and ('laugh' in line.lower() or 'laughed' in line.lower()):
        print(f"Nikolai laugh line {i+1}: {line.strip()[:150]}")