# -*- coding: utf-8 -*-
"""
export_static.py — ROADMAP P1.5: bake the live site into a static mirror
for GitHub Pages (https://magicrulerr-art.github.io/ethra/).

The Flask server is the canonical writing environment; this script is a
READ-ONLY consumer of it. It imports server.py, calls every public view
function under a root request context, rewrites absolute /static/ and
/api/ references to the /ethra/ mount (the shape Pages serves at), and
emits a self-contained _pages/ tree:

    _pages/index.html            landing + all sections (lazy fetches baked)
    _pages/map/index.html        the canon map viewer
    _pages/api/...               every API response as a static file
    _pages/static/...            the full asset tree (node_modules excluded)

Frontend fetch paths already use /ethra/api/... so the baked tree is a
drop-in mirror. The write-only dev endpoint (/api/map/upload) is NOT
exported — it stays local-Flask exclusive.

Usage:  python tools/export_static.py        (no running server needed)
Output: ethra_site/_pages/
"""
import importlib.util
import json
import os
import shutil
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, '_pages')
ROOT = '/ethra'

# ── load server.py as a module without launching app.run() ─────────
_spec = importlib.util.spec_from_file_location(
    'ethra_server', os.path.join(BASE, 'server.py'))
srv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(srv)

IGNORED_STATIC_DIRS = {'node_modules', 'dist', '__pycache__', '_archive'}


def _write(path_parts, text):
    path = os.path.join(OUT, *path_parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)


def _rootify_html(html):
    """Rewrite a root-mounted HTML document for the /ethra/ mount."""
    html = srv.rewrite_static_paths(html, ROOT)
    html = html.replace("'/static/", "'" + ROOT + "/static/")
    html = html.replace('"/static/', '"' + ROOT + '/static/')
    # site-nav links
    html = html.replace('href="/"', 'href="%s/"' % ROOT)
    html = html.replace('href="/map/"', 'href="%s/map/"' % ROOT)
    html = html.replace('href="/?', 'href="%s/?' % ROOT)
    return html


def _call(view, *args):
    """Invoke a view function; return (status, body_text, is_json)."""
    rv = view(*args)
    if isinstance(rv, tuple):
        body, status = rv[0], rv[1]
    else:
        body, status = rv, 200
    if hasattr(body, 'get_data'):
        is_json = 'json' in (body.mimetype or '')
        return status, body.get_data(as_text=True), is_json
    return status, body, False


def _bake_json(name_parts, view, *args):
    status, text, is_json = _call(view, *args)
    if status != 200:
        print('  [skip] %s (HTTP %s)' % ('/'.join(name_parts), status))
        return False
    if is_json:
        data = json.loads(text)
        text = json.dumps(data, ensure_ascii=False)
    text = text.replace('/static/', ROOT + '/static/')
    _write(['api'] + list(name_parts), text)
    return True


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    n = 0
    with srv.app.test_request_context('/'):
        # landing page (rendered + minified exactly as Flask serves it)
        status, html, _ = _call(srv.index)
        _write(['index.html'], _rootify_html(html))
        n += 1

        # canon map viewer
        with open(os.path.join(BASE, 'static', 'ethra_map_standalone.html'),
                  encoding='utf-8') as f:
            _write(['map', 'index.html'], _rootify_html(f.read()))
        n += 1

        # ── API surface (read-only endpoints only) ──
        _bake_json(['health'], srv.health); n += 1
        _bake_json(['navigation'], srv.api_navigation); n += 1
        _bake_json(['chapters'], srv.api_chapters); n += 1
        _bake_json(['bestiary'], srv.api_bestiary); n += 1
        _bake_json(['biomes'], srv.api_biomes); n += 1
        _bake_json(['map', 'coordinates'], srv.api_map_coordinates); n += 1
        _bake_json(['places'], srv.api_places); n += 1

        for ch in json.loads(_call(srv.api_chapters)[1]):
            _bake_json(['chapter', ch['id']], srv.api_chapter, ch['id']); n += 1
        # api/world is both a list endpoint AND a directory of sections;
        # Pages resolves /ethra/api/world -> /ethra/api/world/ -> index.html
        _bake_json(['world', 'index.html'], srv.api_world_sections); n += 1
        for sec in json.loads(_call(srv.api_world_sections)[1]):
            _bake_json(['world', sec['id']], srv.api_world_section, sec['id']); n += 1
        biomes = json.loads(_call(srv.api_biomes)[1])
        for biome, names in biomes.items():
            _bake_json(['creatures', biome], srv.api_creatures_by_biome, biome); n += 1
            for name in names:
                _bake_json(['creature', biome, name],
                           srv.api_creature, biome, name); n += 1
        for p in json.loads(_call(srv.api_places)[1]):
            _bake_json(['place', p['slug']], srv.api_place, p['slug']); n += 1

    # ── static asset tree ──
    def _ignore(dir, names):
        return [x for x in names
                if x in IGNORED_STATIC_DIRS
                or x.endswith('.pyc')]
    shutil.copytree(os.path.join(BASE, 'static'),
                    os.path.join(OUT, 'static'), ignore=_ignore)

    print('exported %d documents -> %s' % (n, OUT))
    total = 0
    for dirpath, _dirs, files in os.walk(OUT):
        for f in files:
            total += os.path.getsize(os.path.join(dirpath, f))
    print('total size: %.1f MB' % (total / 1e6))
    return 0


if __name__ == '__main__':
    sys.exit(main())
