with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for E1 target
search_terms = [
    "well now that's out of the way",
    "talky",
    "M'rak",
    "out of the way"
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