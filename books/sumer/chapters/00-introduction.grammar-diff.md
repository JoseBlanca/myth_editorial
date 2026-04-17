# Grammar-check diff: 00-introduction

Stage: 14b grammar-check
Input: `chapters/00-introduction.resolved.adoc`
Output: `chapters/00-introduction.grammar-checked.adoc`

## Changes applied

### Change 1 — Line 54 (Enlil and Sud paragraph, closing sentence)

**Issue**: Sentence exceeds 50 words (~59 words) and carries three subordinate structures in sequence (participial phrase "establishing a narrative continuity"; colon-introduced elaboration; concessive "though" clause). Splitting relieves the pile-up without altering meaning.

**Original**:
> Notably, the text ends with the renaming of Sud as Ninlil, establishing a narrative continuity between the two Enlil cycle compositions: the courtship and renaming in Enlil and Sud precede the more violent events of Enlil and Ninlil in the mythological sequence, though the two compositions circulated independently and were not read as sequential chapters of a single story.

**Corrected**:
> Notably, the text ends with the renaming of Sud as Ninlil, establishing a narrative continuity between the two Enlil cycle compositions: the courtship and renaming in Enlil and Sud precede the more violent events of Enlil and Ninlil in the mythological sequence. The two compositions, though, circulated independently and were not read as sequential chapters of a single story.

**Rationale**: Split at the concessive "though" to create two sentences. "Though" retained as a mid-sentence adverb in the new second sentence, preserving the concessive relation. No facts changed: the renaming still creates narrative continuity, the mythological sequence is unchanged, and the two compositions still circulated independently.

---

### Change 2 — Line 64 (Lugal-e paragraph, Chaoskampf comparative sentence)

**Issue**: Sentence exceeds 50 words (~52 words) and stacks an em-dash parenthetical apposition with a three-item prepositional series followed by a "where" relative clause — four layered structures in one sentence. The trailing "where" clause attaches only to the Vedic item but its length makes the attachment momentarily ambiguous on first reading.

**Original**:
> The Chaoskampf pattern it exemplifies -- a young warrior god defeating a chaos monster to organise the cosmos -- reappears in the later Babylonian Enuma Elish (Marduk versus Tiamat), in the Greek Zeus-Typhon conflict, and in the Vedic Indra-Vrtra combat, where the warrior god slays a serpentine demon blocking the waters.

**Corrected**:
> The Chaoskampf pattern it exemplifies -- a young warrior god defeating a chaos monster to organise the cosmos -- reappears in the later Babylonian Enuma Elish (Marduk versus Tiamat), in the Greek Zeus-Typhon conflict, and in the Vedic Indra-Vrtra combat. In the Vedic version, the warrior god slays a serpentine demon blocking the waters.

**Rationale**: Split off the "where" clause into a separate sentence keyed explicitly to the Vedic version. The attachment is now unambiguous and no factual claim is changed (the Vedic warrior god, the serpent, and the blocked waters all remain).

---

### Change 3 — Line 123 (Marriage of Martu paragraph, ethnographic catalogue sentence)

**Issue**: Sentence exceeds 50 words (~60 words) and welds two independent main clauses joined by "and" across a long em-dash list, producing a run-on feel. Splitting at the "-- and" junction restores clarity.

**Original**:
> The ethnographic catalogue of Amorite deficiencies is one of the liveliest passages in Sumerian literature -- the Amorites "know no grain," they "eat raw meat," they "have no houses in their lifetime," and "are not brought to burial when they die" -- and the bride's decision to marry Martu despite all this is presented without irony as an act of divine love.

**Corrected**:
> The ethnographic catalogue of Amorite deficiencies is one of the liveliest passages in Sumerian literature -- the Amorites "know no grain," they "eat raw meat," they "have no houses in their lifetime," and "are not brought to burial when they die." The bride's decision to marry Martu despite all this is presented without irony as an act of divine love.

**Rationale**: Replaced the closing em-dash and "and" with a full stop, preserving both halves verbatim. The list of Amorite deficiencies is still a dash-set aside of the first sentence; the bride's decision now stands as its own complete statement. No factual content changed.

---

### Change 4 — Line 143 (Gilgamesh, Enkidu, and the Nether World paragraph, main narrative sentence)

**Issue**: Nested parenthetical aside — an em-dash parenthetical ("a tree of uncertain species, sacred to Inanna") sits inside a round-bracketed parenthetical ("the _pukku_ and _mekku_, possibly a drum and drumstick, fashioned from the _huluppu_ tree ..."). The readability rule says flatten nested parentheticals. Flatten by replacing the inner em-dash with a comma so the _huluppu_ description becomes an ordinary in-parenthesis appositive at a single level of nesting.

**Original**:
> The main narrative tells how Gilgamesh's ritual objects (the _pukku_ and _mekku_, possibly a drum and drumstick, fashioned from the _huluppu_ tree -- a tree of uncertain species, sacred to Inanna) fall into the underworld.

**Corrected**:
> The main narrative tells how Gilgamesh's ritual objects (the _pukku_ and _mekku_, possibly a drum and drumstick, fashioned from the _huluppu_ tree, a tree of uncertain species sacred to Inanna) fall into the underworld.

**Rationale**: Replaced " -- a tree of uncertain species, sacred to Inanna" with ", a tree of uncertain species sacred to Inanna". Dropping the internal comma before "sacred" turns "sacred to Inanna" into a bound restrictive modifier of "species", which keeps the single appositive short and prevents the reader from parsing two independent asides (species-uncertainty, Inanna-sacredness). All facts preserved: _huluppu_ tree species uncertain, sacred to Inanna.

---

### Change 5 — Line 164 (Lugalbanda pair, second-composition sentence)

**Issue**: Sentence exceeds 50 words (~60 words) and carries three subordinate constructions (em-dash apposition for the Anzud bird; participial phrase "by caring tenderly ..."; inner parenthesis listing the three acts of care; final relative clause "who grants him ..."). Splitting after the em-dash clause relieves the load.

**Original**:
> In the second composition, he encounters the nest of the Anzud bird -- a divine lion-headed eagle of terrifying size -- and by caring tenderly for its chick (feeding it, anointing it with oil, adorning it with a crown of vegetation) earns the gratitude of the returning parent bird, who grants him the gift of supernatural speed.

**Corrected**:
> In the second composition, he encounters the nest of the Anzud bird -- a divine lion-headed eagle of terrifying size. By caring tenderly for its chick (feeding it, anointing it with oil, adorning it with a crown of vegetation), he earns the gratitude of the returning parent bird, who grants him the gift of supernatural speed.

**Rationale**: Split at " -- and by caring tenderly" so the Anzud bird description closes one sentence and the reciprocity sequence becomes its own sentence with explicit subject "he". No facts changed: Lugalbanda still cares for the chick with the three listed acts, still earns gratitude, still receives supernatural speed.

---

### Change 6 — Line 175 (Eridu Genesis paragraph, "What survives" sentence)

**Issue**: Sentence reaches ~50 words and ends with a relative clause that itself contains two conjoined predicates ("who builds ... and is afterwards granted ..."), with a parenthetical tucked inside the first predicate. The list-then-relative-clause structure makes the reader shift gears midway. Splitting at the relative pronoun keeps the list clean and gives Ziusudra's actions their own sentence.

**Original**:
> What survives describes the creation of humans, the establishment of cities and kingship, a divine decision to destroy humanity by flood, and the survival of the pious king Ziusudra, who builds a boat at Enki's secret instruction (communicated through a reed wall) and is afterwards granted immortality in Dilmun.

**Corrected**:
> What survives describes the creation of humans, the establishment of cities and kingship, a divine decision to destroy humanity by flood, and the survival of the pious king Ziusudra. Ziusudra builds a boat at Enki's secret instruction (communicated through a reed wall) and is afterwards granted immortality in Dilmun.

**Rationale**: Converted the relative clause into a new sentence with Ziusudra as explicit subject. All facts preserved: Ziusudra builds the boat, the instruction comes secretly from Enki through a reed wall, and he is granted immortality in Dilmun.

---

### Change 7 — Line 176 (Eridu Genesis paragraph, parallels sentence)

**Issue**: Sentence exceeds 50 words (~55 words) and joins two claims with "and" after a colon: first that the text is the sole Sumerian flood narrative, second that its parallels to Akkadian and biblical floods are the most-discussed cross-cultural resonance. Each deserves its own sentence; the second is weighed down by two parentheticals listing the parallel texts.

**Original**:
> Despite its ruinous state, this is a central text: it is the sole Sumerian flood narrative, and its parallels to the Akkadian traditions (Utnapishtim in Gilgamesh Tablet XI, the Atrahasis epic) and to the biblical flood of Noah (Genesis 6-9) are the most direct and widely discussed cross-cultural resonance in the entire Mesopotamian literary corpus.

**Corrected**:
> Despite its ruinous state, this is a central text: it is the sole Sumerian flood narrative. Its parallels to the Akkadian traditions (Utnapishtim in Gilgamesh Tablet XI, the Atrahasis epic) and to the biblical flood of Noah (Genesis 6-9) are the most direct and widely discussed cross-cultural resonance in the entire Mesopotamian literary corpus.

**Rationale**: Split at "and its parallels". The colon-introduced claim about the Eridu Genesis being the sole Sumerian flood narrative now ends cleanly; the second clause about parallels begins with "Its parallels", keeping referential clarity. All factual content preserved (Utnapishtim/Atrahasis/Noah parallels, central-text status).

---

### Change 8 — Line 191 (Debate Poems section, opening)

**Issue**: AsciiDoc structure bug. Two sentences sat on a single physical line after the EVIDENCE line-comment ("// EVIDENCE: source_id=black-2004 ; loc=pp. 207-209 Two personified entities -- a pair of animals ..."). Because `//` in AsciiDoc starts a comment that runs to the end of the line, the "Two personified entities ..." sentence would be consumed by the comment and silently dropped at render time. Inserting a newline after the EVIDENCE comment restores the intended AsciiDoc structure so the sentence renders.

**Original** (single physical line):
> The Sumerian debate poems are a genre with few close parallels in later Western literature, though medieval European debate poetry -- such as _The Owl and the Nightingale_ -- offers a distant echo.footnote:[Black et al. 2004, pp. 207-209.] // EVIDENCE: source_id=black-2004 ; loc=pp. 207-209 Two personified entities -- a pair of animals, plants, tools, metals, or seasons -- argue their respective merits before a divine judge, who delivers a verdict. They are products of the _edubba_ and represent the scribal school's intellectual culture at its most playful and systematic.

**Corrected** (newline inserted before "Two personified entities"):
> The Sumerian debate poems are a genre with few close parallels in later Western literature, though medieval European debate poetry -- such as _The Owl and the Nightingale_ -- offers a distant echo.footnote:[Black et al. 2004, pp. 207-209.] // EVIDENCE: source_id=black-2004 ; loc=pp. 207-209
> Two personified entities -- a pair of animals, plants, tools, metals, or seasons -- argue their respective merits before a divine judge, who delivers a verdict. They are products of the _edubba_ and represent the scribal school's intellectual culture at its most playful and systematic.

**Rationale**: Purely structural AsciiDoc fix. No text was added, removed, or reworded — only a newline was inserted so the `//` line-comment terminates before the next sentence. This matches the pattern used throughout the rest of the chapter, where every EVIDENCE comment ends a physical line.

---

## Issues noted but NOT fixed (per "What NOT to fix" and marker-preservation rules)

### Flag 1 — Line 71 (Ninurta and the Turtle paragraph, closing parenthetical)

**Text**: `_(The text appears to function as a deliberate deflation of the heroic mode, suggesting that even within the Sumerian tradition the Chaoskampf was not treated with unmixed reverence..footnote:[Inference: . Risk: .])_`

**Issue**: Double full stop before `footnote:` ("reverence..footnote:"); empty `Inference:` and `Risk:` slots inside the footnote. This is a resolved inference-marker artefact. Per rule 4 (no content changes to resolved marker passages) and rule 2 (no footnote changes), left as-is.

### Flag 2 — Line 89 (Inanna and Gudam paragraph)

**Text**: `_[At this point the tablet breaks. The text is too fragmentary for its precise cultural function to be determined with confidence..]_`

**Issue**: Double full stop before the closing bracket ("confidence..]"). This is a marker-resolved tablet-break notice; left as-is per rule 4.

### Flag 3 — Line 110 (Inanna and Bilulu paragraph)

**Text**: `_[At this point the tablet breaks. The fragmentary state prevents confident reconstruction of the full narrative logic..]_`

**Issue**: Double full stop before the closing bracket. Marker-resolved tablet-break notice; left as-is.

### Flag 4 — Line 117 (Nanna-Suen's Journey paragraph, closing parenthetical)

**Text**: `_(The composition may have functioned as a ritual text performed in connection with actual tribute deliveries or ceremonial journeys between the two cities, lending mythological prestige to what was, at its core, an economic transaction..footnote:[Inference: . Risk: .])_`

**Issue**: Double full stop before `footnote:`; empty Inference/Risk slots. Marker-resolved inference; left as-is.

### Flag 5 — Line 124 (Marriage of Martu paragraph, closing parenthetical)

**Text**: `_(The text likely dates from a period of active Amorite integration into Mesopotamian urban society, encoding anxieties about cultural absorption through a narrative that resolves them in divine favour. By the end of the Old Babylonian period, Amorite dynasties ruled most of Mesopotamia; this text may reflect an earlier moment when such an outcome seemed less inevitable and more troubling..footnote:[Inference: . Risk: .])_`

**Issue**: Double full stop before `footnote:`; empty Inference/Risk slots. Marker-resolved inference; left as-is.

### Flag 6 — Line 136 (Gilgamesh and the Bull of Heaven paragraph)

**Text**: `_[At this point the tablet breaks. Much of the narrative is lost; the composition's precise textual form cannot be fully reconstructed from surviving tablets..]_`

**Issue**: Double full stop before the closing bracket. Marker-resolved tablet-break notice; left as-is.

### Flag 7 — Line 145 (Gilgamesh, Enkidu, and the Nether World paragraph)

**Text**: `_(.footnote:[Inference: . Risk: .])_`

**Issue**: Entirely empty inference parenthetical — the sentence content slot and both footnote slots are empty. This is an unresolved marker artefact inside a parenthetical that renders as essentially nothing. Per rule 4 (no changes to resolved marker passages) and rule 2 (no footnote changes), and because removing it would be a content change rather than a grammar fix, left as-is. Recommend human review.

### Flag 8 — Line 149 (Death of Gilgamesh paragraph)

**Text**: `_[At this point the tablet breaks. The Nippur manuscripts alone are insufficient for a complete text; the Tell Haddad material fills substantial gaps but the ending remains damaged..]_`

**Issue**: Double full stop before the closing bracket. Marker-resolved tablet-break notice; left as-is.

### Flag 9 — Line 181 (Ningishzida's Journey paragraph)

**Text**: `_[At this point the tablet breaks. Too little text survives for a confident assessment of the composition's function or narrative structure..]_`

**Issue**: Double full stop before the closing bracket. Marker-resolved tablet-break notice; left as-is.

### Flag 10 — Line 206 (Copper and Silver / Date Palm and Tamarisk paragraph)

**Text**: `_[At this point the tablet breaks. Neither composition can be fully analysed without substantial missing text..]_`

**Issue**: Double full stop before the closing bracket. Marker-resolved tablet-break notice; left as-is.

### Flag 11 — Line 225 (Closing analysis paragraph)

**Text**: `_(The convergence of these four concerns -- order, death, power, and knowledge -- in a corpus produced by and for a professional scribal class suggests that Sumerian literary mythology functioned less as popular religion and more as an intellectual curriculum for the administrative elite, a way of training young bureaucrats and priests to think about the systems they were inheriting..footnote:[Inference: . Risk: .])_`

**Issue**: Double full stop before `footnote:`; empty Inference/Risk slots. Marker-resolved inference; left as-is.

### Flag 12 — Line 139 (Gilgamesh and Huwawa paragraph)

**Text**: "Both tell how Gilgamesh journeys to the Cedar Forest, confronts its guardian Huwawa (guardian of the Cedar Forest, appointed by Enlil, wielder of seven _me-lam_), tricks him into surrendering his radiances, and kills him."

**Issue**: The phrase "guardian of the Cedar Forest" appears both in the main clause ("its guardian Huwawa") and in the parenthetical gloss. The repetition is redundant but not ungrammatical. Pruning it would be a word-choice edit, which falls under line-edit's remit per rule 3 and the "What NOT to fix" list. Flagged for line-edit attention.

## Self-check summary

- No factual content changed across any applied fix (checked claim-by-claim in each Rationale block).
- No footnotes modified, added, or removed. EVIDENCE comments preserved verbatim. Footnote count unchanged.
- AsciiDoc structure preserved: all section headings (`==`, `===`), comparative-hook and EVIDENCE comment markers, formatting emphasis (`_..._`, `*...*`), and footnote references intact. The only structural edit was the newline repair on line 191, which corrects a pre-existing AsciiDoc structure defect rather than introducing one.
- Every change above "Issues noted but NOT fixed" is logged with original/corrected pair plus rationale. No silent edits.
