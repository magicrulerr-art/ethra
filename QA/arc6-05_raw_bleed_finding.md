# FINDING — Arc VI Epilogue raw-direction bleed

- **Status:** EXCISED (Ainz-sama's word: "excise it, then we continue", 2026-08-25)
  Commit `f9953c3` pushed; backup `chapter-arc6-05.md.bak.sulheim_bleed` kept;
  live server verified serving clean text (91,048 bytes, zero "sulheim" hits);
  junction flow verified (Nikolai's shade plea → "Ajani looked from Nikolai's
  defeated posture..." reads clean).
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
