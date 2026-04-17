# Grammar-check diff: Chapter 20 - Gilgamesh and the Bull of Heaven

Input: `20-gilgamesh-and-the-bull-of-heaven.resolved.adoc`
Output: `20-gilgamesh-and-the-bull-of-heaven.grammar-checked.adoc`

Changes logged below in "original → corrected" format with rationale. Changes restricted to grammar, punctuation, and readability (per stage 14b rules). No factual, stylistic, footnote-content, or AsciiDoc-structural changes.

---

## 1. Line 10 — double periods inside italic editorial bracket note (damage summary)

**Original:**
> _[At this point the tablet breaks. ... The Akkadian Gilgamesh Tablet VI is a separate tradition and must not be used to fill gaps.. Partial from Sumerian sources, with important contributions from the Me-Turan manuscripts published by Cavigneaux and Al-Rawi (1993)..]_

**Corrected:**
> _[At this point the tablet breaks. ... The Akkadian Gilgamesh Tablet VI is a separate tradition and must not be used to fill gaps. Partial from Sumerian sources, with important contributions from the Me-Turan manuscripts published by Cavigneaux and Al-Rawi (1993).]_

**Rationale:** Two doubled-period typos (`gaps..` and `(1993)..`) reduced to single periods. The bracketed block is an editorial damage note in running italic prose (not a `footnote:[]` macro), so routine punctuation correction applies. Consistent with the treatment of analogous bracketed damage notes in chapter 19 (grammar-diff #3). No content change.

---

## 2. Line 16 — 58-word sentence with nested parentheticals split into two

**Original:**
> The composition is a Sumerian text narrating the episode in which Inanna — goddess of love, war, and the morning and evening star — sends the Bull of Heaven against Uruk (Sumerian: Unug), the great walled city of southern Mesopotamia, and Gilgamesh (Sumerian: Bilgames), king of Uruk, two-thirds divine hero, together with his companion Enkidu, slays it.footnote:[...]

**Corrected:**
> The composition is a Sumerian text narrating the episode in which Inanna — goddess of love, war, and the morning and evening star — sends the Bull of Heaven against Uruk (Sumerian: Unug), the great walled city of southern Mesopotamia. Gilgamesh (Sumerian: Bilgames), king of Uruk, two-thirds divine hero, together with his companion Enkidu, slays it.footnote:[...]

**Rationale:** The original sentence runs 58 words and combines a dash-offset epithet for Inanna, two `(Sumerian: X)` parentheticals, and a four-item appositive chain on Gilgamesh (king of Uruk, two-thirds divine hero, together with his companion Enkidu) suspended between the subject and the verb `slays`. This exceeds the 50-word threshold and forces the reader to re-parse to locate the second coordinate clause. Split at the comma before `and Gilgamesh` into two sentences (first ~33 words, second ~23 words). Coordinate `and` removed because it is no longer joining clauses within a single sentence; all information preserved verbatim. Footnote and EVIDENCE line unchanged.

---

## 3. Line 22 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(The motivation for Inanna's sending of the bull appears to involve Gilgamesh's rejection of her advances or some form of insult, consistent with the broader tradition..footnote:[Inference: ...])_

**Corrected:**
> _(The motivation for Inanna's sending of the bull appears to involve Gilgamesh's rejection of her advances or some form of insult, consistent with the broader tradition.footnote:[Inference: ...])_

**Rationale:** Doubled sentence-terminating period (`tradition..`) immediately before the `footnote:[...]` macro reduced to a single period. Same class of error fixed in chapter 19 grammar-diff #2 and #4. Double periods *inside* the footnote interior (`trigger..`, `alone..`) left untouched per hard rule 2 (no footnote changes).

---

## 4. Line 52 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(The Sumerian and Akkadian Bull of Heaven episodes share a common narrative kernel — Inanna's offence, the bull's attack, the heroes' slaying — but the Akkadian version represents an independent literary development, not a translation..footnote:[Inference: ...])_

**Corrected:**
> _(The Sumerian and Akkadian Bull of Heaven episodes share a common narrative kernel — Inanna's offence, the bull's attack, the heroes' slaying — but the Akkadian version represents an independent literary development, not a translation.footnote:[Inference: ...])_

**Rationale:** Same class of error as #3: doubled sentence-terminating period (`translation..`) before the `footnote:[...]` macro reduced to one. Double periods *inside* this footnote's interior text (`two traditions..`, `Sumerian text..`) left untouched per hard rule 2.

---

## Sentences reviewed for length/complexity but NOT changed

The following long or clause-heavy sentences were evaluated against the >50-word / 3+-subordinate-clause / nested-parenthetical tests and judged clear enough to retain as written. Logged here so the human can spot-check:

- Line 3: "The tablets are heavily damaged, especially in the sections describing the confrontation with the bull itself — the very event that gives the composition its name." (~27 words; single dash-offset appositive, parses on first reading).
- Line 26: "The pasture, the water, the trees: the infrastructure of life in a Mesopotamian city, swallowed or shattered by a creature operating on a cosmic scale." (~26 words; colon-introduced summary fragment for rhetorical effect, intentional and clear).
- Line 29: "The Me-Turan text is specific about the killing blow — Gilgamesh smites the Bull's skull with his axe weighing seven talents." (~22 words; post-dash illustration clause, clear).
- Line 32: "The detail of the seven-talent axe is characteristic of Sumerian heroic narrative — the weapon is impossibly heavy, the hero impossibly strong, and the text does not pause to explain how a mortal lifts what should be beyond mortal lifting." (~41 words; dash-offset tricolon plus coordinate clause, reads as a list by design).
- Line 41: "The identification of generic bull-combat contest scenes with the specific Gilgamesh Bull of Heaven narrative is, however, debated — most such scenes show a conventional struggle without identifying labels, and only a small number of explicitly labeled or contextually clear cases can be linked with confidence to this particular story." (~51 words; structure is `X is debated — [two-clause explanation]`, each sub-clause under 25 words, the dash break yields two parseable halves).
- Line 49: "The Akkadian Gilgamesh epic — specifically Standard Babylonian Tablet VI — contains a fully developed version of the Bull of Heaven episode, complete with Inanna's courtship, Gilgamesh's rejection speech, and a detailed battle narrative." (~35 words; one embedded parenthetical, three-item serial list in the tail, clear).
- Line 58: "The bull-slaying motif that runs through thousands of cylinder seals — heroes grappling with divine beasts in an image so persistent that it became one of the defining visual signatures of Mesopotamian culture — originated in a story that we can no longer fully read." (~46 words; one long dash-offset elaboration, main verb `originated` clearly locatable after the closing dash).

After change #2, no sentence exceeds the 50-word threshold. No remaining nested parentheticals. No subject-verb, tense, pronoun-reference, or article errors identified.

---

## Items deliberately NOT fixed (per hard rules)

- Double periods *inside* `footnote:[...]` interiors on lines 22 and 52 (`as the trigger..`, `text alone..`, `two traditions..`, `Sumerian text..`) — hard rule 2 forbids footnote changes.
- "his axe weighing seven talents" (line 29) — the participial modifier reads slightly stiffly; rephrasing to "his seven-talent axe" or "his axe, which weighs seven talents" would be smoother, but it is grammatically correct and the choice falls under word-choice/style (deferred to line-edit, stage 15).
- Register and word choice across the chapter (e.g., "infrastructure of life", "borrowed flesh") — deferred to line-edit.

---

## Self-check

1. Factual content: unchanged. No claim about texts, dates, people, places, or events was altered.
2. Footnote count: unchanged (12 `footnote:[...]` macros in input and output; interior text preserved verbatim).
3. EVIDENCE tokens: unchanged (11 `// EVIDENCE:` comments, identical).
4. AsciiDoc structure: unchanged (`== Gilgamesh and the Bull of Heaven` heading, four `'''` section breaks, three `// COMPARATIVE-HOOK:` comments, italic markup `_..._`, em-dashes `—` all preserved).
5. Every change is logged above. No silent changes.
