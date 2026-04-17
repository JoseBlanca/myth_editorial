# Grammar-check diff — Chapter 04: Enki's Journey to Nibru

Input: `chapters/04-enkis-journey-to-nibru.resolved.adoc`
Output: `chapters/04-enkis-journey-to-nibru.grammar-checked.adoc`

Each entry: the changed original passage, the corrected version, and the rationale. No factual content, footnotes, EVIDENCE tokens, AsciiDoc markup, or marker-resolved passages were altered. Stylistic matters (word choice, rhythm, nominalisations, paragraph transitions) were left for the line-edit stage.

---

## Change 1 — Line 12: consecutive em-dash parentheticals flattened into two sentences

**Original:**
> The composition opens in Eridu — the oldest city in Sumerian tradition, seat of Enki's temple the E-abzu — where Enki — god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath Eridu — constructs or adorns his temple, the E-engura ("House of the _abzu_").

**Corrected:**
> The composition opens in Eridu — the oldest city in Sumerian tradition and seat of Enki's temple the E-abzu. There, Enki — god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath Eridu — constructs or adorns his temple, the E-engura ("House of the _abzu_").

**Rationale:**
- Readability: the original sentence contained two consecutive em-dash parenthetical asides — one describing Eridu, another describing Enki — with only the connective "where Enki" separating them. The reader had to hold two long appositives in suspension and resolve both before reaching the main verb "constructs". The skill flags "nested parenthetical asides: flatten (move to a separate sentence or footnote)".
- The fix closes the first em-dash aside with a full stop, promotes the relative clause to an independent clause ("There, Enki … constructs or adorns his temple"), and leaves the Enki appositive as a single em-dash pair inside the new second sentence. This keeps exactly one em-dash parenthetical per sentence, which the chapter already establishes as its baseline rhythm (see the Enlil and Baal appositives elsewhere).
- The comma-plus-"and" join ("in Sumerian tradition and seat of Enki's temple") replaces the original comma-spliced appositive list to keep the appositive grammatical as a standalone closing phrase.
- No factual content added, removed, or altered: Eridu is still the oldest city in Sumerian tradition and the seat of the E-abzu; Enki is still characterised identically; the temple he builds or adorns is still the E-engura, glossed identically.

---

## Self-check

- No factual content changed. Every named deity, city, tablet reference, line number, manuscript count, and inference is preserved verbatim.
- Footnote count unchanged (the footnote on the opening-section sentence is preserved at the close of the recast second sentence, on the same text it originally annotated); no footnotes added, removed, or edited.
- EVIDENCE tokens unchanged: same count, same order, same loc fields.
- COMPARATIVE-HOOK comments unchanged.
- AsciiDoc structure preserved: section heading (`==`), thematic breaks (`'''`), italic emphasis (`_abzu_`, `_[...]_` gap marker, `_(...)_` inference parenthetical), footnote syntax, and EVIDENCE/COMPARATIVE-HOOK comment lines are all intact.
- Marker-resolved passages (the `_[At this point the tablet breaks …]_` gap marker on what was line 15, and the `_(The barge journey models the pattern …)_` inference parenthetical on what was line 31) were left untouched per the skill's hard rules.
- Every change above is logged — no silent edits.
- Items noted but deliberately not fixed:
  - "supplemented by ETCSL composite text" (paragraph 1) is a template-artefact-looking word-choice / redundancy issue, not a grammar or readability defect under the stage's scope; deferred to line-edit.
  - Tense shift in "The text was attested as a standard Old Babylonian curriculum text" (final source-overview sentence) versus the present-tense framing elsewhere ("This is a standard Old Babylonian curriculum text") is defensible as referring specifically to the OB period, and falls under register/tense-flow polish for line-edit rather than a mechanical grammar error.
  - No sentence exceeded the 50-word threshold; no compound subject-verb agreement errors were found (the plural "require" in "Enki's authority over the _abzu_ and his cult at Eridu require ratification" correctly agrees with its compound subject).
