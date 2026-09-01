# ETHRA FIX — BRIDGE-PASS RULES (shared by all batch agents)
Issued by Mare Bello Fiore under Ainz-sama's order to fix all Ethra defects.

## The defect
Dictation left "thought-dialogue bridges" inside speech blocks, e.g.:
`<p class="speech-line">'ok here it goes...' - "Brothers, my father's last words..."</p>`
Single-quoted fragments are Ajani's (or another character's) INTERNAL thoughts; double-quoted parts are spoken dialogue. Publishing them fused in one speech block is the manuscript's biggest markup defect.

## The transformation (mechanical, no invention)
1. Every single-quoted thought becomes an INLINE ITALIC PROSE LINE (`*Like this.*`) OUTSIDE any div, placed immediately before the dialogue block (or after, if the thought comes after the speech). Never inside a speech block. Never a thought-block div.
2. The spoken dialogue stays in its `<div class="dialogue-block">` (`<p class="speech-line">` or `<span class="speech">`).
3. Clean the dialogue's mechanics ONLY: capitalization (sentence starts, proper nouns: Ajani, Sylva, Vasha, Maren, Seris, T'van, Kareth, Zara, Wengari, Humman(s), Styxian, Bright Paw, etc.), punctuation garbage (`!!,` `?!?` runs → single marks, missing periods/commas), stray lowercase. NEVER change words, NEVER rewrite phrasing, NEVER shorten.
4. Clean the thought's mechanics the same way (capitalize, punctuate); keep wording exact.
5. Standalone single-quoted thought lines already outside divs: just wrap them in `*...*` italics and clean mechanics. If two thoughts are fused with a dash, keep both inside one italic line.
6. Keep blank-line spacing consistent with the file (blank line before/after the new italic line and the div).
7. All-caps shouts/proclamations: KEEP CAPS, fix only punctuation garbage inside them.
8. Before each edit verify target text is unique. Use edit_file with enough context, or a Python script for many similar edits. NEVER touch `raw/`, `arcs.json`, `chapters/`, or any file not named in your task. No regenerate, no commit — Mare integrates.

## Worked example
BEFORE:
```
<div class="dialogue-block">
<p class="speech-line">'laugh now, booming' — "Hahaha, what makes you believe the Wengari even need you Hummans? How many loads ca..."</p>
</div>
```
AFTER:
```
*Laugh now. Booming.*

<div class="dialogue-block">
<p class="speech-line">"Hahaha! What makes you believe the Wengari even need you Hummans? How many loads ca..."</p>
</div>
```

## READ-ONLY (never alter, even for "improvement")
- Kyre Tree / Golden Sun telepathic monologues (long single-quoted multi-paragraph passages — the Tree's voice and the Golden Sun's negotiation are intentional form).
- Any passage that is pure narration prose.
- Protected passages per Ainz-sama: Kyre-Tree negotiation, Ajani's dual register, mythic narration, seven-architecture, grief vignettes. Bridges INSIDE dialogue scenes are in scope; never rewrite narration.

## Output format
Numbered edit log: file, line, before→after (≤120 chars each), plus anything flagged/uncertain. Then STOP.
