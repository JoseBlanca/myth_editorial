# Grammar-Check Diff — Chapter 07: Lugal-e

Input: `chapters/07-lugal-e.resolved.adoc`
Output: `chapters/07-lugal-e.grammar-checked.adoc`

Every change below is mechanical (grammar, punctuation, readability). No word-choice, rhythm, or content edits. Footnotes and EVIDENCE tokens are unchanged. AsciiDoc structure is preserved.

---

## Change 1 — Nested parenthetical flattened (line 3)

**Location**: Opening paragraph, second sentence.

**Original**:
> Numerous Old Babylonian manuscripts from Nippur (Sumerian: Nibru) -- the religious capital of Sumer, seat of Enlil's temple the E-kur -- and from other scribal centres attest its wide circulation...

**Corrected**:
> Numerous Old Babylonian manuscripts from Nippur -- the religious capital of Sumer (Sumerian: Nibru), seat of Enlil's temple the E-kur -- and from other scribal centres attest its wide circulation...

**Rationale**: The original stacks a parenthetical `(Sumerian: Nibru)` inside an em-dash aside — a nested parenthetical flagged by the grammar-check criteria. Moving the parens to sit cleanly inside the single em-dash span removes the nesting. The gloss "(Sumerian: Nibru)" was attached to Nippur originally; it now attaches to the apposition "the religious capital of Sumer," which is the same referent, so meaning is preserved.

---

## Change 2 — Sentence start capitalised after period (line 23, inside tablet-break marker)

**Original**:
> ...invocation and initial battle context fragmentary. composite reconstruction from multiple OB manuscripts restores most of the opening.

**Corrected**:
> ...invocation and initial battle context fragmentary. Composite reconstruction from multiple OB manuscripts restores most of the opening.

**Rationale**: A sentence following a period must begin with a capital letter. "composite" → "Composite". Pure mechanical fix.

---

## Change 3 — Overlong, multi-clause sentence split (line 75)

**Location**: Paragraph on the primeval-waters crisis.

**Original** (57 words, two em-dash asides plus three trailing participial clauses):
> Whatever role the demon played in the underground architecture of the world -- however inadvertently, however malignantly -- his destruction has left a gap, and through that gap the deep waters pour upward, flooding the surface, swallowing the fields, turning the cultivated land back into the formless, watery condition that preceded the separation of earth and water.

**Corrected** (split at the conjunction; each half is now well under 50 words):
> Whatever role the demon played in the underground architecture of the world -- however inadvertently, however malignantly -- his destruction has left a gap. Through that gap the deep waters pour upward, flooding the surface, swallowing the fields, turning the cultivated land back into the formless, watery condition that preceded the separation of earth and water.

**Rationale**: 57-word sentence with three-plus subordinate clauses. The "and" after "gap" was a comma-and joint between two independent clauses; replacing it with a period produces two clean sentences with no loss of meaning.

---

## Change 4 — Stacked em-dash list flattened (line 112)

**Location**: Catalogue-inventory paragraph near the close of the stone-fate section.

**Original** (four em-dashes used to introduce three sub-lists; parse is ambiguous):
> The catalogue includes stones used in building -- limestone, bitite -- stones used as weights and tools -- hematite -- and decorative stones, reflecting a comprehensive Sumerian mineralogical knowledge embedded in mythological narrative.

**Corrected**:
> The catalogue includes building stones such as limestone and bitite, stones used as weights and tools such as hematite, and decorative stones, reflecting a comprehensive Sumerian mineralogical knowledge embedded in mythological narrative.

**Rationale**: Four em-dashes in one sentence, alternating between category labels and examples, force the reader to re-parse. The corrected form uses "such as" to attach each example to its category, yielding a clear three-item list with serial comma. Meaning, referents, and category/example pairings are identical to the original.

---

## Change 5 — Sentence start capitalised after period (line 98, tablet-break marker)

**Original**:
> ...damaged, with gaps in the individual verdicts for some stones. overlapping manuscripts cover different subsections but no single witness is complete.

**Corrected**:
> ...damaged, with gaps in the individual verdicts for some stones. Overlapping manuscripts cover different subsections, but no single witness is complete.

**Rationale**: Two fixes in one line — "overlapping" → "Overlapping" (capital after period), and a comma added before "but" joining two independent clauses (standard coordinating-conjunction comma). Both are mechanical punctuation fixes.

---

## Change 6 — Nested parenthetical flattened (line 129)

**Location**: Paragraph introducing the mother-renaming episode.

**Original**:
> It is a naming ceremony -- the same kind of theological act that we saw in "Enlil and Sud" (chapter 6), where the young goddess Sud was renamed Ninlil upon her marriage to Enlil.

**Corrected**:
> It is a naming ceremony -- the same kind of theological act that we saw in "Enlil and Sud" in chapter 6, where the young goddess Sud was renamed Ninlil upon her marriage to Enlil.

**Rationale**: The parenthetical "(chapter 6)" sits inside an em-dash aside, creating a nested parenthetical. Converting it to the prepositional phrase "in chapter 6" removes the nesting while preserving the cross-reference.

---

## Change 7 — Sentence start capitalised after period (line 132, tablet-break marker)

**Original**:
> ...has minor gaps in the praise formula and the mother-renaming passage. multiple manuscripts preserve the ending with minor variation.

**Corrected**:
> ...has minor gaps in the praise formula and the mother-renaming passage. Multiple manuscripts preserve the ending with minor variation.

**Rationale**: "multiple" → "Multiple". Capital after period.

---

## Change 8 — Long multi-clause sentence split (line 157)

**Location**: Closing comparative paragraph on Enuma Elish derivation.

**Original** (52 words, em-dash aside plus three trailing participial clauses governed by a single verb):
> If anything, the Enuma Elish drew on the tradition that Lugal-e represents -- adapting the Sumerian pattern of Ninurta and Asag to the Babylonian context of Marduk and Tiamat, substituting the patron god of Babylon for the champion of Nippur, but retaining the fundamental structure of the narrative: battle, victory, cosmic reorganisation.

**Corrected** (split between the two contrasting actions "substituting" and "retaining"):
> If anything, the Enuma Elish drew on the tradition that Lugal-e represents, adapting the Sumerian pattern of Ninurta and Asag to the Babylonian context of Marduk and Tiamat. It substituted the patron god of Babylon for the champion of Nippur but retained the fundamental structure of the narrative: battle, victory, cosmic reorganisation.

**Rationale**: Over 50 words with three trailing `-ing` clauses attached to "drew on." The original em-dash also introduced an asymmetry (a single "adapting" clause further elaborated by a "substituting... but retaining" coordinated pair). The split creates two sentences of equal readability and converts the second pair from participles to finite verbs ("substituted... retained"), which also resolves an unclear verb-form parallel. Meaning is preserved exactly.

---

## Self-check

- **Factual content**: No claims altered. All referents, dates, line ranges, stone names, and names of gods are identical in both files.
- **Footnotes**: 41 in both files. Content unchanged; no footnote added, removed, or modified.
- **EVIDENCE tokens**: 34 in both files. Unchanged.
- **COMPARATIVE-HOOK lines**: 4 in both files. Unchanged.
- **AsciiDoc structure**: Heading, section dividers (`'''`), italic-bracketed tablet-break blocks, italic-paren inference blocks, and footnote syntax all preserved.
- **Line count**: 171 in both files (no paragraph splitting across blank lines; all splits were within existing paragraphs).
- **Marker-resolved inference paragraphs (lines 85, 115, 160)**: Left untouched per skill rule "No content changes to resolved marker passages."
- **Every change logged above**: No silent edits.
