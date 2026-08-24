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

