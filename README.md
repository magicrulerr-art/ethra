# Ethra — The Great Orrery

> *An isolated, content-driven internal site for the collaborative world-building project "The Great Orrery."*

## Quick Start

```bash
cd ethra_site
python server.py
```

Visit `http://127.0.0.1:8790` — the site is live.

## Content-Driven Architecture

The site parses Markdown files at request time. **No code changes needed to add content.**

### Adding to the Bestiary
Edit `content/bestiary.md`. Save. Refresh. Done.

### Adding to the World Bible
Edit `content/world.md`. Save. Refresh. Done.

### Adding a New Chapter
Drop a new `.md` file into `content/story/` with the naming convention:

```
content/story/chapter-07.md   →  auto-detected as "Chapter 7"
content/story/chapter-08.md   →  auto-detected as "Chapter 8"
```

The server scans `content/story/chapter-*.md` on every request and builds the navigation dynamically.

### Adding Images
Place images in `static/images/` with matching filenames:

```
static/images/chapter-01.png   →  appears after Chapter One
static/images/chapter-02.png   →  appears after Chapter Two
```

Each chapter end has a styled image placeholder that hints at the expected filename.

## Structure

```
ethra_site/
├── server.py              # Flask server (port 8790)
├── content/
│   ├── bestiary.md        # Bestiary of Ethra
│   ├── world.md           # World of Ethra
│   └── story/
│       ├── chapter-01.md  # The White Dawn
│       ├── chapter-02.md  # Council of the Families
│       ├── chapter-03.md  # The Tournament
│       ├── chapter-04.md  # Consolidation I
│       ├── chapter-05.md  # Consolidation II
│       └── chapter-06.md  # Consolidation III
├── static/
│   ├── css/               # CSS overrides (if needed)
│   └── images/            # Chapter illustrations
└── templates/
    └── index.html          # Ethra-themed single-page app
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Main site (all sections, all chapters) |
| `/api/health` | Health check (status, chapter count) |
| `/api/navigation` | Navigation structure as JSON |
| `/api/chapters` | Chapter list as JSON |
| `/static/<path>` | Static file serving |

## Tailscale Deployment

To expose via Tailscale:

```bash
tailscale serve --bg /ethra http://127.0.0.1:8790
```

The middleware rewrites `/ethra/*` paths automatically.

## Theme

- **Steadfast Gold** — `#c9a059` — the stable sun, Sorcery, knowledge
- **Flicker Crimson** — `#8b2a2a` — the wandering sun, Aura, instinct
- **Deep Midnight** — `#0a1628` — the abyss between stars

## Requirements

- Python 3.8+
- Flask (`pip install flask`)
- No other dependencies — Markdown parser is built-in
