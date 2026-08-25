# Title-band pilot assets: 2 retrofit crops from the misc archive + 1 hand-authored pixel sprite.
# Zero AI generation. Pure PIL crops + parametric pixel painting.
import os
from PIL import Image

ROOT = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site"
ARC = os.path.join(ROOT, "archive", "images-of-ethra")
OUT = os.path.join(ROOT, "static", "images")

# ---------- 1. retrofit crops ----------
def crop_save(src, box, dst, width=320):
    im = Image.open(os.path.join(ARC, src)).convert("RGB")
    w, h = im.size
    l, t, r, b = box
    c = im.crop((int(l*w), int(t*h), int(r*w), int(b*h)))
    scale = width / c.width
    c = c.resize((width, int(c.height*scale)), Image.LANCZOS)
    c.save(os.path.join(OUT, dst), "WEBP", quality=82)
    print(dst, c.size, os.path.getsize(os.path.join(OUT, dst)), "bytes")

# The Chamber: right door panel + rune rows + stone column + torch bowl.
# Figures only appear below y~0.66 -> crop stays scenery-only (zero drift).
crop_save("chapter-arc1-02-v3.webp", (0.50, 0.05, 1.00, 0.60), "title-arc1-02.webp")

# The Gifts: seated Ajani from behind — mane, feather, white robe, open ledger,
# spear shaft. Excludes the two-tail drift (below y~0.72) and the bearer's hands.
crop_save("chapter-arc4-05-v8.webp", (0.44, 0.38, 0.75, 0.74), "title-arc4-05.webp")

# ---------- 2. arena pixel sprite ----------
PAL = {
    'K': (26, 18, 12),    # outline dark
    'T': (201, 154, 82),  # tawny fur
    'W': (242, 234, 214), # white mane/cloth
    'G': (212, 175, 55),  # gold fist
    'D': (107, 50, 38),   # sash
    'P': (185, 138, 94),  # pillar stone
    'p': (138, 95, 60),   # pillar shadow
    'E': (232, 177, 132), # dust/ember
    'S': (169, 124, 79),  # sand
}
FW, FH, NF = 40, 16, 6

def grid(): return [['.']*FW for _ in range(FH)]
def px(g, x, y, c):
    if 0 <= x < FW and 0 <= y < FH: g[y][x] = c

def pillar(g, top_dx):
    for x in range(29, 37):           # capital
        px(g, x+top_dx, 2, 'P'); px(g, x+top_dx, 3, 'p' if x in (29, 36) else 'P')
    for y in range(4, 14):            # shaft
        dx = top_dx if y <= 6 else 0
        for x in range(30, 36):
            c = 'P'
            if x in (30, 35): c = 'p'
            px(g, x+dx, y, c)
    for x, y in ((32, 5), (34, 8), (31, 10), (33, 12)):  # masonry flecks
        px(g, x, y, 'p')
    for x in range(29, 37):           # base
        px(g, x, 14, 'P' if 30 <= x <= 35 else 'p')
    for x in range(26, 40, 2):        # sand
        px(g, x, 15, 'S')

def ajani(g, dx, arm):
    # ears + mane + face (facing right)
    px(g, 19+dx, 2, 'T'); px(g, 21+dx, 2, 'T')
    for x, y in [(17,2),(18,2),(16,3),(17,3),(18,3),(16,4),(17,4),(16,5),(17,5),(16,6),(17,6)]:
        px(g, x+dx, y, 'W')
    for x in range(19, 22):
        for y in range(3, 6): px(g, x+dx, y, 'T')
    px(g, 22+dx, 4, 'T'); px(g, 22+dx, 5, 'T')
    px(g, 21+dx, 4, 'K')                      # eye
    px(g, 19+dx, 6, 'T'); px(g, 20+dx, 6, 'T')
    # torso + sash
    for x in range(17, 22):
        for y in range(7, 12): px(g, x+dx, y, 'D' if y == 10 else 'T')
    # tail
    px(g, 15+dx, 9, 'T'); px(g, 14+dx, 10, 'T'); px(g, 13+dx, 11, 'T'); px(g, 12+dx, 12, 'W')
    # legs
    for y in range(12, 15):
        px(g, 17+dx, y, 'T'); px(g, 20+dx, y, 'T')
    # arm
    if arm == 'down':
        px(g, 22+dx, 8, 'T'); px(g, 22+dx, 9, 'T')
    elif arm == 'windup':
        for x in (14, 15, 16): px(g, x+dx, 7, 'T')
        px(g, 13+dx, 7, 'G'); px(g, 13+dx, 8, 'G')
    elif arm == 'punch':
        for x in range(22, 28): px(g, x+dx, 7, 'T')
        px(g, 28+dx, 7, 'G'); px(g, 29+dx, 7, 'G'); px(g, 28+dx, 8, 'G')

FRAMES = [
    (-3, 'down',   0, 0),
    (-1, 'windup', 0, 0),
    ( 0, 'punch',  0, 0),
    ( 0, 'punch',  1, 1),
    ( 0, 'punch', -1, 2),
    (-2, 'down',   0, 0),
]
DUST = {1: [(28, 2), (37, 3), (29, 1)],
        2: [(27, 4), (38, 5), (28, 6)]}

pal_idx = {k: i+1 for i, k in enumerate(PAL)}
raw = Image.new('L', (FW*NF, FH), 0)
for f, (dx, arm, tdx, dust) in enumerate(FRAMES):
    g = grid()
    pillar(g, tdx)
    ajani(g, dx, arm)
    for x, y in DUST.get(dust, []): px(g, x, y, 'E')
    for y in range(FH):
        for x in range(FW):
            ch = g[y][x]
            raw.putpixel((f*FW+x, y), pal_idx[ch] if ch != '.' else 0)
out = Image.new('P', (FW*NF, FH))
# index 0 = transparent; 1..N = palette order
out.putpalette([0, 0, 0] + sum((list(PAL[k]) for k in PAL), []) + [0, 0, 0]*(255-len(PAL)))
out.info['transparency'] = 0
pix = out.load()
for y in range(FH):
    for x in range(FW*NF):
        pix[x, y] = raw.getpixel((x, y))
sp = os.path.join(OUT, "arena-sprite.png")
out.save(sp)
print("arena-sprite.png", out.size, os.path.getsize(sp), "bytes")
# 3x preview for audit (kept OUT of the served tree)
out.resize((FW*NF*3, FH*3), Image.NEAREST).save(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "_audit_sprite_preview.png"))
print("preview saved")
