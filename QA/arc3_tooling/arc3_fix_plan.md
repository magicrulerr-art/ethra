# Arc 3 Remediation — Master Plan (approved J1-J4; execution spec)

Umbrella master: content/story/chapter-03.md (2894 lines, verified 2026-08-24).
Splits regenerate from umbrella via regenerate_chapters.py at ethra_site ROOT (NOT content/scripts).
Backup: content/story/chapter-03.md.bak_arc3_fix (copy BEFORE any edit).
ALL line numbers below verified against the 2894-line umbrella on 2026-08-24.
Script MUST assert every anchor (content match) and ABORT WITHOUT WRITING on any failure.

## Deletion blocks (original umbrella line numbers; delete bottom-up)

| ID | Lines | Content (verified anchors) |
|---|---|---|
| D1 J1 | 318-327 | Torek version A dialogue block (318-320, contains "I have served four kings,") + premature closing beats 323 ("The elders filed out of the chamber...") and 325 ("The negotiations were complete...") + intervening/trailing blanks. KEEP version B at 328-330 ("I served your father,"). After delete: 315 `</div>`, blanks 316-317, then 328 version B. |
| D2 J2 | 333-354 | "**The Fire Feet — Lore Confirmed**" heading (333) + 7 bullets (336-348) + planning prose (351 ends "...piecing together clues from Ajani's past.") + trailing blanks 352-354. Bullets relocated to QA/bestiary_notes.md FIRST (already present there; dedupe handled separately). After delete: 330 `</div>`, blanks 331-332, then 355 "The chamber had emptied." |
| D3 J4a | 883-908 | Solen confrontation occurrence 1: starts 883 "The Bright Paw elders did not wait for the chaos to subside", ends 906 "The other Bright Paws fell silent, their golden eyes fixed on their young king." + trailing blanks 907-908. CAPTURE joke block 896-898 FIRST (see I2). After delete: preceding blanks, then 909 "**The Hour Before the Tournament**". |
| D4 J4b | 1536-1613 | Battle occurrence 1: starts 1536 "Rask led the charge, her massive frame barreling toward the Motted Paws with the full force of a caravan at full gallop. Tor and Varn flanked her, their formation tightening, their auras blazing." (NO "gold") through stray fragment 1611 `*The basin erupted.*` + blanks 1612-1613. KEEP: 1528 "Glory was the currency...", 1531 thought (normalize in place, see I3), 1533 "The basin erupted.", blanks 1534-1535, then occ2 at 1614 "Rask led the charge, ... their auras blazing gold." CAPTURE good-regents thought 1608 FIRST (see I1). |
| D5 | 1657-1721 | Duplicated incense closer 1657 "The incense stick crumbled into ash. The first phase was over." + recap layers X/Y/Z (1660-1719) + blanks 1720-1721. KEEP layer W starting 1722 (identical incense sentence — the surviving phase closer, per audit §6.2 "recommend keep L553"). |
| D6 | 1945-1947 | Planning transition 1945 "Let's follow the arena as the Styx feathers measure the champions..." + trailing blanks 1946-1947. After delete: blanks 1943-1944, then 1948 "The Pyrinae moved with the quiet efficiency..." |
| D7 J3 | 2452-2454 | Zara Ember-gift beat occurrence 2: paragraph 2452 "Zara watched the exchange from the fence rail... The king was a fan of the fire feet. ... Not tribute. Not politics. A gift from one rider to another." + trailing blanks 2453-2454. KEEP occurrence 1 at 2386-2390. KEEP 2455 (Kareth Eight-Points beat). |
| D8 | 2278-2297 | Mounted phase version A (Rask as rider): 2278 "The incense flared to life, and the arena held its breath. Ajani stood at the edge..." through 2296 + trailing blank 2297. KEEP version B 2298-2321 (Torin as rider; opens with identical sentence). |
| D9 | 2570-2622 | "**Logic**" craft-notes block 2570-2620 (14 paragraphs incl duplicated green-fire para 2620 "The green fire is the mark of that year...") + trailing blanks 2621-2622. After delete: blanks 2568-2569, then 2623 "The third strike was the kill shot..." |
| D10 | 2770-2772 | Compressed feint/concession dialogue block: 2770 `<div class="dialogue-block">`, 2771 `<span class="speech">"The feint,"</span> she said quietly... "I yield. The crown is yours. The regency is mine. And the desert has witnessed."`, 2772 `</div>`. KEEP canon at 2792 ("The feint," acknowledgment in "The crowd erupted. The Styx screamed." block) and 2797 ("I yield" / regency canon). |

Bottom-up order: D10, D9, D8, D7, D6, D5, D4, D3, D2, D1.

## Insertions (after deletions, located by unique content anchors)

### I1 — good-regents thought (J4)
Extracted from 1608: `*'yes they would make good regents, two for two and they're unscathed '*`
Normalized: `'yes they would make good regents, two for two and they're unscathed'`
Anchor A: paragraph starting "Two champions remained standing: Sylva of the Motted Paws, her silver aura flickering faintly, her claws stained with Vex's blood."
Anchor B (must be UNIQUE after D5): line "The incense stick crumbled into ash. The first phase was over." (layer W opener).
Action: set the lines strictly between anchor A and anchor B to exactly: ['', "'yes they would make good regents, two for two and they're unscathed'", ''].

### I2 — breakfast joke fold (J4)
Captured block (verbatim, from 896-898):
`<div class="dialogue-block">`
`<p class="speech-line">"Without even eating breakfast," <span class="speech-attr">muttered a younger elder from the back, and was immediately silenced by a glare from Solen.</span></p>`
`</div>`
Anchor: line containing `You just offered it as a prize. To anyone. Without consulting us.` (occ2 Vasha block), then the NEXT line must be `</div>`.
Action: insert after that `</div>` line: ['', the 3 block lines above].

### I3 — half-of-it-down thought normalize (in place)
Find exact line: `*'half of it down, no one is engaging, it should end soon... They will want glory for their name'*` (must occur exactly once after D4).
Replace with: `'half of it down, no one is engaging, it should end soon... They will want glory for their name'`
(After D4 this line sits immediately before "The basin erupted." + kept occ2 battle — satisfies "relocate before kept battle".)

## See arc3_fix_plan_part2.md for the mechanical replacement map (M1-M29) and assertions.
