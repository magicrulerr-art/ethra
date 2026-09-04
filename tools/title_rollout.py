# -*- coding: utf-8 -*-
"""title_rollout.py — cut the 32 title-band fragments + emit the CSS block.

Reads the crop table below (normalized rectangles chosen by visual review of
the contact sheets, 2026-08-25), crops each source, auto-widens any crop
narrower than MIN_RATIO so `background: ... / cover` never loses the iconic
element, writes static/images/title-arcN-YY.webp, then emits
tools/title_rollout_css_block.css (the exact CSS the surgical edit splices in)
and an audit contact sheet of the final bands.

Doctrine: relative url() only; ≤0.6 opacity; mask fades toward text;
crops exclude faces and every flagged drift region.
"""
import os
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS = os.path.dirname(BASE)
OUT_DIR = os.path.join(BASE, 'static', 'images')
MIN_RATIO = 1.7
OUT_W = 512

# index: (chapter_id, source_rel, x0, y0, x1, y1)
CROPS = {
    1:  ('arc1-ch01', 'static/images/chapter-arc1-01-v3.png',            0.62, 0.00, 1.00, 0.40),
    2:  ('arc1-ch03', 'archive/images-of-ethra/chapter-arc1-03-v3.png',  0.55, 0.00, 1.00, 0.35),
    3:  ('arc1-ch04', 'static/images/chapter-arc1-04-v2.png',            0.62, 0.05, 1.00, 0.50),
    4:  ('arc1-ch05', 'static/images/chapter-arc1-05.png',               0.60, 0.00, 1.00, 0.45),
    5:  ('arc1-ch06', 'static/images/chapter-arc1-06-v2.png',            0.55, 0.00, 1.00, 0.50),
    6:  ('arc2-ch01', 'static/images/chapter-arc2-01-v3.png',            0.60, 0.15, 1.00, 0.60),
    7:  ('arc2-ch02', 'static/images/chapter-arc2-02.png',               0.30, 0.25, 0.80, 0.70),
    8:  ('arc2-ch03', 'static/images/chapter-arc2-03.png',               0.60, 0.35, 1.00, 0.80),
    9:  ('arc2-ch04', 'archive/images-of-ethra/chapter-arc2-04-v5.png',  0.60, 0.00, 1.00, 0.35),
    10: ('arc2-ch05', 'archive/images-of-ethra/chapter-arc2-05-v6.png',  0.65, 0.10, 1.00, 0.75),
    11: ('arc2-ch06', 'static/images/chapter-arc2-06.png',               0.55, 0.10, 1.00, 0.60),
    12: ('arc3-ch01', 'static/images/chapter-arc3-01-v4.png',            0.70, 0.00, 1.00, 0.35),
    13: ('arc3-ch02', 'static/images/chapter-arc3-02.png',               0.20, 0.00, 0.65, 0.22),
    14: ('arc3-ch03', 'archive/images-of-ethra/chapter-arc3-03-v3.png',  0.30, 0.30, 0.80, 0.70),
    15: ('arc3-ch04', 'static/images/chapter-arc3-04.png',               0.55, 0.00, 1.00, 0.35),
    16: ('arc3-ch05', 'static/images/chapter-arc3-05.png',               0.60, 0.00, 1.00, 0.45),
    17: ('arc4-ch01', 'static/images/chapter-arc4-01-v6.png',            0.55, 0.05, 1.00, 0.55),
    18: ('arc4-ch02', 'static/images/chapter-arc4-02.png',               0.55, 0.05, 1.00, 0.60),
    19: ('arc4-ch03', 'static/images/chapter-arc4-03.png',               0.35, 0.05, 0.80, 0.55),
    20: ('arc4-ch04', 'static/images/chapter-arc4-04-v3.png',            0.62, 0.45, 1.00, 0.80),
    21: ('arc4-ch06', 'static/images/chapter-arc4-06-v5.png',            0.68, 0.15, 1.00, 0.60),
    22: ('arc5-ch01', 'static/images/chapter-arc5-01-v3.png',            0.55, 0.25, 1.00, 0.75),
    23: ('arc5-ch05', 'static/images/chapter-arc5-05-v2.png',            0.55, 0.15, 1.00, 0.75),
    24: ('arc5-ch11', 'archive/images-of-ethra/chapter-arc5-11-v101.png',0.55, 0.00, 1.00, 0.35),
    25: ('arc5-ch19', 'static/images/chapter-arc5-19-v5.png',            0.55, 0.05, 1.00, 0.60),
    26: ('arc5-ch22', 'static/images/chapter-arc5-22-v7.png',            0.62, 0.30, 1.00, 0.70),
    27: ('arc6-ch01', 'archive/images-of-ethra/chapter-arc6-01-v4.png',  0.68, 0.30, 1.00, 0.75),
    28: ('arc6-ch02', 'static/images/chapter-arc6-02-v3.png',            0.62, 0.00, 1.00, 0.25),
    29: ('arc6-ch03', 'archive/images-of-ethra/chapter-arc6-03-v2.png',  0.60, 0.00, 1.00, 0.50),
    30: ('arc6-ch04', 'static/images/chapter-arc6-04-v2.png',            0.72, 0.00, 1.00, 0.40),
    31: ('arc6-ch05', 'static/images/chapter-arc6-05-v1.png',            0.55, 0.10, 1.00, 0.60),
    32: ('arc7-ch01', 'archive/images-of-ethra/chapter-arc7-01-v3.png',  0.55, 0.00, 1.00, 0.38),
    33: ('arc7-ch02', 'static/images/chapter-arc7-02-v4.png',            0.55, 0.00, 1.00, 0.38),
    34: ('arc7-ch03', 'static/images/chapter-arc7-03-v9.png',            0.35, 0.05, 0.80, 0.45),
}
# the two live pilots fold into the shared block (existing webps kept as-is)
PILOTS = ['arc1-ch02', 'arc4-ch05']


def fit(x0, y0, x1, y1):
    """Bands are horizontal strips: if the chosen region is too tall for the
    MIN_RATIO, TRIM HEIGHT about its vertical centre. Never widen sideways —
    widening re-includes the drift/face regions the crop was chosen to
    exclude (bug found in audit pass 1)."""
    w, h = x1 - x0, y1 - y0
    if w / h >= MIN_RATIO:
        return x0, y0, x1, y1
    h2 = w / MIN_RATIO
    cy = (y0 + y1) / 2.0
    y0 = max(0.0, cy - h2 / 2.0)
    y1 = min(1.0, y0 + h2)
    y0 = max(0.0, y1 - h2)
    return x0, y0, x1, y1


def main():
    made = []
    for idx in sorted(CROPS):
        cid, rel, x0, y0, x1, y1 = CROPS[idx]
        x0, y0, x1, y1 = fit(x0, y0, x1, y1)
        src = os.path.join(BASE, rel)
        im = Image.open(src).convert('RGB')
        W, H = im.size
        box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
        crop = im.crop(box)
        scale = OUT_W / crop.width
        crop = crop.resize((OUT_W, max(1, int(crop.height * scale))), Image.LANCZOS)
        out = os.path.join(OUT_DIR, 'title-%s.webp' % cid)
        crop.save(out, 'WEBP', quality=72)
        made.append((cid, out, os.path.getsize(out)))
        print('%-10s %6d B  %s' % (cid, os.path.getsize(out), out))

    # ── emit the CSS block ─────────────────────────────────────────────
    all_ids = PILOTS + [CROPS[i][0] for i in sorted(CROPS)]
    sel_h2 = ',\n'.join('#%s h2' % c for c in all_ids)
    sel_before = ',\n'.join('#%s h2::before' % c for c in all_ids)
    lines = []
    lines.append('/* ═══ CHAPTER TITLE BANDS — retrofit identity (2026-08-25) ═══')
    lines.append('   Ainz ruling: retrofit fragments are the site-wide title')
    lines.append('   identity; pixel sprite retired. Each band is a masked')
    lines.append('   fragment of the chapter\'s own scene (discard where one')
    lines.append('   yields a drift-free fragment, else the canonical cover).')
    lines.append('   Relative url() ONLY — absolute /static/ 404s on Pages. */')
    lines.append('%s { background: none; }' % sel_h2)
    lines.append('')
    lines.append('%s {' % sel_before)
    lines.append("  content: ''; position: absolute; right: -4px; top: -12px; bottom: -6px; width: 168px;")
    lines.append('  background: right center / cover no-repeat;')
    lines.append('  -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,0.95), rgba(0,0,0,0.40) 60%, transparent 96%);')
    lines.append('          mask-image: linear-gradient(to left, rgba(0,0,0,0.95), rgba(0,0,0,0.40) 60%, transparent 96%);')
    lines.append('  opacity: 0.55; pointer-events: none; border-radius: 4px;')
    lines.append('}')
    lines.append('')
    for c in all_ids:
        lines.append("#%s h2::before { background-image: url('../images/title-%s.webp'); }" % (c, c))
    lines.append("#arc1-ch02 h2::before { filter: brightness(1.25); }  /* tuned on the live pilot */")
    css = '\n'.join(lines) + '\n'
    css_out = os.path.join(BASE, 'tools', 'title_rollout_css_block.css')
    with open(css_out, 'w', encoding='utf-8') as f:
        f.write(css)
    print('css block: %d selectors -> %s' % (len(all_ids), css_out))

    # ── audit contact sheet of the final bands ────────────────────────
    from PIL import ImageDraw, ImageFont
    try:
        font = ImageFont.load_default(size=20)
    except TypeError:
        font = ImageFont.load_default()
    COLS = 6
    TW, TH, LH = 300, 160, 26
    rows = [all_ids[i:i + COLS] for i in range(0, len(all_ids), COLS)]
    canvas = Image.new('RGB', (COLS * (TW + 6) + 6, len(rows) * (TH + LH + 6) + 6), (8, 12, 20))
    d = ImageDraw.Draw(canvas)
    for r, row in enumerate(rows):
        for c, cid in enumerate(row):
            x = 6 + c * (TW + 6)
            y = 6 + r * (TH + LH + 6)
            d.rectangle([x, y, x + TW, y + LH], fill=(0, 0, 0))
            d.text((x + 6, y + 2), cid, fill=(240, 208, 128), font=font)
            im = Image.open(os.path.join(OUT_DIR, 'title-%s.webp' % cid)).convert('RGB')
            im.thumbnail((TW, TH), Image.LANCZOS)
            canvas.paste(im, (x, y + LH))
    sheet = os.path.join(WS, 'title_bands_audit.jpg')
    canvas.save(sheet, quality=88)
    print('audit sheet ->', sheet)


if __name__ == '__main__':
    main()
