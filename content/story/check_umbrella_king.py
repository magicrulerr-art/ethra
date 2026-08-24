with open('chapter-06.md', 'r') as f:
    lines = f.readlines()

# Check line 144
if 143 < len(lines):
    line = lines[143]
    print(f"Line 144: {line.strip()}")
    # Find "King"
    import re
    for match in re.finditer(r'\bKing\b(?![a-z])', line):
        print(f"  Match at {match.start()}: '{match.group()}'")
        print(f"  Context: '{line[max(0,match.start()-30):match.end()+30]}'")