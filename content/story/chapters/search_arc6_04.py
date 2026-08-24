with open('chapter-arc6-04.md', 'r') as f:
    content = f.read()

lines = content.splitlines(keepends=True)
print(f"Arc6-04 total lines: {len(lines)}")

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

# Search for key debris phrases from regions_dump
print("\n=== Key debris phrases ===")
key_phrases = [
    'You should not have known them',
    'You are here again. You have questions. Ask.',
    'Before the Wengari. Before the Tyrants.',
    'It was not the Plague. It was not the creature.',
    'The shadow you speak of',
    'You killed the thing that came this time',
    'Let us look at the immediate aftermath',
    'Three days pass',
    'We are in the throne room',
    'The chapter is working',
    'You can write the next scene',
    'Seris goes to report',
    'Few more days pass',
    'two weeks have passed',
]
for phrase in key_phrases:
    for i, line in enumerate(lines):
        if phrase in line:
            print(f"  '{phrase[:50]}' at line {i+1}: {line.strip()[:120]}")