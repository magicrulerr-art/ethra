import re

with open('C:/Users/magic_new.BETOS-AIO.000/.qwenpaw/workspaces/default/ethra_site/content/story/chapters/chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

patterns = [
    "well now that's out of the way",
    "hmm the council worked as designed",
    "The next scene is a couple of hours after ajani",
    "so these are the ones",
    "Ambassador these are your people",
    "Let's follow the rest of the cast",
    "Now let's see Yvaria",
    "its worse than I thought",
    "theyre brutes"
]

for pattern in patterns:
    matches = list(re.finditer(pattern, content, re.IGNORECASE))
    for m in matches:
        line_num = content[:m.start()].count('\n') + 1
        print(f'Found "{pattern}" at line ~{line_num}: {m.group()[:80]}')