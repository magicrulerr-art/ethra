# Ethra Protected Passages — line-anchored do-not-fix markers

**Doctrine:** Ainz-sama's "do not fix" list, made mechanical. Any editorial pass must
check hits against these anchors; a hit inside an anchored range is **read-only** unless
Ainz explicitly directs a change. Anchors carry a verification quote; `compile_canon.py`
flags `ANCHOR-STALE` when the quote drifts from its line window (recompute then required).

**No-cut-without-ruling:** back-half arcs (V–VII) and any cut of meaningful volume
require Ainz's explicit scope ruling first. These markers only ever *protect*; they never
authorize a cut.

## Anchored passages (point ranges)

| id | file | lines | label | verify-quote |
|---|---|---|---|---|
| P1 | chapter-01.md | 170-200 | Kyre-Tree negotiation — Uthgard's charge | the pact with the Kyre Tree—the ancient one |
| P2 | chapter-01.md | 440-630 | Kyre-Tree negotiation — first descent and pact | The Kyre Tree gave the equivalent of a long held breath |
| P3 | chapter-02.md | 210-470 | Kyre-Tree negotiation — chamber of the five families | Waiting for a king who could speak to it as an equal |
| P4 | chapter-04.md | 1095-1190 | Kyre-Tree negotiation / Tree POV — mythic narration | The lord of the desert had been called many things across millions of years |
| P5 | chapter-06.md | 1186-1215 | Tree absolution — White Dawn address | Do not die on the road, White Dawn |

## Class protections (no single anchor — read-only by category)

| id | class | scope | rule |
|---|---|---|---|
| C1 | Ajani's dual register | all chapters | Public speech (double quotes) and internal monologue (single-quoted italics) never "normalized," merged, or re-tagged |
| C2 | Mythic narration | Tree/Deep POV passages, deep-time lines | "millions of years" / 20,000-year figures never normalized; predator voice preserved |
| C3 | Seven-architecture | chapter structure | The seven-part architecture is structural — never collapsed or renumbered for polish |
| C4 | Grief vignettes | Kareth, Lena, and all plain-grief passages | Grief stays plain; no gratuitous "five thousand years" callbacks; no polish-trading |
| C5 | Back-half arcs V–VII | chapter-05/06/07 + arc7 splits | No editorial triage without Ainz's explicit scope ruling |

## Recompute discipline

Anchors were cut 2026-09-01 against masters `content/story/chapter-0*.md`. After any
master edit, run `python canon/compile_canon.py` — stale anchors report as
`ANCHOR-STALE <id>`; re-anchor by hand (the recompute step is formalized as detect-now,
re-anchor-on-flag, matching the arcs.json precedent — no live auto-shifter exists yet).
