with open('chapter-arc6-01.md.bak', 'r') as f:
    content = f.read()

# Search for each debris pattern from regions.json descriptions
patterns = [
    ("L123", r'Next scene beats >When all have said their piece Lira speaks angrily'),
    ("L197", r'well now that\'s out of the way, I need the talky, M\'rak'),
    ("L313", r'hmm the council worked as designed I\'ll need to reward them'),
    ("L439", r'\*The next scene is a couple of hours after ajani is sitting on the throne'),
    ("L443", r'\'so these are the ones\' - "So you are the ones who unleashed'),
    ("L485", r'Ambassador these are your people, deal with them as you see fit'),
    ("L810", r'\*Let\'s follow the rest of the cast how is the city doing after the battle'),
    ("L905", r'\*Now let\'s see Yvaria, Reva, lira and vex\*'),
    ("L963", r'\'its worse than I thought \' - "call for Maren please"'),
    ("L1042", r'\'theyre brutes, brutes !\' - "Generals I meant from Verdantis'),
]

import re
lines = content.splitlines(keepends=True)

for label, pattern in patterns:
    found = False
    for i, line in enumerate(lines):
        if re.search(pattern, line):
            print(f"{label} FOUND at line {i+1}: {line.strip()[:120]}")
            found = True
            break
    if not found:
        # Try case-insensitive
        for i, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                print(f"{label} FOUND (ci) at line {i+1}: {line.strip()[:120]}")
                found = True
                break
    if not found:
        print(f"{label} NOT FOUND")

# Also search for any lines containing asterisk-directives or DRAFT- markers
print("\n=== All asterisk lines in backup ===")
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('*') and not stripped.startswith('**'):
        print(f"Line {i+1}: {stripped[:120]}")

# Search for DRAFT, DIRECTIVE, SYNOPSIS, CRAFT, SCAFFOLD, PLANNING, DUP, CORRECTIONS
print("\n=== Debris markers in backup ===")
markers = ['DRAFT-', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-', 'SCAFFOLD', 'PLANNING', 'DUP-', 'CORRECTIONS-']
for marker in markers:
    for i, line in enumerate(lines):
        if marker in line:
            print(f"  {marker} at line {i+1}: {line.strip()[:100]}")