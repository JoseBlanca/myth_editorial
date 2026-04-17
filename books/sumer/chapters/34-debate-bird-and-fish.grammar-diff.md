# Grammar-check diff — Chapter 34: The Debate between Bird and Fish

Input: `34-debate-bird-and-fish.resolved.adoc`
Output: `34-debate-bird-and-fish.grammar-checked.adoc`

This chapter was already in clean shape. Only one readability change was applied; no grammar errors, punctuation issues, or ambiguous references required fixing.

## Changes

### Change 1 — Split sentence over 50 words (readability: >50-word rule)

**Location:** Final section ("The composition in context"), final paragraph, last sentence.

**Original (53 words):**
> The Sumerian composition takes the animal fable to a place that later traditions, on the whole, chose not to follow: the place where argument fails and force begins, and where the existence of a legitimate authority to settle the matter is not a given but a necessity discovered through the experience of destruction.

**Corrected:**
> The Sumerian composition takes the animal fable to a place that later traditions, on the whole, chose not to follow: the place where argument fails and force begins. Here, the existence of a legitimate authority to settle the matter is not a given but a necessity discovered through the experience of destruction.

**Rationale:** The original is 53 words with three coordinated "where"/"and where" clauses hanging off a colon-introduced apposition. Split after "force begins" and replaced the coordinator "and where" with a new sentence beginning "Here,". Meaning is preserved: the two relative clauses become two claims about the same "place". No factual content changed.

## Items reviewed and left unchanged

The following were examined and judged to need no grammar intervention (style/rhythm decisions are deferred to line-edit):

- **Line 8, sentence with nested glosses** ("Bird (Sumerian _mušen_) and Fish (Sumerian _ku₆_)" set off by em-dashes): the parenthetical inserts are inline glosses for named entities, not nested asides. Kept.
- **Line 12, participial phrase** "Enki's wisdom stands behind the royal verdict, acknowledged in the closing doxology but not exercised directly": the participle "acknowledged" logically attaches to "Enki's wisdom" (the subject), not the nearest noun "verdict". Borderline dangling; rewriting would change rhythm without improving grammar. Left.
- **Line 19, "given to it by divine decree"**: "it" = "creature", clear from context. Left.
- **Line 22, "Fish inhabits the deep waters, abundant in the rivers and canals"**: modifier applies to "Fish" (or to "waters"); either parse yields the same meaning. Left.
- **Line 45, "It inverts it"**: repeated "it" reads cleanly in the established parallelism ("the insult ... the claim"). Left.
- **Line 59, editorial aside with two stacked -ing clauses** ("demonstrating ... necessitating ..."): flagged aside in italics/parens, not mainline prose; register allows it. Left.
- **Line 80, "making it one of the most literarily accomplished..."**: "it" refers to the composition; the participle attaches naturally via the scholarly evaluation. Left.
- **Line 87, "uses personified animals teaching through competitive interaction"**: mild reduced-relative awkwardness ("animals [who are] teaching"); fix would be word choice, which is line-edit's job. Left.
- **Punctuation**: em-dashes (`--`), en-dashes in page/line ranges, quotation marks, and apostrophes in non-English terms (_mušen_, _ku₆_, _abzu_, _edubba_) are consistent. No changes.
- **AsciiDoc structure**: all headings, thematic breaks (`'''`), italic emphasis, EVIDENCE comments, footnotes, and COMPARATIVE-HOOK comments preserved unchanged.

## Self-check

1. Factual content unchanged — compared claims before/after; only word-order in one sentence.
2. Footnotes: 17 in original, 17 in output; content identical.
3. AsciiDoc structure intact: 1 `==` heading, 4 `===` headings, 5 `'''` breaks, all EVIDENCE and COMPARATIVE-HOOK lines preserved.
4. Every change logged above.
