"""Process azgaar_pack_v2.json → cells_v2.geojson, burgs_v2.json, routes_v2.json"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, 'azgaar_pack_v2.json'), 'r', encoding='utf-8') as f:
    pack = json.load(f)

cells = pack['cells']
states = pack.get('states', {})
cultures = pack.get('cultures', {})
religions = pack.get('religions', {})
burgs = pack.get('burgs', {})
routes = pack.get('routes', [])

p = cells['p']     # list of [x,y]
v = cells['v']     # list of [vertex_idx, ...]
h = cells['h']     # dict: str(idx)→height
biome = cells.get('biome', {})
state_arr = cells.get('state', {})
culture_arr = cells.get('culture', {})
religion_arr = cells.get('religion', {})
pop_arr = cells.get('pop', {})
burg_arr = cells.get('burg', {})
fl_arr = cells.get('fl', {})
conf_arr = cells.get('conf', {})
f_arr = cells.get('f', {})

def gv(d, idx, default=0):
    if isinstance(d, dict):
        return d.get(str(idx), default)
    if isinstance(d, list) and idx < len(d):
        return d[idx]
    return default

# ── cells_v2.geojson ─────────────────────────────────
features = []
total = len(v)
print(f"Total cells: {total}")

for i in range(total):
    ht = gv(h, i, 0)
    if ht < 20:
        continue
    verts = v[i]
    coords = []
    for vi in verts:
        vi = int(vi)
        if vi < len(p):
            coords.append([round(p[vi][0], 2), round(p[vi][1], 2)])
    if len(coords) < 3:
        continue
    coords.append(coords[0])
    
    feat = {
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": [coords]},
        "properties": {
            "id": i,
            "height": round(ht, 1),
            "biome": int(gv(biome, i, 0)),
            "state": int(gv(state_arr, i, 0)),
            "culture": int(gv(culture_arr, i, 0)),
            "religion": int(gv(religion_arr, i, 0)),
            "pop": round(float(gv(pop_arr, i, 0)), 2),
            "burg": int(gv(burg_arr, i, 0)),
            "flux": int(gv(fl_arr, i, 0)),
            "conf": int(gv(conf_arr, i, 0)),
            "forest": int(gv(f_arr, i, 0)),
        }
    }
    features.append(feat)

geojson = {"type": "FeatureCollection", "features": features}
with open(os.path.join(BASE, 'cells_v2.geojson'), 'w', encoding='utf-8') as f:
    json.dump(geojson, f, ensure_ascii=False)
sz = os.path.getsize(os.path.join(BASE, 'cells_v2.geojson'))
print(f"cells_v2.geojson: {len(features)} features, {sz} bytes ({sz/1024:.0f} KB)")

# ── burgs_v2.json ─────────────────────────────────
burg_list = []
for bid in sorted(burgs.keys(), key=lambda x: int(x) if str(x).lstrip('-').isdigit() else 0):
    b = burgs[bid]
    if not b.get('name') or str(bid) == '0':
        continue
    burg_list.append({
        "id": int(bid) if str(bid).lstrip('-').isdigit() else bid,
        "cell": b.get('cell'),
        "name": b.get('name'),
        "state": b.get('state'),
        "culture": b.get('culture'),
        "x": round(b.get('x', 0), 2),
        "y": round(b.get('y', 0), 2),
        "population": round(b.get('population', 0), 3),
        "type": b.get('type', ''),
        "capital": bool(b.get('capital')),
        "port": bool(b.get('port')),
    })

with open(os.path.join(BASE, 'burgs_v2.json'), 'w', encoding='utf-8') as f:
    json.dump(burg_list, f, ensure_ascii=False, indent=2)
sz2 = os.path.getsize(os.path.join(BASE, 'burgs_v2.json'))
print(f"burgs_v2.json: {len(burg_list)} burgs, {sz2} bytes ({sz2/1024:.0f} KB)")

# ── routes_v2.json ─────────────────────────────────
route_list = []
for r in routes:
    pts = []
    for pt in r.get('points', []):
        pts.append([round(pt[0], 1), round(pt[1], 1)])
    route_list.append({
        "i": r.get('i'),
        "type": r.get('type', 'military'),
        "name": r.get('name', ''),
        "group": r.get('group', 'roads'),
        "points": pts,
    })

with open(os.path.join(BASE, 'routes_v2.json'), 'w', encoding='utf-8') as f:
    json.dump(route_list, f, ensure_ascii=False, indent=2)
sz3 = os.path.getsize(os.path.join(BASE, 'routes_v2.json'))
print(f"routes_v2.json: {len(route_list)} routes, {sz3} bytes ({sz3/1024:.0f} KB)")

print("\n=== EXPORT COMPLETE ===")
print(f"7 SVGs: landmass, biomes, heightmap, states, religions, cultures, routes")
print(f"cells_v2.geojson: {len(features)} land cells ({sz/1024:.0f}KB)")
print(f"burgs_v2.json:    {len(burg_list)} settlements ({sz2/1024:.0f}KB)")
print(f"routes_v2.json:   {len(route_list)} routes ({sz3/1024:.0f}KB)")
