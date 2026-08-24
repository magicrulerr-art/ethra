# Ethra QA Report — Arc III ("The Tournament") Proactive Audit

- **Prepared by:** Demiurge's audit subagent — script-first audit using the defect battery established in the Arc I–II reader-feedback audit (`QA/arc1_arc2_reader_feedback_report.md`).
- **Date:** 2026-08-24
- **Scope (READ-ONLY):** published splits `content/story/chapters/chapter-arc3-01..05.md` + umbrella master `content/story/chapter-03.md` (276.7 KB, 2,893 lines; scanned via grep + targeted line reads only).
- **Tooling:** `QA/arc3_tooling/` — adapted copies of the Arc I–II battery (FILES re-targeted to arc3; originals untouched): `arc3_lint.py`, `arc3_lint_pass2.py`, `arc3_em_census.py`, `arc3_em_classify.py`, `arc3_quote_pair_check.py`, `arc3_delimiter_cross_check.py`, `arc3_final_tally.py`, `arc3_umbrella_scan.py`, `arc3_typo_probe.py`, `arc3_dialogue_probe.py`, `arc3_dash_edge_probe.py`. Raw outputs retained in the same folder.
- **Mode:** PROACTIVE — no reader feedback exists for Arc III.
- **Line numbers:** split line numbers refer to the published chapter files; umbrella line numbers to `chapter-03.md`. All cited lines were spot-verified by direct read.

---

## 1. Executive Summary

### 1.1 Defect counts per class (published splits)

| # | Defect class | Count | Verdict |
|---|---|---|---|
| 1 | Contractions missing apostrophe | **23 hits / 11 lines** | MECHANICAL |
| 2 | Standalone lowercase "i" | **13 hits / 5 lines** | MECHANICAL |
| 3 | Dialogue delimiter defects (asterisk thoughts / crossed `*…'`) | **13 blocks; 8 crossed or double-marked** | MECHANICAL (normalize) |
| 4 | Em-dash canon | **421 em dashes, 0 unclosed / 0 off-canon** | PASS |
| 5 | Race-name deviations (`humans`, `hummans`) | **4 hits, all in arc3-01** | MECHANICAL |
| 6 | king/King rule | **0 violations** (29 "King Ajani", 251 generic lowercase) | PASS |
| 7 | Meta/scaffold contamination | **4 sites** (incl. 2 large blocks) | EDITORIAL delete |
| 8 | Duplicate draft blocks | **10 groups** (3 chapter-scale) | EDITORIAL delete (canon designated, §5) |
| 9 | Typos / garbled words | **24 distinct fixes** | MECHANICAL / EDITORIAL |
| 10 | Lowercase proper nouns | **7 hits** (subset of #9) | MECHANICAL |
| 11 | Quote balance (double quotes) | **0 anomalies** — balanced in every chapter | PASS |

Split-vs-umbrella consistency verified: Humman census, king/King census, and em-dash totals are identical between umbrella and splits (Humman 34 / Hummans 33 / humans 3 / hummans 1; King 29 / king 251; em dashes 421) — no drift between master and published files.

### 1.2 Arc health verdict

**CONDITIONAL PASS — publish-blocked by draft debris, not by mechanics.**

Arc III inherits the Arc I–II mechanical cleanup: dialogue quotes are perfectly balanced, king/King is fully canon, em dashes are fully canon (no unclosed dashes, no ASCII-hyphen openers), and Humman spelling is canon in four of five chapters. The remaining mechanical layer is small and fully scriptable (~60 closed replacements).

However, Arc III is the first arc with **large-scale structural debris in published chapters**: a triple-drafted phase-one aftermath in arc3-03 (three mutually contradictory recap layers plus a duplicated battle sequence), a misplaced pre-interlude draft of the Solen confrontation in arc3-02, a duplicated mounted-phase opening in arc3-04, a ~50-line author craft-notes block (`**Logic**`) in arc3-05, a bestiary-style lore dump with a "Lore Confirmed" scaffold heading in arc3-01, and a compressed duplicate of Sylva's concession in arc3-05. All duplicate blocks have been cross-referenced against downstream chapters (arc3-03 → arc3-04 → arc3-05 continuity) and canon versions are designated in §5; every deletion is determinable without Ainz-sama's input except three flagged JUDGMENT items (§6.3).

---

## 2. Per-chapter defect catalog

### 2.1 chapter-arc3-01.md (524 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L45 | lowercase `wengari` ("welcome to the wengari brothers!") | MECH |
| L78 | `"t'vat call for the elder council of the striped paws, now please "` — lowercase T'vat, lowercase Stripe Paws, trailing space inside quote | MECH |
| L116 | `'therye here, good...'` → they're | MECH |
| L140 | lowercase `wengari` ("who rules the wengari?") | MECH |
| L158 | `hummans` (lowercase, double-m) — race-name case deviation | MECH |
| L176 | `the humans` ×2 (single-m) — race-name deviation | MECH |
| L194 | `the humans` (single-m) — race-name deviation | MECH |
| L208 | lowercase `stripe paws` ("the stripe paws will become what they were me…") | MECH |
| L318–326 | Torek farewell **version A** ("I have served four kings… Uthgard VII…") + premature scene-closing beat ("The elders filed out of the chamber… The negotiations were complete") — duplicate take of L330 | EDIT/JUDG (§5.1) |
| L330–332 | Torek farewell **version B** ("I served your father… Uthgard VIII…") — second take | EDIT/JUDG (§5.1) |
| L334–352 | `**The Fire Feet — Lore Confirmed**` scaffold heading + 7 bestiary-format bullets (L337–349, incl. the arc's only en dash, L341) + author planning prose (L352: "…are now trying to determine *which* caravan… Their goal is to offer him a fire feet as a coronation gift—but to do so discreetly…") | EDIT delete (§4, §5.2) |

### 2.2 chapter-arc3-02.md (646 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L219 | `'bow...what did father always said'` → say | MECH |
| L273 | `FRIEND'S!!` → FRIENDS; `CANT` → CAN'T | MECH |
| L360–383 | **Solen confrontation occurrence 1** — misplaced early draft (opens "The Bright Paw elders did not wait for the chaos to subside…", "Have you lost your mind?!", Vasha objection L369, "breakfast" joke L374, ends L383 without resolution) | EDIT delete (§5.3) |
| L533 | `*The king has put his crown on the line… What should I do?*` — the Quick's thought in asterisks; canon: thoughts in single quotes only | MECH normalize |
| L539 | `*The Bright Paw Elders (Closing Scene)*` — scaffold annotation "(Closing Scene)" in scene subheading | EDIT trim |
| L564 | `"tell me solen, who rules the wenfari ?"` — lowercase Solen; `wenfari` → Wengari | MECH |

### 2.3 chapter-arc3-03.md (590 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L40 | `'fhe sun is up in the sky…'` → the; `BROTHERS STEMMED GUESTS` → ESTEEMED | MECH |
| L90 | `RISED TO THE CHALLENGE` → RISEN; `LETS` → LET'S | MECH |
| L146 | `ESPECTACULAR` → SPECTACULAR; `ITS A TOURNAMENT` → IT'S | MECH |
| L230 | Quick's mycelial message in asterisks (`*The White Dawn does not ask for mercy…*`) | MECH normalize |
| L310–312 | Quick's pulse message in asterisks **spanning a blank line** (`*The White Dawn has changed the rules.` …blank… `The tournament will be a battle…*`) | MECH normalize + close |
| L338 | `*Let's begin!*` — asterisk thought delimiter | MECH normalize |
| L362 | `*'half of it down…'*` — double-marked thought (asterisk + single quote) | MECH normalize |
| L364–442 | **Phase-one battle occurrence 1** (draft: Rask charge L367 → ambush L373 → Rask falls to poison L419 → Motted Paws concede L433) + double-marked thoughts L393/L439 + stray fragment `*The basin erupted.*` L442 | EDIT delete (§5.4) |
| L393, L439 | `*'it begins '*`, `*'yes they would make good regents…'*` — double-marked thoughts (inside occurrence-1 block) | MECH normalize (if salvaged) |
| L442 | `*The basin erupted.*` — stray asterisk fragment, verbatim double of L364 | EDIT delete |
| L491–494 | **Recap layer X** — "The Motted Paws had drawn first blood. The Shadow Paws had lost two of three…" + "Six champions would advance. Two Shadow Paws. Two Motted Paws. Two Stripe Paws." — contradicts canon roster | EDIT delete (§5.4) |
| L497–532 | **Recap layer Y** — "Two champions remained standing…" (second occurrence) → "Four champions stood at the end of the first phase" — contradicts canon roster | EDIT delete (§5.4) |
| L535–550 | **Recap layer Z** — "Eight champions remained… The Stripe Paws had lost no one… Rask had fallen taking Thane with her" — internally contradictory | EDIT delete (§5.4) |

### 2.4 chapter-arc3-04.md (611 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L151 | `IN THE DESER` → DESERT; `FRIENDS PYRANEI` → PYRINAE; `ILL DEMONSTRATE` → I'LL | MECH |
| L186 | `Let's follow the arena as the Styx feathers measure the champions. The Pyrinae will handle the ceremony… The six champions will be paired…` — author planning transition (imperative + future-tense summary of the scene that follows) | EDIT delete (§4) |
| L515 | `'oh goody... war mounts!!!, i havent seen one since i was a child… i touched one?… dont look too much…'` — lowercase i ×3, havent, dont | MECH |
| L519–537 | **Mounted phase version A** ("The champions mounted. Thane… Rask… Sylva…" — Rask as rider; rules speech L535) — superseded draft | EDIT delete (§5.5) |

### 2.5 chapter-arc3-05.md (522 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L18 vs L82 | "The king was a fan of the fire feet" + Ember-gift planning beat twice (Zara POV) — redundant exposition | EDIT/JUDG (§6.3) |
| L70 | `'styx in heaven i blew it!!…'` — lowercase Styx, lowercase i ×2, `definetly` → definitely | MECH |
| L130 | `THEN I SHALL IS IT DONE` — garbled draft sentence; `PYRANEI` → PYRINAE; `'ill gauge their eyes out'` → I'll gouge | MECH/EDIT |
| L200–250 | `**Logic**` scaffold heading + 14 author craft-analysis paragraphs (future-tense planning: "This duel will be the tournament's defining memory…", "The feint is the resolution. Ajani will win…"), incl. verbatim-duplicated green-fire paragraph (L240 = L243) | EDIT delete (§4, §5.6) |
| L267 | `*OH, ok, she has claws... spear then'` — crossed `*…'` + cant/im missing apostrophes | MECH |
| L296 | `*What on....ok... calm, breathe, shes unarmed… dual blade'` — crossed `*…'`; shes/lets/dont/im; `dual blade` → dual blades | MECH |
| L325 | `*This is getting annoying!!!… catching me?!'` — crossed `*…'`; cant/im×3/wont; `Faint` → Feint; lowercase i ×3 | MECH |
| L351 | `*OK THIS ENDS NOW, SHE NEEDS TO GO DOWN, NOW'` — crossed `*…'`; youre/cant/havent/ill; lowercase i ×4; `loose` → lose; `millenia` → millennia; `heir of the light` → heir of the Light | MECH |
| L401 | `"The feint," she said quietly… "I yield. The crown is yours…"` — compressed early draft of the concession (canon at L422 + L427) | EDIT delete (§5.7) |
| L472 | `*what?'` opener + `'Infurating woman… statecraft...*` closer — crossed delimiters both ends; `Infurating` → Infuriating | MECH |
| L490 | `'im this close to skewering her..'` — im → I'm | MECH |

---

## 3. Canon-rule compliance

### 3.1 king/King — COMPLIANT (0 violations)

- 29 capitalized `King` in splits — **every one** is title+name ("King Ajani"; no "King Uthgard" appears in arc3). Spot-verified all 29 contexts via pass2 census: arc3-01 ×15, arc3-02 ×4 (L250, L379, L556, L572), arc3-03 ×4 (L85, L141, L157, L176), arc3-04 ×4 (L78, L124, L288, L327), arc3-05 ×2 (L147, L467).
- 251 lowercase `king` — all determiner/generic/apposition/direct-address uses ("the king", "my king", "their king", "a Bright Paw king").
- No "the King/a King" generic capitalization; no "My king" capitalization errors; no lowercase-before-name ("king Ajani") hits.
- Umbrella census identical (King 29 / king 251) — master and splits in agreement.

### 3.2 Humman/Humans — 4 deviations, all in arc3-01

Census (case-sensitive exact forms, splits = umbrella): `Humman` 34, `Hummans` 33, `humans` 3, `hummans` 1.

| Location | Form | Fix |
|---|---|---|
| arc3-01 L158 | `hummans` (lowercase) | `Hummans` |
| arc3-01 L176 | `the humans` ×2 | `the Hummans` |
| arc3-01 L194 | `the humans` | `the Hummans` |

All three single-m hits are in Zara's dialogue in the same negotiation scene — none are out-of-universe Earth-gloss contexts, so no exception applies. Chapters arc3-02..05 are fully canon.

### 3.3 Dialogue formatting

- **Double quotes:** ASCII `"` throughout (0 curly). Cross-line walk confirms **perfect balance in all 5 chapters** — no quote left open across a blank line or at EOF. No lines with odd double-quote count.
- **Single quotes:** all odd-parity lines verified as legitimate possessives/contractions (e.g., `families' champions` L437, `Vein-Dwellers' staffs` L132/L456, plural possessives at L68/L257/L579 of arc3-03) except the 8 crossed/double-marked lines below.
- **Asterisk canon (thoughts in single quotes ONLY):** 13 asterisk-wrapped thought/message blocks — all violations:
  - arc3-02 L533 (Quick's thought);
  - arc3-03 L230 (Quick message), L310–312 (Quick message spanning a blank line), L338 (`*Let's begin!*`), L362/L393/L439 (double-marked `*'…'*`), L442 (`*The basin erupted.*` stray fragment);
  - arc3-05 L267, L296, L325, L351, L472 — five blocks opened with `*` and closed with `'` (crossed) or vice versa.
  - Legitimate asterisk uses confirmed and excluded: bold scene headings (`**…**`), italic scene subheadings (arc3-02 `*The Pyrinae Section*` etc.), emphasis of quoted words (arc3-01 L63 `*The desert is not kind to the weak.*`, arc3-02 L607 `*Warm, unflinching, unforgiving.*`, arc3-05 L248 `*he*`), and the bestiary-style bullets in the arc3-01 scaffold block (deleted per §5.2).
- **Contractions missing apostrophe:** 23 hits / 11 lines — arc3-02 L273 (`CANT`); arc3-03 L90 (`LETS`), L146 (`ITS`); arc3-04 L151 (`ILL`), L515 (`dont`, `havent`); arc3-05 L130 (`ill`), L267 (`lets`), L296 (`dont`, `im`, `shes`, `lets`), L325 (`cant`, `wont`, `im`×4), L351 (`cant`, `ill`, `youre`, `havent`), L490 (`im`). All in Ajani's rough internal voice or shouted speech; closed replacement map in §6.1.
- **Standalone lowercase `i`:** 13 hits / 5 lines — arc3-04 L515 (×3); arc3-05 L70 (×2), L130 (×1), L325 (×3), L351 (×4). Same voice cluster as the contractions.

### 3.4 Em dashes — COMPLIANT (0 defects)

- Census: **421 em dashes** (arc3-01: 87, arc3-02: 83, arc3-03: 88, arc3-04: 78, arc3-05: 85); umbrella identical (421).
- 57 quote-adjacent dashes (`"—` / `—"`) = speech cutoffs — canon use 1.
- All 207 odd-count dash lines classified: every unpaired dash is either a speech cutoff or a dash introducing an elaboration running to sentence/paragraph end (canon use 3). The classifier's "OPEN-MID" heuristic flags were spot-verified on 8 lines (arc3-01 L30, arc3-02 L81, arc3-03 L200/L448, arc3-04 L186, arc3-05 L154/L240) — all legitimate elaborations, same narrative usage ratified in Arc I–II.
- **0 unclosed dashes:** no line ends in an em dash (no open parenthetical carried to the next line), no doubled/spaced dashes, no ASCII hyphen runs, no hyphen/en-dash dialogue openers.
- En dashes: exactly 1 — arc3-01 L341 (`30–35 years`), inside the bestiary scaffold block slated for deletion (§5.2); disappears with the block.

---

## 4. Umbrella draft-debris inventory (chapter-03.md)

All debris exists in the umbrella **and** in the published splits (verified by cross-line reads); the umbrella line numbers below anchor the source of truth for remediation. Debris-only rows — canonical narrative rows are not listed.

| Umbrella lines | Split counterpart | Debris | Disposition | Canon evidence |
|---|---|---|---|---|
| L319–325 | arc3-01 L320–326 | Torek farewell **version A** + premature closing beat | DELETE (or keep per §5.1 judgment) | version B leads directly into the continuing scene at L355 |
| L333–352 | arc3-01 L334–352 | `**The Fire Feet — Lore Confirmed**` scaffold + bestiary bullets + planning prose | DELETE from chapter (see §5.2) | scaffold marker; non-narrative format; planning prose is author-voice |
| L883–906 | arc3-02 L360–383 | Solen confrontation occurrence 1 (unresolved draft) | DELETE | occurrence 2 (umb L1065–1170) is the scene arc3-03 L3–24 continues from |
| L1537–1612 | arc3-03 L364–442 | Phase-one battle occurrence 1 + stray `*The basin erupted.*` (umb L1611) | DELETE | occurrence 2 (umb L1614–1657) + arc3-04 roster |
| L1660–1663 | arc3-03 L491–494 | Recap layer X | DELETE | contradicts arc3-04 L55/L100 |
| L1667–1699 | arc3-03 L497–532 | Recap layer Y ("Four champions stood") | DELETE | contradicts arc3-04 L55/L100 |
| L1703–1720 | arc3-03 L535–550 | Recap layer Z ("Eight champions remained") | DELETE | self-contradictory; contradicts arc3-04 L55/L100 |
| L1722–1742 | arc3-03 L553–571 | Recap layer **W** — KEEP | KEEP (canon recap) | matches arc3-04 L55/L100/L117/L144 exactly |
| L1910 | arc3-04 L151 | `DESER`, `PYRANEI` typos | FIX | — |
| L2278–2296 | arc3-04 L519–537 | Mounted phase version A (Rask as rider) | DELETE | arc3-05 L4/L48/L57 riders are Thane/Sylva/Torin |
| L2298–2321 | arc3-04 L539–562 | Mounted phase version B — KEEP | KEEP | same |
| L2440 | arc3-05 L70 | `definetly`, lowercase `styx` | FIX | — |
| L2500 | arc3-05 L130 | `PYRANEI`, `gauge` (→gouge), garbled "THEN I SHALL IS IT DONE" | FIX | — |
| L2570–2620 | arc3-05 L200–250 | `**Logic**` craft-notes block (14 paragraphs), incl. duplicated green-fire paragraph (umb L2610–2614) | DELETE | author planning voice; future-tense; no narrative content |
| L1945 | arc3-04 L186 | `Let's follow the arena…` planning transition | DELETE | author-voice imperative |
| L2666 | arc3-05 L296 | `dual blade` | FIX | — |
| L2695 | arc3-05 L325 | `Faint` → Feint | FIX | — |
| L2721 | arc3-05 L351 | `loose` → lose, `millenia` → millennia | FIX | — |
| L2771 | arc3-05 L401 | Compressed feint/concession draft | DELETE | canon at umb L2792 + L2797 (arc3-05 L422 + L427), which arc3-05 L431+ continues |
| L796 | arc3-02 L273 | `FRIEND'S` | FIX | — |
| L1087 | arc3-02 L564 | `wenfari`, lowercase `solen` | FIX | — |
| L1209 | arc3-03 L40 | `fhe`, `STEMMED` | FIX | — |
| L1259 | arc3-03 L90 | `RISED` | FIX | — |
| L1315 | arc3-03 L146 | `ESPECTACULAR` | FIX | — |

Notes:
- The umbrella also carries the typo anchors for arc3-01 (umb L44/L139 `wengari`, L77 `t'vat`/`striped paws`, L115 `therye`, L207 `stripe paws`, L157 `hummans`, L175×2/L193 `humans`).
- Umbrella-only scan hits verified as false positives: L1852 (`TAKE A REST` dialogue) and L1166/L2536-style `Let me` matches inside Ajani dialogue — all legitimate in-story speech, not author voice.
- Umbrella `**Logic**` block (L2570–2620) and arc3-05 L200–250 are line-for-line identical (verified L2568–2625); the green-fire paragraph duplication exists in both (umb L2610/2613 ↔ split L240/243).

---

## 5. Duplicate blocks with canon designation

Every group below was cross-referenced against downstream chapters; "canon" means the version the continuing story requires.

### 5.1 Torek's farewell — two takes (arc3-01 L320–326 vs L330–332; umb L319–325 vs L329–331)

- **Version A:** "I have served four kings. Your father. His father before him. Uthgard VII, who was strict but just. And now you…" followed by a scene-closing beat ("The elders filed out of the chamber… The negotiations were complete. The pact was renewed.").
- **Version B:** "I served your father… and his father before him—Uthgard VIII, strict but just. My own father served the king before that… Four generations of my family have watched the Brightmane throne."
- Both are canon-consistent with the Uthgard numbering (A: VII/VIII/IX/Ajani served personally; B: VIII grandfather, IX father, VII via Torek's father). The draft never deleted the superseded take.
- **Designation: JUDGMENT for Ainz-sama** (§6.3) — recommendation: keep **version B** (it leads directly into the continuing scene "The chamber had emptied…" at arc3-01 L356, and the four-generations beat echoes Torek's "three generations" line at arc3-03 L9 without contradicting it); delete version A + its premature closing beat.

### 5.2 Fire Feet lore block (arc3-01 L334–352; umb L333–352)

- Bestiary-format dump with scaffold heading `**The Fire Feet — Lore Confirmed**` and author planning prose. Not narrative.
- **Designation: DELETE from chapter.** If the lore is wanted in canon, it belongs in the bestiary doc (outside this audit's write scope) — flag for Demiurge.

### 5.3 Solen confrontation — occurrence 1 vs occurrence 2 (arc3-02 L360–383 vs L539–646; umb L883–906 vs L1065–1170)

- Occurrence 1 opens the confrontation before the interlude scenes and stops without resolution (L383 bridges to the interludes). Occurrence 2 is the full scene: objection → Ajani's green-fire response → Solen's collapse → the elders' bow → the apology arc that arc3-03 L3–24 continues verbatim ("Solen stumbled backward… 'I—my king—I did not—'").
- **Designation: canon = occurrence 2.** DELETE arc3-02 L360–383. Salvage candidate (unique content): the young elder's "Without even eating breakfast" joke (L374) — editorial option.

### 5.4 arc3-03 phase one — duplicated battle + three contradictory recap layers

- **Battle occurrence 1 (arc3-03 L364–442):** Rask falls to poison; Motted Paws concede the phase. **Superseded.**
- **Battle occurrence 2 (arc3-03 L445–488):** Tor rakes Thane's shoulder then is poisoned; Varn poisoned by Sera; Sylva drops Vex; Rask knocks Thane unconscious; Sera poisons Rask from behind; "Two champions remained standing: Sylva… and Sera" (L485). **Canon** — every injury matches arc3-04 (Thane "regained consciousness after Rask's blow" L58, "shoulder still bound where Tor had raked him" L128; Sera's ruined face; Rask shaking off poison L70).
- **Layer X (L491–494):** "Six champions would advance. Two Shadow Paws. Two Motted Paws. Two Stripe Paws." — wrong roster (canon: one Stripe Paw).
- **Layer Y (L497–532):** "Four champions stood…" — wrong roster (drops Thane and Rask).
- **Layer Z (L535–550):** "Eight champions remained… The Stripe Paws had lost no one… Rask had fallen…" — internally contradictory.
- **Layer W (L553–571):** "Six champions remained: three Motted Paws, two Shadow Paws, one Stripe Paw." **Canon** — matches arc3-04 L55 ("The six champions who had survived the first phase") and L100's explicit roster ("Thane and Sera of the Shadow Paws, Rask of the Stripe Paws, Sylva and her two companions of the Motted Paws").
- **Designation: KEEP occurrence 2 + layer W; DELETE occurrence 1 (L364–442) + layers X, Y, Z (L491–550).** Housekeeping after deletion: thought L362 belongs before the kept battle (relocate + normalize delimiters); the "incense stick crumbled into ash" closer survives at both L488 and L553 — cut one (editorial, recommend cutting L488's duplicate beat is unnecessary — keep L553 only if L488 reads redundant; see §6.3); L439's "good regents" thought may be salvaged after L485 (editorial option).

### 5.5 Mounted-phase opening — version A vs B (arc3-04 L519–537 vs L539–562; umb L2278–2296 vs L2298–2321)

- Version A mounts Thane, **Rask**, Sylva. Version B mounts Thane, Sylva, **Torin** and states "The Stripe Paws were gone, eliminated in the second phase."
- **Designation: canon = version B** — arc3-05's mounted phase features Torin as a rider (L4 "Torin's fire foot shouldered Thane's mount", L48, L57) and Rask signing autographs at the festival (L172). DELETE arc3-04 L519–537.
- Continuity note (editorial, not blocking): the Rask-vs-Torin second-phase duel that version B references ("who had defeated Rask with a single precise strike") is not shown on-page anywhere in arc3-04; Ainz-sama may want a sentence bridging this.

### 5.6 Green-fire craft paragraph duplication (arc3-05 L240 = L243; umb L2610 = L2613)

- Verbatim duplicate inside the `**Logic**` block. **Disappears with the block deletion** (§4).

### 5.7 Sylva's concession — compressed draft vs canon (arc3-05 L401 vs L422 + L427; umb L2771 vs L2792 + L2797)

- L401 crams the feint acknowledgment, the yield, and the regency line into one speech — an early draft.
- **Designation: canon = L422** ("The feint… You learned something after all. The ji was the distraction. The saber was the truth. Well played.") **+ L427** ("I yield. The crown is yours. The regency is mine. And the desert has witnessed."), from which arc3-05 L431 onward continues. DELETE arc3-05 L401.

### 5.8 Minor repetitions (editorial review, not deletions)

- "The king was a fan of the fire feet" + Ember-gift beat twice in Zara's POV (arc3-05 L18 and L82) — keep one (see §6.3).
- "The Styx circled above, their fires painting the twilight in shifting shades of flame" ×5 in arc3-05 (e.g., L319, L345) — deliberate refrain, acceptable but on the heavy side.
- "he had served three generations of Bright Paw kings" ×3 (arc3-02 L45, L616; arc3-03 L9) — deliberate refrain, acceptable.
- arc3-05 L319 vs L345 — near-duplicate "heir of the Lightbringer" paragraph pair; intentional escalation, keep.

---

## 6. Remediation classification

### 6.1 Mechanical (scriptable, closed replacement maps — apply to umbrella AND splits)

| Map | Hits | Lines |
|---|---|---|
| Contractions: `CANT`→`CAN'T`, `LETS`→`LET'S`, `ILL`→`I'LL`, `dont`→`don't`, `havent`→`haven't`, `im`→`I'm`, `cant`→`can't`, `shes`→`she's`, `lets`→`let's`, `wont`→`won't`, `youre`→`you're`, `ITS`→`IT'S` (L146 only) | 23 | arc3-02 L273; arc3-03 L90, L146; arc3-04 L151, L515; arc3-05 L130, L267, L296, L325, L351, L490 |
| Standalone `i`→`I` | 13 | arc3-04 L515; arc3-05 L70, L130, L325, L351 |
| Humman: `humans`→`Hummans` (L176×2, L194), `hummans`→`Hummans` (L158) | 4 | arc3-01 |
| Delimiter normalization (asterisk thoughts → single quotes; fix crossed `*…'`/`'…*`; close L310–312 to one paragraph) | 13 blocks | arc3-02 L533; arc3-03 L230, L310–312, L338, L362, L393, L439; arc3-05 L267, L296, L325, L351, L472 |
| Typos (unique corrections): `therye`→`they're`; `t'vat`→`T'vat`; `striped paws`→`Stripe Paws`; `stripe paws`→`Stripe Paws`; `wengari`→`Wengari`; `said`→`say` (L219); `FRIEND'S`→`FRIENDS`; `solen`→`Solen`; `wenfari`→`Wengari`; `fhe`→`the`; `STEMMED`→`ESTEEMED`; `RISED`→`RISEN`; `ESPECTACULAR`→`SPECTACULAR`; `DESER`→`DESERT`; `PYRANEI`→`PYRINAE` (×2); `definetly`→`definitely`; `styx`→`Styx`; `gauge`→`gouge`; `dual blade`→`dual blades`; `Faint`→`Feint`; `loose`→`lose`; `millenia`→`millennia`; `Infurating`→`Infuriating`; `heir of the light`→`heir of the Light` | 24 | arc3-01 L45, L78, L116, L140, L208; arc3-02 L219, L273, L564; arc3-03 L40, L90, L146; arc3-04 L151; arc3-05 L70, L130, L296, L325, L351, L472 |

Total mechanical: **~64 closed replacements**, all unambiguous, all present identically in umbrella and splits.

### 6.2 Editorial (judgment deletions/rewords — executable without Ainz-sama once §5 designations are accepted)

| Action | Target |
|---|---|
| DELETE confrontation occurrence 1 | arc3-02 L360–383 (umb L883–906) |
| Trim "(Closing Scene)" from subheading | arc3-02 L539 |
| DELETE battle occurrence 1 + stray fragment | arc3-03 L364–442 (umb L1537–1612); relocate thought L362 before L445 |
| DELETE recap layers X, Y, Z | arc3-03 L491–550 (umb L1660–1720); keep layer W L553–571 |
| Cut one duplicated incense closer | arc3-03 L488 or L553 (recommend keep L553) |
| DELETE mounted version A | arc3-04 L519–537 (umb L2278–2296) |
| DELETE planning transition | arc3-04 L186 |
| DELETE `**Logic**` craft block | arc3-05 L200–250 (umb L2570–2620) |
| DELETE compressed feint draft | arc3-05 L401 (umb L2771) |
| DELETE lore scaffold block | arc3-01 L334–352 (umb L333–352) — contingent on §6.3 bestiary decision |
| Reword garbled shout | arc3-05 L130 "THEN I SHALL IS IT DONE" → e.g. "THEN IT SHALL BE DONE" |
| Optionally bridge the unseen Rask-vs-Torin duel | arc3-04 second phase (editorial add, one sentence) |

### 6.3 Judgment (needs Ainz-sama's decision)

| # | Item | Options | Recommendation |
|---|---|---|---|
| J1 | Torek take A vs B (arc3-01) | Keep A ("four kings I served"); keep B ("four generations of my family") | **B** — flows into the continuing scene; Uthgard VIII grandfather canon-consistent |
| J2 | Fire Feet lore content | Delete outright; relocate bullets to bestiary doc first | Relocate-then-delete (preserve worldbuilding) |
| J3 | arc3-05 Zara refrain (L18 vs L82 "fan of the fire feet"/Ember) | Keep both; cut one | Cut L82's second planning beat, keep L18 |
| J4 | Salvage from deleted drafts: "breakfast" joke (arc3-02 L374); "good regents" thought (arc3-03 L439) | Keep in canon scene; drop | Fold joke into occurrence 2's Vasha beat; keep thought after L485 |

---

## 7. Status

- [x] Skeleton written
- [x] Lint battery adapted to `QA/arc3_tooling/` and run against all 5 arc3 splits
- [x] Umbrella debris scan complete (grep + targeted reads only)
- [x] Spot-verification of script output complete (all cited lines read directly)
- [x] Duplicate-block canon designations cross-referenced against downstream chapters
- [x] Report sections filled

**FINAL** — Arc III audit complete. Findings: ~64 mechanical fixes (scriptable), 12 editorial deletions/trims with canon designated, 4 judgment items for Ainz-sama. Story content untouched (read-only honored); all tooling in `QA/arc3_tooling/`; umbrella master remains the source of truth for remediation.
