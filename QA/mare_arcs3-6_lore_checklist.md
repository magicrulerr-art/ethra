# Mare — Arcs III–VI Lore Continuity Checklist

**Author:** Mare (lore authority, tandem audit) · **Commissioned by:** Demiurge (Ainz-sama's directive)
**Date opened:** 2026-08-24 · **Status:** COMPLETE (all sections filled; one ADJUDICATE item needs Demiurge's ratification)
**Purpose:** Canon continuity checklist for Arcs III–VI, drawn from bestiary/world docs + chapter corpus + raw conversation.
After Demiurge's quality gate, this file is the **adjudication basis** for judgment items in the four
subagent reports (`QA/arc3_audit_report.md` … `QA/arc6_audit_report.md`).

**Usage rule for reviewers:** items marked **CANON** are fixed law — deviations in chapter text are findings.
Items marked **ADJUDICATE** await a ruling (pending Ainz-sama decisions D1–D5 from the Arc I–II audit or new
evidence). Items marked **KNOWN-RESIDUAL** are documented contamination — flag, do not canonicalize (§8).

---

## 1. Umbrella Status Verification (Demiurge item 3)

### 1.1 Arc IV — what pass does current `content/story/chapter-04.md` represent?

**VERIFIED from disk timestamps + sizes (all artifacts on disk, `content/story/`):**

| File | Modified | Bytes | Role |
|---|---|---|---|
| `chapter-04.md.stripped_meta` | 2026-06-18 23:02 | 532,079 | Pass: meta-commentary stripped |
| `chapter-04.md.stripped_passes` | 2026-06-18 23:13 | 509,459 | Pass: stacked draft passes stripped |
| `chapter-04.md_pass3_only.md` | 2026-06-19 05:40 | 57,447 | Extracted pass-3-only fragment |
| `chapter-04.md.repass3` | 2026-06-19 05:55 | 503,185 | Pass: re-pass-3 integration |
| `chapter-04.md.alpha_excise` | 2026-06-20 00:37 | 492,264 | Pass: alpha-content excision |
| **`chapter-04.md` (current)** | **2026-06-20 14:08** | **481,075** | **Final cleaned umbrella** |

**Ruling:** the current `chapter-04.md` is the **latest and final stage of the Arc IV cleaning chain** —
it post-dates `.alpha_excise` (by ~13.5 h and ~11 KB of further excision). Sizes decrease monotonically down
the chain (532,079 → 509,459 → 503,185 → 492,264 → 481,075), confirming strictly reductive passes. All five
artifacts share the identical head (`# Chapter 4: The Consolidation` + opening dialogue-block), confirming
same-lineage, no re-authoring. The Arc IV sub-chapters `chapter-arc4-01..06.md` were **regenerated from this
final umbrella on 2026-06-27 19:38** (all six share that timestamp) — served slices match the final pass.
**Arc IV editorial state: CLEAN/FINAL at umbrella level as of 2026-06-20; slices in sync since 2026-06-27.**
Caveat: "final" = final *meta/draft-stack* pass. Raw-voice dialogue lines (missing apostrophes, lowercase)
survived that pass — see §8 item 4. The pre-cleanup original survives at `raw/chapter-04.md` (510,116 b) —
never served, never audit as canon.

### 1.2 Arc VI — what was the 2026-08-23 17:45–17:51 work, and is Arc VI mid-pass?

**VERIFIED from disk timestamps + memory log `memory/2026-08-23.md` ("Arc 6 OPENS" evening session):**

- `chapter-06.md.bak.before_pass1` (514,876 b, frozen 2026-06-16 23:35) = pre-scrub snapshot.
- `chapter-arc6-04.md` modified **2026-08-23 17:45** (101,328 b): Ch 4 "The Road Begins" — raw author
  planning-bleed (*"On the 7th day… the scene should revolve around…"*) stripped from umbrella + slice.
- `chapter-06.md` (umbrella, 495,904 b) + `chapter-arc6-01.md` (90,556 b) modified **17:51**: Ch 1 "The Cost"
  quadruple-stacked drafts (~12 KB: two "So who can tell me" asks, two cacophony paragraphs, three M'rak
  report passes) deduplicated via `dedupe_arc6_ch1.py` — kept opening + eruption-1 + canonical report pass 3.
  **Canon fix in the same pass:** eruption draft had Seris say Lena was "executed by Mekhmed"; this
  contradicts canon (Lena **missing, fate unknown**) and was corrected to the canon-consistent line.
  Net umbrella reduction: 514,876 → 495,904 b (~19 KB).

**Ruling:** that work was **Arc VI meta-scrub pass 1** (ch4 planning-bleed excision, then ch1 draft-stack
dedupe + Seris/Lena canon fix), applied umbrella-first and re-emitted to the touched slices. **Arc VI is
MID-PASS:** pass 1 is done on record, but a fresh scan today (2026-08-24) found **three residual
contamination markers the pass did not catch** (§8 items 1–3, all with umbrella + slice coordinates).
Subagents auditing Arc VI must treat it as not-yet-final; findings there are expected, not anomalous.

---

## 2. The Attendant-Name Problem: T'van / T'vat / L'vat — ADJUDICATED

**Evidence gathered today (raw conversation = `ethra_full_conversation.json`, the DM/Ainz source of truth):**

| Name | Raw conversation | Chapter sub-files |
|---|---|---|
| T'van | **135** | 44 (arc3 = 10, arc4 = 14, arc5 = 0, arc6 = 0) |
| T'vat | **3** | 3 |
| L'vat | 262 | 92 |

**RULING (resolves pending decision D4 from the Arc I–II audit):** **T'vat is a misspelling of T'van — not a
distinct character.** T'van (young Bright Paw priest, Ajani's loyal attendant, canon from Arcs I–II) continues
as the attendant through Arcs III–IV (24 sub-chapter appearances). All three T'vat instances are drift:
1. `chapter-arc3-01.md` L78: `"t'vat call for the elder council of the striped paws, now please "` (also
   lowercase-t and "striped paws" drift — see §6)
2. `chapter-arc4-02.md` L240: `"T'vat, send in the humans, but before call the royal guards outside…"`
3. `chapter-arc4-02.md` L288: `'I hate her so, so much' - "T'vat, send them in"`
→ **Fix all three to T'van** (preserving the lowercase→capital correction at arc3-01 L78).

**L'vat is unrelated — never conflate.** Canon docs (bestiary.md L118/L310–311): L'vat is a **Lament**
(Lament-avatar of the Mycelial Deep) who trained Ajani (Iris Serpent used in training); the Threx trust Ajani
partly because of it. Neither T'van nor T'vat appears in bestiary/world docs — both are corpus-only characters.

**Note for Arcs V–VI:** T'van has **zero** mentions in Arc V and Arc VI. This is canon (war arc + aftermath;
attendant function absorbed by Kira/Zephyr/scorpions), not missing text — do not flag the absence.

---

## 3. Veylar "Twenty Thousand Years" Canon + World Chronology

**CANON:** the Veylar / sentient-life figure is **twenty thousand years**, always spelled out in prose.
Established as canon in the Arc I–II audit (arc2-06 Version A's "millions of years" was ruled a contradiction
and cut). All Arc III–VI instances verified **consistent** (6 hits, all "twenty thousand years", zero "20,000"):

- arc4-01 L424 — "Sentient life has existed for roughly twenty thousand years" (world chronology anchor)
- arc4-04 L210 — Sylara: "The Veylar have been patient for twenty thousand years."
- arc6-03 L682 — Coral Citadel voice: "We have been patient for twenty thousand years."
- arc6-04 L1129 — Veylar procession "alive for twenty thousand years"
- arc6-05 L161, L388 — Veylar queen / diplomacy "twenty thousand years"

**"Million years" occurrences — RULED LEGITIMATE (do not flag, do not normalize):**
- arc6-02 L987/L1040 — Kyre Tree voice: "I have nothing else to do for the next million years."
- arc6-03 L556 — Tree voice: the scar from the thing out of the belt "took a million years to heal."
- arc6-02 (draft B narration, ~L1010/L1025): the Tree "reaching back across **millions of years** of memory",
  sensations stored "for **millions of years**".
**Ruling rationale:** the narration itself confirms the Tree's memory spans millions of years — the Tree
predates sentient life by orders of magnitude ("Before the Wengari walked the desert. Before the pact. Before
the Lightbringer gave me a name."). 20,000 years bounds *sentient life and the Veylar*, not the Tree. Battery:
never rewrite Tree-voice timescales to fit the 20k figure.

**Full chronological ladder for consistency checks (all canon, from corpus):**
1. **~millions of years** — Kyre Tree's own age/memory (Tree-voice only; the scar from the darkness out of the belt).
2. **~20,000 years** — sentient life on Ethra; Veylar civilization patience.
3. **~5,000 years** — First Tyrant's purge of the Wengari families; Snow Paws fled north (arc5-11); Motted Paws
   "waited five thousand years to be recognized as equals" (arc4-01 L255); Shadow Paws' shame "five thousand
   years" (arc6-04 L662).
4. **~3,000 years** — the Pact / Lightbringer era; Bright Paws as royal family; Pyrinae vassalage ("freed the
   Pyrinae from three thousand years of vassalage" — arc6-04 L4).
5. **~1,092 years** — Tyrant cycle (five Tyrants, Convergence-born, touched by both suns); the Fifth Tyrant
   ~500 years ago; Ajani = the **sixth White Dawn**, "born five hundred years after the Fifth Tyrant—far too
   early by the ancient cycle" (arc4-01 L424).

---

## 4. Humman(s) Spelling Canon

**CANON (established Arc I–II audit, from bestiary.md/world.md consistency):** **"Humman / Hummans"
(double m)** is the race name. Single-m "human/humans" is drift. Two carve-outs still pending Ainz-sama:
- **D3** — adjectival "human" (e.g. "the human quarter", "the human general"): flag, hold for ruling.
- **D5** — lowercase "humman(s)" inside thought-text: flag, hold for ruling.

**Corpus census, Arcs III–VI (sub-chapters, 2026-08-24):**
- ARC3: Humman = 68, human = 3
- ARC4: Humman = 204, human = 3
- ARC5: Humman = 138, HUMAN = 2 (all-caps — check whether shouted dialogue; may be legitimate emphasis)
- ARC6: Humman = 199, **human = 86** ← anomaly

**ADJUDICATE (Arc VI spike) — preliminary ruling:** sampled Arc VI single-m hits cluster in raw-voice passages
(missing apostrophes, scene-direction asterisk blocks — arc6-01 L313/L439/L485/L1042), i.e. unpolished session
text, not a deliberate spelling choice. Note arc6-01 L485 mixes both forms inside one speech ("more hummans
were like you" + "the human quarter"). Working ruling for the battery: treat all single-m tokens as
drift-to-flag; hold adjectival uses for D3; do NOT auto-fix anything in Arc VI until pass 2 (§1.2).

---

## 5. King Titulature

**CANON rule (established Arc I–II audit):** capitalize **King** when used as a title before a name or as
direct substitute for a specific named king's title; lowercase **king** for generic/predicative reference.
Royal formal register uses "the crown" / "This king recognizes you" (arc6-01 L485) — canon register, not error.

**Calibration examples for the battery:**
- `"He is king," Nikolai said` + `"He is not merely a king. He is a White Dawn."` (arc6-04 L4) — predicative
  generic → **lowercase correct**. Do not flag.
- `King Ajani` (arc4-01 L217), `king's favorite mount` (arc3 summary) — title/substitute → capital contexts.
- **"the defeated Tsar of the Snow Paws"** (arc6-05 L1135) — Nikolai's style is **Tsar**, never King of the
  Snow Paws; flag any king/Tsar cross-contamination between Wengari and Ice City contexts.

**Canon titulature litany (arc6-04 L4, Cefiro's ambassadorial summary — use as fact-check anchor):**
Ajani Brightmane = King of the Wengari; the White Dawn; Convergence-born; touched by both suns; renewed the
pact with the lord of the desert (Kyre Tree); trained under the lord of the marsh (L'vat); freed the Pyrinae
from 3,000 years of vassalage; held a tournament and put his crown on the line; survived an assassination
attempt, a coup, a coma, and a war; summoned six elemental spirits and destroyed a Plague creature with a
thunderstorm; united the four families; built offices/councils/trade routes. Arc IV L424 anchor: "the sixth
White Dawn". Any battery finding that implies a different title set is a lore conflict → escalate.

---

## 6. Faction / Race Name Consistency

**Wengari family-count rule — CANON (the corpus explains it; do NOT normalize four↔five):**
- **Four families** is the home-desert political reality from Arc IV onward: Bright, Stripe, Shadow, Motted.
  Ajani formalizes it: "Four families. Four shares." (arc4-01 L239–255), with Bright Paws as the royal family
  ("We are simply the branch that rules").
- **Five families** is correct in: (a) ritual/archaic references (Arc I–II ceremonial prose: "elders of the
  five families" — arc2-01/02/03, arc3-02 L266 "the Five Families had assembled"); (b) the arc5-11 Cefiro
  reveal — Snow Paws are the fifth family, fled north ~5,000 years ago when the First Tyrant purged the others
  (arc5-11 L102/L126); (c) Arc VI homecoming language ("welcomed the fifth", arc6-05 L1135; "He wishes for the
  fifth family to come home", arc6-04 L4; "There are four families now. Five, if you count us", arc6-04 L662).
- **Special case — the white spear symbolism** (arc4-05 L669, Nefere): "Five families. One spear." counts
  four Wengari families + the Pyrinae as the fifth element (fire/water/light/darkness/earth). Legitimate.
- Post-reveal Arc VI prose saying "banners of the **four** families" (arc6-01 L789, arc6-02 L231/L388/L483/
  L1043, arc6-05 L344/L447) is **correct** — Snow Paws not yet resident; their banner is added explicitly as
  new ("the frozen star of the Snow Paws", arc6-05 L344).

**Family names — CANON forms + drift found:**
- **Bright Paws** (lions, royal; Lightbringer bloodline; Four Pillars martial art; "royal family for three
  thousand years"). Arc I–II singular form "Bright Paw" also canon (adjectival).
- **Stripe Paws** (tigers; caravan masters/merchants/mercenaries; Fire Paws style; Zara = Stripe Paw chief;
  Ajani's mother was Stripe Paw — arc4-05 L431 "Your mother was one of us"). Raw conversation: "Stripe Paw"
  = 766, **"Striped Paw" = 0** → "striped paws" at arc3-01 L78 is drift (also lowercase) → fix to "Stripe Paws".
- **Shadow Paws** (panthers; assassins/spies; First Tyrant's shame; Kareth; Black Fire Tide Wolf cavalry).
- **Motted Paws** — **ADJUDICATE (docs vs corpus split):** chapter corpus = **Motted 296 vs Mottled 8**
  (Mottled hits: arc3-02, arc3-05, arc4-03, arc5-11, arc6-01 ×2, arc6-02 ×2). BUT bestiary.md's lineage table
  (L24: "Mottled Paws | Jaguars | Rune Belt") and world.md L120 say "Mottled Paws", while bestiary L231 body
  says "Motted Paws" and image assets are "mottled-paw.*". **Mare's recommendation:** standardize on
  **Motted Paws** in story text (corpus 97 %+ majority + Demiurge's directive spelling); treat the 8 chapter
  "Mottled" hits as drift; leave bestiary table/world.md/image filenames for a separate docs-alignment task
  (flag, don't silently edit docs during the audit). Needs Demiurge ratification.
- **Snow Paws** (snow leopards; fifth family; Ice City; Sunraptor riders; Cefiro = Snow Paw **prince**, styled
  "Peregrine" in bestiary L296 — "Snow Paw Peregrine Cefiro"; Tsar Nikolai; Nadya).
- **M'rak, Yvaria, Irek, Toren, Kira, Pearl** (Arc V principals — note M'rak is a Wengari commander, Yvaria
  rides/commands ghosts with a silver-furred drum; bestiary confirms "the Motted Paws speak to [Ghosts]
  through drums" — cross-consistent ✓).

**Other races — CANON forms:**
- **Veylar** — Shell-Singers, Tide-Wardens, Deep-Watchers; Petal-Shells; Resonant Network; Coral Citadel;
  Tidepools; queen in Arc VI (living-coral chair carried from the Tidepools); Xal'thyra = Veylar Tyrant, only
  Styx-rider. "Sylara" = Shell-Singer of record (Arc II+).
- **Pyrinae** — rune-glass artisans, Hydromancers, Styx-feather trade; vassalage ended by Ajani; Nefere
  (notable, spear-forging); the **Sun-Walkers** are a Pyrinae order (Mira = Nefere's most trusted, arc4-06
  L556). Rune Belt is their territory (Ghost bats, Razor Hares, kyre flowers).
- **Hummans** — mercantile empire; capital **Verdantis**; Amuk siege-beasts; generals **Mekhmed** and
  **Tamsin** (Tamsin defected, honored by Ajani — arc6-01 L485); "Golden Cloaks" = Humman/Wengari? unit
  risen during the war (arc6-01 L297-region) — [battery: if a lint flags "Golden Cloaks" as unknown term,
  LEGITIMATE]; coiled-scorpion banner (arc6-05 L344).
- **Threx** — Lament / Quick / Rooted forms; the Deep; L'vat (see §2); mycelial-web banner (arc6-05 L344).
- **Styx** — **a flying-creature species, NOT a faction** (omens; feathers; ridable only by Xal'thyra; prey =
  Razor Hares). Battery: never merge **Styx** with **Styxian** (the Wengari capital) or **Styxian**
  adjectival; 166 "Styx" substring hits in sub-chapters include heavy "Styxian" use. "Styx crown" (arc6-01)
  = regalia named for the creature. Dragari = ancient myth-tier singers (gave Cefiro the pearly medallion).
- **Chi'Thak** = the Blight (spawned the Plague creature of Arc V). **Plague weapons** = old-world weapons
  from **Velarius**, given to the Humman king by a shape-wearing shadow (arc6-02 draft B — canon reveal).

**Other named-figure drift watch:** **Sylva** (canon; raw conversation = 860) vs **Sylvia** (raw = 3; chapter
corpus = 1 hit: arc4-02 L240 "call Sylvia") → **Sylvia is drift → fix to Sylva.** Note Sylva is the Motted
Paw / council figure who becomes **Regent** during Ajani's coma (Arc IV→VI; see §7 Arc VI). Do not confuse
Sylva with **Sylara** (Veylar Shell-Singer) — distinct characters, similar names, battery should treat any
Sylva↔Sylara substitution as a critical lore error.

**Arc IV–VI recurring cast (flag any spelling drift):** Ajani Brightmane, Kareth, Zara, Nyasha, Seris
(Humman ambassador), Sylara, Elyra (Motted Paws; grimoire of Flowing Water; carries the regency burden per
arc6-01), Solen (aged Bright Paw High Priest), Anktor (True Dawn rival claimant, Arc IV), Nefere, Mira,
M'rak, Yvaria, Irek, Toren, Kira, Pearl, Black Fire, Red Fire, Mekhmed, Tamsin, Zephyr (legion commander;
shadow riders, arc6-04 L1129), Cefiro, Nikolai, Nadya, Maren (pensions/reparations officer, arc6-01 L313),
Vasha (arc5 opener "Vasha Storms In"), Lena (Sylva's maid — see §7).

---

## 7. Arc-Specific Canon Facts (invisible to mechanical audit)

**Arc III — "The Tournament"** (5 chapters, 44,077 words; subs: The Arena / First Blood / The Fire Feet /
The Tyrant Cycle / The Hour Before):
- Ajani **puts his crown on the line** in the tournament (retrospectively confirmed arc6-04 L4). Fire Feet =
  arena mounts (Ember is one: "She carried you through the marshes for a year" — arc4-05 L431).
- Canon events referenced later: the broken warriors of his own blood / the apology (arc-03 summary), Sylva's
  arena intervention (silver-furred, arc3-05), the Tyrant Cycle lore reveal. T'van present (10 mentions).
- Known drift: arc3-01 L78 (`t'vat` + `striped paws`, §2/§6). "Five Families" ceremonial assembly (arc3-02
  L266) — legitimate per §6 family-count rule.

**Arc IV — "The Consolidation"** (6 chapters, 78,195 words; subs: Bureaucracy / The Caravans / The Pyrinae
Accord / The Humman Delegation / The Gifts / Aftermath):
- Umbrella = final pass state (§1.1). Bright Paws "royal family for three thousand years" (Solen, arc-04
  summary). Four-families settlement (arc4-01 L220–255; note L220 is a raw-voice line — §8 item 4).
- Veylar delegation opens the Pyrinae Accord (living coral for the hanging gardens); Humman delegation chapter.
- Gifts: Ember + ceremonial barding of all four families (Stripe Paws/Zara); grimoire of Flowing Water (Motted
  Paws/Elyra); the white spear of five elements (Nefere, arc4-05 L669 — §6 special case).
- arc4-06 = coup crisis: the **True Dawn faction** (canon name; arc4-06 L492/L505/L556/L584) argues Ajani is
  incapacitated ("the armor had rejected him"), invokes birthright; **Anktor** is the silent rival claimant;
  Elyra reports; Nefere + Mira the Sun-Walker + a razor hare set out pre-dawn; Sylva heads the war table
  ("the king wakes or the city fell"); the **Humman army arrives with the sunrise** — bridge into Arc V.
- arc4-01 L424 = world-chronology anchor paragraph (moon/axial tilt, 20k years, 1,092-year cycle, sixth White
  Dawn) — any contradicting number anywhere in Arcs III–VI is a critical finding against this paragraph.

**Arc V — "The Great War"** (22 chapters, 47,706 words; the timestamp arc):
- Structure canon: every chapter opens on a timestamp, canonical formula "It was X:XX in the morning, the
  seventh day of the Month of Storms, in the first year of the reign of Ajani Brightmane…" — 22 timestamps
  05:25 → 12:06 (~7 real-time hours). Sub-titles ARE the timestamps ("05:25 — Vasha Storms In").
- Siege of Styxian by the Humman army: Mekhmed, Tamsin, Amuk siege-beasts, scorpion riders, the Wohs;
  defenders: M'rak, Yvaria + ghosts, Irek, Toren, Kira, Pearl, Black Fire & Red Fire, Nefere, the Golden
  Cloaks, the wall, the northern wall victory. Ajani summons six elemental spirits and kills the Chi'Thak
  Plague creature with a thunderstorm; falls into a coma (the coup of Arc IV's True Dawn overlaps).
- arc5-11 = Cefiro reveal (§6: fifth family, Dragari medallion, prophecy "the bulwark of paws will rise").
- T'van absent (0 mentions) — canon, §2.
- Battery note: `content/story/arcs/arc-05.md` (summary file only) shows **mojibake** ("### 05:25 ƒ?" Vasha
  Storms In" — double-encoded em dash). Encoding anomalies in CHAPTER text are findings; in the summary file,
  known and separate.

**Arc VI — "Aftermath & The Road"** (5 chapters, 80,677 words; subs: The Cost / Rebuilding / The Vision /
The Road Begins / Epilogue) — **mid-pass, see §1.2**:
- The Cost: throne room = hospital ward + war council + family gathering; Ajani in bed; bracers now "simple
  wrist wards barely a claw long"; Black Fire & Red Fire full-size (~2 m male / ~1.8 m female) on his arms.
- Canon reckoning scene (arc6-01 L295–313): M'rak exposes the Council's secret war-prep ("we brought
  regiments instead of legions… the fifth and sixth didn't come. The messages never reached them"); **Sylva
  confesses and tenders her resignation — Lena was HER maid and a spy**: copied correspondence, learned guard
  rotations, sent letters to Verdantis for weeks; Humman army disguised as "a hundred scorpions… a trade
  mission". Ajani refuses the resignation: "you fought to be regent now bear the weight till it's taken from
  you." **Lena's canon state = missing, fate unknown** (NEVER "executed by Mekhmed" — that was the draft line
  fixed 2026-08-23).
- Rebuilding: memorial pillar + celebration; Kyre Tree scene (draft B is canon — §8 item 3): a shape-wearing
  shadow gave the Humman king old Plague weapons from Velarius; the Tree remembers what passed over the desert
  millions of years ago ("the same darkness. The same hunger… out of the belt" — connects to the canon entity
  "the one in the Rune-Belt"); "You destroyed its weapon. You destroyed its creature. You did not destroy it."
- The Vision: Ajani + Blackie/Reddy through the great bronze doors; "The Road" policy continues.
- The Road Begins: Cefiro presents the royal seal to **Tsar Nikolai** on the frozen landing platform, Ice
  City; "The starving boy who wandered into our city three years ago is now a king"; formal diplomatic
  relations + invitation for the fifth family to come home. Sepia-vs-cold palette question was cover-side only.
- Epilogue: four Heavenly Generals + first Knight of the Wengari named (arc6-05 L1135); atrium with four
  family sigils + allied-race banners + the frozen star of the Snow Paws raised for the first time; Veylar
  queen attends via carried coral chair / Shell-Singers (diplomatically absent in person — arc6-05 L388
  analysis is canon intent); Resonant Network reveal (arc6-03 L682); Yvaria's ghosts find their voice;
  Nadya: "He's taller than I remembered"; "the defeated Tsar of the Snow Paws" (arc6-05 L1135 — cite verbatim;
  do not speculate beyond the line).

---

## 8. Known Residual Contamination — DO NOT CANONICALIZE (all coordinates verified 2026-08-24)

1. **"We switch to" bath-scene planner line** — `chapter-06.md` L527 ≡ `chapter-arc6-01.md` L528:
   `<p class="speech-line">We switch to the night at the throne room ajani is taking a bath the bracers have
   become simple wrist wards barely a claw long, Cefiro is next to him…</p>` — user-planning "we-switch-to"
   bleed in a speech-line wrapper (same family as Arc V excisions, cuts 10–16). Missed by pass 1. The scene
   facts inside (bracers→wrist wards, Cefiro) ARE canon (§7); the wrapper sentence is not prose.
2. **Asterisk scene-direction block** — `chapter-06.md` L438 ≡ `chapter-arc6-01.md` L439: `*The next scene
   is a couple of hours after ajani is sitting on the throne now… then we see zephyr bringing Tamsin in
   chains… seris is also there but her face is Unreadable*` — planning voice in thought-style italics; the
   scene facts are canon (Tamsin in chains, arc6-01 L485 pays them off), the block itself is residue.
3. **"I like it, let's write it" approval marker + Tree-scene double draft** — `chapter-06.md` L2035 ≡
   `chapter-arc6-02.md` L990. Structure: [draft A tail, arc6-02 ~L975–989, ending "…next million years."] →
   marker `*I like it, let's write it*` → [draft B, the full canon scene: "The descent into the inner chamber
   had become familiar…", containing the pool-vision + Velarius-weapons lore, ending L1040 "…Now go. I am
   hungry."] → continuation L1043 "Two weeks had passed…". **Canon = draft B + continuation; draft A tail +
   marker are residue.** Exact excision boundaries: from the start of the duplicated "The roots pulsed once…"
   tail back through the marker — editor must locate where draft A's tail begins (search upward for the first
   scene opening preceding L975) before cutting; do not cut blind.
4. **Class note — Arc IV raw-voice lines survived the final pass** (e.g. arc4-01 L220: "thats because we call
   ourselves five families but we have been four for years, bright paws, shadow paws, motted paws, stripe
   paws, were actually just four..."). Arc IV umbrella is final for meta/draft-stack removal but NOT
   line-polished. Battery grammar findings on Arc IV are genuine findings, not pass-status artifacts.
5. **Class note — Arc VI raw-voice passages** (arc6-01 L313 speech-line: missing apostrophes, "theyre",
   French-accent "réparations/régent"; also L1042 "the humans have more than once city" [sic, "one"]). Same
   treatment as item 4: genuine lint findings; also feeds the §4 Arc VI human=86 anomaly.
6. **Summary-file-only:** `content/story/arcs/arc-05.md` heading mojibake ("05:25 ƒ?"). Not chapter text.

---

## 9. Adjudication Workflow (post quality-gate)

1. Each subagent report item receives one verdict: **CONFIRMED-DRIFT** (fix per canon above, cite §),
   **LEGITIMATE** (canon exception, cite §), or **ADJUDICATE** (needs a ruling from Demiurge/Ainz — currently
   queued: D1 em-dash style, D3 adjectival "human", D5 lowercase "humman" in thoughts, and new: Motted/Mottled
   docs-alignment (§6), Arc VI pass-2 execution order vs corrections (§1.2)).
2. This checklist's section numbers are the citation basis for all lore calls.
3. Arc VI findings must carry the **mid-pass caveat** (§1.2): some will be resolved by Mare's scrub pass 2
   (items §8.1–3 already queued) rather than by audit corrections — coordinate before editing.
4. Umbrella-first rule for any fix: edit `content/story/chapter-0X.md`, then `python regenerate_chapters.py`;
   never patch only the slice (Arc I–II audit architecture finding; heuristic splitter — verify split
   boundaries after regen). `raw/` copies are untouched originals by policy.

---
*All sections COMPLETE. Evidence: disk timestamps/sizes, `memory/2026-08-23.md` + `memory/2026-08-24/*`,
raw-conversation name census (135 T'van / 3 T'vat / 860 Sylva / 3 Sylvia / 766 Stripe Paw / 0 Striped Paw),
corpus grep 2026-08-24. Sole ratification pending with Demiurge: Motted-vs-Mottled standardization (§6).*
