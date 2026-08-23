# -*- coding: utf-8 -*-
"""Ethra canon map — Deliverable #1 (v2: painted base plate).
Layered SVG (2400x1000). The terrain base is the Qwen-Image painted plate
base_ethra_painted.png (layout-faithful to canon); all semantic overlays
(cities, races, creatures, routes, labels, legend) are hand-authored vectors
positioned from static/data/map-coordinates.json (schema v2).
Layers are named <g id="layer-..."> for the Deliverable #2 toggle system.
"""
import base64, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "static", "data", "map-coordinates.json")
OUT = os.path.join(HERE, "static", "maps", "ethra_canon_v1.svg")
BASE_PNG = os.path.join(HERE, "static", "maps", "base_ethra_painted.png")
W, H = 2400, 1000

# embed the painted plate as a data URI so the SVG is self-contained
# (SVGs loaded via <img> cannot fetch external resources)
with open(BASE_PNG, "rb") as f:
    BASE_IMG = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

with open(DATA, encoding="utf-8") as f:
    CANON = json.load(f)

def X(p): return p * 24.0
def Y(p): return p * 10.0

def cr_path(pts, closed=True):
    """Catmull-Rom smoothed path through points."""
    n = len(pts)
    if closed:
        P = [pts[-1]] + list(pts) + [pts[0], pts[1]]
    else:
        P = [pts[0]] + list(pts) + [pts[-1]]
    d = "M %.0f %.0f" % pts[0]
    rng = range(1, n + 1) if closed else range(1, n - 1)
    for i in rng:
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
        d += " C %.0f %.0f %.0f %.0f %.0f %.0f" % (c1[0], c1[1], c2[0], c2[1], p2[0], p2[1])
    return d + (" Z" if closed else "")

# ---------------- palette (site canon colors) ----------------
C_OCEAN   = "#0a1628"
C_RUNE    = "#6f8f4f"
C_DESERT  = "#d9b36a"
C_UMBRAL  = "#aebfd4"
C_FLICK   = "#a4553f"
C_TIDE    = "#3f7f8c"
C_CAVE    = "#241c18"
C_MYCEL   = "#7fd4c1"
C_GOLD    = "#c9a059"
C_CRIM    = "#8b2a2a"
C_INK     = "#e8e2d0"
C_HALO    = "#0a1628"   # dark halo behind light text for readability on the painted plate

# ---------------- hand-authored overlay geometry (pct of canvas) ----------------
CITIES = [("Styxian", 33.1, 41.6), ("Verdantis", 46.5, 44.5), ("Vey'sul", 21.3, 64.3)]

ROUTES = [
 ("Pyrinae Caravan Route", [(46.1,59.5),(40.0,50.0),(33.1,41.6)]),
 ("Humman Trade Route",    [(46.5,44.5),(47.5,52.0),(46.1,59.5),(52.0,66.0),(60.0,70.0),(65.4,72.8)]),
 ("Wengari Supply Line",   [(33.1,41.6),(40.0,45.0),(48.0,48.2)]),
 ("Wengari Supply Line II",[(33.1,41.6),(26.0,50.0),(19.7,58.6)]),
 ("Dragari Song Road",     [(19.7,58.6),(20.5,61.5),(21.3,64.3),(23.6,76.6)]),
 ("Threx Spore Route",     [(64.6,32.1),(66.0,45.0),(66.0,60.0),(65.4,72.8)]),
]

# faint biome tint ellipses (cx,cy,rx,ry in pct) — toggleable semantic layer over the painted plate
BIOME_TINT = {
 "rune-belt":        (39, 33, 20, 23, C_RUNE),
 "steadfast-desert": (52, 60, 18, 20, C_DESERT),
 "umbral-ring":      (23, 65, 10, 16, C_UMBRAL),
 "flickermarch":     (66, 37,  9, 24, C_FLICK),
 "tidepools":        (66, 72, 7.5, 9, C_TIDE),
}

# per-slug race label offsets (dx, dy from marker) to avoid label collisions
RACE_LABEL_OFF = {"pyrinae": (0, 40), "veylar": (0, 40)}

CAVE_RECT = (2030, 700, 340, 260)  # x,y,w,h  underground inset

# ---------------- layer builders ----------------
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&apos;")

def halo_text(x, y, fill, size, body, anchor="middle", extra=""):
    return ('<text x="%.0f" y="%.0f" fill="%s" font-size="%d" text-anchor="%s" '
            'stroke="%s" stroke-width="4" paint-order="stroke" stroke-linejoin="round" %s>%s</text>'
            % (x, y, fill, size, anchor, C_HALO, extra, body))

P = []
P.append('<?xml version="1.0" encoding="UTF-8"?>')
P.append('<svg id="ethra-canon" xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="Georgia, serif">' % (W, H, W, H))
P.append('<title>Ethra — The Great Orrery (canon map v2, painted base)</title>')

# ocean (fallback backdrop beneath the painted plate)
P.append('<g id="layer-ocean">')
P.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, C_OCEAN))
P.append('</g>')

# landmass = painted base plate
P.append('<g id="layer-landmass">')
P.append('<image href="%s" x="0" y="0" width="%d" height="%d" preserveAspectRatio="none"/>' % (BASE_IMG, W, H))
P.append('</g>')

# biomes = faint semantic tint (toggleable; painted plate carries the art)
P.append('<g id="layer-biomes" opacity="0.10">')
for slug, (cx, cy, rx, ry, col) in BIOME_TINT.items():
    P.append('<ellipse id="biome-%s" cx="%.0f" cy="%.0f" rx="%.0f" ry="%.0f" fill="%s"/>' % (slug, X(cx), Y(cy), X(rx), Y(ry), col))
P.append('</g>')

# routes
P.append('<g id="layer-routes" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="2 6" stroke-linecap="round" opacity="0.95">' % C_GOLD)
for name, rpts in ROUTES:
    px = [(X(a), Y(b)) for a, b in rpts]
    P.append('<path d="%s" data-name="%s"/>' % (cr_path(px, closed=False), esc(name)))
P.append('</g>')

# underground inset
x, y, w, h = CAVE_RECT
P.append('<g id="layer-underground">')
P.append('<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="%s" fill-opacity="0.88" stroke="%s" stroke-width="2.5"/>' % (x, y, w, h, C_CAVE, C_MYCEL))
P.append('<path d="M %d %d Q %d %d %d %d L %d %d L %d %d Z" fill="#17110e" stroke="%s" stroke-width="1.5"/>' % (x+30, y+h-40, x+w/2, y+40, x+w-30, y+h-40, x+w-30, y+h-20, x+30, y+h-20, C_MYCEL))
for t in [(x+60, y+h-30, x+120, y+90), (x+w-60, y+h-30, x+w-130, y+100), (x+w/2, y+h-25, x+w/2, y+70)]:
    P.append('<path d="M %d %d Q %d %d %d %d" fill="none" stroke="%s" stroke-width="1.5" opacity="0.7"/>' % (t[0], t[1], (t[0]+t[2])/2+15, (t[1]+t[3])/2, t[2], t[3], C_MYCEL))
P.append('<text x="%d" y="%d" fill="%s" font-size="22" text-anchor="middle" font-weight="bold">THE UNDERGROUND</text>' % (x+w/2, y+32, C_MYCEL))
P.append('<text x="%d" y="%d" fill="%s" font-size="14" text-anchor="middle" font-style="italic">Mycelial Deep — Chi&apos;Thak swarm</text>' % (x+w/2, y+54, C_INK))
uc = CANON["underground_cave"]
P.append('<circle cx="%d" cy="%d" r="9" fill="%s" stroke="%s" stroke-width="2"/>' % (x+90, y+h-70, C_CRIM, C_MYCEL))
P.append('<text x="%d" y="%d" fill="%s" font-size="13" text-anchor="middle">%s</text>' % (x+90, y+h-44, C_INK, esc(uc["constituents"][0]["name"])))
P.append('<circle cx="%d" cy="%d" r="7" fill="%s" stroke="%s" stroke-width="2"/>' % (x+w-90, y+h-70, C_MYCEL, C_MYCEL))
P.append('<text x="%d" y="%d" fill="%s" font-size="13" text-anchor="middle">%s</text>' % (x+w-90, y+h-44, C_INK, esc(uc["constituents"][1]["name"])))
P.append('</g>')

# cities (canonical three)
P.append('<g id="layer-cities">')
for name, px, py in CITIES:
    cx, cy = X(px), Y(py)
    P.append('<path d="M %.0f %.0f l 9 9 l -9 9 l -9 -9 Z" fill="%s" stroke="%s" stroke-width="2" data-name="%s"/>' % (cx, cy-9, C_GOLD, C_INK, esc(name)))
    P.append(halo_text(cx, cy+34, C_INK, 19, esc(name), extra='font-weight="bold"'))
P.append('</g>')

# races (7 canonical)
P.append('<g id="layer-races">')
for c in CANON["creatures"]:
    if c["kind"] != "race":
        continue
    cx, cy = X(c["x_pct"]), Y(c["y_pct"])
    P.append('<circle cx="%.0f" cy="%.0f" r="13" fill="none" stroke="%s" stroke-width="3" data-slug="%s"/>' % (cx, cy, C_GOLD, c["slug"]))
    P.append('<circle cx="%.0f" cy="%.0f" r="5" fill="%s"/>' % (cx, cy, C_GOLD))
    dx, dy = RACE_LABEL_OFF.get(c["slug"], (0, -22))
    P.append(halo_text(cx+dx, cy+dy, C_GOLD, 20, esc(c["name"].split(" (")[0]), extra='font-weight="bold"'))
P.append('</g>')

# creatures
P.append('<g id="layer-creatures">')
for c in CANON["creatures"]:
    if c["kind"] != "creature":
        continue
    cx, cy = X(c["x_pct"]), Y(c["y_pct"])
    P.append('<circle cx="%.0f" cy="%.0f" r="5" fill="%s" stroke="%s" stroke-width="1.5" data-slug="%s" data-name="%s"/>' % (cx, cy, C_CRIM, C_INK, c["slug"], esc(c["name"])))
    P.append(halo_text(cx+4, cy+18, C_INK, 12, esc(c["name"]), extra='opacity="0.95"'))
P.append('</g>')

# labels (biome names)
P.append('<g id="layer-labels">')
for b in CANON["biomes"]:
    if b["slug"] == "underground":
        continue
    P.append(halo_text(X(b["region_x"]), Y(b["region_y"]), C_INK, 30, esc(b["name"].upper()), extra='font-weight="bold" letter-spacing="4" opacity="0.95"'))
P.append('</g>')

# world-ocean caption
P.append('<g id="layer-caption">')
P.append(halo_text(1200, 985, C_INK, 20, "The World-Ocean", extra='font-style="italic" opacity="0.85"'))
P.append('</g>')

# legend + cartouche
P.append('<g id="layer-legend">')
lx, ly, lw, lh = 1985, 40, 385, 372
P.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s" fill-opacity="0.92" stroke="%s" stroke-width="2"/>' % (lx, ly, lw, lh, C_OCEAN, C_GOLD))
P.append('<text x="%d" y="%d" fill="%s" font-size="26" font-weight="bold" text-anchor="middle">ETHRA</text>' % (lx+lw/2, ly+34, C_GOLD))
P.append('<text x="%d" y="%d" fill="%s" font-size="13" font-style="italic" text-anchor="middle">The Great Orrery — canon map v2</text>' % (lx+lw/2, ly+54, C_INK))
P.append('<circle cx="%d" cy="%d" r="10" fill="%s"/><text x="%d" y="%d" fill="%s" font-size="12">Steadfast</text>' % (lx+30, ly+78, C_GOLD, lx+46, ly+82, C_INK))
P.append('<circle cx="%d" cy="%d" r="10" fill="%s"/><text x="%d" y="%d" fill="%s" font-size="12">Flicker</text>' % (lx+130, ly+78, C_CRIM, lx+146, ly+82, C_INK))
row = 0
items = [("Rune Belt", C_RUNE), ("Steadfast Desert", C_DESERT), ("Umbral Ring", C_UMBRAL),
         ("Flickermarch", C_FLICK), ("Tidepools", C_TIDE), ("Underground", C_CAVE)]
for nm, col in items:
    yy = ly + 108 + row * 26
    P.append('<rect x="%d" y="%d" width="18" height="14" fill="%s" stroke="%s" stroke-width="1"/>' % (lx+24, yy-11, col, C_INK))
    P.append('<text x="%d" y="%d" fill="%s" font-size="14">%s</text>' % (lx+50, yy, C_INK, nm))
    row += 1
yy = ly + 108 + row * 26 + 4
P.append('<path d="M %d %d l 7 7 l -7 7 l -7 -7 Z" fill="%s"/><text x="%d" y="%d" fill="%s" font-size="14">Canonical city</text>' % (lx+31, yy-7, C_GOLD, lx+50, yy+4, C_INK))
yy += 24
P.append('<circle cx="%d" cy="%d" r="7" fill="none" stroke="%s" stroke-width="2.5"/><text x="%d" y="%d" fill="%s" font-size="14">Sentient race</text>' % (lx+31, yy-4, C_GOLD, lx+50, yy, C_INK))
yy += 24
P.append('<circle cx="%d" cy="%d" r="4" fill="%s"/><text x="%d" y="%d" fill="%s" font-size="14">Creature</text>' % (lx+31, yy-4, C_CRIM, lx+50, yy, C_INK))
yy += 24
P.append('<path d="M %d %d h 20" stroke="%s" stroke-width="2.5" stroke-dasharray="2 5"/><text x="%d" y="%d" fill="%s" font-size="14">Trade / song route</text>' % (lx+22, yy-4, C_GOLD, lx+50, yy, C_INK))
P.append('</g>')

P.append('</svg>')

svg = "\n".join(P)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("WROTE %s (%d bytes, %d elements)" % (OUT, len(svg), len(P)))
