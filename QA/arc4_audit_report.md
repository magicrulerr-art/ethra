# Ethra QA Report — Arc IV "The Consolidation" — Proactive Audit

- **Prepared by:** Demiurge's audit subagent (Tri-Guardian QA), defect battery inherited from the Arc I–II reader-feedback audit (`QA/arc1_arc2_reader_feedback_report.md`).
- **Date:** 2026-08-24
- **Audit mode:** PROACTIVE — no reader feedback exists for Arc IV; the Arc I–II defect battery is applied wholesale.
- **Scope (READ-ONLY throughout):**
  - Published splits (primary audit targets): `content/story/chapters/chapter-arc4-01.md … chapter-arc4-06.md` (6 files; 564 / 597 / 545 / 612 / 678 / 676 lines; 3,672 lines total)
  - Umbrella master (source of truth for future fixes): `content/story/chapter-04.md` (481,075 bytes; 3,668 lines)
- **Editorial-history artifacts (listed for provenance; NOT audited — audit covers current `chapter-04.md` only):**
  - `chapter-04.md.alpha_excise` (492,264 B, 2026-06-20)
  - `chapter-04.md.repass3` (503,185 B, 2026-06-19)
  - `chapter-04.md.stripped_meta` (532,079 B, 2026-06-18)
  - `chapter-04.md.stripped_passes` (509,459 B, 2026-06-18)
  - `chapter-04.md_pass3_only.md` (57,447 B, 2026-06-19)
  - *Naming implies a multi-pass editorial pipeline (meta-stripping → pass re-runs → alpha excision) was already applied to the umbrella before publication. Its coverage was evidently scoped to previously-known marker classes: every debris class cataloged below survives in the current umbrella. Audit covers current `chapter-04.md` only.*
- **Tooling:** `QA/arc4_tooling/` — adapted copies of the Arc I–II battery (lint_arc4.py, lint_pass2_arc4.py, em_census_arc4.py, em_classify_arc4.py, quote_pair_check_arc4.py, delimiter_cross_check_arc4.py, final_tally_arc4.py) plus new arc4 scripts (umbrella_debris_scan.py, meta_scan_splits_arc4.py, umbrella_locate.py/.2, umbrella_headings.py, humman_diff.py, crossref_letter.py, thought_blocks.py, peek.py/peek2.py, em_tally.py) and their output artifacts. Originals in `QA/` untouched.
- **Architecture notes (verified in `arcs.json` + file inspection):**
  - Arc IV has no `split_anchors`; `regenerate_chapters.py` splits `chapter-04.md` by even-word heuristic. All fixes must land in the umbrella, then regenerate. Split line numbers below are audit references; each debris item also carries its umbrella line number(s), located by exact text search.
  - The generator strips markdown headings from umbrella content and inserts `## Chapter N: <sub-title>` (from `arcs.json`) as line 1 of each split (verified: arc4-01 L1 "## Chapter 1: Bureaucracy" … arc4-06 L1 "## Chapter 6: Aftermath"). These generated headings are pipeline output, not content defects. The extra "Humman" in splits (99) vs umbrella (98) is the arc4-04 generated heading "The Humman Delegation" — resolved, not a deviation.
  - The umbrella's stale internal heading `## Chapter 5: The Gifts` (umbrella L2572) is stripped by the generator and does not reach published output, but it is umbrella debris (stale numbering, see §4).
- **Status:** see §7.

---

## 1. Executive Summary

**Arc health verdict: NOT PUBLISHABLE AS-IS — worst structural condition of any arc audited to date.** The prose mechanics of Arc IV are comparable to pre-fix Arc I–II (moderate contraction/capitalization drift, one unbalanced quote, a handful of crossed delimiters). But the published arc carries **≈650 lines of draft debris — roughly 18% of the published text**: two complete worldbuilding/craft scaffold documents, thirteen author markers/self-prompts, and **nine duplicated scene complexes** (including one scene present in THREE takes). Arc I–II debris of this kind was isolated and reader-discovered; in Arc IV it ships wholesale in all six chapters.

**Counts per defect class**

| Class | Count | Notes |
|---|---|---|
| EDITORIAL — meta/scaffold deletions | ~225 lines | 2 scaffold documents (arc4-01 L418–552; arc4-02 L37–95), 5 planning/craft blocks, 13 markers/prompts |
| EDITORIAL — duplicated take deletions | ~425 lines | 9 scene complexes; canon designated in §5 |
| MECHANICAL — scriptable closed map | ~105 line-level fixes | contractions 32; lowercase *i* 14; race-name 9; proper-noun ~20 lines; quote repairs 6; asterisk thoughts 5; typos 11; caps-punctuation pattern |
| JUDGMENT — needs Ainz-sama's decision | 7 items | J1–J7 in §6.3 |

**Top findings**
1. Two full scaffold documents published: "Here is a comprehensive summary of Ethra and Ajani's tale…" + worldbuilding sections (arc4-01 L418–552) and "The Chapter's Cadence / Ajani's Voice / What This Reveals About the Speaker" (arc4-02 L37–95).
2. The Kira pickpocket scene exists in **three** takes (arc4-04 L316–363 / L366–418 / L422–470) wrapped around author prompts and a marker ("Here's how that could play out.").
3. arc4-03's Kyre Tree communion contains three opening takes plus an internal rewrite, and arc4-03's crowd scene, arc4-02's search scene and Nefere entrance, arc4-05's kill scene and water hole, and arc4-06's grimoire demonstration each exist in two published takes.
4. arc4-01 L394: a long Ajani speech is missing its closing quote (file total 277 double quotes = odd; DQ walker unbalanced to EOF).
5. Arc I–II typo battery found **zero** hits in Arc IV; the new typos found (whar, hare, coming, Sylvia, togheter, traning stipen…) are all in lowercase dialogue lines.
6. Canon compliance is otherwise solid: king/King fully compliant (41/41), em-dash usage consistent (559 em, 0 en, splits ≡ umbrella), Humman deviations confined to 9 narrative tokens + 3 tokens inside meta lines slated for deletion.

**Editorial-history note:** the `.stripped_meta` / `.stripped_passes` / `.repass3` / `.alpha_excise` artifacts show a cleanup pipeline ran pre-publication; it demonstrably did not cover author-voice planning prose, asterisk self-prompts, or duplicated takes. The remediation pass designed from this report should be added to that pipeline's marker set.

---

## 2. Per-Chapter Defect Catalog

Tags: **[M]** mechanical (scriptable), **[E]** editorial (judgment deletion/reword, canon determined here), **[J]** needs Ainz-sama's decision. Line numbers are split-file lines; umbrella lines in parentheses where located.

### 2.1 chapter-arc4-01.md — "Bureaucracy" (564 lines; umbrella L1–564)

| Line | Defect | Class |
|---|---|---|
| L5 | Crossed delimiters: `*i seriously hare this woman' … 'lets see what they want *` — thought opened `*`, closed `'`, then `'…` closed `*`. Also `hare`→hate, `lets`→let's, lowercase *i*. | M |
| L181 | Thought line: `'next as long as i Live, … 'i hear the screams coming '` — lowercase *i*; `coming`→coming; `Live` miscapitalized; `" ,` space-before-comma. | M |
| L220–222 | Ajani speech **outside dialogue markup**, opening `"` never closed on the line; closing quote sits alone on L222 (`"`), two blank lines apart. Line contains `thats`, `were`→we're and five lowercase family names (bright paws, shadow paws, motted paws, stripe paws). | E (restructure into dialogue-block) + M |
| L277 | Thought `'goos they're nots just going along'` (`goos`→good, `nots`→not); `humman` lowercase; `traning stipen`→training stipend (line tail: "providing a traning stipen[d]"). | M |
| L371 | `"…Maren sounds like hell Fit right in, objections?"` — `hell Fit` is either "she'll fit" (corruption) or legit "hell" + fragment; ambiguous. Also `roles ,` spacing. | J (J7) + M |
| L394 | **Missing closing quote**: long lowercase Ajani speech opens `"the security advisor will oversee…` and ends `…they need to do this before 20 years` with no `"`. Whole file has 277 double quotes (odd); DQ walker unbalanced at EOF. Also `capitals shield`→capital's shield; `20 years`→twenty years. | M (priority) |
| L418–552 | **Scaffold document #1 published**: "Here is a comprehensive summary of Ethra and Ajani's tale, verified against everything we…" followed by bold sections **The Cosmic Structure of Ethra / The Magic System / The Super-Organisms / The Biomes / The Seven Sentient Races / The Five Tyrants / Ajani's Tale** (~135 lines; umbrella L417–552). Contains `wengari` lowercase at split L551. Story resumes at L554 (acceptance scene continues into arc4-02 — normal split boundary). | E delete |

### 2.2 chapter-arc4-02.md — "The Caravans" (597 lines; umbrella L565–1161)

| Line | Defect | Class |
|---|---|---|
| L37–95 | **Scaffold document #2 published**: **The Chapter's Cadence / Ajani's Voice / What This Reveals About the Speaker** (umbrella L599–657). Includes meta sentences "Ajani's internal monologue is the chapter's emotional engine…" (L48, embedded inside a dialogue-block before legitimate speech) and "The speaker also reveals a deep understanding of character voice…" (L65). L48 carries the only split-`human` deviation (dies with the line). | E delete |
| L97 / L115 / L131 | Bold scene headings: `**The Shadow Paws — Underground Training Halls, Night**`, `**The Bright Paws — Temple of the Lightbringer, Night**`, `**The Motted Paws — The Silent Halls, Midnight**` (umbrella L659/677/693). No Arc I–III published chapter uses headings. | J (J3) |
| L154 | `'lets see what they want now'` (`lets`); `whar can this king d…`→what; `wengari`, `white dawn` lowercase. | M |
| L157–166 | **Nefere entrance — take A** (duplicated by take B at L167–176; entrance paragraph and title dialogue appear verbatim twice). | E delete (canon = take B) |
| L182 | `i am not being dragged to that stink bugs nest !!` — lowercase *i*; `stink bugs nest`→stink bugs' nest; `nefere` lowercase; `stripe paws` lowercase (line start). | M |
| L204 | `'i hope shes already spying on the hummans'` — lowercase *i*; `shes`→she's; `hummans` lowercase. | M |
| L240 | `"send in the humans"` — single-m deviation (narrative dialogue); `call Sylvia`→**Sylva** (name typo; corpus census: Sylvia=1, Sylva=59); `armor ,` spacing. | M |
| L288 | T'vat the attendant reference — canon per Arc I–II D4; no action. | — |
| L315 / L353 / L375 | Double-marked thoughts `*'…'*` (e.g. `*'no one fainted...so disappointing…'*`). Canon: thoughts single-quotes only. | M (strip asterisks) |
| L326–328 | **Humman greeting — v1** ("The Hummans are honored by the king's welcome…") duplicated by revised v2 at L336–338 ("…despite the tremor in the merchant behind her"). Sylva's formal welcome L329–333 sits between and is kept. | E delete v1 |
| L391–436 | **Search scene — take A**: includes `"GUARDS WHAT DID YOU FIND ?'` (opens `"`, closes `'` — crossed) and the meta line L427 "**In Chapter Three**, during the delegations, Seris and her merchants could barely take ten steps…" (author continuity note in prose). Superseded by take B L439+ per marker L437. | E delete; L391 quote M if salvaged |
| L437 | Marker: "Let me rewrite the scene from the search onward." | E delete |
| L478 / L494 | ALL-CAPS shouts with stacked punctuation `?!,` `!!` — cleanup pattern (also L413, arc4-03 L398–434). | M |
| L494 / L538 / L566 | `humman` lowercase (in dialogue/thoughts). | M |
| L552 / L556 | `hummans` lowercase; `wengari` lowercase; **`veylara`** x2 (L552, L566) — Arc I–II D7 precedent says probably "Veylar". | M + J (J5) |

### 2.3 chapter-arc4-03.md — "The Pyrinae Accord" (545 lines; umbrella L1162–1706)

| Line | Defect | Class |
|---|---|---|
| L151–167 | **Communion opening — take A** (short version; ends with Ajani walking away, contradicting the negotiation that follows). | E delete |
| L169 | Asterisk author self-prompt: `*You can start wherever you see fit as long as all threads are covered and we arrive with ajani at the end in the inner chamber*` (umbrella L1327). | E delete |
| L171–210 | **Communion opening — take B** (superseded by marker L211). | E delete |
| L211 | Marker: "Let me rewrite Ajani's opening and the Tree's response." Take C (canon) begins L213. | E delete |
| L233–389 | Entity ("Golden Sun") speech rendered as 22 balanced asterisk blocks across paragraph pairs. Canon §3 requires speech in double quotes; this is stylized telepathy. Asterisks balance file-wide (no unclosed spans). | J (J1) |
| L253–271 | Premature acceptance block ("I accept your pact… This is the new pact. It is done. Now go.") sits **before** the point-by-point objections (L273+/L299+) and the final acceptance L387–389 — layered drafts of the negotiation; reading order is contradictory. | J (J2) |
| L270 / L338 / L388 | Pact phrase "and when the tide comes, i will shield your people…" x3 — fingerprint of the layering above. | J (J2) |
| L273–295 | **Tree's response — v1**, superseded by v2 at L299–315 per marker L297 (pairs: L274/L300, L283/L305). | E delete |
| L297 | Marker: "Let me rewrite the Tree's response." | E delete |
| L342 | `styx` lowercase; contractions `dont`, `its` in the Golden-Sun naming speech. | M |
| L366 | `wengari` lowercase; `togheter`→together; `doesnt`, `ill`, `thats`. | M |
| L398–434 | ALL-CAPS proclamation with missing apostrophes: CANT, DOESNT, DONT, HES×3, IM×2, ISNT, IVE, ILL (L246, L318, L342, L366, L398, L416, L434, L464, L522 — 25 hits, all in this chapter). | M |
| L420–480 | **Crowd scene — v1** (plaza reactions: warrior, merchants, Seris, priests, `now old thing dont let me down`), superseded by crowd-perspective v2 L483–546 per marker L481. Overlap fingerprints: L427≡L545 ("Sylva stood motionless…armor gleaming"), L449≡L544 ("her daughter was in Sylva's service"). | E delete |
| L481 | Marker: "Let me rewrite the scene from the crowd's perspective." | E delete |

### 2.4 chapter-arc4-04.md — "The Humman Delegation" (612 lines; umbrella L1707–2318)

| Line | Defect | Class |
|---|---|---|
| L10 | ALL-CAPS with ILL, DONT, YOULL + lowercase *i* thought `'good, now all of them will walk it, this is so tiring.. i need a bath'`. | M |
| L305–313 | **Planning block (5 paragraphs)**: "I need to either retroactively establish her or remove her entirely…"; "The Fire Beetles fill a crucial gap…"; "This explains why the Bright Paws…live in walled cities…"; "The evolutionary arms race you have described is elegant…" (co-author address); "Kira's revised backstory is grounded in this ecology…" (umbrella L2007–2015). | E delete |
| L316–363 | **Kira market scene — take 1** (pens → scratch → alley dialogue → west-wall-breach exchange). | E delete |
| L364 | Asterisk self-prompt: `*lets start then, ajani is in the market escaping the palace as usual… its a bit Aladdin like but i believe it works, feedback?*` (umbrella L2066). | E delete |
| L366–418 | **Kira market scene — take 2** (adds market intro paragraph; same beats). | E delete |
| L420 | Marker: "Here's how that could play out." — contains the chapter's single stray curly apostrophe (`'`, U+2019; quote census: curlyClose′=1). Deleting the line resolves both. | E delete |
| L422–470 | Kira market scene — **take 3 = CANON** (continues into new content L472+: Sera appears, blood pact L486). | keep |
| L483 | `youre`→you're. | M |
| L507 | `'cheeky little...' - "…cooped in the palace me hahaha!!!…"` — `palace me` probably "palace, meh,"; minor. | M (low) |
| L536–564 | **Craft-critique block (15 paragraphs)**: numbered "First/Second/Third/Fourth" analysis of the Kira scene ("Kira is walking exposition, and you designed her…", "The west wall breach becomes a historical event we feel because we meet someone…", "oldest and most effective trick in the storyteller's kit") ending in asterisk rebuttal L564 `*No, it's because she's walking exposition, through her we can learn lore in an organic way… schism she's…*` (umbrella L2244–2266). Story resumes L566 (Vex). | E delete |

### 2.5 chapter-arc4-05.md — "The Gifts" (678 lines; umbrella L2319–2996)

| Line | Defect | Class |
|---|---|---|
| L53 | Asterisk self-prompt: `*With that understanding let's continue the vignettes ajani met Kira one week after the golden Sun, you must now include vignettes of her… we should see her in class with tutors, with sylva,*` (umbrella L2366). Contains meta-`hummans`. | E delete |
| L70 | `"tell it to my face humman"` — lowercase humman. | M |
| L93–111 | **Kill scene — take A** (merchant's death; calm Ajani self-intro "I am Ajani, first of my name…"). Superseded by take B L113–143: continuation L141 ("dragged the dead merchant's body **to Seris's feet**") matches take B's L113 placement, not take A's. | E delete |
| L113–143 | Kill scene — take B = CANON (ALL-CAPS shout L128–138; "AND THIS IS KIRA! MY SISTER!"). | keep |
| L148 | `ill` ×2 = "We will never speak **ill** of you again…" — legitimate word; false positive, no action. | — |
| L373–435 | **Water-hole scene — take A** (setup through Zara stepping forward / Ajani rising). Superseded by take B L438+ whose continuation (Vasha/Ember arrival L456+, reunion L459–493) is what the chapter continues with. Take A's unique beats (Zara L431, Ajani rising L435) are covered in take B at L496. | E delete |
| L438–439 | **Nested markup bug in canon take B**: `<div class="dialogue-block">` opened twice before "This is perfect". | M (fix while keeping B) |
| L514–528 | **Planning block (8 paragraphs)**: "Kira has been carrying that bag for months. Ajani noticed it but never asked…"; "Vex told her about the daggers…"; "And then the elders changed the gift without telling them."; "Kira's outburst is not merely disappointment. It is betrayal…"; "Vex's reaction **will be** the most telling moment…"; "Ajani **will be** looking at Kira…"; "The Stripe Paws grinning…is the perfect punctuation…"; "I have only one small note. The Tide Wolf claw beads are a beautiful detail, but we should make…" (umbrella L2828–2842). Story resumes L529 (Shadow Paw contingent) — the planned scene does exist after the block, so deletion is safe, but the L528 note ("we should make…") may encode an intended tweak worth applying. | E delete (+J6 note) |

### 2.6 chapter-arc4-06.md — "Aftermath" (676 lines; umbrella L2997–3668)

| Line | Defect | Class |
|---|---|---|
| L25–67 | **Grimoire demonstration — take A**: thought block L27–29 `*Perhaps it will work...*`; test ritual; Elyra explanation v1 (L50 "The grimoire is bound to its owner. As you use it, it will grow…"); "This is the best gift…" L54; coda L65–67 (sorcery reflection + "the green fire was still flickering…") unique to this take. Superseded by take B. | E delete (+J4 coda salvage) |
| L69–116 | Grimoire demonstration — **take B = CANON**: Elyra explanation v2 (L94 "It is a living thing…"); revised echo L106 "This is **still** the best gift I have received today."; continuation L117+ ("He opened his mouth to answer…") flows from B. | keep |
| L72 | Asterisk thought `*Perhaps it will work...*` inside canon take B — canon §3: thoughts in single quotes, never `*…*`. | M (*→') |
| L184 | Asterisk self-prompt: `*Very well are we ready to continue with the gift giving? We are only missing the humans and the explanation of what ajani tried to do with the grimoi[re]…*` (umbrella L3175). Contains meta-`humans`. | E delete |
| L197 / L289 / L297 | Asterisk thought-blocks: `*Please, please not one of those foul creatures please.*`, `*Get them off!! Get them off!!*`, `*Oh. This isn't so bad… kind of cute.*` — likely Kira's thoughts; verify attribution when converting. | M (*→') |
| L330 / L430 / L496 | Possessive apostrophes (elders', scorpion's, Ajani's) — delimiter-checker false positives; no action. | — |
| L482–484 | "The king was **ill**." — legitimate word (Ajani's condition), false positive. "the **Humman King** was coming" — capitalized office title; compliant by Rule-2 analogy (cf. "King of the Wengari"); noted only. | — |

---

## 3. Canon-Rule Compliance

### 3.1 king/King — **PASS**
- Splits: `King` capitalized 41×, lowercase `king` 360×; umbrella identical (41/360).
- Every capitalized instance verified by context dump: all are title+name ("King Ajani" ×37) or formal office/proclamation titles ("King of the Wengari" arc4-02 L40–46; "the Humman King" arc4-06 L482–673 — Rule-2 analog).
- Zero lowercase `king Ajani/Uthgard` violations (umbrella-wide targeted check: none).
- Generic/apposition/direct-address uses correctly lowercase throughout ("the king was ill", "my king").

### 3.2 Humman — **NEAR-PASS (9 narrative deviations, all mechanical)**
- Canon forms dominate: splits Humman 99 (98 in umbrella + 1 in the generator-inserted arc4-04 heading) + Hummans 96. Umbrella: 98 + 96.
- Deviations (12 tokens): narrative 9 — arc4-01 L277 `humman`; arc4-02 L240 `humans`, L494/538/566 `humman`, L204/552×2 `hummans`; arc4-05 L70 `humman` — plus 3 tokens sitting in meta lines already condemned for deletion (arc4-02 L48 `human`, arc4-05 L53 `hummans`, arc4-06 L184 `humans`). After debris removal + mechanical fixes: zero.
- Corpus check reproduces the Arc I–II tally artifact (negative "plain human" count = arithmetic artifact of subtracting double-m from single-m totals; disregarded as in the reference report).

### 3.3 Dialogue formatting — **FAIL (bounded, enumerated)**
- Speech uses ASCII straight double quotes everywhere; curly quote census clean except one stray U+2019 apostrophe at arc4-04 L420 (a marker line — dies with deletion).
- **Quote balance:** arc4-01 has 277 double quotes (odd). Root cause L394 (speech missing closing `"`); the L220/L222 anomaly (orphaned closing quote on its own line) is internally paired. DQ walker otherwise balanced in all six chapters.
- **Crossed/double-marked:** arc4-02 L391 `"GUARDS WHAT DID YOU FIND ?'` (open `"` close `'`); arc4-02 L315/353/375 `*'…'*` double-marked thoughts; arc4-01 L5 `*…'…'…*` crossed. All mechanical.
- **Asterisk thoughts:** five thought-blocks in arc4-06 (L28 — dies with take A, L72, L197, L289, L297) render thoughts as `*…*` — canon requires single quotes.
- **Entity speech:** arc4-03 L233–389 asterisk blocks — J1 (stylistic telepathy vs canon).
- **Contractions:** 38 battery hits; 3 false positives (`ill` legitimate ×3), 1 ambiguous (`hell` — J7), 2 inside condemned meta lines; **32 genuine mechanical fixes**, concentrated in ALL-CAPS proclamation lines (arc4-03: 25).
- **Standalone lowercase *i*:** 14 genuine (arc4-01 ×2, arc4-02 ×2, arc4-03 ×8, arc4-04 ×2) + 1 inside condemned meta (arc4-04 L364).
- **Lowercase proper nouns:** ~20 narrative lines (arc4-01 L93/L143/L220; arc4-02 L154/L182/L315/L494–L566; arc4-03 L342/L366) — family names, Wengari, White Dawn, Styx, Veylara (→J5). All inside lowercase dialogue/thought lines; mechanical capitalization pass.

### 3.4 Em dashes — **PASS (canon maintained)**
- Splits: 91+110+96+94+93+75 = **559 em dashes = umbrella 559 exactly**; **0 en dashes, 0 hbars, 0 ASCII-hyphen dialogue openers**.
- Odd-count lines 279, classified: CUT(speech) 36, TAIL(elaboration) 59, OPEN-MID(suspect heuristic) 184. Spot-samples of OPEN-MID (arc4-01 L89/L398/L424, arc4-03 L349, arc4-04 L428, arc4-06 L653) are all canon usage #3 (single dash introducing an elaboration running to sentence end) or paired parentheticals. Inherits Arc I–II D1: full 184-line review list is only needed if Ainz-sama declines the canon reading.

---

## 4. Umbrella Draft-Debris Inventory

All fixes target `content/story/chapter-04.md`. Umbrella line numbers below were located by exact text search (umbrella_locate.py / umbrella_debris_scan.py). Keep/delete = recommendation; canon evidence in §5 where applicable.

| Umbrella lines | Split location | Debris type | Keep/Delete |
|---|---|---|---|
| L417 | arc4-01 L418 | "Here is a comprehensive summary of Ethra and Ajani's tale, verified against everything we…" | DELETE |
| L419–552 (headings L419/425/431/439/453/473/487) | arc4-01 L420–552 | Scaffold doc #1: Cosmic Structure / Magic System / Super-Organisms / Biomes / Seven Sentient Races / Five Tyrants / Ajani's Tale | DELETE |
| L599–657 (headings L599/607/617) | arc4-02 L37–95 | Scaffold doc #2: The Chapter's Cadence / Ajani's Voice / What This Reveals About the Speaker (contains "emotional engine" L610, "reveals a deep understanding" L627) | DELETE |
| L659 / L677 / L693 | arc4-02 L97/115/131 | Bold scene headings (Shadow/Bright/Motted Paws night vignettes) | J3 (delete vs keep-as-separators) |
| L719–736 | arc4-02 L157–176 | Nefere entrance, two takes | DELETE take A (L719–726 ≈ split L157–166) |
| L888–898 | arc4-02 L326/336 | Humman greeting v1/v2 | DELETE v1 (L888) |
| L989 | arc4-02 L427 | "In Chapter Three…" author continuity note | DELETE (inside take A block) |
| L999 | arc4-02 L437 | Marker "Let me rewrite the scene from the search onward." | DELETE |
| L~953–998 | arc4-02 L391–436 | Search scene take A (incl. crossed quote L391) | DELETE (canon = L1001+) |
| L1311–1367 | arc4-03 L151–167 + prompt L169 | Communion take A + asterisk self-prompt (L1327) | DELETE |
| L1329–1368 | arc4-03 L171–210 | Communion take B | DELETE |
| L1369 | arc4-03 L211 | Marker "Let me rewrite Ajani's opening and the Tree's response." | DELETE |
| L~1425–1454 | arc4-03 L273–295 | Tree's response v1 | DELETE (canon = L1457+) |
| L1455 | arc4-03 L297 | Marker "Let me rewrite the Tree's response." | DELETE |
| L~1415–1435 vs L1465–1545 | arc4-03 L233–389 | Entity asterisk-block negotiation; acceptance layer L253–271 vs final L387–389; pact phrase x3 (umbrella L1427/1495/1545) | J1 + J2 |
| L1585–1641 | arc4-03 L420–546 | Crowd scene v1/v2 overlap (fingerprints L1585≡L1703, L1625≡L1641) | DELETE v1 (marker L1639; canon = L1641+) |
| L1639 | arc4-03 L481 | Marker "Let me rewrite the scene from the crowd's perspective." | DELETE |
| L2007–2015 | arc4-04 L305–313 | Kira planning block (5 paragraphs) | DELETE |
| L2018–2065 | arc4-04 L316–363 | Kira scene take 1 (tripled at L2018/2070/2126) | DELETE |
| L2066 | arc4-04 L364 | Asterisk self-prompt "lets start then… Aladdin like… feedback?" | DELETE |
| L2068–2121 | arc4-04 L366–418 | Kira scene take 2 | DELETE |
| L2122 | arc4-04 L420 | Marker "Here's how that could play out." (+ stray curly apostrophe) | DELETE |
| L2124–2172 | arc4-04 L422–470 | Kira scene take 3 | KEEP (canon) |
| L2244–2266 | arc4-04 L536–564 | Craft-critique block + asterisk rebuttal ("walking exposition" L2254/2266) | DELETE |
| L2366 | arc4-05 L53 | Asterisk self-prompt "let's continue the vignettes…" | DELETE |
| L2406–2424 | arc4-05 L93–111 | Kill scene take A | DELETE (canon = L2426+) |
| L2692–2752 | arc4-05 L373–435 | Water-hole take A | DELETE (canon = L2754+) |
| L2828–2842 | arc4-05 L514–528 | Planning block (8 paragraphs; L2842 ends mid-sentence "but we should make…") | DELETE (verify J6 tweak first) |
| L3016–3056 | arc4-06 L25–67 | Grimoire take A (thought-block L3018–3020; coda ≈L3054–3056) | DELETE (J4 coda salvage) |
| L3060–3106 | arc4-06 L69–116 | Grimoire take B | KEEP (canon) |
| L3175 | arc4-06 L184 | Asterisk self-prompt "are we ready to continue…" | DELETE |
| L2572 | (stripped by generator; not published) | Stale heading "## Chapter 5: The Gifts" (old flat numbering; the only sub-chapter with an internal heading) | DELETE |
| L1 / L2300 / L2348 | — | "# Chapter 4" title (generator strips); "corrected" in narrative prose (Kira vignettes) | KEEP (not debris) |

---

## 5. Duplicate Blocks with Canon Designation

Nine complexes. Canon direction determined by (a) author markers, (b) revision fingerprints, (c) narrative continuity of the text that follows each block. "Takes" are listed in file order.

| # | Scene | Takes (split lines) | Canon | Evidence |
|---|---|---|---|---|
| 1 | arc4-02 Nefere entrance | A: L157–166 · B: L167–176+ | **B** | Entrance paragraph + title dialogue verbatim in both; B continues into extended road dialogue; A's tail sentences (L162/L166) are reissued in B (L172/L176) |
| 2 | arc4-02 Humman greeting | v1: L326–328 · v2: L336–338 | **v2** | v2 adds "despite the tremor in the merchant behind her" (links preceding scene); Sylva's welcome L329–333 between them is unique and kept |
| 3 | arc4-02 Search scene | A: L391–436 · B: L439–500+ | **B** | Marker L437 "Let me rewrite the scene from the search onward."; B supersedes A's letter-device with the sleeve-stone device and continues into the confrontation. Note: A's "sealed letter" beat has no downstream references found (crossref_letter.py); verify stone-device consistency with arc5 at remediation |
| 4 | arc4-03 Communion opening | A: L151–167 · B: L171–210 · C: L213+ | **C** | A ends with Ajani leaving (contradicts continuation); marker L211 explicitly rewrites into C; self-prompt L169 sits between A and B |
| 5 | arc4-03 Tree's response | v1: L273–295 · v2: L299–315 | **v2** | Marker L297; pairs L274≡L300, L283≡L305 |
| 6 | arc4-03 Crowd scene | v1: L420–480 · v2: L483–546 | **v2** | Marker L481 "rewrite the scene from the crowd's perspective"; overlap fingerprints L427≡L545, L449≡L544 |
| 7 | arc4-04 Kira market scene | 1: L316–363 · 2: L366–418 · 3: L422–470 | **3** | Marker L420 "Here's how that could play out."; take 3 flows into unique continuation (Sera, blood pact L472–486); 6 core paragraphs verbatim x3 |
| 8 | arc4-05 Kill scene | A: L93–111 · B: L113–143 | **B** | Continuation L141 matches B's staging (body "to Seris's feet"); B's shout-version self-intro is what the following Kira scene responds to |
| 9 | arc4-05 Water-hole scene | A: L373–435 · B: L438–452+ | **B** | Continuation (Vasha/Ember arrival, reunion L459–493) flows from B; A's unique beats (Zara L431, Ajani rising L435) recur in B-continuation at L496 |
| 10 | arc4-06 Grimoire demonstration | A: L25–67 · B: L69–116 | **B** | B revises the echo ("This is **still** the best gift") and expands Elyra's lore ("It is a living thing"); continuation L117+ answers B's closing silence. **Salvage note:** A's coda L65–67 (sorcery reflection) is unique — see J4 |

**Layering caveat (not a simple block deletion):** complex 4's continuation contains the entity negotiation with a premature acceptance block (arc4-03 L253–271) preceding the objections and the final acceptance (L387–389); pact language appears x3 (L270/338/388). Untangling this reading order is J2.

---

## 6. Remediation Classification

### 6.1 MECHANICAL (scriptable closed map — no creative judgment)

| Fix | Lines (split) | Operation |
|---|---|---|
| Missing closing quote | arc4-01 L394 | Append `"` at speech end (then re-run quote walker; expect balance) |
| Crossed quote | arc4-02 L391 | `'`→`"` at line end |
| Crossed/double-marked thoughts | arc4-01 L5; arc4-02 L315, L353, L375 | Strip `*`, keep single quotes |
| Asterisk thought-blocks | arc4-06 L72, L197, L289, L297 (L28 dies with take A) | `*…*`→`'…'`; verify owner (likely Kira) |
| Contractions | arc4-01 L5, L220; arc4-02 L154, L204; arc4-03 L246, L318, L342, L366, L398, L416, L434, L464, L522; arc4-04 L10, L483 | Insert apostrophes (incl. inside ALL-CAPS: CANT→CAN'T etc.) |
| Lowercase *i* | arc4-01 L5, L181; arc4-02 L182, L204; arc4-03 L246, L318, L342, L522; arc4-04 L10 | Capitalize standalone I |
| Race name | arc4-01 L277; arc4-02 L204, L240, L494, L538, L552×2, L566; arc4-05 L70 | humman(s)→Humman(s), humans→Hummans |
| Proper nouns | arc4-01 L93, L143, L220; arc4-02 L154, L182, L315, L494–L566 (wengari, white dawn, stripe paws, family names); arc4-03 L342 (styx), L366 | Capitalize |
| Typos | arc4-01 L5 hare→hate, L181 coming→coming + Live→live, L277 goos→good/nots→not/traning stipen→training stipend; arc4-02 L154 whar→what, L240 Sylvia→Sylva; arc4-03 L366 togheter→together; arc4-02 L182 stink bugs nest→stink bugs' nest; arc4-01 L394 capitals shield→capital's shield, 20 years→twenty years; arc4-04 L507 palace me→palace, meh (low confidence) | Word map |
| Punctuation spacing/stacking | arc4-01 L181/L371 `" ,` `roles ,`; arc4-02 L391 `?'`; ALL-CAPS `?!,` `!!` (arc4-02 L413/L478/L494; arc4-03 L398–434) | Normalize |
| Nested div | arc4-05 L438–439 | Remove duplicate `<div class="dialogue-block">` |

All of the above live in the umbrella at the §4-mapped positions; apply there, regenerate splits, re-run `QA/arc4_tooling/` battery as acceptance gate.

### 6.2 EDITORIAL (judgment deletion/reword; canon already determined by this audit)

Execute §4 DELETE rows + §5 canon designations. Order of operations: (1) delete scaffold docs and meta blocks; (2) delete superseded takes (keep canon takes); (3) delete markers/prompts; (4) delete stale umbrella heading L2572; (5) restructure arc4-01 L220–222 orphaned speech into a dialogue-block; (6) mechanical pass §6.1; (7) regenerate + battery re-run. Estimated removable volume ≈650 lines (~18% of published arc). No creative rewriting required — every deletion has a surviving canon counterpart except the scaffold docs (pure planning text; the story they summarize is told in-scene elsewhere).

### 6.3 JUDGMENT (needs Ainz-sama's decision)

| ID | Item | Options / recommendation |
|---|---|---|
| J1 | arc4-03 L233–389: entity ("Golden Sun") speech as asterisk blocks | (a) convert to double-quoted dialogue like other speakers; (b) convert to single-quoted telepathy per thought-canon; (c) keep as deliberate telepathic styling. Rec: (b) or (c) with an explicit canon rule for telepathy |
| J2 | arc4-03 communion layering: premature acceptance L253–271 vs objections L273+/L299+ vs final acceptance L387–389; pact phrase x3 | Requires a read-through to order the negotiation coherently; likely demote L253–271 to a tentative "I am listening" beat or delete |
| J3 | arc4-02 L97/115/131 bold scene headings | Delete (Arc I–III precedent: no headings) or keep as scene separators; if kept, style consistently |
| J4 | arc4-06 take-A coda L65–67 (sorcery reflection, unique prose) | Salvage into take B's continuation, or drop |
| J5 | arc4-02 L552/L566 `veylara` | Arc I–II D7 precedent: probably "Veylar"; confirm intent |
| J6 | arc4-05 L528 planning note ends mid-thought ("…but we should make…") | Recover the intended tweak from `.stripped_passes`/`.repass3` artifacts if desired before deleting (artifacts are read-only reference) |
| J7 | arc4-01 L371 "Maren sounds like hell Fit right in" | Reconstruct intent ("she'll fit right in" vs legit "hell"), then fix |
| D1 (inherited) | 184 OPEN-MID em-dash lines | Only if Ainz-sama declines the Arc I–II canon reading; spot samples are compliant |

---

## 7. Status

- [x] Skeleton created (2026-08-24)
- [x] Lint battery executed on splits (lint_arc4.py, lint_pass2_arc4.py, quote_pair_check_arc4.py, delimiter_cross_check_arc4.py, em_census_arc4.py, em_classify_arc4.py, final_tally_arc4.py)
- [x] Umbrella debris scan executed (umbrella_debris_scan.py + umbrella_locate.py/.2 + umbrella_headings.py; grep + targeted line reads only — no whole-file reads)
- [x] Spot-verification of script output against actual lines (all catalog entries read in source; take boundaries walked line-by-line)
- [x] Sections 1–6 filled
- [x] **FINAL** — audit complete. No story content was modified; outputs confined to `QA/arc4_audit_report.md` and `QA/arc4_tooling/`. Awaiting Ainz-sama's judgment on J1–J7 before remediation executes.




