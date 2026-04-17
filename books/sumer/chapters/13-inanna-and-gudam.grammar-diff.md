# Grammar-check diff — Chapter 13: Inanna and Gudam

Stage: 14b grammar-check
Input: `chapters/13-inanna-and-gudam.resolved.adoc`
Output: `chapters/13-inanna-and-gudam.grammar-checked.adoc`

## Changes

### 1. Missing comma between independent clauses (source overview, paragraph 1)

- Original: `Very few manuscript copies survive and all are heavily damaged, indicating either extremely limited circulation or catastrophic preservation failure;`
- Corrected: `Very few manuscript copies survive, and all are heavily damaged, indicating either extremely limited circulation or catastrophic preservation failure;`
- Rationale: Two independent clauses ("Very few manuscript copies survive" and "all are heavily damaged") joined by the coordinating conjunction "and" require a comma before "and." Punctuation fix; no change to meaning.

### 2. Restrictive-to-non-restrictive relative clause (body, paragraph beginning "What can be recovered")

- Original: `The opening that would have told us where Gudam came from and what kind of creature it was is largely destroyed.`
- Corrected: `The opening, which would have told us where Gudam came from and what kind of creature it was, is largely destroyed.`
- Rationale: The text has only one opening, so the relative clause is non-restrictive and should be set off by commas. The original forced the reader to parse the adjacent "was is" across a clause boundary, an ambiguous-structure readability issue flagged by the skill ("Ambiguous sentence structure where the reader must re-read to parse correctly"). The comma pair makes the subject-verb boundary explicit. No change to meaning; no change to word choice or tone.

## Not fixed (flagged for human / downstream stages)

- **Redundancy in source overview** — "survives on a small number of tablets; CBS 13859 is a complete witness" and the subsequent "The text is, however, very fragmentary overall, though CBS 13859 preserves a complete text" restate the same two facts. This is a style/concision matter, not a grammar error; leaving for line-edit.
- **"the fragments do not permit it"** (end of resolution paragraph) — pronoun "it" refers back loosely to the act of saying / determining. Readable in context; rewriting would veer into word choice and is left for line-edit.
- **Marker-resolved passages** — the `_[At this point the tablet breaks. ...  none available..]_` bracketed notes and the `_( ... ..footnote:[Inference: ...  Risk: ...  ])_` inference block contain double-dot artefacts and nested parentheticals, but per the skill's hard rules these resolved marker passages are locked and were not modified.
- **Source overview register** — the academic tone of paragraph 1 is a deliberate register choice per the skill's "What NOT to fix" list.

## Self-check

- Factual content: unchanged (no proper nouns, dates, citations, or claims altered).
- Footnote count: unchanged (11 `footnote:[` instances in both files).
- EVIDENCE tokens: unchanged (10 `// EVIDENCE:` lines in both files).
- AsciiDoc structure: unchanged (section heading, `'''` thematic breaks, `footnote:[...]`, include-style comments all preserved).
- All changes logged above; no silent edits.
