with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for all the debris patterns from regions.json descriptions
search_terms = [
    "well that's understandable, he is odd",
    "hmm the council worked as designed",
    "The next scene is a couple of hours after ajani",
    "so these are the ones",
    "Ambassador these are your people",
    "Let's follow the rest of the cast",
    "Now let's see Yvaria, Reva, lira and vex",
    "its worse than I thought",
    "theyre brutes, brutes",
    "Next scene beats",
    "well now that's out of the way"
]

for term in search_terms:
    idx = content.find(term)
    if idx >= 0:
        line_num = content[:idx].count('\n') + 1
        start = max(0, idx - 100)
        end = min(len(content), idx + len(term) + 200)
        print(f'Found "{term}" at line {line_num}:')
        print(f'  Context: {content[start:end]}')
        print()
    else:
        print(f'NOT FOUND: "{term}"')
        print()