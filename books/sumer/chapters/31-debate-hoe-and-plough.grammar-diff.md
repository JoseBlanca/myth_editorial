# Grammar-check diff: 31-debate-hoe-and-plough

Stage: 14b grammar-check
Input: `chapters/31-debate-hoe-and-plough.resolved.adoc`
Output: `chapters/31-debate-hoe-and-plough.grammar-checked.adoc`

Every mechanical change is listed below as `original → corrected` with a rationale. No factual, stylistic, or footnote-content changes were made. AsciiDoc structure, footnote count, EVIDENCE markers, and COMPARATIVE-HOOK markers are preserved verbatim.

---

## Change 1 — Line 3 (opening paragraph): semicolon joining a noun-phrase fragment

**Original:**
> The composition known as "The Debate between Hoe and Plough" is catalogued as ETCSL 5.3.1 and survives on Old Babylonian tablets from Nippur (Sumerian: Nibru) -- the religious capital of Sumer, seat of Enlil's temple the E-kur -- and Ur; a standard curriculum text.footnote:[ETCSL 5.3.1, bibliography.]

**Corrected:**
> The composition known as "The Debate between Hoe and Plough" is catalogued as ETCSL 5.3.1 and survives on Old Babylonian tablets from Nippur (Sumerian: Nibru) -- the religious capital of Sumer, seat of Enlil's temple the E-kur -- and Ur. It was a standard curriculum text.footnote:[ETCSL 5.3.1, bibliography.]

**Rationale:** Punctuation / fragment fix. A semicolon should join two independent clauses, but "a standard curriculum text" is a noun-phrase fragment, not an independent clause. The original also stretched a single sentence over four clauses plus a nested em-dash parenthetical. Splitting into two sentences (ending "…and Ur." + "It was a standard curriculum text.") repairs the semicolon misuse, removes the fragment, and reduces clause load. No factual content changed: the tablets are still Old Babylonian, still from Nippur and Ur, Nippur is still the religious capital of Sumer and seat of the E-kur, and the composition is still described as a standard curriculum text. Footnote unchanged.

---

## Change 2 — Line 89 (closing paragraph): over-50-word sentence with nested em-dash parenthetical

**Original:**
> What is clear is that the Sumerian version is the oldest surviving example of the genre, and that its treatment of the subject -- agricultural tools as cosmologically significant entities whose relative worth requires divine adjudication -- reflects a worldview in which human technology was not merely practical but divinely ordered.

**Corrected:**
> What is clear is that the Sumerian version is the oldest surviving example of the genre. Its treatment of the subject -- agricultural tools as cosmologically significant entities whose relative worth requires divine adjudication -- reflects a worldview in which human technology was not merely practical but divinely ordered.

**Rationale:** Readability fix. The original sentence ran to about 51 words, joined two independent "that"-clauses under one "What is clear is…" frame, and embedded an em-dash parenthetical across the join, forcing the reader to hold the syntax open over a long span. Splitting after "…the oldest surviving example of the genre." produces two sentences under 40 words each, keeps the em-dash parenthetical inside a single sentence, and preserves the logical link (the second sentence picks up the subject with "Its treatment"). No factual content changed: the Sumerian version is still identified as the oldest surviving example, the subject is still characterised the same way, and the worldview claim is unchanged.

---

## Flagged — not fixed

### Flag 1 — Line 71: nested parentheses inside the italicised editorial inference note

**Text:**
> _(Enlil's verdict for the Hoe reflects the tool's wider utility and its cosmogonic priority (Enlil created it first in the prologue).footnote:[Inference: The prologue gives Hoe primordial precedence; the verdict is consistent with the debate structure favouring the more versatile entity. Risk: The text does not state the reasoning behind the verdict in explicit analytical terms; this is interpretive.])_

**Issue:** The italicised inference note contains nested parentheses: the outer `_( … )_` wrapper encloses another `( … )` parenthetical around "Enlil created it first in the prologue". Under the readability rules this would ordinarily be flattened.

**Why not fixed:** This is a resolved marker passage (an `Inference/Risk` editorial note produced by stage 13 marker-resolve). The brief locks the content of marker-resolved passages. Flattening the inner parenthetical — whether by replacing the inner parens with em-dashes or by promoting the aside to a separate sentence — would edit the text of that protected passage. Flagged for human review at line-edit.

---

## Self-check

1. **No factual content changed.** Every claim about ETCSL 5.3.1, the manuscript witnesses (Nippur and Ur), the Old Babylonian date, the _edubba_ curriculum, the debate genre (_a-da-min_), the two disputants (Hoe / _al_ and Plough / _apin_), the cosmogonic prologue, Enlil's role, the arguments marshalled by each implement, the verdict in favour of the Hoe, and the comparative parallels (_The Owl and the Nightingale_, the _conflictus_ genre, _Conflictus Veris et Hiemis_) is preserved verbatim. Source attributions (ETCSL, Black et al. 2004, Civil 1994, Kramer 1961) are unchanged.
2. **Footnote count and content unchanged.** All footnote macros and their text are preserved verbatim; no footnotes added, removed, or edited.
3. **EVIDENCE and COMPARATIVE-HOOK tokens preserved verbatim** in all positions.
4. **AsciiDoc structure intact:** chapter heading `==`, section headings `===`, section breaks `'''`, italic emphasis (`_al_`, `_apin_`, `_a-da-min_`, `_edubba_`, `_conflictus_`, `_Conflictus Veris et Hiemis_`, `_The Owl and the Nightingale_`), italicised editorial inset `_[ … ]_`, and the italicised inference note `_( … )_` are all in place and position.
5. **Every change logged above.** No silent edits.
