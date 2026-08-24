with open('chapter-arc6-02.md', 'r') as f:
    content = f.read()

lines = content.splitlines(keepends=True)
# Search for Ajani giving promotions
for i, line in enumerate(lines):
    if 'promot' in line.lower() and ('ajani' in line.lower() or 'i am' in line.lower() or 'your highness' in line.lower()):
        print(f"Line {i+1}: {line.strip()[:150]}")

# Also check for "two star" or "legion" spoken by Ajani
print("\n=== Ajani speech lines ===")
for i, line in enumerate(lines):
    if '<p class="speech-line">' in line and ('ajani' in content[max(0,content.find(line)-200):content.find(line)].lower() or 'Your Highness' in line or 'I am' in line):
        if 'promot' in line.lower() or 'general' in line.lower() or 'legion' in line.lower():
            print(f"Line {i+1}: {line.strip()[:150]}")