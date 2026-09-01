import io, re
for f in ['content/story/chapter-03.md','content/story/chapter-04.md','content/story/chapter-05.md','content/story/chapter-06.md']:
    t = io.open(f, encoding='utf-8').read()
    print(f.split('/')[-1],
          '| wine:', len(re.findall(r'(?i)\bwine\b', t)),
          '| vineyard:', len(re.findall(r'(?i)vineyard', t)),
          '| humman-king:', len(re.findall(r'(?i)humman\s+king', t)),
          '| king-of-hummans:', len(re.findall(r'(?i)king of the hummans', t)),
          '| Humman-Sultan:', len(re.findall(r'Humman Sultan', t)),
          '| Bitter-Ale:', t.count('Bitter Ale'),
          '| rune-berry:', len(re.findall(r'(?i)rune berry', t)),
          '| Sultans:', len(re.findall(r'Sultans', t)))
