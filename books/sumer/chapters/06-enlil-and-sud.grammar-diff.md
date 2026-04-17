# Grammar-check diff — Chapter 06: Enlil and Sud

Input: `chapters/06-enlil-and-sud.resolved.adoc`
Output: `chapters/06-enlil-and-sud.grammar-checked.adoc`

Each entry: the changed original passage, the corrected version, and the rationale. No factual content, footnotes, EVIDENCE tokens, AsciiDoc markup, COMPARATIVE-HOOK comments, or marker-resolved passages (the `_[At this point the tablet breaks …]_` gap marker and the two `_(Inference …)_` parentheticals) were altered. Stylistic matters (word choice, rhythm, nominalisations, paragraph transitions) were left for the line-edit stage.

---

## Change 1 — Line 3 (source-overview, narrative-fidelity sentence): sentence fragment repaired

**Original:**
> Generally well-preserved.

**Corrected:**
> The composition is generally well-preserved.

**Rationale:**
- Grammar: the original is a bare sentence fragment — an adverb + past-participial adjective with no subject and no finite verb. It reads as a template/notes-style carry-over from the source-overview marker resolution that was not fully rendered into prose. The skill flags "Sentence fragments (unless clearly intentional for effect)" as a grammar defect; in this opening expository paragraph, no rhetorical-fragment effect is in play, so the fragment is simply ungrammatical.
- The fix supplies the missing subject and finite verb ("The composition is") so that the sentence becomes a complete independent clause. The semantic content is preserved verbatim: the claim is still "(the composition is) generally well-preserved", attached to the same footnote.
- Parallels chapter 05's grammar-check fix of the analogous fragment "Mostly complete narrative with some damage in the pursuit sequences and ending." → "The narrative is mostly complete, with some damage in the pursuit sequences and ending." (chapter 05 grammar-diff, Change 2).
- No factual content added, removed, or altered: the preservation claim is identical; the footnote `ETCSL 1.2.2, composite text.` and the following EVIDENCE token remain attached to the same sentence.

---

## Items flagged but deliberately not changed

- **Line 3 — duplicated claim "catalogued as ETCSL 1.2.2":** the first and second sentences of the source-overview paragraph both state that the text is catalogued as ETCSL 1.2.2. This is a redundancy, not a grammar defect. Removing one instance would be a content/editorial decision rather than a mechanical grammar fix (it would delete a footnoted attestation claim), and the skill's hard rule "No factual changes" — including "if a grammar fix would change the meaning of a sentence, flag it for human review instead of fixing it" — argues for flagging over editing. Left for human / line-edit review.
- **Line 17 — fronted-participle construction before em-dash:** "The king of the gods, encountering a young goddess, making a direct sexual advance -- the pattern is identical to the canal scene in "Enlil and Ninlil."" The first noun phrase + two participial modifiers + em-dash + main clause is an unusual but deliberate rhetorical fronting, mirroring the preceding paragraph's anaphoric list ("no preamble, no negotiation, no intermediary"). It parses cleanly on a first read and is a style choice, not a grammar error.
- **Line 80 — "formalized" vs. British spelling elsewhere ("behaviour" line 22, "jewellery" line 44, "modelling" line 46):** the text uses British spelling throughout but slips to the American form "formalized" here. Spelling-variant normalisation is word-choice territory (the skill's "What NOT to fix" list names "Word choice" first) and not a grammar defect; each spelling is itself correct. Flagged for line-edit review rather than silently normalised.
- **Line 88 — "organization" and line 90 — "honored":** same class as the item above — American spellings appearing in a text that otherwise uses British forms. Grammatically correct as written; flagged for line-edit consistency pass, not fixed here.
- **Line 86 — footnote prose ("The prevalent version is chosen here because Standard composite; …"):** the "because Standard composite" clause is ungrammatical (missing subject and verb after "because"), but the skill's hard rule "No footnote changes" forbids modifying footnote content at this stage. Flagged for the human / fact-check review of the `source_notes.md` that this footnote was generated from.
- **Line 32 — the `_[At this point the tablet breaks …]_` gap marker** and **lines 50 and 74 — the two `_(Inference: …)_` parentheticals:** these are marker-resolved passages that were reviewed and locked at stage 13. The skill's hard rule "No content changes to resolved marker passages" forbids modification at the grammar-check stage. The lowercase "none -- single manuscript tradition" inside the gap marker on line 32 was therefore left untouched.
- **Line 34 — "presides over the _edubba_ — the scribal school where these texts were copied and taught — and over every act":** a single em-dash pair glossing _edubba_, followed by a coordinated "and over …" that continues the main clause's preposition. Not a nested parenthetical; parses unambiguously on first read.
- **Line 88 — 36-word "Formal divine courtship …" sentence and 33-word "And the divine renaming …" sentence:** each is under the skill's 50-word threshold. They carry em-dash appositives but no nested parentheticals, and no chain of three-plus subordinate clauses. Left alone.

---

## Self-check

- No factual content changed. Every named deity (Enlil, Sud, Nisaba, Nusku, Ninlil; Shiva, Parvati; Abram/Abraham, Jacob/Israel), city (Eresh, Nippur, Shuruppag), institution (_edubba_, E-kur), tablet/line reference (ETCSL 1.2.2, lines 1–170 et al.), bibliographic citation (Black et al. 2004 pp. 106–115; Jacobsen 1987 pp. 167–168), and inference is preserved verbatim.
- Footnote count unchanged: every `footnote:[...]` in the input appears at the same attachment point in the output, with identical text. The single prose edit (fragment → complete sentence on line 3) keeps its footnote attached to the word "well-preserved" as in the original.
- EVIDENCE tokens unchanged: same count, same order, same `source_id` and `loc` fields, same line-association.
- COMPARATIVE-HOOK comments unchanged (three lines at end of file).
- AsciiDoc structure preserved: the `==` section heading, the five `'''` thematic breaks, italic emphasis (`_edubba_`, `_[...]_` gap marker, `_(...)_` inference parentheticals), footnote syntax, and comment lines (EVIDENCE, COMPARATIVE-HOOK) are all intact.
- Marker-resolved passages (the `_[At this point the tablet breaks …]_` block on line 32 and the two `_(Inference: …)_` parentheticals on lines 50 and 74) were left untouched per the skill's hard rule 4.
- Every change to the output file is logged in "Change 1" above — no silent edits. All other candidate items are enumerated in the "Items flagged but deliberately not changed" section.
