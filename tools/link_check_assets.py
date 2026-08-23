#!/usr/bin/env python3
"""Asset link-checker for the Ethra site (P2 asset diet).

Scans the LIVE source tree (never _pages/, which is build output):
  - templates/*.html
  - static/**/*.html, static/**/*.css, static/**/*.js, static/**/*.json
    (excluding static/maps/azgaar_src — gitignored build tooling)
  - content/**/*.md  (rendered markdown also resolves to static assets)

Extracts static-asset references (src/href/srcset/url()/JS string
literals/frontmatter image fields), resolves them against the site root,
and reports:
  1. referenced-but-MISSING assets (with file:line of each reference)
  2. the full set of resolved+existing references (JSON, for diet analysis)
  3. dynamic-probe patterns that cannot be statically resolved
     (e.g. arc5_timeline.js version probing -> computed probe set)

Usage:  python tools/link_check_assets.py [--json tools/linkcheck.json]
Exit code 1 if any referenced-but-missing assets are found, else 0.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSET_EXT = r'(?:png|jpe?g|webp|svg|gif|ico|avif)'

# Attribute-style references (HTML + XML-ish)
RE_ATTR = re.compile(
    r'(?:src|href|data-src|data-full-png|data-full-jpg|data-full-webp|'
    r'poster|content|xlink:href|srcset|image)\s*=\s*["\']([^"\']+)["\']',
    re.IGNORECASE,
)
# CSS url(...)
RE_CSSURL = re.compile(r'url\(\s*[\'"]?([^\'")]+?)[\'"]?\s*\)', re.IGNORECASE)
# JS / JSON string literals that END in an asset extension (path-like: must
# contain a '/' so bare filenames in prose/JSON keys don't false-positive).
RE_JSSTR = re.compile(r'[\'"]([^\'"\n]*?/[^\'"\n]*?\.' + ASSET_EXT + r')[\'"]',
                      re.IGNORECASE)
# markdown ![alt](path) and frontmatter image: path
RE_MD_IMG = re.compile(r'!\[[^\]]*\]\(\s*<?([^)>\s]+?)>?\s*\)')
RE_MD_FIELD = re.compile(r'^\s*(?:image|image_full|cover|map)\s*:\s*(\S+)',
                         re.MULTILINE)

SKIP_PREFIXES = ('http://', 'https://', 'data:', 'mailto:', '#', '//', '{', '{{')


def norm_posix(p: str) -> str:
    return p.replace('\\', '/')


def is_asset_ref(ref: str) -> bool:
    return bool(re.search(r'\.' + ASSET_EXT + r'$', ref, re.IGNORECASE))


def clean_ref(ref: str) -> str | None:
    """Strip query/fragment; return None if not a checkable asset ref."""
    ref = ref.strip().strip('\'"')
    if not ref or ref.startswith(SKIP_PREFIXES):
        return None
    # srcset can hold comma-separated candidates
    ref = ref.split(',')[0].strip().split(' ')[0]
    ref = ref.split('?')[0].split('#')[0]
    if not is_asset_ref(ref):
        return None
    # Pages-export prefix — live site serves the same file without it
    if ref.startswith('/ethra/'):
        ref = ref[len('/ethra'):]
    return ref


def resolve(ref: str, src_file: str) -> str | None:
    """Resolve a cleaned ref to a site-root-relative posix path, or None."""
    if ref.startswith('/static/'):
        return ref[1:]  # strip leading '/'
    if ref.startswith('static/'):
        return ref
    if ref.startswith('/'):
        return None  # non-static absolute route (/api/..., /map/...)
    # relative — resolve against the referencing file's directory
    base = os.path.dirname(src_file)
    joined = norm_posix(os.path.normpath(os.path.join(base, ref)))
    return joined


def scan_file(path: str, refs: dict, rel: str):
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            text = f.read()
    except OSError as e:
        print(f'!! cannot read {rel}: {e}', file=sys.stderr)
        return
    lines = text.splitlines()
    ext = os.path.splitext(path)[1].lower()

    candidates: list[tuple[str, re.Match]] = []
    if ext in ('.html', '.svg', '.md', '.json'):
        for m in RE_ATTR.finditer(text):
            candidates.append((m.group(1), m))
    if ext in ('.css', '.html', '.svg', '.js', '.md'):
        for m in RE_CSSURL.finditer(text):
            candidates.append((m.group(1), m))
    if ext in ('.js', '.json', '.html', '.css'):
        for m in RE_JSSTR.finditer(text):
            candidates.append((m.group(1), m))
    if ext == '.md':
        for m in RE_MD_IMG.finditer(text):
            candidates.append((m.group(1), m))
        for m in RE_MD_FIELD.finditer(text):
            candidates.append((m.group(1), m))

    for raw, m in candidates:
        # srcset may contain several urls
        parts = [raw] if ',' not in raw or not is_asset_ref(raw.split(',')[0].strip().split(' ')[0]) \
            else [p.strip() for p in raw.split(',')]
        for part in parts:
            ref = clean_ref(part)
            if not ref:
                continue
            resolved = resolve(ref, rel)
            if resolved is None:
                continue
            line = text.count('\n', 0, m.start()) + 1
            refs[resolved].append((rel, line, ref))


def main():
    refs: dict[str, list] = defaultdict(list)   # resolved path -> [(file,line,raw)]
    dynamic: list[dict] = []

    # ── files to scan ─────────────────────────────────────────
    scan_targets = []
    tpl = os.path.join(ROOT, 'templates')
    for fn in sorted(os.listdir(tpl)):
        if fn.endswith('.html'):
            scan_targets.append(os.path.join(tpl, fn))
    static = os.path.join(ROOT, 'static')
    for dirpath, dirnames, filenames in os.walk(static):
        # never scan gitignored build tooling, the Pages mirror, or the
        # superseded-art archive (its refs are historical by definition)
        dirnames[:] = [d for d in dirnames
                       if d not in ('azgaar_src', 'node_modules', 'dist', '_archive')]
        for fn in sorted(filenames):
            if fn.lower().endswith(('.html', '.css', '.js', '.json')):
                scan_targets.append(os.path.join(dirpath, fn))
    content = os.path.join(ROOT, 'content')
    for dirpath, dirnames, filenames in os.walk(content):
        for fn in sorted(filenames):
            if fn.endswith('.md'):
                scan_targets.append(os.path.join(dirpath, fn))

    for path in scan_targets:
        rel = norm_posix(os.path.relpath(path, ROOT))
        scan_file(path, refs, rel)

    # ── dynamic probe: arc5_timeline.js med-slot version sweep ──
    # The JS probes /static/images/arc5-med-arc5-chNN-v{X}.png for
    # MED_CHAPTERS_ABS = [1,5,11,19,22], trying 16 versions each.
    ORDER = ['v101', 'v100', 'v99', 'v98', 'v97', 'v96', 'v95',
             'v9', 'v8', 'v7', 'v6', 'v5', 'v4', 'v3', 'v2', 'v1']
    probe_paths = []
    for ch in (1, 5, 11, 19, 22):
        for v in ORDER:
            probe_paths.append(f'static/images/arc5-med-arc5-ch{ch:02d}-{v}.png')
    probe_missing = [p for p in probe_paths
                     if not os.path.exists(os.path.join(ROOT, p.replace('/', os.sep)))]
    dynamic.append({
        'source': 'static/arc5_timeline.js (runtime Image() probe, '
                  'first on-disk hit wins; 404s are the discovery mechanism)',
        'total_probe_paths': len(probe_paths),
        'probe_paths_missing_on_disk': probe_missing,
    })

    # ── runtime-computed refs the static scan cannot see ──
    # server.py get_chapter_images(): highest -vN.png per chapter, plus the
    # template's .webp/.jpg siblings of that base (image_exists gated).
    img_dir = os.path.join(ROOT, 'static', 'images')
    best: dict[str, tuple[int, str]] = {}
    for f in os.listdir(img_dir):
        m = re.match(r'chapter-arc(\d+)-(\d+)(-v(\d+))?\.png$', f)
        if not m:
            continue
        key = f'arc{m.group(1)}-ch{int(m.group(2)):02d}'
        ver = int(m.group(4)) if m.group(4) else 0
        if key not in best or ver > best[key][0]:
            best[key] = (ver, f)
    runtime_refs = []
    for key, (ver, f) in sorted(best.items()):
        base = f[:-4]
        for ext in ('.png', '.webp', '.jpg'):
            runtime_refs.append('static/images/' + base + ext)
    dynamic.append({
        'source': 'server.py get_chapter_images() + templates/index.html '
                  '<picture> siblings (highest version per chapter)',
        'paths': runtime_refs,
    })

    # ── classify ──────────────────────────────────────────────
    missing = {}
    existing = {}
    for resolved, sites in sorted(refs.items()):
        disk = os.path.join(ROOT, resolved.replace('/', os.sep))
        if os.path.exists(disk):
            existing[resolved] = sites
        else:
            missing[resolved] = sites

    # runtime chapter refs that exist: fold into existing set (no file:line)
    for p in runtime_refs:
        if p not in existing and p not in missing:
            if os.path.exists(os.path.join(ROOT, p.replace('/', os.sep))):
                existing[p] = [('<runtime: server.py chapter-cover pick>', 0, p)]
            else:
                missing[p] = [('<runtime: server.py chapter-cover pick>', 0, p)]

    report = {
        'root': ROOT,
        'scanned_files': len(scan_targets),
        'referenced_and_existing': len(existing),
        'referenced_but_missing': len(missing),
        'missing_detail': {
            p: [f'{f}:{ln}  (ref: {raw})' for f, ln, raw in sites]
            for p, sites in missing.items()
        },
        'dynamic_probes': dynamic,
        'existing_refs': sorted(existing.keys()),
    }

    out = os.path.join(ROOT, 'tools', 'linkcheck.json')
    if '--json' in sys.argv:
        out = sys.argv[sys.argv.index('--json') + 1]
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    print(f'scanned {len(scan_targets)} source files')
    print(f'referenced & existing : {len(existing)}')
    print(f'referenced but MISSING: {len(missing)}')
    for p, sites in sorted(missing.items()):
        print(f'\n  MISSING  {p}')
        for f, ln, raw in sites:
            print(f'           <- {f}:{ln}  (ref: {raw})')
    for d in dynamic:
        n = len(d.get('probe_paths_missing_on_disk', d.get('paths', [])))
        print(f'\n[dynamic] {d["source"]}\n          {n} paths')
    print(f'\nfull report -> {os.path.relpath(out, ROOT)}')
    return 1 if missing else 0


if __name__ == '__main__':
    sys.exit(main())
