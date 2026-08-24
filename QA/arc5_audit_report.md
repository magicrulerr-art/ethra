# Ethra QA Report — Arc V "The Great War" Proactive Audit

- **Prepared by:** Demiurge's audit subagent (script-first method; defect battery established in the Arc I–II audit)
- **Date:** 2026-08-24
- **Scope:** `ethra_site/content/story/chapters/chapter-arc5-01..22.md` (22 published split files, READ-ONLY) + umbrella master `content/story/chapter-05.md` (293,483 bytes on disk, CRLF; 2,275 lines; READ-ONLY; source of truth for future fixes)
- **Splitting architecture:** `regenerate_chapters.py` splits the umbrella at LINE anchors from `arcs.json → arcs.5.split_anchors` (21 anchors: 410, 550, 728, 772, 792, 998, 1090, 1111, 1146, 1278, 1592, 1636, 1668, 1703, 1762, 1872, 1909, 2023, 2132, 2156, 2193). Chapter headings (`## Chapter N: <timestamp> — <title>`) are GENERATED from `arcs.json → sub_titles`; the umbrella itself contains only `# Chapter 5: The Great War` (L1).
- **Tooling:** `ethra_site/QA/arc5_tooling/` — adapted copies of the Arc I–II battery (FILES = 22 arc5 files) plus new scripts: `a5_boundary.py` (regeneration + boundary check), `a5_umbrella.py` (umbrella debris scan), spot-readers. Outputs prefixed `a5_*`. Original QA scripts untouched. All story files READ-ONLY throughout.
- **Status:** FINAL (§7)

---

## 1. Executive Summary

Arc V is typographically clean and mechanically the best-formed arc audited to date — **zero** missing-apostrophe contractions, zero lowercase standalone *i*, zero unbalanced quotes, zero crossed delimiters, zero lowercase proper nouns in polished prose, zero Arc I–II typo-list hits, and fully canon-compliant em-dash usage (446 dashes reviewed). However, it carries a **severe draft-hygiene problem**: 17 debris/duplicate blocks spread across 11 of the 22 chapters (ch01, 03, 06, 07, 11, 13, 15, 16, 18, 19, 22), the same root cause as Arc II (pre-correction take + corrected take published together, plus raw author stage-directions left in the file).

### Defect counts by class

| Class | Description | Count |
|---|---|---|
| A — Author meta-text / draft-instruction blocks | Present-tense stage directions, craft commentary, AI-instruction lines published in-story | **9 blocks** |
| B — Duplicate draft blocks | Same scene present twice (two takes) or re-hashed a third time | **8 groups** |
| C — Canon deviations in polished prose | king/King (1), Humman single-m (1), thought-delimiter `*`/`_` (7), inscription/memory delimiter (2) | **11 items** (of which 2 are conditional on judgment J2) |
| D — Editorial formatting | Narrative prose wrapped in `<p class="speech-line">` | **3 items** |
| E — Em-dash defects | — | **0** |
| F — Quote/contraction/proper-noun/typo defects | — | **0** |
| **Total actionable** | | **31 items** |

### Arc health verdict

**NOT reader-ready as published; fully recoverable with one remediation pass.** All 17 Class A/B blocks are deletions (no prose rewriting required — every deleted beat is either duplicated elsewhere or covered by a polished version later in the arc). Classes C/D are small mechanical/editorial fixes. The 22 published splits are **byte-identical** to a fresh regeneration from the umbrella (Part 1 of §6b), so all fixes must land in `chapter-05.md` followed by `regenerate_chapters.py`.

### Top findings

1. **Raw author stage-directions published inside `<div class="dialogue-block">`** at arc5-15 L4, arc5-16 L110, arc5-18 L4 & L90, arc5-19 L4, arc5-22 L4 — e.g. *"Ajani tores a fifth page… he chants visibily strained"*, *"The light walk begins to crack, then it breaks Nefere yells 'FIRE'… cleaves trough the sand"*. Each is immediately followed by its polished version.
2. **Explicit AI-collaboration instruction published in-story:** arc5-11 L157 `*Then you should write the scene please (the Cefiro scene )*`.
3. **Author craft-essay published as story text:** arc5-07 L59–73 ("Velarius Vane has been seeded since the earliest chapters of the Ethra exercise… we have established… the reader should feel…").
4. **Whole scenes doubled** in ch01 (war room; Council of the Untrustworthy), ch03 (the dome), ch06 (fire-pillar aftermath + Mekhmed's tent), ch11 (civilian army), ch15 (cannon volley), ch16 (battle re-hash), ch19 (the five-minute sequence).
5. **New non-canon thought delimiters:** `*…*` (arc5-02 L11/L49, arc5-22 L47, arc5-21 L10 inside a `thought-block` div) and `_…_` (arc5-11 L25/L171) — canon is single quotes only. Note: `chapter-arc4-06.md` already uses `thought-block` + `*…*` five times, so the convention question is escalated as judgment J2.
6. **Bonus boundary check (§6b): PASS.** No chapter boundary cuts a sentence mid-clause; all 22 files end on sentence-final punctuation; regeneration round-trip is byte-identical.

### Open judgment items (need Ainz-sama)

- **J1** — arc5-01 Council scene: pick a take or ratify the recommended merge (take-B spine + take-A's member introductions).
- **J2** — Thought presentation: enforce single-quote canon everywhere, or ratify `thought-block` + `*…*` as a sanctioned style (Arc IV precedent).
- **J3** — "the young Bright Mane soldier" (arc5-02 L29, arc5-05 L19): Brightmane / Bright Paw / lowercase descriptor.
- **J4** — arc5-11 civilian-army speech: take A (M'rak's long speech) vs take B (delegation to Tamsin). Recommendation: B.

---

## 2. Per-Chapter Defect Catalog

Line numbers refer to the **published split files** (`content/story/chapters/chapter-arc5-NN.md`). Umbrella line numbers for the same content are given in §4. Chapters not listed (04, 05, 08, 10, 14, 17, 20) are clean except where noted.

### chapter-arc5-01.md (05:25 — Vasha Storms In)
| Line(s) | Class | Finding |
|---|---|---|
| L74–142 | B1 | **Duplicate war-room scene, take A** (later-timeline scout report: "The first vanguard is destroyed… The second vanguard is advancing—two hundred and fifty riders"). Contradicts the chapter's 5:25 frame. Canon = take B (L144–232). |
| L144–232 | B1 | Duplicate war-room scene, **take B (CANON)** — contains Vasha's entrance matching the chapter title ("At 5:25 in the morning, Vasha stormed into the war room unannounced." L146). |
| L236–291 | B2 | **Duplicate Council scene, take A** — richer member introductions (Maren, Sylen, Toren, Kellan). |
| L292–375 | B2 | **Duplicate Council scene, take B** — Kellan-focused, flows into the Mekhmed tent scene (L376). See J1. |
| L359 | C | `"that the Humman King thinks he is attacking a wounded city…"` — capitalized *King* with determiner → should be `the Humman king` (canon rule 1). |

### chapter-arc5-02.md (06:55 — Sera Holds The Gate)
| Line(s) | Class | Finding |
|---|---|---|
| L11 | C | `*We can't win against four hundred. We barely survived fifty.*` — asterisk thought (Sera). Canon: single quotes. |
| L29 | C/J3 | `Irek was among them—the young Bright Mane soldier…` — "Bright Mane" (two words); corpus canon is "Brightmane" (291 occurrences elsewhere; zero outside the arc5 umbrella). |
| L49 | C | `*We cannot hold.*` — asterisk thought (Sera). |
| L68 | — | False positive checked: "Our king lies **ill**" — adjective, not a contraction. No defect. |

### chapter-arc5-03.md (06:25 — The War Room Still Watches)
| Line(s) | Class | Finding |
|---|---|---|
| L51–86 | B3 | **Duplicate dome scene, take A** (mirror "carried since the capital was founded… three thousand years ago"). Canon = take B. |
| L87–122 | B3 | **Take B (CANON)** — High-Speaker lineage lore ("passed from High Speaker to High Speaker since the time of the Third Tyrant"). |
| L92 | C | Inside canon take B: `*You will never use this unless the capital itself is in danger…*` — asterisk-quoted inscription inside a speech-line → convert to double quotes. |
| L171 | C | `*Stay here. Stay hidden. Don't make a sound…*` — asterisk-remembered speech (Kira's mother) → convert to double quotes. |

### chapter-arc5-05.md (08:15 — The Second Shot)
| Line(s) | Class | Finding |
|---|---|---|
| L19 | C/J3 | `The young Bright Mane soldier who had watched the first wave die…` — second occurrence of "Bright Mane". |

### chapter-arc5-06.md (08:20 — The Light Shield Falls)
| Line(s) | Class | Finding |
|---|---|---|
| L7 | — | `The gate was still—` checked: intentional narrative interruption (cut off by "A flash. A thunder."). Valid, no defect. |
| L135–159 | B4 | **Duplicate aftermath + tent scene, take A** — includes a premature messenger scene ("The Woh riders had arrived. The ghosts were coming." L159) contradicting the 08:20 timeline (reinforcements arrive 10:35–11:50). |
| L161–177 | B4 | **Take B (CANON)** — timeline-consistent; flows into Tamsin's ride (L178+). |
| L190 | C | `"I'M TAMSIN, GENERAL OF THE HUMANS!"` — single-m in all-caps → `HUMMANS`. |

### chapter-arc5-07.md (08:40 — The Plague Comes)
| Line(s) | Class | Finding |
|---|---|---|
| L59–61 | A | **Craft meta-text inside dialogue markup:** `<div class="dialogue-block"><p class="speech-line">Velarius Vane has been seeded since the earliest chapters of the Ethra exercise… the reader should feel a cold shock of recognition…</p></div>` |
| L63–73 | A | **Craft-essay paragraphs:** "The suicide scorpions are also consistent with the Humman character **we have established**…" / "**This scene also serves a structural purpose**…" / "The deaths of the Wengari feel weighty because **we have spent time with them**…" — all author voice, delete. |

### chapter-arc5-08.md (08:45 — Scorpions Still Marching)
Clean. (Ends mid-scene on a dialogue block that continues in ch09 — intentional cliffhanger, verified well-formed.)

### chapter-arc5-09.md (09:00 — The Truce Lasts An Hour)
| Line(s) | Class | Finding |
|---|---|---|
| L3–5 | D | Scene-closing narrative paragraph wrapped in `<div class="dialogue-block"><p class="speech-line">` ("He did not need to say who 'he' was…"). Editorial reformat. |

### chapter-arc5-11.md (09:45 — The War Becomes Worse)
| Line(s) | Class | Finding |
|---|---|---|
| L25 | C | `_This is hell. I've stepped into hell._` — underscore thought delimiter (M'rak), unique to Arc V. → single quotes. |
| L157 | A | `*Then you should write the scene please (the Cefiro scene )*` — **author instruction to the writing system, published in-story.** Delete. |
| L171 | C | `_Can we win with that?_` — underscore thought. → single quotes. |
| L181–199 | B5 | **Duplicate civilian-army scene, take A** — M'rak's long speech ("You answer to me. You answer to her… The enemy is across the sand."). |
| L201–223 | B5 | **Take B (CANON, pending J4)** — delegates the civilians to Tamsin ("Here is your army. Man the wall. If the wall falls, we all fall. Go."), consistent with her redemption arc. |
| L218 | D | Inside canon take B: narrative + speech mixed in one speech-line (`M'rak nodded. He gestured… "Here is your army…"`). Editorial reformat. |
| L225 | D/J | "Cefiro's voice had its own music — 'cousin' instead of 'brother'…" — craft-flavoured narration; reads as narrator voice but borders on author commentary. Keep by default; flag for awareness. |

### chapter-arc5-12.md (10:35 — The Wall Blanketed)
| Line(s) | Class | Finding |
|---|---|---|
| L43–45 | D | Shadow-Paw arrival: narrative + dialogue in one speech-line (`The shadow riders reached the gate… "We are the Shadow Paws… We are here."`). Polished prose, wrong wrapper. Editorial reformat. |

### chapter-arc5-13.md (11:20 — The Shadow Figure Drinks)
| Line(s) | Class | Finding |
|---|---|---|
| L31–33 | A | **Draft scene-summary inside dialogue markup:** "At the wall, the black thing took shape before them… M'rak asked everyone present… Zephyr said, 'Open the gates for the humans, don't give it more food'…" — also contains single-m "humans". The open-the-gates beat is properly told in canon form at arc5-14 L24–31 (Tamsin: "OPEN THE GATES! THOSE ARE MY PEOPLE!"), so deletion loses nothing. |

### chapter-arc5-14.md (11:35 — The Wall Learns Horror)
Clean. (Contains the canon gate-opening scene.)

### chapter-arc5-15.md (11:40 — M'rak Yells Clear)
| Line(s) | Class | Finding |
|---|---|---|
| L3–5 | A | **Draft instruction block inside dialogue markup:** "The black thing approaches slowly as if it couldn't quite control it's body, M'rak yells 'ALL CANNONS FIRE!!!! FIRE THE RAY!!!! NOW!!!'…" (typos: *it's body*, run-on present tense). |
| L7–33 | B6 | **Duplicate cannon sequence, take A** — includes "FIRE THE RAY" and the ray firing at 11:40 ("the mirror array had fired its last shot and was dark", L31), contradicting ch16 (ray still needs 3 min, L30) and ch18 (Nefere fires at 11:59). |
| L35–61 | B6 | **Take B (CANON)** — cannons only, no premature ray. |

### chapter-arc5-16.md (11:50 — Vows Are Absolved)
| Line(s) | Class | Finding |
|---|---|---|
| L27–65 | B7 | **Canon sequence** — creature approach, ray countdown, Zephyr's charge, Solen's priest column and absolution (matches chapter title). |
| L67–105 | B7 | **Third copy of the cannon/reform sequence** (verbatim from ch15 take B: L67 approach, L70 "ALL CANNONS FIRE!", L73 volley, L79 reform, L84 "It reformed") + re-hash of L27–51 (ray countdown L88, wolf charge L95–97, Zephyr's frustration L102 verbatim ×2, "barely two leagues away" L105 vs L27). Internally contradictory (point-blank cannons followed by "two leagues away"). Delete. |
| L107 | B7 | Duplicate 11:50 boilerplate (second in chapter). |
| L109–111 | A | **Draft scene-summary with stage direction:** "…Solen emerged wreathed in golden armor… Tamsin asked, 'Who is he?'… **Back to M'rak.** He said…" — the polished version of this exact scene is arc5-17 L11–35. Chapter currently ENDS on this draft block. |

### chapter-arc5-17.md (11:55 — The Legend Answers)
Clean (contains the canon Solen-descent scene).

### chapter-arc5-18.md (11:59 — Nefere Fires)
| Line(s) | Class | Finding |
|---|---|---|
| L3–5 | A | **Draft instruction block:** "The light walk begins to crack, then it breaks Nefere yells 'FIRE' an impossibly hot beam of light cleaves trough the sand… postrated… it's 11:59" (typos: *trough*, *postrated*). Polished version follows at L7+. |
| L89–91 | A | **Draft instruction block:** "Ajani lands on the wall shouting 'STATUS STATUS…' we hear awed whispers 'his highness' Al around solen turns to ajani and quickly kneels… ajani roars 'LESS KNEELING AND MORE TALKING!!!'" — polished version follows at L93–105. |

### chapter-arc5-19.md (12:02 — Ajani Throws The Spear)
| Line(s) | Class | Finding |
|---|---|---|
| L3–5 | A | **Draft instruction block:** "Ajani says 'crap' and flies up in the sky… beseeschs… zephyr says 'you heard him, charge!!!'… it's now 12:02". |
| L7–41 | B8 | **Duplicate five-minute sequence, take A** — merged-spear → fire-spirit concept; ends "It was 12:02 in the morning—noon" (self-contradictory phrasing). |
| L43–79 | B8 | **Take B (CANON)** — five-spear pentagon, page ritual, IFRIT invocation, fire-copy; correct "It was 12:02 in the afternoon" (L79). Page-ritual structure is what ch20–22 continue ("the fifth page"). |

### chapter-arc5-21.md (12:05 — The Light Cage Fades)
| Line(s) | Class | Finding |
|---|---|---|
| L9–11 | C/J2 | `<div class="thought-block">*Just two more. And then... well, let's hope I can still speak.*</div>` — asterisk thought inside a CSS-supported `thought-block` (same pattern as `chapter-arc4-06.md` ×5). Subject to J2. |

### chapter-arc5-22.md (12:06 — The White Dawn Wakes)
| Line(s) | Class | Finding |
|---|---|---|
| L3–5 | A | **Draft instruction block:** "Ajani tores a fifth page, deep gold runes adorn it and he chants visibily strained… Kira clutches pearl tightly then ajani tores a sixth page…" (typos: *tores* ×2, *visibily*). Polished version follows (L7+ "Ajani reached for the fifth page…"). |
| L47 | C | `*This is it. I barely have ten seconds, I think. I hope it's enough.*` — bare asterisk thought → single quotes (or thought-block per J2). |

---

## 3. Canon-Rule Compliance

### 3.1 king/King rule
69 lines contain king/King. **68 compliant.** Lowercase usages are uniformly determiner/possessive/generic/apposition ("the king", "my king", "his king", "its king", "our young king") — all correct, including direct address ("my king"). Deviations:

| Location | Text | Fix |
|---|---|---|
| arc5-01 L359 | "the Humman **King** thinks he is attacking…" | → lowercase (determiner + modifier). Mechanical. |
| arc5-22 L83 | "the reign of **King Ajani Brightmane**" | Correct (title + name). No action. |

### 3.2 Humman/Hummans race name
Census (polished + draft text): **Humman ×118, Hummans ×20** (canon, double-m) vs **single-m ×2**:
| Location | Text | Fix |
|---|---|---|
| arc5-06 L190 | "GENERAL OF THE **HUMANS**!" (all-caps, Tamsin's shout) | → HUMMANS. Mechanical. |
| arc5-13 L32 | "Open the gates for the **humans**" | Inside A-class draft block — resolved by deletion. |

Compliance 138/140 = 98.6% (99.3% counting the deleted-block hit as resolved). Rest-of-corpus check: canon "Humman(s)" dominates everywhere (1,924+ occurrences outside arc5).

### 3.3 Dialogue formatting
- **Double quotes:** ASCII straight quotes throughout (curly count = 0), matching site style. Every file's quotes balance (cross-line walker: 22/22 OK, zero open-across-blank, zero EOF-imbalance).
- **Crossed delimiters (`*…'` / `'…*`):** **zero** in all 22 files.
- **Single-quote odd lines:** 20 flagged by the walker — all verified as plural-possessive apostrophes (scorpions', riders', wolves', months', Wohs', Cloaks'…). Zero genuine.
- **Contractions:** zero missing-apostrophe defects. Both flagged tokens verified false positives ("lies **ill**" — adjective; "This is **hell**" — noun).
- **Standalone lowercase i:** zero.
- **Thought delimiters (canon: single quotes ONLY):** deviations listed in §2 — asterisks: arc5-02 L11, L49; arc5-03 L92 (inscription), L171 (remembered speech); arc5-16 L92 (deleted with block); arc5-21 L10; arc5-22 L47. Underscores (novel in Arc V): arc5-11 L25, L171. Precedent note: `chapter-arc4-06.md` uses `thought-block` + `*…*` ×5 → J2.
- **Speech-in-speech-line integrity:** 3 narrative-prose-in-speech-line wraps (D-class, §2).

### 3.4 Em dashes
Census: **446 em dashes, 0 en dashes, 0 horizontal bars, 0 ASCII-hyphen/en-dash dialogue openers.** Odd-count lines classified:

| Category | Count | Verdict |
|---|---|---|
| CUT (speech cutoff) | 20 | Canon ✓ |
| TAIL (elaboration to sentence/line end) | 60 | Canon ✓ |
| TAIL (empty — line ends on dash) | 1 | arc5-06 L7 "The gate was still—" — intentional narrative interruption by the next paragraph ("A flash. A thunder."). Valid ✓ |
| OPEN-MID (suspect) | 105 | **All 105 manually reviewed** (`a5_openmid_review.txt`): every case is a single dash introducing an appositive/elaboration that runs to the end of its sentence; the regex trigger is merely the following next sentence. Per the Arc I–II reconciliation precedent, these are valid. **Zero genuine unclosed parentheticals.** |

**Em-dash verdict: fully compliant.** (Chapter-heading dashes — 22, from `sub_titles` — are scaffold and excluded from defect accounting.)

---

## 4. Umbrella Draft-Debris Inventory

Source of truth: `content/story/chapter-05.md` (2,275 lines). Mapping: split ch N line k (k≥3) ≈ umbrella L(anchor_N + k − 3). All items below were located by `a5_umbrella.py` + grep and verified by targeted reads. **Keep/delete column reflects the recommendation; all deletions are story-safe (canon evidence in §5).**

| Umbrella L | Split location | Type | Keep/Delete | Canon evidence |
|---|---|---|---|---|
| L1056–1070 (≈) | arc5-07 L59–73 | Craft commentary ("seeded since the earliest chapters of the Ethra exercise", "we have established", "the reader should feel", "This scene also serves a structural purpose") | **DELETE** | Pure author voice; no story content; scene it annotates continues at arc5-07 L75+ |
| L1433 | arc5-11 L157 | AI-instruction: `*Then you should write the scene please (the Cefiro scene )*` | **DELETE** | Not narrative; the Cefiro scene itself exists (arc5-11 L118+, L225+) |
| L1666–1668 (≈) | arc5-13 L31–33 | Draft scene-summary ("M'rak asked everyone present… Zephyr said, 'Open the gates for the humans…'") | **DELETE** | Gate-opening beat retold in canon form at arc5-14 L24–31 (Tamsin: "OPEN THE GATES! THOSE ARE MY PEOPLE!") |
| L1704 | arc5-15 L3–5 | Draft stage-direction ("…it couldn't quite control it's body, M'rak yells 'ALL CANNONS FIRE!!!! FIRE THE RAY!!!! NOW!!!'") | **DELETE** | Polished take at arc5-15 L35–61 (canon take B, §5) |
| L1827–1867 | arc5-16 L67–107 | Third copy of cannon/reform block + re-hashed ray/wolf sequence + duplicate 11:50 boilerplate | **DELETE** | Canon sequence = arc5-16 L27–65; verbatim duplicates of L1707–1755 umbrella block (×3 census) |
| L1869–1871 (≈) | arc5-16 L109–111 | Draft scene-summary with "Back to M'rak." stage direction | **DELETE** | Polished scene at arc5-17 L11–35 (twenty-first pillar, Solen's descent, "Golden what?", legend exposition) |
| L1910 | arc5-18 L3–5 | Draft stage-direction ("The light walk begins to crack… cleaves trough the sand… postrated") | **DELETE** | Polished version arc5-18 L7+ (wall falls, ray fires) |
| L1996 | arc5-18 L89–91 | Draft stage-direction ("Ajani lands on the wall shouting 'STATUS STATUS…' Al around solen turns to ajani…") | **DELETE** | Polished version arc5-18 L93–105 (identical beats, correct spelling) |
| L2024 | arc5-19 L3–5 | Draft stage-direction ("Ajani says 'crap'… beseeschs… zephyr says…") | **DELETE** | Polished take at arc5-19 L43–79 (canon take B, §5) |
| L2194 | arc5-22 L3–5 | Draft stage-direction ("Ajani tores a fifth page… chants visibily strained… tores a sixth page") | **DELETE** | Polished version arc5-22 L7+ ("Ajani reached for the fifth page…") |

Also in umbrella (context, no action needed for Arc V): duplicate scene blocks at L75–143/L145–233 (war room), L237–292/L293–376 (Council), L600–633/L635–670 (dome), L925–949/L951–967 (aftermath+tent), L1457–1475/L1477–1499 (civilian army), L1707–1733/L1735–1761 (cannon volley), L2027–2051/L2063–2087 (five-minute sequence); duplicate formulaic openers at L1733/L1761 and L1825/L1867. Heading inventory: only `# Chapter 5: The Great War` (L1); no bold scaffold lines; no "Version A/B", "Corrected", "Montage", "Let me rewrite" markers (Arc V's debris style is stage-directions and craft essays, not Arc I–II's correction markers).

## 5. Duplicate Blocks with Canon Designation

| # | Location (split lines) | Takes | CANON designation | Evidence |
|---|---|---|---|---|
| B1 | arc5-01 L74–142 vs L144–232 | A: later-timeline report (vanguard destroyed, third wave) · B: Vasha's 5:25 entrance | **Take B** | Chapter title "05:25 — Vasha Storms In"; take B contains the storming-in scene (L146) and Vasha's full assessment (L229); take A's scout numbers belong to a later moment and break the 5:25 frame |
| B2 | arc5-01 L236–291 vs L292–375 | A: full member introductions + longer Vasha speech · B: Kellan-centric, tighter | **JUDGMENT (J1)** — recommend B spine + optional restore of A's introductions | Both takes contain unique material; B flows into the tent scene (L376) and ends with Kellan's reaction; A's member intros (Maren, Sylen, Toren) are the only unique lore |
| B3 | arc5-03 L51–86 vs L87–122 | A: mirror from capital's founding / 3,000 yrs · B: High-Speaker lineage since Third Tyrant | **Take B** | Positioned directly before Mekhmed's reaction to the dome (L123 "had just swallowed the Wengari capital whole"); richer lore; final paragraph of both takes is identical (L85 = L121), so B's continuation is seamless. Note take-B L92 asterisk-inscription fix (§3.3). Lore conflict between takes (3,000 yrs vs Third Tyrant era) resolves in B's favor |
| B4 | arc5-06 L135–159 vs L161–177 | A: adds premature messenger ("The Woh riders had arrived") · B: tent scene only | **Take B** | Timeline: at 08:20 reinforcements are still hours out (they arrive 10:35–11:50, ch12–16); B flows directly into Tamsin's approach (L178–190) |
| B5 | arc5-11 L181–199 vs L201–223 | A: M'rak's long rallying speech · B: delegation to Tamsin | **Take B (pending J4)** | B integrates Tamsin's redemption arc (she trains the civilians, L221), reuses the established line "If the wall falls we all fall" (echoed at L202), and matches the shorter, exhausted-commander register of the moment |
| B6 | arc5-15 L7–33 vs L35–61 | A: includes ray fire at 11:40 · B: cannons only | **Take B** | Ray chronology: arc5-16 L30 "How long for the ray?! Three minutes!" (11:50) and arc5-18 "11:59 — Nefere Fires" prove the ray cannot have fired at 11:40 |
| B7 | arc5-16 L67–107 (+draft L109–111) vs L27–65 | single canon sequence + redundant re-hash | **L27–65** (the absolution sequence matching the chapter title "Vows Are Absolved") | Re-hash repeats ch15 text verbatim, contradicts itself (point-blank cannons then "two leagues away"), and the chapter ends cleanly on the L65 boilerplate after deletion |
| B8 | arc5-19 L7–41 vs L43–79 | A: merged spear → fire spirit · B: five-spear pentagon + page ritual | **Take B** | B's page-ritual structure is what ch20–22 continue ("third page" L2135 umb., "fifth page" arc5-22); B fixes A's self-contradictory "12:02 in the morning—noon" to "afternoon" (L79); B is the superset in staging detail |

## 6. Remediation Classification

**Guarantee (as in the Arc I–II report):** every recommended edit is (1) a character-level mechanical fix from a closed map, (2) a deletion of author meta-text/draft-instruction, or (3) a deletion of one of two near-identical takes keeping the canon-designated one. No new prose, no dialogue rewording beyond capitalization/delimiter fixes. All fixes target `content/story/chapter-05.md`, then `regenerate_chapters.py` re-splits (round-trip byte-identity proven in §6b).

### 6.1 Mechanical (scriptable, closed map) — 8 items
| # | File (split) | Umbrella (≈) | Fix |
|---|---|---|---|
| M1 | arc5-01 L359 | L358 | `the Humman King thinks` → `the Humman king thinks` |
| M2 | arc5-06 L190 | L980 | `GENERAL OF THE HUMANS` → `GENERAL OF THE HUMMANS` |
| M3 | arc5-02 L11 | L419 | `*We can't win against four hundred…*` → `'We can't win against four hundred…'` |
| M4 | arc5-02 L49 | L457 | `*We cannot hold.*` → `'We cannot hold.'` |
| M5 | arc5-11 L25 | L1301 | `_This is hell. I've stepped into hell._` → `'This is hell. I've stepped into hell.'` |
| M6 | arc5-11 L171 | L1447 | `_Can we win with that?_` → `'Can we win with that?'` |
| M7 | arc5-22 L47 | L2237 | `*This is it. I barely have ten seconds…*` → `'This is it…'` |
| M8 | arc5-03 L92, L171 | L640, L719 | asterisk inscription/memory → double quotes (`"You will never use this…"` / `"Stay here. Stay hidden…"`) |

(Conditional on J2 = "enforce canon": add arc5-21 L10 → `'Just two more…'` keeping or dropping the thought-block div per J2 wording. Conditional on J3: 2× `Bright Mane` replacements.)

### 6.2 Editorial (judgment deletion / reformat) — 13 items
| # | Item | Action |
|---|---|---|
| E1–E9 | 9 Class-A debris blocks (§4 table) | Delete listed umbrella line ranges; verify adjacent paragraphs still flow (all verified: polished versions exist or scene continues) |
| E10 | arc5-01 war-room take A (umbrella ≈L73–141) | Delete; keep take B (≈L143–231) |
| E11 | arc5-03 dome take A (umbrella ≈L599–633) | Delete; keep take B (≈L635–669) |
| E12 | arc5-06 take A (umbrella ≈L925–949); arc5-15 take A (umbrella L1707–1733); arc5-16 re-hash (umbrella L1827–1871); arc5-19 take A (umbrella L2027–2051) | Delete; keep canon designations §5 (B4/B6/B7/B8) |
| E13 | arc5-11 take A (umbrella ≈L1457–1475) | Delete pending J4 confirmation |

Formatting-only (optional, no story impact): restructure speech-line-wrapped narrative at arc5-09 L4, arc5-12 L44, arc5-11 L218 into prose + `span.speech`/dialogue-block pattern (D-class, 3 items).

### 6.3 Judgment items (need Ainz-sama's decision) — 4 items
| # | Question | Recommendation |
|---|---|---|
| J1 | arc5-01 Council of the Untrustworthy: take A vs take B? | Ratify merge: keep take B (umbrella ≈L293–376) as spine; optionally splice in take-A's council-member introduction paragraph (umbrella ≈L240–246 region) before Vasha speaks. If no merge is wanted, keep B alone. |
| J2 | Thought presentation: enforce single-quote canon strictly, or ratify Arc IV's `thought-block` + `*…*` pattern as a sanctioned style? | Enforce canon (single quotes) for bare asterisk/underscore thoughts regardless; for thought-block-wrapped thoughts (arc5-21 only in Arc V), either normalize or ratify — but decide corpus-wide, since arc4-06 has 5 instances. |
| J3 | "the young Bright Mane soldier" (arc5-02 L29, arc5-05 L19): intended name/term? | Corpus has Brightmane ×291 and no other "Bright Mane". If Irek is of the royal house → `Brightmane`; if it describes his family unit → `Bright Paw` (he fights among Bright Paw guards); if an epithet → lowercase `bright-maned`. Ask Ainz-sama; default `Brightmane`. |
| J4 | arc5-11 civilian-army scene: keep take A's M'rak speech or take B's Tamsin delegation? | Take B (canon evidence §5-B5). |

---

## 6b. Chapter-Boundary Check Results

**Part 1 — Regeneration round-trip (consistency with umbrella).** Rebuilt all 22 splits in-memory from `chapter-05.md` using the exact `regenerate_chapters.py` algorithm (line-anchor → char-offset conversion, heading injection from `arcs.json → sub_titles`, `## Chapter` dedup). Result: **22/22 MATCH — byte-identical.** Consequence: every fix must be applied to the umbrella, then regenerated; no split-only patching is possible or needed.

**Part 2 — Boundary integrity (sentence/clause cuts).** For each of the 21 boundaries, the last prose line of chapter N and the first prose line of chapter N+1 were inspected (`a5_boundary.txt`):

- **22/22 chapters end on sentence-final punctuation** (period, quote-close, or a deliberate dash-cutoff at ch06-internal L7 only). Zero mid-clause cuts.
- Div balance: every file's `<div class="dialogue-block">` opens equal closes (verified per file).
- Every chapter opens with a fresh sentence after its generated heading.
- Notable (all intentional, no action): ch08 ends inside a dialogue block whose scene resolves in ch09's opening line ("He did not need to say who 'he' was"); ch19→20 and ch21→22 cut between consecutive minutes of the same battle (12:02→12:03, 12:05→12:06) by design.
- **Timestamp convention check:** heading timestamps denote the chapter's key event, verified consistent (ch18 "11:59 — Nefere Fires": body runs 11:55→11:59 fire; ch21 "12:05 — The Light Cage Fades": body runs 12:04→12:05 fade). Non-monotonic headings ch02 (06:55) → ch03 (06:25) are an intentional POV rewind (parallel scenes in two war rooms), not a defect.

**Verdict: PASS — no boundary remediation needed.**

### Cross-audit observations (out of Arc V scope, recorded for the record)
- `chapter-arc4-06.md` contains a self-duplicated thought-block (L27–29 = L71–73) and five asterisk-thoughts — recommend folding into the next arc-level audit.
- `content/story/chapter-04.md` L2250 carries a possible author-meta line ("the adoption ritual you wrote") — flagged, not audited here.

## 7. Status

- [x] Report skeleton written (interruption resilience)
- [x] Tool battery adapted to 22-file list in `QA/arc5_tooling/` (originals untouched); all lints + census + classify + boundary + umbrella scans run
- [x] Spot-verification passes (draft blocks, duplicate takes, thought delimiters, king/King contexts, hum variants, OPEN-MID review of all 105 lines, umbrella line numbers via grep)
- [x] Sections 1–6b filled
- [x] **FINAL**

**Method note:** no story file was modified; all work products are this report plus `ethra_site/QA/arc5_tooling/` (scripts + outputs). Pending Ainz-sama's decisions on J1–J4, the remediation pass is fully specified (§6 tables) and mechanically executable against the umbrella.

