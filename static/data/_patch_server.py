"""One-shot patcher: insert /api/map/coordinates route into server.py.

Runs PowerShell-equivalent raw-byte replacement but in Python so no
shell escaping is needed. Idempotent — exits cleanly if the route
already exists.
"""
import os
import sys

ROOT = r"C:\Users\magic\.copaw\workspaces\default\ethra_site"
TARGET = os.path.join(ROOT, "server.py")

ROUTE = '''


@app.route("/api/map/coordinates")
def api_map_coordinates():
    """Return the supercontinent map coordinate overlay data.

    Source of truth: static/data/map-coordinates.json
    Holds per-creature (x_pct, y_pct) on the 24:10 panorama, biome region
    centres, the special underground-cave aggregate entry, and a
    `city_pins: []` placeholder reserved for the future culture/society
    revamp (when settlements get plotted on the same map).

    The frontend map layer reads this endpoint and lays down dots.
    Coordinates are 0..100 percentages relative to the map's
    aspect-ratio-locked container so dots scale at any viewport.
    """
    coord_path = os.path.join(STATIC_DIR, "data", "map-coordinates.json")
    if not os.path.exists(coord_path):
        return jsonify({'error': 'map-coordinates.json not found'}), 404
    try:
        with open(coord_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        return jsonify({'error': 'map coordinates unreadable', 'detail': str(e)}), 500
    return jsonify(data)
'''

with open(TARGET, "r", encoding="utf-8") as f:
    src = f.read()

if "/api/map/coordinates" in src:
    print("ALREADY_PATCHED")
    sys.exit(0)

MARKER = "return jsonify(sorted(creatures))"
idx = src.find(MARKER)
if idx < 0:
    print("MARKER_NOT_FOUND")
    sys.exit(1)

ins_pos = idx + len(MARKER)
new = src[:ins_pos] + ROUTE + src[ins_pos:]
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(new)
print(f"INSERTED delta_bytes={len(ROUTE)}")
