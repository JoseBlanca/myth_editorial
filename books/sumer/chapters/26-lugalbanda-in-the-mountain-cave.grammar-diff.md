# Grammar-check diff — Chapter 26: Lugalbanda in the Mountain Cave

Every change made by the grammar-check stage, with rationale. No factual content, footnote content, or AsciiDoc structure was altered. Changes address only grammar, punctuation, and readability (sentence length, nested parentheticals, chain-clauses).

---

## Change 1 — Split long sentence with chained relative clause (line 18)

**Original:**
> Lugalbanda -- soldier and later king of Uruk, father of Gilgamesh in tradition -- served in the army of Enmerkar, king of Uruk, who was leading his forces across mountainous terrain toward the distant city of Aratta -- the fabulously wealthy city beyond the mountains, rival of Uruk.

**Corrected:**
> Lugalbanda -- soldier and later king of Uruk, father of Gilgamesh in tradition -- served in the army of Enmerkar, king of Uruk. Enmerkar was leading his forces across mountainous terrain toward the distant city of Aratta -- the fabulously wealthy city beyond the mountains, rival of Uruk.

**Rationale:** The original was a ~55-word sentence carrying three em-dash appositives and a long relative clause ("who was leading…") whose antecedent is the second "Uruk" rather than its nearer noun "Enmerkar." Splitting into two sentences removes the ambiguous pronoun reference, reduces clause count, and keeps readers from re-parsing. No content or emphasis changed.

---

## Change 2 — Remove doubled periods inside resolved parenthetical (line 40)

**Original:**
> _(Lugalbanda's piety is correct and meticulous even in a wilderness setting -- the text emphasizes that proper devotion is rewarded even outside temple or city..footnote:[Inference: The three deities each accept his prayers and grant healing.. Risk: The text presents the prayers and divine responses without explicit commentary on ritual correctness..])_

**Corrected:**
> _(Lugalbanda's piety is correct and meticulous even in a wilderness setting -- the text emphasizes that proper devotion is rewarded even outside temple or city.footnote:[Inference: The three deities each accept his prayers and grant healing. Risk: The text presents the prayers and divine responses without explicit commentary on ritual correctness.])_

**Rationale:** Three instances of doubled terminal periods (`city..`, `healing..`, `correctness..`) — mechanical punctuation errors. The footnote body and the sentence itself are otherwise unchanged. (This is a resolved-marker passage but the changes are purely punctuation and do not touch wording or meaning, falling under the grammar-check mandate for punctuation.)

---

## Change 3 — Flatten nested em-dash parentheticals in god-list sentence (line 61)

**Original:**
> Then Lugalbanda received a dream vision from the god Zangara, who instructed him to sacrifice the animals he had caught; he performed the sacrifices and made a banquet invoking An, Enlil -- king of the gods, lord of wind and command, supreme authority in Nippur -- Enki -- god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath Eridu -- and Ninhursaja -- mother goddess, lady of the mountain.

**Corrected:**
> Then Lugalbanda received a dream vision from the god Zangara, who instructed him to sacrifice the animals he had caught. He performed the sacrifices and made a banquet invoking four great gods: An; Enlil, king of the gods, lord of wind and command, supreme authority in Nippur; Enki, god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath Eridu; and Ninhursaja, mother goddess, lady of the mountain.

**Rationale:** The original sentence was ~70 words with three consecutive em-dash parenthetical appositives running together, so that the em-dashes served double duty as both opening and closing brackets for adjacent gods. This made it hard to tell where each god's gloss ended and the next began. Fixes applied:
1. Split at the semicolon into two sentences (the semicolon was already separating two independent clauses).
2. Replaced the chain of em-dash appositives with a colon-introduced list using semicolons to separate list items (because each item contains internal commas). Serial semicolon retained before the final item.
3. Added "four great gods:" as an anticipatory phrase (the same count already stated in the immediately following sentence — no factual addition).

The four gods and their descriptive glosses are preserved verbatim. Only punctuation and sentence boundaries changed.

---

## Items considered and left unchanged

- **Line 3** (opening sentence with multiple em-dash glosses for Nippur and Ur): long but each parenthetical is non-nested and serves a reference function; splitting would remove the paired glosses. Left as is.
- **Line 27** ("These were not strangers…"): long paragraph but individual sentences are under 50 words and parse cleanly.
- **Line 44** (Utu / Inanna / Nanna sequence): parallel em-dash phrasing is intentional and parses cleanly because each phrase stands alone on its own sentence, not nested.
- Em-dashes, en-dashes, serial commas, and AsciiDoc constructs: consistent throughout; no fixes needed.
- Spellings "civilisation," "behaviour," "favour," "centre," "emphasizes": British English predominates but "emphasizes" (US spelling) appears once on line 40. Left unchanged because the grammar-check skill excludes word-choice fixes, and consistency of orthography is a style/house-style concern handled later.

---

## Self-check

1. Factual claims: unchanged. Gods, line numbers, citations, events all match original.
2. Footnote count: 17 footnotes in original, 17 in corrected. Contents identical except removal of doubled periods inside the parenthetical on line 40.
3. AsciiDoc structure: heading, thematic breaks (`'''`), EVIDENCE comments, COMPARATIVE-HOOK comments, italic block delimiters all intact.
4. Every change logged above.
