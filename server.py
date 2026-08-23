"""
╔══════════════════════════════════════════════════════════════╗
║                     ETHRA — THE GREAT ORRERY                 ║
║              Content-Driven Internal Site Server              ║
║   Add a chapter: drop arcXX-chYY.md into content/story/chapters/ ║
║   Add to bestiary: edit content/bestiary.md                  ║
╚══════════════════════════════════════════════════════════════╝
"""
import os
import re
import json
import glob
import gzip
import io
import hashlib
from datetime import datetime
from collections import OrderedDict
from flask import Flask, render_template, jsonify, send_from_directory, request
from flask_compress import Compress

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# ── Paths ──────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
STORY_DIR = os.path.join(CONTENT_DIR, "story")
CHAPTERS_DIR = os.path.join(STORY_DIR, "chapters")
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# ── Public URL Prefix (C1 mechanism) ───────────────────────
# When serving through a public proxy (Tailscale Funnel on /), all relative
# asset/API URLs in rendered HTML need to carry `/ethra` so the browser hits
# <public>/ethra/static/<file> instead of <public>/static/<file> (which the
# proxy has no rule for). Set via PUBLIC_URL_PREFIX env var; empty default.
PUBLIC_URL_PREFIX = os.environ.get('PUBLIC_URL_PREFIX', '').rstrip('/')

app.template_folder = TEMPLATES_DIR

# ── Tailscale Path Rewrite Middleware ──────────────────────
class EthraPrefixMiddleware:
    """
    Strip a configurable mount-point prefix from PATH_INFO so Flask can
    route at '/' regardless of whether the request arrived via Tailscale
    Serve (mounted at /ethra) or Tailscale Funnel (mounted at /).

    Configurable via the ETHRA_PREFIX environment variable.
    Default is '/ethra' for backward compatibility with historical Tailnet
    Serve configs.
    """
    DEFAULT_PREFIX = '/ethra'

    def __init__(self, app, prefix=None):
        self.app = app
        self.prefix = prefix or os.environ.get('ETHRA_PREFIX', self.DEFAULT_PREFIX)

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '')
        if path.startswith(self.prefix):
            new_path = path[len(self.prefix):] or '/'
            environ['PATH_INFO'] = new_path
            # Strip matching prefix from SCRIPT_NAME too so Flask's url_for works
            environ['SCRIPT_NAME'] = self.prefix
        return self.app(environ, start_response)

app.wsgi_app = EthraPrefixMiddleware(app.wsgi_app)

# ── Aggressive compression: Flask-Compress only (single registration) ──
# PREVIOUSLY this block had a second `Compress(app)` call AFTER the first one
# earlier in the file (line ~38 region), which double-registered the
# compression middleware. Flask-Compress was already initialized once at
# top-of-file, so the second call corrupted the response pipeline and
# surfaced as a 500 Internal Server Error on text/html routes
# (e.g. /static/Ethra_viewer.html). Consolidated here: config knobs only,
# single Compress(app) — Compress(app) lives at the top of this file now.
#
# Strategy knobs:
#   • brotli at level 11   (best ratio; ~10-15% smaller than Flask-Compress default 5)
#   • gzip at level 9      (best ratio; ~5% smaller than default 6)
#   • min size 200 B       (compress even tiny payloads — Funnel relays penalize every byte)
#   • extended mimetypes   (include image/svg+xml which compresses ~80%)
app.config['COMPRESS_ALGORITHM'] = ['br', 'gzip']
app.config['COMPRESS_BR_LEVEL'] = 11
app.config['COMPRESS_GZIP_LEVEL'] = 9
app.config['COMPRESS_MIN_SIZE'] = 200
app.config['COMPRESS_MIMETYPES'] = [
    'text/html',
    'text/css',
    'text/xml',
    'text/javascript',
    'application/json',
    'application/javascript',
    'application/xml',
    'application/xhtml+xml',
    'application/rss+xml',
    'application/atom+xml',
    'image/svg+xml',
]

# Single registration of Flask-Compress (was previously double-registered,
# causing 500s on text/html routes). All config knobs above are consumed here.
Compress(app)

# ── Cache busting for HTML responses ───────────────────────
# We edit templates/index.html frequently during fix-iteration sessions, and
# client browsers (especially mobile) tend to cache the previous version. By
# emitting no-cache headers on the rendered HTML response, we force a fresh
# fetch on every page load. This is now the SINGLE after_request hook in this
# file (was previously `_no_cache_html` baked into app.after_request, which
# collided with the duplicated `add_cache_headers` registration below and
# produced 500s on text/html responses). Static .css/.js/images use the
# default 24h cache because they're versioned (chapter-arc4-05-v8.png) or
# fingerprinted assets.
@app.after_request
def _no_cache_html(response):
    ct = response.headers.get('Content-Type', '')
    if 'text/html' in ct or 'application/xhtml' in ct or ct == '':
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

# ── HTML Minification Filter (post-compress) ──────────────
# Remove inter-tag whitespace + HTML comments. Conservative:
# only collapses whitespace BETWEEN TAGS (``>\s+<`` -> ``><``) and
# only strips ``<!-- ... -->`` block comments. Never touches text inside
# <pre>, <code>, <textarea>, or <script> bodies.
import re as _re_min
def _minify_html(html: str) -> str:
    if not isinstance(html, str):
        return html
    html = _re_min.sub(r'<!--.*?-->', '', html, flags=_re_min.DOTALL)
    html = _re_min.sub(r'>\s+<', '><', html)
    html = _re_min.sub(r'\n\s*\n+', '\n', html)
    return html.strip()


# ── Caching Headers ────────────────────────────────────────
@app.after_request
def add_cache_headers(response):
    """Add ETag and Cache-Control for non-HTML cacheable content types.

    Strategy (S2 + S9):
      • text/html     → delegated to `_no_cache_html` (this function SKIPS HTML)
      • application/json → public, max-age=300, must-revalidate  (5 min — bestiary updates land faster)
      • image/biome-* → public, max-age=604800, immutable  (7 days — biome art rarely changes)
      • image/png (other) → public, max-age=86400       (24h)

    Note: HTML responses are explicitly skipped here because `_no_cache_html`
    is the single authority on HTML caching. Two after_request hooks both
    touching HTML Cache-Control headers previously caused 500 Internal Server
    Errors on text/html routes (e.g. /static/Ethra_viewer.html).
    """
    ct = response.content_type or ''
    if 'text/html' in ct or 'application/xhtml' in ct:
        # HTML is owned by `_no_cache_html`. Never touch it here.
        return response
    if 'image/' in ct:
        response.cache_control.no_cache = None
        response.cache_control.public = True
        # 7-day immutable for biome art (changes ~once per chapter-arc)
        if request.path.startswith('/static/images/biome-') or request.path.startswith('/static/images/wengari-bestiary.png'):
            response.cache_control.max_age = 604800
            response.cache_control.immutable = True
        else:
            response.cache_control.max_age = 86400
        response.make_conditional(request)
        return response
    if 'application/json' in ct:
        # send_from_directory responses are direct-passthrough: get_data() would
        # raise RuntimeError ("implicit sequence conversion") and 500 the request
        # (seen on /static/data/map-coordinates.json). Only hash in-memory bodies;
        # passthrough files already carry Last-Modified for make_conditional.
        if not response.direct_passthrough:
            etag = hashlib.md5(response.get_data()).hexdigest()
            response.set_etag(etag)
        response.make_conditional(request)
        response.cache_control.public = True
        response.cache_control.max_age = 300        # 5 min, must-revalidate
        return response
    return response

# ── Helper: rewrite static URLs for the active mount point ───────
def rewrite_static_paths(html, root=""):
    """
    Rewrite absolute /static/ and /api/ references in rendered HTML to the
    active mount-root.

    Priority order for root selection:
      1. Explicit `root` arg passed by caller (used by chapter content rendering
         which already knows its mount context)
      2. PUBLIC_URL_PREFIX env var (set when serving through a public proxy)
      3. request.script_root (handle for tailnet Serve)
      4. empty (root-mount)

    Rewrites cover src= and href= for /static/ and the absolute /api/ paths
    emitted by [data-api] navigation in index.html. Relative paths and external
    URLs are untouched.
    """
    if not root:
        try:
            root = PUBLIC_URL_PREFIX or request.script_root or ''
        except Exception:
            root = PUBLIC_URL_PREFIX or ''

    if not root:
        return html

    # /static/ assets
    html = html.replace('src="/static/', f'src="{root}/static/')
    html = html.replace('href="/static/', f'href="{root}/static/')
    # /api/ endpoints (data-api attributes and action URLs)
    html = html.replace('src="/api/', f'src="{root}/api/')
    html = html.replace('href="/api/', f'href="{root}/api/')
    html = html.replace('"/api/', f'"{root}/api/')  # bare /api/ for fetch() strings
    # fetch('/api/...') and fetch("/api/...") json calls
    html = html.replace("'/api/", f"'{root}/api/")
    # Form action attributes
    html = html.replace('action="/api/', f'action="{root}/api/')
    return html


def _swap_bestiary_to_thumbnails(html: str) -> str:
    """
    Rewrite bestiary <picture> tags so the gallery loads thumbnails (~5-10 KB)
    while the full-size WebP/JPEG/PNG remain available in data-* attributes for
    a click-to-zoom modal.

    Pattern targeted (after markdown rendering, before rewrite_static_paths):
        <picture>
          <source srcset="/static/images/{name}.webp" type="image/webp" />
          <source srcset="/static/images/{name}.jpg"  type="image/jpeg" />
          <img    src="/static/images/{name}.png" alt="..." class="..." />
        </picture>

    Rewrite to:
        <picture data-full-webp="/static/images/{name}.webp"
                 data-full-jpg="/static/images/{name}.jpg"
                 data-full-png="/static/images/{name}.png">
          <source srcset="/static/images/thumbnails/{name}.webp" type="image/webp" />
          <img    src="/static/images/thumbnails/{name}.webp" alt="..." class="..." />
          <img class="fullsize-fallback" loading="lazy" hidden />
        </picture>

    Only images that have a thumbnail in static/images/thumbnails/ are rewritten.
    Falls back to the original markup when no thumbnail exists.
    """
    if not html:
        return html
    thumbs_dir = os.path.join(STATIC_DIR, "images", "thumbnails")
    pattern = re.compile(
        r'(<picture[^>]*>)(.*?)(</picture>)',
        flags=re.DOTALL,
    )

    def _has_thumb(name: str) -> bool:
        return os.path.exists(os.path.join(thumbs_dir, f"{name}.webp"))

    def _rewrite_one(match: re.Match) -> str:
        block = match.group(0)
        m = re.search(r'/static/images/([\w\-]+)\.webp', block)
        if not m:
            return block
        name = m.group(1)
        if not _has_thumb(name):
            return block
        # Extract alt text + class to preserve on the <img>
        img_match = re.search(
            r'<img\s+src="/static/images/' + re.escape(name) + r'\.png"\s+alt="([^"]*)"\s+class="([^"]*)"([^>]*)>',
            block,
        )
        alt = img_match.group(1) if img_match else ''
        cls = img_match.group(2) if img_match else 'creature-portrait'
        extra = img_match.group(3) if img_match else ''
        # Original full-size paths stored as data-* for the JS modal
        full_webp = f'/static/images/{name}.webp'
        full_jpg = f'/static/images/{name}.jpg'
        full_png = f'/static/images/{name}.png'
        thumb_webp = f'/static/images/thumbnails/{name}.webp'
        return (
            f'<picture data-full-webp="{full_webp}" '
            f'data-full-jpg="{full_jpg}" data-full-png="{full_png}" '
            f'class="creature-zoomable">'
            f'<source srcset="{thumb_webp}" type="image/webp" />'
            f'<img src="{thumb_webp}" alt="{alt}" class="{cls}" '
            f'loading="lazy" decoding="async"{extra} />'
            f'</picture>'
        )

    return pattern.sub(_rewrite_one, html)


# ── Static Files ──────────────────────────────────────────
# Register WebP MIME type globally so send_from_directory picks it up.
import mimetypes as _mt
_mt.add_type('image/webp', '.webp')
_mt.add_type('image/avif', '.avif')

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)


# ═══════════════════════════════════════════════════════════
#  MARKDOWN PARSER (lightweight — no dependencies)
# ═══════════════════════════════════════════════════════════

def parse_markdown(text):
    lines = text.split('\n')
    html = []
    in_list = False
    list_type = None
    in_para = False
    para_buf = []
    
    def flush_para():
        nonlocal in_para
        if para_buf:
            html.append(f"<p>{' '.join(para_buf)}</p>")
            para_buf.clear()
        in_para = False
    
    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            tag = 'ol' if list_type == 'ol' else 'ul'
            html.append(f'</{tag}>')
            in_list = False
            list_type = None
    
    for line in lines:
        stripped = line.strip()
        
        if stripped.startswith('### '):
            flush_para(); flush_list()
            html.append(f'<h3>{_inline_markdown(stripped[4:])}</h3>')
        elif stripped.startswith('## '):
            flush_para(); flush_list()
            html.append(f'<h2>{_inline_markdown(stripped[3:])}</h2>')
        elif stripped.startswith('# '):
            flush_para(); flush_list()
            html.append(f'<h1>{_inline_markdown(stripped[2:])}</h1>')
        elif stripped.startswith('---') or stripped.startswith('***'):
            flush_para(); flush_list()
            html.append('<hr>')
        elif stripped.startswith('- ') or stripped.startswith('* '):
            flush_para()
            if not in_list or list_type != 'ul':
                flush_list()
                html.append('<ul>')
                in_list = True
                list_type = 'ul'
            html.append(f'<li>{_inline_markdown(stripped[2:])}</li>')
        elif re.match(r'^\d+\.\s', stripped):
            flush_para()
            if not in_list or list_type != 'ol':
                flush_list()
                html.append('<ol>')
                in_list = True
                list_type = 'ol'
            content = re.sub(r'^\d+\.\s', '', stripped)
            html.append(f'<li>{_inline_markdown(content)}</li>')
        elif stripped.startswith('**') and ':**' in stripped:
            flush_para(); flush_list()
            html.append(f'<h4>{_inline_markdown(stripped)}</h4>')
        elif stripped.startswith('|') and stripped.endswith('|'):
            flush_para(); flush_list()
            if '---' in stripped:
                continue
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            is_header = all(c.startswith('**') and c.endswith('**') for c in cells if c)
            if is_header:
                cells_display = [c.strip('*') for c in cells]
                html.append('<table><thead><tr>' + ''.join(f'<th>{c}</th>' for c in cells_display) + '</tr></thead><tbody>')
            else:
                html.append('<tr>' + ''.join(f'<td>{_inline_markdown(c)}</td>' for c in cells) + '</tr>')
        elif stripped.startswith('> '):
            flush_para(); flush_list()
            html.append(f'<blockquote>{_inline_markdown(stripped[2:])}</blockquote>')
        elif (stripped.startswith('<div') or stripped.startswith('</div') or
              stripped.startswith('<span') or stripped.startswith('</span') or
              stripped.startswith('<p class=') or stripped.startswith('</p') or
              stripped.startswith('<hr class=')):
            flush_para(); flush_list()
            html.append(stripped)
        elif not stripped:
            flush_para()
        else:
            flush_list()
            if not in_para:
                in_para = True
            para_buf.append(_inline_markdown(stripped))
    
    flush_para()
    flush_list()
    result = '\n'.join(html)
    result = result.replace('</tbody>\n<table>', '</tbody></table>\n<table>')
    if '<tbody>' in result and '</tbody>' not in result:
        result += '</tbody></table>'
    return result


def _inline_markdown(text):
    html_spans = []
    def _protect(m):
        html_spans.append(m.group(0))
        return f'\x00HTML{len(html_spans)-1}\x00'
    
    text = re.sub(r'<span[^>]*>.*?</span>', _protect, text)
    text = re.sub(r'<p class="[^"]*">', _protect, text)
    text = re.sub(r'</p>', _protect, text)
    text = re.sub(r'<div[^>]*>', _protect, text)
    text = re.sub(r'</div>', _protect, text)
    
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    
    for i, span in enumerate(html_spans):
        text = text.replace(f'\x00HTML{i}\x00', span)
    return text


# ═══════════════════════════════════════════════════════════
#  CONTENT LOADING
# ═══════════════════════════════════════════════════════════

def _load_arc_manifest():
    """Read content/story/arcs.json — the single source of truth for arc
    metadata, shared with regenerate_chapters.py. Adding an arc = one entry
    in that file; no server code change needed. Falls back to an empty
    dict (generic titles) if the manifest is missing or unreadable."""
    try:
        with open(os.path.join(STORY_DIR, 'arcs.json'), 'r', encoding='utf-8') as f:
            return json.load(f).get('arcs', {})
    except (OSError, ValueError):
        return {}

ARC_META = _load_arc_manifest()
ARC_TITLES = {int(k): v.get('title', f"Arc {k}") for k, v in ARC_META.items()}

def load_md(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return parse_markdown(content)


def get_arcs_and_chapters():
    """Scan content/story/chapters/ for chapter-arcX-YY.md files.
    Returns OrderedDict: {arc_num: {'title': ..., 'chapters': [...]}}"""
    pattern = os.path.join(CHAPTERS_DIR, "chapter-arc*.md")
    files = sorted(glob.glob(pattern))
    
    arcs = OrderedDict()
    for f in files:
        basename = os.path.basename(f)
        m = re.match(r'chapter-arc(\d+)-(\d+)\.md', basename)
        if not m:
            continue
        arc_num = int(m.group(1))
        ch_num = int(m.group(2))
        
        # Parse chapter title from file content
        title = f"Chapter {ch_num}"
        try:
            with open(f, 'r', encoding='utf-8') as cf:
                first = cf.read(500)
                h2 = re.search(r'^## Chapter \d+:\s+(.+)$', first, re.MULTILINE)
                if h2:
                    title = h2.group(1)
        except:
            pass
        
        if arc_num not in arcs:
            arcs[arc_num] = {
                'title': ARC_TITLES.get(arc_num, f"Arc {arc_num}"),
                'chapters': []
            }
        
        arcs[arc_num]['chapters'].append({
            'arc_num': arc_num,
            'ch_num': ch_num,
            'filename': basename,
            'title': title,
            'id': f"arc{arc_num}-ch{ch_num:02d}",
        })

    # Attach sequential-navigation markers (First / Prev / Next / Last),
    # walking all chapters in arc+chapter order across all arcs as one
    # flat sequence. This lets the template render Previous/Next/Go-to-End
    # buttons without needing to know arc boundaries.
    flat = []
    for arc_num in sorted(arcs.keys()):
        for ch in arcs[arc_num]['chapters']:
            flat.append(ch)

    if flat:
        first_id = flat[0]['id']
        last_id = flat[-1]['id']
        for idx, ch in enumerate(flat):
            ch['is_first'] = (idx == 0)
            ch['is_last'] = (idx == len(flat) - 1)
            ch['prev_id'] = flat[idx - 1]['id'] if idx > 0 else first_id
            ch['next_id'] = flat[idx + 1]['id'] if idx < len(flat) - 1 else last_id
            ch['prev_title'] = flat[idx - 1]['title'] if idx > 0 else flat[0]['title']
            ch['next_title'] = flat[idx + 1]['title'] if idx < len(flat) - 1 else flat[-1]['title']
            ch['first_id'] = first_id
            ch['last_id'] = last_id
            ch['flat_index'] = idx + 1
            ch['flat_total'] = len(flat)

    return arcs


# ═══════════════════════════════════════════════════════════
#  CHAPTER IMAGE DETECTION
# ═══════════════════════════════════════════════════════════

def static_image_exists(name):
    """True if STATIC_DIR/<name> is on disk — the template uses this to
    avoid emitting <picture> sources for derivatives that were never
    generated (a missing WebP source would otherwise break the image)."""
    return os.path.exists(os.path.join(STATIC_DIR, name))


def get_chapter_images():
    """Scan static/images/ for chapter images and return a dict of ch.id -> image filename.
    Prefers the highest version number (e.g. -v3 over -v2 over base)."""
    image_dir = os.path.join(STATIC_DIR, "images")
    chapter_images = {}
    if not os.path.isdir(image_dir):
        return chapter_images
    for f in os.listdir(image_dir):
        m = re.match(r'chapter-arc(\d+)-(\d+)(-v\d+)?\.png$', f)
        if not m:
            continue
        arc_num = int(m.group(1))
        ch_num = int(m.group(2))
        version = m.group(3) or ''
        ch_id = f"arc{arc_num}-ch{ch_num:02d}"
        # Prefer higher version numbers
        if ch_id not in chapter_images:
            chapter_images[ch_id] = f
        elif version > '' and (chapter_images[ch_id].count('-v') == 0 or
              int(version[2:]) > int(chapter_images[ch_id].split('-v')[-1].split('.')[0])):
            chapter_images[ch_id] = f
    return chapter_images


# ═══════════════════════════════════════════════════════════
#  ROUTES
# ═══════════════════════════════════════════════════════════

@app.route("/")
def index():
    bestiary_html = load_md(os.path.join(CONTENT_DIR, "bestiary.md")) or "<p><em>Bestiary content not found.</em></p>"
    world_html = load_md(os.path.join(CONTENT_DIR, "world.md")) or "<p><em>World content not found.</em></p>"
    arcs = get_arcs_and_chapters()

    # Lazy chapter loading: chapters are no longer inlined into the index page.
    # Each chapter is fetched on demand via /api/chapter/<id> by index.html JS.
    # The skeleton still passes an EMPTY chapter_content dict so the template
    # renders empty chapter-content divs with the correct ids (data-chapter
    # hooks for lazy fetch). This is what drops GET / from ~2 MB to ~30 KB.

    # Detect which chapter images exist
    chapter_images = get_chapter_images()

    # Rewrite static paths for active mount point (Tailscale Serve adds /ethra, Funnel keeps root)
    root = request.script_root
    # Bestiary gallery uses thumbnails by default (~7 KB ea vs ~200 KB originals).
    # Click handler in index.html opens the full-size image in a modal.
    bestiary_html = _swap_bestiary_to_thumbnails(bestiary_html)
    bestiary_html = rewrite_static_paths(bestiary_html, root)
    world_html = rewrite_static_paths(world_html, root)

    html = render_template(
        "index.html",
        bestiary_content="",         # LAZY: served via /api/bestiary on first access
        world_content=world_html,
        arcs=arcs,
        chapter_content={},          # LAZY: served via /api/chapter/<id>
        chapter_images=chapter_images,
        image_exists=static_image_exists,
        current_year=datetime.now().year
    )
    # Rewrite hardcoded paths in the template itself (landing page, JavaScript)
    html = rewrite_static_paths(html, request.script_root)

    # Strategy (S7): Minify rendered HTML before sending. Runs AFTER
    # Flask-Compress so the wire bytes are unminified-then-compressed —
    # compression handles whitespace better when it sees runs together.
    html = _minify_html(html)
    return html

@app.route("/api/bestiary")
def api_bestiary():
    """Return the bestiary content HTML on demand.

    Used by index.html JS to lazy-load the bestiary section instead of
    inlining all 60+ thumbnails (~2 MB) into the initial page load.
    """
    bestiary_html = load_md(os.path.join(CONTENT_DIR, "bestiary.md")) or "<p><em>Bestiary content not found.</em></p>"
    bestiary_html = _swap_bestiary_to_thumbnails(bestiary_html)
    bestiary_html = rewrite_static_paths(bestiary_html, request.script_root)
    return jsonify({'content': bestiary_html})


@app.route("/api/navigation")
def api_navigation():
    arcs = get_arcs_and_chapters()
    arc_list = []
    for arc_num, arc in arcs.items():
        arc_list.append({
            'id': f'arc{arc_num:02d}',
            'label': arc['title'],
            'chapters': arc['chapters']
        })
    return jsonify({
        'sections': [
            {'id': 'bestiary', 'label': 'Bestiary'},
            {'id': 'world', 'label': 'World of Ethra'},
            {'id': 'story', 'label': 'Story of Ajani', 'arcs': arc_list}
        ]
    })

@app.route("/api/chapter/<chapter_id>")
def api_chapter(chapter_id):
    """Return a single chapter's rendered HTML on demand.

    Used by index.html JS to lazy-load chapter content on tab click instead of
    inlining all 32 chapters into the initial page (was 2 MB / 1.94 MB unmin).
    """
    arcs = get_arcs_and_chapters()
    target = None
    for arc_num, arc in arcs.items():
        for ch in arc['chapters']:
            if ch['id'] == chapter_id:
                target = ch
                break
        if target:
            break
    if not target:
        return ("Chapter not found: " + str(chapter_id), 404)
    html = load_md(os.path.join(CHAPTERS_DIR, target['filename']))
    if not html:
        return ("Chapter markdown unreadable: " + str(chapter_id), 500)
    html = rewrite_static_paths(html, request.script_root)
    return html

@app.route("/api/chapters")
def api_chapters():
    arcs = get_arcs_and_chapters()
    all_chapters = []
    for arc_num, arc in arcs.items():
        for ch in arc['chapters']:
            all_chapters.append(ch)
    return jsonify(all_chapters)

@app.route("/api/health")
def health():
    arcs = get_arcs_and_chapters()
    total = sum(len(arc['chapters']) for arc in arcs.values())
    return jsonify({
        'status': 'ok',
        'project': 'Ethra — The Great Orrery',
        'arcs': len(arcs),
        'chapters': total,
        'timestamp': datetime.now().isoformat()
    })

# ═══════════════════════════════════════════════════════════
#  WORLD SECTION ROUTES
# ═══════════════════════════════════════════════════════════

@app.route("/api/world")
def api_world_sections():
    """List all world sub-sections."""
    world_dir = os.path.join(CONTENT_DIR, "world")
    sections = []
    section_order = ['cosmology', 'magic', 'geography', 'religion', 'history', 'culture']
    section_labels = {
        'cosmology': 'Cosmology: The Twin Fires',
        'magic': 'Magic: Aura & Sorcery',
        'geography': 'Geography: The Six Biomes',
        'religion': 'Religion & Theology',
        'history': 'History: The Five Tyrants',
        'culture': 'Culture & Society'
    }
    for key in section_order:
        filepath = os.path.join(world_dir, f"{key}.md")
        if os.path.exists(filepath):
            sections.append({
                'id': key,
                'label': section_labels.get(key, key.replace('-', ' ').title())
            })
    # Auto-discover any world/*.md files not in the known order — a new
    # lore section is now a one-file drop-in, no code edit needed.
    try:
        for fn in sorted(os.listdir(world_dir)):
            if not fn.endswith('.md'):
                continue
            key = fn[:-3]
            if key not in section_order and os.path.isfile(os.path.join(world_dir, fn)):
                sections.append({
                    'id': key,
                    'label': section_labels.get(key, key.replace('-', ' ').title())
                })
    except OSError:
        pass
    return jsonify(sections)

@app.route("/api/world/<section>")
def api_world_section(section):
    """Get individual world section content."""
    filepath = os.path.join(CONTENT_DIR, "world", f"{section}.md")
    if not os.path.exists(filepath):
        return jsonify({'error': 'Section not found'}), 404
    html = load_md(filepath) or "<p><em>Section content not found.</em></p>"
    html = rewrite_static_paths(html, request.script_root)
    return jsonify({
        'id': section,
        'content': html
    })

# ═══════════════════════════════════════════════════════════
#  CREATURE ROUTES
# ═══════════════════════════════════════════════════════════

@app.route("/api/biomes")
def api_biomes():
    """Lightweight count of creatures per biome for nav badges."""
    """List all biomes and their creatures."""
    creatures_dir = os.path.join(CONTENT_DIR, "creatures")
    biomes = {}
    if os.path.exists(creatures_dir):
        for biome in os.listdir(creatures_dir):
            biome_path = os.path.join(creatures_dir, biome)
            if os.path.isdir(biome_path):
                creatures = []
                for creature in os.listdir(biome_path):
                    if creature.endswith('.md'):
                        creatures.append(creature[:-3])
                biomes[biome] = sorted(creatures)
    return jsonify(biomes)

@app.route("/api/creature/<biome>/<creature_name>")
def api_creature(biome, creature_name):
    """Get individual creature content."""
    filepath = os.path.join(CONTENT_DIR, "creatures", biome, f"{creature_name}.md")
    if not os.path.exists(filepath):
        return jsonify({'error': 'Creature not found'}), 404
    html = load_md(filepath)
    html = rewrite_static_paths(html, request.script_root)
    return jsonify({
        'biome': biome,
        'creature': creature_name,
        'content': html
    })

@app.route("/api/creatures/<biome>")
def api_creatures_by_biome(biome):
    """Get all creature names in a biome."""
    filepath = os.path.join(CONTENT_DIR, "creatures", biome)
    creatures = []
    if os.path.exists(filepath):
        for creature in os.listdir(filepath):
            if creature.endswith('.md'):
                creatures.append(creature[:-3])
    return jsonify(sorted(creatures))


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

    # Merge place pins (P1 drop-in): any content/places/*.md carrying
    # x_pct/y_pct becomes a map pin without touching map-coordinates.json.
    # Frontmatter pins win over same-id entries already in the JSON.
    if os.path.isdir(PLACES_DIR):
        pins = data.setdefault('city_pins', [])
        pin_ids = {p.get('id') for p in pins if isinstance(p, dict)}
        for fn in sorted(os.listdir(PLACES_DIR)):
            if not fn.endswith('.md'):
                continue
            loaded = _read_place(fn[:-3])
            if not loaded:
                continue
            meta, _ = loaded
            if 'x_pct' not in meta or 'y_pct' not in meta:
                continue
            try:
                pin = {
                    'id': meta['slug'],
                    'name': meta.get('name', meta['slug']),
                    'kind': meta.get('kind', 'place'),
                    'x_pct': float(meta['x_pct']),
                    'y_pct': float(meta['y_pct']),
                }
            except (ValueError, TypeError):
                continue
            if pin['id'] in pin_ids:
                continue
            pins.append(pin)
            pin_ids.add(pin['id'])

    return jsonify(data)


# ═══════════════════════════════════════════════════════════
#  PLACES (P1 drop-in) — content/places/<slug>.md with frontmatter
# ═══════════════════════════════════════════════════════════
# A place (city / ruin / landmark) is ONE file:
#   content/places/vashar.md
#   ---
#   name: Vashar
#   kind: city
#   biome: steadfast-desert
#   x_pct: 62.4
#   y_pct: 41.0
#   race: Wengari
#   blurb: The capital of the Wengari kingdoms.
#   ---
#   (gazetteer body in markdown)
# It then appears in /api/places, /api/place/<slug>, and as a pin on the
# map via the city_pins merge in /api/map/coordinates — no code edit.

PLACES_DIR = os.path.join(CONTENT_DIR, "places")

# Slug convention: lowercase letters/digits/hyphens, starting with a
# letter or digit. The filename IS the slug (keystone.md -> slug "keystone").
_PLACE_SLUG_RE = re.compile(r'^[a-z0-9][a-z0-9\-]*$')


def _parse_frontmatter(text):
    """Parse a YAML-lite frontmatter block (flat key: value pairs only).
    Returns (meta_dict, body_text). Files without frontmatter pass through
    with an empty meta dict."""
    meta = {}
    body = text
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip().strip('"\'')
            body = parts[2]
    return meta, body


def _read_place(slug):
    """Read one place file by slug. Returns (meta, body) or None."""
    if not _PLACE_SLUG_RE.match(slug):
        return None
    path = os.path.join(PLACES_DIR, f"{slug}.md")
    if not os.path.isfile(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            meta, body = _parse_frontmatter(f.read())
    except OSError:
        return None
    meta['slug'] = slug
    return meta, body


@app.route("/api/places")
def api_places():
    """List all places with their frontmatter metadata (no body)."""
    places = []
    if os.path.isdir(PLACES_DIR):
        for fn in sorted(os.listdir(PLACES_DIR)):
            if not fn.endswith('.md'):
                continue
            loaded = _read_place(fn[:-3])
            if loaded:
                places.append(loaded[0])
    return jsonify(places)


@app.route("/api/place/<slug>")
def api_place(slug):
    """One place: metadata + rendered gazetteer body."""
    loaded = _read_place(slug)
    if not loaded:
        return jsonify({'error': 'Place not found'}), 404
    meta, body = loaded
    html = rewrite_static_paths(parse_markdown(body), request.script_root)
    return jsonify({**meta, 'content': html})


# ═══════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    port = int(os.environ.get("ETHRA_PORT", 8790))
    arcs = get_arcs_and_chapters()
    total = sum(len(arc['chapters']) for arc in arcs.values())
    print(f"\n  ** ETHRA - The Great Orrery **")
    print(f"  Content-driven site server")
    print(f"  Port: {port}")
    print(f"  Arcs: {len(arcs)}  Chapters: {total}")
    print(f"  Add a chapter: drop chapter-arcX-YY.md into content/story/chapters/")
    print(f"  Ctrl+C to stop\n")

# === DEBUG: WSGI environment inspector
@app.route("/__debug/environ")
def debug_environ():
    """Return WSGI env vars that show what the upstream proxy forwarded. Loopback-only."""
    if request.remote_addr not in ("127.0.0.1", "::1") or request.environ.get("HTTP_X_FORWARDED_FOR"):
        from flask import abort
        abort(403)
    from flask import jsonify
    import werkzeug.wsgi as wz
    keys_of_interest = [
        'PATH_INFO', 'SCRIPT_NAME', 'RAW_URI', 'REQUEST_URI',
        'HTTP_X_FORWARDED_PATH', 'HTTP_X_FORWARDED_PREFIX', 'HTTP_X_FORWARDED_PROTO',
        'HTTP_X_FORWARDED_HOST', 'QUERY_STRING', 'SERVER_NAME', 'SERVER_PORT',
        'HTTP_HOST', 'REMOTE_ADDR',
    ]
    env = {k: request.environ.get(k) for k in keys_of_interest if k in request.environ}
    env['request_script_root'] = request.script_root
    env['request_url_root'] = request.url_root
    env['request_path'] = request.path
    return jsonify(env)

# ═══════════════════════════════════════════════════════════
#  ETHRA INTERACTIVE MAP — Entry Point
# ═══════════════════════════════════════════════════════════

@app.route("/map/")
def ethra_map():
    """Interactive 10-layer map — served from static file, bypass Jinja2."""
    map_path = os.path.join(STATIC_DIR, "ethra_map_standalone.html")
    with open(map_path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Inject PREFIX-aware image path for public proxy
    prefix = request.script_root or ''
    if prefix:
        html = html.replace('/static/', prefix + '/static/')
    return html, 200, {'Content-Type': 'text/html; charset=utf-8'}


# ═══════════════════════════════════════════════════════════
#  MAP EXPORT ENDPOINT — receive data from Azgaar
# ═══════════════════════════════════════════════════════════

MAPS_DIR = os.path.join(STATIC_DIR, "maps")

@app.route("/api/map/upload", methods=["POST"])
def api_map_upload():
    """Receive map export data from Azgaar browser context.
    
    Accepts JSON: { filename: "cells_v2.geojson", data: <JSON-serializable> }
    Saves to ethra_site/static/maps/<filename>.
    """
    payload = request.get_json(force=True, silent=True)
    if not payload:
        return jsonify({"error": "invalid or empty JSON body"}), 400
    filename = payload.get("filename", "")
    if not filename or ".." in filename or "/" in filename or "\\" in filename:
        return jsonify({"error": "invalid filename"}), 400
    data = payload.get("data")
    if data is None:
        return jsonify({"error": "missing 'data' field"}), 400
    filepath = os.path.join(MAPS_DIR, filename)
    os.makedirs(MAPS_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2 if filename.endswith(".geojson") else None, ensure_ascii=False)
    size = os.path.getsize(filepath)
    return jsonify({"ok": True, "filename": filename, "bytes": size})


if __name__ == "__main__":
    # `port` is defined in the __main__ banner block above (module scope).
    # Guarded so `import server` never starts the listener (was previously
    # a bare module-level app.run()).
    app.run(host="0.0.0.0", port=port, debug=False)
