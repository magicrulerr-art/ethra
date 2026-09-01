# ETHRA FIX BATCH 1+4 — Arc VI master + Arc IV master
**Assigned by:** Mare Bello Fiore (Chronicler of Ethra), under direct order of Ainz-sama.
**Agent:** Demiurge. **Files you may edit (ONLY these two):**
- `C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-06.md`
- `C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-04.md`

## Hard constraints
1. Edit ONLY the two master files above. Never touch `raw/` ledgers, `arcs.json`, `chapters/` splits, `server.py`, anything else.
2. Do NOT run regenerate_chapters.py. Do NOT commit. Do NOT push. Mare integrates.
3. Never invent new prose. This is delete-raw-keep-polished surgery. Where a fix requires cleaning a line in place, change the minimum (case, punctuation, tense) and report it.
4. Style rule: dialogue only inside `<div class="dialogue-block">` with `<span class="speech">` or `<p class="speech-line">`; thoughts are inline single-quoted italics in prose (`*like this*`), never in speech blocks.
5. When deleting a raw block, delete the ENTIRE `<div class="dialogue-block">...</div>` unit (opening and closing tags).
6. Before each edit_file, verify the target text is unique in the file (grep count == 1); if not unique, include more surrounding context.
7. Report every edit: line number, one-line before, one-line after, rationale.

## BATCH 1 — chapter-06.md (line refs are master-file lines, verified today)

### A. Raw dictation blocks with polished twins — DELETE the raw div, keep the polished:
| raw line | starts with | polished twin |
|---|---|---|
| :2153 | "A few hours later ajani is helping everyone on the wall..." | prose at :2157 ("The wall had become a place of healing...") |
| :2734 | "Ajani looks towards sylva and says 'call for zephyr and Yvaria...'" | div at :2739 ("Sylva was already moving toward the door...") — VERIFY the polished text carries the order (call Zephyr and Yvaria, urgent); if the order content is absent from polished prose, keep a cleaned past-tense version of the raw line instead and report |
| :4228 | "We're back at Styxian three days after the thrax delegation left..." | prose at :4232 ("The dawn broke over Styxian like a promise...") |
| :4287 | "All the délégations stop at the gate before anyone can attempt to receive them Nikolai roars..." (Nikolai gate-fight outline) | full polished fight + salute follows (:4293+); the polished dialogue block contains the full titled salute and "Welcome home, Uncle." — safe pure deletion |
| :4498 | "It's the afternoon of the same day everyone has already settled in the throne room ajani is meeting all his advisors..." | polished briefing scene follows (Vasha, :4529) |
| :4708 | "Ajani stands and sylva passes him a scroll he unfolds it theatrically and proclames..." | polished summons div follows ("Yvaria Whisperwind, Zephyr Flamebound, Reva Firepelt, M'rak Brightmane—present yourselves to the crown!") — ALSO check the one-line prose immediately BEFORE :4708 ("And Ajani rose from the throne, the white spear humming in his paw, and the ceremony began."): if it duplicates the polished scene-opening ("Ajani rose from the throne, the white spear humming in his paw."), delete that one-liner too; otherwise keep |
| :4733 | raw Yvaria award ("...this crown awards you the following titles stand Yvaria heavenly general of the wind!!!") | polished div follows ("Stand, Yvaria, Heavenly General of the Wind!") |
| :4764 | raw M'rak award ("...stand M'rak Heavenly general of the earth !!!") | polished div follows ("Stand, M'rak, Heavenly General of the Earth!") |
| :4791 | raw Reva award (has typos "hope her to do", "eveyeone") | polished div follows |
| :4823 | raw Zephyr award | polished div follows |
| :4853 | raw march-off ("My citizens I give you your generals the four heavenly generals of the wengari!!!...") | polished div follows (two spans, ends "...why no one steals a Wengari cub!") |
| :4886 | "Sylva hands another scroll to ajani he again unfolds if with a theatrical flair and says 'Tamsin of the Hummans present yoursel...'" | polished prose at :4890 ("Sylva stepped forward once more...") — verify polished carries the Tamsin summons dialogue; if the actual summons line exists only in the raw, salvage it as a clean speech span before deleting the rest |
| :5085 | "Salahim had come to offer a veritable mother load of reparations to ajani..." | prose at :5089 ("Salahim, Sultan of the Hummans, had prepared for many things...") |
| :5237 | "Nikolai turns and says utterly defeated 'Come Humman, and perhaps next time bring better guards ?'..." | polished prose at :5241 ("Nikolai turned...") — VERIFY polished carries that parting line; if not, keep cleaned past-tense version and report |

### B. Verbatim duplicate — briefing paragraph
"The prize ceremony will follow the memorial. The four two-star generals will be honored—M'rak, Reva, Zephyr, and Yvaria..." occurs TWICE (:4529 and :4597), same scene. KEEP the first (:4529), DELETE the second div (:4597). First verify both are in the same scene (they are in the same briefing sequence; if the second is genuinely a later re-statement in a different scene, DO NOT delete — report instead).

### C. Check-and-clean (judgment)
- :2025 raw dialogue "I accept both the first and second the third is over reach and very prone to miss use vasha, you will not use the office to co..." — search within 40 lines for a polished version of this same speech. If found: delete raw div. If NOT found: clean in place (fix punctuation/case; "over reach"→"overreach", "miss use"→"misuse"; keep wording) and report.

## BATCH 4 — chapter-04.md (line refs are master-file lines)

### D. Thought-dialogue bridges — split per style rule (thought → inline single-quoted italics in prose BEFORE the dialogue block; dialogue stays in speech block; clean dialogue punctuation/case, keep wording):
- :179 — `'that went unusually good, I don't trust them' - "ok since you all agree you better ensure no other race ever makes it to the finals..."` (note the mid-line `</span>the tournament watch<span class="speech">` markup mess — the phrase "the tournament watch" is the name of the new office; render it as part of the speech, e.g. quoted office name)
- :246 — `'good they're not just going along' - "The crown will use the entire 30% for infrastruc..."`
- :1664 — `'cheeky little...' - "No it means you learn to be a princess and stay endless hours coo..."`

### E. Lowercase dictation dialogue — clean case/punctuation, keep wording:
- :337 — `"you have proposed vasha for three different roles , you must truly hate your cousin, I..."`
- :894 — `"I see now I can't leave yet, you need training, inner court is a den of green deaths, ..."` — check context; if already acceptable dialogue, leave and report.

### F. All-caps royal roars — KEEP caps (intentional shout), fix only internal punctuation garbage (`?!,`, `!!,`, missing spaces after `!`/`,`), fix misspellings; do not change wording otherwise:
- :806, :1180, :1198 (read each fully first; report any word you are unsure about rather than guessing)

### G. Ember gift echo (arc4-02:461 first occurrence, arc4-05:309 second occurrence — master chapter-04.md, search "Ember is yours")
The second occurrence (Arc IV Ch5, "The Gifts" aftermath) repeats Zara's near-verbatim speech. FIX: before the second speech add one framing line of prose: `Zara spoke the words again — the same words she had spoken at the first gift-giving, and this time they were not formality but blessing.` Then shorten the second speech to its essential line only: `"Ember is yours. She has always been yours. We are only returning what was already given."` — delete the rest of that second speech (the "Not as tribute..." repetition). Report the exact deleted text.

## Output
When done: reply with a numbered edit log (file, master line, action, before→after snippet ≤120 chars each, rationale) + a list of anything you flagged instead of fixing. Then STOP — do not regenerate, commit, or touch other files.
