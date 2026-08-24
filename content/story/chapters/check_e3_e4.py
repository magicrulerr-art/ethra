with open('chapter-arc6-03.md', 'r') as f:
    content = f.read()

# Search for L'vat tour / chiding / city tour
import re
lines = content.splitlines(keepends=True)
for i, line in enumerate(lines):
    if 'L\'vat' in line or "l'vat" in line:
        if 'tour' in line.lower() or 'chid' in line.lower() or 'city' in line.lower():
            print(f"Line {i+1}: {line.strip()[:150]}")

print("\n=== Lira-Maren ===")
for i, line in enumerate(lines):
    if ('Lira' in line or 'Maren' in line) and ('sibling' in line.lower() or 'friction' in line.lower() or 'argu' in line.lower()):
        print(f"Line {i+1}: {line.strip()[:150]}")

# Also check for "Lira" and "Maren" together
print("\n=== Lira & Maren together ===")
for i, line in enumerate(lines):
    if 'Lira' in line and 'Maren' in line:
        print(f"Line {i+1}: {line.strip()[:150]}")