# ETHRA FIX BATCH 3+6 — Arc III master + Arc I master
**Assigned by:** Mare Bello Fiore (Chronicler of Ethra), under direct order of Ainz-sama.
**Agent:** Sebas. **Files you may edit (ONLY these two):**
- `C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-03.md`
- `C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-01.md`

## Hard constraints
1. Edit ONLY the two master files above. Never touch `raw/`, `arcs.json`, `chapters/`, anything else.
2. Do NOT run regenerate_chapters.py. Do NOT commit. Mare integrates.
3. Never invent new prose. Minimum-change edits. One explicitly-worded replacement is provided below (Muay Thai); use it verbatim.
4. Style rule: dialogue only inside `<div class="dialogue-block">` (speech spans / speech-line paragraphs); thoughts are inline single-quoted italics in prose (`*like this*`), never inside speech blocks.
5. Before each edit_file, verify target text is unique (grep count == 1); otherwise add context.
6. Line refs are master-file lines (verified today). Report every edit: before → after snippet, rationale.

## BATCH 3 — chapter-03.md

### A. Thought-dialogue bridges — split per style rule (thought → inline single-quoted italics as prose; dialogue stays in speech block; clean dialogue punctuation/case; keep wording):
- :669 — `'forty minutes ?! That's not enough!!!' - "send for the royal armor, I'll skip breakfas..."` (speaker context: king hurrying; dialogue becomes "Send for the royal armor. I'll skip breakfast..." — read the full line)
- :2360 — `'OK THIS ENDS NOW, SHE NEEDS TO GO DOWN, NOW' - "oh... you're going down now, you're go..."` (tournament fight; thought stays caps as internal shout; dialogue cleaned)
- :1997, :2138, :2335 — speech-lines that BEGIN with single-quoted thoughts ('oh goody... war mounts!!!...', 'Styx in heaven I blew it!!...', 'This is getting annoying!!!...') — these are interior thoughts wrongly inside speech blocks. Extract the thought to inline single-quoted italic prose immediately before the div; if any actual spoken dialogue remains in the line, keep it in the speech block; if the line is thought-only, replace the whole div with a prose line of italic thought. Read each in full context first.

### B. "Muay Thai" real-world reference — EXACT replacement
:1832 (Sera vs Thane duel): `It was a full commitment—a Muay Thai combination, claws and elbows and knees in a blur of dark motion` → `It was a full commitment—a combination of claws and elbows and knees in a blur of dark motion` (delete only the real-world style name; change nothing else).

### C. "DEVOURE" line — speaker identification first
:1209: `"DOES THE STYX ASKS PERMISSION TO DEVOURE THE FIRE FEET? I SAID ALL"` (followed by Zara grinning).
STEP 1: identify the speaker from surrounding context (read :1150–1260).
STEP 2: search ALL of chapter-03.md (and chapter-06.md is OFF-LIMITS for you — skip it) for other lines spoken by the SAME character: do they consistently speak in broken all-caps?
- If YES consistent broken-caps voice → keep caps and voice, fix ONLY spelling/concord: `"DOES THE STYX ASK PERMISSION TO DEVOUR THE FIRE FEET? I SAID ALL"`
- If NO (the speaker normally speaks correct prose) → normalize fully: `"Does the Styx ask permission to devour the Fire Feet? I said all."`
Report the speaker identity and your decision.

### D. All-caps tournament proclamation — keep caps, fix punctuation garbage
:1924: `"WONDERFUL DISPLAY OF CHAMPIONS!!!, NOW FOR THE FINALS!!, I WILL REQUIRE HELP OF OUR FRIENDS AGAIN, PLEASE DESTROY THE ARENA, C..."` — read the full line; fix the `!!!,` / `!!,` clutter to clean `!` + space, fix any misspelling you can verify from context (report uncertain ones). Keep caps (public proclamation).

### E. Arc III Ch2 title problem — PROPOSE ONLY, do not edit arcs.json
Arc III Ch2 is titled "First Blood" but no blood is drawn and no fight occurs in it (reviewer finding; split file chapter-arc3-02.md, master = the second section of chapter-03.md). Read that chapter's content and propose ONE replacement title in the manuscript's register (short, concrete, noun-phrase like the siblings: "The Arena", "The Fire Feet", "The Tyrant Cycle"). Report the proposal + one-line justification. Do not apply it.

## BATCH 6 — chapter-01.md

### F. Dictation bridge + typo (master :412)
`'Mother....' -<span class="speech">"The son acknowledges, his mother sacrifice..."</span>, 'look at him, so frail, even the king pays its tithe to the tree...', <span class="speech">"Please take me to the inner chamber, Father"</span>`
This fuses crowd-thoughts and dialogue in one line. FIX: read :395–430 for context, then restructure: crowd onlookers' thoughts become inline single-quoted italic prose (attributed to the onlookers); the two actual spoken lines ("The son acknowledges..." and "Please take me to the inner chamber, Father") become proper speech blocks; fix **"his mother sacrifice" → "his mother's sacrifice"**. Report the full before/after.

### G. Thought inside speech-line (master :444)
`<p class="speech-line">'It's just as L'vat described, the spiral stair, the faint lights... the air gets thinner...'</p>` — interior thought wrongly in a speech-line. Extract to inline single-quoted italic prose (keep wording). If context shows it is actually SPOKEN aloud, report why and leave it.

### H. Verbatim tic double (masters :183 and :255)
:183 `His golden eyes—still fierce, still sharp—found Ajani's.` — KEEP.
:255 `His eyes, still fierce, still sharp, softened.` → replace with exactly: `His eyes, fierce as ever, softened.`

## Output
When done: numbered edit log (file, action, before→after ≤120 chars each, rationale) + DEVOURE speaker finding + title proposal. Then STOP — no regenerate, no commit.
