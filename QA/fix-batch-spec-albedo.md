# ETHRA FIX BATCH 2 — Arc II master
**Assigned by:** Mare Bello Fiore (Chronicler of Ethra), under direct order of Ainz-sama.
**Agent:** Albedo. **File you may edit (ONLY this one):**
- `C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-02.md`

## Hard constraints
1. Edit ONLY chapter-02.md. Never touch `raw/`, `arcs.json`, `chapters/` splits, anything else.
2. Do NOT run regenerate_chapters.py. Do NOT commit. Mare integrates.
3. Never invent new prose beyond the one explicitly-provided replacement below. Minimum-change edits.
4. Style rule: dialogue only inside `<div class="dialogue-block">` (speech spans / speech-line paragraphs); thoughts are inline single-quoted italics in prose, never inside speech blocks.
5. Before each edit_file, verify target text is unique (grep count == 1); otherwise add context.
6. Line references below are SPLIT-file lines (chapter-arc2-0X.md); the master differs — locate by the quoted text.
7. Report every edit: before → after snippet, rationale.

## Fixes

### 1. Kareth's king-tally contradiction (CANON RULING: served three kings, buried TWO of them — the third king, Uthgard IX, is still alive at this point in the story)
Two lines say "buried three"; two narration lines already say "buried two". Fix the two dialogue lines:
- arc2-01:183: Kareth dialogue `"...I have buried three kings of the Bright Paws, and I will bury a fourth..."` → change **"buried three kings"** to **"buried two kings"** (keep everything else).
- arc2-02:102: `"And I—I have buried three kings."` → `"And I—I have buried two kings."`
Do NOT touch the narration lines that say "served three kings and buried two of them" (arc2-01:229, arc2-02:9) — they are the canon.

### 2. Tyrant ordinal contradiction
Canon table (Arc VI Ch4 formal list, and Arc I Ch1): 1st = Black Fire, 2nd = the Blight (Crr'zzak), 3rd = Uthgar Lightbringer, 4th = Xal'thyra, 5th = Velarius Vane (the Plague).
- arc2-06:53 (master: search "the Black Fire, the Lightbringer, the Fear-on-Wings, the Tidebreaker, and the Plague") — this chronological list wrongly implies Lightbringer is 2nd. FIX by reordering to: **"the Black Fire, the Fear-on-Wings, the Lightbringer, the Tidebreaker, and the Plague"** (Fear-on-Wings = the Blight swarm = 2nd; Tidebreaker = Xal'thyra = 4th). Change ONLY the order, nothing else.
- Verify: search chapter-02.md for other "Second Tyrant"/"Third Tyrant"/"Fifth Tyrant" ordinal claims and report any that contradict the canon table above (do not fix without reporting). Known-good context: arc2-01:76 ("served the 3rd, who built this city") and arc2-04:33 ("the 5th Tyrant—our Tyrant", Humman = Velarius) are CORRECT — leave them.

### 3. Spear-echo verbatim double
The sentence "A spear thrown by a young king, however precisely, was not the worst thing she had endured." appears twice in Arc II Ch5 (arc2-05:21 and arc2-05:54). KEEP the SECOND (later) occurrence; DELETE the first occurrence's sentence only (leave the surrounding paragraph intact).

### 4. Hall of the Sun vs arena
arc2-03:125: a summons says `"Assemble the delegations in the Hall of the Sun"` but everything in Arc II Chapters 3–6 is staged in the arena. FIX: change to `"Assemble the delegations in the arena"`. (Search for any other "Hall of the Sun" mentions in chapter-02.md and report them; do not change them without reporting.)

### 5. Water-over-stone image reuse (keep it for the Pyrinae, vary it for the Veylar)
- KEEP: arc2-04:143 — the Pyrinae Hydromancer's `"Her voice was soft as water over stone."` — untouched.
- CHANGE: arc2-06:40 (Sylara, Shell-Singer of the Veylar) — current: `Her voice was melodic, resonant, the sound of water over stone, of waves retreating from shore.` → replace with exactly: `Her voice was melodic, resonant — a chord struck underwater, the sound of waves retreating from shore.`

### 6. Thought-dialogue bridge (arc2-03 region, master ~:662)
`'the absolute insolence!' — "I AM AJANI, KEEPER OF THE LIGHT, HEIR TO THE FIRST AND THE..."` — a thought is fused with a shouted declaration inside one speech-line. FIX per style rule: move the thought out as inline single-quoted italic prose before the dialogue block (e.g. `*'The absolute insolence!'*` as prose narration — read the surrounding paragraph to attribute it to the correct thinker, it may be a watcher's thought about Ajani OR Ajani's own; report your attribution decision), keep the shouted declaration in its speech block with caps preserved, fix its punctuation.

## Output
When done: numbered edit log (action, before→after ≤120 chars each, rationale) + flagged items. Then STOP — no regenerate, no commit.
