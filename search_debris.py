with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for the specific debris content described in regions.json
search_terms = [
    "Next scene beats",
    "well now that's out of the way",
    "well that's understandable, he is odd",
    "hmm the council worked as designed",
    "The next scene is a couple of hours after ajani",
    "so these are the ones",
    "Ambassador these are your people",
    "Let's follow the rest of the cast",
    "Now let's see Yvaria, Reva, lira and vex",
    "its worse than I thought",
    "theyre brutes, brutes"
]

for term in search_terms:
    idx = content.find(term)
    if idx >= 0:
        # Find line number
        line_num = content[:idx].count('\n') + 1
        # Show context
        start = max(0, idx - 50)
        end = min(len(content), idx + len(term) + 50)
        print(f'Found "{term}" at line {line_num}:')
        print(f'  ...{content[start:end]}...')
        print()
    else:
        print(f'NOT FOUND: "{term}"')
        print()