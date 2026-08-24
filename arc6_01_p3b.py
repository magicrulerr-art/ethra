with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# P3b: J3 thought unification
# Find all *text* patterns that are not **bold** and not inside HTML tags
import re

# First, let's find all asterisk-wrapped content
pattern = re.compile(r'(?<!\*)\*([^*\n]+)\*(?!\*)')
matches = list(pattern.finditer(content))
print("Found {} asterisk-wrapped patterns:".format(len(matches)))
for m in matches:
    start = max(0, m.start()-40)
    end = min(len(content), m.end()+40)
    line_num = content[:m.start()].count('\n')+1
    print("  Line {}: ...{}...".format(line_num, content[start:end]))

# Also check for the umbrella target lines mentioned in the order:
# U L1270, L1993, L2004, L2010, L2018, L2032, L2048, L2059, L2065, L2073, L2079, L2085
# These are umbrella line numbers, but might correspond to content in splits