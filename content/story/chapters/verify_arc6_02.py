with open('chapter-arc6-02.md', 'r') as f:
    content = f.read()

lines = content.splitlines(keepends=True)

print("=== P5 Verification for Arc6-02 ===\n")

# 1. Zero debris markers
markers = ['DRAFT-', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-', 'SCAFFOLD', 'PLANNING', 'DUP-', 'CORRECTIONS-']
print("1. Debris markers:")
found_any = False
for marker in markers:
    for i, line in enumerate(lines):
        if marker in line:
            print(f"  FAIL: {marker} at line {i+1}: {line.strip()[:100]}")
            found_any = True
if not found_any:
    print("  PASS: No debris markers found")

# 2. Zero "Humman" tokens
print("\n2. Humman tokens:")
humman_count = 0
for i, line in enumerate(lines):
    if 'Humman' in line:
        print(f"  FAIL: Humman at line {i+1}: {line.strip()[:100]}")
        humman_count += 1
if humman_count == 0:
    print("  PASS: No 'Humman' tokens")

# 3. Zero standalone "King" 
import re
print("\n3. Standalone King tokens:")
king_count = 0
for i, line in enumerate(lines):
    for match in re.finditer(r'\bKing\b(?![a-z])', line):
        context = line[max(0, match.start()-20):match.end()+20]
        if 'Ice King' not in context and 'Shadow King' not in context:
            print(f"  FAIL: King at line {i+1}: {line.strip()[:100]}")
            king_count += 1
if king_count == 0:
    print("  PASS: No standalone 'King' tokens")

# 4. Quote parity
print("\n4. Quote parity in speech-lines:")
quote_issues = 0
for i, line in enumerate(lines):
    if '<p class="speech-line">' in line:
        quotes = line.count('"')
        if quotes % 2 == 1:
            print(f"  FAIL: Odd quotes ({quotes}) at line {i+1}: {line.strip()[:100]}")
            quote_issues += 1
if quote_issues == 0:
    print("  PASS: All speech-lines have balanced quotes")

# 5. No asterisk-thoughts
print("\n5. Asterisk-thoughts:")
asterisk_count = 0
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('*') and not stripped.startswith('**'):
        print(f"  FAIL: Asterisk line at {i+1}: {stripped[:100]}")
        asterisk_count += 1
if asterisk_count == 0:
    print("  PASS: No asterisk-thoughts")

# 6. Golden text
print("\n6. Golden text presence:")
golden_texts = [
    "Tamsin V2 Golden Claw",
    "Nikolai laugh V2",
    "Dinner V2",
    "L'vat strike V3",
    "Maren report V1+Nikolai splice"
]
for gt in golden_texts:
    if gt in content:
        print(f"  FOUND: {gt}")
    else:
        keywords = gt.split()
        found = any(kw in content for kw in keywords if len(kw) > 3)
        if found:
            print(f"  PARTIAL: {gt} (keywords found)")
        else:
            print(f"  MISSING: {gt}")

print("\n=== Verification Complete ===")