import io, glob
for f in sorted(glob.glob('content/story/chapters/*.md')):
    t = io.open(f, encoding='utf-8').read()
    if 'Sylara' in t:
        print(f.split('/')[-1], t.count('Sylara'))
