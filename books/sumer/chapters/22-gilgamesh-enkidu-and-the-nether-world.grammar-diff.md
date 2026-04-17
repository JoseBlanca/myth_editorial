# Grammar-check diff: Chapter 22 — Gilgamesh, Enkidu, and the Nether World

Input: `22-gilgamesh-enkidu-and-the-nether-world.resolved.adoc`
Output: `22-gilgamesh-enkidu-and-the-nether-world.grammar-checked.adoc`

Changes logged below in "original → corrected" format with rationale. Changes restricted to grammar, punctuation, and readability (per stage 14b rules). No factual, stylistic, footnote-content, or AsciiDoc-structural changes.

---

## 1. Line 38 — sentence fragment (missing main verb)

**Original:**
> A throne: the instrument of authority. A bed: the instrument of union. The two objects that define Inanna's double sovereignty over political power and sexual force, and both of them will come from this tree, if the tree will grow.

**Corrected:**
> A throne: the instrument of authority. A bed: the instrument of union. These are the two objects that define Inanna's double sovereignty over political power and sexual force, and both of them will come from this tree, if the tree will grow.

**Rationale:** The third sentence, as written, is a fragment. "The two objects that define Inanna's double sovereignty over political power and sexual force" is a noun phrase consisting of a head ("The two objects") plus a restrictive relative clause ("that define…") with no main verb. The coordinating "and" then attaches a fully independent clause ("both of them will come from this tree…") to what was not itself a clause. Inserting "These are" supplies a subject and copula, turning the noun phrase into an independent clause ("These are the two objects that define…") and regularising the coordination with the second clause. Factual content preserved; referent ("these" = the throne and bed just named) is unambiguous; rhetorical cadence (two colon-gloss sentences followed by an explanatory third) preserved.

---

## 2. Line 50 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(The huluppu-tree episode encodes Inanna's dependence on male heroic action (Gilgamesh) to realise her aspirations (the throne and bed), while simultaneously providing the origin of the objects whose loss drives the second half of the narrative..footnote:[Inference: The text shows Inanna unable to use the tree until Gilgamesh intervenes.. Risk: This is one modern scholarly reading; the text does not make this gendered interpretation explicit..])_footnote:[ETCSL 1.8.1.4, lines 20–100.]

**Corrected:**
> _(The huluppu-tree episode encodes Inanna's dependence on male heroic action (Gilgamesh) to realise her aspirations (the throne and bed), while simultaneously providing the origin of the objects whose loss drives the second half of the narrative.footnote:[Inference: The text shows Inanna unable to use the tree until Gilgamesh intervenes.. Risk: This is one modern scholarly reading; the text does not make this gendered interpretation explicit..])_footnote:[ETCSL 1.8.1.4, lines 20–100.]

**Rationale:** Doubled sentence-terminating period (`narrative..`) immediately before the `footnote:[...]` macro reduced to a single period. Same class of marker-resolve punctuation artefact fixed in chapter 19 grammar-diff #2, chapter 20 grammar-diff #3, and chapter 21 grammar-diff #5/#6. The double periods *inside* the footnote interior (`intervenes..`, `explicit..`) are left untouched per hard rule 2 (no footnote changes).

---

## 3. Line 56 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(The exact identification of the pukku and mekku is uncertain. Proposals include a ball and mallet used in a game, a drum and drumstick, or ritual objects of unknown function..footnote:[Inference: Scholarly reviews of the evidence find no definitive identification.. Risk: The identification remains one of the most debated questions in Sumerian philology; any specific rendering is provisional..])_

**Corrected:**
> _(The exact identification of the pukku and mekku is uncertain. Proposals include a ball and mallet used in a game, a drum and drumstick, or ritual objects of unknown function.footnote:[Inference: Scholarly reviews of the evidence find no definitive identification.. Risk: The identification remains one of the most debated questions in Sumerian philology; any specific rendering is provisional..])_

**Rationale:** Same class of error as change 2. Doubled sentence-terminating period (`function..`) before the `footnote:[...]` macro reduced to one. Double periods *inside* this footnote's interior (`identification..`, `provisional..`) left untouched per hard rule 2.

---

## 4. Line 80 — double periods inside italic editorial bracket note (damage summary)

**Original:**
> _[At this point the tablet breaks. Portions of Enkidu's taboo-breaking instructions and descent sequence (approximately lines 150–175) are partially damaged.. Numerous OB tablets overlap and allow reconstruction of most gaps; the taboo catalogue is substantially secure..]_

**Corrected:**
> _[At this point the tablet breaks. Portions of Enkidu's taboo-breaking instructions and descent sequence (approximately lines 150–175) are partially damaged. Numerous OB tablets overlap and allow reconstruction of most gaps; the taboo catalogue is substantially secure.]_

**Rationale:** Two doubled-period typos (`damaged..` and `secure..`) reduced to single periods. The bracketed block is an editorial damage note in running italic prose (not a `footnote:[]` macro), so routine punctuation correction applies. Consistent with chapter 19 grammar-diff #3, chapter 20 grammar-diff #1, and chapter 21 grammar-diff #3/#4. No content change.

---

## 5. Line 97 — missing comma before non-restrictive appositive

**Original:**
> Gilgamesh then approaches Enki in Eridu, the oldest city in Sumerian tradition, seat of Enki's temple the E-abzu.

**Corrected:**
> Gilgamesh then approaches Enki in Eridu, the oldest city in Sumerian tradition, seat of Enki's temple, the E-abzu.

**Rationale:** "The E-abzu" is a non-restrictive appositive naming the single, unambiguous temple already referred to ("Enki's temple" — there is only one E-abzu in Eridu). Non-restrictive appositives must be set off with a comma. Without the comma, the reader briefly parses "Enki's temple the E-abzu" as if "the E-abzu" were a restrictive modifier (as though distinguishing among several temples of Enki), which reverses the intended grammatical relationship. The added comma also completes the parallel three-element appositive chain for "Eridu" (oldest city / seat of Enki's temple / the E-abzu). No lexical or factual change.

---

## 6. Line 121 — double periods inside italic editorial bracket note (damage summary)

**Original:**
> _[At this point the tablet breaks. Parts of Enkidu's ghost's report on afterlife conditions (approximately lines 240–270) are fragmentary in some witnesses.. Partial; manuscript overlap covers most but not all of the catalogue of the dead; some conditions described for specific categories of the dead remain uncertain..]_

**Corrected:**
> _[At this point the tablet breaks. Parts of Enkidu's ghost's report on afterlife conditions (approximately lines 240–270) are fragmentary in some witnesses. Partial; manuscript overlap covers most but not all of the catalogue of the dead; some conditions described for specific categories of the dead remain uncertain.]_

**Rationale:** Same class of error as change 4. Two doubled-period typos (`witnesses..` and `uncertain..`) reduced to single periods. Editorial bracket note in running prose, not a `footnote:[]` macro. No content change.

---

## 7. Line 140 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(The absence of moral judgement in the nether-world catalogue — fates depend on biography, not ethics — represents a fundamentally different eschatological logic from traditions that organise the afterlife by moral desert..footnote:[Inference: The catalogue sorts the dead by manner of death, social status, and number of children, with no mention of virtuous or sinful conduct.. Risk: The text may be incomplete or selective; absence of evidence for moral judgement is not evidence of its absence in the broader tradition..])_

**Corrected:**
> _(The absence of moral judgement in the nether-world catalogue — fates depend on biography, not ethics — represents a fundamentally different eschatological logic from traditions that organise the afterlife by moral desert.footnote:[Inference: The catalogue sorts the dead by manner of death, social status, and number of children, with no mention of virtuous or sinful conduct.. Risk: The text may be incomplete or selective; absence of evidence for moral judgement is not evidence of its absence in the broader tradition..])_

**Rationale:** Same class of error as changes 2 and 3. Doubled sentence-terminating period (`desert..`) before the `footnote:[...]` macro reduced to one. Double periods *inside* this footnote's interior (`conduct..`, `tradition..`) left untouched per hard rule 2.

---

## Sentences reviewed for length/complexity but NOT changed

The following long or clause-heavy sentences were evaluated against the >50-word / 3+-subordinate-clause / nested-parenthetical tests and judged clear enough (or stylistically essential enough) to retain as written. Logged here so the human can spot-check:

- Line 3 (opening paragraph, sentence 2): "It is one of the most widely attested Sumerian Gilgamesh poems — approximately 303 lines in the ETCSL composite, with Gadotti's 2014 critical edition drawing on seventy-four manuscripts to produce a text of some 330 lines." (~38 words; single dash-offset elaboration, clear).
- Line 7: "This is a composite-editorial text: the ETCSL composite draws on numerous Old Babylonian tablets to produce the standard scholarly text, and the continuous narrative that results is a modern editorial achievement, not something any ancient scribe held in his hands." (~40 words; colon-introduced explanation, two independent clauses joined by "and", parallel structure clear).
- Line 20: "The primordial separation: An carried off heaven, Enlil — king of the gods, lord of wind and command — carried off earth, and the _kur_ — the nether world, realm of the dead beneath the earth — was given to Ereshkigal — queen of the underworld — as a prize." (~50 words; three sequential (not nested) dash-offset appositives, each gloss short, parallel tricolon "An carried off X, Enlil carried off Y, the _kur_ was given to Z", parses on first reading).
- Line 26: "The cosmogonic prologue should be treated as integral to the composition, not as a later scribal addition, because it establishes the cosmological framework — the existence and nature of the _kur_ — that the entire subsequent narrative depends on." (~42 words; single dash-offset gloss, causal "because"-clause, clear).
- Line 29: "Then comes a passage whose full meaning is lost. Enki — god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath Eridu — sets sail for the _kur_, and the sea attacks his boat." (~37 words; single dash-offset gloss, compound predicate, clear).
- Line 38 (after change 1): "She transplants the huluppu tree to her holy garden in Uruk — the great walled city of southern Mesopotamia — intending to fashion from it a throne and a bed when it has grown to maturity." (~36 words; single dash-offset gloss plus participial tail, clear).
- Line 42: "Root, crown, and trunk: the three zones of the tree are occupied, each by a creature that refuses to yield — a vertical cosmology in miniature, echoing the tripartite division of the cosmos that opened the composition." (~37 words; colon-introduced elaboration, dash-offset summary, two subordinate clauses but each short, clear).
- Line 47: "He kills the serpent at the roots, causing the Anzud bird to flee with its young to the mountains and the phantom maid to flee to the wilderness." (~28 words; single participial consequence clause with parallel infinitival pair, clear).
- Line 53: "What the text makes clear is that these objects matter — they are made from the sacred tree, they are Gilgamesh's personal possessions, and they will drive everything that follows." (~30 words; dash-offset tricolon elaborating "matter", clear).
- Line 60: "Whether the oppression involves forced labour, compulsory participation in a game, or some form of ritualized dominance, the citizens cry out." (~21 words; concessive "whether"-triplet plus main clause, clear).
- Line 63: "The narrative logic is clear: Gilgamesh abused the objects, and they are gone — fallen into the _kur_, the same nether world that was created at the beginning of the composition, the same realm assigned to Ereshkigal when the cosmos was young." (~43 words; colon-introduced explanation, dash-offset participial tail with symmetric "the same X that… the same Y assigned…" parallel, clear).
- Line 66: "A hero who killed a serpent and felled a sacred tree and fashioned ritual objects from its wood cannot reach down past the threshold of the dead and take back what has fallen there." (~34 words; single three-part subject relative clause joined by polysyndetic "and… and… and", intentional rhythmic build, parses on first reading).
- Line 74 (sentence beginning "Clean clothes, fragrant oil…"): "Clean clothes, fragrant oil, sandals, the sounds of daily life, the touch of family — these are the signatures of a person who belongs above, who eats, who loves, who moves through the world as someone with a body and a place." (~42 words; opening enumerated series resolved by dash + "these are", trailing four parallel "who"-clauses are deliberate anaphora, each sub-clause well under 10 words, rhetorically essential).
- Line 74 (final sentence): "To do any of these things in the nether world is to declare yourself alive, and to declare yourself alive among the dead is to be seized by the dead and made one of them." (~36 words; two parallel "to do X is to Y" copular clauses joined by "and", chiasmus preserved, clear).
- Line 94: "Enlil's refusal is a structural constant in Sumerian narrative — the king of the gods maintains cosmic order, and cosmic order includes the finality of the nether world." (~28 words; dash-offset gloss, clear).
- Line 116: "What follows is the most significant section of the composition and the most detailed Sumerian eschatological text that survives: an extended catalogue of the dead, a systematic report on the fates of the deceased organised by manner of death, number of children, and social status." (~44 words; colon-introduced two-part appositive elaboration with serial comma list, clear).
- Line 134 (final sentence): "The system it describes operates on a different logic entirely: the logic of biographical fact, of measurable conditions, of the specific circumstances under which a person entered the nether world." (~31 words; colon-introduced triplet of parallel "of…" phrases, clear).
- Line 147: "The dead are sorted by the facts of their deaths — how many children they had, whether they were buried, whether they died in battle or by fire or by neglect — and these facts determine their condition below with the impersonal efficiency of an administrative system." (~47 words; symmetric dash-offset triplet of parallel factual criteria ("how many…, whether…, whether…"), followed by one main-clause tail, clear).
- Line 154: "The last word belongs not to the hero but to the system — the nether world and its classifications, ancient and immutable, operating long before Gilgamesh was born and certain to operate long after he is gone." (~37 words; single dash-offset elaboration with symmetric before/after tail, clear).
- Line 156 (sentence beginning "Without the cosmogonic prologue…"): "Without the huluppu tree, there would be no pukku and mekku, and without the pukku and mekku, there would be no loss, and without the loss, there would be no descent, and without the descent, there would be no ghost at the aperture between worlds, delivering the only eyewitness report the Sumerian tradition possesses of what it is like to be dead." (~72 words; five-step cumulative anadiplosis ("no X… without X, no Y… without Y, no Z…"), rhetorical crescendo is the whole point of the sentence; splitting would collapse the chained inference that drives the paragraph's summary; retained by design under the "length essential for meaning" clause).
- Line 158: "They copied it, and they copied it again, and they kept copying it, because the question it answers is the one that does not go away: what happens when you die, and does it matter how you lived?" (~41 words; three-step polysyndetic repetition + causal clause + colon-introduced double question, rhythmic build deliberate, clear).
- Line 158 (next sentence): "The Sumerian answer, delivered by a ghost to a grieving king through a hole in the ground opened by the sun, is this: it matters, but not in the way you think." (~34 words; single participial middle modifying "answer", colon-introduced pithy resolution, clear).

After the changes above, no remaining sentence exceeds the 50-word threshold except line 156 (retained by design as a rhetorical crescendo central to the chapter's closing argument). No remaining nested parentheticals. No subject-verb, tense, or article errors identified.

---

## Items deliberately NOT fixed (per hard rules)

- Double periods *inside* `footnote:[...]` interiors on lines 50, 56, and 140 (e.g., `intervenes..`, `explicit..`, `identification..`, `provisional..`, `conduct..`, `tradition..`) — hard rule 2 forbids footnote changes.
- Sentence fragments used intentionally for rhetorical emphasis and retained:
  - Line 3: "Seventy-four manuscripts." (deliberate punch-sentence after the cited number).
  - Line 24: "Heaven above. Earth in the middle. The nether world below." (parallel fragments cataloguing the tripartite cosmos).
  - Line 29: "A primordial conflict, a journey by the god of wisdom toward the nether world, an ocean that fights back — a reference to a tradition whose full context is lost to us." (asyndetic noun-phrase series resolving with a dash-offset appositive; stylistic).
  - Line 123: "Not on moral conduct. Not on piety. Not on virtue or sin. On biography — on the specific, countable facts of how you lived and how you died." (anaphora marking the argumentative pivot).
  - Line 156: "Three narratives, then, woven into one composition. The separation of the cosmos. A sacred tree and the objects fashioned from it. A descent, a loss, a ghost, and a catalogue of the dead." (summary-list fragments recapping the composition's three sections).
- Inconsistency in catalogue-entry syntax at line 125: "He who had one son: he weeps bitterly…" (topic-comment colon) vs. "He who had seven sons sits on a throne…" (direct subject-verb) — rhythmic/stylistic variation at the climax of the series. Deferred to line-edit (stage 15).
- Second-person "you" in the generic sense ("if you do what the living do, you are identified and seized" at line 77; "what happens when you die, and does it matter how you lived" at line 158; the "Were you buried? How did you die?" at line 134; "how many sons you had… whether you were buried… how you died… whether you were good" at line 158) — a consistent register choice across the chapter addressing the reader directly; not a pronoun-reference error. Register/voice is line-edit's scope.
- Word choice (e.g., "moralize" and "ritualized" at lines 60 and 134, which use the -ize ending in a chapter whose surrounding text uses British "-ise" spellings for "realise", "organised", "characterised"; the -ize/-ise variation is tolerated by many British style guides and is consistent with the verb-level mix already established across earlier chapters of this book — see e.g. chapter 14 "moralize"). Deferred to line-edit.
- Register and paragraph transitions across the chapter: deferred to line-edit (stage 15).
- Stray leading period at start of any `_(...)_` italic-paren block: none in this chapter (the line-77 artefact flagged in chapter 21 does not recur here).

---

## Self-check

1. **Factual content**: unchanged. No claim about texts, dates, people, places, deities, manuscript counts (e.g., the "seventy-four manuscripts", the "approximately 303 lines", Gadotti 2014, the ETCSL catalogue number 1.8.1.4), or events was altered.
2. **Footnote count**: unchanged (34 `footnote:[...]` macros in input; 34 in output; interior text preserved verbatim).
3. **EVIDENCE tokens**: unchanged (37 `// EVIDENCE:` comments in input; 37 in output; identical).
4. **AsciiDoc structure**: unchanged (the single `== Gilgamesh, Enkidu, and the Nether World` chapter heading, all six `'''` section-break markers, all four `// COMPARATIVE-HOOK:` comments, italic markup `_..._`, em-dashes `—` all preserved; line count is 160 in both input and output).
5. Every change is logged above. No silent changes.
