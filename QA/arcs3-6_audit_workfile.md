# Ethra Arcs III–VI — Consolidated Audit Workfile

**Compiled by:** Demiurge (Overseer, quality gate)
**Date:** 2026-08-24
**Directive:** Ainz-sama — tandem audit of the remaining arcs, one report per arc under a single shared workfile, quality-gated, with remediation plan and mitigation steps.
**Execution:** 4 parallel audit subagents (one per arc) + Mare (Chronicler — lore checklist, umbrella status, canon adjudication) + Demiurge (oversight, monitoring, quality gate, merge).

## Contents

- Part 0 — Oversight summary & quality gate (this section)
- Part I — Arc III audit report (FINAL, verbatim)
- Part II — Arc IV audit report (FINAL, verbatim)
- Part III — Arc V audit report (FINAL, verbatim)
- Part IV — Arc VI audit report (FINAL, verbatim)
- Part V — Mare's lore continuity checklist (verbatim, includes umbrella-status rulings and adjudications)
- Part VI — Remediation plan & mitigation steps (Demiurge)

---

# PART 0 — OVERSIGHT SUMMARY & QUALITY GATE

## 0.1 Corpus state at audit time

| Arc | Title | Chapters | Umbrella | Umbrella state (Mare §1) |
|---|---|---|---|---|
| III | The Tournament | 5 (arc3-01..05) | chapter-03.md, 277 KB | never cleaned |
| IV | The Consolidation | 6 (arc4-01..06) | chapter-04.md, 481 KB | final of meta/draft-stack pass chain (2026-06-20); NOT line-polished |
| V | The Great War | 22 (arc5-01..22) | chapter-05.md, 293 KB | never cleaned |
| VI | Aftermath & The Road | 5 (arc6-01..05) | chapter-06.md, 496 KB | MID-PASS: pass-1 ran 2026-08-23 (ch1 dedupe + ch4 planning-bleed excision) |

Integrity: SHA-256 baseline of all 38 split files + 4 umbrellas taken before audit (`demiurge workspace: chapter_hashes_arcs3-6_baseline_2026-08-24.txt`); verified unchanged throughout (final re-verification appended to this part).

## 0.2 Verdicts at a glance

| Arc | Mechanics | Structure | Publishable? |
|---|---|---|---|
| III | CONDITIONAL PASS (~66 mechanical fixes) | 10 duplicate/draft groups, 4 meta sites | NO — debris-blocked |
| IV | moderate (~105 mechanical fixes; 1 unbalanced quote) | WORST: ~650 debris lines (~18% of arc), 2 scaffold docs, 9 duplicated scene complexes incl. one triple-take | NO |
| V | cleanest arc audited (0 contractions/quotes/delimiter defects; 8 delimiter-canon fixes) | severe draft hygiene: 9 meta blocks + 8 duplicate groups | NO — debris-blocked |
| VI | polished prose near-clean (1 missing quote; ~52 Humman spelling; 4 king-title caps) | dirtiest debris class: ~350–400 non-story lines, 6 duplicated scene versions | NO |

Root cause common to all four arcs: superseded takes and author-voice planning text were never excised before publication (Arc IV's cleaning chain covered only previously-known marker classes). Arc I–II's reader-discovered defects are present at scale here — the proactive audit found them before readers did.

## 0.3 Quality-gate method

Each report was read in full by Demiurge; load-bearing claims were re-verified against the files themselves (independent greps/line reads) and against the subagents' own tool artifacts (lint JSONs, tallies, scans). Mare's checklist was cross-applied as the lore authority. Results:

**Passed at gate (independently re-verified):**
- Arc III: hum census (Humman 34/Hummans 33/humans 3/hummans 1), king census (29/251), 421 em dashes — all identical to tool artifacts; recap-layer canon designations (W kept; X/Y/Z deleted) cross-checked against arc3-04 roster L55/L100.
- Arc IV: king 41/360 and em 559 split≡umbrella; missing closing quote arc4-01 L394 (odd file count); scaffold doc L418 "Here is a comprehensive summary..." verbatim; "Let me rewrite" ×4 exact; Humman 99-vs-98 split/umbrella delta correctly explained (generated heading "The Humman Delegation").
- Arc V: AI-instruction line arc5-11 L157, craft essay arc5-07 L59–73, stage direction arc5-22 L3–5, king deviation arc5-01 L359, HUMANS arc5-06 L190 — all five spot-checks verbatim; boundary/round-trip claims accepted (byte-identity proven by subagent tooling).
- Arc VI: missing opening quote arc6-01 L641 (file quote total odd), `king of the humans` arc6-02 L714, Tamsin V2 canon proven by 6 "Golden Claw" references (incl. L665/L675 inside V2), pass-1 residual state (0 explicit markers) — all verified.
- Arc V cross-observation confirmed: arc4-06 `*Perhaps it will work...*` verbatim self-duplicate L27–29 ≡ L71–73 (captured by Arc IV report as take-A debris + take-B asterisk-thought fix).

**Gate corrections (binding — remediation plan Part VI incorporates these):**
- **G1 (Arc III):** umbrella L1852 ≡ arc3-04 L93 — the report dismissed this line as a false positive ("TAKE A REST dialogue"). The dismissal is right that it is genuine in-story speech (a royal proclamation, not scaffold), but WRONG that it is clean: `"SO ITS SPOKEN..."` needs `ITS→IT'S`, and `BRIGHTPAWS` needs `BRIGHT PAWS`. Add to Arc III mechanical map (+2 fixes; also review the same line's comma usage).
- **G2 (Arc III):** typo map said `t'vat→T'vat`. Overruled — Mare §2 adjudicates (resolves Arc I–II pending decision D4): **T'vat is a misspelling of T'van** (raw-conversation census 135 T'van : 3 T'vat; attendant is one canon character). Fix arc3-01 L78 to `T'van` (with capitalization and `striped paws→Stripe Paws`).
- **G3 (Arc IV):** report said "T'vat the attendant reference — canon per Arc I–II D4; no action". Overruled per Mare §2: fix arc4-02 L240 and L288 `T'vat→T'van` (+2 mechanical fixes).
- **G4 (Arc VI):** two residual debris markers missed by the subagent, found by Mare's fresh scan (§8.1, §8.2): (a) umbrella L527 ≡ arc6-01 L528 "We switch to the night at the throne room..." planning line in speech-line wrapper; (b) umbrella L438 ≡ arc6-01 L439 asterisk scene-direction block ("*The next scene is a couple of hours after...*"). Both DELETE (scene facts inside are canon and paid off elsewhere). Mare §8.3 was already captured by the Arc VI report (Kyre-Tree V1/V2 + "*I like it, let's write it*" marker).
- **G5 (cross-arc):** `Mottled→Motted` drift, 8 hits (arc3-02, arc3-05, arc4-03, arc5-11, arc6-01 ×2, arc6-02 ×2) — not flagged by any subagent. Mare §6 recommended standardizing story text on **Motted Paws** (corpus 296:8); **Demiurge ratifies**. Add 8 mechanical fixes; bestiary-table/world.md/image-filename alignment is a separate docs task (flag only, do not edit docs in this pass).
- **G6 (Arc V, informational):** arc5-06 L190 "HE HAS—HE HAS VELARIUS MADNESS!" — dramatic stutter, likely intentional; classified editorial-awareness, not a defect.
- **G7 (Arc IV, informational):** Sylvia census = 1 chapter-corpus hit (arc4-02 L240), already in Arc IV map; raw-conversation total 3 — the other 2 are outside chapter corpus; no extra action.

**Lore adjudications adopted into the remediation baseline (Mare checklist):**
- T'van spelling (above); L'vat is unrelated (Lament) — never conflate.
- Four/five-families rule: both counts canon in their contexts (Mare §6) — battery must not normalize.
- Sylva vs Sylvia vs Sylara: Sylva canon; Sylvia drift; Sylara is a different character — any Sylva↔Sylara substitution is a critical lore error.
- Styx (species) never merged with Styxian (capital/adjective).
- "Bright Mane" (arc5-02 L29, arc5-05 L19) — unresolved, judgment J-V3 for Ainz-sama (default: Brightmane).
- "veylara" (arc4-02 L552/L566) — probably Veylar, judgment J-IV5 for Ainz-sama.

## 0.4 Consolidated decision list for Ainz-sama

Mechanical remediation (~330 closed fixes + ~1,400 debris lines) is fully specified and needs no decisions. The following require rulings:

**Cross-arc:**
- **X1 — Thought/telepathy presentation canon** (consolidates Arc IV J1, Arc V J2, Arc VI J3a): single quotes everywhere for thoughts; decide status of (a) arc4-03 entity asterisk blocks (22 balanced blocks — stylized telepathy), (b) `thought-block` + `*…*` pattern (arc4-06 ×5, arc5-21 ×1), (c) non-Ajani asterisk thoughts (arc6-04 Nikolai, arc6-02 shared thought), (d) underscore thoughts (arc5-11 ×2). Recommendation: enforce single quotes for all character thoughts; if telepathy gets an exception, define it explicitly (Tree telepathy `*...*` is already established canon and would be exempted).
- **X2 — Craft-block archiving** (Arc VI J3b, applies to all arcs): the craft-feedback/planning blocks are genuine editorial analysis. Delete outright, or export to `QA/archive/` first? Recommendation: export-then-delete (one-time script, trivial).
- **X3 — Inherited from Arc I–II, still open:** D1 em-dash style ratification (all four new arcs are em-dash-compliant under the canon reading; decision only needed to change the canon); D3 adjectival "human"; D5 lowercase "hummans" in thought-voice.

**Arc III:** J-III1 Torek farewell take (rec: B) · J-III2 Fire Feet lore bullets: relocate to bestiary doc vs delete (rec: relocate-then-delete) · J-III3 Zara refrain cut (rec: cut L82 beat) · J-III4 salvage "breakfast" joke + "good regents" thought (rec: salvage both).

**Arc IV:** J-IV2 communion negotiation layering (premature acceptance L253–271 vs final L387–389; needs read-through ordering) · J-IV3 bold scene headings arc4-02 (rec: delete per Arc I–III precedent) · J-IV4 grimoire take-A coda salvage · J-IV5 `veylara`→Veylar? · J-IV6 recover truncated planning tweak from `.repass3` artifacts before deletion (optional) · J-IV7 "hell Fit right in" reconstruction.

**Arc V:** J-V1 Council scene take/merge (rec: B spine + A's member introductions) · J-V4 civilian-army speech (rec: take B, Tamsin delegation) · J-V3 "Bright Mane" intended term (rec: Brightmane if royal-house reference).

**Arc VI:** J-VI1 Maren-report contradiction (rec: keep V1, splice Nikolai's "no names to add" speech) · J-VI2 dinner-V1 unique beats (Nadya/Vanya) salvage or drop.

## 0.5 Process record

- Subagent resilience protocol (skeleton-first writes) worked as designed: all four reports survived long composition phases; zero stalls requiring takeover; all four finished within their 1-hour budgets (started 23:46, reports complete 00:23–00:37).
- Mare's interruption-resilience (skeleton-first, daily memory notes) also held.
- No worker required correction-by-restart; the only corrections were content-level gate corrections G1–G7 above.
- READ-ONLY discipline: story content unmodified during the entire audit (final hash verification below).

## 0.6 Final integrity verification

(Recomputed after all audit work concluded; baseline file: `demiurge workspace: chapter_hashes_arcs3-6_baseline_2026-08-24.txt`.)

**Result: 42/42 files unchanged (38 splits + 4 umbrellas), 0 changed.** The entire tandem audit was read-only against story content; all writes went to `QA/` artifacts only.



---

# PART I - ARC III AUDIT REPORT (verbatim)

# Ethra QA Report â€” Arc III ("The Tournament") Proactive Audit

- **Prepared by:** Demiurge's audit subagent â€” script-first audit using the defect battery established in the Arc Iâ€“II reader-feedback audit (`QA/arc1_arc2_reader_feedback_report.md`).
- **Date:** 2026-08-24
- **Scope (READ-ONLY):** published splits `content/story/chapters/chapter-arc3-01..05.md` + umbrella master `content/story/chapter-03.md` (276.7 KB, 2,893 lines; scanned via grep + targeted line reads only).
- **Tooling:** `QA/arc3_tooling/` â€” adapted copies of the Arc Iâ€“II battery (FILES re-targeted to arc3; originals untouched): `arc3_lint.py`, `arc3_lint_pass2.py`, `arc3_em_census.py`, `arc3_em_classify.py`, `arc3_quote_pair_check.py`, `arc3_delimiter_cross_check.py`, `arc3_final_tally.py`, `arc3_umbrella_scan.py`, `arc3_typo_probe.py`, `arc3_dialogue_probe.py`, `arc3_dash_edge_probe.py`. Raw outputs retained in the same folder.
- **Mode:** PROACTIVE â€” no reader feedback exists for Arc III.
- **Line numbers:** split line numbers refer to the published chapter files; umbrella line numbers to `chapter-03.md`. All cited lines were spot-verified by direct read.

---

## 1. Executive Summary

### 1.1 Defect counts per class (published splits)

| # | Defect class | Count | Verdict |
|---|---|---|---|
| 1 | Contractions missing apostrophe | **23 hits / 11 lines** | MECHANICAL |
| 2 | Standalone lowercase "i" | **13 hits / 5 lines** | MECHANICAL |
| 3 | Dialogue delimiter defects (asterisk thoughts / crossed `*â€¦'`) | **13 blocks; 8 crossed or double-marked** | MECHANICAL (normalize) |
| 4 | Em-dash canon | **421 em dashes, 0 unclosed / 0 off-canon** | PASS |
| 5 | Race-name deviations (`humans`, `hummans`) | **4 hits, all in arc3-01** | MECHANICAL |
| 6 | king/King rule | **0 violations** (29 "King Ajani", 251 generic lowercase) | PASS |
| 7 | Meta/scaffold contamination | **4 sites** (incl. 2 large blocks) | EDITORIAL delete |
| 8 | Duplicate draft blocks | **10 groups** (3 chapter-scale) | EDITORIAL delete (canon designated, Â§5) |
| 9 | Typos / garbled words | **24 distinct fixes** | MECHANICAL / EDITORIAL |
| 10 | Lowercase proper nouns | **7 hits** (subset of #9) | MECHANICAL |
| 11 | Quote balance (double quotes) | **0 anomalies** â€” balanced in every chapter | PASS |

Split-vs-umbrella consistency verified: Humman census, king/King census, and em-dash totals are identical between umbrella and splits (Humman 34 / Hummans 33 / humans 3 / hummans 1; King 29 / king 251; em dashes 421) â€” no drift between master and published files.

### 1.2 Arc health verdict

**CONDITIONAL PASS â€” publish-blocked by draft debris, not by mechanics.**

Arc III inherits the Arc Iâ€“II mechanical cleanup: dialogue quotes are perfectly balanced, king/King is fully canon, em dashes are fully canon (no unclosed dashes, no ASCII-hyphen openers), and Humman spelling is canon in four of five chapters. The remaining mechanical layer is small and fully scriptable (~60 closed replacements).

However, Arc III is the first arc with **large-scale structural debris in published chapters**: a triple-drafted phase-one aftermath in arc3-03 (three mutually contradictory recap layers plus a duplicated battle sequence), a misplaced pre-interlude draft of the Solen confrontation in arc3-02, a duplicated mounted-phase opening in arc3-04, a ~50-line author craft-notes block (`**Logic**`) in arc3-05, a bestiary-style lore dump with a "Lore Confirmed" scaffold heading in arc3-01, and a compressed duplicate of Sylva's concession in arc3-05. All duplicate blocks have been cross-referenced against downstream chapters (arc3-03 â†’ arc3-04 â†’ arc3-05 continuity) and canon versions are designated in Â§5; every deletion is determinable without Ainz-sama's input except three flagged JUDGMENT items (Â§6.3).

---

## 2. Per-chapter defect catalog

### 2.1 chapter-arc3-01.md (524 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L45 | lowercase `wengari` ("welcome to the wengari brothers!") | MECH |
| L78 | `"t'vat call for the elder council of the striped paws, now please "` â€” lowercase T'vat, lowercase Stripe Paws, trailing space inside quote | MECH |
| L116 | `'therye here, good...'` â†’ they're | MECH |
| L140 | lowercase `wengari` ("who rules the wengari?") | MECH |
| L158 | `hummans` (lowercase, double-m) â€” race-name case deviation | MECH |
| L176 | `the humans` Ã—2 (single-m) â€” race-name deviation | MECH |
| L194 | `the humans` (single-m) â€” race-name deviation | MECH |
| L208 | lowercase `stripe paws` ("the stripe paws will become what they were meâ€¦") | MECH |
| L318â€“326 | Torek farewell **version A** ("I have served four kingsâ€¦ Uthgard VIIâ€¦") + premature scene-closing beat ("The elders filed out of the chamberâ€¦ The negotiations were complete") â€” duplicate take of L330 | EDIT/JUDG (Â§5.1) |
| L330â€“332 | Torek farewell **version B** ("I served your fatherâ€¦ Uthgard VIIIâ€¦") â€” second take | EDIT/JUDG (Â§5.1) |
| L334â€“352 | `**The Fire Feet â€” Lore Confirmed**` scaffold heading + 7 bestiary-format bullets (L337â€“349, incl. the arc's only en dash, L341) + author planning prose (L352: "â€¦are now trying to determine *which* caravanâ€¦ Their goal is to offer him a fire feet as a coronation giftâ€”but to do so discreetlyâ€¦") | EDIT delete (Â§4, Â§5.2) |

### 2.2 chapter-arc3-02.md (646 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L219 | `'bow...what did father always said'` â†’ say | MECH |
| L273 | `FRIEND'S!!` â†’ FRIENDS; `CANT` â†’ CAN'T | MECH |
| L360â€“383 | **Solen confrontation occurrence 1** â€” misplaced early draft (opens "The Bright Paw elders did not wait for the chaos to subsideâ€¦", "Have you lost your mind?!", Vasha objection L369, "breakfast" joke L374, ends L383 without resolution) | EDIT delete (Â§5.3) |
| L533 | `*The king has put his crown on the lineâ€¦ What should I do?*` â€” the Quick's thought in asterisks; canon: thoughts in single quotes only | MECH normalize |
| L539 | `*The Bright Paw Elders (Closing Scene)*` â€” scaffold annotation "(Closing Scene)" in scene subheading | EDIT trim |
| L564 | `"tell me solen, who rules the wenfari ?"` â€” lowercase Solen; `wenfari` â†’ Wengari | MECH |

### 2.3 chapter-arc3-03.md (590 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L40 | `'fhe sun is up in the skyâ€¦'` â†’ the; `BROTHERS STEMMED GUESTS` â†’ ESTEEMED | MECH |
| L90 | `RISED TO THE CHALLENGE` â†’ RISEN; `LETS` â†’ LET'S | MECH |
| L146 | `ESPECTACULAR` â†’ SPECTACULAR; `ITS A TOURNAMENT` â†’ IT'S | MECH |
| L230 | Quick's mycelial message in asterisks (`*The White Dawn does not ask for mercyâ€¦*`) | MECH normalize |
| L310â€“312 | Quick's pulse message in asterisks **spanning a blank line** (`*The White Dawn has changed the rules.` â€¦blankâ€¦ `The tournament will be a battleâ€¦*`) | MECH normalize + close |
| L338 | `*Let's begin!*` â€” asterisk thought delimiter | MECH normalize |
| L362 | `*'half of it downâ€¦'*` â€” double-marked thought (asterisk + single quote) | MECH normalize |
| L364â€“442 | **Phase-one battle occurrence 1** (draft: Rask charge L367 â†’ ambush L373 â†’ Rask falls to poison L419 â†’ Motted Paws concede L433) + double-marked thoughts L393/L439 + stray fragment `*The basin erupted.*` L442 | EDIT delete (Â§5.4) |
| L393, L439 | `*'it begins '*`, `*'yes they would make good regentsâ€¦'*` â€” double-marked thoughts (inside occurrence-1 block) | MECH normalize (if salvaged) |
| L442 | `*The basin erupted.*` â€” stray asterisk fragment, verbatim double of L364 | EDIT delete |
| L491â€“494 | **Recap layer X** â€” "The Motted Paws had drawn first blood. The Shadow Paws had lost two of threeâ€¦" + "Six champions would advance. Two Shadow Paws. Two Motted Paws. Two Stripe Paws." â€” contradicts canon roster | EDIT delete (Â§5.4) |
| L497â€“532 | **Recap layer Y** â€” "Two champions remained standingâ€¦" (second occurrence) â†’ "Four champions stood at the end of the first phase" â€” contradicts canon roster | EDIT delete (Â§5.4) |
| L535â€“550 | **Recap layer Z** â€” "Eight champions remainedâ€¦ The Stripe Paws had lost no oneâ€¦ Rask had fallen taking Thane with her" â€” internally contradictory | EDIT delete (Â§5.4) |

### 2.4 chapter-arc3-04.md (611 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L151 | `IN THE DESER` â†’ DESERT; `FRIENDS PYRANEI` â†’ PYRINAE; `ILL DEMONSTRATE` â†’ I'LL | MECH |
| L186 | `Let's follow the arena as the Styx feathers measure the champions. The Pyrinae will handle the ceremonyâ€¦ The six champions will be pairedâ€¦` â€” author planning transition (imperative + future-tense summary of the scene that follows) | EDIT delete (Â§4) |
| L515 | `'oh goody... war mounts!!!, i havent seen one since i was a childâ€¦ i touched one?â€¦ dont look too muchâ€¦'` â€” lowercase i Ã—3, havent, dont | MECH |
| L519â€“537 | **Mounted phase version A** ("The champions mounted. Thaneâ€¦ Raskâ€¦ Sylvaâ€¦" â€” Rask as rider; rules speech L535) â€” superseded draft | EDIT delete (Â§5.5) |

### 2.5 chapter-arc3-05.md (522 lines)

| Line(s) | Defect | Class |
|---|---|---|
| L18 vs L82 | "The king was a fan of the fire feet" + Ember-gift planning beat twice (Zara POV) â€” redundant exposition | EDIT/JUDG (Â§6.3) |
| L70 | `'styx in heaven i blew it!!â€¦'` â€” lowercase Styx, lowercase i Ã—2, `definetly` â†’ definitely | MECH |
| L130 | `THEN I SHALL IS IT DONE` â€” garbled draft sentence; `PYRANEI` â†’ PYRINAE; `'ill gauge their eyes out'` â†’ I'll gouge | MECH/EDIT |
| L200â€“250 | `**Logic**` scaffold heading + 14 author craft-analysis paragraphs (future-tense planning: "This duel will be the tournament's defining memoryâ€¦", "The feint is the resolution. Ajani will winâ€¦"), incl. verbatim-duplicated green-fire paragraph (L240 = L243) | EDIT delete (Â§4, Â§5.6) |
| L267 | `*OH, ok, she has claws... spear then'` â€” crossed `*â€¦'` + cant/im missing apostrophes | MECH |
| L296 | `*What on....ok... calm, breathe, shes unarmedâ€¦ dual blade'` â€” crossed `*â€¦'`; shes/lets/dont/im; `dual blade` â†’ dual blades | MECH |
| L325 | `*This is getting annoying!!!â€¦ catching me?!'` â€” crossed `*â€¦'`; cant/imÃ—3/wont; `Faint` â†’ Feint; lowercase i Ã—3 | MECH |
| L351 | `*OK THIS ENDS NOW, SHE NEEDS TO GO DOWN, NOW'` â€” crossed `*â€¦'`; youre/cant/havent/ill; lowercase i Ã—4; `loose` â†’ lose; `millenia` â†’ millennia; `heir of the light` â†’ heir of the Light | MECH |
| L401 | `"The feint," she said quietlyâ€¦ "I yield. The crown is yoursâ€¦"` â€” compressed early draft of the concession (canon at L422 + L427) | EDIT delete (Â§5.7) |
| L472 | `*what?'` opener + `'Infurating womanâ€¦ statecraft...*` closer â€” crossed delimiters both ends; `Infurating` â†’ Infuriating | MECH |
| L490 | `'im this close to skewering her..'` â€” im â†’ I'm | MECH |

---

## 3. Canon-rule compliance

### 3.1 king/King â€” COMPLIANT (0 violations)

- 29 capitalized `King` in splits â€” **every one** is title+name ("King Ajani"; no "King Uthgard" appears in arc3). Spot-verified all 29 contexts via pass2 census: arc3-01 Ã—15, arc3-02 Ã—4 (L250, L379, L556, L572), arc3-03 Ã—4 (L85, L141, L157, L176), arc3-04 Ã—4 (L78, L124, L288, L327), arc3-05 Ã—2 (L147, L467).
- 251 lowercase `king` â€” all determiner/generic/apposition/direct-address uses ("the king", "my king", "their king", "a Bright Paw king").
- No "the King/a King" generic capitalization; no "My king" capitalization errors; no lowercase-before-name ("king Ajani") hits.
- Umbrella census identical (King 29 / king 251) â€” master and splits in agreement.

### 3.2 Humman/Humans â€” 4 deviations, all in arc3-01

Census (case-sensitive exact forms, splits = umbrella): `Humman` 34, `Hummans` 33, `humans` 3, `hummans` 1.

| Location | Form | Fix |
|---|---|---|
| arc3-01 L158 | `hummans` (lowercase) | `Hummans` |
| arc3-01 L176 | `the humans` Ã—2 | `the Hummans` |
| arc3-01 L194 | `the humans` | `the Hummans` |

All three single-m hits are in Zara's dialogue in the same negotiation scene â€” none are out-of-universe Earth-gloss contexts, so no exception applies. Chapters arc3-02..05 are fully canon.

### 3.3 Dialogue formatting

- **Double quotes:** ASCII `"` throughout (0 curly). Cross-line walk confirms **perfect balance in all 5 chapters** â€” no quote left open across a blank line or at EOF. No lines with odd double-quote count.
- **Single quotes:** all odd-parity lines verified as legitimate possessives/contractions (e.g., `families' champions` L437, `Vein-Dwellers' staffs` L132/L456, plural possessives at L68/L257/L579 of arc3-03) except the 8 crossed/double-marked lines below.
- **Asterisk canon (thoughts in single quotes ONLY):** 13 asterisk-wrapped thought/message blocks â€” all violations:
  - arc3-02 L533 (Quick's thought);
  - arc3-03 L230 (Quick message), L310â€“312 (Quick message spanning a blank line), L338 (`*Let's begin!*`), L362/L393/L439 (double-marked `*'â€¦'*`), L442 (`*The basin erupted.*` stray fragment);
  - arc3-05 L267, L296, L325, L351, L472 â€” five blocks opened with `*` and closed with `'` (crossed) or vice versa.
  - Legitimate asterisk uses confirmed and excluded: bold scene headings (`**â€¦**`), italic scene subheadings (arc3-02 `*The Pyrinae Section*` etc.), emphasis of quoted words (arc3-01 L63 `*The desert is not kind to the weak.*`, arc3-02 L607 `*Warm, unflinching, unforgiving.*`, arc3-05 L248 `*he*`), and the bestiary-style bullets in the arc3-01 scaffold block (deleted per Â§5.2).
- **Contractions missing apostrophe:** 23 hits / 11 lines â€” arc3-02 L273 (`CANT`); arc3-03 L90 (`LETS`), L146 (`ITS`); arc3-04 L151 (`ILL`), L515 (`dont`, `havent`); arc3-05 L130 (`ill`), L267 (`lets`), L296 (`dont`, `im`, `shes`, `lets`), L325 (`cant`, `wont`, `im`Ã—4), L351 (`cant`, `ill`, `youre`, `havent`), L490 (`im`). All in Ajani's rough internal voice or shouted speech; closed replacement map in Â§6.1.
- **Standalone lowercase `i`:** 13 hits / 5 lines â€” arc3-04 L515 (Ã—3); arc3-05 L70 (Ã—2), L130 (Ã—1), L325 (Ã—3), L351 (Ã—4). Same voice cluster as the contractions.

### 3.4 Em dashes â€” COMPLIANT (0 defects)

- Census: **421 em dashes** (arc3-01: 87, arc3-02: 83, arc3-03: 88, arc3-04: 78, arc3-05: 85); umbrella identical (421).
- 57 quote-adjacent dashes (`"â€”` / `â€”"`) = speech cutoffs â€” canon use 1.
- All 207 odd-count dash lines classified: every unpaired dash is either a speech cutoff or a dash introducing an elaboration running to sentence/paragraph end (canon use 3). The classifier's "OPEN-MID" heuristic flags were spot-verified on 8 lines (arc3-01 L30, arc3-02 L81, arc3-03 L200/L448, arc3-04 L186, arc3-05 L154/L240) â€” all legitimate elaborations, same narrative usage ratified in Arc Iâ€“II.
- **0 unclosed dashes:** no line ends in an em dash (no open parenthetical carried to the next line), no doubled/spaced dashes, no ASCII hyphen runs, no hyphen/en-dash dialogue openers.
- En dashes: exactly 1 â€” arc3-01 L341 (`30â€“35 years`), inside the bestiary scaffold block slated for deletion (Â§5.2); disappears with the block.

---

## 4. Umbrella draft-debris inventory (chapter-03.md)

All debris exists in the umbrella **and** in the published splits (verified by cross-line reads); the umbrella line numbers below anchor the source of truth for remediation. Debris-only rows â€” canonical narrative rows are not listed.

| Umbrella lines | Split counterpart | Debris | Disposition | Canon evidence |
|---|---|---|---|---|
| L319â€“325 | arc3-01 L320â€“326 | Torek farewell **version A** + premature closing beat | DELETE (or keep per Â§5.1 judgment) | version B leads directly into the continuing scene at L355 |
| L333â€“352 | arc3-01 L334â€“352 | `**The Fire Feet â€” Lore Confirmed**` scaffold + bestiary bullets + planning prose | DELETE from chapter (see Â§5.2) | scaffold marker; non-narrative format; planning prose is author-voice |
| L883â€“906 | arc3-02 L360â€“383 | Solen confrontation occurrence 1 (unresolved draft) | DELETE | occurrence 2 (umb L1065â€“1170) is the scene arc3-03 L3â€“24 continues from |
| L1537â€“1612 | arc3-03 L364â€“442 | Phase-one battle occurrence 1 + stray `*The basin erupted.*` (umb L1611) | DELETE | occurrence 2 (umb L1614â€“1657) + arc3-04 roster |
| L1660â€“1663 | arc3-03 L491â€“494 | Recap layer X | DELETE | contradicts arc3-04 L55/L100 |
| L1667â€“1699 | arc3-03 L497â€“532 | Recap layer Y ("Four champions stood") | DELETE | contradicts arc3-04 L55/L100 |
| L1703â€“1720 | arc3-03 L535â€“550 | Recap layer Z ("Eight champions remained") | DELETE | self-contradictory; contradicts arc3-04 L55/L100 |
| L1722â€“1742 | arc3-03 L553â€“571 | Recap layer **W** â€” KEEP | KEEP (canon recap) | matches arc3-04 L55/L100/L117/L144 exactly |
| L1910 | arc3-04 L151 | `DESER`, `PYRANEI` typos | FIX | â€” |
| L2278â€“2296 | arc3-04 L519â€“537 | Mounted phase version A (Rask as rider) | DELETE | arc3-05 L4/L48/L57 riders are Thane/Sylva/Torin |
| L2298â€“2321 | arc3-04 L539â€“562 | Mounted phase version B â€” KEEP | KEEP | same |
| L2440 | arc3-05 L70 | `definetly`, lowercase `styx` | FIX | â€” |
| L2500 | arc3-05 L130 | `PYRANEI`, `gauge` (â†’gouge), garbled "THEN I SHALL IS IT DONE" | FIX | â€” |
| L2570â€“2620 | arc3-05 L200â€“250 | `**Logic**` craft-notes block (14 paragraphs), incl. duplicated green-fire paragraph (umb L2610â€“2614) | DELETE | author planning voice; future-tense; no narrative content |
| L1945 | arc3-04 L186 | `Let's follow the arenaâ€¦` planning transition | DELETE | author-voice imperative |
| L2666 | arc3-05 L296 | `dual blade` | FIX | â€” |
| L2695 | arc3-05 L325 | `Faint` â†’ Feint | FIX | â€” |
| L2721 | arc3-05 L351 | `loose` â†’ lose, `millenia` â†’ millennia | FIX | â€” |
| L2771 | arc3-05 L401 | Compressed feint/concession draft | DELETE | canon at umb L2792 + L2797 (arc3-05 L422 + L427), which arc3-05 L431+ continues |
| L796 | arc3-02 L273 | `FRIEND'S` | FIX | â€” |
| L1087 | arc3-02 L564 | `wenfari`, lowercase `solen` | FIX | â€” |
| L1209 | arc3-03 L40 | `fhe`, `STEMMED` | FIX | â€” |
| L1259 | arc3-03 L90 | `RISED` | FIX | â€” |
| L1315 | arc3-03 L146 | `ESPECTACULAR` | FIX | â€” |

Notes:
- The umbrella also carries the typo anchors for arc3-01 (umb L44/L139 `wengari`, L77 `t'vat`/`striped paws`, L115 `therye`, L207 `stripe paws`, L157 `hummans`, L175Ã—2/L193 `humans`).
- Umbrella-only scan hits verified as false positives: L1852 (`TAKE A REST` dialogue) and L1166/L2536-style `Let me` matches inside Ajani dialogue â€” all legitimate in-story speech, not author voice.
- Umbrella `**Logic**` block (L2570â€“2620) and arc3-05 L200â€“250 are line-for-line identical (verified L2568â€“2625); the green-fire paragraph duplication exists in both (umb L2610/2613 â†” split L240/243).

---

## 5. Duplicate blocks with canon designation

Every group below was cross-referenced against downstream chapters; "canon" means the version the continuing story requires.

### 5.1 Torek's farewell â€” two takes (arc3-01 L320â€“326 vs L330â€“332; umb L319â€“325 vs L329â€“331)

- **Version A:** "I have served four kings. Your father. His father before him. Uthgard VII, who was strict but just. And now youâ€¦" followed by a scene-closing beat ("The elders filed out of the chamberâ€¦ The negotiations were complete. The pact was renewed.").
- **Version B:** "I served your fatherâ€¦ and his father before himâ€”Uthgard VIII, strict but just. My own father served the king before thatâ€¦ Four generations of my family have watched the Brightmane throne."
- Both are canon-consistent with the Uthgard numbering (A: VII/VIII/IX/Ajani served personally; B: VIII grandfather, IX father, VII via Torek's father). The draft never deleted the superseded take.
- **Designation: JUDGMENT for Ainz-sama** (Â§6.3) â€” recommendation: keep **version B** (it leads directly into the continuing scene "The chamber had emptiedâ€¦" at arc3-01 L356, and the four-generations beat echoes Torek's "three generations" line at arc3-03 L9 without contradicting it); delete version A + its premature closing beat.

### 5.2 Fire Feet lore block (arc3-01 L334â€“352; umb L333â€“352)

- Bestiary-format dump with scaffold heading `**The Fire Feet â€” Lore Confirmed**` and author planning prose. Not narrative.
- **Designation: DELETE from chapter.** If the lore is wanted in canon, it belongs in the bestiary doc (outside this audit's write scope) â€” flag for Demiurge.

### 5.3 Solen confrontation â€” occurrence 1 vs occurrence 2 (arc3-02 L360â€“383 vs L539â€“646; umb L883â€“906 vs L1065â€“1170)

- Occurrence 1 opens the confrontation before the interlude scenes and stops without resolution (L383 bridges to the interludes). Occurrence 2 is the full scene: objection â†’ Ajani's green-fire response â†’ Solen's collapse â†’ the elders' bow â†’ the apology arc that arc3-03 L3â€“24 continues verbatim ("Solen stumbled backwardâ€¦ 'Iâ€”my kingâ€”I did notâ€”'").
- **Designation: canon = occurrence 2.** DELETE arc3-02 L360â€“383. Salvage candidate (unique content): the young elder's "Without even eating breakfast" joke (L374) â€” editorial option.

### 5.4 arc3-03 phase one â€” duplicated battle + three contradictory recap layers

- **Battle occurrence 1 (arc3-03 L364â€“442):** Rask falls to poison; Motted Paws concede the phase. **Superseded.**
- **Battle occurrence 2 (arc3-03 L445â€“488):** Tor rakes Thane's shoulder then is poisoned; Varn poisoned by Sera; Sylva drops Vex; Rask knocks Thane unconscious; Sera poisons Rask from behind; "Two champions remained standing: Sylvaâ€¦ and Sera" (L485). **Canon** â€” every injury matches arc3-04 (Thane "regained consciousness after Rask's blow" L58, "shoulder still bound where Tor had raked him" L128; Sera's ruined face; Rask shaking off poison L70).
- **Layer X (L491â€“494):** "Six champions would advance. Two Shadow Paws. Two Motted Paws. Two Stripe Paws." â€” wrong roster (canon: one Stripe Paw).
- **Layer Y (L497â€“532):** "Four champions stoodâ€¦" â€” wrong roster (drops Thane and Rask).
- **Layer Z (L535â€“550):** "Eight champions remainedâ€¦ The Stripe Paws had lost no oneâ€¦ Rask had fallenâ€¦" â€” internally contradictory.
- **Layer W (L553â€“571):** "Six champions remained: three Motted Paws, two Shadow Paws, one Stripe Paw." **Canon** â€” matches arc3-04 L55 ("The six champions who had survived the first phase") and L100's explicit roster ("Thane and Sera of the Shadow Paws, Rask of the Stripe Paws, Sylva and her two companions of the Motted Paws").
- **Designation: KEEP occurrence 2 + layer W; DELETE occurrence 1 (L364â€“442) + layers X, Y, Z (L491â€“550).** Housekeeping after deletion: thought L362 belongs before the kept battle (relocate + normalize delimiters); the "incense stick crumbled into ash" closer survives at both L488 and L553 â€” cut one (editorial, recommend cutting L488's duplicate beat is unnecessary â€” keep L553 only if L488 reads redundant; see Â§6.3); L439's "good regents" thought may be salvaged after L485 (editorial option).

### 5.5 Mounted-phase opening â€” version A vs B (arc3-04 L519â€“537 vs L539â€“562; umb L2278â€“2296 vs L2298â€“2321)

- Version A mounts Thane, **Rask**, Sylva. Version B mounts Thane, Sylva, **Torin** and states "The Stripe Paws were gone, eliminated in the second phase."
- **Designation: canon = version B** â€” arc3-05's mounted phase features Torin as a rider (L4 "Torin's fire foot shouldered Thane's mount", L48, L57) and Rask signing autographs at the festival (L172). DELETE arc3-04 L519â€“537.
- Continuity note (editorial, not blocking): the Rask-vs-Torin second-phase duel that version B references ("who had defeated Rask with a single precise strike") is not shown on-page anywhere in arc3-04; Ainz-sama may want a sentence bridging this.

### 5.6 Green-fire craft paragraph duplication (arc3-05 L240 = L243; umb L2610 = L2613)

- Verbatim duplicate inside the `**Logic**` block. **Disappears with the block deletion** (Â§4).

### 5.7 Sylva's concession â€” compressed draft vs canon (arc3-05 L401 vs L422 + L427; umb L2771 vs L2792 + L2797)

- L401 crams the feint acknowledgment, the yield, and the regency line into one speech â€” an early draft.
- **Designation: canon = L422** ("The feintâ€¦ You learned something after all. The ji was the distraction. The saber was the truth. Well played.") **+ L427** ("I yield. The crown is yours. The regency is mine. And the desert has witnessed."), from which arc3-05 L431 onward continues. DELETE arc3-05 L401.

### 5.8 Minor repetitions (editorial review, not deletions)

- "The king was a fan of the fire feet" + Ember-gift beat twice in Zara's POV (arc3-05 L18 and L82) â€” keep one (see Â§6.3).
- "The Styx circled above, their fires painting the twilight in shifting shades of flame" Ã—5 in arc3-05 (e.g., L319, L345) â€” deliberate refrain, acceptable but on the heavy side.
- "he had served three generations of Bright Paw kings" Ã—3 (arc3-02 L45, L616; arc3-03 L9) â€” deliberate refrain, acceptable.
- arc3-05 L319 vs L345 â€” near-duplicate "heir of the Lightbringer" paragraph pair; intentional escalation, keep.

---

## 6. Remediation classification

### 6.1 Mechanical (scriptable, closed replacement maps â€” apply to umbrella AND splits)

| Map | Hits | Lines |
|---|---|---|
| Contractions: `CANT`â†’`CAN'T`, `LETS`â†’`LET'S`, `ILL`â†’`I'LL`, `dont`â†’`don't`, `havent`â†’`haven't`, `im`â†’`I'm`, `cant`â†’`can't`, `shes`â†’`she's`, `lets`â†’`let's`, `wont`â†’`won't`, `youre`â†’`you're`, `ITS`â†’`IT'S` (L146 only) | 23 | arc3-02 L273; arc3-03 L90, L146; arc3-04 L151, L515; arc3-05 L130, L267, L296, L325, L351, L490 |
| Standalone `i`â†’`I` | 13 | arc3-04 L515; arc3-05 L70, L130, L325, L351 |
| Humman: `humans`â†’`Hummans` (L176Ã—2, L194), `hummans`â†’`Hummans` (L158) | 4 | arc3-01 |
| Delimiter normalization (asterisk thoughts â†’ single quotes; fix crossed `*â€¦'`/`'â€¦*`; close L310â€“312 to one paragraph) | 13 blocks | arc3-02 L533; arc3-03 L230, L310â€“312, L338, L362, L393, L439; arc3-05 L267, L296, L325, L351, L472 |
| Typos (unique corrections): `therye`â†’`they're`; `t'vat`â†’`T'vat`; `striped paws`â†’`Stripe Paws`; `stripe paws`â†’`Stripe Paws`; `wengari`â†’`Wengari`; `said`â†’`say` (L219); `FRIEND'S`â†’`FRIENDS`; `solen`â†’`Solen`; `wenfari`â†’`Wengari`; `fhe`â†’`the`; `STEMMED`â†’`ESTEEMED`; `RISED`â†’`RISEN`; `ESPECTACULAR`â†’`SPECTACULAR`; `DESER`â†’`DESERT`; `PYRANEI`â†’`PYRINAE` (Ã—2); `definetly`â†’`definitely`; `styx`â†’`Styx`; `gauge`â†’`gouge`; `dual blade`â†’`dual blades`; `Faint`â†’`Feint`; `loose`â†’`lose`; `millenia`â†’`millennia`; `Infurating`â†’`Infuriating`; `heir of the light`â†’`heir of the Light` | 24 | arc3-01 L45, L78, L116, L140, L208; arc3-02 L219, L273, L564; arc3-03 L40, L90, L146; arc3-04 L151; arc3-05 L70, L130, L296, L325, L351, L472 |

Total mechanical: **~64 closed replacements**, all unambiguous, all present identically in umbrella and splits.

### 6.2 Editorial (judgment deletions/rewords â€” executable without Ainz-sama once Â§5 designations are accepted)

| Action | Target |
|---|---|
| DELETE confrontation occurrence 1 | arc3-02 L360â€“383 (umb L883â€“906) |
| Trim "(Closing Scene)" from subheading | arc3-02 L539 |
| DELETE battle occurrence 1 + stray fragment | arc3-03 L364â€“442 (umb L1537â€“1612); relocate thought L362 before L445 |
| DELETE recap layers X, Y, Z | arc3-03 L491â€“550 (umb L1660â€“1720); keep layer W L553â€“571 |
| Cut one duplicated incense closer | arc3-03 L488 or L553 (recommend keep L553) |
| DELETE mounted version A | arc3-04 L519â€“537 (umb L2278â€“2296) |
| DELETE planning transition | arc3-04 L186 |
| DELETE `**Logic**` craft block | arc3-05 L200â€“250 (umb L2570â€“2620) |
| DELETE compressed feint draft | arc3-05 L401 (umb L2771) |
| DELETE lore scaffold block | arc3-01 L334â€“352 (umb L333â€“352) â€” contingent on Â§6.3 bestiary decision |
| Reword garbled shout | arc3-05 L130 "THEN I SHALL IS IT DONE" â†’ e.g. "THEN IT SHALL BE DONE" |
| Optionally bridge the unseen Rask-vs-Torin duel | arc3-04 second phase (editorial add, one sentence) |

### 6.3 Judgment (needs Ainz-sama's decision)

| # | Item | Options | Recommendation |
|---|---|---|---|
| J1 | Torek take A vs B (arc3-01) | Keep A ("four kings I served"); keep B ("four generations of my family") | **B** â€” flows into the continuing scene; Uthgard VIII grandfather canon-consistent |
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

**FINAL** â€” Arc III audit complete. Findings: ~64 mechanical fixes (scriptable), 12 editorial deletions/trims with canon designated, 4 judgment items for Ainz-sama. Story content untouched (read-only honored); all tooling in `QA/arc3_tooling/`; umbrella master remains the source of truth for remediation.



---

# PART II - ARC IV AUDIT REPORT (verbatim)

# Ethra QA Report â€” Arc IV "The Consolidation" â€” Proactive Audit

- **Prepared by:** Demiurge's audit subagent (Tri-Guardian QA), defect battery inherited from the Arc Iâ€“II reader-feedback audit (`QA/arc1_arc2_reader_feedback_report.md`).
- **Date:** 2026-08-24
- **Audit mode:** PROACTIVE â€” no reader feedback exists for Arc IV; the Arc Iâ€“II defect battery is applied wholesale.
- **Scope (READ-ONLY throughout):**
  - Published splits (primary audit targets): `content/story/chapters/chapter-arc4-01.md â€¦ chapter-arc4-06.md` (6 files; 564 / 597 / 545 / 612 / 678 / 676 lines; 3,672 lines total)
  - Umbrella master (source of truth for future fixes): `content/story/chapter-04.md` (481,075 bytes; 3,668 lines)
- **Editorial-history artifacts (listed for provenance; NOT audited â€” audit covers current `chapter-04.md` only):**
  - `chapter-04.md.alpha_excise` (492,264 B, 2026-06-20)
  - `chapter-04.md.repass3` (503,185 B, 2026-06-19)
  - `chapter-04.md.stripped_meta` (532,079 B, 2026-06-18)
  - `chapter-04.md.stripped_passes` (509,459 B, 2026-06-18)
  - `chapter-04.md_pass3_only.md` (57,447 B, 2026-06-19)
  - *Naming implies a multi-pass editorial pipeline (meta-stripping â†’ pass re-runs â†’ alpha excision) was already applied to the umbrella before publication. Its coverage was evidently scoped to previously-known marker classes: every debris class cataloged below survives in the current umbrella. Audit covers current `chapter-04.md` only.*
- **Tooling:** `QA/arc4_tooling/` â€” adapted copies of the Arc Iâ€“II battery (lint_arc4.py, lint_pass2_arc4.py, em_census_arc4.py, em_classify_arc4.py, quote_pair_check_arc4.py, delimiter_cross_check_arc4.py, final_tally_arc4.py) plus new arc4 scripts (umbrella_debris_scan.py, meta_scan_splits_arc4.py, umbrella_locate.py/.2, umbrella_headings.py, humman_diff.py, crossref_letter.py, thought_blocks.py, peek.py/peek2.py, em_tally.py) and their output artifacts. Originals in `QA/` untouched.
- **Architecture notes (verified in `arcs.json` + file inspection):**
  - Arc IV has no `split_anchors`; `regenerate_chapters.py` splits `chapter-04.md` by even-word heuristic. All fixes must land in the umbrella, then regenerate. Split line numbers below are audit references; each debris item also carries its umbrella line number(s), located by exact text search.
  - The generator strips markdown headings from umbrella content and inserts `## Chapter N: <sub-title>` (from `arcs.json`) as line 1 of each split (verified: arc4-01 L1 "## Chapter 1: Bureaucracy" â€¦ arc4-06 L1 "## Chapter 6: Aftermath"). These generated headings are pipeline output, not content defects. The extra "Humman" in splits (99) vs umbrella (98) is the arc4-04 generated heading "The Humman Delegation" â€” resolved, not a deviation.
  - The umbrella's stale internal heading `## Chapter 5: The Gifts` (umbrella L2572) is stripped by the generator and does not reach published output, but it is umbrella debris (stale numbering, see Â§4).
- **Status:** see Â§7.

---

## 1. Executive Summary

**Arc health verdict: NOT PUBLISHABLE AS-IS â€” worst structural condition of any arc audited to date.** The prose mechanics of Arc IV are comparable to pre-fix Arc Iâ€“II (moderate contraction/capitalization drift, one unbalanced quote, a handful of crossed delimiters). But the published arc carries **â‰ˆ650 lines of draft debris â€” roughly 18% of the published text**: two complete worldbuilding/craft scaffold documents, thirteen author markers/self-prompts, and **nine duplicated scene complexes** (including one scene present in THREE takes). Arc Iâ€“II debris of this kind was isolated and reader-discovered; in Arc IV it ships wholesale in all six chapters.

**Counts per defect class**

| Class | Count | Notes |
|---|---|---|
| EDITORIAL â€” meta/scaffold deletions | ~225 lines | 2 scaffold documents (arc4-01 L418â€“552; arc4-02 L37â€“95), 5 planning/craft blocks, 13 markers/prompts |
| EDITORIAL â€” duplicated take deletions | ~425 lines | 9 scene complexes; canon designated in Â§5 |
| MECHANICAL â€” scriptable closed map | ~105 line-level fixes | contractions 32; lowercase *i* 14; race-name 9; proper-noun ~20 lines; quote repairs 6; asterisk thoughts 5; typos 11; caps-punctuation pattern |
| JUDGMENT â€” needs Ainz-sama's decision | 7 items | J1â€“J7 in Â§6.3 |

**Top findings**
1. Two full scaffold documents published: "Here is a comprehensive summary of Ethra and Ajani's taleâ€¦" + worldbuilding sections (arc4-01 L418â€“552) and "The Chapter's Cadence / Ajani's Voice / What This Reveals About the Speaker" (arc4-02 L37â€“95).
2. The Kira pickpocket scene exists in **three** takes (arc4-04 L316â€“363 / L366â€“418 / L422â€“470) wrapped around author prompts and a marker ("Here's how that could play out.").
3. arc4-03's Kyre Tree communion contains three opening takes plus an internal rewrite, and arc4-03's crowd scene, arc4-02's search scene and Nefere entrance, arc4-05's kill scene and water hole, and arc4-06's grimoire demonstration each exist in two published takes.
4. arc4-01 L394: a long Ajani speech is missing its closing quote (file total 277 double quotes = odd; DQ walker unbalanced to EOF).
5. Arc Iâ€“II typo battery found **zero** hits in Arc IV; the new typos found (whar, hare, cumming, Sylvia, togheter, traning stipenâ€¦) are all in lowercase dialogue lines.
6. Canon compliance is otherwise solid: king/King fully compliant (41/41), em-dash usage consistent (559 em, 0 en, splits â‰¡ umbrella), Humman deviations confined to 9 narrative tokens + 3 tokens inside meta lines slated for deletion.

**Editorial-history note:** the `.stripped_meta` / `.stripped_passes` / `.repass3` / `.alpha_excise` artifacts show a cleanup pipeline ran pre-publication; it demonstrably did not cover author-voice planning prose, asterisk self-prompts, or duplicated takes. The remediation pass designed from this report should be added to that pipeline's marker set.

---

## 2. Per-Chapter Defect Catalog

Tags: **[M]** mechanical (scriptable), **[E]** editorial (judgment deletion/reword, canon determined here), **[J]** needs Ainz-sama's decision. Line numbers are split-file lines; umbrella lines in parentheses where located.

### 2.1 chapter-arc4-01.md â€” "Bureaucracy" (564 lines; umbrella L1â€“564)

| Line | Defect | Class |
|---|---|---|
| L5 | Crossed delimiters: `*i seriously hare this woman' â€¦ 'lets see what they want *` â€” thought opened `*`, closed `'`, then `'â€¦` closed `*`. Also `hare`â†’hate, `lets`â†’let's, lowercase *i*. | M |
| L181 | Thought line: `'next as long as i Live, â€¦ 'i hear the screams cumming '` â€” lowercase *i*; `cumming`â†’coming; `Live` miscapitalized; `" ,` space-before-comma. | M |
| L220â€“222 | Ajani speech **outside dialogue markup**, opening `"` never closed on the line; closing quote sits alone on L222 (`"`), two blank lines apart. Line contains `thats`, `were`â†’we're and five lowercase family names (bright paws, shadow paws, motted paws, stripe paws). | E (restructure into dialogue-block) + M |
| L277 | Thought `'goos they're nots just going along'` (`goos`â†’good, `nots`â†’not); `humman` lowercase; `traning stipen`â†’training stipend (line tail: "providing a traning stipen[d]"). | M |
| L371 | `"â€¦Maren sounds like hell Fit right in, objections?"` â€” `hell Fit` is either "she'll fit" (corruption) or legit "hell" + fragment; ambiguous. Also `roles ,` spacing. | J (J7) + M |
| L394 | **Missing closing quote**: long lowercase Ajani speech opens `"the security advisor will overseeâ€¦` and ends `â€¦they need to do this before 20 years` with no `"`. Whole file has 277 double quotes (odd); DQ walker unbalanced at EOF. Also `capitals shield`â†’capital's shield; `20 years`â†’twenty years. | M (priority) |
| L418â€“552 | **Scaffold document #1 published**: "Here is a comprehensive summary of Ethra and Ajani's tale, verified against everything weâ€¦" followed by bold sections **The Cosmic Structure of Ethra / The Magic System / The Super-Organisms / The Biomes / The Seven Sentient Races / The Five Tyrants / Ajani's Tale** (~135 lines; umbrella L417â€“552). Contains `wengari` lowercase at split L551. Story resumes at L554 (acceptance scene continues into arc4-02 â€” normal split boundary). | E delete |

### 2.2 chapter-arc4-02.md â€” "The Caravans" (597 lines; umbrella L565â€“1161)

| Line | Defect | Class |
|---|---|---|
| L37â€“95 | **Scaffold document #2 published**: **The Chapter's Cadence / Ajani's Voice / What This Reveals About the Speaker** (umbrella L599â€“657). Includes meta sentences "Ajani's internal monologue is the chapter's emotional engineâ€¦" (L48, embedded inside a dialogue-block before legitimate speech) and "The speaker also reveals a deep understanding of character voiceâ€¦" (L65). L48 carries the only split-`human` deviation (dies with the line). | E delete |
| L97 / L115 / L131 | Bold scene headings: `**The Shadow Paws â€” Underground Training Halls, Night**`, `**The Bright Paws â€” Temple of the Lightbringer, Night**`, `**The Motted Paws â€” The Silent Halls, Midnight**` (umbrella L659/677/693). No Arc Iâ€“III published chapter uses headings. | J (J3) |
| L154 | `'lets see what they want now'` (`lets`); `whar can this king dâ€¦`â†’what; `wengari`, `white dawn` lowercase. | M |
| L157â€“166 | **Nefere entrance â€” take A** (duplicated by take B at L167â€“176; entrance paragraph and title dialogue appear verbatim twice). | E delete (canon = take B) |
| L182 | `i am not being dragged to that stink bugs nest !!` â€” lowercase *i*; `stink bugs nest`â†’stink bugs' nest; `nefere` lowercase; `stripe paws` lowercase (line start). | M |
| L204 | `'i hope shes already spying on the hummans'` â€” lowercase *i*; `shes`â†’she's; `hummans` lowercase. | M |
| L240 | `"send in the humans"` â€” single-m deviation (narrative dialogue); `call Sylvia`â†’**Sylva** (name typo; corpus census: Sylvia=1, Sylva=59); `armor ,` spacing. | M |
| L288 | T'vat the attendant reference â€” canon per Arc Iâ€“II D4; no action. | â€” |
| L315 / L353 / L375 | Double-marked thoughts `*'â€¦'*` (e.g. `*'no one fainted...so disappointingâ€¦'*`). Canon: thoughts single-quotes only. | M (strip asterisks) |
| L326â€“328 | **Humman greeting â€” v1** ("The Hummans are honored by the king's welcomeâ€¦") duplicated by revised v2 at L336â€“338 ("â€¦despite the tremor in the merchant behind her"). Sylva's formal welcome L329â€“333 sits between and is kept. | E delete v1 |
| L391â€“436 | **Search scene â€” take A**: includes `"GUARDS WHAT DID YOU FIND ?'` (opens `"`, closes `'` â€” crossed) and the meta line L427 "**In Chapter Three**, during the delegations, Seris and her merchants could barely take ten stepsâ€¦" (author continuity note in prose). Superseded by take B L439+ per marker L437. | E delete; L391 quote M if salvaged |
| L437 | Marker: "Let me rewrite the scene from the search onward." | E delete |
| L478 / L494 | ALL-CAPS shouts with stacked punctuation `?!,` `!!` â€” cleanup pattern (also L413, arc4-03 L398â€“434). | M |
| L494 / L538 / L566 | `humman` lowercase (in dialogue/thoughts). | M |
| L552 / L556 | `hummans` lowercase; `wengari` lowercase; **`veylara`** x2 (L552, L566) â€” Arc Iâ€“II D7 precedent says probably "Veylar". | M + J (J5) |

### 2.3 chapter-arc4-03.md â€” "The Pyrinae Accord" (545 lines; umbrella L1162â€“1706)

| Line | Defect | Class |
|---|---|---|
| L151â€“167 | **Communion opening â€” take A** (short version; ends with Ajani walking away, contradicting the negotiation that follows). | E delete |
| L169 | Asterisk author self-prompt: `*You can start wherever you see fit as long as all threads are covered and we arrive with ajani at the end in the inner chamber*` (umbrella L1327). | E delete |
| L171â€“210 | **Communion opening â€” take B** (superseded by marker L211). | E delete |
| L211 | Marker: "Let me rewrite Ajani's opening and the Tree's response." Take C (canon) begins L213. | E delete |
| L233â€“389 | Entity ("Golden Sun") speech rendered as 22 balanced asterisk blocks across paragraph pairs. Canon Â§3 requires speech in double quotes; this is stylized telepathy. Asterisks balance file-wide (no unclosed spans). | J (J1) |
| L253â€“271 | Premature acceptance block ("I accept your pactâ€¦ This is the new pact. It is done. Now go.") sits **before** the point-by-point objections (L273+/L299+) and the final acceptance L387â€“389 â€” layered drafts of the negotiation; reading order is contradictory. | J (J2) |
| L270 / L338 / L388 | Pact phrase "and when the tide comes, i will shield your peopleâ€¦" x3 â€” fingerprint of the layering above. | J (J2) |
| L273â€“295 | **Tree's response â€” v1**, superseded by v2 at L299â€“315 per marker L297 (pairs: L274/L300, L283/L305). | E delete |
| L297 | Marker: "Let me rewrite the Tree's response." | E delete |
| L342 | `styx` lowercase; contractions `dont`, `its` in the Golden-Sun naming speech. | M |
| L366 | `wengari` lowercase; `togheter`â†’together; `doesnt`, `ill`, `thats`. | M |
| L398â€“434 | ALL-CAPS proclamation with missing apostrophes: CANT, DOESNT, DONT, HESÃ—3, IMÃ—2, ISNT, IVE, ILL (L246, L318, L342, L366, L398, L416, L434, L464, L522 â€” 25 hits, all in this chapter). | M |
| L420â€“480 | **Crowd scene â€” v1** (plaza reactions: warrior, merchants, Seris, priests, `now old thing dont let me down`), superseded by crowd-perspective v2 L483â€“546 per marker L481. Overlap fingerprints: L427â‰¡L545 ("Sylva stood motionlessâ€¦armor gleaming"), L449â‰¡L544 ("her daughter was in Sylva's service"). | E delete |
| L481 | Marker: "Let me rewrite the scene from the crowd's perspective." | E delete |

### 2.4 chapter-arc4-04.md â€” "The Humman Delegation" (612 lines; umbrella L1707â€“2318)

| Line | Defect | Class |
|---|---|---|
| L10 | ALL-CAPS with ILL, DONT, YOULL + lowercase *i* thought `'good, now all of them will walk it, this is so tiring.. i need a bath'`. | M |
| L305â€“313 | **Planning block (5 paragraphs)**: "I need to either retroactively establish her or remove her entirelyâ€¦"; "The Fire Beetles fill a crucial gapâ€¦"; "This explains why the Bright Pawsâ€¦live in walled citiesâ€¦"; "The evolutionary arms race you have described is elegantâ€¦" (co-author address); "Kira's revised backstory is grounded in this ecologyâ€¦" (umbrella L2007â€“2015). | E delete |
| L316â€“363 | **Kira market scene â€” take 1** (pens â†’ scratch â†’ alley dialogue â†’ west-wall-breach exchange). | E delete |
| L364 | Asterisk self-prompt: `*lets start then, ajani is in the market escaping the palace as usualâ€¦ its a bit Aladdin like but i believe it works, feedback?*` (umbrella L2066). | E delete |
| L366â€“418 | **Kira market scene â€” take 2** (adds market intro paragraph; same beats). | E delete |
| L420 | Marker: "Here's how that could play out." â€” contains the chapter's single stray curly apostrophe (`'`, U+2019; quote census: curlyCloseâ€²=1). Deleting the line resolves both. | E delete |
| L422â€“470 | Kira market scene â€” **take 3 = CANON** (continues into new content L472+: Sera appears, blood pact L486). | keep |
| L483 | `youre`â†’you're. | M |
| L507 | `'cheeky little...' - "â€¦cooped in the palace me hahaha!!!â€¦"` â€” `palace me` probably "palace, meh,"; minor. | M (low) |
| L536â€“564 | **Craft-critique block (15 paragraphs)**: numbered "First/Second/Third/Fourth" analysis of the Kira scene ("Kira is walking exposition, and you designed herâ€¦", "The west wall breach becomes a historical event we feel because we meet someoneâ€¦", "oldest and most effective trick in the storyteller's kit") ending in asterisk rebuttal L564 `*No, it's because she's walking exposition, through her we can learn lore in an organic wayâ€¦ schism she'sâ€¦*` (umbrella L2244â€“2266). Story resumes L566 (Vex). | E delete |

### 2.5 chapter-arc4-05.md â€” "The Gifts" (678 lines; umbrella L2319â€“2996)

| Line | Defect | Class |
|---|---|---|
| L53 | Asterisk self-prompt: `*With that understanding let's continue the vignettes ajani met Kira one week after the golden Sun, you must now include vignettes of herâ€¦ we should see her in class with tutors, with sylva,*` (umbrella L2366). Contains meta-`hummans`. | E delete |
| L70 | `"tell it to my face humman"` â€” lowercase humman. | M |
| L93â€“111 | **Kill scene â€” take A** (merchant's death; calm Ajani self-intro "I am Ajani, first of my nameâ€¦"). Superseded by take B L113â€“143: continuation L141 ("dragged the dead merchant's body **to Seris's feet**") matches take B's L113 placement, not take A's. | E delete |
| L113â€“143 | Kill scene â€” take B = CANON (ALL-CAPS shout L128â€“138; "AND THIS IS KIRA! MY SISTER!"). | keep |
| L148 | `ill` Ã—2 = "We will never speak **ill** of you againâ€¦" â€” legitimate word; false positive, no action. | â€” |
| L373â€“435 | **Water-hole scene â€” take A** (setup through Zara stepping forward / Ajani rising). Superseded by take B L438+ whose continuation (Vasha/Ember arrival L456+, reunion L459â€“493) is what the chapter continues with. Take A's unique beats (Zara L431, Ajani rising L435) are covered in take B at L496. | E delete |
| L438â€“439 | **Nested markup bug in canon take B**: `<div class="dialogue-block">` opened twice before "This is perfect". | M (fix while keeping B) |
| L514â€“528 | **Planning block (8 paragraphs)**: "Kira has been carrying that bag for months. Ajani noticed it but never askedâ€¦"; "Vex told her about the daggersâ€¦"; "And then the elders changed the gift without telling them."; "Kira's outburst is not merely disappointment. It is betrayalâ€¦"; "Vex's reaction **will be** the most telling momentâ€¦"; "Ajani **will be** looking at Kiraâ€¦"; "The Stripe Paws grinningâ€¦is the perfect punctuationâ€¦"; "I have only one small note. The Tide Wolf claw beads are a beautiful detail, but we should makeâ€¦" (umbrella L2828â€“2842). Story resumes L529 (Shadow Paw contingent) â€” the planned scene does exist after the block, so deletion is safe, but the L528 note ("we should makeâ€¦") may encode an intended tweak worth applying. | E delete (+J6 note) |

### 2.6 chapter-arc4-06.md â€” "Aftermath" (676 lines; umbrella L2997â€“3668)

| Line | Defect | Class |
|---|---|---|
| L25â€“67 | **Grimoire demonstration â€” take A**: thought block L27â€“29 `*Perhaps it will work...*`; test ritual; Elyra explanation v1 (L50 "The grimoire is bound to its owner. As you use it, it will growâ€¦"); "This is the best giftâ€¦" L54; coda L65â€“67 (sorcery reflection + "the green fire was still flickeringâ€¦") unique to this take. Superseded by take B. | E delete (+J4 coda salvage) |
| L69â€“116 | Grimoire demonstration â€” **take B = CANON**: Elyra explanation v2 (L94 "It is a living thingâ€¦"); revised echo L106 "This is **still** the best gift I have received today."; continuation L117+ ("He opened his mouth to answerâ€¦") flows from B. | keep |
| L72 | Asterisk thought `*Perhaps it will work...*` inside canon take B â€” canon Â§3: thoughts in single quotes, never `*â€¦*`. | M (*â†’') |
| L184 | Asterisk self-prompt: `*Very well are we ready to continue with the gift giving? We are only missing the humans and the explanation of what ajani tried to do with the grimoi[re]â€¦*` (umbrella L3175). Contains meta-`humans`. | E delete |
| L197 / L289 / L297 | Asterisk thought-blocks: `*Please, please not one of those foul creatures please.*`, `*Get them off!! Get them off!!*`, `*Oh. This isn't so badâ€¦ kind of cute.*` â€” likely Kira's thoughts; verify attribution when converting. | M (*â†’') |
| L330 / L430 / L496 | Possessive apostrophes (elders', scorpion's, Ajani's) â€” delimiter-checker false positives; no action. | â€” |
| L482â€“484 | "The king was **ill**." â€” legitimate word (Ajani's condition), false positive. "the **Humman King** was coming" â€” capitalized office title; compliant by Rule-2 analogy (cf. "King of the Wengari"); noted only. | â€” |

---

## 3. Canon-Rule Compliance

### 3.1 king/King â€” **PASS**
- Splits: `King` capitalized 41Ã—, lowercase `king` 360Ã—; umbrella identical (41/360).
- Every capitalized instance verified by context dump: all are title+name ("King Ajani" Ã—37) or formal office/proclamation titles ("King of the Wengari" arc4-02 L40â€“46; "the Humman King" arc4-06 L482â€“673 â€” Rule-2 analog).
- Zero lowercase `king Ajani/Uthgard` violations (umbrella-wide targeted check: none).
- Generic/apposition/direct-address uses correctly lowercase throughout ("the king was ill", "my king").

### 3.2 Humman â€” **NEAR-PASS (9 narrative deviations, all mechanical)**
- Canon forms dominate: splits Humman 99 (98 in umbrella + 1 in the generator-inserted arc4-04 heading) + Hummans 96. Umbrella: 98 + 96.
- Deviations (12 tokens): narrative 9 â€” arc4-01 L277 `humman`; arc4-02 L240 `humans`, L494/538/566 `humman`, L204/552Ã—2 `hummans`; arc4-05 L70 `humman` â€” plus 3 tokens sitting in meta lines already condemned for deletion (arc4-02 L48 `human`, arc4-05 L53 `hummans`, arc4-06 L184 `humans`). After debris removal + mechanical fixes: zero.
- Corpus check reproduces the Arc Iâ€“II tally artifact (negative "plain human" count = arithmetic artifact of subtracting double-m from single-m totals; disregarded as in the reference report).

### 3.3 Dialogue formatting â€” **FAIL (bounded, enumerated)**
- Speech uses ASCII straight double quotes everywhere; curly quote census clean except one stray U+2019 apostrophe at arc4-04 L420 (a marker line â€” dies with deletion).
- **Quote balance:** arc4-01 has 277 double quotes (odd). Root cause L394 (speech missing closing `"`); the L220/L222 anomaly (orphaned closing quote on its own line) is internally paired. DQ walker otherwise balanced in all six chapters.
- **Crossed/double-marked:** arc4-02 L391 `"GUARDS WHAT DID YOU FIND ?'` (open `"` close `'`); arc4-02 L315/353/375 `*'â€¦'*` double-marked thoughts; arc4-01 L5 `*â€¦'â€¦'â€¦*` crossed. All mechanical.
- **Asterisk thoughts:** five thought-blocks in arc4-06 (L28 â€” dies with take A, L72, L197, L289, L297) render thoughts as `*â€¦*` â€” canon requires single quotes.
- **Entity speech:** arc4-03 L233â€“389 asterisk blocks â€” J1 (stylistic telepathy vs canon).
- **Contractions:** 38 battery hits; 3 false positives (`ill` legitimate Ã—3), 1 ambiguous (`hell` â€” J7), 2 inside condemned meta lines; **32 genuine mechanical fixes**, concentrated in ALL-CAPS proclamation lines (arc4-03: 25).
- **Standalone lowercase *i*:** 14 genuine (arc4-01 Ã—2, arc4-02 Ã—2, arc4-03 Ã—8, arc4-04 Ã—2) + 1 inside condemned meta (arc4-04 L364).
- **Lowercase proper nouns:** ~20 narrative lines (arc4-01 L93/L143/L220; arc4-02 L154/L182/L315/L494â€“L566; arc4-03 L342/L366) â€” family names, Wengari, White Dawn, Styx, Veylara (â†’J5). All inside lowercase dialogue/thought lines; mechanical capitalization pass.

### 3.4 Em dashes â€” **PASS (canon maintained)**
- Splits: 91+110+96+94+93+75 = **559 em dashes = umbrella 559 exactly**; **0 en dashes, 0 hbars, 0 ASCII-hyphen dialogue openers**.
- Odd-count lines 279, classified: CUT(speech) 36, TAIL(elaboration) 59, OPEN-MID(suspect heuristic) 184. Spot-samples of OPEN-MID (arc4-01 L89/L398/L424, arc4-03 L349, arc4-04 L428, arc4-06 L653) are all canon usage #3 (single dash introducing an elaboration running to sentence end) or paired parentheticals. Inherits Arc Iâ€“II D1: full 184-line review list is only needed if Ainz-sama declines the canon reading.

---

## 4. Umbrella Draft-Debris Inventory

All fixes target `content/story/chapter-04.md`. Umbrella line numbers below were located by exact text search (umbrella_locate.py / umbrella_debris_scan.py). Keep/delete = recommendation; canon evidence in Â§5 where applicable.

| Umbrella lines | Split location | Debris type | Keep/Delete |
|---|---|---|---|
| L417 | arc4-01 L418 | "Here is a comprehensive summary of Ethra and Ajani's tale, verified against everything weâ€¦" | DELETE |
| L419â€“552 (headings L419/425/431/439/453/473/487) | arc4-01 L420â€“552 | Scaffold doc #1: Cosmic Structure / Magic System / Super-Organisms / Biomes / Seven Sentient Races / Five Tyrants / Ajani's Tale | DELETE |
| L599â€“657 (headings L599/607/617) | arc4-02 L37â€“95 | Scaffold doc #2: The Chapter's Cadence / Ajani's Voice / What This Reveals About the Speaker (contains "emotional engine" L610, "reveals a deep understanding" L627) | DELETE |
| L659 / L677 / L693 | arc4-02 L97/115/131 | Bold scene headings (Shadow/Bright/Motted Paws night vignettes) | J3 (delete vs keep-as-separators) |
| L719â€“736 | arc4-02 L157â€“176 | Nefere entrance, two takes | DELETE take A (L719â€“726 â‰ˆ split L157â€“166) |
| L888â€“898 | arc4-02 L326/336 | Humman greeting v1/v2 | DELETE v1 (L888) |
| L989 | arc4-02 L427 | "In Chapter Threeâ€¦" author continuity note | DELETE (inside take A block) |
| L999 | arc4-02 L437 | Marker "Let me rewrite the scene from the search onward." | DELETE |
| L~953â€“998 | arc4-02 L391â€“436 | Search scene take A (incl. crossed quote L391) | DELETE (canon = L1001+) |
| L1311â€“1367 | arc4-03 L151â€“167 + prompt L169 | Communion take A + asterisk self-prompt (L1327) | DELETE |
| L1329â€“1368 | arc4-03 L171â€“210 | Communion take B | DELETE |
| L1369 | arc4-03 L211 | Marker "Let me rewrite Ajani's opening and the Tree's response." | DELETE |
| L~1425â€“1454 | arc4-03 L273â€“295 | Tree's response v1 | DELETE (canon = L1457+) |
| L1455 | arc4-03 L297 | Marker "Let me rewrite the Tree's response." | DELETE |
| L~1415â€“1435 vs L1465â€“1545 | arc4-03 L233â€“389 | Entity asterisk-block negotiation; acceptance layer L253â€“271 vs final L387â€“389; pact phrase x3 (umbrella L1427/1495/1545) | J1 + J2 |
| L1585â€“1641 | arc4-03 L420â€“546 | Crowd scene v1/v2 overlap (fingerprints L1585â‰¡L1703, L1625â‰¡L1641) | DELETE v1 (marker L1639; canon = L1641+) |
| L1639 | arc4-03 L481 | Marker "Let me rewrite the scene from the crowd's perspective." | DELETE |
| L2007â€“2015 | arc4-04 L305â€“313 | Kira planning block (5 paragraphs) | DELETE |
| L2018â€“2065 | arc4-04 L316â€“363 | Kira scene take 1 (tripled at L2018/2070/2126) | DELETE |
| L2066 | arc4-04 L364 | Asterisk self-prompt "lets start thenâ€¦ Aladdin likeâ€¦ feedback?" | DELETE |
| L2068â€“2121 | arc4-04 L366â€“418 | Kira scene take 2 | DELETE |
| L2122 | arc4-04 L420 | Marker "Here's how that could play out." (+ stray curly apostrophe) | DELETE |
| L2124â€“2172 | arc4-04 L422â€“470 | Kira scene take 3 | KEEP (canon) |
| L2244â€“2266 | arc4-04 L536â€“564 | Craft-critique block + asterisk rebuttal ("walking exposition" L2254/2266) | DELETE |
| L2366 | arc4-05 L53 | Asterisk self-prompt "let's continue the vignettesâ€¦" | DELETE |
| L2406â€“2424 | arc4-05 L93â€“111 | Kill scene take A | DELETE (canon = L2426+) |
| L2692â€“2752 | arc4-05 L373â€“435 | Water-hole take A | DELETE (canon = L2754+) |
| L2828â€“2842 | arc4-05 L514â€“528 | Planning block (8 paragraphs; L2842 ends mid-sentence "but we should makeâ€¦") | DELETE (verify J6 tweak first) |
| L3016â€“3056 | arc4-06 L25â€“67 | Grimoire take A (thought-block L3018â€“3020; coda â‰ˆL3054â€“3056) | DELETE (J4 coda salvage) |
| L3060â€“3106 | arc4-06 L69â€“116 | Grimoire take B | KEEP (canon) |
| L3175 | arc4-06 L184 | Asterisk self-prompt "are we ready to continueâ€¦" | DELETE |
| L2572 | (stripped by generator; not published) | Stale heading "## Chapter 5: The Gifts" (old flat numbering; the only sub-chapter with an internal heading) | DELETE |
| L1 / L2300 / L2348 | â€” | "# Chapter 4" title (generator strips); "corrected" in narrative prose (Kira vignettes) | KEEP (not debris) |

---

## 5. Duplicate Blocks with Canon Designation

Nine complexes. Canon direction determined by (a) author markers, (b) revision fingerprints, (c) narrative continuity of the text that follows each block. "Takes" are listed in file order.

| # | Scene | Takes (split lines) | Canon | Evidence |
|---|---|---|---|---|
| 1 | arc4-02 Nefere entrance | A: L157â€“166 Â· B: L167â€“176+ | **B** | Entrance paragraph + title dialogue verbatim in both; B continues into extended road dialogue; A's tail sentences (L162/L166) are reissued in B (L172/L176) |
| 2 | arc4-02 Humman greeting | v1: L326â€“328 Â· v2: L336â€“338 | **v2** | v2 adds "despite the tremor in the merchant behind her" (links preceding scene); Sylva's welcome L329â€“333 between them is unique and kept |
| 3 | arc4-02 Search scene | A: L391â€“436 Â· B: L439â€“500+ | **B** | Marker L437 "Let me rewrite the scene from the search onward."; B supersedes A's letter-device with the sleeve-stone device and continues into the confrontation. Note: A's "sealed letter" beat has no downstream references found (crossref_letter.py); verify stone-device consistency with arc5 at remediation |
| 4 | arc4-03 Communion opening | A: L151â€“167 Â· B: L171â€“210 Â· C: L213+ | **C** | A ends with Ajani leaving (contradicts continuation); marker L211 explicitly rewrites into C; self-prompt L169 sits between A and B |
| 5 | arc4-03 Tree's response | v1: L273â€“295 Â· v2: L299â€“315 | **v2** | Marker L297; pairs L274â‰¡L300, L283â‰¡L305 |
| 6 | arc4-03 Crowd scene | v1: L420â€“480 Â· v2: L483â€“546 | **v2** | Marker L481 "rewrite the scene from the crowd's perspective"; overlap fingerprints L427â‰¡L545, L449â‰¡L544 |
| 7 | arc4-04 Kira market scene | 1: L316â€“363 Â· 2: L366â€“418 Â· 3: L422â€“470 | **3** | Marker L420 "Here's how that could play out."; take 3 flows into unique continuation (Sera, blood pact L472â€“486); 6 core paragraphs verbatim x3 |
| 8 | arc4-05 Kill scene | A: L93â€“111 Â· B: L113â€“143 | **B** | Continuation L141 matches B's staging (body "to Seris's feet"); B's shout-version self-intro is what the following Kira scene responds to |
| 9 | arc4-05 Water-hole scene | A: L373â€“435 Â· B: L438â€“452+ | **B** | Continuation (Vasha/Ember arrival, reunion L459â€“493) flows from B; A's unique beats (Zara L431, Ajani rising L435) recur in B-continuation at L496 |
| 10 | arc4-06 Grimoire demonstration | A: L25â€“67 Â· B: L69â€“116 | **B** | B revises the echo ("This is **still** the best gift") and expands Elyra's lore ("It is a living thing"); continuation L117+ answers B's closing silence. **Salvage note:** A's coda L65â€“67 (sorcery reflection) is unique â€” see J4 |

**Layering caveat (not a simple block deletion):** complex 4's continuation contains the entity negotiation with a premature acceptance block (arc4-03 L253â€“271) preceding the objections and the final acceptance (L387â€“389); pact language appears x3 (L270/338/388). Untangling this reading order is J2.

---

## 6. Remediation Classification

### 6.1 MECHANICAL (scriptable closed map â€” no creative judgment)

| Fix | Lines (split) | Operation |
|---|---|---|
| Missing closing quote | arc4-01 L394 | Append `"` at speech end (then re-run quote walker; expect balance) |
| Crossed quote | arc4-02 L391 | `'`â†’`"` at line end |
| Crossed/double-marked thoughts | arc4-01 L5; arc4-02 L315, L353, L375 | Strip `*`, keep single quotes |
| Asterisk thought-blocks | arc4-06 L72, L197, L289, L297 (L28 dies with take A) | `*â€¦*`â†’`'â€¦'`; verify owner (likely Kira) |
| Contractions | arc4-01 L5, L220; arc4-02 L154, L204; arc4-03 L246, L318, L342, L366, L398, L416, L434, L464, L522; arc4-04 L10, L483 | Insert apostrophes (incl. inside ALL-CAPS: CANTâ†’CAN'T etc.) |
| Lowercase *i* | arc4-01 L5, L181; arc4-02 L182, L204; arc4-03 L246, L318, L342, L522; arc4-04 L10 | Capitalize standalone I |
| Race name | arc4-01 L277; arc4-02 L204, L240, L494, L538, L552Ã—2, L566; arc4-05 L70 | humman(s)â†’Humman(s), humansâ†’Hummans |
| Proper nouns | arc4-01 L93, L143, L220; arc4-02 L154, L182, L315, L494â€“L566 (wengari, white dawn, stripe paws, family names); arc4-03 L342 (styx), L366 | Capitalize |
| Typos | arc4-01 L5 hareâ†’hate, L181 cummingâ†’coming + Liveâ†’live, L277 goosâ†’good/notsâ†’not/traning stipenâ†’training stipend; arc4-02 L154 wharâ†’what, L240 Sylviaâ†’Sylva; arc4-03 L366 togheterâ†’together; arc4-02 L182 stink bugs nestâ†’stink bugs' nest; arc4-01 L394 capitals shieldâ†’capital's shield, 20 yearsâ†’twenty years; arc4-04 L507 palace meâ†’palace, meh (low confidence) | Word map |
| Punctuation spacing/stacking | arc4-01 L181/L371 `" ,` `roles ,`; arc4-02 L391 `?'`; ALL-CAPS `?!,` `!!` (arc4-02 L413/L478/L494; arc4-03 L398â€“434) | Normalize |
| Nested div | arc4-05 L438â€“439 | Remove duplicate `<div class="dialogue-block">` |

All of the above live in the umbrella at the Â§4-mapped positions; apply there, regenerate splits, re-run `QA/arc4_tooling/` battery as acceptance gate.

### 6.2 EDITORIAL (judgment deletion/reword; canon already determined by this audit)

Execute Â§4 DELETE rows + Â§5 canon designations. Order of operations: (1) delete scaffold docs and meta blocks; (2) delete superseded takes (keep canon takes); (3) delete markers/prompts; (4) delete stale umbrella heading L2572; (5) restructure arc4-01 L220â€“222 orphaned speech into a dialogue-block; (6) mechanical pass Â§6.1; (7) regenerate + battery re-run. Estimated removable volume â‰ˆ650 lines (~18% of published arc). No creative rewriting required â€” every deletion has a surviving canon counterpart except the scaffold docs (pure planning text; the story they summarize is told in-scene elsewhere).

### 6.3 JUDGMENT (needs Ainz-sama's decision)

| ID | Item | Options / recommendation |
|---|---|---|
| J1 | arc4-03 L233â€“389: entity ("Golden Sun") speech as asterisk blocks | (a) convert to double-quoted dialogue like other speakers; (b) convert to single-quoted telepathy per thought-canon; (c) keep as deliberate telepathic styling. Rec: (b) or (c) with an explicit canon rule for telepathy |
| J2 | arc4-03 communion layering: premature acceptance L253â€“271 vs objections L273+/L299+ vs final acceptance L387â€“389; pact phrase x3 | Requires a read-through to order the negotiation coherently; likely demote L253â€“271 to a tentative "I am listening" beat or delete |
| J3 | arc4-02 L97/115/131 bold scene headings | Delete (Arc Iâ€“III precedent: no headings) or keep as scene separators; if kept, style consistently |
| J4 | arc4-06 take-A coda L65â€“67 (sorcery reflection, unique prose) | Salvage into take B's continuation, or drop |
| J5 | arc4-02 L552/L566 `veylara` | Arc Iâ€“II D7 precedent: probably "Veylar"; confirm intent |
| J6 | arc4-05 L528 planning note ends mid-thought ("â€¦but we should makeâ€¦") | Recover the intended tweak from `.stripped_passes`/`.repass3` artifacts if desired before deleting (artifacts are read-only reference) |
| J7 | arc4-01 L371 "Maren sounds like hell Fit right in" | Reconstruct intent ("she'll fit right in" vs legit "hell"), then fix |
| D1 (inherited) | 184 OPEN-MID em-dash lines | Only if Ainz-sama declines the Arc Iâ€“II canon reading; spot samples are compliant |

---

## 7. Status

- [x] Skeleton created (2026-08-24)
- [x] Lint battery executed on splits (lint_arc4.py, lint_pass2_arc4.py, quote_pair_check_arc4.py, delimiter_cross_check_arc4.py, em_census_arc4.py, em_classify_arc4.py, final_tally_arc4.py)
- [x] Umbrella debris scan executed (umbrella_debris_scan.py + umbrella_locate.py/.2 + umbrella_headings.py; grep + targeted line reads only â€” no whole-file reads)
- [x] Spot-verification of script output against actual lines (all catalog entries read in source; take boundaries walked line-by-line)
- [x] Sections 1â€“6 filled
- [x] **FINAL** â€” audit complete. No story content was modified; outputs confined to `QA/arc4_audit_report.md` and `QA/arc4_tooling/`. Awaiting Ainz-sama's judgment on J1â€“J7 before remediation executes.







---

# PART III - ARC V AUDIT REPORT (verbatim)

# Ethra QA Report â€” Arc V "The Great War" Proactive Audit

- **Prepared by:** Demiurge's audit subagent (script-first method; defect battery established in the Arc Iâ€“II audit)
- **Date:** 2026-08-24
- **Scope:** `ethra_site/content/story/chapters/chapter-arc5-01..22.md` (22 published split files, READ-ONLY) + umbrella master `content/story/chapter-05.md` (293,483 bytes on disk, CRLF; 2,275 lines; READ-ONLY; source of truth for future fixes)
- **Splitting architecture:** `regenerate_chapters.py` splits the umbrella at LINE anchors from `arcs.json â†’ arcs.5.split_anchors` (21 anchors: 410, 550, 728, 772, 792, 998, 1090, 1111, 1146, 1278, 1592, 1636, 1668, 1703, 1762, 1872, 1909, 2023, 2132, 2156, 2193). Chapter headings (`## Chapter N: <timestamp> â€” <title>`) are GENERATED from `arcs.json â†’ sub_titles`; the umbrella itself contains only `# Chapter 5: The Great War` (L1).
- **Tooling:** `ethra_site/QA/arc5_tooling/` â€” adapted copies of the Arc Iâ€“II battery (FILES = 22 arc5 files) plus new scripts: `a5_boundary.py` (regeneration + boundary check), `a5_umbrella.py` (umbrella debris scan), spot-readers. Outputs prefixed `a5_*`. Original QA scripts untouched. All story files READ-ONLY throughout.
- **Status:** FINAL (Â§7)

---

## 1. Executive Summary

Arc V is typographically clean and mechanically the best-formed arc audited to date â€” **zero** missing-apostrophe contractions, zero lowercase standalone *i*, zero unbalanced quotes, zero crossed delimiters, zero lowercase proper nouns in polished prose, zero Arc Iâ€“II typo-list hits, and fully canon-compliant em-dash usage (446 dashes reviewed). However, it carries a **severe draft-hygiene problem**: 17 debris/duplicate blocks spread across 11 of the 22 chapters (ch01, 03, 06, 07, 11, 13, 15, 16, 18, 19, 22), the same root cause as Arc II (pre-correction take + corrected take published together, plus raw author stage-directions left in the file).

### Defect counts by class

| Class | Description | Count |
|---|---|---|
| A â€” Author meta-text / draft-instruction blocks | Present-tense stage directions, craft commentary, AI-instruction lines published in-story | **9 blocks** |
| B â€” Duplicate draft blocks | Same scene present twice (two takes) or re-hashed a third time | **8 groups** |
| C â€” Canon deviations in polished prose | king/King (1), Humman single-m (1), thought-delimiter `*`/`_` (7), inscription/memory delimiter (2) | **11 items** (of which 2 are conditional on judgment J2) |
| D â€” Editorial formatting | Narrative prose wrapped in `<p class="speech-line">` | **3 items** |
| E â€” Em-dash defects | â€” | **0** |
| F â€” Quote/contraction/proper-noun/typo defects | â€” | **0** |
| **Total actionable** | | **31 items** |

### Arc health verdict

**NOT reader-ready as published; fully recoverable with one remediation pass.** All 17 Class A/B blocks are deletions (no prose rewriting required â€” every deleted beat is either duplicated elsewhere or covered by a polished version later in the arc). Classes C/D are small mechanical/editorial fixes. The 22 published splits are **byte-identical** to a fresh regeneration from the umbrella (Part 1 of Â§6b), so all fixes must land in `chapter-05.md` followed by `regenerate_chapters.py`.

### Top findings

1. **Raw author stage-directions published inside `<div class="dialogue-block">`** at arc5-15 L4, arc5-16 L110, arc5-18 L4 & L90, arc5-19 L4, arc5-22 L4 â€” e.g. *"Ajani tores a fifth pageâ€¦ he chants visibily strained"*, *"The light walk begins to crack, then it breaks Nefere yells 'FIRE'â€¦ cleaves trough the sand"*. Each is immediately followed by its polished version.
2. **Explicit AI-collaboration instruction published in-story:** arc5-11 L157 `*Then you should write the scene please (the Cefiro scene )*`.
3. **Author craft-essay published as story text:** arc5-07 L59â€“73 ("Velarius Vane has been seeded since the earliest chapters of the Ethra exerciseâ€¦ we have establishedâ€¦ the reader should feelâ€¦").
4. **Whole scenes doubled** in ch01 (war room; Council of the Untrustworthy), ch03 (the dome), ch06 (fire-pillar aftermath + Mekhmed's tent), ch11 (civilian army), ch15 (cannon volley), ch16 (battle re-hash), ch19 (the five-minute sequence).
5. **New non-canon thought delimiters:** `*â€¦*` (arc5-02 L11/L49, arc5-22 L47, arc5-21 L10 inside a `thought-block` div) and `_â€¦_` (arc5-11 L25/L171) â€” canon is single quotes only. Note: `chapter-arc4-06.md` already uses `thought-block` + `*â€¦*` five times, so the convention question is escalated as judgment J2.
6. **Bonus boundary check (Â§6b): PASS.** No chapter boundary cuts a sentence mid-clause; all 22 files end on sentence-final punctuation; regeneration round-trip is byte-identical.

### Open judgment items (need Ainz-sama)

- **J1** â€” arc5-01 Council scene: pick a take or ratify the recommended merge (take-B spine + take-A's member introductions).
- **J2** â€” Thought presentation: enforce single-quote canon everywhere, or ratify `thought-block` + `*â€¦*` as a sanctioned style (Arc IV precedent).
- **J3** â€” "the young Bright Mane soldier" (arc5-02 L29, arc5-05 L19): Brightmane / Bright Paw / lowercase descriptor.
- **J4** â€” arc5-11 civilian-army speech: take A (M'rak's long speech) vs take B (delegation to Tamsin). Recommendation: B.

---

## 2. Per-Chapter Defect Catalog

Line numbers refer to the **published split files** (`content/story/chapters/chapter-arc5-NN.md`). Umbrella line numbers for the same content are given in Â§4. Chapters not listed (04, 05, 08, 10, 14, 17, 20) are clean except where noted.

### chapter-arc5-01.md (05:25 â€” Vasha Storms In)
| Line(s) | Class | Finding |
|---|---|---|
| L74â€“142 | B1 | **Duplicate war-room scene, take A** (later-timeline scout report: "The first vanguard is destroyedâ€¦ The second vanguard is advancingâ€”two hundred and fifty riders"). Contradicts the chapter's 5:25 frame. Canon = take B (L144â€“232). |
| L144â€“232 | B1 | Duplicate war-room scene, **take B (CANON)** â€” contains Vasha's entrance matching the chapter title ("At 5:25 in the morning, Vasha stormed into the war room unannounced." L146). |
| L236â€“291 | B2 | **Duplicate Council scene, take A** â€” richer member introductions (Maren, Sylen, Toren, Kellan). |
| L292â€“375 | B2 | **Duplicate Council scene, take B** â€” Kellan-focused, flows into the Mekhmed tent scene (L376). See J1. |
| L359 | C | `"that the Humman King thinks he is attacking a wounded cityâ€¦"` â€” capitalized *King* with determiner â†’ should be `the Humman king` (canon rule 1). |

### chapter-arc5-02.md (06:55 â€” Sera Holds The Gate)
| Line(s) | Class | Finding |
|---|---|---|
| L11 | C | `*We can't win against four hundred. We barely survived fifty.*` â€” asterisk thought (Sera). Canon: single quotes. |
| L29 | C/J3 | `Irek was among themâ€”the young Bright Mane soldierâ€¦` â€” "Bright Mane" (two words); corpus canon is "Brightmane" (291 occurrences elsewhere; zero outside the arc5 umbrella). |
| L49 | C | `*We cannot hold.*` â€” asterisk thought (Sera). |
| L68 | â€” | False positive checked: "Our king lies **ill**" â€” adjective, not a contraction. No defect. |

### chapter-arc5-03.md (06:25 â€” The War Room Still Watches)
| Line(s) | Class | Finding |
|---|---|---|
| L51â€“86 | B3 | **Duplicate dome scene, take A** (mirror "carried since the capital was foundedâ€¦ three thousand years ago"). Canon = take B. |
| L87â€“122 | B3 | **Take B (CANON)** â€” High-Speaker lineage lore ("passed from High Speaker to High Speaker since the time of the Third Tyrant"). |
| L92 | C | Inside canon take B: `*You will never use this unless the capital itself is in dangerâ€¦*` â€” asterisk-quoted inscription inside a speech-line â†’ convert to double quotes. |
| L171 | C | `*Stay here. Stay hidden. Don't make a soundâ€¦*` â€” asterisk-remembered speech (Kira's mother) â†’ convert to double quotes. |

### chapter-arc5-05.md (08:15 â€” The Second Shot)
| Line(s) | Class | Finding |
|---|---|---|
| L19 | C/J3 | `The young Bright Mane soldier who had watched the first wave dieâ€¦` â€” second occurrence of "Bright Mane". |

### chapter-arc5-06.md (08:20 â€” The Light Shield Falls)
| Line(s) | Class | Finding |
|---|---|---|
| L7 | â€” | `The gate was stillâ€”` checked: intentional narrative interruption (cut off by "A flash. A thunder."). Valid, no defect. |
| L135â€“159 | B4 | **Duplicate aftermath + tent scene, take A** â€” includes a premature messenger scene ("The Woh riders had arrived. The ghosts were coming." L159) contradicting the 08:20 timeline (reinforcements arrive 10:35â€“11:50). |
| L161â€“177 | B4 | **Take B (CANON)** â€” timeline-consistent; flows into Tamsin's ride (L178+). |
| L190 | C | `"I'M TAMSIN, GENERAL OF THE HUMANS!"` â€” single-m in all-caps â†’ `HUMMANS`. |

### chapter-arc5-07.md (08:40 â€” The Plague Comes)
| Line(s) | Class | Finding |
|---|---|---|
| L59â€“61 | A | **Craft meta-text inside dialogue markup:** `<div class="dialogue-block"><p class="speech-line">Velarius Vane has been seeded since the earliest chapters of the Ethra exerciseâ€¦ the reader should feel a cold shock of recognitionâ€¦</p></div>` |
| L63â€“73 | A | **Craft-essay paragraphs:** "The suicide scorpions are also consistent with the Humman character **we have established**â€¦" / "**This scene also serves a structural purpose**â€¦" / "The deaths of the Wengari feel weighty because **we have spent time with them**â€¦" â€” all author voice, delete. |

### chapter-arc5-08.md (08:45 â€” Scorpions Still Marching)
Clean. (Ends mid-scene on a dialogue block that continues in ch09 â€” intentional cliffhanger, verified well-formed.)

### chapter-arc5-09.md (09:00 â€” The Truce Lasts An Hour)
| Line(s) | Class | Finding |
|---|---|---|
| L3â€“5 | D | Scene-closing narrative paragraph wrapped in `<div class="dialogue-block"><p class="speech-line">` ("He did not need to say who 'he' wasâ€¦"). Editorial reformat. |

### chapter-arc5-11.md (09:45 â€” The War Becomes Worse)
| Line(s) | Class | Finding |
|---|---|---|
| L25 | C | `_This is hell. I've stepped into hell._` â€” underscore thought delimiter (M'rak), unique to Arc V. â†’ single quotes. |
| L157 | A | `*Then you should write the scene please (the Cefiro scene )*` â€” **author instruction to the writing system, published in-story.** Delete. |
| L171 | C | `_Can we win with that?_` â€” underscore thought. â†’ single quotes. |
| L181â€“199 | B5 | **Duplicate civilian-army scene, take A** â€” M'rak's long speech ("You answer to me. You answer to herâ€¦ The enemy is across the sand."). |
| L201â€“223 | B5 | **Take B (CANON, pending J4)** â€” delegates the civilians to Tamsin ("Here is your army. Man the wall. If the wall falls, we all fall. Go."), consistent with her redemption arc. |
| L218 | D | Inside canon take B: narrative + speech mixed in one speech-line (`M'rak nodded. He gesturedâ€¦ "Here is your armyâ€¦"`). Editorial reformat. |
| L225 | D/J | "Cefiro's voice had its own music â€” 'cousin' instead of 'brother'â€¦" â€” craft-flavoured narration; reads as narrator voice but borders on author commentary. Keep by default; flag for awareness. |

### chapter-arc5-12.md (10:35 â€” The Wall Blanketed)
| Line(s) | Class | Finding |
|---|---|---|
| L43â€“45 | D | Shadow-Paw arrival: narrative + dialogue in one speech-line (`The shadow riders reached the gateâ€¦ "We are the Shadow Pawsâ€¦ We are here."`). Polished prose, wrong wrapper. Editorial reformat. |

### chapter-arc5-13.md (11:20 â€” The Shadow Figure Drinks)
| Line(s) | Class | Finding |
|---|---|---|
| L31â€“33 | A | **Draft scene-summary inside dialogue markup:** "At the wall, the black thing took shape before themâ€¦ M'rak asked everyone presentâ€¦ Zephyr said, 'Open the gates for the humans, don't give it more food'â€¦" â€” also contains single-m "humans". The open-the-gates beat is properly told in canon form at arc5-14 L24â€“31 (Tamsin: "OPEN THE GATES! THOSE ARE MY PEOPLE!"), so deletion loses nothing. |

### chapter-arc5-14.md (11:35 â€” The Wall Learns Horror)
Clean. (Contains the canon gate-opening scene.)

### chapter-arc5-15.md (11:40 â€” M'rak Yells Clear)
| Line(s) | Class | Finding |
|---|---|---|
| L3â€“5 | A | **Draft instruction block inside dialogue markup:** "The black thing approaches slowly as if it couldn't quite control it's body, M'rak yells 'ALL CANNONS FIRE!!!! FIRE THE RAY!!!! NOW!!!'â€¦" (typos: *it's body*, run-on present tense). |
| L7â€“33 | B6 | **Duplicate cannon sequence, take A** â€” includes "FIRE THE RAY" and the ray firing at 11:40 ("the mirror array had fired its last shot and was dark", L31), contradicting ch16 (ray still needs 3 min, L30) and ch18 (Nefere fires at 11:59). |
| L35â€“61 | B6 | **Take B (CANON)** â€” cannons only, no premature ray. |

### chapter-arc5-16.md (11:50 â€” Vows Are Absolved)
| Line(s) | Class | Finding |
|---|---|---|
| L27â€“65 | B7 | **Canon sequence** â€” creature approach, ray countdown, Zephyr's charge, Solen's priest column and absolution (matches chapter title). |
| L67â€“105 | B7 | **Third copy of the cannon/reform sequence** (verbatim from ch15 take B: L67 approach, L70 "ALL CANNONS FIRE!", L73 volley, L79 reform, L84 "It reformed") + re-hash of L27â€“51 (ray countdown L88, wolf charge L95â€“97, Zephyr's frustration L102 verbatim Ã—2, "barely two leagues away" L105 vs L27). Internally contradictory (point-blank cannons followed by "two leagues away"). Delete. |
| L107 | B7 | Duplicate 11:50 boilerplate (second in chapter). |
| L109â€“111 | A | **Draft scene-summary with stage direction:** "â€¦Solen emerged wreathed in golden armorâ€¦ Tamsin asked, 'Who is he?'â€¦ **Back to M'rak.** He saidâ€¦" â€” the polished version of this exact scene is arc5-17 L11â€“35. Chapter currently ENDS on this draft block. |

### chapter-arc5-17.md (11:55 â€” The Legend Answers)
Clean (contains the canon Solen-descent scene).

### chapter-arc5-18.md (11:59 â€” Nefere Fires)
| Line(s) | Class | Finding |
|---|---|---|
| L3â€“5 | A | **Draft instruction block:** "The light walk begins to crack, then it breaks Nefere yells 'FIRE' an impossibly hot beam of light cleaves trough the sandâ€¦ postratedâ€¦ it's 11:59" (typos: *trough*, *postrated*). Polished version follows at L7+. |
| L89â€“91 | A | **Draft instruction block:** "Ajani lands on the wall shouting 'STATUS STATUSâ€¦' we hear awed whispers 'his highness' Al around solen turns to ajani and quickly kneelsâ€¦ ajani roars 'LESS KNEELING AND MORE TALKING!!!'" â€” polished version follows at L93â€“105. |

### chapter-arc5-19.md (12:02 â€” Ajani Throws The Spear)
| Line(s) | Class | Finding |
|---|---|---|
| L3â€“5 | A | **Draft instruction block:** "Ajani says 'crap' and flies up in the skyâ€¦ beseeschsâ€¦ zephyr says 'you heard him, charge!!!'â€¦ it's now 12:02". |
| L7â€“41 | B8 | **Duplicate five-minute sequence, take A** â€” merged-spear â†’ fire-spirit concept; ends "It was 12:02 in the morningâ€”noon" (self-contradictory phrasing). |
| L43â€“79 | B8 | **Take B (CANON)** â€” five-spear pentagon, page ritual, IFRIT invocation, fire-copy; correct "It was 12:02 in the afternoon" (L79). Page-ritual structure is what ch20â€“22 continue ("the fifth page"). |

### chapter-arc5-21.md (12:05 â€” The Light Cage Fades)
| Line(s) | Class | Finding |
|---|---|---|
| L9â€“11 | C/J2 | `<div class="thought-block">*Just two more. And then... well, let's hope I can still speak.*</div>` â€” asterisk thought inside a CSS-supported `thought-block` (same pattern as `chapter-arc4-06.md` Ã—5). Subject to J2. |

### chapter-arc5-22.md (12:06 â€” The White Dawn Wakes)
| Line(s) | Class | Finding |
|---|---|---|
| L3â€“5 | A | **Draft instruction block:** "Ajani tores a fifth page, deep gold runes adorn it and he chants visibily strainedâ€¦ Kira clutches pearl tightly then ajani tores a sixth pageâ€¦" (typos: *tores* Ã—2, *visibily*). Polished version follows (L7+ "Ajani reached for the fifth pageâ€¦"). |
| L47 | C | `*This is it. I barely have ten seconds, I think. I hope it's enough.*` â€” bare asterisk thought â†’ single quotes (or thought-block per J2). |

---

## 3. Canon-Rule Compliance

### 3.1 king/King rule
69 lines contain king/King. **68 compliant.** Lowercase usages are uniformly determiner/possessive/generic/apposition ("the king", "my king", "his king", "its king", "our young king") â€” all correct, including direct address ("my king"). Deviations:

| Location | Text | Fix |
|---|---|---|
| arc5-01 L359 | "the Humman **King** thinks he is attackingâ€¦" | â†’ lowercase (determiner + modifier). Mechanical. |
| arc5-22 L83 | "the reign of **King Ajani Brightmane**" | Correct (title + name). No action. |

### 3.2 Humman/Hummans race name
Census (polished + draft text): **Humman Ã—118, Hummans Ã—20** (canon, double-m) vs **single-m Ã—2**:
| Location | Text | Fix |
|---|---|---|
| arc5-06 L190 | "GENERAL OF THE **HUMANS**!" (all-caps, Tamsin's shout) | â†’ HUMMANS. Mechanical. |
| arc5-13 L32 | "Open the gates for the **humans**" | Inside A-class draft block â€” resolved by deletion. |

Compliance 138/140 = 98.6% (99.3% counting the deleted-block hit as resolved). Rest-of-corpus check: canon "Humman(s)" dominates everywhere (1,924+ occurrences outside arc5).

### 3.3 Dialogue formatting
- **Double quotes:** ASCII straight quotes throughout (curly count = 0), matching site style. Every file's quotes balance (cross-line walker: 22/22 OK, zero open-across-blank, zero EOF-imbalance).
- **Crossed delimiters (`*â€¦'` / `'â€¦*`):** **zero** in all 22 files.
- **Single-quote odd lines:** 20 flagged by the walker â€” all verified as plural-possessive apostrophes (scorpions', riders', wolves', months', Wohs', Cloaks'â€¦). Zero genuine.
- **Contractions:** zero missing-apostrophe defects. Both flagged tokens verified false positives ("lies **ill**" â€” adjective; "This is **hell**" â€” noun).
- **Standalone lowercase i:** zero.
- **Thought delimiters (canon: single quotes ONLY):** deviations listed in Â§2 â€” asterisks: arc5-02 L11, L49; arc5-03 L92 (inscription), L171 (remembered speech); arc5-16 L92 (deleted with block); arc5-21 L10; arc5-22 L47. Underscores (novel in Arc V): arc5-11 L25, L171. Precedent note: `chapter-arc4-06.md` uses `thought-block` + `*â€¦*` Ã—5 â†’ J2.
- **Speech-in-speech-line integrity:** 3 narrative-prose-in-speech-line wraps (D-class, Â§2).

### 3.4 Em dashes
Census: **446 em dashes, 0 en dashes, 0 horizontal bars, 0 ASCII-hyphen/en-dash dialogue openers.** Odd-count lines classified:

| Category | Count | Verdict |
|---|---|---|
| CUT (speech cutoff) | 20 | Canon âœ“ |
| TAIL (elaboration to sentence/line end) | 60 | Canon âœ“ |
| TAIL (empty â€” line ends on dash) | 1 | arc5-06 L7 "The gate was stillâ€”" â€” intentional narrative interruption by the next paragraph ("A flash. A thunder."). Valid âœ“ |
| OPEN-MID (suspect) | 105 | **All 105 manually reviewed** (`a5_openmid_review.txt`): every case is a single dash introducing an appositive/elaboration that runs to the end of its sentence; the regex trigger is merely the following next sentence. Per the Arc Iâ€“II reconciliation precedent, these are valid. **Zero genuine unclosed parentheticals.** |

**Em-dash verdict: fully compliant.** (Chapter-heading dashes â€” 22, from `sub_titles` â€” are scaffold and excluded from defect accounting.)

---

## 4. Umbrella Draft-Debris Inventory

Source of truth: `content/story/chapter-05.md` (2,275 lines). Mapping: split ch N line k (kâ‰¥3) â‰ˆ umbrella L(anchor_N + k âˆ’ 3). All items below were located by `a5_umbrella.py` + grep and verified by targeted reads. **Keep/delete column reflects the recommendation; all deletions are story-safe (canon evidence in Â§5).**

| Umbrella L | Split location | Type | Keep/Delete | Canon evidence |
|---|---|---|---|---|
| L1056â€“1070 (â‰ˆ) | arc5-07 L59â€“73 | Craft commentary ("seeded since the earliest chapters of the Ethra exercise", "we have established", "the reader should feel", "This scene also serves a structural purpose") | **DELETE** | Pure author voice; no story content; scene it annotates continues at arc5-07 L75+ |
| L1433 | arc5-11 L157 | AI-instruction: `*Then you should write the scene please (the Cefiro scene )*` | **DELETE** | Not narrative; the Cefiro scene itself exists (arc5-11 L118+, L225+) |
| L1666â€“1668 (â‰ˆ) | arc5-13 L31â€“33 | Draft scene-summary ("M'rak asked everyone presentâ€¦ Zephyr said, 'Open the gates for the humansâ€¦'") | **DELETE** | Gate-opening beat retold in canon form at arc5-14 L24â€“31 (Tamsin: "OPEN THE GATES! THOSE ARE MY PEOPLE!") |
| L1704 | arc5-15 L3â€“5 | Draft stage-direction ("â€¦it couldn't quite control it's body, M'rak yells 'ALL CANNONS FIRE!!!! FIRE THE RAY!!!! NOW!!!'") | **DELETE** | Polished take at arc5-15 L35â€“61 (canon take B, Â§5) |
| L1827â€“1867 | arc5-16 L67â€“107 | Third copy of cannon/reform block + re-hashed ray/wolf sequence + duplicate 11:50 boilerplate | **DELETE** | Canon sequence = arc5-16 L27â€“65; verbatim duplicates of L1707â€“1755 umbrella block (Ã—3 census) |
| L1869â€“1871 (â‰ˆ) | arc5-16 L109â€“111 | Draft scene-summary with "Back to M'rak." stage direction | **DELETE** | Polished scene at arc5-17 L11â€“35 (twenty-first pillar, Solen's descent, "Golden what?", legend exposition) |
| L1910 | arc5-18 L3â€“5 | Draft stage-direction ("The light walk begins to crackâ€¦ cleaves trough the sandâ€¦ postrated") | **DELETE** | Polished version arc5-18 L7+ (wall falls, ray fires) |
| L1996 | arc5-18 L89â€“91 | Draft stage-direction ("Ajani lands on the wall shouting 'STATUS STATUSâ€¦' Al around solen turns to ajaniâ€¦") | **DELETE** | Polished version arc5-18 L93â€“105 (identical beats, correct spelling) |
| L2024 | arc5-19 L3â€“5 | Draft stage-direction ("Ajani says 'crap'â€¦ beseeschsâ€¦ zephyr saysâ€¦") | **DELETE** | Polished take at arc5-19 L43â€“79 (canon take B, Â§5) |
| L2194 | arc5-22 L3â€“5 | Draft stage-direction ("Ajani tores a fifth pageâ€¦ chants visibily strainedâ€¦ tores a sixth page") | **DELETE** | Polished version arc5-22 L7+ ("Ajani reached for the fifth pageâ€¦") |

Also in umbrella (context, no action needed for Arc V): duplicate scene blocks at L75â€“143/L145â€“233 (war room), L237â€“292/L293â€“376 (Council), L600â€“633/L635â€“670 (dome), L925â€“949/L951â€“967 (aftermath+tent), L1457â€“1475/L1477â€“1499 (civilian army), L1707â€“1733/L1735â€“1761 (cannon volley), L2027â€“2051/L2063â€“2087 (five-minute sequence); duplicate formulaic openers at L1733/L1761 and L1825/L1867. Heading inventory: only `# Chapter 5: The Great War` (L1); no bold scaffold lines; no "Version A/B", "Corrected", "Montage", "Let me rewrite" markers (Arc V's debris style is stage-directions and craft essays, not Arc Iâ€“II's correction markers).

## 5. Duplicate Blocks with Canon Designation

| # | Location (split lines) | Takes | CANON designation | Evidence |
|---|---|---|---|---|
| B1 | arc5-01 L74â€“142 vs L144â€“232 | A: later-timeline report (vanguard destroyed, third wave) Â· B: Vasha's 5:25 entrance | **Take B** | Chapter title "05:25 â€” Vasha Storms In"; take B contains the storming-in scene (L146) and Vasha's full assessment (L229); take A's scout numbers belong to a later moment and break the 5:25 frame |
| B2 | arc5-01 L236â€“291 vs L292â€“375 | A: full member introductions + longer Vasha speech Â· B: Kellan-centric, tighter | **JUDGMENT (J1)** â€” recommend B spine + optional restore of A's introductions | Both takes contain unique material; B flows into the tent scene (L376) and ends with Kellan's reaction; A's member intros (Maren, Sylen, Toren) are the only unique lore |
| B3 | arc5-03 L51â€“86 vs L87â€“122 | A: mirror from capital's founding / 3,000 yrs Â· B: High-Speaker lineage since Third Tyrant | **Take B** | Positioned directly before Mekhmed's reaction to the dome (L123 "had just swallowed the Wengari capital whole"); richer lore; final paragraph of both takes is identical (L85 = L121), so B's continuation is seamless. Note take-B L92 asterisk-inscription fix (Â§3.3). Lore conflict between takes (3,000 yrs vs Third Tyrant era) resolves in B's favor |
| B4 | arc5-06 L135â€“159 vs L161â€“177 | A: adds premature messenger ("The Woh riders had arrived") Â· B: tent scene only | **Take B** | Timeline: at 08:20 reinforcements are still hours out (they arrive 10:35â€“11:50, ch12â€“16); B flows directly into Tamsin's approach (L178â€“190) |
| B5 | arc5-11 L181â€“199 vs L201â€“223 | A: M'rak's long rallying speech Â· B: delegation to Tamsin | **Take B (pending J4)** | B integrates Tamsin's redemption arc (she trains the civilians, L221), reuses the established line "If the wall falls we all fall" (echoed at L202), and matches the shorter, exhausted-commander register of the moment |
| B6 | arc5-15 L7â€“33 vs L35â€“61 | A: includes ray fire at 11:40 Â· B: cannons only | **Take B** | Ray chronology: arc5-16 L30 "How long for the ray?! Three minutes!" (11:50) and arc5-18 "11:59 â€” Nefere Fires" prove the ray cannot have fired at 11:40 |
| B7 | arc5-16 L67â€“107 (+draft L109â€“111) vs L27â€“65 | single canon sequence + redundant re-hash | **L27â€“65** (the absolution sequence matching the chapter title "Vows Are Absolved") | Re-hash repeats ch15 text verbatim, contradicts itself (point-blank cannons then "two leagues away"), and the chapter ends cleanly on the L65 boilerplate after deletion |
| B8 | arc5-19 L7â€“41 vs L43â€“79 | A: merged spear â†’ fire spirit Â· B: five-spear pentagon + page ritual | **Take B** | B's page-ritual structure is what ch20â€“22 continue ("third page" L2135 umb., "fifth page" arc5-22); B fixes A's self-contradictory "12:02 in the morningâ€”noon" to "afternoon" (L79); B is the superset in staging detail |

## 6. Remediation Classification

**Guarantee (as in the Arc Iâ€“II report):** every recommended edit is (1) a character-level mechanical fix from a closed map, (2) a deletion of author meta-text/draft-instruction, or (3) a deletion of one of two near-identical takes keeping the canon-designated one. No new prose, no dialogue rewording beyond capitalization/delimiter fixes. All fixes target `content/story/chapter-05.md`, then `regenerate_chapters.py` re-splits (round-trip byte-identity proven in Â§6b).

### 6.1 Mechanical (scriptable, closed map) â€” 8 items
| # | File (split) | Umbrella (â‰ˆ) | Fix |
|---|---|---|---|
| M1 | arc5-01 L359 | L358 | `the Humman King thinks` â†’ `the Humman king thinks` |
| M2 | arc5-06 L190 | L980 | `GENERAL OF THE HUMANS` â†’ `GENERAL OF THE HUMMANS` |
| M3 | arc5-02 L11 | L419 | `*We can't win against four hundredâ€¦*` â†’ `'We can't win against four hundredâ€¦'` |
| M4 | arc5-02 L49 | L457 | `*We cannot hold.*` â†’ `'We cannot hold.'` |
| M5 | arc5-11 L25 | L1301 | `_This is hell. I've stepped into hell._` â†’ `'This is hell. I've stepped into hell.'` |
| M6 | arc5-11 L171 | L1447 | `_Can we win with that?_` â†’ `'Can we win with that?'` |
| M7 | arc5-22 L47 | L2237 | `*This is it. I barely have ten secondsâ€¦*` â†’ `'This is itâ€¦'` |
| M8 | arc5-03 L92, L171 | L640, L719 | asterisk inscription/memory â†’ double quotes (`"You will never use thisâ€¦"` / `"Stay here. Stay hiddenâ€¦"`) |

(Conditional on J2 = "enforce canon": add arc5-21 L10 â†’ `'Just two moreâ€¦'` keeping or dropping the thought-block div per J2 wording. Conditional on J3: 2Ã— `Bright Mane` replacements.)

### 6.2 Editorial (judgment deletion / reformat) â€” 13 items
| # | Item | Action |
|---|---|---|
| E1â€“E9 | 9 Class-A debris blocks (Â§4 table) | Delete listed umbrella line ranges; verify adjacent paragraphs still flow (all verified: polished versions exist or scene continues) |
| E10 | arc5-01 war-room take A (umbrella â‰ˆL73â€“141) | Delete; keep take B (â‰ˆL143â€“231) |
| E11 | arc5-03 dome take A (umbrella â‰ˆL599â€“633) | Delete; keep take B (â‰ˆL635â€“669) |
| E12 | arc5-06 take A (umbrella â‰ˆL925â€“949); arc5-15 take A (umbrella L1707â€“1733); arc5-16 re-hash (umbrella L1827â€“1871); arc5-19 take A (umbrella L2027â€“2051) | Delete; keep canon designations Â§5 (B4/B6/B7/B8) |
| E13 | arc5-11 take A (umbrella â‰ˆL1457â€“1475) | Delete pending J4 confirmation |

Formatting-only (optional, no story impact): restructure speech-line-wrapped narrative at arc5-09 L4, arc5-12 L44, arc5-11 L218 into prose + `span.speech`/dialogue-block pattern (D-class, 3 items).

### 6.3 Judgment items (need Ainz-sama's decision) â€” 4 items
| # | Question | Recommendation |
|---|---|---|
| J1 | arc5-01 Council of the Untrustworthy: take A vs take B? | Ratify merge: keep take B (umbrella â‰ˆL293â€“376) as spine; optionally splice in take-A's council-member introduction paragraph (umbrella â‰ˆL240â€“246 region) before Vasha speaks. If no merge is wanted, keep B alone. |
| J2 | Thought presentation: enforce single-quote canon strictly, or ratify Arc IV's `thought-block` + `*â€¦*` pattern as a sanctioned style? | Enforce canon (single quotes) for bare asterisk/underscore thoughts regardless; for thought-block-wrapped thoughts (arc5-21 only in Arc V), either normalize or ratify â€” but decide corpus-wide, since arc4-06 has 5 instances. |
| J3 | "the young Bright Mane soldier" (arc5-02 L29, arc5-05 L19): intended name/term? | Corpus has Brightmane Ã—291 and no other "Bright Mane". If Irek is of the royal house â†’ `Brightmane`; if it describes his family unit â†’ `Bright Paw` (he fights among Bright Paw guards); if an epithet â†’ lowercase `bright-maned`. Ask Ainz-sama; default `Brightmane`. |
| J4 | arc5-11 civilian-army scene: keep take A's M'rak speech or take B's Tamsin delegation? | Take B (canon evidence Â§5-B5). |

---

## 6b. Chapter-Boundary Check Results

**Part 1 â€” Regeneration round-trip (consistency with umbrella).** Rebuilt all 22 splits in-memory from `chapter-05.md` using the exact `regenerate_chapters.py` algorithm (line-anchor â†’ char-offset conversion, heading injection from `arcs.json â†’ sub_titles`, `## Chapter` dedup). Result: **22/22 MATCH â€” byte-identical.** Consequence: every fix must be applied to the umbrella, then regenerated; no split-only patching is possible or needed.

**Part 2 â€” Boundary integrity (sentence/clause cuts).** For each of the 21 boundaries, the last prose line of chapter N and the first prose line of chapter N+1 were inspected (`a5_boundary.txt`):

- **22/22 chapters end on sentence-final punctuation** (period, quote-close, or a deliberate dash-cutoff at ch06-internal L7 only). Zero mid-clause cuts.
- Div balance: every file's `<div class="dialogue-block">` opens equal closes (verified per file).
- Every chapter opens with a fresh sentence after its generated heading.
- Notable (all intentional, no action): ch08 ends inside a dialogue block whose scene resolves in ch09's opening line ("He did not need to say who 'he' was"); ch19â†’20 and ch21â†’22 cut between consecutive minutes of the same battle (12:02â†’12:03, 12:05â†’12:06) by design.
- **Timestamp convention check:** heading timestamps denote the chapter's key event, verified consistent (ch18 "11:59 â€” Nefere Fires": body runs 11:55â†’11:59 fire; ch21 "12:05 â€” The Light Cage Fades": body runs 12:04â†’12:05 fade). Non-monotonic headings ch02 (06:55) â†’ ch03 (06:25) are an intentional POV rewind (parallel scenes in two war rooms), not a defect.

**Verdict: PASS â€” no boundary remediation needed.**

### Cross-audit observations (out of Arc V scope, recorded for the record)
- `chapter-arc4-06.md` contains a self-duplicated thought-block (L27â€“29 = L71â€“73) and five asterisk-thoughts â€” recommend folding into the next arc-level audit.
- `content/story/chapter-04.md` L2250 carries a possible author-meta line ("the adoption ritual you wrote") â€” flagged, not audited here.

## 7. Status

- [x] Report skeleton written (interruption resilience)
- [x] Tool battery adapted to 22-file list in `QA/arc5_tooling/` (originals untouched); all lints + census + classify + boundary + umbrella scans run
- [x] Spot-verification passes (draft blocks, duplicate takes, thought delimiters, king/King contexts, hum variants, OPEN-MID review of all 105 lines, umbrella line numbers via grep)
- [x] Sections 1â€“6b filled
- [x] **FINAL**

**Method note:** no story file was modified; all work products are this report plus `ethra_site/QA/arc5_tooling/` (scripts + outputs). Pending Ainz-sama's decisions on J1â€“J4, the remediation pass is fully specified (Â§6 tables) and mechanically executable against the umbrella.




---

# PART IV - ARC VI AUDIT REPORT (verbatim)

# Ethra QA Report â€” Arc VI ("Aftermath & The Road") PROACTIVE Audit

- **Prepared by:** Demiurge's audit subagent â€” script-first QA audit using the Arc Iâ€“II defect battery (`QA/*.py`, copied & adapted into `QA/arc6_tooling/`).
- **Date:** 2026-08-24
- **Scope:** `content/story/chapters/chapter-arc6-01.md â€¦ chapter-arc6-05.md` (published splits, primary targets) + `content/story/chapter-06.md` (umbrella master, 495,904 B; grep + targeted line reads only). READ-ONLY throughout â€” no story content modified.
- **Mode:** PROACTIVE â€” no reader feedback exists for Arc VI; defect battery per `QA/arc1_arc2_reader_feedback_report.md`.

### File state at audit time (recorded timestamps)
| File | Size | Last modified | Note |
|---|---|---|---|
| chapter-06.md (umbrella) | 495,904 B | **2026-08-23 17:51** | most recently touched umbrella in corpus |
| chapter-arc6-01.md | 90,556 B | **2026-08-23 17:51** | re-touched same minute as umbrella |
| chapter-arc6-02.md | 103,268 B | 2026-06-27 19:38 | |
| chapter-arc6-03.md | 102,345 B | 2026-06-27 19:38 | |
| chapter-arc6-04.md | 101,328 B | **2026-08-23 17:45** | re-touched 6 min before umbrella |
| chapter-arc6-05.md | 103,032 B | 2026-06-27 19:38 | |
| chapter-06.md.bak.before_pass1 | 514,876 B | 2026-06-16 23:35 | backup exists; **existence noted only, NOT audited** |

> **Recent-modification note:** arc6-01, arc6-04 and the umbrella were modified 2026-08-23 between 17:45 and 17:51; the umbrella shrank ~19 KB vs its pre-pass1 backup, i.e. a **pass-1 cleanup already ran** (explicit "Let me rewriteâ€¦"/"Here is the correction" markers now 0 hits). This audit covers the CURRENT residual state.

- **Artifacts:** `QA/arc6_tooling/` â€” arc6_lint.py (+results JSON/summary), arc6_quote_pair.py (+.txt), arc6_delim_cross.py (+.txt), arc6_em_classify.py (+.txt), arc6_tally.py (+.txt), arc6_hyphen_audit.py (+.txt), arc6_umbrella_scan.py (+debris .txt/.json).
- **Status:** see Â§7.

---

## 1. Executive Summary

Arc VI's **polished prose is canon-healthy** (king/King â‰ˆ fully compliant; em-dash usage â‰ˆ fully compliant; Ajani's thoughts single-quoted throughout; no missing-apostrophe contractions in polished text) â€” but the arc is the **dirtiest in the corpus for draft debris**: whole draft/synopsis beats, author directives, craft-feedback blocks and duplicated scene versions were published inside all five chapters and remain in the umbrella master.

**Counts by defect class (full detail Â§6):**

| Class | Count | Nature |
|---|---|---|
| MECHANICAL (scriptable closed map) | **59 fixes** | 1 missing opening quote (arc6-01 L641, root cause of whole-file quote imbalance) Â· 4 "king of the Wengari/humans" formal-title capitalizations Â· ~50 single-m `human(s)` â†’ `Humman(s)` (concentrated: arc6-03 â‰ˆ 35) Â· 2 lowercase `humman(s)` capitalizations Â· 2 `again.M'rak`/`with it.The` concatenations (both inside blocks already slated for deletion) |
| DEBRIS (author meta-text â€” delete) | **~62 individual lines + 12 blocks (â‰ˆ 350â€“400 lines total)** | draft beats, synopsis beats ("We are in the gardensâ€¦"), author directives ("*I like it, let's write it*"), planning notes, craft-feedback paragraphs (one block duplicated across arc6-03 AND arc6-04), scaffold headings (**The Halberd User (Nikolai)** etc.), 6 duplicated scene versions |
| EDITORIAL (judgment deletion/reword) | **7 items** | draft-format lines carrying unique scene content (need reword, not just delete); V1/V2 scene-version selection with unique beats; thought-style consistency (Nikolai's `*...*` thought) |
| JUDGMENT (needs Ainz-sama) | **3 items** | J1 arc6-05 Maren-report V1/V2 contradiction Â· J2 arc6-04 dinner V1 unique beats salvage Â· J3 whether craft-note blocks are archived elsewhere before deletion |

**Top findings:**
1. **arc6-01 L641** â€” Cefiro's Sunraptor paragraph is missing its opening `"`; this is the single root cause of the whole-chapter quote imbalance (file total 395 double quotes = odd). One-character mechanical fix.
2. **Six duplicated scene blocks published in full**: arc6-02 Kyre-Tree scene Ã—2 (canon = 2nd); arc6-03 L'vat strike scene Ã—3 (canon = 3rd); arc6-04 Snow-Paw dinner Ã—2 + Nikolai laugh Ã—2 (canon = 2nd each); arc6-05 M'rak exaltation reactions Ã—2 + Tamsin investiture Ã—2 (canon = V2, proven by downstream refs to "Knight of the Golden Claw").
3. **arc6-03 carries ~35 single-m `human(s)` tokens in polished prose** â€” the largest Humman-spelling concentration in the arc (e.g. L120, L226, L252, L307, L384, L491, L641, L831).
4. **Craft-feedback blocks published as story text**: arc6-02 L779â€“790; arc6-03 L866â€“891; arc6-04 L1148â€“1190 (the arc6-03 block copied verbatim + extras) and L1230â€“1264 (scaffold headings **Feedback on the Combat Choreography**/**The Halberd User (Nikolai)**/**The Four Pillars User (Ajani)**/**The Verdict**); arc6-05 L133â€“140, L295â€“316, L378â€“406, L684â€“708.
5. **Umbrella chapter-06.md retains ALL of the above** (pass-1 removed only explicit rewrite markers) â€” fixes must be applied to the umbrella, then re-split.

**Arc health verdict:** NOT reader-ready. The underlying polished narrative is high quality and nearly canon-clean, but ~12â€“15% of published arc text is non-story material. Remediation is overwhelmingly mechanical deletion + one closed map (Humman spelling); the judgment items are few and well-bounded.

---

## 2. Per-Chapter Defect Catalog

Line numbers refer to the published split files. "Polished twin" = the rewritten version that makes the flagged line deletable.

### 2.1 chapter-arc6-01.md (90,556 B)

**Debris (author meta / draft formatting):**
- **L123** â€” draft beat: `Next scene beats >When all have said their piece Lira speaks angrily "WHAT !? I THOUGHT THE WENGARI AND THE HUMMANS WERE BROTHERS..."` (polished twin L134).
- **L197** â€” draft-format Ajani line in `speech-line` markup: `"well now that's out of the way, I need the talky, M'rak..."` â€” **carries unique scene content** (the "how many did we lose" question); no polished twin found â†’ EDITORIAL reword (J4).
- **L313** â€” draft hybrid `'hmm the council worked as designed I'll need to reward them...' - "The resignation is not accepted..."` (single-quote thought + `' - '` separator; lowercase).
- **L443** â€” draft hybrid `'so these are the ones' - "So you are the ones who unleashed Velarius madness..."` (lowercase `velarius`).
- **L485** â€” draft-format Ajani line: `"Ambassador these are your people, deal with them as you see fit..."` (uncapitalized start, run-on).
- **L905** â€” author directive: `*Now let's see Yvaria, Reva, lira and vex*` (lowercase names).
- **L963** â€” draft hybrid: `'its worse than I thought ' - 'call for Maren please'` (missing apostrophe `its`â†’`it's`; both segments single-quoted).
- **L1042** â€” draft beat: `'theyre brutes, brutes !' - "Generals I meant from Verdantis not the humans currently in the city..."` (polished twin = arc6-02 L4; note the twin also carries single-m "humans").

**Mechanical defects (polished text):**
- **L641** â€” Cefiro's Sunraptor paragraph: closing `"` present, **opening `"` missing** (also not wrapped in dialogue-block like neighbours). Root cause of whole-file quote imbalance. Fix: prepend `"` (MECHANICAL).
- **L192** â€” formal title lowercase: `...holder of Luxor, king of the Wengari.` â†’ `King of the Wengari` (canon rule 1).
- **L1011** â€” `"Generals it appears we will need to ask for reparations from the hummans...what is your recommendations for achieving so ?"` â€” lowercase `hummans`; grammar `what is your recommendations` â†’ EDITORIAL reword.

**Quote balance:** ascii double quotes = 395 (odd) â†’ walk desyncs from L641 to EOF (`arc6_quote_pair.txt`); single root cause above.

**king/King:** compliant apart from L192. **Em dashes:** all CUT/TAIL/elaboration uses canon-compliant. **Ajani thoughts:** single-quoted in all draft lines (L147, L313, L443) â€” no asterisk thoughts.

### 2.2 chapter-arc6-02.md (103,268 B)

**Debris:**
- **L176** â€” draft beat: `After the meeting ajani goes down to the inner chamber , and extends his hand to the flower "I'm here this is what happened"...` (polished twin L180+).
- **L352** â€” draft-format promotion speech (`"I am promoting these four to two star generals..."`; lowercase `hummans coin`, `wengari`; run-on) â€” verify polished twin before delete, else reword (J4).
- **L486** â€” author directive: `*Let's look at the immediate aftermath of ajani leaving the room, Seris is waiting outside...*`
- **L489** â€” synopsis beat: `We are in the gardens, Cefiro tells Ajani he's seen enough and he must return home...`
- **L585** â€” draft beat: `after the war council ajani tells Cefiro to rest but before Cefiro takes his leave, ajani takes out his royal seal...`
- **L672** â€” synopsis beat: `We are in the throne room the very next day, Ajani is meeting with seris in a visibily more relaxed maner...` (typos `visibily`, `maner`; lowercase `ajani`, `seris`, `sylva`, `hummans`).
- **L779â€“790** â€” craft-feedback block (4 paragraphs): `The chapter is working on all three fronts you've identified.` + analysis of the Humman reaction, the interrogation, Ajani's behavior. Contains cross-chapter copy sentence `her questionâ€”'if you are truly sorry, why did you not chase after mekhmed?'â€”is the blade that cuts through the paper shield.` (also in arc6-03/arc6-04 blocks).
- **L895** â€” author directive: `*You can write the next scene you have full creative authority it should be a few hours later seris questioning salahim outside the gate*`
- **L898** â€” draft beat: `Seris goes to report to ajani he was waiting inside the gates leaned on a wall...`
- **L948â€“988** â€” **Kyre-Tree scene V1** (duplicate). Opens directly with `*You are here again. You have questions. Ask.*`; its tail `*The memorial celebration will bring pilgrims...*` (L987) is folded into V2's closing paragraph L1040. **Canon = V2 (L992â€“1041)**, which has the descent transition (L992), Ajani's spoken line (L996) and the consolidated ending. Debris between: **L990** author approval `*I like it, let's write it*`.

**Mechanical defects (polished text):**
- **L4** â€” `Not the humans currently in the city. The Hummans have more than one city...` â€” single-m `humans` mixed with correct `Hummans` in one breath â†’ `Hummans` (MECHANICAL).
- **L710** â€” `A human dismounted from the lead hawk.` â†’ `A Humman` (Sultan's party = Hummans).
- **L714** â€” `I am the great Sultan Salahim, king of the humans.` â†’ `King of the Hummans` (formal proclamation title + spelling; MECHANICAL, 2 fixes in line).

**Consistency notes (not hard rule-3 violations â€” rule covers Ajani):** L693 shared Wengari+Humman thought in `*...*` (`*Not again. Please, not again.*`); Tree telepathy `*...*` (L208â€“225) is the established canon format for the Tree. See Â§6.3 J3.

**king/King:** `Sultan Salahim` (title+name) correct; `king of the humans` L714 flagged above. **Em dashes:** compliant (L782/L785 are inside the craft block slated for deletion).

### 2.3 chapter-arc6-03.md (102,345 B)

**Debris:**
- **L78** â€” synopsis beat: `A few hours later ajani is helping everyone on the wall, he explains that he can feel where the wall is weakest...` (`theyre`, lowercase `ajani`).
- **L133** â€” draft beat: `Then without warning the lament extends a limb and touches ajanis forehead, a light passes between them then too fast for anyone to react it snaps the back of ajanis head...` (`slawjacked`).
- **L137â€“190** â€” **L'vat strike scene V1** (duplicate): `The Lament's limb touched Ajani's forehead` â€¦ `STUPID DISCIPLE!` â€¦ `It always is with you. Explain. Now.` (L190).
- **L194â€“228** â€” **L'vat strike scene V2** (duplicate): `Then L'vat spoke. His voice was not the booming shout...` â€¦ `Tell them the humans fought on the wall.` (L226).
- **L230â€“272** â€” **L'vat strike scene V3 = CANON** (final rewrite; `The Deep felt the elements shift`; resolves with `Stand down. The White Dawn vouches for them.` L272). Even canon V3 carries single-m fixes: L230, L252, L256, L262, L267.
- **L277** â€” draft beat: `We see a humman mother and daughter can't be more than four hugging each other...` (polished twin L281+, which carries `humman woman` lowercase fix).
- **L318** â€” draft line: `Ajani very flustered says "I apologize for our guests humman cubs are very curious she meant no offense"...` (polished twin L323 â€” which carries single-m `Human cubs` fix).
- **L610** â€” draft beat: `*Ajani has returned to the throne room for the afternoon, the threx are touring the city like children...*`
- **L710** â€” draft line: `Ajani looks towards sylva and says "call for zephyr and Yvaria, tell them its urgent"` (`its`â†’`it's`).
- **L765** â€” draft beat: `"Ambassador please tell them Wich direction to take" , we move three days ahead the threx are getting ready to...` (`Wich`).
- **L866â€“891** â€” craft-feedback block (9 paragraphs: L866, L869, L871, L875 [inside a dialogue-block div], L879, L881, L884, L888, L891). **Duplicated verbatim into arc6-04 L1148â€“1171** (see Â§5.7).
- **L895** â€” synopsis beat: `Let's now follow Cefiro and Kira, they are lost again Kira is chastising Cefiro "YOU SAID YOU REMEMBERED THE WAY!!"...`

**Mechanical defects (polished text):** ~35 single-m `human(s)` tokens â€” the arc's worst cluster. Key lines: L120 (`'The humans fought on the wall,' L'vat said flatly. 'The humans fought on the wall. Tell them.'`), L128, L161, L217, L221, L226, L230, L252, L256, L262, L267, L307, L323 (`Human cubs`), L351, L356, L384, L403, L407, L416, L420, L491 (`To a human, they were cheap souvenirs`), L511, L578, L583, L641 (`Humans and Wengari fighting side by side`), L735, L773, L802, L831. Plus capitalization: **L281** `The humman woman was perhaps thirty` â†’ `Humman woman`.

**king/King:** fully compliant â€” the single capitalized `King` in the chapter is **L606 `King Ajani`** (title+name, canon).

### 2.4 chapter-arc6-04.md (101,328 B)

**Debris:**
- **L36â€“145** â€” **Snow-Paw dinner scene V1** (~110 lines, duplicate). Contains the Velarius-knowledge inconsistency (`L87 ...deployed weapons from Velarius.` â€” Snow Paws are isolated, cannot know Velarius) plus a dangling mid-sentence dash at **L41** (`...if she was tired, if she had ever seen a white bear, if sheâ€”` paragraph ends there). **Canon = V2 (L149â€“313)** â€” V2 removes Velarius, adds the Snow-Paw interruptions demanded by the corrections note, and flows into the arena scene. V1 carries unique beats (see J2).
- **L146** â€” author directive: `*We follow them to the dinning room Ivan is trying very hard...*` (typo `dinning`).
- **L315** â€” author corrections note: `*/corrections 1) the snow paws are isolated they don't have idea who Velarius is... if you agree let's rewrite the scene*` â€” its demands ARE implemented by V2; note is debris (out of place after V2).
- **L318** â€” draft beat: `Before they have taken ten paces Kira takes out her Wooden saber and shouts "TAKE THAT BACK!, NO ONE CAN BEST AJANI!!"...` (polished twin L323+).
- **L641** â€” draft beat: `Later at night Nikolai ask Cefiro 'so, the Truth son, when do we meet with Ajani ?'...` (polished twin L649+).
- **L715** â€” draft beat: `The next day at breakfast Nikolai announces 'today we start teaching the kids !...'` (`kiras`; polished twin L719+).
- **L1101** â€” author directive: `*Let's follow them in the journey we learn Nikolai like Ivan is a fan of the wurms...*`
- **L1105** â€” draft beat: `The journey is uneventful , Kira learns snow paw history and customs and is surprised to learn Nikolai's grandfather was humman...`
- **L1148â€“1190** â€” craft-feedback block: the arc6-03 block copied verbatim (L1148, L1152, L1154, L1158 [inside dialogue-block div], L1162, L1164, L1167, L1171) + arc6-04 extras (L1174 Cefiro/Kira journey, L1176, L1179 lore drops, L1181, L1184, L1188, L1190).
- **L1194** â€” draft beat: the full sparring fight as one run-on synopsis ending in the lowercase salute `This Ajani brightmane... king of the wengari salutes Nikolai silver pelt... welcome home uncle` (polished twin L1202â€“1226).
- **L1221** â€” **Nikolai laugh V1** (`A long silence. Then Nikolai threw back his head and laughedâ€”...` ending `The Snow Paws are honored to come home."`). **Canon = L1226 V2**, which adds the formal salute (`Nikolai Silverpelt, champion of the frozen wastes... salutes Ajani Brightmane...`).
- **L1230â€“1264** â€” scaffold block: headings `**Feedback on the Combat Choreography**`, `**The Halberd User (Nikolai)**`, `**The Four Pillars User (Ajani)**`, `**The Verdict**` + analysis paragraphs (L1236, L1243 `When Ajani dodged sideways, Nikolai switched to a wide sweep. This is correctâ€”a sweep converts...`, L1246, L1253, L1264).
- **L1270** â€” draft beat: `Everyone cheers for Ajani everyone but l'vat who approaches and unceremoniously starts critiquing him...` (polished twin L1305â€“1321).

**Mechanical defects (polished text):**
- **L247** â€” Tyrant list: `The Fifth was Velarius Vane. Human.` â†’ `Humman.` (race-name label parallel to `Veylar`, `Bright Paw`).
- **L256** â€” `...the last of them was human. The weakest race on Ethra produced the worst monster.` â†’ `Humman` (MECHANICAL; in-character but race-name).
- **L266** â€” `A human nearly destroyed the Wengari. We remember.` â†’ `A Humman`.
- **L1216** â€” polished salute: `...caller of spirits, king of the Wengari, salutes Nikolai Silverpelt...` â†’ `King of the Wengari` (formal title; MECHANICAL).
- **L1226** â€” `...salutes Ajani Brightmane, first of his name, White Dawn, king of the Wengari.` â†’ `King of the Wengari`.

**Consistency note:** L1321 Nikolai's thought in `*...*` (`*That's an incomplete form,* he thought.`) â€” rule 3 binds Ajani only; flag for J3. L528â€“530 Kira's remembered Ajani-lesson: quoted speech inside `*...*` across a blank line â€” file-level quote balance OK; stylistically fine, note only.

### 2.5 chapter-arc6-05.md (103,032 B)

**Debris:**
- **L129â€“140** â€” planning block: L129 `Now we enter a sub arc "the great cÃ©lÃ©bration !!" It will be exposition heavy and light hearted, I'll cover a month`; L133 `The Great Celebration is the right structural choice...`; L137 political-function paragraph; L140 `I am ready to begin whenever you are. What is the first beat of the Great Celebration?` (assistant dialogue).
- **L144** â€” synopsis beat: `It's the afternoon of the same day everyone has already settled in the throne room ajani is meeting with sylva...`
- **L238â€“248** â€” **Maren report V2 fragment** (duplicate start of the scene; see J1). V1 = L165â€“234 (complete, ends `The court dispersed into the afternoon light...`).
- **L253** â€” synopsis beat: `Ok next one is a MASSIVE scene, we start from the palace it's early morning an hour before dawn ajani is wearing an uncharacteristic black robe... 40 coffins...`
- **L295â€“316** â€” funeral craft-feedback block (L295 silence, L298 multi-species procession, L304 speech analysis [inside speech-line markup], L311 not-turning beat, L314 â€” contains its own **internal duplication + concatenation** `...And the reader mourns with it.The scene earns its silence...`, L316 transition note).
- **L342** â€” synopsis beat: `*Ajani declared the day a mourning day. The city closed. The market stalls went dark...*`
- **L378â€“406** â€” throne-room craft-feedback block (L378 three-throne configuration, L383 Nikolai on the left, L401 coalition made visible, L404 diplomatic-tradition paragraph incl. real-world `English royalty visited the French court` gloss, L406?).
- **L410** â€” draft beat: `Ajani stands and sylva passes him a scroll he unrolls it and proclames 'Yvaria whisperwind, Sephyr flamebound, Reva firepelt, M'rak brightmane present yourselves to the crown!!'` (polished twin L418; note `Sephyr` vs canon `Zephyr`).
- **L466** â€” draft M'rak citation: `"For believing when no one believed, for being the first and last bulwark in the line of duty..."` (lowercase commas version). **Canon = L474** (periods/capitals version).
- **L493â€“511** â€” **duplicated polished M'rak block**: L493 is a concatenation defect (`...prepared to speak again.M'rak rose from his knees...` â€” the L470 paragraph glued without space), then L495 citation repeat, L499 tremor repeat, L504 Reva repeat, L508 Kira repeat. **Canon = L470â€“491** (first occurrence); delete L493â€“511.
- **L515** â€” draft Reva citation: `"For crossing the belt and the desert in one night, for bringing and doing more than anyone would have hope her to do, for standing where eveyeone else fell..."` (`hope her`, `eveyeone`; polished twin L524).
- **L576** â€” draft proclamation: `"My citizens I give you your generals the four heavenly generals of the wengari!!!..."` (polished twin L584 â€” which carries the single-m `humans` fix).
- **L609â€“651** â€” **Tamsin investiture V1** (duplicate): draft beat L609 (`Sylva hands another scroll to ajani he again unfolds if with a theatrical flair...`), L612 `A second scroll passed`, L617 call, L621â€“628 procession, L631 V1 citation (`You were our enemy... You held the gate alongside my soldiers...`), L639 title **`Stand, Tamsin, the Sun's Mercy, Honorary General of the Wengari!`**, L644 crowd+oath V1 (`I am not Wengari... This I swear.`), L648 `That is all we ask.` **Canon = V2 (L653â€“681)** â€” title **`Rise, Tamsin, the first and only Knight of the Wengari. Rise, Tamsin of the Golden Claw!`** â€” proven canon by downstream references: L721 `The Knight of the Golden Claw had been named.`, L739 `The Knight of the Golden Claw fought at the gate.`, L1135 `...the first Knight of the Wengari...`. (V2's `a third scroll` L653 vs V1's `A second scroll`: only one scroll precedes (the generals', L414) â€” V2 numbering is a minor continuity error â†’ EDITORIAL note.)
- **L684â€“708** â€” proclamation craft-feedback block (L684 template, L689 elemental naming, L692 M'rak elevation, L695 Tamsin structurally distinct, L700 theatricality, L702 template for the future, L708 diplomatic function).
- **L717** â€” draft beat: `Sylva hands another scroll to Ajani this one is black he reads 'Vasha of the stripe paws, Mira su walker of the Pyrinae present yourselves to the crown!!'` (polished twin L721+).
- **L771** â€” draft Mira citation: `"for inventing new ways to defend us in under a week, for defending us when even we didn't knew we need defending..."` (**Canon = L781**: `For inventing new ways to defend us in under a week. For defending us when even we didn't know we needed defending... Rise, Mira Sun-Walker.`).
- **L800** â€” synopsis beat: `As the spirits are high a war horn sounds from the gate, three dÃ©lÃ©gations are approaching...` (`dÃ©nies`-style French spellings recur).
- **L882** â€” synopsis beat: `Salahim had come to offer a veritable mother load : grain and timber and iron and cloth...`
- **L1034** â€” draft-style line in speech-line markup: `Nikolai turns and says utterly defeated "Come humman, and perhaps next time bring better guards ?" As he slowly very slowly walks back...` (polished twin L1038+).
- **L1173** â€” synopsis beat: `Ajani looks at Nikolai confused then to sulheim 'what is it that we are signing ?'...` (lowercase `sulheim` for Salahim).

**Mechanical defects (polished text):** single-m `human(s)` â€” L262 (`the humans carried their fallen`), L267 (`Humans emerged from the Humman quarter`), L273, L292, L322 (memorial pillar paragraph), L332 (`The human refugees`), L372 (`Wengari and human and Pyrinae alike`), L584 (proclamation: `Teach the treacherous humans in Verdantis a lesson`), L901 (Salahim: `I am Salahim, current Sultan of the Humans.` â†’ `Hummans`; also contradicts his arc6-02 self-title form â€” see Â§3.2).

**king/King:** compliant (no formal-title instances; lowercase generics correct).

---

## 3. Canon-Rule Compliance

### 3.1 king/King (rule 1)
Census (`arc6_tally.py`): arc6-01 King=3/king=47 Â· arc6-02 King=1/king=44 Â· arc6-03 King=1/king=65 Â· arc6-04 King=0/king=46 Â· arc6-05 King=0/king=26.
- **Zero** determiner violations (`the King`/`my King`/`a King`): none found anywhere.
- **Zero** lowercase-king-before-Name violations.
- The capitalized instances: arc6-03 L606 `King Ajani` (title+name â€” canon âœ“); arc6-01's 3 capitalized hits are `King of the Wengari`-context checks â€” **the deviations are the reverse direction**: formal proclamation titles left lowercase:
  - arc6-01 L192 `king of the Wengari` (Ajani's full-title greeting)
  - arc6-04 L1216 `king of the Wengari` (Ajani's salute to Nikolai)
  - arc6-04 L1226 `king of the Wengari` (Nikolai's salute to Ajani)
  - arc6-02 L714 `king of the humans` (Salahim's self-title; double deviation with spelling)
  â†’ **4 MECHANICAL capitalization fixes.** All other lowercase uses are generic/apposition/direct-address (`a king needs something bigger than a crown` arc6-04 L453; `the king's morning vigil` arc6-04 L1112) and are canon-correct.
- **Verdict: ~99% compliant; 4 fixes.**

### 3.2 Humman/Hummans (rule 2)
Census per chapter (`arc6_tally.py`, case-sensitive exact forms):
| File | Humman | Hummans | humman | hummans | human | humans | Human | Humans |
|---|---|---|---|---|---|---|---|---|
| arc6-01 | 19 | 4 | 3 | 3 | 5 | 6 | 0 | 0 |
| arc6-02 | 44 | 14 | 1 | 4 | 3 | 10 | 0 | 0 |
| arc6-03 | 33 | 12 | 5 | 3 | 12 | 37 | 1 | 1 |
| arc6-04 | 12 | 2 | 0 | 0 | 2 | 0 | 1 | 0 |
| arc6-05 | 18 | 26 | 3 | 0 | 4 | 17 | 1 | 2 |

- Correct forms (Humman/Hummans) dominate: 126+58 = 184 tokens.
- **Single-m spelling deviations** (human/humans/Human/Humans): 85 tokens total, but **~48 of them sit in draft/synopsis lines that get deleted with the debris**; **~50 remain in polished text** after debris removal, concentrated in **arc6-03 (~35)** â€” see Â§2.3 line list. Notable polished instances outside arc6-03: arc6-02 L4/L710/L714; arc6-04 L247/L256/L266; arc6-05 L262/L267/L273/L292/L322/L332/L372/L584/L901.
- **Lowercase double-m** (capitalization only): arc6-01 L1011 (`hummans`), arc6-03 L281 (`humman woman`); the rest are in draft lines.
- No Earth-gloss contexts anywhere in Arc VI â€” every single-m token is a deviation.
- Cross-chapter consistency note: Sultan Salahim styles himself `king of the humans` (arc6-02 L714) vs `Sultan of the Humans` (arc6-05 L901); both should converge on `King/Sultan of the Hummans`.
- **Verdict: the arc's largest mechanical defect class â€” ~52 fixes, all scriptable via closed map (humanâ†’Humman, humansâ†’Hummans, Humanâ†’Humman, Humansâ†’Hummans in the listed polished lines).**

### 3.3 Dialogue formatting (rule 3)
- **Speech in double quotes:** universal in polished text. **One hard defect:** arc6-01 L641 missing opening `"` (see Â§2.1) â€” sole cause of the file-level imbalance (395 = odd). All other chapters: file-level double-quote walk balanced (arc6-04's L528â€“530 flashback quotes balance across the paragraph break â€” legitimate).
- **Ajani's inner thoughts:** single-quoted everywhere they appear (`'hmm the council worked as designed...'` arc6-01 L313; `'this grows tiresome'` arc6-02 L37; `'well that's understandable, he is odd'` arc6-01 L147; `'so these are the ones'` arc6-01 L443). **No Ajani thought ever uses `*...*`.** Crossed `*...'`/`'...*` markup: **zero** across all five chapters (`arc6_delim_cross.py`: 0 CROSSED flags).
- Non-Ajani asterisk usage (Tree telepathy; Nikolai's thought arc6-04 L1321; shared thought arc6-02 L693; Blackie gesture arc6-02 L613) â€” see Â§6.3 J3.
- **Contractions:** 0 missing-apostrophe contractions in polished prose. All `dont/cant/wont/theyre/thats/its/ive` etc. hits are inside draft/synopsis lines (deleted with debris): arc6-01 L123/L197/L313/L963/L1042; arc6-02 L37/L672/L895; arc6-03 L78/L277/L318/L710/L765/L895; arc6-04 L318/L641/L715/L1105/L1270; arc6-05 L144/L253/L410/L515/L576/L800/L1034/L1173.
- **Standalone lowercase `i`:** 0 in polished text (all hits inside draft lines or roman-numeral false positives none).
- **Verdict: compliant apart from the single missing-quote defect + draft-line hygiene that deletion resolves.**

### 3.4 Em dashes U+2014 (rule 4)
Census (`arc6_em_classify.py`): arc6-01 em=216 Â· arc6-02 em=232 Â· arc6-03 em=217 Â· arc6-04 em=277 Â· arc6-05 em=287. Classification of odd-dash lines: CUT(speech) 43 Â· TAIL(elab/empty) 57 Â· OPEN-MID 159.
- Spot-verification of the OPEN-MID bucket shows **~all are canon case-3** (single dash introducing an elaboration that runs to sentence end), e.g. arc6-01 L103 `his accent distinctâ€”formal and unhurried, the voice of...`, arc6-04 L432, arc6-05 L531. The classifier's heuristic over-flags; manual sampling found **no unclosed mid-sentence dashes in polished text**.
- Paired parentheticals (canon case-2) used correctly, e.g. arc6-05 L1195 `The Threxâ€”the silent, shimmering Threxâ€”whom the Wengari had once driven...`.
- **No ASCII-hyphen/en-dash dialogue openers** (`arc6_hyphen_audit.py`: zero spaced hyphens outside draft `' - '` markers; all 109 unique word-word hyphen tokens are legitimate compounds/adjectives â€” burn-scarred, rune-glass, seventy-three, court-martial etc.).
- Scene-divider headings (`**Solen â€” The Temple**` arc6-02 L737 etc.) use em dashes as heading separators â€” deliberate formatting consistent across the corpus, not a defect.
- Two cosmetic anomalies, both inside debris blocks (no fix needed beyond deletion): arc6-04 L41 dangling paragraph-final dash (dinner V1); arc6-01 L99/L251 confirmed to be legit em-dash elaborations (console display artifacts â€” no ASCII hyphens).
- **Verdict: fully compliant.**

---

## 4. Umbrella Draft-Debris Inventory (chapter-06.md, 5,874 lines)

Scan method: `arc6_umbrella_scan.py` + targeted greps (never whole-file reads). The 2026-08-23 pass-1 removed explicit rewrite markers (`Let me rewrite`, `Here is the correction`, `Version A/B`, `Montage`, `pass1/pass2`: **all now 0 hits**) but **left every beat/duplicate/craft-note/scaffold in place**. All debris below survives in the umbrella; umbrella line numbers given (splits were generated from it 2026-08-23 17:45â€“17:51, so the same text sits at the split lines listed in Â§2).

| Umbrella L | Content | Split twin | Disposition | Canon evidence |
|---|---|---|---|---|
| L122 | draft beat `Next scene beats >...Lira speaks angrily...` | arc6-01 L123 | DELETE | polished twin L134 |
| L904 | directive `*Now let's see Yvaria, Reva, lira and vex*` | arc6-01 L905 | DELETE | author meta |
| L1253â€“1267 | Kyre-Tree response (single, correct) | arc6-02 L208â€“225 | KEEP | â€” |
| L1531 | directive `*Let's look at the immediate aftermath...*` | arc6-02 L486 | DELETE | author meta |
| L1824â€“1835 | craft block `The chapter is working on all three fronts...` | arc6-02 L779â€“790 | DELETE | author meta (J3 archive?) |
| L1940 | directive `*You can write the next scene...*` | arc6-02 L895 | DELETE | author meta |
| L1993â€“2033 | Kyre-Tree scene V1 | arc6-02 L948â€“988 | DELETE | V2 at U-L2037â€“2086 is canon |
| L2035 | approval `*I like it, let's write it*` | arc6-02 L990 | DELETE | author meta |
| L2330 | draft beat `Then without warning the lament...` | arc6-03 L133 | DELETE | polished V3 |
| L2334â€“2389 | L'vat strike V1 | arc6-03 L137â€“190 | DELETE | V3 canon |
| L2391â€“2425 | L'vat strike V2 | arc6-03 L194â€“228 | DELETE | V3 canon |
| L2427â€“2470 | L'vat strike V3 | arc6-03 L230â€“272 | **KEEP (canon)** + apply Â§2.3 hum fixes | final rewrite, connects to girl scene |
| L2474 | draft beat `We see a humman mother...` | arc6-03 L277 | DELETE | polished twin |
| L3072â€“3100 | craft block (Shadow Office etc.) | arc6-03 L866â€“891 | DELETE | author meta |
| L3372â€“3480 | Snow-Paw dinner V1 | arc6-04 L36â€“145 | DELETE (J2 salvage) | V2 canon; V1 has Velarius inconsistency |
| L3482 | directive `*We follow them to the dinning room...*` | arc6-04 L146 | DELETE | author meta |
| L3651 | corrections note `*/corrections 1) the snow paws...*` | arc6-04 L315 | DELETE | implemented by V2 |
| L3977 | draft beat `Later at night Nikolai ask Cefiro...` | arc6-04 L641 | DELETE | polished twin |
| L4051 | draft beat `The next day at breakfast Nikolai announces...` | arc6-04 L715 | DELETE | polished twin |
| L4489â€“4528 | craft block (arc6-03 copy + extras) | arc6-04 L1148â€“1190 | DELETE | author meta |
| L4530 | draft beat (sparring run-on) | arc6-04 L1194 | DELETE | polished twin L1202â€“1226 |
| L4557 | Nikolai laugh V1 | arc6-04 L1221 | DELETE | V2 at L1226 canon |
| L4566/4569/4586/4597 | scaffold headings `**Feedback on the Combat Choreography**` / `**The Halberd User (Nikolai)**` / `**The Four Pillars User (Ajani)**` / `**The Verdict**` + analysis | arc6-04 L1230â€“1264 | DELETE | author meta (rule 5) |
| L4606 | draft beat `Everyone cheers for Ajani everyone but l'vat...` | arc6-04 L1270 | DELETE | polished twin L1305+ |
| L4830â€“4896 | Maren report V1 | arc6-05 L165â€“234 | **KEEP (canon)** per J1 recommendation | complete scene w/ closer |
| L4898â€“4908 | Maren report V2 fragment | arc6-05 L238â€“248 | DELETE or splice Nikolai speech (J1) | contradicts V1 |
| L4913 | draft beat (funeral, `40 coffins`) | arc6-05 L253 | DELETE | polished twin |
| L5126 | draft M'rak citation | arc6-05 L466 | DELETE | polished L474 |
| L5134â€“5151 | M'rak polished block (1st) | arc6-05 L470â€“491 | **KEEP (canon)** | first occurrence |
| L5153â€“5168 | M'rak polished block (duplicate, incl. `again.M'rak` glue) | arc6-05 L493â€“511 | DELETE | exact repeat |
| L5269 | draft beat Tamsin scroll | arc6-05 L609 | DELETE | polished V2 |
| L5277â€“5300 | Tamsin V1 (`Sun's Mercy, Honorary General`) | arc6-05 L613â€“651 | DELETE | V2 title proven canon by L721/L739/L1135 refs |
| L5317â€“5340 | Tamsin V2 (`Knight of the Wengari / Golden Claw`) | arc6-05 L653â€“681 | **KEEP (canon)**; fix `a third scroll`â†’`a second scroll` (EDITORIAL) | downstream refs |
| L5377 | draft beat Vasha/Mira scroll | arc6-05 L717 | DELETE | polished twin |
| L5406 | draft Mira citation | arc6-05 L771 | DELETE | polished L781 |
| L5460 | draft beat war horn | arc6-05 L800 | DELETE | polished twin |
| L5542 | draft beat Salahim `mother load` | arc6-05 L882 | DELETE | polished twin |
| L5833 | draft beat Sulheim | arc6-05 L1173 | DELETE | polished twin |

Additionally in the umbrella (as in the splits): arc6-02 L176/L352/L585/L672/L898 twins (â‰ˆ U-L1221/L1397/L1630/L1717/L1943); arc6-03 L78/L610/L710/L765/L895 twins; arc6-05 L129â€“140/L144/L295â€“316/L342/L378â€“406/L410/L515/L576/L684â€“708/L1034 twins. All DELETE.

**Rule-5 check (author meta-text):** explicit markers eliminated by pass-1; surviving meta-text is exactly the inventory above. `chapter-06.md.bak.before_pass1` (514,876 B, 2026-06-16 23:35) exists â€” existence noted, not audited, per instructions.

---

## 5. Duplicate Blocks with Canon Designation

| # | Chapter | Versions (split lines) | Canon designation | Evidence |
|---|---|---|---|---|
| 5.1 | arc6-02 | Kyre-Tree scene: V1 L948â€“988 Â· V2 L992â€“1041 | **V2** | V2 has descent transition (L992), Ajani's spoken line (L996), consolidated ending (L1040 absorbs V1's L987 tail); V1 opens abruptly with no entry |
| 5.2 | arc6-03 | L'vat strike: V1 L137â€“190 Â· V2 L194â€“228 Â· V3 L230â€“272 | **V3** | final rewrite (`The Deep felt the elements shift`); only V3 resolves the standoff (`Stand down. The White Dawn vouches for them.` L272) and connects to the girl/Quick scene; V1/V2 are superseded takes |
| 5.3 | arc6-04 | Snow-Paw dinner: V1 L36â€“145 Â· V2 L149â€“313 | **V2** | V2 removes the Velarius knowledge the corrections note (L315) forbids, adds the Snow-Paw interruptions the note demands, and flows into the arena scene (L323+). V1's unique beats â†’ J2 |
| 5.4 | arc6-04 | Nikolai laugh: V1 L1221 Â· V2 L1226 | **V2** | V2 adds the formal salute paragraph (`Nikolai Silverpelt... salutes Ajani Brightmane...`), mirroring Ajani's L1216 salute; V1 is the shorter early take |
| 5.5 | arc6-05 | M'rak exaltation reactions: 1st L470â€“491 Â· 2nd L493â€“511 | **1st occurrence (L470â€“491)** | 2nd is a verbatim repeat whose first line is a glue defect (`...prepared to speak again.M'rak rose...` L493); delete L493â€“511 |
| 5.6 | arc6-05 | Tamsin investiture: V1 L609â€“651 Â· V2 L653â€“681 | **V2** | downstream canon refs to `Knight of the Golden Claw` (L721, L739) and `first Knight of the Wengari` (L1135); V1's `Sun's Mercy/Honorary General` appears nowhere else in the corpus |
| 5.7 | arc6-03 + arc6-04 | craft block: arc6-03 L866â€“891 â‰¡ arc6-04 L1148â€“1171 (verbatim) | **delete both** | author meta-text, not story; identical wording incl. the `paper shield` sentence; arc6-04 copy then continues with chapter-specific extras L1174â€“1190 (also delete) |
| 5.8 | arc6-05 | Maren report: V1 L165â€“234 Â· V2 fragment L238â€“248 | **V1 (recommended) â€” JUDGMENT** | V1 complete with scene closer; V2 orphaned (no Ajani prompt) and contradicts V1 (`We have no names to add` vs V1 `the Snow Paw names that the Tsar has provided`). V2's Nikolai funeral-set-up speech is worth salvaging â†’ J1 |
| 5.9 | arc6-01/04 | `The Humman army marched from Verdantis...` arc6-01 L77 â‰¡ arc6-04 L94 â‰¡ arc6-04 L163 | **keep all (NOT a defect)** | intentional in-story repetition: Cefiro repeats his report to the Snow Paws (arc6-04 L94=V1 dinner, L163=V2 dinner â€” one dies with each version's deletion anyway) |

Cross-chapter intentional echoes verified as non-defects: `Life in the desert is hard. Only those strong enough survive.` (arc6-05 L304 quote-back in craft block + speech), salute title lists (arc6-01 L192 â‰¡ arc6-04 L1216 â€” both polished, both need the same King fix).

---

## 6. Remediation Classification

All fixes must be applied to the **umbrella chapter-06.md** (source of truth), then re-split. The splits are regenerated artifacts. Umbrella line map in Â§4.

### 6.1 MECHANICAL (scriptable closed map) â€” 59 fixes
**M1. Missing opening quote (1):** arc6-01 L641 â€” prepend `"` to `Peregrine variants. We call them Sunraptors...` (paragraph already ends with closing `"`); optionally wrap in dialogue-block like neighbours (EDITORIAL part optional).

**M2. Formal-title capitalization (4):**
| File | Line | Current | Fixed |
|---|---|---|---|
| arc6-01 | L192 | `...holder of Luxor, king of the Wengari.` | `King of the Wengari` |
| arc6-02 | L714 | `...great Sultan Salahim, king of the humans.` | `King of the Hummans` (also M3) |
| arc6-04 | L1216 | `...caller of spirits, king of the Wengari, salutes...` | `King of the Wengari` |
| arc6-04 | L1226 | `...White Dawn, king of the Wengari.` | `King of the Wengari` |

**M3. Humman spelling/capitalization closed map (~52 polished-text tokens):** replace, in the polished lines listed below only: `humanâ†’Humman`, `humansâ†’Hummans`, `Humanâ†’Humman`, `Humansâ†’Hummans`, `hummanâ†’Humman`, `hummansâ†’Hummans`.
- arc6-02: L4 (`the humans currently`), L710, L714.
- arc6-03: L120 (Ã—2), L128, L137* (only via canon V3 L230), L161, L230, L252 (Ã—2), L256, L262, L267, L281 (`humman woman`), L307, L323 (`Human cubs`), L351, L356, L384, L403 (Ã—2), L407, L416, L420 (Ã—2), L491, L511, L578, L583, L641, L735, L773 (Ã—2), L802, L831 (Ã—2). (*V1/V2 occurrences die with the debris deletion; apply the map to canon V3 L230â€“267.)
- arc6-04: L247 (`Human.`â†’`Humman.`), L256, L266.
- arc6-05: L262, L267, L273, L292, L322, L332, L372, L584, L901 (`Sultan of the Humans`â†’`Sultan of the Hummans`).
- arc6-01: L1011 (`hummans`â†’`Hummans`).

**M4. Concatenation/glue defects (2, both inside blocks already deleted by D-list â€” no standalone fix needed, listed for completeness):** arc6-05 L493 `again.M'rak`; arc6-05 L314 `with it.The scene` (craft block).

**M5. Tamsin scroll numbering (1):** arc6-05 L653 (canon V2) `a third scroll passed` â†’ `a second scroll` (only the generals' scroll precedes). EDITORIAL-mechanical hybrid; safe to script.

**Script for M2+M3:** a line-addressed sed/python patch keyed to umbrella line numbers (Â§4 map) is trivially derivable from `arc6_tooling/arc6_lint_results.json` + `arc6_tally.txt`; no regex-wide replace (would hit draft lines that are being deleted anyway â€” harmless either way, but line-addressed is cleaner).

### 6.2 EDITORIAL (judgment deletion/reword) â€” 7 items
**E1.** arc6-01 draft-format lines with **unique scene content** (no polished twin found): L197 (Ajani's "how many did we lose" question to M'rak), L313 (resignation-refusal + reward thought), L443 (Velarius-madison question to Seris â€” note: polished continuation L447 reacts to it, so the line cannot simply vanish), L485 (orders to Seris/Tamsin). â†’ **Rewrite into polished prose** (matching surrounding register), or confirm a twin exists and delete.
**E2.** arc6-02 L352 (draft promotion-and-rebuke speech): verify polished twin in the same council scene; if none, rewrite (scene depends on the promotion order).
**E3.** arc6-05 L238â€“248 (Maren V2 fragment): delete the duplicated report; decide whether to splice Nikolai's `We have no names to add to your pillar, but we will stand with you at the memorial. The fifth family will honor the fallen of the four.` into canon V1 (replacing V1's `the Snow Paw names that the Tsar has provided` clause) â€” see J1.
**E4.** arc6-04 dinner V1 unique beats salvage (J2): Nadya/Vanya questioning block (L112â€“122, incl. `Are any of them as beautiful as me?`), Vanya `Good. I will fight them all.` (L117), Ivan beats (L80). If kept, reword into V2; if dropped, plain deletion.
**E5.** arc6-04 L41 dangling sentence-final dash â€” dies with dinner V1 deletion; if V1 is salvaged per E4, the sentence must be completed.
**E6.** arc6-01 L641 dialogue-block wrapper: optionally wrap the fixed paragraph in `<div class="dialogue-block">` for structural consistency with neighbours.
**E7.** arc6-05 L653 see M5 (listed once; execute with M batch).

### 6.3 JUDGMENT (needs Ainz-sama's decision) â€” 3 items
**J1. arc6-05 Maren-report contradiction (L165â€“234 vs L238â€“248).** Two mutually exclusive facts: V1 says the Tsar **has provided** Snow Paw names for the pillar; V2's Nikolai says the Snow Paws have **no names to add** but will stand at the memorial. Both lead into the funeral scene. Recommendation: keep V1 as the scene, splice V2's Nikolai speech in place of V1's names clause (the speech is the stronger beat and sets up Nikolai walking beside Ajani at the pyre). **Decision needed:** splice vs plain V1.
**J2. arc6-04 dinner V1 unique beats.** V1 (canon-superseded) contains beats absent from canon V2 (Nadya's marriage/beauty question, Vanya's fight-them-all). **Decision needed:** salvage into V2 (E4) or drop.
**J3. Non-Ajani `*...*` thoughts + craft-block archiving.** (a) Rule 3 binds Ajani only; Nikolai's thought (arc6-04 L1321) and the shared Wengari+Humman thought (arc6-02 L693) use `*...*`. Tree telepathy in `*...*` is established canon. **Decision needed:** keep as-is, or unify ALL character thoughts to single quotes. (b) The craft-feedback blocks (Â§4) are genuine editorial analysis; **decision needed:** delete outright or export to `QA/` archive before deletion.

### Deletion batch (D-list, mechanical but large â€” ~350â€“400 lines)
Execute after J1â€“J3: all Â§4 inventory rows marked DELETE (draft beats, synopsis beats, directives, planning notes, craft blocks, scaffold block, duplicate versions V1/superseded takes, approval lines). Every deletion is line-addressed in Â§4/Â§5; no content judgment required except where E1â€“E4 flag unique content.

---

## 7. Status

**FINAL.** All seven sections complete; every finding script-derived and spot-verified against actual file lines (line numbers in this report are exact split-file lines; umbrella lines exact for chapter-06.md). READ-ONLY discipline maintained throughout â€” story content untouched; writes confined to this report and `QA/arc6_tooling/`. Artifacts retained for the remediation pass: `arc6_lint_results.json` (per-line hit map), `arc6_tally.txt`, `arc6_em_classify.txt`, `arc6_quote_pair.txt`, `arc6_delim_cross.txt`, `arc6_hyphen_audit.txt`, `arc6_umbrella_debris.json`.

Pending downstream: Ainz-sama's decisions J1â€“J3 â†’ then a single umbrella patch pass (D-list deletions + M1â€“M5 map) â†’ re-split â†’ re-run `arc6_tooling` battery as verification (expected residual: 0 debris markers, even quote counts in all five files, zero single-m tokens outside Earth-glosses â€” none exist).



---

# PART V - MARE LORE CONTINUITY CHECKLIST (verbatim)

# Mare â€” Arcs IIIâ€“VI Lore Continuity Checklist

**Author:** Mare (lore authority, tandem audit) Â· **Commissioned by:** Demiurge (Ainz-sama's directive)
**Date opened:** 2026-08-24 Â· **Status:** COMPLETE (all sections filled; one ADJUDICATE item needs Demiurge's ratification)
**Purpose:** Canon continuity checklist for Arcs IIIâ€“VI, drawn from bestiary/world docs + chapter corpus + raw conversation.
After Demiurge's quality gate, this file is the **adjudication basis** for judgment items in the four
subagent reports (`QA/arc3_audit_report.md` â€¦ `QA/arc6_audit_report.md`).

**Usage rule for reviewers:** items marked **CANON** are fixed law â€” deviations in chapter text are findings.
Items marked **ADJUDICATE** await a ruling (pending Ainz-sama decisions D1â€“D5 from the Arc Iâ€“II audit or new
evidence). Items marked **KNOWN-RESIDUAL** are documented contamination â€” flag, do not canonicalize (Â§8).

---

## 1. Umbrella Status Verification (Demiurge item 3)

### 1.1 Arc IV â€” what pass does current `content/story/chapter-04.md` represent?

**VERIFIED from disk timestamps + sizes (all artifacts on disk, `content/story/`):**

| File | Modified | Bytes | Role |
|---|---|---|---|
| `chapter-04.md.stripped_meta` | 2026-06-18 23:02 | 532,079 | Pass: meta-commentary stripped |
| `chapter-04.md.stripped_passes` | 2026-06-18 23:13 | 509,459 | Pass: stacked draft passes stripped |
| `chapter-04.md_pass3_only.md` | 2026-06-19 05:40 | 57,447 | Extracted pass-3-only fragment |
| `chapter-04.md.repass3` | 2026-06-19 05:55 | 503,185 | Pass: re-pass-3 integration |
| `chapter-04.md.alpha_excise` | 2026-06-20 00:37 | 492,264 | Pass: alpha-content excision |
| **`chapter-04.md` (current)** | **2026-06-20 14:08** | **481,075** | **Final cleaned umbrella** |

**Ruling:** the current `chapter-04.md` is the **latest and final stage of the Arc IV cleaning chain** â€”
it post-dates `.alpha_excise` (by ~13.5 h and ~11 KB of further excision). Sizes decrease monotonically down
the chain (532,079 â†’ 509,459 â†’ 503,185 â†’ 492,264 â†’ 481,075), confirming strictly reductive passes. All five
artifacts share the identical head (`# Chapter 4: The Consolidation` + opening dialogue-block), confirming
same-lineage, no re-authoring. The Arc IV sub-chapters `chapter-arc4-01..06.md` were **regenerated from this
final umbrella on 2026-06-27 19:38** (all six share that timestamp) â€” served slices match the final pass.
**Arc IV editorial state: CLEAN/FINAL at umbrella level as of 2026-06-20; slices in sync since 2026-06-27.**
Caveat: "final" = final *meta/draft-stack* pass. Raw-voice dialogue lines (missing apostrophes, lowercase)
survived that pass â€” see Â§8 item 4. The pre-cleanup original survives at `raw/chapter-04.md` (510,116 b) â€”
never served, never audit as canon.

### 1.2 Arc VI â€” what was the 2026-08-23 17:45â€“17:51 work, and is Arc VI mid-pass?

**VERIFIED from disk timestamps + memory log `memory/2026-08-23.md` ("Arc 6 OPENS" evening session):**

- `chapter-06.md.bak.before_pass1` (514,876 b, frozen 2026-06-16 23:35) = pre-scrub snapshot.
- `chapter-arc6-04.md` modified **2026-08-23 17:45** (101,328 b): Ch 4 "The Road Begins" â€” raw author
  planning-bleed (*"On the 7th dayâ€¦ the scene should revolve aroundâ€¦"*) stripped from umbrella + slice.
- `chapter-06.md` (umbrella, 495,904 b) + `chapter-arc6-01.md` (90,556 b) modified **17:51**: Ch 1 "The Cost"
  quadruple-stacked drafts (~12 KB: two "So who can tell me" asks, two cacophony paragraphs, three M'rak
  report passes) deduplicated via `dedupe_arc6_ch1.py` â€” kept opening + eruption-1 + canonical report pass 3.
  **Canon fix in the same pass:** eruption draft had Seris say Lena was "executed by Mekhmed"; this
  contradicts canon (Lena **missing, fate unknown**) and was corrected to the canon-consistent line.
  Net umbrella reduction: 514,876 â†’ 495,904 b (~19 KB).

**Ruling:** that work was **Arc VI meta-scrub pass 1** (ch4 planning-bleed excision, then ch1 draft-stack
dedupe + Seris/Lena canon fix), applied umbrella-first and re-emitted to the touched slices. **Arc VI is
MID-PASS:** pass 1 is done on record, but a fresh scan today (2026-08-24) found **three residual
contamination markers the pass did not catch** (Â§8 items 1â€“3, all with umbrella + slice coordinates).
Subagents auditing Arc VI must treat it as not-yet-final; findings there are expected, not anomalous.

---

## 2. The Attendant-Name Problem: T'van / T'vat / L'vat â€” ADJUDICATED

**Evidence gathered today (raw conversation = `ethra_full_conversation.json`, the DM/Ainz source of truth):**

| Name | Raw conversation | Chapter sub-files |
|---|---|---|
| T'van | **135** | 44 (arc3 = 10, arc4 = 14, arc5 = 0, arc6 = 0) |
| T'vat | **3** | 3 |
| L'vat | 262 | 92 |

**RULING (resolves pending decision D4 from the Arc Iâ€“II audit):** **T'vat is a misspelling of T'van â€” not a
distinct character.** T'van (young Bright Paw priest, Ajani's loyal attendant, canon from Arcs Iâ€“II) continues
as the attendant through Arcs IIIâ€“IV (24 sub-chapter appearances). All three T'vat instances are drift:
1. `chapter-arc3-01.md` L78: `"t'vat call for the elder council of the striped paws, now please "` (also
   lowercase-t and "striped paws" drift â€” see Â§6)
2. `chapter-arc4-02.md` L240: `"T'vat, send in the humans, but before call the royal guards outsideâ€¦"`
3. `chapter-arc4-02.md` L288: `'I hate her so, so much' - "T'vat, send them in"`
â†’ **Fix all three to T'van** (preserving the lowercaseâ†’capital correction at arc3-01 L78).

**L'vat is unrelated â€” never conflate.** Canon docs (bestiary.md L118/L310â€“311): L'vat is a **Lament**
(Lament-avatar of the Mycelial Deep) who trained Ajani (Iris Serpent used in training); the Threx trust Ajani
partly because of it. Neither T'van nor T'vat appears in bestiary/world docs â€” both are corpus-only characters.

**Note for Arcs Vâ€“VI:** T'van has **zero** mentions in Arc V and Arc VI. This is canon (war arc + aftermath;
attendant function absorbed by Kira/Zephyr/scorpions), not missing text â€” do not flag the absence.

---

## 3. Veylar "Twenty Thousand Years" Canon + World Chronology

**CANON:** the Veylar / sentient-life figure is **twenty thousand years**, always spelled out in prose.
Established as canon in the Arc Iâ€“II audit (arc2-06 Version A's "millions of years" was ruled a contradiction
and cut). All Arc IIIâ€“VI instances verified **consistent** (6 hits, all "twenty thousand years", zero "20,000"):

- arc4-01 L424 â€” "Sentient life has existed for roughly twenty thousand years" (world chronology anchor)
- arc4-04 L210 â€” Sylara: "The Veylar have been patient for twenty thousand years."
- arc6-03 L682 â€” Coral Citadel voice: "We have been patient for twenty thousand years."
- arc6-04 L1129 â€” Veylar procession "alive for twenty thousand years"
- arc6-05 L161, L388 â€” Veylar queen / diplomacy "twenty thousand years"

**"Million years" occurrences â€” RULED LEGITIMATE (do not flag, do not normalize):**
- arc6-02 L987/L1040 â€” Kyre Tree voice: "I have nothing else to do for the next million years."
- arc6-03 L556 â€” Tree voice: the scar from the thing out of the belt "took a million years to heal."
- arc6-02 (draft B narration, ~L1010/L1025): the Tree "reaching back across **millions of years** of memory",
  sensations stored "for **millions of years**".
**Ruling rationale:** the narration itself confirms the Tree's memory spans millions of years â€” the Tree
predates sentient life by orders of magnitude ("Before the Wengari walked the desert. Before the pact. Before
the Lightbringer gave me a name."). 20,000 years bounds *sentient life and the Veylar*, not the Tree. Battery:
never rewrite Tree-voice timescales to fit the 20k figure.

**Full chronological ladder for consistency checks (all canon, from corpus):**
1. **~millions of years** â€” Kyre Tree's own age/memory (Tree-voice only; the scar from the darkness out of the belt).
2. **~20,000 years** â€” sentient life on Ethra; Veylar civilization patience.
3. **~5,000 years** â€” First Tyrant's purge of the Wengari families; Snow Paws fled north (arc5-11); Motted Paws
   "waited five thousand years to be recognized as equals" (arc4-01 L255); Shadow Paws' shame "five thousand
   years" (arc6-04 L662).
4. **~3,000 years** â€” the Pact / Lightbringer era; Bright Paws as royal family; Pyrinae vassalage ("freed the
   Pyrinae from three thousand years of vassalage" â€” arc6-04 L4).
5. **~1,092 years** â€” Tyrant cycle (five Tyrants, Convergence-born, touched by both suns); the Fifth Tyrant
   ~500 years ago; Ajani = the **sixth White Dawn**, "born five hundred years after the Fifth Tyrantâ€”far too
   early by the ancient cycle" (arc4-01 L424).

---

## 4. Humman(s) Spelling Canon

**CANON (established Arc Iâ€“II audit, from bestiary.md/world.md consistency):** **"Humman / Hummans"
(double m)** is the race name. Single-m "human/humans" is drift. Two carve-outs still pending Ainz-sama:
- **D3** â€” adjectival "human" (e.g. "the human quarter", "the human general"): flag, hold for ruling.
- **D5** â€” lowercase "humman(s)" inside thought-text: flag, hold for ruling.

**Corpus census, Arcs IIIâ€“VI (sub-chapters, 2026-08-24):**
- ARC3: Humman = 68, human = 3
- ARC4: Humman = 204, human = 3
- ARC5: Humman = 138, HUMAN = 2 (all-caps â€” check whether shouted dialogue; may be legitimate emphasis)
- ARC6: Humman = 199, **human = 86** â† anomaly

**ADJUDICATE (Arc VI spike) â€” preliminary ruling:** sampled Arc VI single-m hits cluster in raw-voice passages
(missing apostrophes, scene-direction asterisk blocks â€” arc6-01 L313/L439/L485/L1042), i.e. unpolished session
text, not a deliberate spelling choice. Note arc6-01 L485 mixes both forms inside one speech ("more hummans
were like you" + "the human quarter"). Working ruling for the battery: treat all single-m tokens as
drift-to-flag; hold adjectival uses for D3; do NOT auto-fix anything in Arc VI until pass 2 (Â§1.2).

---

## 5. King Titulature

**CANON rule (established Arc Iâ€“II audit):** capitalize **King** when used as a title before a name or as
direct substitute for a specific named king's title; lowercase **king** for generic/predicative reference.
Royal formal register uses "the crown" / "This king recognizes you" (arc6-01 L485) â€” canon register, not error.

**Calibration examples for the battery:**
- `"He is king," Nikolai said` + `"He is not merely a king. He is a White Dawn."` (arc6-04 L4) â€” predicative
  generic â†’ **lowercase correct**. Do not flag.
- `King Ajani` (arc4-01 L217), `king's favorite mount` (arc3 summary) â€” title/substitute â†’ capital contexts.
- **"the defeated Tsar of the Snow Paws"** (arc6-05 L1135) â€” Nikolai's style is **Tsar**, never King of the
  Snow Paws; flag any king/Tsar cross-contamination between Wengari and Ice City contexts.

**Canon titulature litany (arc6-04 L4, Cefiro's ambassadorial summary â€” use as fact-check anchor):**
Ajani Brightmane = King of the Wengari; the White Dawn; Convergence-born; touched by both suns; renewed the
pact with the lord of the desert (Kyre Tree); trained under the lord of the marsh (L'vat); freed the Pyrinae
from 3,000 years of vassalage; held a tournament and put his crown on the line; survived an assassination
attempt, a coup, a coma, and a war; summoned six elemental spirits and destroyed a Plague creature with a
thunderstorm; united the four families; built offices/councils/trade routes. Arc IV L424 anchor: "the sixth
White Dawn". Any battery finding that implies a different title set is a lore conflict â†’ escalate.

---

## 6. Faction / Race Name Consistency

**Wengari family-count rule â€” CANON (the corpus explains it; do NOT normalize fourâ†”five):**
- **Four families** is the home-desert political reality from Arc IV onward: Bright, Stripe, Shadow, Motted.
  Ajani formalizes it: "Four families. Four shares." (arc4-01 L239â€“255), with Bright Paws as the royal family
  ("We are simply the branch that rules").
- **Five families** is correct in: (a) ritual/archaic references (Arc Iâ€“II ceremonial prose: "elders of the
  five families" â€” arc2-01/02/03, arc3-02 L266 "the Five Families had assembled"); (b) the arc5-11 Cefiro
  reveal â€” Snow Paws are the fifth family, fled north ~5,000 years ago when the First Tyrant purged the others
  (arc5-11 L102/L126); (c) Arc VI homecoming language ("welcomed the fifth", arc6-05 L1135; "He wishes for the
  fifth family to come home", arc6-04 L4; "There are four families now. Five, if you count us", arc6-04 L662).
- **Special case â€” the white spear symbolism** (arc4-05 L669, Nefere): "Five families. One spear." counts
  four Wengari families + the Pyrinae as the fifth element (fire/water/light/darkness/earth). Legitimate.
- Post-reveal Arc VI prose saying "banners of the **four** families" (arc6-01 L789, arc6-02 L231/L388/L483/
  L1043, arc6-05 L344/L447) is **correct** â€” Snow Paws not yet resident; their banner is added explicitly as
  new ("the frozen star of the Snow Paws", arc6-05 L344).

**Family names â€” CANON forms + drift found:**
- **Bright Paws** (lions, royal; Lightbringer bloodline; Four Pillars martial art; "royal family for three
  thousand years"). Arc Iâ€“II singular form "Bright Paw" also canon (adjectival).
- **Stripe Paws** (tigers; caravan masters/merchants/mercenaries; Fire Paws style; Zara = Stripe Paw chief;
  Ajani's mother was Stripe Paw â€” arc4-05 L431 "Your mother was one of us"). Raw conversation: "Stripe Paw"
  = 766, **"Striped Paw" = 0** â†’ "striped paws" at arc3-01 L78 is drift (also lowercase) â†’ fix to "Stripe Paws".
- **Shadow Paws** (panthers; assassins/spies; First Tyrant's shame; Kareth; Black Fire Tide Wolf cavalry).
- **Motted Paws** â€” **ADJUDICATE (docs vs corpus split):** chapter corpus = **Motted 296 vs Mottled 8**
  (Mottled hits: arc3-02, arc3-05, arc4-03, arc5-11, arc6-01 Ã—2, arc6-02 Ã—2). BUT bestiary.md's lineage table
  (L24: "Mottled Paws | Jaguars | Rune Belt") and world.md L120 say "Mottled Paws", while bestiary L231 body
  says "Motted Paws" and image assets are "mottled-paw.*". **Mare's recommendation:** standardize on
  **Motted Paws** in story text (corpus 97 %+ majority + Demiurge's directive spelling); treat the 8 chapter
  "Mottled" hits as drift; leave bestiary table/world.md/image filenames for a separate docs-alignment task
  (flag, don't silently edit docs during the audit). Needs Demiurge ratification.
- **Snow Paws** (snow leopards; fifth family; Ice City; Sunraptor riders; Cefiro = Snow Paw **prince**, styled
  "Peregrine" in bestiary L296 â€” "Snow Paw Peregrine Cefiro"; Tsar Nikolai; Nadya).
- **M'rak, Yvaria, Irek, Toren, Kira, Pearl** (Arc V principals â€” note M'rak is a Wengari commander, Yvaria
  rides/commands ghosts with a silver-furred drum; bestiary confirms "the Motted Paws speak to [Ghosts]
  through drums" â€” cross-consistent âœ“).

**Other races â€” CANON forms:**
- **Veylar** â€” Shell-Singers, Tide-Wardens, Deep-Watchers; Petal-Shells; Resonant Network; Coral Citadel;
  Tidepools; queen in Arc VI (living-coral chair carried from the Tidepools); Xal'thyra = Veylar Tyrant, only
  Styx-rider. "Sylara" = Shell-Singer of record (Arc II+).
- **Pyrinae** â€” rune-glass artisans, Hydromancers, Styx-feather trade; vassalage ended by Ajani; Nefere
  (notable, spear-forging); the **Sun-Walkers** are a Pyrinae order (Mira = Nefere's most trusted, arc4-06
  L556). Rune Belt is their territory (Ghost bats, Razor Hares, kyre flowers).
- **Hummans** â€” mercantile empire; capital **Verdantis**; Amuk siege-beasts; generals **Mekhmed** and
  **Tamsin** (Tamsin defected, honored by Ajani â€” arc6-01 L485); "Golden Cloaks" = Humman/Wengari? unit
  risen during the war (arc6-01 L297-region) â€” [battery: if a lint flags "Golden Cloaks" as unknown term,
  LEGITIMATE]; coiled-scorpion banner (arc6-05 L344).
- **Threx** â€” Lament / Quick / Rooted forms; the Deep; L'vat (see Â§2); mycelial-web banner (arc6-05 L344).
- **Styx** â€” **a flying-creature species, NOT a faction** (omens; feathers; ridable only by Xal'thyra; prey =
  Razor Hares). Battery: never merge **Styx** with **Styxian** (the Wengari capital) or **Styxian**
  adjectival; 166 "Styx" substring hits in sub-chapters include heavy "Styxian" use. "Styx crown" (arc6-01)
  = regalia named for the creature. Dragari = ancient myth-tier singers (gave Cefiro the pearly medallion).
- **Chi'Thak** = the Blight (spawned the Plague creature of Arc V). **Plague weapons** = old-world weapons
  from **Velarius**, given to the Humman king by a shape-wearing shadow (arc6-02 draft B â€” canon reveal).

**Other named-figure drift watch:** **Sylva** (canon; raw conversation = 860) vs **Sylvia** (raw = 3; chapter
corpus = 1 hit: arc4-02 L240 "call Sylvia") â†’ **Sylvia is drift â†’ fix to Sylva.** Note Sylva is the Motted
Paw / council figure who becomes **Regent** during Ajani's coma (Arc IVâ†’VI; see Â§7 Arc VI). Do not confuse
Sylva with **Sylara** (Veylar Shell-Singer) â€” distinct characters, similar names, battery should treat any
Sylvaâ†”Sylara substitution as a critical lore error.

**Arc IVâ€“VI recurring cast (flag any spelling drift):** Ajani Brightmane, Kareth, Zara, Nyasha, Seris
(Humman ambassador), Sylara, Elyra (Motted Paws; grimoire of Flowing Water; carries the regency burden per
arc6-01), Solen (aged Bright Paw High Priest), Anktor (True Dawn rival claimant, Arc IV), Nefere, Mira,
M'rak, Yvaria, Irek, Toren, Kira, Pearl, Black Fire, Red Fire, Mekhmed, Tamsin, Zephyr (legion commander;
shadow riders, arc6-04 L1129), Cefiro, Nikolai, Nadya, Maren (pensions/reparations officer, arc6-01 L313),
Vasha (arc5 opener "Vasha Storms In"), Lena (Sylva's maid â€” see Â§7).

---

## 7. Arc-Specific Canon Facts (invisible to mechanical audit)

**Arc III â€” "The Tournament"** (5 chapters, 44,077 words; subs: The Arena / First Blood / The Fire Feet /
The Tyrant Cycle / The Hour Before):
- Ajani **puts his crown on the line** in the tournament (retrospectively confirmed arc6-04 L4). Fire Feet =
  arena mounts (Ember is one: "She carried you through the marshes for a year" â€” arc4-05 L431).
- Canon events referenced later: the broken warriors of his own blood / the apology (arc-03 summary), Sylva's
  arena intervention (silver-furred, arc3-05), the Tyrant Cycle lore reveal. T'van present (10 mentions).
- Known drift: arc3-01 L78 (`t'vat` + `striped paws`, Â§2/Â§6). "Five Families" ceremonial assembly (arc3-02
  L266) â€” legitimate per Â§6 family-count rule.

**Arc IV â€” "The Consolidation"** (6 chapters, 78,195 words; subs: Bureaucracy / The Caravans / The Pyrinae
Accord / The Humman Delegation / The Gifts / Aftermath):
- Umbrella = final pass state (Â§1.1). Bright Paws "royal family for three thousand years" (Solen, arc-04
  summary). Four-families settlement (arc4-01 L220â€“255; note L220 is a raw-voice line â€” Â§8 item 4).
- Veylar delegation opens the Pyrinae Accord (living coral for the hanging gardens); Humman delegation chapter.
- Gifts: Ember + ceremonial barding of all four families (Stripe Paws/Zara); grimoire of Flowing Water (Motted
  Paws/Elyra); the white spear of five elements (Nefere, arc4-05 L669 â€” Â§6 special case).
- arc4-06 = coup crisis: the **True Dawn faction** (canon name; arc4-06 L492/L505/L556/L584) argues Ajani is
  incapacitated ("the armor had rejected him"), invokes birthright; **Anktor** is the silent rival claimant;
  Elyra reports; Nefere + Mira the Sun-Walker + a razor hare set out pre-dawn; Sylva heads the war table
  ("the king wakes or the city fell"); the **Humman army arrives with the sunrise** â€” bridge into Arc V.
- arc4-01 L424 = world-chronology anchor paragraph (moon/axial tilt, 20k years, 1,092-year cycle, sixth White
  Dawn) â€” any contradicting number anywhere in Arcs IIIâ€“VI is a critical finding against this paragraph.

**Arc V â€” "The Great War"** (22 chapters, 47,706 words; the timestamp arc):
- Structure canon: every chapter opens on a timestamp, canonical formula "It was X:XX in the morning, the
  seventh day of the Month of Storms, in the first year of the reign of Ajani Brightmaneâ€¦" â€” 22 timestamps
  05:25 â†’ 12:06 (~7 real-time hours). Sub-titles ARE the timestamps ("05:25 â€” Vasha Storms In").
- Siege of Styxian by the Humman army: Mekhmed, Tamsin, Amuk siege-beasts, scorpion riders, the Wohs;
  defenders: M'rak, Yvaria + ghosts, Irek, Toren, Kira, Pearl, Black Fire & Red Fire, Nefere, the Golden
  Cloaks, the wall, the northern wall victory. Ajani summons six elemental spirits and kills the Chi'Thak
  Plague creature with a thunderstorm; falls into a coma (the coup of Arc IV's True Dawn overlaps).
- arc5-11 = Cefiro reveal (Â§6: fifth family, Dragari medallion, prophecy "the bulwark of paws will rise").
- T'van absent (0 mentions) â€” canon, Â§2.
- Battery note: `content/story/arcs/arc-05.md` (summary file only) shows **mojibake** ("### 05:25 Æ’?" Vasha
  Storms In" â€” double-encoded em dash). Encoding anomalies in CHAPTER text are findings; in the summary file,
  known and separate.

**Arc VI â€” "Aftermath & The Road"** (5 chapters, 80,677 words; subs: The Cost / Rebuilding / The Vision /
The Road Begins / Epilogue) â€” **mid-pass, see Â§1.2**:
- The Cost: throne room = hospital ward + war council + family gathering; Ajani in bed; bracers now "simple
  wrist wards barely a claw long"; Black Fire & Red Fire full-size (~2 m male / ~1.8 m female) on his arms.
- Canon reckoning scene (arc6-01 L295â€“313): M'rak exposes the Council's secret war-prep ("we brought
  regiments instead of legionsâ€¦ the fifth and sixth didn't come. The messages never reached them"); **Sylva
  confesses and tenders her resignation â€” Lena was HER maid and a spy**: copied correspondence, learned guard
  rotations, sent letters to Verdantis for weeks; Humman army disguised as "a hundred scorpionsâ€¦ a trade
  mission". Ajani refuses the resignation: "you fought to be regent now bear the weight till it's taken from
  you." **Lena's canon state = missing, fate unknown** (NEVER "executed by Mekhmed" â€” that was the draft line
  fixed 2026-08-23).
- Rebuilding: memorial pillar + celebration; Kyre Tree scene (draft B is canon â€” Â§8 item 3): a shape-wearing
  shadow gave the Humman king old Plague weapons from Velarius; the Tree remembers what passed over the desert
  millions of years ago ("the same darkness. The same hungerâ€¦ out of the belt" â€” connects to the canon entity
  "the one in the Rune-Belt"); "You destroyed its weapon. You destroyed its creature. You did not destroy it."
- The Vision: Ajani + Blackie/Reddy through the great bronze doors; "The Road" policy continues.
- The Road Begins: Cefiro presents the royal seal to **Tsar Nikolai** on the frozen landing platform, Ice
  City; "The starving boy who wandered into our city three years ago is now a king"; formal diplomatic
  relations + invitation for the fifth family to come home. Sepia-vs-cold palette question was cover-side only.
- Epilogue: four Heavenly Generals + first Knight of the Wengari named (arc6-05 L1135); atrium with four
  family sigils + allied-race banners + the frozen star of the Snow Paws raised for the first time; Veylar
  queen attends via carried coral chair / Shell-Singers (diplomatically absent in person â€” arc6-05 L388
  analysis is canon intent); Resonant Network reveal (arc6-03 L682); Yvaria's ghosts find their voice;
  Nadya: "He's taller than I remembered"; "the defeated Tsar of the Snow Paws" (arc6-05 L1135 â€” cite verbatim;
  do not speculate beyond the line).

---

## 8. Known Residual Contamination â€” DO NOT CANONICALIZE (all coordinates verified 2026-08-24)

1. **"We switch to" bath-scene planner line** â€” `chapter-06.md` L527 â‰¡ `chapter-arc6-01.md` L528:
   `<p class="speech-line">We switch to the night at the throne room ajani is taking a bath the bracers have
   become simple wrist wards barely a claw long, Cefiro is next to himâ€¦</p>` â€” user-planning "we-switch-to"
   bleed in a speech-line wrapper (same family as Arc V excisions, cuts 10â€“16). Missed by pass 1. The scene
   facts inside (bracersâ†’wrist wards, Cefiro) ARE canon (Â§7); the wrapper sentence is not prose.
2. **Asterisk scene-direction block** â€” `chapter-06.md` L438 â‰¡ `chapter-arc6-01.md` L439: `*The next scene
   is a couple of hours after ajani is sitting on the throne nowâ€¦ then we see zephyr bringing Tamsin in
   chainsâ€¦ seris is also there but her face is Unreadable*` â€” planning voice in thought-style italics; the
   scene facts are canon (Tamsin in chains, arc6-01 L485 pays them off), the block itself is residue.
3. **"I like it, let's write it" approval marker + Tree-scene double draft** â€” `chapter-06.md` L2035 â‰¡
   `chapter-arc6-02.md` L990. Structure: [draft A tail, arc6-02 ~L975â€“989, ending "â€¦next million years."] â†’
   marker `*I like it, let's write it*` â†’ [draft B, the full canon scene: "The descent into the inner chamber
   had become familiarâ€¦", containing the pool-vision + Velarius-weapons lore, ending L1040 "â€¦Now go. I am
   hungry."] â†’ continuation L1043 "Two weeks had passedâ€¦". **Canon = draft B + continuation; draft A tail +
   marker are residue.** Exact excision boundaries: from the start of the duplicated "The roots pulsed onceâ€¦"
   tail back through the marker â€” editor must locate where draft A's tail begins (search upward for the first
   scene opening preceding L975) before cutting; do not cut blind.
4. **Class note â€” Arc IV raw-voice lines survived the final pass** (e.g. arc4-01 L220: "thats because we call
   ourselves five families but we have been four for years, bright paws, shadow paws, motted paws, stripe
   paws, were actually just four..."). Arc IV umbrella is final for meta/draft-stack removal but NOT
   line-polished. Battery grammar findings on Arc IV are genuine findings, not pass-status artifacts.
5. **Class note â€” Arc VI raw-voice passages** (arc6-01 L313 speech-line: missing apostrophes, "theyre",
   French-accent "rÃ©parations/rÃ©gent"; also L1042 "the humans have more than once city" [sic, "one"]). Same
   treatment as item 4: genuine lint findings; also feeds the Â§4 Arc VI human=86 anomaly.
6. **Summary-file-only:** `content/story/arcs/arc-05.md` heading mojibake ("05:25 Æ’?"). Not chapter text.

---

## 9. Adjudication Workflow (post quality-gate)

1. Each subagent report item receives one verdict: **CONFIRMED-DRIFT** (fix per canon above, cite Â§),
   **LEGITIMATE** (canon exception, cite Â§), or **ADJUDICATE** (needs a ruling from Demiurge/Ainz â€” currently
   queued: D1 em-dash style, D3 adjectival "human", D5 lowercase "humman" in thoughts, and new: Motted/Mottled
   docs-alignment (Â§6), Arc VI pass-2 execution order vs corrections (Â§1.2)).
2. This checklist's section numbers are the citation basis for all lore calls.
3. Arc VI findings must carry the **mid-pass caveat** (Â§1.2): some will be resolved by Mare's scrub pass 2
   (items Â§8.1â€“3 already queued) rather than by audit corrections â€” coordinate before editing.
4. Umbrella-first rule for any fix: edit `content/story/chapter-0X.md`, then `python regenerate_chapters.py`;
   never patch only the slice (Arc Iâ€“II audit architecture finding; heuristic splitter â€” verify split
   boundaries after regen). `raw/` copies are untouched originals by policy.

---
*All sections COMPLETE. Evidence: disk timestamps/sizes, `memory/2026-08-23.md` + `memory/2026-08-24/*`,
raw-conversation name census (135 T'van / 3 T'vat / 860 Sylva / 3 Sylvia / 766 Stripe Paw / 0 Striped Paw),
corpus grep 2026-08-24. Sole ratification pending with Demiurge: Motted-vs-Mottled standardization (Â§6).*




---

# PART VI â€” REMEDIATION PLAN & MITIGATION STEPS (Demiurge)

## 6.0 Principles

1. **Umbrella-first, always.** Every fix lands in `content/story/chapter-0X.md`; `regenerate_chapters.py` re-emits the splits. Never patch a split directly (splits are regenerated artifacts; Arc V round-trip byte-identity is proven; Arcs III/IV use the heuristic word-offset splitter, so boundaries must be re-verified after every regen).
2. **Line-addressed edits, never wide regex.** Replacement maps are keyed to umbrella line coordinates (report Â§4 tables + gate corrections). Wide regex would strike lines slated for deletion and legitimate words (`ill`, `hell`, "TAKE A REST").
3. **Deletion safety rule.** A block is deletable only if it is pure author meta-text OR a superseded take with a designated canon counterpart. Every deletion in Parts Iâ€“IV satisfies this; the sole exceptions needing Ainz-sama are the salvage judgments (X2, J-III2/4, J-IV4/6, J-VI2).
4. **One arc at a time, fully gated, before the next.** Order: Arc III â†’ Arc IV â†’ Arc V â†’ Arc VI (ascending corpus size and risk; Arc VI additionally coordinates with Mare's pending scrub pass 2).
5. **Acceptance battery per arc = the audit battery re-run.** Residual must be: 0 debris markers, even double-quote counts in every split, 0 crossed delimiters, 0 single-m `human(s)` outside Earth-glosses (none exist in Arcs IIIâ€“VI), king/King census at expected values, splitâ†”umbrella census identity, em-dash canon unchanged.

## 6.1 Phase 0 â€” Decisions (owner: Ainz-sama)

Rule on Â§0.4 list. Mechanical work does NOT wait for these; only the following are gated on decisions:
- X1 outcome determines the delimiter-normalization scope for ~35 thought blocks across the four arcs.
- X2 determines whether an export script runs before the deletion batch.
- Salvage judgments (J-III2/4, J-IV4/6, J-VI2) determine ~5 rewording actions.
Everything else (~330 mechanical fixes + ~1,400 debris-line deletions + all canon-designated take deletions) executes without further input.

## 6.2 Phase 1 â€” Freeze & backup (owner: Demiurge, ~5 min)

1. Snapshot umbrellas: copy `chapter-03/04/05/06.md` â†’ `chapter-0X.md.bak.before_arcs3-6_remediation` alongside.
2. Record SHA-256 baseline of the 4 umbrellas + all 38 splits (baseline file already exists from the audit; re-stamp at phase start).
3. Confirm serving state (port 8790 PID, default\ethra_site) â€” remediation edits content only; no server restart needed, but readers see changes immediately upon regen â†’ schedule the execution window accordingly.

## 6.3 Phase 2 â€” Per-arc umbrella patch pass (owner: execution agent under Demiurge oversight; Arc VI co-executed with Mare)

For each arc, in order:
1. **Deletions:** all Â§4 DELETE rows (debris, superseded takes, markers, prompts, scaffold docs) + gate additions G4 (arc6-01 L528/L439). Volume: Arc III ~250 lines Â· Arc IV ~650 lines Â· Arc V ~430 lines Â· Arc VI ~350â€“400 lines.
2. **Mechanical map:** contractions, standalone-i, Humman spelling (incl. G5 MottledÃ—8, G2/G3 T'vanÃ—3, G1 arc3-04 L93), king-title caps (4Ã— Arc VI), delimiter normalization per X1, quote repairs (arc4-01 L394 close, arc6-01 L641 open, arc4-02 L391 crossed), typos (Arc III 24 + Arc IV 11 + scattered), nested-div fix arc4-05 L438â€“439, stale umbrella heading arc4 L2572.
3. **Editorial actions:** restructure arc4-01 L220â€“222 orphaned speech; reformat 3 Arc V speech-line-wrapped narrative paragraphs (optional); Arc VI E1â€“E4 rewords of draft lines carrying unique content (per decisions); Tamsin scroll numbering (a thirdâ†’a second, arc6-05 L653).
4. **Regenerate:** `python regenerate_chapters.py` (Arcs III/IV/VI heuristic splitter: verify no sentence cut at new boundaries; Arc V anchor splitter: byte-exact expectation).
5. **Mare's Arc VI scrub pass 2 (Â§8.1â€“3) is absorbed into this pass** â€” coordinates identical to G4; no separate edit run.

## 6.4 Phase 3 â€” Acceptance battery (owner: Demiurge)

Per arc: re-run the corresponding `QA/arcN_tooling/` battery against regenerated splits + umbrella census identity check + boundary check. Full acceptance criteria in Â§6.0.5. Any residual â‰  0 â†’ fix-forward in the same phase, no advancement to the next arc.

## 6.5 Phase 4 â€” Lore review (owner: Mare)

Post-battery, Mare runs the Â§9 adjudication workflow over the patched text: CONFIRMED-DRIFT / LEGITIMATE / ADJUDICATE pass against the checklist (name spellings, four/five-families contexts, Styx/Styxian, Sylva/Sylara separation, T'van census should read 3 fewer T'vat). Final sign-off report appended to this workfile.

## 6.6 Mitigation & rollback

| Risk | Mitigation |
|---|---|
| Wrong deletion of story content | Deletion safety rule (Â§6.0.3); every deletion canon-evidenced in Parts Iâ€“IV Â§5; snapshot in Phase 1 |
| Heuristic splitter moves a boundary after deletions (Arcs III/IV/VI) | Post-regen boundary walk (first/last prose line per split) as part of acceptance; anchors Arc V unaffected |
| Wide regex collateral | Line-addressed patching only; maps generated from tooling JSONs |
| Server serves mid-edit content | All edits umbrella-side (not served directly); visible change occurs only at regen step â†’ batch regens per arc, reader-facing diff is one clean cutover per arc |
| Concurrent editing (Mare pass 2 vs remediation) | Sequenced: pass 2 absorbed into Phase 2 Arc VI; no parallel writers on the same umbrella; Demiurge owns the write lock per arc |
| Catastrophic error | Restore `chapter-0X.md.bak.before_arcs3-6_remediation` + regenerate â†’ exact pre-remediation state (hash-verified) |
| Decision latency stalls work | Phase 2 mechanical/deletion work proceeds without decisions; only X1/X2/salvage items held |

## 6.7 Effort estimate

- Phase 1: minutes (scripted).
- Phase 2: the four patch passes are script-executable for mechanical+deletion work (~90% of volume); editorial rewords (~15 lines total) are manual. Estimate: one focused execution session per arc.
- Phase 3: battery runs are automated; review ~minutes per arc.
- Phase 4: Mare review session.

## 6.8 Post-remediation

- Update this workfile with acceptance results + Mare sign-off; re-stamp hash baseline.
- The Arc IV cleaning-pipeline lesson (Mare Â§1.1 caveat): future passes must include the marker classes cataloged here (self-prompts `*...*` directives, synopsis beats "We are in...", "Here's how that could play out", craft-feedback paragraphs, duplicated takes). Recommendation: add a standing pre-publication lint gate using `QA/arcN_tooling/` generalised across all arcs before any future chapter goes live.
- Docs-alignment task (separate): bestiary.md lineage table / world.md / image filenames `Mottled`â†”`Motted` reconciliation per G5 ratification.

*â€” End of workfile. Parts Iâ€“V follow verbatim in concatenated order. â€”*


