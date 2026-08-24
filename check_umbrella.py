with open(r'content\story\chapter-06.md', 'r', encoding='utf-8') as f:
    content = f.read()
print('Humman count:', content.count('Humman'))
print('Human count:', content.count('Human'))
print('King count:', content.count('King'))
print('king count:', content.count('king'))