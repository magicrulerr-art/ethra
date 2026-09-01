#!/usr/bin/env python3
"""
ethra_index.py — Derived SQLite index over the Ethra site.

Doctrine: the FILES remain the source of truth. This database is a
derived, regenerable, disposable index: canon full-text search, chapter
metadata, and the media ledger. If it ever lies, delete ethra.db and
rebuild:  python ethra_index.py build

Subcommands:
  build              rebuild ethra.db from scratch
  search QUERY       full-text search (options: --type, --arc, --limit, --raw)
  stats              summary of what is indexed

doc_type values in corpus_fts:
  canon_chapter      published chapter prose (the canon)
  canon_reference    bestiary / world bible / creature files
  corpus_message     raw conversation corpus (Ainz's directions + drafts)
  raw_draft          raw/arcN work files (directions + superseded drafts)

Canon verification rule: filter --type canon_chapter to see only what is
published; drafts and directions must never masquerade as canon.
"""
import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT, 'ethra.db')
CORPUS_DEFAULT = os.path.join(os.path.dirname(ROOT), 'ethra_full_conversation.json')

TAG_RE = re.compile(r'<[^>]+>')
SCENE_RE = re.compile(r'^\*\*(.+?)\*\*\s*$')
CHAPTER_HDR_RE = re.compile(r'^## Chapter (\d+):\s+(.+?)\s*$')
COVER_RE = re.compile(r'^chapter-arc(\d+)-(\d+)(?:-v(\d+))?\.(png|webp|jpg)$')
ARC5_COVER_RE = re.compile(r'^arc(\d+)-med-arc\1-ch(\d+)-v(\d+)\.(png|webp|jpg)$')


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


def iso_mtime(path):
    return datetime.fromtimestamp(os.path.getmtime(path), timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def strip_tags(text):
    return TAG_RE.sub(' ', text)


# ── build ────────────────────────────────────────────────────────────────

def build(corpus_path):
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executescript('''
    CREATE TABLE chapters (
        id TEXT PRIMARY KEY, arc INTEGER, chapter INTEGER, title TEXT,
        path TEXT, words INTEGER, scenes TEXT, file_size INTEGER,
        sha256 TEXT, mtime TEXT
    );
    CREATE TABLE media (
        path TEXT PRIMARY KEY, stem TEXT, kind TEXT,
        arc INTEGER, chapter INTEGER, version INTEGER,
        ext TEXT, file_size INTEGER, sha256 TEXT, mtime TEXT
    );
    CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
    ''')
    c.execute('''CREATE VIRTUAL TABLE corpus_fts USING fts5(
        doc_type UNINDEXED, source UNINDEXED, arc UNINDEXED,
        chapter UNINDEXED, role UNINDEXED, inserted_at UNINDEXED, body)''')

    n_ch = index_chapters(c)
    n_media = index_media(c)
    n_ref = index_canon_references(c)
    n_raw = index_raw_drafts(c)
    n_msg = index_corpus(c, corpus_path)

    c.execute("INSERT INTO meta VALUES ('built_at', ?)", (datetime.now(timezone.utc).isoformat(),))
    c.execute("INSERT INTO meta VALUES ('corpus', ?)", (corpus_path if os.path.exists(corpus_path) else 'MISSING',))
    conn.commit()
    size_mb = os.path.getsize(DB_PATH) / 1048576
    print(f'ethra.db built: {size_mb:.1f} MB')
    print(f'  chapters:        {n_ch}')
    print(f'  media files:     {n_media}')
    print(f'  canon refs:      {n_ref}')
    print(f'  raw drafts:      {n_raw}')
    print(f'  corpus messages: {n_msg}')
    conn.close()


def index_chapters(c):
    chdir = os.path.join(ROOT, 'content', 'story', 'chapters')
    n = 0
    for fn in sorted(os.listdir(chdir)):
        if not re.match(r'^chapter-arc\d+-\d+\.md$', fn):
            continue
        path = os.path.join(chdir, fn)
        text = open(path, encoding='utf-8').read()
        m = re.match(r'^chapter-arc(\d+)-(\d+)\.md$', fn)
        arc, chapter = int(m.group(1)), int(m.group(2))
        title = ''
        for line in text.splitlines():
            hm = CHAPTER_HDR_RE.match(line)
            if hm:
                title = hm.group(2)
                break
        scenes = '|'.join(SCENE_RE.match(l).group(1) for l in text.splitlines() if SCENE_RE.match(l))
        body = strip_tags(text)
        c.execute('INSERT INTO chapters VALUES (?,?,?,?,?,?,?,?,?,?)', (
            f'arc{arc}-ch{chapter:02d}', arc, chapter, title, fn,
            len(body.split()), scenes, os.path.getsize(path),
            sha256_of(path), iso_mtime(path)))
        c.execute('INSERT INTO corpus_fts VALUES (?,?,?,?,?,?,?)', (
            'canon_chapter', fn, arc, chapter, '', '', body))
        n += 1
    return n


def index_media(c):
    imgdir = os.path.join(ROOT, 'static', 'images')
    n = 0
    for dp, dirs, fs in os.walk(imgdir):
        dirs[:] = [d for d in dirs if d not in ('_archive', 'thumbnails')]
        for fn in sorted(fs):
            path = os.path.join(dp, fn)
            rel = os.path.relpath(path, imgdir).replace('\\', '/')
            stem, ext = os.path.splitext(fn)
            ext = ext.lstrip('.').lower()
            kind, arc, chapter, version = 'asset', None, None, None
            if ext == 'md':
                kind = 'ledger' if stem == 'CANONICAL_VERSIONS' else 'prompt_record'
            else:
                cm = COVER_RE.match(fn)
                a5 = ARC5_COVER_RE.match(fn)
                if cm:
                    kind = 'cover'
                    arc, chapter = int(cm.group(1)), int(cm.group(2))
                    version = int(cm.group(3)) if cm.group(3) else 0
                    stem = f'chapter-arc{arc}-{chapter}'
                elif a5:
                    kind = 'cover'
                    arc, chapter, version = int(a5.group(1)), int(a5.group(2)), int(a5.group(3))
                    stem = f'chapter-arc{arc}-{chapter}'
                else:
                    vm = re.match(r'^(.*?)-v(\d+)$', stem)
                    if vm:
                        version = int(vm.group(2))
                    if stem.startswith('biome-'):
                        kind = 'biome'
                    elif stem.startswith('city-'):
                        kind = 'city'
                    elif stem.startswith('map-'):
                        kind = 'map'
                    else:
                        kind = 'portrait'
            c.execute('INSERT OR REPLACE INTO media VALUES (?,?,?,?,?,?,?,?,?,?)', (
                rel, stem, kind, arc, chapter, version, ext,
                os.path.getsize(path), sha256_of(path), iso_mtime(path)))
            n += 1
    return n


def index_canon_references(c):
    n = 0
    targets = [
        os.path.join(ROOT, 'content', 'bestiary.md'),
        os.path.join(ROOT, 'content', 'world.md'),
    ]
    cdir = os.path.join(ROOT, 'content', 'creatures')
    if os.path.isdir(cdir):
        for dp, _, fs in os.walk(cdir):
            targets += [os.path.join(dp, f) for f in sorted(fs) if f.endswith('.md')]
    cdir = os.path.join(ROOT, 'canon')
    if os.path.isdir(cdir):
        targets += [os.path.join(cdir, f) for f in sorted(os.listdir(cdir))
                    if f.endswith('.md')]
    for path in targets:
        if not os.path.exists(path):
            continue
        rel = os.path.relpath(path, ROOT).replace('\\', '/')
        body = strip_tags(open(path, encoding='utf-8').read())
        c.execute('INSERT INTO corpus_fts VALUES (?,?,?,?,?,?,?)', (
            'canon_reference', rel, None, None, '', '', body))
        n += 1
    # Adjudicated rulings — indexed in place from digest/ (never moved/duplicated)
    ws = os.path.dirname(ROOT)
    rulings = [
        os.path.join(ws, 'digest', 'personal', 'ethra-canon-rulings.md'),
        os.path.join(ws, 'digest', 'wiki',
                     'ethra-canonical-identity-state-kira-and-mira.md'),
        os.path.join(ws, 'digest', 'personal',
                     'ainz-protected-content-and-no-cut-without-ruling.md'),
    ]
    for path in rulings:
        if not os.path.exists(path):
            continue
        rel = os.path.relpath(path, ws).replace('\\', '/')
        body = strip_tags(open(path, encoding='utf-8').read())
        c.execute('INSERT INTO corpus_fts VALUES (?,?,?,?,?,?,?)', (
            'ruling', rel, None, None, '', '', body))
        n += 1
    return n


def index_raw_drafts(c):
    n = 0
    rawroot = os.path.join(ROOT, 'raw')
    if not os.path.isdir(rawroot):
        return 0
    for dp, _, fs in os.walk(rawroot):
        for fn in sorted(fs):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(dp, fn)
            rel = os.path.relpath(path, ROOT).replace('\\', '/')
            am = re.search(r'arc(\d+)', rel)
            body = open(path, encoding='utf-8').read()
            c.execute('INSERT INTO corpus_fts VALUES (?,?,?,?,?,?,?)', (
                'raw_draft', rel, int(am.group(1)) if am else None, None, '', '', body))
            n += 1
    return n


def index_corpus(c, corpus_path):
    if not os.path.exists(corpus_path):
        print(f'  (corpus not found at {corpus_path} — skipped)')
        return 0
    data = json.load(open(corpus_path, encoding='utf-8'))
    messages = data.get('data', {}).get('biz_data', {}).get('messages', [])
    n = 0
    for msg in messages:
        content = msg.get('content') or ''
        if isinstance(content, list):
            content = '\n'.join(p.get('text', '') for p in content if isinstance(p, dict))
        if not content.strip():
            continue
        c.execute('INSERT INTO corpus_fts VALUES (?,?,?,?,?,?,?)', (
            'corpus_message', str(msg.get('message_id', '')), None, None,
            msg.get('role', ''), msg.get('inserted_at', ''), content))
        n += 1
    return n


# ── search ───────────────────────────────────────────────────────────────

def fts_query(text, raw):
    if raw:
        return text
    tokens = [t for t in text.split() if t]
    if len(tokens) == 1:
        return '"%s"' % tokens[0].replace('"', '')
    # default: exact phrase (ordered adjacency) — precision for canon checks
    return '"%s"' % ' '.join(t.replace('"', '') for t in tokens)


def search(query, doc_type=None, arc=None, limit=10, raw=False):
    if not os.path.exists(DB_PATH):
        sys.exit('ethra.db not found — run: python ethra_index.py build')
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    where = ['corpus_fts MATCH ?']
    args = [fts_query(query, raw)]
    if doc_type:
        where.append('doc_type = ?')
        args.append(doc_type)
    if arc is not None:
        where.append('arc = ?')
        args.append(arc)
    sql = ('''SELECT doc_type, source, arc, chapter, role, inserted_at,
                     snippet(corpus_fts, 6, '[[', ']]', ' … ', 14)
              FROM corpus_fts WHERE %s
              ORDER BY rank LIMIT ?''' % ' AND '.join(where))
    args.append(limit)
    rows = c.execute(sql, args).fetchall()
    if not rows:
        print('no matches')
        return
    for dt, src, a, ch, role, ts, snip in rows:
        loc = src
        if dt == 'canon_chapter':
            loc = f'arc{a} ch{ch} ({src})'
        elif dt == 'corpus_message':
            loc = f'msg {src} · {role} · {ts}'
        print(f'[{dt}] {loc}')
        print(f'    {snip}')
    conn.close()


def stats():
    if not os.path.exists(DB_PATH):
        sys.exit('ethra.db not found — run: python ethra_index.py build')
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    print('ethra.db — %s' % (datetime.fromtimestamp(os.path.getmtime(DB_PATH)).strftime('%Y-%m-%d %H:%M')))
    for k, v in c.execute('SELECT key, value FROM meta'):
        print(f'  {k}: {v}')
    print('  fts documents by type:')
    for dt, n in c.execute('SELECT doc_type, COUNT(*) FROM corpus_fts GROUP BY doc_type ORDER BY 2 DESC'):
        print(f'    {dt:<16} {n}')
    print('  media by kind:')
    for kind, n in c.execute('SELECT kind, COUNT(*) FROM media GROUP BY kind ORDER BY 2 DESC'):
        print(f'    {kind:<16} {n}')
    total_words = c.execute('SELECT SUM(words) FROM chapters').fetchone()[0]
    print(f'  published words: {total_words}')
    conn.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Ethra derived index (files remain canon)')
    sub = ap.add_subparsers(dest='cmd', required=True)
    pb = sub.add_parser('build')
    pb.add_argument('--corpus', default=CORPUS_DEFAULT)
    ps = sub.add_parser('search')
    ps.add_argument('query')
    ps.add_argument('--type', dest='doc_type', default=None,
                    help='canon_chapter|canon_reference|corpus_message|raw_draft')
    ps.add_argument('--arc', type=int, default=None)
    ps.add_argument('--limit', type=int, default=10)
    ps.add_argument('--raw', action='store_true', help='pass query as raw FTS5 syntax')
    sub.add_parser('stats')
    a = ap.parse_args()
    if a.cmd == 'build':
        build(a.corpus)
    elif a.cmd == 'search':
        search(a.query, a.doc_type, a.arc, a.limit, a.raw)
    else:
        stats()
