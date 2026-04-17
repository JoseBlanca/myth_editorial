# Grammar-check diff: 01-enki-and-ninhursaja

Stage: 14b grammar-check
Input: `chapters/01-enki-and-ninhursaja.resolved.adoc`
Output: `chapters/01-enki-and-ninhursaja.grammar-checked.adoc`

## Changes applied

### Change 1 — Line 3 (opening paragraph, first sentence)

**Issue**: Sentence exceeds 50 words (~54 words) and contains a potentially dangling modifier ("dating to the Old Babylonian period") whose attachment point is ambiguous (could attach to "tablets", "witnesses", or the composition). Splitting also removes the stylistically awkward repetition of "Old Babylonian" within a single sentence.

**Original**:
> The composition known to scholars as "Enki and Ninhursaja" is catalogued as ETCSL 1.1.1 and survives in multiple Old Babylonian manuscript witnesses on clay tablets from both Nippur (Sumerian: Nibru) — the religious capital of Sumer — and Ur, the great port city of the south, dating to the Old Babylonian period (ca. 2000–1600 BCE).

**Corrected**:
> The composition known to scholars as "Enki and Ninhursaja" is catalogued as ETCSL 1.1.1. It survives in multiple Old Babylonian manuscript witnesses (ca. 2000–1600 BCE) on clay tablets from both Nippur (Sumerian: Nibru) — the religious capital of Sumer — and Ur, the great port city of the south.

**Rationale**: Split one >50-word sentence into two. Moved the date range next to "Old Babylonian" so the period reference does the temporal work that "dating to the Old Babylonian period" did in the original, without repeating the phrase and without a dangling modifier. No factual content changed: the manuscripts are still Old Babylonian (ca. 2000–1600 BCE), still on clay tablets, still from Nippur and Ur, and Nippur is still characterised as the religious capital of Sumer and Ur as the great port city of the south.

---

## Issues flagged (not fixed — see "What NOT to fix" and marker-preservation rules)

### Flag 1 — Line 17 (footnote)

**Text**: "The prevalent version is chosen here because ETCSL editorial decision; Ur tribute passage presented separately."

**Issue**: Ungrammatical — "because ETCSL editorial decision" is missing a preposition ("because of the ETCSL editorial decision") or a subordinator ("because the ETCSL made an editorial decision"). This is boilerplate from a resolved alternate-tradition marker and lives inside a footnote.

**Why not fixed**: The brief requires footnotes to remain intact. Flagged for human review at the line-edit or copy-edit stage.

### Flag 2 — Line 41 (footnote)

**Text**: "The prevalent version is chosen here because Co-equal witnesses; Ur tribute passage should be presented as a clearly marked inset per brief instructions."

**Issue**: Same ungrammatical construction as Flag 1 ("because Co-equal witnesses" lacks a verb or preposition). Also capitalisation of "Co-equal" mid-clause is odd.

**Why not fixed**: Footnote content is locked.

### Flag 3 — Line 76 (italicised editorial note)

**Text**: `_(.footnote:[Inference: The text shows Enki eating the plants followed immediately by Ninhursaja's curse; the causal link is strongly implied. Risk: The text does not explicitly label the eating as forbidden or use a word for "transgression".])_`

**Issue**: The italicised editorial note appears to have lost its carrier sentence — only a lone period precedes the footnote call. Likely a marker-resolve artefact where the parenthetical gloss was dropped but the footnote marker remained.

**Why not fixed**: Italicised editorial notes are preserved per the brief. Fixing would require reconstructing content; flagged for human review.

### Flag 4 — Line 104 (italicised editorial note, pronoun agreement)

**Text**: "Each newly born deity is assigned a specific role or domain by Enki, integrating them into the divine order."

**Issue**: Singular antecedent "Each newly born deity" followed by plural pronoun "them". Grammatically, either "Each ... is assigned ... integrating it" (singular) or "The newly born deities are assigned ... integrating them" (plural) would be correct. "Each ... them" is an informal agreement pattern that a strict copy-edit would flag.

**Why not fixed**: The text sits inside an italicised editorial note, which the brief requires be preserved. Flagged for human review.

---

## Self-check

1. Factual content: unchanged. The single edit (Change 1) splits one sentence and relocates the date parenthetical. Every named entity, source, manuscript attribution, and factual claim is preserved verbatim.
2. Footnote count and content: unchanged. No footnote text was altered; no footnotes were added or removed.
3. AsciiDoc structure: unchanged. All headings, section breaks (`'''`), EVIDENCE comments, COMPARATIVE-HOOK comments, and italicised editorial notes remain in place and position.
4. All changes are logged above; no silent edits.
