# Grammar-check diff: 09-ninurta-and-the-turtle

Input: `09-ninurta-and-the-turtle.resolved.adoc`
Output: `09-ninurta-and-the-turtle.grammar-checked.adoc`

Each entry shows the original sentence, the corrected sentence, and the rationale. Only mechanical grammar, readability (>50 words / nested parentheticals / 3+ clauses), and punctuation fixes were made. No word-choice, rhythm, or style changes.

---

## Change 1 — Line 8: sentence fragment (no main verb)

**Original:**
> ETCSL 1.6.3 fragmentary Sumerian text, recovery of tablet by Ninurta stated or implied in surviving lines.

**Corrected:**
> ETCSL 1.6.3 is a fragmentary Sumerian text in which Ninurta's recovery of the tablet is stated or implied in the surviving lines.

**Rationale:** The original is grammatically a fragment — it has no finite main verb. Minimal repair: insert "is a" to form the main clause, recast the comma-joined stub as a relative clause with "in which ... is stated or implied", and add the missing articles ("the tablet", "the surviving lines"). No factual content added or removed.

---

## Change 2 — Line 17: capitalisation after period (bracketed editorial aside)

**Original:**
> ...the context for the theft of the Tablet of Destinies and Ninurta's recovery of it is largely lost. the Akkadian Anzud myth provides a parallel narrative of the tablet theft...

**Corrected:**
> ...the context for the theft of the Tablet of Destinies and Ninurta's recovery of it is largely lost. The Akkadian Anzud myth provides a parallel narrative of the tablet theft...

**Rationale:** Sentence-initial capitalisation after a full stop.

---

## Change 3 — Line 44: capitalisation after period (bracketed editorial aside)

**Original:**
> ...details of the turtle's creation by Enki and the precise mechanism of the trap are partially lost. no other Sumerian witness fills these gaps.

**Corrected:**
> ...details of the turtle's creation by Enki and the precise mechanism of the trap are partially lost. No other Sumerian witness fills these gaps.

**Rationale:** Sentence-initial capitalisation after a full stop.

---

## Change 4 — Line 57: capitalisation after period (bracketed editorial aside)

**Original:**
> ...and what moral the text draws are all uncertain. no Sumerian source fills these gaps; the ending remains unresolved in the surviving record.

**Corrected:**
> ...and what moral the text draws are all uncertain. No Sumerian source fills these gaps; the ending remains unresolved in the surviving record.

**Rationale:** Sentence-initial capitalisation after a full stop.

---

## Change 5 — Line 59: catalogue-code capitalisation (footnote body)

**Original:**
> This passage reconstructs the lacuna at etcsl 1.6.3, late section from the parallel account...

**Corrected:**
> This passage reconstructs the lacuna at ETCSL 1.6.3, late section from the parallel account...

**Rationale:** The catalogue code is rendered as "ETCSL" throughout the chapter (and across the book); this lone lowercase instance is an inconsistency. Punctuation/capitalisation fix only; content unchanged.

---

## Flagged for human review (not auto-fixed)

- **Line 59 footnote**, phrase "from the parallel account in narrative pattern consistent with other Enki-as-trickster episodes" reads as garbled — likely a dropped word ("from the parallel / narrative pattern" or "from ... narrative patterns consistent with"). Because a fix here could change meaning, it is flagged rather than corrected. Recommend the line-edit pass address this.

---

## Self-check

- Factual claims unchanged — the only semantic addition is the implicit copula "is a" and articles "the" in Change 1, which restore grammaticality without introducing new facts.
- Footnote count unchanged (14 `footnote:[...]` instances in both files).
- AsciiDoc structure intact: section heading, horizontal rules (`'''`), italic markers, EVIDENCE comments, COMPARATIVE-HOOK comments all preserved in their original positions.
- Every change is logged above; no silent changes.
