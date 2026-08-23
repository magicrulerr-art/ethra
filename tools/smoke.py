"""
Ethra smoke suite — ROADMAP P0 safety net.

Hits every endpoint of the live server and verifies structural invariants
(arc/chapter counts, navigation, creatures, world sections, map data).
Includes a live DROP-IN test: writes a temporary place file into
content/places/, asserts it appears in /api/places, /api/place/<slug> and
the /api/map/coordinates city_pins merge, then removes it.

Usage:  python tools/smoke.py           (server must be running)
Env:    ETHRA_URL=http://127.0.0.1:8790
Exit code 0 = ALL PASS.
"""
import json
import os
import sys
import urllib.request

BASE = os.environ.get('ETHRA_URL', 'http://127.0.0.1:8790').rstrip('/')
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILURES = []


def get(path):
    req = urllib.request.Request(BASE + path, headers={'User-Agent': 'ethra-smoke/1.0'})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.status, r.read().decode('utf-8', 'replace')


def jget(path):
    status, body = get(path)
    return status, json.loads(body)


def check(name, cond, detail=''):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  — {detail}" if detail and not cond else ''))
    if not cond:
        FAILURES.append(name)


def main():
    print(f"Ethra smoke suite -> {BASE}\n")

    # 1. Landing page
    st, html = get('/')
    check('GET / returns 200', st == 200)
    check('landing page title', 'THE GREAT ORRERY' in html.upper())

    # 2. Health
    st, data = jget('/api/health')
    check('/api/health ok', st == 200 and data.get('status') == 'ok')
    check('health: 6 arcs', data.get('arcs') == 6, f"got {data.get('arcs')}")
    check('health: 50 chapters', data.get('chapters') == 50, f"got {data.get('chapters')}")

    # 3. Navigation
    st, nav = jget('/api/navigation')
    ids = [s['id'] for s in nav.get('sections', [])]
    check('/api/navigation sections', {'bestiary', 'world', 'story'} <= set(ids), str(ids))
    story = next(s for s in nav['sections'] if s['id'] == 'story')
    check('navigation: 6 arcs', len(story.get('arcs', [])) == 6)
    arc_titles = [a['label'] for a in story.get('arcs', [])]
    check('arc titles from manifest', all(t.startswith('Arc') for t in arc_titles), str(arc_titles))

    # 4. Chapters
    st, chs = jget('/api/chapters')
    check('/api/chapters = 50', len(chs) == 50, f"got {len(chs)}")
    arc5 = [c for c in chs if c['arc_num'] == 5]
    check('arc5 = 22 timestamped chapters', len(arc5) == 22, f"got {len(arc5)}")
    seq_ok = all(ch.get('next_id') for ch in chs if not ch.get('is_last'))
    check('sequential nav markers present', seq_ok)
    bad = []
    sample = chs[:2] + arc5[:2] + chs[-2:]
    for c in sample:
        st2, h2 = get(f"/api/chapter/{c['id']}")
        if st2 != 200 or 'Chapter' not in h2:
            bad.append(c['id'])
    check('sample chapter fetches', not bad, str(bad))

    # 5. Bestiary
    st, b = jget('/api/bestiary')
    check('/api/bestiary content', st == 200 and 'wengari' in b.get('content', '').lower())

    # 6. World sections (auto-discovery)
    st, secs = jget('/api/world')
    wids = [s['id'] for s in secs]
    check('/api/world >= 6 sections', len(wids) >= 6, str(wids))
    st, w = jget('/api/world/' + wids[0])
    check('world section content', st == 200 and len(w.get('content', '')) > 200)

    # 7. Creatures
    st, biomes = jget('/api/biomes')
    check('/api/biomes', st == 200 and len(biomes) > 0)
    first_biome = sorted(biomes)[0]
    st, names = jget(f'/api/creatures/{first_biome}')
    check(f'creatures in {first_biome}', st == 200 and len(names) > 0)
    st, cr = jget(f'/api/creature/{first_biome}/{names[0]}')
    check('creature content', st == 200 and len(cr.get('content', '')) > 100)

    # 8. Map coordinates
    st, coords = jget('/api/map/coordinates')
    check('map coordinates + creatures', st == 200 and len(coords.get('creatures', [])) > 0)
    check('city_pins list present', isinstance(coords.get('city_pins'), list))

    # 9. Places DROP-IN fixture test (proves one-file addition works)
    places_dir = os.path.join(SITE_ROOT, 'content', 'places')
    os.makedirs(places_dir, exist_ok=True)
    fixture = os.path.join(places_dir, 'zz-smoke-test.md')
    with open(fixture, 'w', encoding='utf-8') as f:
        f.write("---\nname: Smoke Test Hold\nkind: city\nbiome: steadfast-desert\n"
                "x_pct: 12.5\ny_pct: 34.5\n---\n\nThe fixture gazetteer body.\n")
    try:
        st, pl = jget('/api/places')
        check('drop-in place in /api/places', any(p.get('slug') == 'zz-smoke-test' for p in pl))
        st, one = jget('/api/place/zz-smoke-test')
        check('drop-in place content', st == 200 and 'fixture gazetteer' in one.get('content', ''))
        check('drop-in place meta', one.get('name') == 'Smoke Test Hold' and one.get('x_pct') == '12.5')
        st, coords2 = jget('/api/map/coordinates')
        merged = any(p.get('id') == 'zz-smoke-test' and abs(p.get('x_pct', 0) - 12.5) < 0.01
                     for p in coords2.get('city_pins', []))
        check('drop-in place merged into city_pins', merged)
    finally:
        os.remove(fixture)
    st, pl2 = jget('/api/places')
    check('fixture removed cleanly', not any(p.get('slug') == 'zz-smoke-test' for p in pl2))

    # 10. Map viewer + static data
    st, mhtml = get('/map/')
    check('GET /map/ 200', st == 200 and '<html' in mhtml.lower())
    st, _ = get('/static/data/map-coordinates.json')
    check('static map json served', st == 200)

    print()
    if FAILURES:
        print(f"SMOKE FAILED: {len(FAILURES)} check(s):")
        for f_ in FAILURES:
            print("  -", f_)
        sys.exit(1)
    print("SMOKE: ALL PASS")
    sys.exit(0)


if __name__ == '__main__':
    main()
