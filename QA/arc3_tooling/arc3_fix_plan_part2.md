# Arc 3 Remediation — Part 2: Mechanical replacement map (M1-M29)

All are EXACT substring replacements on the umbrella, applied AFTER deletions/insertions
(except where noted). Each entry asserts occurrence count >= 1 before replacing;
any failure ABORTS the whole run without writing. Line refs are ORIGINAL umbrella
numbers (pre-deletion) for locating context only.

| ID | umb line | Replace (exact) | With (exact) |
|---|---|---|---|
| M1 | 44 | `welcome to the wengari brothers!` | `welcome to the Wengari brothers!` |
| M2 | 77 | `"t'vat call for the elder council of the striped paws, now please "` | `"T'vat call for the elder council of the Stripe Paws, now please "` |
| M3 | 115 | `'therye here, good...why do they seem mad?'` | `'they're here, good...why do they seem mad?'` |
| M4 | 139 | `who rules the wengari?` | `who rules the Wengari?` |
| M5 | 157 | `news about the hummans as well` | `news about the Hummans as well` |
| M6 | 175 | `"the best of the humans here means...what Zara ? Tell me what do the humans do best ?"` | `"the best of the Hummans here means...what Zara ? Tell me what do the Hummans do best ?"` |
| M7 | 193 | `the humans will send their best here` | `the Hummans will send their best here` |
| M8 | 207 | `"the stripe paws will become` | `"the Stripe Paws will become` |
| M9 | 742 | `what did father always said ,` | `what did father always say ,` |
| M10a | 796 | `FRIEND'S!!` | `FRIENDS!!` |
| M10b | 796 | `A KING CANT BE` | `A KING CAN'T BE` |
| M11 | 1062 | `*The Bright Paw Elders (Closing Scene)*` | `**The Bright Paw Elders**` |
| M12 | 1056 | `*The king has put his crown on the line. The tournament begins in an hour. The Wengari are choosing their champions. The other races are choosing theirs. What should I do?*` | `'The king has put his crown on the line. The tournament begins in an hour. The Wengari are choosing their champions. The other races are choosing theirs. What should I do?'` |
| M13 | 1087 | `"tell me solen, who rules the wenfari ?"` | `"tell me Solen, who rules the Wengari ?"` |
| M14a | 1209 | `'fhe sun is up` | `'the sun is up` |
| M14b | 1209 | `BROTHERS STEMMED GUESTS` | `BROTHERS ESTEEMED GUESTS` |
| M15 | 1259 | `GUESTS RISED TO THE CHALLENGE, LETS HONOR` | `GUESTS RISEN TO THE CHALLENGE, LET'S HONOR` |
| M16a | 1315 | `ESPECTACULAR, THIS` | `SPECTACULAR, THIS` |
| M16b | 1315 | `NO MORTAL WOUNDS ITS A TOURNAMENT` | `NO MORTAL WOUNDS IT'S A TOURNAMENT` |
| M17 | 1399 | `mycelial network: *The White Dawn does not ask for mercy. The White Dawn does not offer it. The tournament will be brutal. The tournament will be remembered.*` | `mycelial network: 'The White Dawn does not ask for mercy. The White Dawn does not offer it. The tournament will be brutal. The tournament will be remembered.'` |
| M18 | 1479-1481 | Two lines + blank: `...network: *The White Dawn has changed the rules.` / blank / `The tournament will be a battle. The desert will drink deep today.*` | Merge to ONE line: `...network: 'The White Dawn has changed the rules. The tournament will be a battle. The desert will drink deep today.'` (delete the blank line between; see implementation note) |
| M19 | 1507 | `*Let's begin!*` | `'Let's begin!'` |
| M20a | 1910 | `LIVE NOT ONLY ON THE DESER BUT` | `LIVE NOT ONLY ON THE DESERT BUT` |
| M20b | 1910 | `ILL DEMONSTRATE, FRIENDS PYRANEI` | `I'LL DEMONSTRATE, FRIENDS PYRINAE` |
| M21a | 2274 | `i havent seen one since i was a child` | `I haven't seen one since I was a child` |
| M21b | 2274 | `care if i touched one?!` | `care if I touched one?!` |
| M21c | 2274 | `dont look too much, regal!` | `don't look too much, regal!` |
| M22a | 2440 | `'styx in heaven i blew it!!` | `'Styx in heaven I blew it!!` |
| M22b | 2440 | `so good!!, i should make` | `so good!!, I should make` |
| M22c | 2440 | `definetly.. a yearly thing` | `definitely.. a yearly thing` |
| M23a | 2500 | `THEN I SHALL IS IT DONE, AFTER THE DUEL ENDS` | `THEN, WHEN IT IS DONE, AFTER THE DUEL ENDS` |
| M23b | 2500 | `AND THE PYRANEI, THIS` | `AND THE PYRINAE, THIS` |
| M23c | 2500 | `ill gauge their eyes out` | `I'll gouge their eyes out` |
| M23d | 2500 | `i can already see` | `I can already see` |
| M24a | 2637 | `*OH, ok, she has claws... spear then'` | `'OH, ok, she has claws... spear then'` |
| M24b | 2637 | `should be, lets have the sun` | `should be, let's have the sun` |
| M24c | 2637 | `dead in two moves*` | `dead in two moves'` |
| M25a | 2666 | `*What on....ok... calm, breathe, shes unarmed, sword then, lets see her try to catch a dual blade'-` | `'What on....ok... calm, breathe, she's unarmed, sword then, let's see her try to catch a dual blades'-` |
| M25b | 2666 | `"You're good, but im better!"` | `"You're good, but I'm better!"` |
| M25c | 2666 | `dont allow her openings` | `don't allow her openings` |
| M25d | 2666 | `my fur is starting to bristle*` | `my fur is starting to bristle'` |
| M26a | 2695 | `*This is getting annoying!!!, why cant i reach her?!, im faster than her, im sure i am, im stronger than her, how is she still catching me?!'` | `'This is getting annoying!!!, why can't I reach her?!, I'm faster than her, I'm sure I am, I'm stronger than her, how is she still catching me?!'` |
| M26b | 2695 | `but im still better!!` | `but I'm still better!!` |
| M26c | 2695 | `'Faint, open with the sword` | `'Feint, open with the sword` |
| M26d | 2695 | `all i need is one good strike*` | `all I need is one good strike'` |
| M27a | 2721 | `*OK THIS ENDS NOW, SHE NEEDS TO GO DOWN, NOW'` | `'OK THIS ENDS NOW, SHE NEEDS TO GO DOWN, NOW'` |
| M27b | 2721 | `youre good, i admit it` | `you're good, I admit it` |
| M27c | 2721 | `but i am still the heir of the light, WITNESS` | `but I am still the heir of the Light, WITNESS` |
| M27d | 2721 | `i cant loose the crown!!!` | `I can't lose the crown!!!` |
| M27e | 2721 | `i havent even made the road yet!!, ill be the laughing stock of the families for millenia` | `I haven't even made the road yet!!, I'll be the laughing stock of the families for millennia` |
| M27f | 2721 | `lost in duel!!*` | `lost in duel!!'` |
| M28a | 2842 | `*what?'` | `'what?'` |
| M28b | 2842 | `statecraft...*` | `statecraft...'` |
| M28c | 2842 | `Infurating woman` | `Infuriating woman` |
| M29 | 2860 | `'im this close to skewering her..'` | `'I'm this close to skewering her..'` |

## Implementation notes

- M18 (pulse merge): find line ending `network: *The White Dawn has changed the rules.` (line X),
  assert X+1 is blank and X+2 equals `The tournament will be a battle. The desert will drink deep today.*`.
  Replace line X with X's prefix up to `network: ` + `'The White Dawn has changed the rules. The tournament will be a battle. The desert will drink deep today.'`, then delete lines X+1 and X+2.
- Order of operations in script: (1) assert+capture joke block and good-regents line; (2) assert all
  deletion anchors; (3) apply deletions bottom-up; (4) insertions I1, I2, I3; (5) apply M1-M29.
- After all edits, run RESIDUAL SELF-CHECKS (assert all zero, else abort):
  * no `*'` sequence remaining; no line starting `*` and ending `*'` or vice versa
  * no remaining: `\bwengari\b`, `wenfari`, `humman`-case errors (`\bhumans\b`, `\bhummans\b` lowercase)
  * no remaining flagged contractions: `\bcant\b`, `\bdont\b`, `\bhavent\b`, `\blets\b` (case-sens lower), `\bshes\b`, `\bwont\b`, `\byoure\b`, `\bim\b`, `\bill\b` (lowercase), `CANT `, `LETS `, `ILL `, `RISED`, `ESPECTACULAR`, `STEMMED`, `PYRANEI`, `DESER `, `therye`, `definetly`, `millenia`, `Infurating`, `Faint,`, `\bloose\b`, `\bstyx\b` (lowercase), `\bt'vat\b`, `FRIEND'S`, `\bsolen\b`, `\bfhe\b`
  * standalone lowercase `\bi\b`: enumerate remaining occurrences with context for the report (should be zero; if any, list them — do not auto-fix beyond map).
- The script prints a full op-log (each deletion range, each insertion, each replacement with count).
- DRY-RUN mode (argv flag): perform ALL assertions and print the op-log, but do NOT write the file.
- Write mode: write umbrella in place (UTF-8, preserve newline style: file uses \n; join with \n;
  original read with encoding='utf-8', newline='' semantics — preserve exactly).

## Out-of-scope / residual (report only, do NOT fix)
- "SO ITS SPOKEN" (umb 1852) and "ITS THE TIDE WOLVES" (umb 1910) — ITS not in closed map (map is L146 only).
- "this is getting though" (umb 2666, should read 'tough') — not in map.
- "some true to your words" (umb 2695) — not in map.
- Optional Rask-vs-Torin bridge sentence (§6.2) — not approved for this pass.
