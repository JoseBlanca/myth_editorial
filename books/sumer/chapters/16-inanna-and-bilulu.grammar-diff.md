# Grammar-check diff — Chapter 16: Inanna and Bilulu

Stage: 14b grammar-check
Input: `chapters/16-inanna-and-bilulu.resolved.adoc`
Output: `chapters/16-inanna-and-bilulu.grammar-checked.adoc`

## Changes

No grammar, readability, or punctuation changes were made to the main prose. Every candidate issue was reviewed and either resolved to "no change needed" by the skill's own rules or deferred to a later stage. The `.grammar-checked.adoc` file is byte-identical to the `.resolved.adoc` input.

## Reviewed and not fixed (with rationale)

### Sentence length

- **Line 15** — `The narrative is set within the broader Dumuzid dying-god cycle: Dumuzid — the shepherd-god, consort of Inanna — is dead, or has been taken to the underworld, and Inanna — goddess of love, war, and the morning and evening star — mourns and seeks vengeance.footnote:[ETCSL 1.4.4; Kramer 1961, pp. 97–101.]`
  - Length: ~41 words. Under the skill's >50-word threshold.
  - Structure: two sequential em-dash appositives (on Dumuzid and on Inanna). The skill flags *nested* parenthetical asides (one aside inside another), not sequential ones, and these two asides are coordinate rather than nested. Parsable on one read.
  - Not fixed.

- **Line 23** — `Not the city, not the temple precinct, not the irrigated fields where civilisation sustains itself, but the open, dry, ungoverned land beyond the canals — the place where shepherds move their flocks, where bandits operate, where the boundary between the human world and something older and less controlled becomes difficult to locate.`
  - Length: ~52 words, just over the >50-word threshold.
  - Structure: deliberate sentence fragment used for rhetorical effect — a `not X, not Y, not Z, but W` parallel construction following the topic sentence `The steppe is the key setting.` and closed by a three-part `— the place where ..., where ..., where ...` appositive. The skill explicitly exempts "sentence fragments (unless clearly intentional for effect)". The parallel rhetorical structure is clearly intentional, and splitting it would destroy the cadence — a style/rhythm decision that belongs to line-edit rather than grammar-check.
  - Not fixed.

- **Line 37** — `Whether Bilulu and Girgire killed Dumuzid directly, whether they enabled his death, or whether they represent something more diffuse — the hostile steppe itself, personified — is a question the fragments cannot answer with certainty.`
  - Length: ~36 words. Under threshold.
  - Structure: three parallel `whether` subject clauses followed by an em-dash gloss. Parsable on one read.
  - Not fixed.

- **Line 60** — `Every time the ritual is performed, every time water is poured for the dead shepherd in the open country, the punishment is re-enacted and the mourning is renewed.`
  - Length: ~29 words. Under threshold.
  - Structure: deliberate parallel `every time ..., every time ...` anaphora. Parsable.
  - Not fixed.

- **Line 76** — `This composition, the final instalment, answers the question of what happens after: grief is followed by the identification of those responsible, identification is followed by confrontation, and confrontation produces not merely punishment but the ritual framework through which the dead will be remembered.`
  - Length: ~44 words. Under threshold.
  - Structure: parallel `X is followed by Y` chain building to a `not merely ... but ...` close. Parsable on one read.
  - Not fixed.

- **Line 78** — `They were preserving an explanation of how a specific desert practice came to exist, why a particular waterskin poured water for a particular god, and how the cosmos turns even its worst violations into instruments of order.`
  - Length: ~37 words. Under threshold.
  - Structure: three parallel indirect-question clauses (`how ..., why ..., how ...`). The mild asymmetry between two `how` clauses and one `why` clause is a rhetorical choice, not a grammar error. Parsable.
  - Not fixed.

### Pronoun reference

- **Line 66** — `The offender is not removed from the system; the offender is absorbed into it, conscripted into a role that serves the very order they violated.`
  - `they` referring to singular `offender` is accepted modern usage (singular *they*) and the antecedent is unambiguous.
  - Not fixed.

- **Line 69** — `The structural similarity is real: a god punishes by changing the offender's form rather than simply killing them.`
  - Same pattern — singular *they* with `offender` as antecedent. Unambiguous.
  - Not fixed.

### Punctuation artefacts in marker-resolved blocks

Per hard rule 4 ("No content changes to resolved marker passages. These were reviewed and locked.") and hard rule 2 ("No footnote changes"), the following marker-resolved blocks are left exactly as received. They contain stray double-period (`..`) and stray-period (`. .`) artefacts that appear to be residues of the marker-resolution stage.

- **Line 21** — `_[At this point the tablet breaks. Opening lines 1–20 heavily damaged; the context for Inanna's mourning is partially lost. Very few manuscript witnesses survive to restore the opening.. none available..]_` — double-dot (`..`) closers on the last two clauses.

- **Line 35** — `_(The exact nature of Bilulu's and Girgire's guilt is debated; Jacobsen interprets them as steppe bandits or desert marauders responsible for Dumuzid's death, but the fragmentary text does not spell out the accusation in full..footnote:[Inference: Jacobsen 1987, pp. 318–320, provides this interpretation from context.. Risk: Other scholars may read the relationship differently given the gaps..])_` — `..footnote:` (double-dot before footnote), plus `context..` and `gaps..` double-dot closers inside the footnote body.

- **Line 45** — `_[At this point the tablet breaks. . none sufficient; Jacobsen fills narrative gaps interpretively..]_` — stray `. .` after `breaks` and `interpretively..` double-dot closer.

- **Line 52** — `The transformation of Bilulu into a waterskin and Girgire into a steppe spirit is Jacobsen's influential reading, based on the surviving fragments and his interpretive reconstruction of the broken sections..footnote:[This passage reconstructs the lacuna at etcsl 1.4.4, lines 95–130 from the parallel account in jacobsen-1987, pp. 320–325; confidence: medium.]` — `sections..footnote:` double-dot before footnote on the lead sentence of a marker-resolved inference block.

The pattern is consistent with what earlier chapters in this pipeline flagged for editorial review of marker-resolution artefacts (cf. the `grammar-diff` files for chapters 12 and 15). Flagged for editorial review; not fixed at this stage.

### Register

- **Lines 3 and 10 (source overview)** — Dense, citation-heavy paragraphs. Per the skill's "What NOT to fix" list ("The academic tone of source overview sections (this is a deliberate register choice)"), these are out of scope. Not fixed.

### Minor style observations deferred to line-edit

- **Line 3** — The inline `supplemented by Jacobsen 1987, pp. 315–325.footnote:[Jacobsen 1987, pp. 315–325.]` duplicates the citation in running prose and in the footnote. This is a citation-style / content-shape question, not a grammar error. Deferred.
- **Line 78** — `how ..., why ..., how ...` mild mixed parallelism (noted above). Deferred to line-edit if smoothing is desired.

## Self-check

- Factual content: unchanged — no proper nouns, dates, line numbers, footnotes, EVIDENCE tokens, COMPARATIVE-HOOK tokens, or citation strings were modified.
- Files are byte-identical: `chapters/16-inanna-and-bilulu.grammar-checked.adoc` is a verbatim copy of `chapters/16-inanna-and-bilulu.resolved.adoc`.
- Footnote count: unchanged — 13 `footnote:[` instances in both files.
- EVIDENCE tokens: unchanged — 17 `// EVIDENCE:` lines in both files.
- COMPARATIVE-HOOK tokens: unchanged — 2 `// COMPARATIVE-HOOK:` lines in both files.
- Line count: 79 in both files.
- AsciiDoc structure: unchanged — section heading `== Inanna and Bilulu: Vengeance for the Shepherd`, all `'''` thematic breaks, all `footnote:[...]` macros, all `_italic_` markers, all `_[ ... ]_` and `_( ... )_` marker-resolution blocks intact.
- All review decisions logged above; no silent edits.
