with open('chapter-arc6-03.md', 'r') as f:
    content = f.read()

# Arc6-03 debris patterns from regions.json descriptions
patterns = [
    ("L123", "After the meeting ajani goes down to the inner chamber"),
    ("L352", "promoting these four to two star generals"),
    ("L486", "Let's look at the immediate aftermath"),
    ("L489", "We are in the gardens, Cefiro tells Ajani"),
    ("L585", "Three days pass, lira has been much more overt"),
    ("L672", "We are in the throne room the very next day"),
    ("L779-790", "The chapter is working on all three fronts"),
    ("L895", "You can write the next scene"),
    ("L898", "Seris goes to report to ajani"),
    ("L948-990", "You are here again. You have questions. Ask."),
    ("L1089", "Few more days pass two weeks have passed"),
]

# Actually let me search for the exact debris content from regions_dump.txt for arc6-03
# The regions_dump shows arc6-03 has debris lines: 123, 352, 486, 489, 585, 672, 779-790, 895, 898, 948-990, 1089
# But those are the same descriptions as arc6-02! Let me search by actual content.

lines = content.splitlines(keepends=True)
print(f"Arc6-03 total lines: {len(lines)}")

# Search for asterisk lines
print("\n=== Asterisk lines ===")
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('*') and not stripped.startswith('**'):
        print(f"Line {i+1}: {stripped[:120]}")

# Search for DRAFT, DIRECTIVE, SYNOPSIS, CRAFT, DUP markers
print("\n=== Debris markers ===")
markers = ['DRAFT-', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-', 'SCAFFOLD', 'PLANNING', 'DUP-', 'CORRECTIONS-']
for marker in markers:
    for i, line in enumerate(lines):
        if marker in line:
            print(f"  {marker} at line {i+1}: {line.strip()[:100]}")

# Search for key debris phrases
print("\n=== Key debris phrases ===")
key_phrases = [
    'After the meeting ajani goes down',
    'promoting these four to two star generals',
    'Let\'s look at the immediate aftermath',
    'We are in the gardens, Cefiro tells Ajani',
    'Three days pass, lira has been much more overt',
    'We are in the throne room the very next day',
    'The chapter is working on all three fronts',
    'You can write the next scene',
    'Seris goes to report to ajani',
    'You are here again. You have questions. Ask.',
    'Few more days pass two weeks have passed',
]
for phrase in key_phrases:
    for i, line in enumerate(lines):
        if phrase in line:
            print(f"  '{phrase[:50]}' at line {i+1}: {line.strip()[:120]}")