# Grammar Check Diff — Chapter 18: The Marriage of Martu

Input: `chapters/18-marriage-of-martu.resolved.adoc`
Output: `chapters/18-marriage-of-martu.grammar-checked.adoc`

## Changes applied

### 1. Number agreement — line 39 (third sentence of the catalogue-of-negation list)

- **Original**: "They do not prepare food properly. They do not build permanent dwelling. They do not observe funerary rites."
- **Corrected**: "They do not prepare food properly. They do not build permanent dwellings. They do not observe funerary rites."
- **Rationale**: "Dwelling" is a countable noun. With the plural subject "they" and no article, the phrase "build permanent dwelling" is ungrammatical. Changed to plural "dwellings" to match the parallel construction of the surrounding list items ("food" = mass noun; "funerary rites" = plural) and the plural subject. No meaning change: the nomads still lack permanent architecture.

## Flagged for human review (no change made)

The following passages contain mechanical punctuation anomalies (double periods) that would normally fall under the grammar-check remit, but they sit inside marker-resolved blocks (`_[ ... ]_`, `_( ... )_`) or inside footnote bodies. Rules 2 and 4 of the skill lock these zones, so they were left untouched and are flagged here instead.

- **Line 33 (marker-resolved block)**: "...are partially broken.. Partial; overlapping manuscripts restore most of the speech, but some details of the ethnographic catalogue remain uncertain..]_" — two instances of double periods (`broken..` and `uncertain..`).
- **Line 35 (footnote body)**: "...ETCSL composite represents consistent manuscript tradition and is the standard text..]" — trailing double period.
- **Line 63 (marker-resolved block and footnote)**: "...the literary tradition could treat with humour rather than anxiety.." and footnote text "...the First Dynasty of Babylon was Amorite).." and "...genuinely cautionary rather than comic..]" — three instances of double periods produced by the marker-resolve stage's period-plus-period concatenation.

Recommend a human review pass on the marker-resolve output to strip trailing "." where the prose sentence already ends in a period.

## Sentences considered but left unchanged

- **Line 67**: "What we can say is that the text, as it reached its Old Babylonian form, reads most naturally as a comedy — a story in which the anxieties of cultural encounter are raised, examined, and then dissolved by the simple expedient of a woman deciding that love, or at least preference, outweighs ethnographic objections." — 56 words. Over the 50-word threshold but splitting would sever the em-dash elaboration from its subject and the concluding parenthetical ("or at least preference") from the main clause. Length is carrying the meaning of a single extended thought; left intact per skill guidance ("unless the length is essential for meaning").
- **Line 13**: "They were the peoples of the western steppe and hill country — semi-nomadic pastoralists who moved with their flocks along the edges of the irrigated lowlands, appearing in Sumerian administrative texts sometimes as trading partners, sometimes as threats, and sometimes simply as people who did things differently." — 46 words, three parallel "sometimes X" clauses. Parallel structure keeps it readable; under threshold; left as is.
- **Line 60**: Long concluding sentence about Amorite conquest — 44 words, clear subject ("The people") followed by a single nested temporal clause. Left as is.
- **Line 42**: "...including proper food preparation, permanent dwelling, and funerary rites" — "permanent dwelling" here functions as a mass-noun concept alongside "proper food preparation" in a list of abstract categories, so the singular reads acceptably in this position. Only the line-39 occurrence (which is a full predicate with "build") was ungrammatical.

## Self-check

- Factual content: unchanged. One number-agreement fix ("dwelling" → "dwellings") does not alter any claim.
- Footnote count: unchanged (15 in input, 15 in output).
- EVIDENCE tokens: unchanged.
- AsciiDoc structure: headings, section breaks (`'''`), and comment directives preserved.
- All changes logged above; no silent edits.
