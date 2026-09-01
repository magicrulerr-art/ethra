#!/usr/bin/env python3
"""Ethra canon compiler — the DERIVED layer of the canon reference.

Regenerable and disposable. Never hand-edit the output (ledger-derived.md).

    python canon/compile_canon.py           # census + anchor check -> ledger-derived.md
    python canon/compile_canon.py --lint    # + drift lint (frequent names absent from roster)

Doctrine: files are the single source of truth; this ledger is a projection, like
ethra.db. The curated skeleton is canon/roster.md (changes only at canonization events);
everything here is computed from the published masters.
"""
import collections
import datetime
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
STORY = ROOT / "content" / "story"
CANON_DIR = ROOT / "canon"
ROSTER = CANON_DIR / "roster.md"
PROTECTED = CANON_DIR / "protected-passages.md"
OUT = CANON_DIR / "ledger-derived.md"

STOPWORDS = set("""a an and as at be been being but by can could did do does for from
had has have he her hers him his how i if in into is it its just may might more most
must my no not now of off on once one only or our ours out over own same shall she
should so some such than that the their theirs them then there these they this those
through to too under until upon us very was we were what when where which while who
whom why will with would you your yours""".split())

# Races, places, species, titles, and world-terms — expected census noise, not
# candidate characters. Extend as the world grows.
KNOWN_COMMON = set("""
ajani wengari paws paw stripe shadow bright brightmane pyrinae humman hummans human humans
motted veylar veylara threx thrax dragari auruch auruchs styx styxian styxians
snow black flowing all red kyre high hydromancer hydromancers
outside untrustworthy don vein royal flicker heir around instead friends
verdantis verdantian rune belt steadfast flickermarch tidepools xhilva ethra march
city hall ice king queen prince princess tsar tsarina sultan highness wealthiness
majesty ambassador ambassadors general generals regent priest priests speaker
speakers council office tyrant tyrants dawn white golden sun suns tree fire
frostfire plague tide tides deep lament laments quick root rooted convergence aura
blight road pact crown chamber reflection pillars harmonic singer heavenly heaven
scorpion scorpions beetle beetles wolf wolves sunraptor sunraptors woh wohs amuk
amuks anuk anuks shell shells petal petals claw claws silk storms storm walker
walkers dweller dwellers cloaks keeper keepers father mother brother sister cub
cubs chapter arena throne garden gardens desert capital palace gate gates wall
walls caravan caravans merchant merchants champion champions mount mounts ghost
ghosts spore sporefall mycelial abyssal heart chi thak crr zzak lightbringer
uthgar uthgard vane immensity first second third fourth fifth something someone
somewhere everybody everyone everything nothing perhaps because behind before after
about again across also another are beside both beyond come even each every let
please points remember remembered send show take tell thank well whatever without
yes yes tomorrow tonight trade water wind war month next none old good great like
new now out please twenty thirty forty fifty twelve eleven ten nine eight seven
six five four three two one""".split())


def canon_files():
    """Published masters first, then Arc VII splits (flagged)."""
    masters = sorted(STORY.glob("chapter-0*.md"))
    arc7 = sorted((STORY / "chapters").glob("chapter-arc7-*.md"))
    return [(p, p.name.replace("chapter-", "").replace(".md", "")) for p in masters] + \
           [(p, "arc7:" + p.stem.replace("chapter-", "")) for p in arc7]


def strip_markup(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[|\]|\(|\)", " ", text)
    return text


def parse_roster():
    """-> (entries, all_terms). entries: list of dicts; all_terms: {term: name}."""
    entries, all_terms = [], {}
    section = None
    for line in ROSTER.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if not line.startswith("|") or line.startswith("|--") or line.startswith("| id"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() in ("name", "---"):
            continue
        name, alias_cell = cells[0], cells[1]
        status = cells[2] if len(cells) > 2 else ""
        note = cells[3] if len(cells) > 3 else ""
        aliases = [a.strip() for a in alias_cell.split(";")
                   if a.strip() and a.strip() != "-"]
        entries.append({"name": name, "aliases": aliases, "status": status,
                        "note": note, "section": section})
        all_terms[name.lower()] = name
        for a in aliases:
            all_terms[a.lower()] = name
    return entries, all_terms


def census(entries, all_terms):
    """Count every roster term per canon file; record first appearance."""
    files = canon_files()
    counts = {e["name"]: collections.Counter() for e in entries}
    first = {}
    for path, label in files:
        text = strip_markup(path.read_text(encoding="utf-8"))
        low = text.lower()
        for term, name in all_terms.items():
            if len(term) < 3:
                continue
            n = len(re.findall(r"(?<![a-z])" + re.escape(term) + r"(?![a-z])", low))
            if n:
                counts[name][label] += n
                first.setdefault(name, label)
    return counts, first, files


def check_anchors():
    """Verify protected-passage quotes sit within their line window (+/-5)."""
    results = []
    text = PROTECTED.read_text(encoding="utf-8")
    for line in text.splitlines():
        if not line.startswith("| P"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        pid, fname, span, label, quote = cells[0], cells[1], cells[2], cells[3], cells[4]
        target = STORY / fname
        if not target.exists():
            results.append((pid, fname, "MISSING-FILE"))
            continue
        try:
            lo, hi = (int(x) for x in span.split("-"))
        except ValueError:
            results.append((pid, fname, "BAD-SPAN"))
            continue
        lines = target.read_text(encoding="utf-8").splitlines()
        window = "\n".join(lines[max(0, lo - 6):min(len(lines), hi + 5)])
        ok = quote.lower() in window.lower()
        results.append((pid, fname, "OK" if ok else "ANCHOR-STALE"))
    return results


def drift_lint(all_terms, min_count=8):
    """Frequent capitalized tokens absent from the roster -> review candidates."""
    known = set(all_terms)
    totals = collections.Counter()
    for path, _label in canon_files():
        text = strip_markup(path.read_text(encoding="utf-8"))
        for tok in re.findall(r"\b([A-Z][a-z]{2,})\b", text):
            totals[tok] += 1
    candidates = []
    for tok, n in totals.most_common():
        if n < min_count:
            break
        if tok.lower() in known or tok.lower() in STOPWORDS \
                or tok.lower() in KNOWN_COMMON:
            continue
        candidates.append((tok, n))
    return candidates


def main():
    lint = "--lint" in sys.argv
    entries, all_terms = parse_roster()
    counts, first, files = census(entries, all_terms)
    anchors = check_anchors()

    out = []
    out.append("# Ethra Canon Ledger — DERIVED (regenerable, never hand-edited)")
    out.append("")
    out.append("Compiled: %s by `canon/compile_canon.py` from %d canon files." %
               (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), len(files)))
    out.append("Source of truth: published masters + canon/roster.md skeleton.")
    out.append("")
    out.append("## Entity census (counts per canonical unit)")
    out.append("")
    out.append("| entity | status | first | total | by unit |")
    out.append("|---|---|---|---|---|")
    for e in entries:
        name = e["name"]
        c = counts[name]
        total = sum(c.values())
        by = ", ".join("%s:%d" % (k, v) for k, v in sorted(c.items())) or "—"
        out.append("| %s | %s | %s | %d | %s |" %
                   (name, e["status"] or "—", first.get(name, "—"), total, by))
    out.append("")
    out.append("## Protected-passage anchor check")
    out.append("")
    for pid, fname, state in anchors:
        out.append("- **%s** %s — %s" % (pid, fname, state))
    if lint:
        out.append("")
        out.append("## Drift lint — frequent names absent from roster (review)")
        out.append("")
        cands = drift_lint(all_terms)
        if cands:
            for tok, n in cands:
                out.append("- %s (%d)" % (tok, n))
        else:
            out.append("- (none above threshold)")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote %s (%d entities, %d anchors%s)" %
          (OUT, len(entries), len(anchors),
           ", lint on" if lint else ""))
    stale = [a for a in anchors if a[2] != "OK"]
    for pid, fname, state in stale:
        print("  ! %s %s: %s" % (pid, fname, state))


if __name__ == "__main__":
    main()
