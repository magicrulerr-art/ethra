# Arc VI ch01 — Raw-Direction Bleed Finding (excised 2026-08-25 by Ainz's order)

## Defect

`content/story/chapters/chapter-arc6-01.md`, lines 511–513: a raw scene
direction leaked into the published prose as a `speech-line`:

    <div class="dialogue-block">
    <p class="speech-line">We switch to the night at the throne room ajani is
    taking a bath the bracers have become simple wrist wards barely a claw
    long, Cefiro is next to him clearly enjoying the warm water, ajani asks
    "Tell me cousin how did you manage to get to the city?"</p>
    </div>

Same defect class as the chapter-arc6-05 sulheim bleed (excised 2026-08-24,
commits f9953c3 + 8727cb1) — pre-dates the two-file doctrine that now
prevents this upstream.

## Canon evidence for the surviving version

The direction's content is fully absorbed by the clean text immediately
following it:
- night/bath setting + bracers shrunk to wrist wards + Cefiro enjoying the
  warm water → the three bathhouse prose paragraphs beginning "The bathhouse
  beneath the palace was a relic of the old world…";
- the question "Tell me cousin how did you manage to get to the city?" →
  the clean dialogue block: Ajani leaned back against the edge of the pool.
  "Tell me, cousin. How did you manage to get to the city? …"

Nothing is lost by excision. The previous scene closes on Kira's "Well.
Black Fire fed himself. I just watched." and the bath scene opens cleanly.

## Backup + baseline

- Backup: `QA/backups/chapter-arc6-01.md.20260825-pre-bleed-excise`
- SHA256 (pre-excise):
  6df2199291e4851e816ab783bddbce9abdc2a5c17e72ef501ee3d919702350eb
