# Grammar-check diff — Chapter 24 (Enmerkar and the Lord of Aratta)

Skill: 14b-grammar-check
Input: `24-enmerkar-and-the-lord-of-aratta.resolved.adoc`
Output: `24-enmerkar-and-the-lord-of-aratta.grammar-checked.adoc`

## Changes applied

### Change 1 (line 34) — Long sentence with semicolon-joined clauses, split into three

**Rationale:** ~48-word sentence joining two independent clauses with a semicolon after a nested em-dash parenthetical. Split for readability; no content removed.

Original:
> And that goddess is Inanna -- goddess of love, war, and the morning and evening star -- patron of Uruk and the pivotal figure whose favour both Enmerkar and the lord of Aratta seek; the contest between the two kings is fundamentally a contest for her divine endorsement.

Corrected:
> And that goddess is Inanna -- goddess of love, war, and the morning and evening star. She is the patron of Uruk and the pivotal figure whose favour both Enmerkar and the lord of Aratta seek. The contest between the two kings is fundamentally a contest for her divine endorsement.

### Change 2 (line 63) — 67-word sentence with 3+ clauses, split into three

**Rationale:** Sentence ran ~67 words and stacked multiple subordinate clauses (semicolon-joined independent clauses, "while"-clause, quoted clause). Split into three sentences. No meaning change; contrast between Kramer's reading and the ETCSL/later-scholars reading preserved by adding "instead" in the third sentence to retain the adversative relationship previously signalled by "while."

Original:
> The passage describes the god Enki -- god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath Eridu -- changing the speech of humanity; Kramer (1961) interpreted this as Enki disrupting a primordial linguistic unity, while later scholars (Vanstiphout, Alster) and the ETCSL translation read it as a prayer for Enki to restore unity -- "may they all address Enlil together in a single language."

Corrected:
> The passage describes the god Enki -- god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath Eridu -- changing the speech of humanity. Kramer (1961) interpreted this as Enki disrupting a primordial linguistic unity. Later scholars (Vanstiphout, Alster) and the ETCSL translation read it instead as a prayer for Enki to restore unity -- "may they all address Enlil together in a single language."

### Change 3 (line 123) — 55-word sentence with nested parenthetical, split and re-punctuated

**Rationale:** Sentence combined a conjoined independent clause ("are well matched, and the messenger...walks") with a lengthy em-dash parenthetical and a participial phrase ("carrying verbal constructions...") that followed without comma. Split into two sentences and added a comma before the participial phrase "carrying..." for clarity.

Original:
> The two kings are well matched, and the messenger -- the same messenger, presumably, though the text does not comment on his fatigue -- walks back and forth across the seven mountain ranges carrying verbal constructions of increasing complexity in a memory that is being asked to do more than memory was designed to do.

Corrected:
> The two kings are well matched. The messenger -- the same messenger, presumably, though the text does not comment on his fatigue -- walks back and forth across the seven mountain ranges, carrying verbal constructions of increasing complexity in a memory that is being asked to do more than memory was designed to do.

## Flagged for human review (not fixed)

These are potential issues the skill scope excludes from automatic correction.

### Flag A (line 3) — Sentence fragment in overview

> Mostly preserved, though some descriptions of the Aratta response are unclear; a peak achievement of Sumerian narrative poetry.

Both halves lack a main verb ("Mostly preserved..." and "a peak achievement..."). Appears to be a marker-resolve artifact (source-overview bullet point rendered verbatim as prose). A grammar-only fix would require adding a verb, which risks touching a marker-resolved passage. Suggest: the line-edit stage rephrase, e.g. "The text is mostly preserved, though some descriptions of the Aratta response are unclear. It is regarded as a peak achievement of Sumerian narrative poetry."

### Flag B (line 3 vs line 8) — Line-count inconsistency

Line 3 gives "approximately 630 lines"; line 8 gives "At approximately 636 lines". Factual change — out of scope for grammar-check. Flag for source-overview or fact-check review.

### Flag C (line 59) — Sentence fragment / marker-resolve artifact

> ETCSL 1.8.2.3, lines 136--155, passage placed early in the narrative as a mythological aside.footnote:[An alternate tradition gives: "Some scholars interpret..."]

Sentence lacks a main verb and reads as unresolved variant-marker text. Fixing would require rewriting a marker-resolved passage.

### Flag D (line 61) — Stray colon-quote and marker-resolve artifact

> Vanstiphout/Alster and ETCSL translation: the passage is a prayer for Enki to restore linguistic unity -- "may they all address Enlil together in a single language" (optative mood).footnote:[An alternate tradition gives: ": the passage describes Enki disrupting..."]

The footnote begins with `: ` (stray colon and space inside the quoted alternate). Appears to be a marker-resolve formatting artifact. Not corrected — marker-resolved content is locked.

### Flag E (line 137) — Lowercase "etcsl" at sentence start / marker artifact

> etcsl 1.8.2.3, lines 500--530, ETCSL composite follows majority manuscript readings.footnote:[...]

Sentence begins with lowercase and reads as a marker-resolve artifact (variant-marker prose rendered verbatim). Fixing would require editing a marker-resolved passage.

### Flag F (lines 74, 104, 178) — Double-period before `.footnote` inside inference markers

Three inline inference markers (pattern: `_(...text..footnote:[Inference:...])_`) contain `..footnote` (two periods before the attribute). Appears in every inference marker in this chapter. Looks like a systematic marker-resolve formatting artifact rather than author intent. Not corrected — marker-resolved content is locked, and the pattern is consistent across all three occurrences, suggesting intended (or at least consistent) formatting.

## Self-check

1. No factual content has changed. The three applied edits split long sentences only; no claim was altered. Line-count discrepancy (630 vs 636) was flagged, not fixed.
2. Footnote count and content unchanged. All `footnote:[...]` and `// EVIDENCE:` lines identical.
3. AsciiDoc structure intact (headings, `'''` section breaks, include-free structure unchanged).
4. All changes logged above; no silent changes.
