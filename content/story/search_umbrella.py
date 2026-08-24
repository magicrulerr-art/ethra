with open('chapter-06.md', 'r') as f:
    content = f.read()

# Search for debris patterns in umbrella
debris_patterns = [
    "Next scene beats >When all have said their piece Lira speaks angrily",
    "well now that's out of the way, I need the talky, M'rak",
    "hmm the council worked as designed I'll need to reward them",
    "The next scene is a couple of hours after ajani is sitting on the throne",
    "so these are the ones' - \"So you are the ones who unleashed Velarius madness",
    "Ambassador these are your people, deal with them as you see fit, I don't want more blood",
    "Let's follow the rest of the cast how is the city doing after the battle",
    "Now let's see Yvaria, Reva, lira and vex",
    "its worse than I thought ' - \"call for Maren please\"",
    "theyre brutes, brutes !' - \"Generals I meant from Verdantis",
]

lines = content.splitlines(keepends=True)
print(f"Umbrella total lines: {len(lines)}")

for pattern in debris_patterns:
    found = False
    for i, line in enumerate(lines):
        if pattern in line:
            print(f"FOUND at line {i+1}: {line.strip()[:150]}")
            found = True
            break
    if not found:
        for i, line in enumerate(lines):
            if pattern.lower() in line.lower():
                print(f"FOUND (ci) at line {i+1}: {line.strip()[:150]}")
                found = True
                break
    if not found:
        print(f"NOT FOUND: {pattern[:60]}...")

# Search for asterisk lines
print("\n=== Asterisk lines in umbrella ===")
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('*') and not stripped.startswith('**'):
        print(f"Line {i+1}: {stripped[:150]}")