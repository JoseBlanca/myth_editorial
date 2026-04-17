# Grammar diff — Chapter 30: The Death of Ur-Namma

Every mechanical change made by the grammar-check stage, listed as `original → corrected` with a rationale. No factual, stylistic, or footnote-content changes were made. AsciiDoc structure, footnote count, and EVIDENCE / COMPARATIVE-HOOK tokens are preserved.

---

## Change 1 — stray double period before footnote token (line 21, first inference note)

**Original:**
`an unusual and deeply humiliating circumstance for a Sumerian king..footnote:[Inference: ...`

**Corrected:**
`an unusual and deeply humiliating circumstance for a Sumerian king.footnote:[Inference: ...`

**Rationale:** Punctuation error. A sentence-terminal period was doubled, producing `..` immediately before the `footnote:` macro. Removed the extra period.

---

## Change 2 — stray double period inside the first Inference note (line 21)

**Original:**
`Inference: The imagery of abandonment and the "crushed vessel" simile imply disgrace beyond ordinary death.. Risk: ...`

**Corrected:**
`Inference: The imagery of abandonment and the "crushed vessel" simile imply disgrace beyond ordinary death. Risk: ...`

**Rationale:** Punctuation error. A doubled sentence-terminal period (`..`) between the Inference and Risk clauses was reduced to a single period.

---

## Change 3 — stray double period at the end of the first Risk clause (line 21)

**Original:**
`Risk: The fragmentary state means we cannot be certain of the exact military context..])_`

**Corrected:**
`Risk: The fragmentary state means we cannot be certain of the exact military context.])_`

**Rationale:** Punctuation error. A doubled sentence-terminal period was reduced to a single period before the closing bracket and parenthesis.

---

## Change 4 — missing capitalisation after sentence-terminal period (line 39, second editorial lacuna note)

**Original:**
`have minor gaps in lines 100–140. overlapping Nippur manuscripts allow reconstruction of most of the passage.`

**Corrected:**
`have minor gaps in lines 100–140. Overlapping Nippur manuscripts allow reconstruction of most of the passage.`

**Rationale:** Capitalisation error. A new sentence began with lowercase `overlapping` after a full stop. Capitalised to `Overlapping` to match standard sentence-initial capitalisation.

---

## Change 5 — stray double period before footnote token (line 62, second inference note)

**Original:**
`the king of Ur retains dignity and commands respect from the underworld powers..footnote:[Inference: ...`

**Corrected:**
`the king of Ur retains dignity and commands respect from the underworld powers.footnote:[Inference: ...`

**Rationale:** Punctuation error. A sentence-terminal period was doubled immediately before the `footnote:` macro. Removed the extra period.

---

## Change 6 — stray double period inside the second Inference note (line 62)

**Original:**
`Inference: The elaborate gift-giving and the honored reception are clearly designed to elevate Ur-Namma's posthumous status.. Risk: ...`

**Corrected:**
`Inference: The elaborate gift-giving and the honored reception are clearly designed to elevate Ur-Namma's posthumous status. Risk: ...`

**Rationale:** Punctuation error. A doubled sentence-terminal period (`..`) between the Inference and Risk clauses was reduced to a single period.

---

## Change 7 — stray double period at the end of the second Risk clause (line 62)

**Original:**
`Risk: The propagandistic function is widely accepted by scholars but the text does not make this meta-purpose explicit..])_`

**Corrected:**
`Risk: The propagandistic function is widely accepted by scholars but the text does not make this meta-purpose explicit.])_`

**Rationale:** Punctuation error. A doubled sentence-terminal period was reduced to a single period before the closing bracket and parenthesis.

---

## Self-check

1. No factual content changed — all claims about ETCSL 2.4.1.1, manuscript witnesses, Flückiger-Hawker/Kramer/Jacobsen/Black references, Ur-Namma's dates (2112–2095 BCE), line ranges, underworld-judges (Gilgamesh/Bilgames, Ningishzida), Ereshkigal tribute, parallels (Egyptian Book of the Dead, Homer's Odyssey Book 11, Gilgamesh), etc. are identical.
2. Footnote count and content unchanged — all footnote macros (ETCSL, Flückiger-Hawker, Kramer, Jacobsen, Black, and the two Inference/Risk editorial footnotes) are preserved verbatim apart from the doubled-period punctuation fixes logged above.
3. EVIDENCE and COMPARATIVE-HOOK tokens preserved verbatim.
4. AsciiDoc structure (heading `==`, section breaks `'''`, italic/emphasis markers, inline emphasis `_kur_`) intact.
5. No sentences exceed 50 words; no nested parentheticals requiring flattening; no three-plus-clause constructions were identified for simplification. All changes above are mechanical punctuation or capitalisation fixes — no sentences were restructured or split.
6. Every change logged above — no silent changes.
