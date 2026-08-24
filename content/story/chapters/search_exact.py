with open('chapter-arc6-01.md.bak', 'r') as f:
    content = f.read()

# Exact debris content from regions_dump.txt (key identifying substrings)
debris_patterns = [
    ("L123", 'Next scene beats >When all have said their piece Lira speaks angrily pointing at Cefiro'),
    ("L197", 'well now that\'s out of the way, I need the talky, M\'rak'),
    ("L313", 'hmm the council worked as designed I\'ll need to reward them'),
    ("L439", 'The next scene is a couple of hours after ajani is sitting on the throne'),
    ("L443", 'so these are the ones\' - "So you are the ones who unleashed Velarius madness'),
    ("L485", 'Ambassador these are your people, deal with them as you see fit, I don\'t want more blood'),
    ("L810", 'Let\'s follow the rest of the cast how is the city doing after the battle'),
    ("L905", 'Now let\'s see Yvaria, Reva, lira and vex'),
    ("L963", 'its worse than I thought \' - "call for Maren please"'),
    ("L1042", 'theyre brutes, brutes !\' - "Generals I meant from Verdantis'),
]

import re
lines = content.splitlines(keepends=True)

for label, pattern in debris_patterns:
    found = False
    for i, line in enumerate(lines):
        if pattern in line:
            print(f"{label} FOUND at line {i+1}: {line.strip()[:150]}")
            found = True
            break
    if not found:
        # Try case-insensitive
        for i, line in enumerate(lines):
            if pattern.lower() in line.lower():
                print(f"{label} FOUND (ci) at line {i+1}: {line.strip()[:150]}")
                found = True
                break
    if not found:
        print(f"{label} NOT FOUND")

# Also search for speech-line containing these patterns
print("\n=== Search in all lines for key phrases ===")
key_phrases = [
    'Next scene beats',
    'well now that\'s out of the way',
    'hmm the council worked as designed',
    'so these are the ones',
    'Ambassador these are your people',
    'its worse than I thought',
    'theyre brutes, brutes',
]
for phrase in key_phrases:
    for i, line in enumerate(lines):
        if phrase in line:
            print(f"  '{phrase}' at line {i+1}: {line.strip()[:150]}")