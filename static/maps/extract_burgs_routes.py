"""Extract burgs_v2.json and routes_v2.json from azgaar_pack_v2.json"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, 'azgaar_pack_v2.json'), 'r', encoding='utf-8') as f:
    pack = json.load(f)

# ── burgs_v2.json ─────────────────────────────────
burgs = pack.get('burgs', [])
burg_list = []
for b in burgs:
    if not isinstance(b, dict) or not b.get('name'):
        continue
    burg_list.append({
        "id": b.get('i'),
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
sz = os.path.getsize(os.path.join(BASE, 'burgs_v2.json'))
print(f"burgs_v2.json: {len(burg_list)} burgs, {sz} bytes")

# ── routes_v2.json ─────────────────────────────────
routes = pack.get('routes', [])
route_list = []
for r in routes:
    if not isinstance(r, dict):
        continue
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
sz2 = os.path.getsize(os.path.join(BASE, 'routes_v2.json'))
print(f"routes_v2.json: {len(route_list)} routes, {sz2} bytes")

print("\nDone — all exports complete")
