"""One-shot: move superseded chapter-cover binaries + sidecars into
archive/images-of-ethra (Ainz ruling 2026-08-25: archive+annotate, don't delete)."""
import os, shutil

base = r'C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site'
img = os.path.join(base, 'static', 'images')
arc = os.path.join(base, 'archive', 'images-of-ethra')
os.makedirs(arc, exist_ok=True)

superseded = {
    'chapter-arc1-02': ['v3'],
    'chapter-arc1-03': ['v2', 'v3'],
    'chapter-arc2-04': ['v4', 'v5'],
    'chapter-arc2-05': ['v5', 'v6'],
    'chapter-arc3-01': ['v2', 'v3'],
    'chapter-arc3-03': ['v3'],
    'chapter-arc4-01': ['v2', 'v3', 'v4', 'v5'],
    'chapter-arc4-04': ['v2'],
    'chapter-arc4-05': ['v8'],
    'chapter-arc4-06': ['v4'],
    'chapter-arc5-01': ['v2'],
    'chapter-arc5-11': ['v101'],
    'chapter-arc5-19': ['v4'],
    'chapter-arc5-22': ['v1'],
    'chapter-arc6-01': ['v1', 'v2', 'v3', 'v4'],
    'chapter-arc6-02': ['v1', 'v2'],
    'chapter-arc6-03': ['v1', 'v2'],
}
moved = []
for ch, vers in superseded.items():
    for v in vers:
        for ext in ('png', 'webp', 'jpg'):
            src = os.path.join(img, '%s-%s.%s' % (ch, v, ext))
            if os.path.exists(src):
                shutil.move(src, os.path.join(arc, '%s-%s.%s' % (ch, v, ext)))
                moved.append('%s-%s.%s' % (ch, v, ext))
        sd = os.path.join(img, '%s-%s-PROMPT-RECORD.md' % (ch, v))
        if os.path.exists(sd):
            shutil.move(sd, os.path.join(arc, '%s-%s-PROMPT-RECORD.md' % (ch, v)))
            moved.append('%s-%s-PROMPT-RECORD.md' % (ch, v))

# failed forges of the arc7-01 cave scene this session (never shipped)
media = r'C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\media\qwen_image'
for src, dst in [('qwen_image_gen_0_1787675409658.png', 'chapter-arc7-01-v5.png'),
                 ('qwen_image_gen_0_1787675521093.png', 'chapter-arc7-01-v6.png'),
                 ('qwen_image_gen_0_1787675611450.png', 'chapter-arc7-01-v7.png')]:
    s = os.path.join(media, src)
    if os.path.exists(s):
        shutil.copy(s, os.path.join(arc, dst))
        moved.append(dst + '  [failed forge, copied]')

print('%d files archived' % len(moved))
for m in moved:
    print(' ', m)
