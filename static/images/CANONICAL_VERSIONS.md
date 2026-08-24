# CANONICAL_VERSIONS.md — Ethra Chapter Cover Illustrations

> ## 2026-08-23 RULING (Ainz-sama): LIVE IS CANONICAL
> When disk, ledger, live server, and memory disagree, the LIVE server state is the truth.
> Applied this turn: supercontinent map series canonical = what is live (template references
> `map-supercontinent-v2.png`; disk holds v1–v4 only). The `v186` lock below and the
> 2026-08-22 "v190 sync" claim are DEMOTED to historical claims (files absent on disk;
> live server 404s both). Do NOT rebuild toward v186/v190. Before any new map work,
> re-baseline this ledger from the live state in the same turn.

> Last updated: 2026-08-23
> Maintained by: Mare Bello Fiore (Guardian of the Sixth Floor)
> Authority: this file is the single source of truth for which illustration
> version is currently shipped as a chapter cover on the Ethra site.
> Updated on lock-in. Source-of-truth precedence: this file → chapter-md
> → arc-XX.md → memory ledger. If they disagree, this file wins.

---

## Site Asset — Supercontinent Map (Bestiary landing)

| Asset                         | Status      | Canonical filename                       | Bytes     | SHA-256 (prefix) | Locked |
|-------------------------------|-------------|------------------------------------------|-----------|------------------|--------|
| Ethra vector SVG (5-biome canonical, self-authored) | 🟡 PATCHED v2 (pending Ainz verdict) | `~/Downloads/Ethra_current.svg` (+ `Ethra_viewer.html`) | 243,613 | `36a35a3d…`       | 2026-07-11 (verdict pending — Ainz to choose accept / iterate / rebuild) |
| Ethra supercontinent panorama (Qwen-Image sepia forge) | 🟡 FORGED v1 | `map-supercontinent-v1.png` (+`.jpg`,`.webp`) | 3,609,119 | `45639e8c…`       | 2026-06-29 (pending Ainz verdict) |

**Latest vector-SVG v2 patches (2026-07-11)**:
- Marine label added to `<g id="region-labels">` at viewBox (1517.9, 43). All 5 region names now present.
- Twin-suns emitted as small disc + smaller disc with combined label "Steadfast · Flicker" (top-right corner, viewBox (2026.56, 38)).
- **Compass rose patch did NOT land** in the on-disk file: `<g id="compass">` group is absent. Reseed required before Ainz verdict — possibly an out-of-band editor overrode the patch.
- `Ethra_viewer.html` is inlined-SVG mirror at 250,493 bytes (`46d488ea…`). 11 layer toggles wired; Show All / Hide All / Biomes-Only buttons functional.

Forge prompt + iteration log: `static/images/map-supercontinent-v1-PROMPT-RECORD.md`.

Drift trade-off acknowledged (v1 of 3 iteration budget): Qwen-Image 2.0 produced
sepia-tonal composition with partial label drift (`compass rose` → `compass nose`;
region cartouches fragmented). Forging stops at v1 per session budget. Ainz may
(a) accept v1 and proceed, (b) request a fresh forge with different anchor,
or (c) composite a parchment background onto a structurally-cleaner base map.

Reusable for future culture/society city-pin overlay (see Phase 5 of the
Bestiary plan). Coordinate data lives at `static/data/map-coordinates.json`.

## Mapping rule
- For chapter `arc{X}-{YY}`:
  - If `chapter-arc{X}-{YY}-v{N}.png` is listed → that {N} is canonical.
  - Otherwise `chapter-arc{X}-{YY}.png` (unversioned) is canonical.
- A version is canonical **only** when the bytes on disk match the
  recorded size and Ainz-sama has approved it.
- Previous versions (v1..v(N-1)) are **NOT deleted** — they form the
  historical record and are referenced by mistake-cadence logs.

---

## Arc 1 — Threshold of Stars

| Chapter | Title | Status | Canonical filename | Bytes | Locked |
|---------|-------|--------|--------------------|-------|--------|
| arc1-01 | Through the Long Dry | 🟡 pre-Mare history | `chapter-arc1-01-v3.png` | — | pre-2026-06 |
| arc1-02 | (TBD) | 🟡 pre-Mare history | `chapter-arc1-02-v3.png` | — | pre-2026-06 |
| arc1-03 | (TBD) | 🟡 pre-Mare history | `chapter-arc1-03-v2.png` | — | pre-2026-06 |
| arc1-04 | (TBD) | 🟡 pre-Mare history | `chapter-arc1-04-v2.png` | — | pre-2026-06 |
| arc1-05 | (TBD) | 🟡 pre-Mare history | `chapter-arc1-05.png` | — | pre-2026-06 |
| arc1-06 | (TBD) | 🟡 pre-Mare history | `chapter-arc1-06-v2.png` | — | pre-2026-06 |

## Arc 2 — The Bone-Colored Peace

| Chapter | Title | Status | Canonical filename | Bytes | Locked |
|---------|-------|--------|--------------------|-------|--------|
| arc2-01 | (TBD) | 🟡 pre-Mare history | `chapter-arc2-01-v3.png` | — | pre-2026-06 |
| arc2-02 | (TBD) | 🟡 pre-Mare history | `chapter-arc2-02.png` | — | pre-2026-06 |
| arc2-03 | (TBD) | 🟡 pre-Mare history | `chapter-arc2-03.png` | — | pre-2026-06 |
| arc2-04 | (TBD) | 🟡 pre-Mare history | `chapter-arc2-04-v4.png` | — | pre-2026-06 |
| arc2-05 | (TBD) | 🟡 pre-Mare history | `chapter-arc2-05-v5.png` | — | pre-2026-06 |
| arc2-06 | (TBD) | 🟡 pre-Mare history | `chapter-arc2-06.png` | — | pre-2026-06 |

## Arc 3 — The Slow Burn

| Chapter | Title | Status | Canonical filename | Bytes | Locked |
|---------|-------|--------|--------------------|-------|--------|
| arc3-01 | (TBD) | 🟡 pre-Mare history | `chapter-arc3-01-v2.png` | — | 2026-06-16 |
| arc3-02 | (TBD) | 🟡 pre-Mare history | `chapter-arc3-02.png` | — | 2026-06-16 |
| arc3-03 | (TBD) | 🟡 pre-Mare history | `chapter-arc3-03-v3.png` | — | 2026-06-16 |
| arc3-04 | (TBD) | 🟡 pre-Mare history | `chapter-arc3-04.png` | — | 2026-06-16 |
| arc3-05 | (TBD) | 🟡 pre-Mare history | `chapter-arc3-05.png` | — | 2026-06-16 |

## Arc 4 — The White Dawn Threshold

| Chapter | Title | Status | Canonical filename | Bytes | Locked |
|---------|-------|--------|--------------------|-------|--------|
| arc4-01 | Bureaucracy | ✅ LOCKED v2 | `chapter-arc4-01-v2.png` | — | 2026-06 |
| arc4-02 | The Caravans | ✅ LOCKED v1 | `chapter-arc4-02.png` | — | 2026-06 |
| arc4-03 | The Pyrinae Accord | ✅ LOCKED v1 | `chapter-arc4-03.png` | — | 2026-06 |
| arc4-04 | The Humman Delegation | ✅ LOCKED v2 | `chapter-arc4-04-v2.png` | — | 2026-06 |
| arc4-05 | The Gifts | ✅ LOCKED v8 | `chapter-arc4-05-v8.png` | 1,771,592 | 2026-06-20 |
| arc4-06 | Aftermath | ✅ LOCKED v4 | `chapter-arc4-06-v4.png` | 6,342,558 | **2026-06-23** |

## Arc 5 — The Great War

| Chapter | Title | Status | Canonical filename | Bytes | Locked |
|---------|-------|--------|--------------------|-------|--------|
| arc5-01 | War Drums | ✅ LOCKED v3 — approved by Ainz 2026-08-24 (doctrine demo; doctrine green-lit for the 13-cover reforge queue) | `chapter-arc5-01-v3.png` | 6,771,866 | **2026-08-24** |
| arc5-02 | The First Battle | 🟡 In progress | — | — | — |
| arc5-03 | (TBD) | ⏳ Not yet forged | — | — | — |
| arc5-04 | (TBD) | ⏳ Not yet forged | — | — | — |
| arc5-05 | The Second Shot | ✅ LOCKED v2 | `chapter-arc5-05-v2.png` | 1,702,387 | **2026-06-29** |
| arc5-11 | The War Becomes Worse | ✅ LOCKED v101 | `chapter-arc5-11-v101.png` | — | **2026-06-28** (Temple Embrace — Stripe Paw + Humman merchant in predator+prey embrace, dim sepia temple) |
| arc5-19 | Ajani Throws The Spear | ✅ LOCKED v4 | `chapter-arc5-19-v4.png` | — | **2026-06-28** (Panoramic: wall of feline defenders left, Ajani mid-throw center, creature on right, sepia engraving) |
| arc5-22 | The White Dawn Wakes | ✅ LOCKED v1 | `chapter-arc5-22-v1.png` | 1,930,774 | **2026-06-29** |

### Emblematic medallion slots (Arc 5 timeline UI)
| Slot | Ch | Mirror | Canonical version |
|------|----|----|----|
| 05:25 | arc5-ch01 | `arc5-med-arc5-ch01-v3.png` | v3 LOCKED (mirror of locked cover; probe priority picks v3) |
| 08:15 | arc5-ch05 | `arc5-med-arc5-ch05-v2.png` | v2 LOCKED |
| 09:45 | arc5-ch11 | `arc5-med-arc5-ch11-v101.png` | v101 LOCKED |
| 12:02 | arc5-ch19 | `arc5-med-arc5-ch19-v4.png` | v4 LOCKED |
| 12:06 | arc5-ch22 | `arc5-med-arc5-ch22-v1.png` | v1 LOCKED |

## Arc 6 — Aftermath & The Road

| Chapter | Title | Status | Canonical filename | Bytes | Locked |
|---------|-------|--------|--------------------|-------|--------|
| arc6-01 | The Cost | ✅ LOCKED v5 — approved by Ainz 2026-08-24 | `chapter-arc6-01-v5.png` | 4,704,553 | v1 2026-08-23 (drift: kitten + human Yvaria); v2 2026-08-24 (drift: metal hospital bed + wall panel + nude sphynx Yvaria); v3 2026-08-24 (Ainz: Ajani good, Yvaria reads male/maned — wrong species); v4 2026-08-24 Yvaria redrawn as canon Mottled Paw female jaguar (Ainz: much better, but scorpions too small); v5 2026-08-24 scorpions enlarged to arm-length "living pauldrons" per canon (Black Fire 2 m / Red Fire 1.8 m), Ajani + Yvaria held from v4; self-audit PASS, minor note: 2nd window elder rendered spotted instead of lioness (background, no canon conflict) (sidecars v1–v5) |
| arc6-02 | Rebuilding | ⏳ Not yet forged (brief anchored: throne, flaring diadem, Elyra below the dais) | — | — | — |
| arc6-03 | The Vision | ⏳ Not yet forged (brief anchored: bronze doors closing behind Ajani + scorpions) | — | — | — |
| arc6-04 | The Road Begins | ⏳ Not yet forged (brief anchored: Cefiro presents seal to Tsar Nikolai, Ice City; palette question open) | — | — | — |
| arc6-05 | Epilogue | ⏳ Not yet forged (brief anchored: delegations beyond the rebuilt gate, twin suns standing arrangement) | — | — | — |

Arc 6 pre-forge scrub (2026-08-23, commit 0cd5006): umbrella `chapter-06.md` + slices meta-scrubbed — Ch 4 planning-bleed stripped; Ch 1 quadruple-stacked opening drafts deduplicated (~12 KB) to the canonical flow; Seris "executed by Mekhmed" draft error corrected to canon (Lena missing). Umbrella snapshot preserved at `chapter-06.md.bak.before_pass1`.

---

## Lock-in cadence (universal)

```
1. PNG exists on disk at canonical filename with verified bytes/sha.
2. Ainz-sama approves ("Much better !!!!" / "Lock in vN").
3. This file's row added/updated.
4. MEMORY.md "Arc ledger" block updated.
5. (Optional) regenerate webp/jpg variants per universal checklist.
6. (Optional) regenerate thumbnails per universal checklist.
7. NEVER delete v1..v(N-1) PNGs.
```

## Promotion trigger

Promote a new version to canonical **only** when:
- (a) The PNG is on disk and byte-identical across canonical + media-mirror.
- (b) Ainz-sama approves with explicit lock-in instruction.
- (c) This file is updated in the SAME work block as the lock-in.
| crimson-hawk-v1.png | v1 | [2026-08-22] | [sepia-ink bestiary plate matching razor-hare-v2/styx register] | crimson-hawk-v1.png | 1761572 | [53f44afb] | ✅ LOCKED v1 — approved by Aina 2026-08-22 | New Steadfast Desert entry: war-bird, feather-detonation volleys (arc5-01). |
| killer-claw-v1.png | v1 | [2026-08-22] | [sepia-ink bestiary plate matching razor-hare-v2/styx register] | killer-claw-v1.png | 1625829 | [f54350e1] | ✅ LOCKED v1 — approved by Aina 2026-08-22 | New Steadfast Desert entry: suicide raptor rigged with rune-bomb (arc5-01). |
| cargo-bird-v1.png | v1 | [2026-08-22] | [sepia-ink bestiary plate matching razor-hare-v2/styx register] | cargo-bird-v1.png | 1886649 | [b884211e] | ✅ LOCKED v1 — approved by Aina 2026-08-22 | New Rune Belt entry: green-plumed transport bird; gate scene with new Sultan (arc6-02). |


---

## Site Behavior — Chronicles Shelf (Round 15)

| Behavior | Status | File | Locked |
|----------|--------|------|--------|
| Tome falls LEFT to first place; all neighbours lean left; switch = replacement animation (FLIP), never full re-drop | ✅ LIVE-VERIFIED 2026-08-23 (fresh fall 3, switches 3→1→5, shelve; zero console errors; ribbon Δx 9.3px) | `ethra_site/templates/index.html` (CSS ~599-614, 777-783; JS `fallenTab`/`flipTabs`/`canonicalSort`/`selectArc`/`shelveAll`) | 2026-08-23 |

Notes: `.lean-r` rule removed; fall zone reserved via `#section-story.reading #arcNav { padding-left: calc(var(--fallw) + 24px) }` (188px desktop / 142px mobile); ribbon grid column 184px/146px under the lying tome. Bug fixed during verification: `fallTome()` strips `lean-l` from the target tab. Mobile behavior code-verified only (browser SDK has no viewport emulation). Supersedes round-9 fall-right geometry in MEMORY.md.

| Ribbon hangs FROM the lying tome (true page marker); banner suns orbit the title | ✅ LIVE-VERIFIED 2026-08-23 (tuck within book span, center Δ ≤9.2px, mark-1 clear of board 14.5px; header Y unclipped, suns animating behind title) | `ethra_site/templates/index.html` (`attachRibbon()`, `.chapter-subnav` reading padding-top 74px, `.header-orbit`/`hdr-orbit` keyframes, `.title-wrap`) | 2026-08-23 |

Round-16 notes: `attachRibbon()` sets inline `margin-top` so the silk's top tucks behind the lying tome (`arcNav.bottom - bw + 12`); shelf `z-index:3` paints board+tome above the silk; cleared on shelve. Header: static `.twin-suns` removed; suns orbit on an 18s elliptical waypoint path (`--orbitR` 210px / 130px mobile), behind the title (z1 vs z2).

| R17: ribbon hangs from tome HEAD edge; domino physics (row slides together, first tome rests on fallen); living planet (supercontinent, oceans, ice, desert, islands, animated drifting clouds) | LIVE-VERIFIED 2026-08-23 (ribbon.left-fallen.left +0.89px arc1 / +2.01px arc3; chain gaps -27..-34px, first-vs-fallen -11.97px; shelve clears margins; wb-surf/wb-clouds animations running; zero console errors) | `ethra_site/templates/index.html` (`attachRibbon()` marginLeft, `.chapter-subnav` justify-self/align-self start, `#section-story.reading #arcNav` nth-child domino transforms, `.wb-svg` planet markup + `wb-drift` keyframes) | 2026-08-23 |

Round-17 notes: ribbon horizontal attach computes `bookLeft = arcNav.left + paddingLeft - tab.offsetHeight` and sets inline margin-left (1:1 after justify-self:start; center alignment had absorbed half the delta). Domino chain: uniform -12deg lean with cumulative translateX -9px per book closes the 10px gaps; first standing book translateX(-38px) rotate(-16deg) rests on the lying tome. Planet: inline SVG in #orrery-world — ocean radial, supercontinent path (landclip-clipped ice cap + southern desert + forest patches), west bay, east islands, shallow-water stroke, blurred cloud bands; surface drifts 90s, clouds 36s (wb-drift -150px wrap with <use x="150"> copies). Declared by Ainz-sama the TRUE FINAL cosmetic edits.

| R18: silk drapes OVER the book's edge (painted in front of the board, fold crease at the crossing); mobile ribbon-to-text gap tightened so the folio is readable on a phone | LIVE-VERIFIED 2026-08-23 (Playwright 480x900: ribbon top -6px above board top, ribbon-to-card gap 6px, card 378px wide; 1280x900: drape -6px; screenshot ribbon_mobile.png shows the fold-over drape and readable folio) | `ethra_site/templates/index.html` (`.chapter-subnav` z-index 4; ::before drape-fold gradient + top chamfer; `attachRibbon()` targetY = navBottom - 6; reading padding-top 44px; reading grid 96px desktop / 56px+10px gap mobile; mobile `.chapter-content .content-card` padding 26px 16px) | 2026-08-23 |

Round-18 notes: the ribbon read as "pasted" because the shelf's z-index 3 painted board+tome ABOVE the silk's tuck, hiding it; now the silk (z4) paints in front of the board's face with its top 6px above the board top, overlapping the lying tome's bottom edge, and the ::before gradient paints light-catch / crease / front-shade / board-lip lines at 0-18px. Mobile dead space came from a 146px ribbon column reserving room for a 40px silk; now 56px + 10px gap. Verification tooling: venv Playwright with real viewport emulation (probe_ribbon.py at workspace root) — the browser SDK still cannot emulate phone widths.

| R19: silk waits as a bare red thread at the tome's edge while the tome is in the air; unfurls only once the tome lies flat (switch path no longer shows the ribbon early) | LIVE-VERIFIED 2026-08-23 (Playwright 480x900, switch 1->3: mid-fall ribbon h=9px sliver at the book edge, settled h=217px top -6px above board; zero console errors; ribbon_midfall.png shows the thread over the moving tome) | `ethra_site/templates/index.html` (`.chapter-subnav.waiting { scale: 1 0.04; animation: none }`; switch path adds waiting + attachRibbon at select, releases at 1080ms with attachRibbon + unfurlRibbon; fresh path clears waiting at the 620ms gate; shelveAll clears waiting) | 2026-08-23 |

Round-19 notes: after R18 put the silk in front of the shelf (z4), the switch path's immediately-visible full ribbon read as "ribbon before the book falls". Now on switch the new panel's ribbon is collapsed to a 4% sliver (a red thread at the tome's edge) until 350ms delay + 700ms fall complete, then re-tucks and unfurls; fresh fall unchanged (panel opacity gate at 620ms, book flat ~700ms).

| R20: ribbon release is LANDING-DRIVEN — transitionend on the fallen tome's transform + sustained-flat rAF fallback (3 consecutive frames) + 1400ms hard timer, token-cancelled by any new selectArc/shelveAll; "flat" is width-relative (box height <= offsetWidth+2), fixing desktop's 1.4s-late release (arc 3 rests at 61px, above the old fixed 60px bar) and mobile's early mid-swing release (overshoot bounce stays under a fixed bar); fresh fall now actually animates (forced reflow between prepend and fallTome); stale unfurl classes cleared on select/shelve | LIVE-VERIFIED 2026-08-23 (probe_sync.py at 480x900 + 1280x900: unfurl 33-52ms after true settle on fresh AND switch paths; sliver 8.6-9.3px while tome airborne; rapid shelve-then-reopen leaves exactly one fallen/one unfurled/no stuck waiting; shelve clean; 0 JS console errors; ribbon_sync_midswitch.png + ribbon_sync_settled.png) | `ethra_site/templates/index.html` (`whenTomeLanded` / `releaseRibbonOnLanding` / `cancelRibbonRelease`; fresh path `void arcNav.offsetHeight`; unfurl cleanup in selectArc+shelveAll) | 2026-08-23 |

Round-20 notes: background subagent (task-0f94520d0e5c) implemented the landing-driven release; Mare hardened and verified. The probe exposed two latent geometry bugs the magic-timeout code hid: (1) the fixed `<60px` flat test NEVER fired on desktop — arc 3 lies at 61px — so the hard timer released the silk 1.4s late; (2) on mobile the overshoot bounce stays under 60px, so a single thin reading could release ~350ms early mid-swing. Width-relative predicate + 3-frame sustained streak fix both. Note: Arc 5 deliberately hides its ribbon (wall-scroll timeline UI, static/arc5_timeline.css) — probes exclude it. Side finding (audit): 56 requests 404 on `arc5-med-*.png` mid-chapter art versions referenced by arc-5 chapter markdowns but absent from static/images.

| R21: GIT REMOTE LIVE — repository pushed to GitHub (https://github.com/magicrulerr-art/ethra.git), branch main = d608a9f (baseline ebbd6a8 + P0/P1-server); the site now has an off-machine backup and rollback point for every future phase | VERIFIED 2026-08-23 (`git ls-remote origin` → refs/heads/main = d608a9f; push ~363 MB completed; working tree clean) | GitHub remote origin (token-auth; token to be rotated per advisory) + all repo files | 2026-08-23 |

Round-21 notes: push unblocked when Ainz-sama delivered the exact PAT in-chat (screenshot OCR had failed earlier). Verified against the GitHub API first, stored via `git credential approve` (BOM-free ASCII input — write_file's UTF-8 BOM corrupts the protocol line; python -c with newline='\n' avoids it), plaintext temp files deleted immediately. STANDING ADVISORY: rotate this PAT (it was pasted in chat and appeared in a desktop screenshot). Rollback for any future break: `git reset --hard d608a9f`.

| R22: P1 DROP-IN LIVE + PUBLIC PAGES MIRROR — (1) cities are now one-file drop-ins: `content/places/<slug>.md` (frontmatter name/kind/biome/x_pct/y_pct/race/faction/region/image/blurb + gazetteer body) drives `/api/places`, `/api/place/<slug>`, pins merged into `/api/map/coordinates`, gold diamonds + gazetteer overlay on the main site, and the canon viewer's dossier layer; six canonical cities migrated. (2) Creature map coordinates moved INTO each creature file's frontmatter (36 files); the JSON creatures array demoted to override-only. (3) GitHub Pages public mirror LIVE at https://magicrulerr-art.github.io/ethra/ — `tools/export_static.py` bakes 119 documents (landing, viewer, every read-only API response, static tree) rooted at `/ethra/`; `.github/workflows/pages.yml` re-bakes + deploys on every push to main | VERIFIED 2026-08-23 (smoke 36/36; probe_p1.py 13/13 against live server; probe_pages.py 11/11 against the PUBLIC Pages URL incl. bestiary diamonds, gazetteer image, viewer dossier; Actions run 32664831864 = success) | commits ef82fbb (P1 content), f4a1387/6351c41/a2044b5 (P1.5 pipeline); adding a city = drop one .md file into content/places/ | 2026-08-23 |

Round-22 notes: configure-pages needs `enablement: true`, and the Pages site itself had to exist first — GITHUB_TOKEN lacks admin to create it, so it was created once via the stored PAT (`build_type: workflow`). Mirror is READ-ONLY by design: `/api/map/upload` is never exported; writing stays on the local Flask (8790). The local live server was RESTARTED on current code later on 2026-08-23 after Ainz-sama authorized PID-specific kills (stale 8790 server + test zombies 8791/8792/8793 all `taskkill /pid`-ed after CommandLine verification; QwenPaw daemon on 8088 untouched); post-restart: smoke 36/36, probe_p1 13/13, probe_r23 6/6 on live AND public. Two small runtime logs (`pages_test.log`, `pages_test_8793.log`) slipped into f4a1387 and are now gitignored but still tracked — untrack with `git rm --cached pages_test.log pages_test_8793.log && git commit` when convenient (policy blocks rm in Mare's session). STANDING ADVISORY: rotate the exposed PAT. Rollback: `git reset --hard d608a9f`.

| R23: PAGES 404 FIX + RIBBON RE-ANCHOR — (1) `descendToMap` (landing orrery: first zoom → click world) used a bare `'/map/'` literal that 404s at the Pages domain root; now reads the Map href from `#site-nav`, prefix-correct in every environment. (2) Ribbon redesign under Ainz-sama's discretion ("change it if it continues not to work"): the silk no longer drapes over the shelf edge via runtime getBoundingClientRect margin math (the desync/drift source on slow devices); it is now a bookmark SEWN AT THE FOLIO'S TOP EDGE — constant -14px CSS tuck, identical on all viewports, nothing to measure. Visual language kept (red silk, chapter numerals, sway, waiting sliver, unfurl gated by whenTomeLanded 33–52ms after settle) | VERIFIED 2026-08-23 (probe_r23.py 6/6 on local mirror AND public Pages; probe_pages.py 11/11 public; Actions run 32666484106 = success) | commit e2c301b; revert = one commit if the old drape is preferred | 2026-08-23 |
