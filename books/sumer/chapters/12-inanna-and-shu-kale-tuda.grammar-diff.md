# Grammar-check diff: Chapter 12 — Inanna and Shu-kale-tuda

Scope: mechanical grammar, punctuation, and readability fixes only. Marker-resolved
passages (text tied to EVIDENCE/RECONSTRUCT markers), footnote content, AsciiDoc
structure, and stylistic choices were preserved.

## Change 1 — Punctuation: duplicated period before footnote (line 45)

- **Original:** `The first plague involves the corruption of water..footnote:[...]`
- **Corrected:** `The first plague involves the corruption of water.footnote:[...]`
- **Rationale:** Double period (`..`) is a punctuation typo — the sentence already
  ends with a period, so the second one is stray. A single sentence-terminating
  period is correct. No change to marker-resolved footnote content.

## Change 2 — Punctuation: duplicated period before footnote (line 68)

- **Original:** `The third plague involves the obstruction of roads or travel..footnote:[...]`
- **Corrected:** `The third plague involves the obstruction of roads or travel.footnote:[...]`
- **Rationale:** Same stray second period as change 1. Fixed for punctuation
  consistency. Footnote content left untouched.

## Change 3 — Readability: split 72-word sentence with nested em-dash aside (line 47)

- **Original:** `In a land where fresh water was not merely important but sacred --
  where Enki, god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath
  Eridu, ruled over the underground freshwater ocean and the entire theological
  architecture of civilisation rested on the canal and the reservoir -- the
  corruption of water is an attack on the foundations of existence.`
- **Corrected:** `In a land where fresh water was not merely important but sacred --
  where Enki, god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath
  Eridu, ruled over the underground freshwater ocean -- the corruption of water is
  an attack on the foundations of existence. The entire theological architecture of
  civilisation rested on the canal and the reservoir.`
- **Rationale:** Original sentence ran to ~72 words with a nested em-dash aside that
  itself joined two independent clauses via "and" (Enki ruled… / architecture
  rested…). That forced the reader to track parallel thoughts inside a parenthetical
  and qualifies for the "over 50 words" and "three or more subordinate clauses"
  rules. Moving the second "architecture rested" clause into its own sentence
  preserves the full content (no factual change) and keeps the em-dash aside to a
  single idea. All proper nouns, facts, and sourcing preserved.

## Change 4 — Grammar: ungrammatical conjunction in paradox sentence (line 91)

- **Original:** `The composition concludes with a paradox that although Shu-kale-tuda
  is destroyed, his name will be remembered…`
- **Corrected:** `The composition concludes with a paradox: although Shu-kale-tuda
  is destroyed, his name will be remembered…`
- **Rationale:** "a paradox that although X, Y" is ungrammatical — "that" introduces
  a noun clause but "although X, Y" is a concessive adverbial construction, not a
  noun clause. Replacing "that" with a colon lets the adverbial clause follow
  correctly as an appositive expansion of "paradox". No content change.

## Change 5 — Readability: split 57-word sentence with parallel subordinate clauses (line 102)

- **Original:** `The theme of collective punishment until a hidden guilty individual
  is revealed appears also in the Achan episode of Joshua 7, where Israel suffers
  military defeat because one man has stolen consecrated goods, and in the opening
  of Homer's Iliad, where Apollo sends plague upon the Greek camp because Agamemnon
  refuses to return a priest's daughter.`
- **Corrected:** `The theme of collective punishment until a hidden guilty individual
  is revealed appears also in the Achan episode of Joshua 7, where Israel suffers
  military defeat because one man has stolen consecrated goods. It appears, too, in
  the opening of Homer's Iliad, where Apollo sends plague upon the Greek camp
  because Agamemnon refuses to return a priest's daughter.`
- **Rationale:** 57 words with four subordinate clauses (two "where…" plus two
  "because…"). Qualifies for the "three or more subordinate clauses" rule. Splitting
  at the conjunction "and in the opening" preserves both parallel examples and
  requires only a light connective ("It appears, too,") to keep the flow. No
  factual change; both citations intact.

## Items flagged for human review (NOT fixed)

### Flag A — Orphan inference marker (line 94)

```
_(.footnote:[Inference: The text explicitly states Shu-kale-tuda's name will
not be forgotten.. Risk: Some scholars may read this as a standard scribal
colophon formula rather than deliberate literary irony..])_
```

This appears to be an unresolved INFERENCE marker that survived the
marker-resolve stage: the leading `.` inside `(.footnote:[...])`, the doubled
periods inside the footnote text, and the italicised parenthetical wrapper are
characteristic of marker syntax rather than reader-facing prose. Per the
hard rule against modifying marker-resolved passages and footnote content, no
change was made. Recommend human review to decide whether to keep the
note as a footnote, promote it into the body, or remove it.

### Flag B — Marker-style `..` inside narrative break notes (lines 14, 43, 58)

The bracketed narrative-break notes such as
`_[At this point the tablet breaks. … partially lost.. partial, some
manuscripts preserve fragments of the opening..]_` use `..` as a separator
between the human-facing text and the manuscript-availability note. This is a
consistent marker convention, not a typo, so it was left untouched. Flagging
only in case the pipeline expects this to be cleaned up at a later stage.

## Self-check

1. No factual claims were changed. Every proper noun, date, citation, and
   source reference in the corrected file matches the original.
2. Footnote count unchanged (original and corrected both contain the same
   `footnote:[...]` instances) and footnote content unchanged.
3. All AsciiDoc structure preserved: the `==` heading, `'''` section breaks,
   italic/bold markup, `// EVIDENCE:` and `// COMPARATIVE-HOOK:` comment
   lines, and the `_[…]_` narrative-break blocks are all intact.
4. Every change above is logged; no silent edits.
