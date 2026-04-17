# Grammar-check diff — Chapter 05: Enlil and Ninlil

Input: `chapters/05-enlil-and-ninlil.resolved.adoc`
Output: `chapters/05-enlil-and-ninlil.grammar-checked.adoc`

Each entry: the changed original passage, the corrected version, and the rationale. No factual content, footnotes, EVIDENCE tokens, AsciiDoc markup, COMPARATIVE-HOOK comments, or marker-resolved passages were altered. Stylistic matters (word choice, rhythm, nominalisations, paragraph transitions) were left for the line-edit stage.

---

## Change 1 — Line 3 (source-overview opening): 56-word sentence split at the semicolon

**Original:**
> The composition known to scholars as "Enlil and Ninlil" is catalogued as ETCSL 1.2.1 and extends to approximately 152 lines in the composite text; it is one of the most heavily attested Sumerian narrative compositions, with numerous Old Babylonian copies from Nippur (Sumerian: Nibru) — the religious capital of Sumer, seat of Enlil's temple the E-kur.

**Corrected:**
> The composition known to scholars as "Enlil and Ninlil" is catalogued as ETCSL 1.2.1 and extends to approximately 152 lines in the composite text. It is one of the most heavily attested Sumerian narrative compositions, with numerous Old Babylonian copies from Nippur (Sumerian: Nibru) — the religious capital of Sumer, seat of Enlil's temple the E-kur.

**Rationale:**
- Readability: the original sentence was 56 words — above the skill's 50-word threshold — and carried two distinct propositions (catalogue/length, attestation/provenance) already joined by a semicolon. The skill flags "sentences over 50 words: split or restructure unless the length is essential for meaning".
- The fix promotes the semicolon to a full stop, converts the pronoun "it" to sentence-initial "It" (capitalisation), and leaves all other punctuation and content unchanged. Each resulting sentence is now under the threshold and carries one main proposition.
- No factual content added, removed, or altered: catalogue number, line count, attestation claim, provenance, parenthetical Sumerian name, and the Nippur appositive are preserved verbatim with their footnote.

---

## Change 2 — Line 6 (source-overview, narrative-fidelity sentence): sentence fragment repaired

**Original:**
> Mostly complete narrative with some damage in the pursuit sequences and ending.

**Corrected:**
> The narrative is mostly complete, with some damage in the pursuit sequences and ending.

**Rationale:**
- Grammar: the original is a sentence fragment — a noun phrase ("Mostly complete narrative …") with no finite verb and no subject-predicate backbone. It looks like a template/notes-style carry-over that was never fully resolved into prose. The skill flags "Sentence fragments (unless clearly intentional for effect)" as a grammar defect; in this context it is clearly not an effect-driven fragment but a leftover from drafting.
- The fix supplies the missing subject and finite verb ("The narrative is") and adds a single comma to separate the main clause from the with-phrase. The fragment's semantic content is preserved: the narrative is mostly complete; the pursuit sequences and ending are where damage falls.
- No factual content added, removed, or altered: the claim about extent of preservation and the location of damage is identical; the footnote remains attached to the same text.

---

## Change 3 — Line 48: resolved the ambiguous em-dash / dangling-appositive structure

**Original:**
> Enlil is sentenced to leave Nippur and descend toward the _kur_ — the underworld — an exile that takes him progressively further from the civilised centre.

**Corrected:**
> Enlil is sentenced to leave Nippur and descend toward the _kur_, the underworld — an exile that takes him progressively further from the civilised centre.

**Rationale:**
- Readability / punctuation: the original sentence had two appositives in a row, each introduced or closed by an em-dash, with no connective between them. The first em-dash pair glosses "_kur_" as "the underworld"; the third em-dash then introduces "an exile that takes him …" as an appositive to the whole descending action. On first read the third em-dash can be misparsed as a second dash of a single pair running "_kur_ — the underworld — an exile", which would make "an exile" an apposition to "the underworld" (wrong: an exile is the act, not the place). The skill flags "Ambiguous sentence structure where the reader must re-read to parse correctly" and "Nested parenthetical asides: flatten".
- The fix converts the first em-dash pair into a comma-pair appositive for the gloss ("toward the _kur_, the underworld"), which is the standard punctuation for a short single-word gloss, and leaves the broader "— an exile that takes him…" appositive with its single em-dash, clearly attached to the whole preceding clause. The sentence now contains exactly one em-dash appositive rather than two stacked ones.
- No factual content added, removed, or altered: "_kur_" is still glossed as "the underworld"; the action is still described as an exile that takes Enlil progressively further from the civilised centre; the footnote remains attached to the same text.

---

## Items flagged but deliberately not changed

- **Line 42 — apparent article error inside a direct quote:** the Sumerian assembly's declaration is rendered as `"Enlil, you are a ritually impure."` The sequence "a ritually impure" reads as ungrammatical (indefinite article followed by adverb+adjective with no noun). Two reasons not to touch it at this stage: (a) it is presented as a direct-quotation rendering of the Sumerian line, so editing it risks silently altering a quotation that the fact-check stage validated against the source; (b) the fix could be either "a ritually impure one" (restoring an implied noun) or "ritually impure" (dropping "a"), and picking between them is not a mechanical call. Flagged for human / line-edit review rather than fixed here, per the skill's "No factual changes" rule and its instruction to "flag it for human review instead of fixing it" when a grammar fix would change meaning.
- **Line 61 and line 69 (marker-resolved gap markers) and line 71 (inference parenthetical):** the lowercase "none — no complete parallel fills this gap" on line 69, and the opening-lowercase "minor overlapping fragments help but gaps remain" on line 61, are inside `_[At this point the tablet breaks …]_` blocks. These are marker-resolved passages reviewed and locked at stage 13, so per the skill's hard rule "No content changes to resolved marker passages" they were not touched.
- **Line 36 — "The audience … were being taught":** British-English notional agreement with a collective noun ("audience") is acceptable and not a grammar defect.
- **Line 33 — "— \"he kissed her, he copulated with her\" —":** a single em-dash pair around a direct Sumerian quote inside a sentence that otherwise runs cleanly; not a nested parenthetical.
- **Line 23 and line 48 other em-dashes, line 85 trailing em-dash appositive, line 51 em-dash aside:** each of these sentences contains at most one em-dash pair; they are not nested and they parse unambiguously on a first read.

---

## Self-check

- No factual content changed. Every named deity, city, tablet reference, line number, epithet, manuscript count, quoted Sumerian phrase, and inference is preserved verbatim.
- Footnote count unchanged; all footnotes remain attached to the same text they originally annotated (on the split sentence the footnote stays on the second half, which is the attestation claim it was already marking).
- EVIDENCE tokens unchanged: same count, same order, same `source_id` and `loc` fields.
- COMPARATIVE-HOOK comments unchanged.
- AsciiDoc structure preserved: section heading (`==`), thematic breaks (`'''`), italic emphasis (`_kur_`, `_kur-gal_`, `_abzu_`, `_edubba_`, `_[...]_` gap markers, `_(...)_` inference parenthetical), footnote syntax, and EVIDENCE/COMPARATIVE-HOOK comment lines are all intact.
- Marker-resolved passages (the two `_[At this point the tablet breaks …]_` gap markers and the `_(The tripled disguise-encounter structure …)_` inference parenthetical) were left untouched per the skill's hard rules.
- Every change above is logged — no silent edits.
