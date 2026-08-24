# Ethra QA Report — Arc VI ("Aftermath & The Road") PROACTIVE Audit

- **Prepared by:** Demiurge's audit subagent — script-first QA audit using the Arc I–II defect battery (`QA/*.py`, copied & adapted into `QA/arc6_tooling/`).
- **Date:** 2026-08-24
- **Scope:** `content/story/chapters/chapter-arc6-01.md … chapter-arc6-05.md` (published splits, primary targets) + `content/story/chapter-06.md` (umbrella master, 495,904 B; grep + targeted line reads only). READ-ONLY throughout — no story content modified.
- **Mode:** PROACTIVE — no reader feedback exists for Arc VI; defect battery per `QA/arc1_arc2_reader_feedback_report.md`.

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

> **Recent-modification note:** arc6-01, arc6-04 and the umbrella were modified 2026-08-23 between 17:45 and 17:51; the umbrella shrank ~19 KB vs its pre-pass1 backup, i.e. a **pass-1 cleanup already ran** (explicit "Let me rewrite…"/"Here is the correction" markers now 0 hits). This audit covers the CURRENT residual state.

- **Artifacts:** `QA/arc6_tooling/` — arc6_lint.py (+results JSON/summary), arc6_quote_pair.py (+.txt), arc6_delim_cross.py (+.txt), arc6_em_classify.py (+.txt), arc6_tally.py (+.txt), arc6_hyphen_audit.py (+.txt), arc6_umbrella_scan.py (+debris .txt/.json).
- **Status:** see §7.

---

## 1. Executive Summary

Arc VI's **polished prose is canon-healthy** (king/King ≈ fully compliant; em-dash usage ≈ fully compliant; Ajani's thoughts single-quoted throughout; no missing-apostrophe contractions in polished text) — but the arc is the **dirtiest in the corpus for draft debris**: whole draft/synopsis beats, author directives, craft-feedback blocks and duplicated scene versions were published inside all five chapters and remain in the umbrella master.

**Counts by defect class (full detail §6):**

| Class | Count | Nature |
|---|---|---|
| MECHANICAL (scriptable closed map) | **59 fixes** | 1 missing opening quote (arc6-01 L641, root cause of whole-file quote imbalance) · 4 "king of the Wengari/humans" formal-title capitalizations · ~50 single-m `human(s)` → `Humman(s)` (concentrated: arc6-03 ≈ 35) · 2 lowercase `humman(s)` capitalizations · 2 `again.M'rak`/`with it.The` concatenations (both inside blocks already slated for deletion) |
| DEBRIS (author meta-text — delete) | **~62 individual lines + 12 blocks (≈ 350–400 lines total)** | draft beats, synopsis beats ("We are in the gardens…"), author directives ("*I like it, let's write it*"), planning notes, craft-feedback paragraphs (one block duplicated across arc6-03 AND arc6-04), scaffold headings (**The Halberd User (Nikolai)** etc.), 6 duplicated scene versions |
| EDITORIAL (judgment deletion/reword) | **7 items** | draft-format lines carrying unique scene content (need reword, not just delete); V1/V2 scene-version selection with unique beats; thought-style consistency (Nikolai's `*...*` thought) |
| JUDGMENT (needs Ainz-sama) | **3 items** | J1 arc6-05 Maren-report V1/V2 contradiction · J2 arc6-04 dinner V1 unique beats salvage · J3 whether craft-note blocks are archived elsewhere before deletion |

**Top findings:**
1. **arc6-01 L641** — Cefiro's Sunraptor paragraph is missing its opening `"`; this is the single root cause of the whole-chapter quote imbalance (file total 395 double quotes = odd). One-character mechanical fix.
2. **Six duplicated scene blocks published in full**: arc6-02 Kyre-Tree scene ×2 (canon = 2nd); arc6-03 L'vat strike scene ×3 (canon = 3rd); arc6-04 Snow-Paw dinner ×2 + Nikolai laugh ×2 (canon = 2nd each); arc6-05 M'rak exaltation reactions ×2 + Tamsin investiture ×2 (canon = V2, proven by downstream refs to "Knight of the Golden Claw").
3. **arc6-03 carries ~35 single-m `human(s)` tokens in polished prose** — the largest Humman-spelling concentration in the arc (e.g. L120, L226, L252, L307, L384, L491, L641, L831).
4. **Craft-feedback blocks published as story text**: arc6-02 L779–790; arc6-03 L866–891; arc6-04 L1148–1190 (the arc6-03 block copied verbatim + extras) and L1230–1264 (scaffold headings **Feedback on the Combat Choreography**/**The Halberd User (Nikolai)**/**The Four Pillars User (Ajani)**/**The Verdict**); arc6-05 L133–140, L295–316, L378–406, L684–708.
5. **Umbrella chapter-06.md retains ALL of the above** (pass-1 removed only explicit rewrite markers) — fixes must be applied to the umbrella, then re-split.

**Arc health verdict:** NOT reader-ready. The underlying polished narrative is high quality and nearly canon-clean, but ~12–15% of published arc text is non-story material. Remediation is overwhelmingly mechanical deletion + one closed map (Humman spelling); the judgment items are few and well-bounded.

---

## 2. Per-Chapter Defect Catalog

Line numbers refer to the published split files. "Polished twin" = the rewritten version that makes the flagged line deletable.

### 2.1 chapter-arc6-01.md (90,556 B)

**Debris (author meta / draft formatting):**
- **L123** — draft beat: `Next scene beats >When all have said their piece Lira speaks angrily "WHAT !? I THOUGHT THE WENGARI AND THE HUMMANS WERE BROTHERS..."` (polished twin L134).
- **L197** — draft-format Ajani line in `speech-line` markup: `"well now that's out of the way, I need the talky, M'rak..."` — **carries unique scene content** (the "how many did we lose" question); no polished twin found → EDITORIAL reword (J4).
- **L313** — draft hybrid `'hmm the council worked as designed I'll need to reward them...' - "The resignation is not accepted..."` (single-quote thought + `' - '` separator; lowercase).
- **L443** — draft hybrid `'so these are the ones' - "So you are the ones who unleashed Velarius madness..."` (lowercase `velarius`).
- **L485** — draft-format Ajani line: `"Ambassador these are your people, deal with them as you see fit..."` (uncapitalized start, run-on).
- **L905** — author directive: `*Now let's see Yvaria, Reva, lira and vex*` (lowercase names).
- **L963** — draft hybrid: `'its worse than I thought ' - 'call for Maren please'` (missing apostrophe `its`→`it's`; both segments single-quoted).
- **L1042** — draft beat: `'theyre brutes, brutes !' - "Generals I meant from Verdantis not the humans currently in the city..."` (polished twin = arc6-02 L4; note the twin also carries single-m "humans").

**Mechanical defects (polished text):**
- **L641** — Cefiro's Sunraptor paragraph: closing `"` present, **opening `"` missing** (also not wrapped in dialogue-block like neighbours). Root cause of whole-file quote imbalance. Fix: prepend `"` (MECHANICAL).
- **L192** — formal title lowercase: `...holder of Luxor, king of the Wengari.` → `King of the Wengari` (canon rule 1).
- **L1011** — `"Generals it appears we will need to ask for reparations from the hummans...what is your recommendations for achieving so ?"` — lowercase `hummans`; grammar `what is your recommendations` → EDITORIAL reword.

**Quote balance:** ascii double quotes = 395 (odd) → walk desyncs from L641 to EOF (`arc6_quote_pair.txt`); single root cause above.

**king/King:** compliant apart from L192. **Em dashes:** all CUT/TAIL/elaboration uses canon-compliant. **Ajani thoughts:** single-quoted in all draft lines (L147, L313, L443) — no asterisk thoughts.

### 2.2 chapter-arc6-02.md (103,268 B)

**Debris:**
- **L176** — draft beat: `After the meeting ajani goes down to the inner chamber , and extends his hand to the flower "I'm here this is what happened"...` (polished twin L180+).
- **L352** — draft-format promotion speech (`"I am promoting these four to two star generals..."`; lowercase `hummans coin`, `wengari`; run-on) — verify polished twin before delete, else reword (J4).
- **L486** — author directive: `*Let's look at the immediate aftermath of ajani leaving the room, Seris is waiting outside...*`
- **L489** — synopsis beat: `We are in the gardens, Cefiro tells Ajani he's seen enough and he must return home...`
- **L585** — draft beat: `after the war council ajani tells Cefiro to rest but before Cefiro takes his leave, ajani takes out his royal seal...`
- **L672** — synopsis beat: `We are in the throne room the very next day, Ajani is meeting with seris in a visibily more relaxed maner...` (typos `visibily`, `maner`; lowercase `ajani`, `seris`, `sylva`, `hummans`).
- **L779–790** — craft-feedback block (4 paragraphs): `The chapter is working on all three fronts you've identified.` + analysis of the Humman reaction, the interrogation, Ajani's behavior. Contains cross-chapter copy sentence `her question—'if you are truly sorry, why did you not chase after mekhmed?'—is the blade that cuts through the paper shield.` (also in arc6-03/arc6-04 blocks).
- **L895** — author directive: `*You can write the next scene you have full creative authority it should be a few hours later seris questioning salahim outside the gate*`
- **L898** — draft beat: `Seris goes to report to ajani he was waiting inside the gates leaned on a wall...`
- **L948–988** — **Kyre-Tree scene V1** (duplicate). Opens directly with `*You are here again. You have questions. Ask.*`; its tail `*The memorial celebration will bring pilgrims...*` (L987) is folded into V2's closing paragraph L1040. **Canon = V2 (L992–1041)**, which has the descent transition (L992), Ajani's spoken line (L996) and the consolidated ending. Debris between: **L990** author approval `*I like it, let's write it*`.

**Mechanical defects (polished text):**
- **L4** — `Not the humans currently in the city. The Hummans have more than one city...` — single-m `humans` mixed with correct `Hummans` in one breath → `Hummans` (MECHANICAL).
- **L710** — `A human dismounted from the lead hawk.` → `A Humman` (Sultan's party = Hummans).
- **L714** — `I am the great Sultan Salahim, king of the humans.` → `King of the Hummans` (formal proclamation title + spelling; MECHANICAL, 2 fixes in line).

**Consistency notes (not hard rule-3 violations — rule covers Ajani):** L693 shared Wengari+Humman thought in `*...*` (`*Not again. Please, not again.*`); Tree telepathy `*...*` (L208–225) is the established canon format for the Tree. See §6.3 J3.

**king/King:** `Sultan Salahim` (title+name) correct; `king of the humans` L714 flagged above. **Em dashes:** compliant (L782/L785 are inside the craft block slated for deletion).

### 2.3 chapter-arc6-03.md (102,345 B)

**Debris:**
- **L78** — synopsis beat: `A few hours later ajani is helping everyone on the wall, he explains that he can feel where the wall is weakest...` (`theyre`, lowercase `ajani`).
- **L133** — draft beat: `Then without warning the lament extends a limb and touches ajanis forehead, a light passes between them then too fast for anyone to react it snaps the back of ajanis head...` (`slawjacked`).
- **L137–190** — **L'vat strike scene V1** (duplicate): `The Lament's limb touched Ajani's forehead` … `STUPID DISCIPLE!` … `It always is with you. Explain. Now.` (L190).
- **L194–228** — **L'vat strike scene V2** (duplicate): `Then L'vat spoke. His voice was not the booming shout...` … `Tell them the humans fought on the wall.` (L226).
- **L230–272** — **L'vat strike scene V3 = CANON** (final rewrite; `The Deep felt the elements shift`; resolves with `Stand down. The White Dawn vouches for them.` L272). Even canon V3 carries single-m fixes: L230, L252, L256, L262, L267.
- **L277** — draft beat: `We see a humman mother and daughter can't be more than four hugging each other...` (polished twin L281+, which carries `humman woman` lowercase fix).
- **L318** — draft line: `Ajani very flustered says "I apologize for our guests humman cubs are very curious she meant no offense"...` (polished twin L323 — which carries single-m `Human cubs` fix).
- **L610** — draft beat: `*Ajani has returned to the throne room for the afternoon, the threx are touring the city like children...*`
- **L710** — draft line: `Ajani looks towards sylva and says "call for zephyr and Yvaria, tell them its urgent"` (`its`→`it's`).
- **L765** — draft beat: `"Ambassador please tell them Wich direction to take" , we move three days ahead the threx are getting ready to...` (`Wich`).
- **L866–891** — craft-feedback block (9 paragraphs: L866, L869, L871, L875 [inside a dialogue-block div], L879, L881, L884, L888, L891). **Duplicated verbatim into arc6-04 L1148–1171** (see §5.7).
- **L895** — synopsis beat: `Let's now follow Cefiro and Kira, they are lost again Kira is chastising Cefiro "YOU SAID YOU REMEMBERED THE WAY!!"...`

**Mechanical defects (polished text):** ~35 single-m `human(s)` tokens — the arc's worst cluster. Key lines: L120 (`'The humans fought on the wall,' L'vat said flatly. 'The humans fought on the wall. Tell them.'`), L128, L161, L217, L221, L226, L230, L252, L256, L262, L267, L307, L323 (`Human cubs`), L351, L356, L384, L403, L407, L416, L420, L491 (`To a human, they were cheap souvenirs`), L511, L578, L583, L641 (`Humans and Wengari fighting side by side`), L735, L773, L802, L831. Plus capitalization: **L281** `The humman woman was perhaps thirty` → `Humman woman`.

**king/King:** fully compliant — the single capitalized `King` in the chapter is **L606 `King Ajani`** (title+name, canon).

### 2.4 chapter-arc6-04.md (101,328 B)

**Debris:**
- **L36–145** — **Snow-Paw dinner scene V1** (~110 lines, duplicate). Contains the Velarius-knowledge inconsistency (`L87 ...deployed weapons from Velarius.` — Snow Paws are isolated, cannot know Velarius) plus a dangling mid-sentence dash at **L41** (`...if she was tired, if she had ever seen a white bear, if she—` paragraph ends there). **Canon = V2 (L149–313)** — V2 removes Velarius, adds the Snow-Paw interruptions demanded by the corrections note, and flows into the arena scene. V1 carries unique beats (see J2).
- **L146** — author directive: `*We follow them to the dinning room Ivan is trying very hard...*` (typo `dinning`).
- **L315** — author corrections note: `*/corrections 1) the snow paws are isolated they don't have idea who Velarius is... if you agree let's rewrite the scene*` — its demands ARE implemented by V2; note is debris (out of place after V2).
- **L318** — draft beat: `Before they have taken ten paces Kira takes out her Wooden saber and shouts "TAKE THAT BACK!, NO ONE CAN BEST AJANI!!"...` (polished twin L323+).
- **L641** — draft beat: `Later at night Nikolai ask Cefiro 'so, the Truth son, when do we meet with Ajani ?'...` (polished twin L649+).
- **L715** — draft beat: `The next day at breakfast Nikolai announces 'today we start teaching the kids !...'` (`kiras`; polished twin L719+).
- **L1101** — author directive: `*Let's follow them in the journey we learn Nikolai like Ivan is a fan of the wurms...*`
- **L1105** — draft beat: `The journey is uneventful , Kira learns snow paw history and customs and is surprised to learn Nikolai's grandfather was humman...`
- **L1148–1190** — craft-feedback block: the arc6-03 block copied verbatim (L1148, L1152, L1154, L1158 [inside dialogue-block div], L1162, L1164, L1167, L1171) + arc6-04 extras (L1174 Cefiro/Kira journey, L1176, L1179 lore drops, L1181, L1184, L1188, L1190).
- **L1194** — draft beat: the full sparring fight as one run-on synopsis ending in the lowercase salute `This Ajani brightmane... king of the wengari salutes Nikolai silver pelt... welcome home uncle` (polished twin L1202–1226).
- **L1221** — **Nikolai laugh V1** (`A long silence. Then Nikolai threw back his head and laughed—...` ending `The Snow Paws are honored to come home."`). **Canon = L1226 V2**, which adds the formal salute (`Nikolai Silverpelt, champion of the frozen wastes... salutes Ajani Brightmane...`).
- **L1230–1264** — scaffold block: headings `**Feedback on the Combat Choreography**`, `**The Halberd User (Nikolai)**`, `**The Four Pillars User (Ajani)**`, `**The Verdict**` + analysis paragraphs (L1236, L1243 `When Ajani dodged sideways, Nikolai switched to a wide sweep. This is correct—a sweep converts...`, L1246, L1253, L1264).
- **L1270** — draft beat: `Everyone cheers for Ajani everyone but l'vat who approaches and unceremoniously starts critiquing him...` (polished twin L1305–1321).

**Mechanical defects (polished text):**
- **L247** — Tyrant list: `The Fifth was Velarius Vane. Human.` → `Humman.` (race-name label parallel to `Veylar`, `Bright Paw`).
- **L256** — `...the last of them was human. The weakest race on Ethra produced the worst monster.` → `Humman` (MECHANICAL; in-character but race-name).
- **L266** — `A human nearly destroyed the Wengari. We remember.` → `A Humman`.
- **L1216** — polished salute: `...caller of spirits, king of the Wengari, salutes Nikolai Silverpelt...` → `King of the Wengari` (formal title; MECHANICAL).
- **L1226** — `...salutes Ajani Brightmane, first of his name, White Dawn, king of the Wengari.` → `King of the Wengari`.

**Consistency note:** L1321 Nikolai's thought in `*...*` (`*That's an incomplete form,* he thought.`) — rule 3 binds Ajani only; flag for J3. L528–530 Kira's remembered Ajani-lesson: quoted speech inside `*...*` across a blank line — file-level quote balance OK; stylistically fine, note only.

### 2.5 chapter-arc6-05.md (103,032 B)

**Debris:**
- **L129–140** — planning block: L129 `Now we enter a sub arc "the great célébration !!" It will be exposition heavy and light hearted, I'll cover a month`; L133 `The Great Celebration is the right structural choice...`; L137 political-function paragraph; L140 `I am ready to begin whenever you are. What is the first beat of the Great Celebration?` (assistant dialogue).
- **L144** — synopsis beat: `It's the afternoon of the same day everyone has already settled in the throne room ajani is meeting with sylva...`
- **L238–248** — **Maren report V2 fragment** (duplicate start of the scene; see J1). V1 = L165–234 (complete, ends `The court dispersed into the afternoon light...`).
- **L253** — synopsis beat: `Ok next one is a MASSIVE scene, we start from the palace it's early morning an hour before dawn ajani is wearing an uncharacteristic black robe... 40 coffins...`
- **L295–316** — funeral craft-feedback block (L295 silence, L298 multi-species procession, L304 speech analysis [inside speech-line markup], L311 not-turning beat, L314 — contains its own **internal duplication + concatenation** `...And the reader mourns with it.The scene earns its silence...`, L316 transition note).
- **L342** — synopsis beat: `*Ajani declared the day a mourning day. The city closed. The market stalls went dark...*`
- **L378–406** — throne-room craft-feedback block (L378 three-throne configuration, L383 Nikolai on the left, L401 coalition made visible, L404 diplomatic-tradition paragraph incl. real-world `English royalty visited the French court` gloss, L406?).
- **L410** — draft beat: `Ajani stands and sylva passes him a scroll he unrolls it and proclames 'Yvaria whisperwind, Sephyr flamebound, Reva firepelt, M'rak brightmane present yourselves to the crown!!'` (polished twin L418; note `Sephyr` vs canon `Zephyr`).
- **L466** — draft M'rak citation: `"For believing when no one believed, for being the first and last bulwark in the line of duty..."` (lowercase commas version). **Canon = L474** (periods/capitals version).
- **L493–511** — **duplicated polished M'rak block**: L493 is a concatenation defect (`...prepared to speak again.M'rak rose from his knees...` — the L470 paragraph glued without space), then L495 citation repeat, L499 tremor repeat, L504 Reva repeat, L508 Kira repeat. **Canon = L470–491** (first occurrence); delete L493–511.
- **L515** — draft Reva citation: `"For crossing the belt and the desert in one night, for bringing and doing more than anyone would have hope her to do, for standing where eveyeone else fell..."` (`hope her`, `eveyeone`; polished twin L524).
- **L576** — draft proclamation: `"My citizens I give you your generals the four heavenly generals of the wengari!!!..."` (polished twin L584 — which carries the single-m `humans` fix).
- **L609–651** — **Tamsin investiture V1** (duplicate): draft beat L609 (`Sylva hands another scroll to ajani he again unfolds if with a theatrical flair...`), L612 `A second scroll passed`, L617 call, L621–628 procession, L631 V1 citation (`You were our enemy... You held the gate alongside my soldiers...`), L639 title **`Stand, Tamsin, the Sun's Mercy, Honorary General of the Wengari!`**, L644 crowd+oath V1 (`I am not Wengari... This I swear.`), L648 `That is all we ask.` **Canon = V2 (L653–681)** — title **`Rise, Tamsin, the first and only Knight of the Wengari. Rise, Tamsin of the Golden Claw!`** — proven canon by downstream references: L721 `The Knight of the Golden Claw had been named.`, L739 `The Knight of the Golden Claw fought at the gate.`, L1135 `...the first Knight of the Wengari...`. (V2's `a third scroll` L653 vs V1's `A second scroll`: only one scroll precedes (the generals', L414) — V2 numbering is a minor continuity error → EDITORIAL note.)
- **L684–708** — proclamation craft-feedback block (L684 template, L689 elemental naming, L692 M'rak elevation, L695 Tamsin structurally distinct, L700 theatricality, L702 template for the future, L708 diplomatic function).
- **L717** — draft beat: `Sylva hands another scroll to Ajani this one is black he reads 'Vasha of the stripe paws, Mira su walker of the Pyrinae present yourselves to the crown!!'` (polished twin L721+).
- **L771** — draft Mira citation: `"for inventing new ways to defend us in under a week, for defending us when even we didn't knew we need defending..."` (**Canon = L781**: `For inventing new ways to defend us in under a week. For defending us when even we didn't know we needed defending... Rise, Mira Sun-Walker.`).
- **L800** — synopsis beat: `As the spirits are high a war horn sounds from the gate, three délégations are approaching...` (`dénies`-style French spellings recur).
- **L882** — synopsis beat: `Salahim had come to offer a veritable mother load : grain and timber and iron and cloth...`
- **L1034** — draft-style line in speech-line markup: `Nikolai turns and says utterly defeated "Come humman, and perhaps next time bring better guards ?" As he slowly very slowly walks back...` (polished twin L1038+).
- **L1173** — synopsis beat: `Ajani looks at Nikolai confused then to sulheim 'what is it that we are signing ?'...` (lowercase `sulheim` for Salahim).

**Mechanical defects (polished text):** single-m `human(s)` — L262 (`the humans carried their fallen`), L267 (`Humans emerged from the Humman quarter`), L273, L292, L322 (memorial pillar paragraph), L332 (`The human refugees`), L372 (`Wengari and human and Pyrinae alike`), L584 (proclamation: `Teach the treacherous humans in Verdantis a lesson`), L901 (Salahim: `I am Salahim, current Sultan of the Humans.` → `Hummans`; also contradicts his arc6-02 self-title form — see §3.2).

**king/King:** compliant (no formal-title instances; lowercase generics correct).

---

## 3. Canon-Rule Compliance

### 3.1 king/King (rule 1)
Census (`arc6_tally.py`): arc6-01 King=3/king=47 · arc6-02 King=1/king=44 · arc6-03 King=1/king=65 · arc6-04 King=0/king=46 · arc6-05 King=0/king=26.
- **Zero** determiner violations (`the King`/`my King`/`a King`): none found anywhere.
- **Zero** lowercase-king-before-Name violations.
- The capitalized instances: arc6-03 L606 `King Ajani` (title+name — canon ✓); arc6-01's 3 capitalized hits are `King of the Wengari`-context checks — **the deviations are the reverse direction**: formal proclamation titles left lowercase:
  - arc6-01 L192 `king of the Wengari` (Ajani's full-title greeting)
  - arc6-04 L1216 `king of the Wengari` (Ajani's salute to Nikolai)
  - arc6-04 L1226 `king of the Wengari` (Nikolai's salute to Ajani)
  - arc6-02 L714 `king of the humans` (Salahim's self-title; double deviation with spelling)
  → **4 MECHANICAL capitalization fixes.** All other lowercase uses are generic/apposition/direct-address (`a king needs something bigger than a crown` arc6-04 L453; `the king's morning vigil` arc6-04 L1112) and are canon-correct.
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
- **Single-m spelling deviations** (human/humans/Human/Humans): 85 tokens total, but **~48 of them sit in draft/synopsis lines that get deleted with the debris**; **~50 remain in polished text** after debris removal, concentrated in **arc6-03 (~35)** — see §2.3 line list. Notable polished instances outside arc6-03: arc6-02 L4/L710/L714; arc6-04 L247/L256/L266; arc6-05 L262/L267/L273/L292/L322/L332/L372/L584/L901.
- **Lowercase double-m** (capitalization only): arc6-01 L1011 (`hummans`), arc6-03 L281 (`humman woman`); the rest are in draft lines.
- No Earth-gloss contexts anywhere in Arc VI — every single-m token is a deviation.
- Cross-chapter consistency note: Sultan Salahim styles himself `king of the humans` (arc6-02 L714) vs `Sultan of the Humans` (arc6-05 L901); both should converge on `King/Sultan of the Hummans`.
- **Verdict: the arc's largest mechanical defect class — ~52 fixes, all scriptable via closed map (human→Humman, humans→Hummans, Human→Humman, Humans→Hummans in the listed polished lines).**

### 3.3 Dialogue formatting (rule 3)
- **Speech in double quotes:** universal in polished text. **One hard defect:** arc6-01 L641 missing opening `"` (see §2.1) — sole cause of the file-level imbalance (395 = odd). All other chapters: file-level double-quote walk balanced (arc6-04's L528–530 flashback quotes balance across the paragraph break — legitimate).
- **Ajani's inner thoughts:** single-quoted everywhere they appear (`'hmm the council worked as designed...'` arc6-01 L313; `'this grows tiresome'` arc6-02 L37; `'well that's understandable, he is odd'` arc6-01 L147; `'so these are the ones'` arc6-01 L443). **No Ajani thought ever uses `*...*`.** Crossed `*...'`/`'...*` markup: **zero** across all five chapters (`arc6_delim_cross.py`: 0 CROSSED flags).
- Non-Ajani asterisk usage (Tree telepathy; Nikolai's thought arc6-04 L1321; shared thought arc6-02 L693; Blackie gesture arc6-02 L613) — see §6.3 J3.
- **Contractions:** 0 missing-apostrophe contractions in polished prose. All `dont/cant/wont/theyre/thats/its/ive` etc. hits are inside draft/synopsis lines (deleted with debris): arc6-01 L123/L197/L313/L963/L1042; arc6-02 L37/L672/L895; arc6-03 L78/L277/L318/L710/L765/L895; arc6-04 L318/L641/L715/L1105/L1270; arc6-05 L144/L253/L410/L515/L576/L800/L1034/L1173.
- **Standalone lowercase `i`:** 0 in polished text (all hits inside draft lines or roman-numeral false positives none).
- **Verdict: compliant apart from the single missing-quote defect + draft-line hygiene that deletion resolves.**

### 3.4 Em dashes U+2014 (rule 4)
Census (`arc6_em_classify.py`): arc6-01 em=216 · arc6-02 em=232 · arc6-03 em=217 · arc6-04 em=277 · arc6-05 em=287. Classification of odd-dash lines: CUT(speech) 43 · TAIL(elab/empty) 57 · OPEN-MID 159.
- Spot-verification of the OPEN-MID bucket shows **~all are canon case-3** (single dash introducing an elaboration that runs to sentence end), e.g. arc6-01 L103 `his accent distinct—formal and unhurried, the voice of...`, arc6-04 L432, arc6-05 L531. The classifier's heuristic over-flags; manual sampling found **no unclosed mid-sentence dashes in polished text**.
- Paired parentheticals (canon case-2) used correctly, e.g. arc6-05 L1195 `The Threx—the silent, shimmering Threx—whom the Wengari had once driven...`.
- **No ASCII-hyphen/en-dash dialogue openers** (`arc6_hyphen_audit.py`: zero spaced hyphens outside draft `' - '` markers; all 109 unique word-word hyphen tokens are legitimate compounds/adjectives — burn-scarred, rune-glass, seventy-three, court-martial etc.).
- Scene-divider headings (`**Solen — The Temple**` arc6-02 L737 etc.) use em dashes as heading separators — deliberate formatting consistent across the corpus, not a defect.
- Two cosmetic anomalies, both inside debris blocks (no fix needed beyond deletion): arc6-04 L41 dangling paragraph-final dash (dinner V1); arc6-01 L99/L251 confirmed to be legit em-dash elaborations (console display artifacts — no ASCII hyphens).
- **Verdict: fully compliant.**

---

## 4. Umbrella Draft-Debris Inventory (chapter-06.md, 5,874 lines)

Scan method: `arc6_umbrella_scan.py` + targeted greps (never whole-file reads). The 2026-08-23 pass-1 removed explicit rewrite markers (`Let me rewrite`, `Here is the correction`, `Version A/B`, `Montage`, `pass1/pass2`: **all now 0 hits**) but **left every beat/duplicate/craft-note/scaffold in place**. All debris below survives in the umbrella; umbrella line numbers given (splits were generated from it 2026-08-23 17:45–17:51, so the same text sits at the split lines listed in §2).

| Umbrella L | Content | Split twin | Disposition | Canon evidence |
|---|---|---|---|---|
| L122 | draft beat `Next scene beats >...Lira speaks angrily...` | arc6-01 L123 | DELETE | polished twin L134 |
| L904 | directive `*Now let's see Yvaria, Reva, lira and vex*` | arc6-01 L905 | DELETE | author meta |
| L1253–1267 | Kyre-Tree response (single, correct) | arc6-02 L208–225 | KEEP | — |
| L1531 | directive `*Let's look at the immediate aftermath...*` | arc6-02 L486 | DELETE | author meta |
| L1824–1835 | craft block `The chapter is working on all three fronts...` | arc6-02 L779–790 | DELETE | author meta (J3 archive?) |
| L1940 | directive `*You can write the next scene...*` | arc6-02 L895 | DELETE | author meta |
| L1993–2033 | Kyre-Tree scene V1 | arc6-02 L948–988 | DELETE | V2 at U-L2037–2086 is canon |
| L2035 | approval `*I like it, let's write it*` | arc6-02 L990 | DELETE | author meta |
| L2330 | draft beat `Then without warning the lament...` | arc6-03 L133 | DELETE | polished V3 |
| L2334–2389 | L'vat strike V1 | arc6-03 L137–190 | DELETE | V3 canon |
| L2391–2425 | L'vat strike V2 | arc6-03 L194–228 | DELETE | V3 canon |
| L2427–2470 | L'vat strike V3 | arc6-03 L230–272 | **KEEP (canon)** + apply §2.3 hum fixes | final rewrite, connects to girl scene |
| L2474 | draft beat `We see a humman mother...` | arc6-03 L277 | DELETE | polished twin |
| L3072–3100 | craft block (Shadow Office etc.) | arc6-03 L866–891 | DELETE | author meta |
| L3372–3480 | Snow-Paw dinner V1 | arc6-04 L36–145 | DELETE (J2 salvage) | V2 canon; V1 has Velarius inconsistency |
| L3482 | directive `*We follow them to the dinning room...*` | arc6-04 L146 | DELETE | author meta |
| L3651 | corrections note `*/corrections 1) the snow paws...*` | arc6-04 L315 | DELETE | implemented by V2 |
| L3977 | draft beat `Later at night Nikolai ask Cefiro...` | arc6-04 L641 | DELETE | polished twin |
| L4051 | draft beat `The next day at breakfast Nikolai announces...` | arc6-04 L715 | DELETE | polished twin |
| L4489–4528 | craft block (arc6-03 copy + extras) | arc6-04 L1148–1190 | DELETE | author meta |
| L4530 | draft beat (sparring run-on) | arc6-04 L1194 | DELETE | polished twin L1202–1226 |
| L4557 | Nikolai laugh V1 | arc6-04 L1221 | DELETE | V2 at L1226 canon |
| L4566/4569/4586/4597 | scaffold headings `**Feedback on the Combat Choreography**` / `**The Halberd User (Nikolai)**` / `**The Four Pillars User (Ajani)**` / `**The Verdict**` + analysis | arc6-04 L1230–1264 | DELETE | author meta (rule 5) |
| L4606 | draft beat `Everyone cheers for Ajani everyone but l'vat...` | arc6-04 L1270 | DELETE | polished twin L1305+ |
| L4830–4896 | Maren report V1 | arc6-05 L165–234 | **KEEP (canon)** per J1 recommendation | complete scene w/ closer |
| L4898–4908 | Maren report V2 fragment | arc6-05 L238–248 | DELETE or splice Nikolai speech (J1) | contradicts V1 |
| L4913 | draft beat (funeral, `40 coffins`) | arc6-05 L253 | DELETE | polished twin |
| L5126 | draft M'rak citation | arc6-05 L466 | DELETE | polished L474 |
| L5134–5151 | M'rak polished block (1st) | arc6-05 L470–491 | **KEEP (canon)** | first occurrence |
| L5153–5168 | M'rak polished block (duplicate, incl. `again.M'rak` glue) | arc6-05 L493–511 | DELETE | exact repeat |
| L5269 | draft beat Tamsin scroll | arc6-05 L609 | DELETE | polished V2 |
| L5277–5300 | Tamsin V1 (`Sun's Mercy, Honorary General`) | arc6-05 L613–651 | DELETE | V2 title proven canon by L721/L739/L1135 refs |
| L5317–5340 | Tamsin V2 (`Knight of the Wengari / Golden Claw`) | arc6-05 L653–681 | **KEEP (canon)**; fix `a third scroll`→`a second scroll` (EDITORIAL) | downstream refs |
| L5377 | draft beat Vasha/Mira scroll | arc6-05 L717 | DELETE | polished twin |
| L5406 | draft Mira citation | arc6-05 L771 | DELETE | polished L781 |
| L5460 | draft beat war horn | arc6-05 L800 | DELETE | polished twin |
| L5542 | draft beat Salahim `mother load` | arc6-05 L882 | DELETE | polished twin |
| L5833 | draft beat Sulheim | arc6-05 L1173 | DELETE | polished twin |

Additionally in the umbrella (as in the splits): arc6-02 L176/L352/L585/L672/L898 twins (≈ U-L1221/L1397/L1630/L1717/L1943); arc6-03 L78/L610/L710/L765/L895 twins; arc6-05 L129–140/L144/L295–316/L342/L378–406/L410/L515/L576/L684–708/L1034 twins. All DELETE.

**Rule-5 check (author meta-text):** explicit markers eliminated by pass-1; surviving meta-text is exactly the inventory above. `chapter-06.md.bak.before_pass1` (514,876 B, 2026-06-16 23:35) exists — existence noted, not audited, per instructions.

---

## 5. Duplicate Blocks with Canon Designation

| # | Chapter | Versions (split lines) | Canon designation | Evidence |
|---|---|---|---|---|
| 5.1 | arc6-02 | Kyre-Tree scene: V1 L948–988 · V2 L992–1041 | **V2** | V2 has descent transition (L992), Ajani's spoken line (L996), consolidated ending (L1040 absorbs V1's L987 tail); V1 opens abruptly with no entry |
| 5.2 | arc6-03 | L'vat strike: V1 L137–190 · V2 L194–228 · V3 L230–272 | **V3** | final rewrite (`The Deep felt the elements shift`); only V3 resolves the standoff (`Stand down. The White Dawn vouches for them.` L272) and connects to the girl/Quick scene; V1/V2 are superseded takes |
| 5.3 | arc6-04 | Snow-Paw dinner: V1 L36–145 · V2 L149–313 | **V2** | V2 removes the Velarius knowledge the corrections note (L315) forbids, adds the Snow-Paw interruptions the note demands, and flows into the arena scene (L323+). V1's unique beats → J2 |
| 5.4 | arc6-04 | Nikolai laugh: V1 L1221 · V2 L1226 | **V2** | V2 adds the formal salute paragraph (`Nikolai Silverpelt... salutes Ajani Brightmane...`), mirroring Ajani's L1216 salute; V1 is the shorter early take |
| 5.5 | arc6-05 | M'rak exaltation reactions: 1st L470–491 · 2nd L493–511 | **1st occurrence (L470–491)** | 2nd is a verbatim repeat whose first line is a glue defect (`...prepared to speak again.M'rak rose...` L493); delete L493–511 |
| 5.6 | arc6-05 | Tamsin investiture: V1 L609–651 · V2 L653–681 | **V2** | downstream canon refs to `Knight of the Golden Claw` (L721, L739) and `first Knight of the Wengari` (L1135); V1's `Sun's Mercy/Honorary General` appears nowhere else in the corpus |
| 5.7 | arc6-03 + arc6-04 | craft block: arc6-03 L866–891 ≡ arc6-04 L1148–1171 (verbatim) | **delete both** | author meta-text, not story; identical wording incl. the `paper shield` sentence; arc6-04 copy then continues with chapter-specific extras L1174–1190 (also delete) |
| 5.8 | arc6-05 | Maren report: V1 L165–234 · V2 fragment L238–248 | **V1 (recommended) — JUDGMENT** | V1 complete with scene closer; V2 orphaned (no Ajani prompt) and contradicts V1 (`We have no names to add` vs V1 `the Snow Paw names that the Tsar has provided`). V2's Nikolai funeral-set-up speech is worth salvaging → J1 |
| 5.9 | arc6-01/04 | `The Humman army marched from Verdantis...` arc6-01 L77 ≡ arc6-04 L94 ≡ arc6-04 L163 | **keep all (NOT a defect)** | intentional in-story repetition: Cefiro repeats his report to the Snow Paws (arc6-04 L94=V1 dinner, L163=V2 dinner — one dies with each version's deletion anyway) |

Cross-chapter intentional echoes verified as non-defects: `Life in the desert is hard. Only those strong enough survive.` (arc6-05 L304 quote-back in craft block + speech), salute title lists (arc6-01 L192 ≡ arc6-04 L1216 — both polished, both need the same King fix).

---

## 6. Remediation Classification

All fixes must be applied to the **umbrella chapter-06.md** (source of truth), then re-split. The splits are regenerated artifacts. Umbrella line map in §4.

### 6.1 MECHANICAL (scriptable closed map) — 59 fixes
**M1. Missing opening quote (1):** arc6-01 L641 — prepend `"` to `Peregrine variants. We call them Sunraptors...` (paragraph already ends with closing `"`); optionally wrap in dialogue-block like neighbours (EDITORIAL part optional).

**M2. Formal-title capitalization (4):**
| File | Line | Current | Fixed |
|---|---|---|---|
| arc6-01 | L192 | `...holder of Luxor, king of the Wengari.` | `King of the Wengari` |
| arc6-02 | L714 | `...great Sultan Salahim, king of the humans.` | `King of the Hummans` (also M3) |
| arc6-04 | L1216 | `...caller of spirits, king of the Wengari, salutes...` | `King of the Wengari` |
| arc6-04 | L1226 | `...White Dawn, king of the Wengari.` | `King of the Wengari` |

**M3. Humman spelling/capitalization closed map (~52 polished-text tokens):** replace, in the polished lines listed below only: `human→Humman`, `humans→Hummans`, `Human→Humman`, `Humans→Hummans`, `humman→Humman`, `hummans→Hummans`.
- arc6-02: L4 (`the humans currently`), L710, L714.
- arc6-03: L120 (×2), L128, L137* (only via canon V3 L230), L161, L230, L252 (×2), L256, L262, L267, L281 (`humman woman`), L307, L323 (`Human cubs`), L351, L356, L384, L403 (×2), L407, L416, L420 (×2), L491, L511, L578, L583, L641, L735, L773 (×2), L802, L831 (×2). (*V1/V2 occurrences die with the debris deletion; apply the map to canon V3 L230–267.)
- arc6-04: L247 (`Human.`→`Humman.`), L256, L266.
- arc6-05: L262, L267, L273, L292, L322, L332, L372, L584, L901 (`Sultan of the Humans`→`Sultan of the Hummans`).
- arc6-01: L1011 (`hummans`→`Hummans`).

**M4. Concatenation/glue defects (2, both inside blocks already deleted by D-list — no standalone fix needed, listed for completeness):** arc6-05 L493 `again.M'rak`; arc6-05 L314 `with it.The scene` (craft block).

**M5. Tamsin scroll numbering (1):** arc6-05 L653 (canon V2) `a third scroll passed` → `a second scroll` (only the generals' scroll precedes). EDITORIAL-mechanical hybrid; safe to script.

**Script for M2+M3:** a line-addressed sed/python patch keyed to umbrella line numbers (§4 map) is trivially derivable from `arc6_tooling/arc6_lint_results.json` + `arc6_tally.txt`; no regex-wide replace (would hit draft lines that are being deleted anyway — harmless either way, but line-addressed is cleaner).

### 6.2 EDITORIAL (judgment deletion/reword) — 7 items
**E1.** arc6-01 draft-format lines with **unique scene content** (no polished twin found): L197 (Ajani's "how many did we lose" question to M'rak), L313 (resignation-refusal + reward thought), L443 (Velarius-madison question to Seris — note: polished continuation L447 reacts to it, so the line cannot simply vanish), L485 (orders to Seris/Tamsin). → **Rewrite into polished prose** (matching surrounding register), or confirm a twin exists and delete.
**E2.** arc6-02 L352 (draft promotion-and-rebuke speech): verify polished twin in the same council scene; if none, rewrite (scene depends on the promotion order).
**E3.** arc6-05 L238–248 (Maren V2 fragment): delete the duplicated report; decide whether to splice Nikolai's `We have no names to add to your pillar, but we will stand with you at the memorial. The fifth family will honor the fallen of the four.` into canon V1 (replacing V1's `the Snow Paw names that the Tsar has provided` clause) — see J1.
**E4.** arc6-04 dinner V1 unique beats salvage (J2): Nadya/Vanya questioning block (L112–122, incl. `Are any of them as beautiful as me?`), Vanya `Good. I will fight them all.` (L117), Ivan beats (L80). If kept, reword into V2; if dropped, plain deletion.
**E5.** arc6-04 L41 dangling sentence-final dash — dies with dinner V1 deletion; if V1 is salvaged per E4, the sentence must be completed.
**E6.** arc6-01 L641 dialogue-block wrapper: optionally wrap the fixed paragraph in `<div class="dialogue-block">` for structural consistency with neighbours.
**E7.** arc6-05 L653 see M5 (listed once; execute with M batch).

### 6.3 JUDGMENT (needs Ainz-sama's decision) — 3 items
**J1. arc6-05 Maren-report contradiction (L165–234 vs L238–248).** Two mutually exclusive facts: V1 says the Tsar **has provided** Snow Paw names for the pillar; V2's Nikolai says the Snow Paws have **no names to add** but will stand at the memorial. Both lead into the funeral scene. Recommendation: keep V1 as the scene, splice V2's Nikolai speech in place of V1's names clause (the speech is the stronger beat and sets up Nikolai walking beside Ajani at the pyre). **Decision needed:** splice vs plain V1.
**J2. arc6-04 dinner V1 unique beats.** V1 (canon-superseded) contains beats absent from canon V2 (Nadya's marriage/beauty question, Vanya's fight-them-all). **Decision needed:** salvage into V2 (E4) or drop.
**J3. Non-Ajani `*...*` thoughts + craft-block archiving.** (a) Rule 3 binds Ajani only; Nikolai's thought (arc6-04 L1321) and the shared Wengari+Humman thought (arc6-02 L693) use `*...*`. Tree telepathy in `*...*` is established canon. **Decision needed:** keep as-is, or unify ALL character thoughts to single quotes. (b) The craft-feedback blocks (§4) are genuine editorial analysis; **decision needed:** delete outright or export to `QA/` archive before deletion.

### Deletion batch (D-list, mechanical but large — ~350–400 lines)
Execute after J1–J3: all §4 inventory rows marked DELETE (draft beats, synopsis beats, directives, planning notes, craft blocks, scaffold block, duplicate versions V1/superseded takes, approval lines). Every deletion is line-addressed in §4/§5; no content judgment required except where E1–E4 flag unique content.

---

## 7. Status

**FINAL.** All seven sections complete; every finding script-derived and spot-verified against actual file lines (line numbers in this report are exact split-file lines; umbrella lines exact for chapter-06.md). READ-ONLY discipline maintained throughout — story content untouched; writes confined to this report and `QA/arc6_tooling/`. Artifacts retained for the remediation pass: `arc6_lint_results.json` (per-line hit map), `arc6_tally.txt`, `arc6_em_classify.txt`, `arc6_quote_pair.txt`, `arc6_delim_cross.txt`, `arc6_hyphen_audit.txt`, `arc6_umbrella_debris.json`.

Pending downstream: Ainz-sama's decisions J1–J3 → then a single umbrella patch pass (D-list deletions + M1–M5 map) → re-split → re-run `arc6_tooling` battery as verification (expected residual: 0 debris markers, even quote counts in all five files, zero single-m tokens outside Earth-glosses — none exist).
