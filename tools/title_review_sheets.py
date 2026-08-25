# -*- coding: utf-8 -*-
"""Contact sheets for the title-band rollout crop review.
Reads the 32 source images, writes labeled sheets to the workspace root
(not the served tree)."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # ethra_site
WS = os.path.dirname(BASE)  # workspace root

SOURCES = [
    (1,  'arc1-ch01', 'static/images/chapter-arc1-01-v3.png'),
    (2,  'arc1-03dv3', 'archive/images-of-ethra/chapter-arc1-03-v3.png'),
    (3,  'arc1-ch04', 'static/images/chapter-arc1-04-v2.png'),
    (4,  'arc1-ch05', 'static/images/chapter-arc1-05.png'),
    (5,  'arc1-ch06', 'static/images/chapter-arc1-06-v2.png'),
    (6,  'arc2-ch01', 'static/images/chapter-arc2-01-v3.png'),
    (7,  'arc2-ch02', 'static/images/chapter-arc2-02.png'),
    (8,  'arc2-ch03', 'static/images/chapter-arc2-03.png'),
    (9,  'arc2-04dv5', 'archive/images-of-ethra/chapter-arc2-04-v5.png'),
    (10, 'arc2-05dv6', 'archive/images-of-ethra/chapter-arc2-05-v6.png'),
    (11, 'arc2-ch06', 'static/images/chapter-arc2-06.png'),
    (12, 'arc3-ch01', 'static/images/chapter-arc3-01-v4.png'),
    (13, 'arc3-ch02', 'static/images/chapter-arc3-02.png'),
    (14, 'arc3-03dv3', 'archive/images-of-ethra/chapter-arc3-03-v3.png'),
    (15, 'arc3-ch04', 'static/images/chapter-arc3-04.png'),
    (16, 'arc3-ch05', 'static/images/chapter-arc3-05.png'),
    (17, 'arc4-ch01', 'static/images/chapter-arc4-01-v6.png'),
    (18, 'arc4-ch02', 'static/images/chapter-arc4-02.png'),
    (19, 'arc4-ch03', 'static/images/chapter-arc4-03.png'),
    (20, 'arc4-ch04', 'static/images/chapter-arc4-04-v3.png'),
    (21, 'arc4-ch06', 'static/images/chapter-arc4-06-v5.png'),
    (22, 'arc5-ch01', 'static/images/chapter-arc5-01-v3.png'),
    (23, 'arc5-ch05', 'static/images/chapter-arc5-05-v2.png'),
    (24, 'arc5-11dv101', 'archive/images-of-ethra/chapter-arc5-11-v101.png'),
    (25, 'arc5-ch19', 'static/images/chapter-arc5-19-v5.png'),
    (26, 'arc5-ch22', 'static/images/chapter-arc5-22-v7.png'),
    (27, 'arc6-01dv4', 'archive/images-of-ethra/chapter-arc6-01-v4.png'),
    (28, 'arc6-ch02', 'static/images/chapter-arc6-02-v3.png'),
    (29, 'arc6-03dv2', 'archive/images-of-ethra/chapter-arc6-03-v2.png'),
    (30, 'arc6-ch04', 'static/images/chapter-arc6-04-v2.png'),
    (31, 'arc6-ch05', 'static/images/chapter-arc6-05-v1.png'),
    (32, 'arc7-01dv3', 'archive/images-of-ethra/chapter-arc7-01-v3.png'),
]

COLS, ROWS = 4, 3
TW, TH = 420, 420      # thumbnail cell
LABEL_H = 30
PAD = 6

def get_font(size):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()

def main():
    font = get_font(22)
    sheets = [SOURCES[i:i + COLS * ROWS] for i in range(0, len(SOURCES), COLS * ROWS)]
    for si, sheet in enumerate(sheets, 1):
        W = COLS * (TW + PAD) + PAD
        H = ROWS * (TH + LABEL_H + PAD) + PAD
        canvas = Image.new('RGB', (W, H), (8, 12, 20))
        d = ImageDraw.Draw(canvas)
        for j, (idx, cid, rel) in enumerate(sheet):
            r, c = divmod(j, COLS)
            x = PAD + c * (TW + PAD)
            y = PAD + r * (TH + LABEL_H + PAD)
            d.rectangle([x, y, x + TW, y + LABEL_H], fill=(0, 0, 0))
            d.text((x + 8, y + 3), f'{idx:02d} {cid}', fill=(240, 208, 128), font=font)
            src = os.path.join(BASE, rel)
            if not os.path.exists(src):
                d.text((x + 8, y + LABEL_H + 20), 'MISSING: ' + rel, fill=(255, 80, 80), font=font)
                continue
            im = Image.open(src).convert('RGB')
            im.thumbnail((TW, TH), Image.LANCZOS)
            canvas.paste(im, (x, y + LABEL_H))
            d.rectangle([x, y + LABEL_H, x + TW, y + LABEL_H + TH], outline=(60, 70, 90))
        out = os.path.join(WS, f'title_review_sheet{si}.jpg')
        canvas.save(out, quality=88)
        print('wrote', out, canvas.size)

if __name__ == '__main__':
    main()
