# Grammar-check diff — Chapter 03: Enki and the World Order

Input: `chapters/03-enki-and-the-world-order.resolved.adoc`
Output: `chapters/03-enki-and-the-world-order.grammar-checked.adoc`

Each entry: the changed original passage, the corrected version, and the rationale. No factual content, footnotes, EVIDENCE tokens, AsciiDoc markup, or marker-resolved passages were altered. Stylistic matters (word choice, rhythm, nominalisations, paragraph transitions) were left for the line-edit stage.

---

## Change 1 — Line 20: over-long, grammatically tangled sentence split into two

**Original:**
> Enki declares that his father An has entrusted him, with Enlil — king of the gods, lord of wind and command, supreme authority in Nippur — delegating authority to him, with the task of organising the world: assigning functions, establishing offices, and decreeing the destinies of lands, rivers, and crafts.

**Corrected:**
> Enki declares that his father An has entrusted him with the task of organising the world: assigning functions, establishing offices, and decreeing the destinies of lands, rivers, and crafts. Enlil — king of the gods, lord of wind and command, supreme authority in Nippur — has likewise delegated authority to him.

**Rationale:**
- Length: the original ran to about 51 words, over the 50-word readability threshold.
- Structure: "has entrusted him, with Enlil … delegating authority to him, with the task" forced the reader to hold two non-parallel "with" phrases in suspension and repeated "him" ambiguously. The construction was grammatically strained and hard to parse on first reading.
- The fix separates the two propositions (An entrusts Enki with the task; Enlil likewise delegates authority to him) into two sentences without adding, removing, or changing any factual content. The Enlil parenthetical is preserved intact.

---

## Change 2 — Line 23: subject-verb agreement

**Original:**
> They are something closer to the operating principles of civilisation itself — the know-how and authority that makes each institution, each craft, each social role possible.

**Corrected:**
> They are something closer to the operating principles of civilisation itself — the know-how and authority that make each institution, each craft, each social role possible.

**Rationale:**
- "The know-how and authority" is a compound subject of the relative clause "that … each institution … possible" and therefore takes the plural verb "make". Changed "makes" to "make" to correct subject-verb agreement. No change in meaning.

---

## Self-check

- No factual content changed. Every named deity, tablet reference, line number, manuscript reference, and inference is preserved.
- Footnote count unchanged (original and corrected both contain the same footnotes in the same positions); no EVIDENCE tokens added or removed.
- AsciiDoc structure preserved: heading, thematic breaks (`'''`), italic emphasis, footnote syntax, gap markers, COMPARATIVE-HOOK comments, and EVIDENCE comments are all intact.
- Every change above is logged — no silent edits.
- Marker-resolved passages (bracketed gap markers, `_(...)_` inference parenthetical, and the alternate-tradition footnote in line 112) were left untouched even where phrasing was awkward, per the skill's hard rules.
- Adverb placement in "sets up narratively the tensions" (line 121) and the fragment-like "because More recent collation …" inside the footnote on line 112 were both noted but deliberately not fixed: the first is a style/word-order question for line-edit, and the second lies inside locked footnote content.
