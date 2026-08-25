# FINDING — Arc VI Epilogue raw-direction bleed

- **Status:** AWAITING VERDICT (Ainz-sama, 2026-08-25): excise now, or route to Demiurge's cleaning queue
- **File:** `content/story/chapters/chapter-arc6-05.md`
- **Location:** lines 1103–1105 (one dialogue-block)
- **Defect (verbatim):**

```html
<div class="dialogue-block">
<p class="speech-line">Ajani looks at Nikolai confused then to sulheim with a questioning look, sulheim says "I have utterly forgotten what happened, may I explain why I am here ? If it's not too much trouble I would also like to sit on the shade"</p>
</div>
```

## Analysis

- Raw directorial voice leaked into the published epilogue: present tense
  ("looks"), unpolished phrasing, "sulheim" misspelling (canon: Salahim).
- It is a DUPLICATE of the polished prose immediately following it
  (Salahim's "I have utterly forgotten it. May I explain why I am here?...
  I would also like to sit in the shade." speech), which supersedes it.
- Canon-safe to remove: nothing in later text depends on this block.

## Prepared excision (execute on Ainz-sama's word)

Delete the block above plus its trailing blank line (lines 1103–1106).
Backup first: `copy chapter-arc6-05.md chapter-arc6-05.md.bak.sulheim_bleed`
Then verify prose flow at the junction (Salahim's arrival → Ajani's laugh)
and commit with message "arc6-05: excise raw-direction bleed (sulheim block)".
