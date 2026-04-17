# Grammar diff — Chapter 29: Ningishzida's Journey to the Nether World

Every mechanical change made by the grammar-check stage, listed as `original → corrected` with a rationale. No factual, stylistic, or footnote-content changes were made. AsciiDoc structure, footnote count, and EVIDENCE tokens are preserved.

---

## Change 1 — stray double period before footnote token (line 28)

**Original:**
`agents who carry out the nether world's demands for a substitute or victim..footnote:[Inference: ...`

**Corrected:**
`agents who carry out the nether world's demands for a substitute or victim.footnote:[Inference: ...`

**Rationale:** Punctuation error. A sentence-terminal period was doubled, producing `..` immediately before the `footnote:` macro. Removed the extra period.

---

## Change 2 — stray double period inside the Inference note (line 28)

**Original:**
`Inference: The galla appear in the same capacity in Inanna's Descent and other texts.. Risk: ...`

**Corrected:**
`Inference: The galla appear in the same capacity in Inanna's Descent and other texts. Risk: ...`

**Rationale:** Punctuation error. A doubled sentence-terminal period (`..`) between the Inference and Risk clauses was reduced to a single period.

---

## Change 3 — stray double period at the end of the Risk clause (line 28)

**Original:**
`the parallel to the substitute-mechanism in Inanna's Descent is structural, not textually explicit in this composition..])_`

**Corrected:**
`the parallel to the substitute-mechanism in Inanna's Descent is structural, not textually explicit in this composition.])_`

**Rationale:** Punctuation error. A doubled sentence-terminal period was reduced to a single period before the closing parenthesis and bracket.

---

## Change 4 — missing capitalisation after sentence-terminal period (line 37)

**Original:**
`only fragments of individual lament stanzas survive. no overlapping manuscripts fill the gaps.`

**Corrected:**
`only fragments of individual lament stanzas survive. No overlapping manuscripts fill the gaps.`

**Rationale:** Capitalisation error. A new sentence began with lowercase `no` after a full stop. Capitalised to `No` to match standard sentence-initial capitalisation.

---

## Change 5 — over-long sentence split at colon (line 48, final paragraph before the comparative hooks)

**Original (one sentence, 62 words):**
`The structural parallel — a divine or semi-divine figure taken below while the living mourn — is close enough to suggest that the pattern addresses something fundamental about how human beings conceptualise death and loss: the departed is taken against their will, those who remain can do nothing but lament, and the lament itself becomes the only response available to the living.`

**Corrected (two sentences):**
`The structural parallel — a divine or semi-divine figure taken below while the living mourn — is close enough to suggest that the pattern addresses something fundamental about how human beings conceptualise death and loss. The departed is taken against their will, those who remain can do nothing but lament, and the lament itself becomes the only response available to the living.`

**Rationale:** Readability — the sentence exceeded the 50-word threshold (62 words) and combined a main clause with a three-item list. Replacing the colon with a full stop splits it cleanly without changing meaning, facts, or emphasis; the list still reads as the unpacking of the preceding claim.

---

## Self-check

1. No factual content changed — all claims about ETCSL 1.7.3, manuscript witnesses, Jacobsen/Kramer/Black references, parallels to Inanna's Descent, galla function, Greek parallels (Persephone/Demeter/Orpheus), etc. are identical.
2. Footnote count and content unchanged — six footnotes (Inference footnote preserved; ETCSL, Jacobsen, Black, Kramer citations unchanged).
3. EVIDENCE and COMPARATIVE-HOOK tokens preserved verbatim.
4. AsciiDoc structure (heading, section breaks `'''`, italics, emphasis) intact.
5. Every change logged above — no silent changes.
