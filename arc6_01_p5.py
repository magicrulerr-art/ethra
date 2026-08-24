with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("=== Arc6-01 P5 Verification ===")
print()

# 1. Zero debris markers
debris_markers = ['*Let\'s', '*You can', 'DRAFT-', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-BLOCK', 'SCAFFOLD-BLOCK', 'PLANNING-BLOCK', 'DUP-', 'CORRECTIONS-']
print("1. Debris markers check:")
for marker in debris_markers:
    count = content.count(marker)
    if count > 0:
        print("  FAIL: '{}' found {} times".format(marker, count))
    else:
        print("  PASS: '{}' not found".format(marker))

# 2. Zero Humman / King (uppercase)
print("\n2. Humman/King check:")
humman_count = content.count('Humman')
king_count = content.count('King')
print("  Humman: {} (target: 0)".format(humman_count))
print("  King: {} (target: 0)".format(king_count))
if humman_count == 0 and king_count == 0:
    print("  PASS")
else:
    print("  FAIL")

# 3. Quote parity: every <p class="speech-line"> has matching "
import re
speech_lines = re.findall(r'<p class="speech-line">([^<]*)</p>', content)
print("\n3. Quote parity check ({} speech lines):".format(len(speech_lines)))
quote_issues = 0
for i, line in enumerate(speech_lines):
    # Count unescaped quotes
    quote_count = line.count('"')
    if quote_count % 2 != 0:
        print("  Line {}: Odd number of quotes ({}): {}".format(i+1, quote_count, line[:80]))
        quote_issues += 1
if quote_issues == 0:
    print("  PASS: All speech lines have balanced quotes")
else:
    print("  FAIL: {} speech lines have unbalanced quotes".format(quote_issues))

# 4. No duplicate blocks (simplified check)
print("\n4. Duplicate block check (simplified):")
# This would need more sophisticated fuzzy matching, skipping for now
print("  SKIP: Requires fuzzy matching implementation")

# 5. All J3 thoughts are single-quoted, no asterisk-thoughts remain
print("\n5. J3 thoughts check:")
asterisk_thoughts = re.findall(r'(?<!\*)\*([^*\n]+)\*(?!\*)', content)
if len(asterisk_thoughts) == 0:
    print("  PASS: No asterisk-thoughts remain")
else:
    print("  FAIL: {} asterisk-thoughts found".format(len(asterisk_thoughts)))
    for t in asterisk_thoughts[:5]:
        print("    - {}".format(t[:80]))

# 6. Golden text present
print("\n6. Golden text check:")
golden_texts = [
    "Tamsin V2 Golden Claw",
    "Nikolai laugh V2",
    "Dinner V2",
    "L'vat strike V3",
    "Maren report V1+Nikolai splice"
]
# These are descriptive names, need to check for actual content
# Let's check for key phrases
key_phrases = {
    "Tamsin V2 Golden Claw": ["Golden Claw", "Tamsin"],
    "Nikolai laugh V2": ["Nikolai", "laugh"],
    "Dinner V2": ["dinner", "Dinner"],
    "L'vat strike V3": ["L'vat", "strike"],
    "Maren report V1+Nikolai splice": ["Maren", "report", "Nikolai"]
}
for name, phrases in key_phrases.items():
    found = all(p in content for p in phrases)
    print("  {}: {}".format(name, "PASS" if found else "FAIL"))

print("\n=== Verification Complete ===")