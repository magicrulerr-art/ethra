with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()
print('Humman:', content.count('Humman'))
print('Human:', content.count('Human'))