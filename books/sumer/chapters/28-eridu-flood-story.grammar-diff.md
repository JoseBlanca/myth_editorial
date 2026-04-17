# Grammar-check diff: Chapter 28 — The Eridu Flood Story

Stage: 14b grammar-check
Input: `28-eridu-flood-story.resolved.adoc`
Output: `28-eridu-flood-story.grammar-checked.adoc`

## Changes

### Change 1 — Line 13 (editorial bracket note)

- **Original:** `...survive only in fragments. no other Sumerian manuscripts preserve these sections...`
- **Corrected:** `...survive only in fragments. No other Sumerian manuscripts preserve these sections...`
- **Rationale:** Sentence-initial capitalization. "no" follows a period, so it begins a new sentence and must be capitalized.

### Change 2 — Line 25 (editorial bracket note)

- **Original:** `...details of the gods' deliberation are largely lost. no other Sumerian manuscripts preserve these sections.`
- **Corrected:** `...details of the gods' deliberation are largely lost. No other Sumerian manuscripts preserve these sections.`
- **Rationale:** Sentence-initial capitalization. "no" follows a period and must be capitalized as the start of a new sentence.

### Change 3 — Line 39 (editorial bracket note)

- **Original:** `...only fragments survive. no other Sumerian manuscripts preserve these sections...`
- **Corrected:** `...only fragments survive. No other Sumerian manuscripts preserve these sections...`
- **Rationale:** Sentence-initial capitalization after a period.

### Change 4 — Line 55 (editorial bracket note)

- **Original:** `...are not fully preserved. no other Sumerian manuscripts preserve these sections.`
- **Corrected:** `...are not fully preserved. No other Sumerian manuscripts preserve these sections.`
- **Rationale:** Sentence-initial capitalization after a period.

## Flagged for human review (not fixed)

### Flag 1 — Line 17 (resolved INFERENCE marker)

- **Text:** `_(The antediluvian section likely described the creation of humanity and the founding of the first cities, based on surviving fragments that mention cities and kingship..footnote:[Inference: Fragmentary lines reference cities (including Eridu) and the descent of kingship from heaven.. Risk: The actual content of the lost columns is unknown; this inference rests on very small textual fragments..])_`
- **Issue:** Three instances of double periods (`..`) — one before `footnote:[`, two inside the footnote content (after "heaven" and "fragments").
- **Why not fixed:** Hard rule 4 prohibits content changes to resolved marker passages, and hard rule 2 prohibits footnote modifications. Two of the three double-period instances are inside footnote text. The passage is flagged for human review so that the author can decide whether the stacked periods are intentional (the INFERENCE marker convention) or should be cleaned up.

## Self-check

- No factual content changed. All fixes are capitalization of a sentence-initial word after a period.
- Footnote count and content unchanged. All `footnote:[...]` tokens and their text are identical in input and output.
- AsciiDoc structure intact (heading, section breaks `'''`, editorial italic brackets, comparative-hook comments, include directives — all preserved).
- No word choice, rhythm, nominalization, or tone changes.
- Every change above is logged; no silent edits.

## Readability audit (no changes required)

- Longest sentence is 49 words (chapter-opening sentence about CBS 10673). Under the 50-word threshold, meaning-essential (ties together ETCSL ID, tablet number, provenance, religious context, and sole-witness status), and already punctuated with em-dash pairs rather than nested parentheticals. Left unchanged.
- Other long sentences (Enlil authority description, Enki-and-reed-wall description, reed-wall-device description) are all 42–48 words with at most two coordinate clauses; none exceed the threshold or nest parentheticals.
- No comma splices, run-on sentences, dangling modifiers, subject-verb disagreements, or ambiguous pronoun references detected.
