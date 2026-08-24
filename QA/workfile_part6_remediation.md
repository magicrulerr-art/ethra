
---

# PART VI — REMEDIATION PLAN & MITIGATION STEPS (Demiurge)

## 6.0 Principles

1. **Umbrella-first, always.** Every fix lands in `content/story/chapter-0X.md`; `regenerate_chapters.py` re-emits the splits. Never patch a split directly (splits are regenerated artifacts; Arc V round-trip byte-identity is proven; Arcs III/IV use the heuristic word-offset splitter, so boundaries must be re-verified after every regen).
2. **Line-addressed edits, never wide regex.** Replacement maps are keyed to umbrella line coordinates (report §4 tables + gate corrections). Wide regex would strike lines slated for deletion and legitimate words (`ill`, `hell`, "TAKE A REST").
3. **Deletion safety rule.** A block is deletable only if it is pure author meta-text OR a superseded take with a designated canon counterpart. Every deletion in Parts I–IV satisfies this; the sole exceptions needing Ainz-sama are the salvage judgments (X2, J-III2/4, J-IV4/6, J-VI2).
4. **One arc at a time, fully gated, before the next.** Order: Arc III → Arc IV → Arc V → Arc VI (ascending corpus size and risk; Arc VI additionally coordinates with Mare's pending scrub pass 2).
5. **Acceptance battery per arc = the audit battery re-run.** Residual must be: 0 debris markers, even double-quote counts in every split, 0 crossed delimiters, 0 single-m `human(s)` outside Earth-glosses (none exist in Arcs III–VI), king/King census at expected values, split↔umbrella census identity, em-dash canon unchanged.

## 6.1 Phase 0 — Decisions (owner: Ainz-sama)

Rule on §0.4 list. Mechanical work does NOT wait for these; only the following are gated on decisions:
- X1 outcome determines the delimiter-normalization scope for ~35 thought blocks across the four arcs.
- X2 determines whether an export script runs before the deletion batch.
- Salvage judgments (J-III2/4, J-IV4/6, J-VI2) determine ~5 rewording actions.
Everything else (~330 mechanical fixes + ~1,400 debris-line deletions + all canon-designated take deletions) executes without further input.

## 6.2 Phase 1 — Freeze & backup (owner: Demiurge, ~5 min)

1. Snapshot umbrellas: copy `chapter-03/04/05/06.md` → `chapter-0X.md.bak.before_arcs3-6_remediation` alongside.
2. Record SHA-256 baseline of the 4 umbrellas + all 38 splits (baseline file already exists from the audit; re-stamp at phase start).
3. Confirm serving state (port 8790 PID, default\ethra_site) — remediation edits content only; no server restart needed, but readers see changes immediately upon regen → schedule the execution window accordingly.

## 6.3 Phase 2 — Per-arc umbrella patch pass (owner: execution agent under Demiurge oversight; Arc VI co-executed with Mare)

For each arc, in order:
1. **Deletions:** all §4 DELETE rows (debris, superseded takes, markers, prompts, scaffold docs) + gate additions G4 (arc6-01 L528/L439). Volume: Arc III ~250 lines · Arc IV ~650 lines · Arc V ~430 lines · Arc VI ~350–400 lines.
2. **Mechanical map:** contractions, standalone-i, Humman spelling (incl. G5 Mottled×8, G2/G3 T'van×3, G1 arc3-04 L93), king-title caps (4× Arc VI), delimiter normalization per X1, quote repairs (arc4-01 L394 close, arc6-01 L641 open, arc4-02 L391 crossed), typos (Arc III 24 + Arc IV 11 + scattered), nested-div fix arc4-05 L438–439, stale umbrella heading arc4 L2572.
3. **Editorial actions:** restructure arc4-01 L220–222 orphaned speech; reformat 3 Arc V speech-line-wrapped narrative paragraphs (optional); Arc VI E1–E4 rewords of draft lines carrying unique content (per decisions); Tamsin scroll numbering (a third→a second, arc6-05 L653).
4. **Regenerate:** `python regenerate_chapters.py` (Arcs III/IV/VI heuristic splitter: verify no sentence cut at new boundaries; Arc V anchor splitter: byte-exact expectation).
5. **Mare's Arc VI scrub pass 2 (§8.1–3) is absorbed into this pass** — coordinates identical to G4; no separate edit run.

## 6.4 Phase 3 — Acceptance battery (owner: Demiurge)

Per arc: re-run the corresponding `QA/arcN_tooling/` battery against regenerated splits + umbrella census identity check + boundary check. Full acceptance criteria in §6.0.5. Any residual ≠ 0 → fix-forward in the same phase, no advancement to the next arc.

## 6.5 Phase 4 — Lore review (owner: Mare)

Post-battery, Mare runs the §9 adjudication workflow over the patched text: CONFIRMED-DRIFT / LEGITIMATE / ADJUDICATE pass against the checklist (name spellings, four/five-families contexts, Styx/Styxian, Sylva/Sylara separation, T'van census should read 3 fewer T'vat). Final sign-off report appended to this workfile.

## 6.6 Mitigation & rollback

| Risk | Mitigation |
|---|---|
| Wrong deletion of story content | Deletion safety rule (§6.0.3); every deletion canon-evidenced in Parts I–IV §5; snapshot in Phase 1 |
| Heuristic splitter moves a boundary after deletions (Arcs III/IV/VI) | Post-regen boundary walk (first/last prose line per split) as part of acceptance; anchors Arc V unaffected |
| Wide regex collateral | Line-addressed patching only; maps generated from tooling JSONs |
| Server serves mid-edit content | All edits umbrella-side (not served directly); visible change occurs only at regen step → batch regens per arc, reader-facing diff is one clean cutover per arc |
| Concurrent editing (Mare pass 2 vs remediation) | Sequenced: pass 2 absorbed into Phase 2 Arc VI; no parallel writers on the same umbrella; Demiurge owns the write lock per arc |
| Catastrophic error | Restore `chapter-0X.md.bak.before_arcs3-6_remediation` + regenerate → exact pre-remediation state (hash-verified) |
| Decision latency stalls work | Phase 2 mechanical/deletion work proceeds without decisions; only X1/X2/salvage items held |

## 6.7 Effort estimate

- Phase 1: minutes (scripted).
- Phase 2: the four patch passes are script-executable for mechanical+deletion work (~90% of volume); editorial rewords (~15 lines total) are manual. Estimate: one focused execution session per arc.
- Phase 3: battery runs are automated; review ~minutes per arc.
- Phase 4: Mare review session.

## 6.8 Post-remediation

- Update this workfile with acceptance results + Mare sign-off; re-stamp hash baseline.
- The Arc IV cleaning-pipeline lesson (Mare §1.1 caveat): future passes must include the marker classes cataloged here (self-prompts `*...*` directives, synopsis beats "We are in...", "Here's how that could play out", craft-feedback paragraphs, duplicated takes). Recommendation: add a standing pre-publication lint gate using `QA/arcN_tooling/` generalised across all arcs before any future chapter goes live.
- Docs-alignment task (separate): bestiary.md lineage table / world.md / image filenames `Mottled`↔`Motted` reconciliation per G5 ratification.

*— End of workfile. Parts I–V follow verbatim in concatenated order. —*

