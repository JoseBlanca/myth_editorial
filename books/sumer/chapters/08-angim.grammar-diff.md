# Grammar-check diff: 08-angim

Input: `chapters/08-angim.resolved.adoc`
Output: `chapters/08-angim.grammar-checked.adoc`

## Summary

One mechanical fix: a missing comma after an introductory prepositional phrase. No other changes were required. The chapter is otherwise grammatically clean: no sentences exceed 50 words, no nested parentheticals exist, no subject-verb mismatches, no dangling modifiers, and punctuation (em-dashes, serial commas, apostrophes in non-English terms) is consistent.

## Changes

### Change 1 — Line 73 (conclusion paragraph, main body)

**Original:**
> In the Sumerian theological framework these are not contradictions.

**Corrected:**
> In the Sumerian theological framework, these are not contradictions.

**Rationale:** Missing comma after the introductory prepositional phrase "In the Sumerian theological framework." Standard punctuation practice is to set off an introductory phrase of five or more words with a comma. Without the comma the reader briefly parses "framework these" as a noun cluster before re-parsing. Pure punctuation fix; no meaning change.

---

## Items considered but NOT changed

The following were noted during the scan but left as-is per the skill's "what NOT to fix" rules.

- **Line 11 (footnote):** The fragment "Black et al. used for literary context and alternate renderings" is missing a verb ("is" / "are"). Inside footnote content; skill forbids footnote edits.
- **Line 11 (footnote):** Subject-verb number ambiguity around "Black et al. 2004 pp. 181–186 offers minor translation differences". Footnote content; left as-is.
- **Line 28 (lacuna marker block):** The sequence "details of the trophy display are fragmentary. partial; the bilingual Akkadian version…" contains an orphaned "partial;" token that appears to be a leftover from marker resolution. Marker-resolved passage; skill forbids changes.
- **Line 38 (inference block in parenthetical italics):** Structural analysis passage; left untouched as a marker-resolved passage.
- **Line 51 (footnote):** "from the parallel account in surrounding intact lines establish the pattern" is ungrammatical (dropped verb/structure), but this is footnote content.
- **Line 63:** "If Enlil's contribution was the formal framework, Ninlil's is the emotional one." Minor tense inconsistency between the two clauses, but the conditional-hypothetical construction ("if we say X about Enlil, then…") is defensible, and changing tense would alter the rhetorical frame. Flagged for human/line-edit awareness rather than auto-corrected.
- **Line 3:** "It survives on Old Babylonian manuscripts" — "on" vs "in" is a preposition/word-choice judgement; belongs to line-edit.
- **Line 35:** "a proportion disproportionate to any other section" — word choice; belongs to line-edit.
- **Long sentences flagged by word count:** three sentences fall in the 40–42-word range (line 13, and two in line 87). All are under the 50-word threshold and parse cleanly; left unchanged.
- **Title italicisation inconsistency:** "Iliad" and "Tain Bo Cuailnge" are unitalicised in the main text while "Lugal-e", "Angim", "riastrad", and "me-lam" are italicised. This is a house-style choice, not grammar.
- **Diacritic inconsistency:** "Tain Bo Cuailnge" (bare) in main text vs. "ríastrad" (acute in comparative hook). House style / transliteration choice.

## Self-check

- Factual content unchanged. Verified via full diff: only a comma inserted at line 73.
- Footnote count: 19 before, 19 after. Footnote content byte-identical.
- AsciiDoc structure intact: heading, section dividers (`'''`), italic lacuna markers, EVIDENCE comments, and COMPARATIVE-HOOK comments all preserved in their original positions.
- Every change logged above (one total).
