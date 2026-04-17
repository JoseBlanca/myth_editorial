# Grammar-check diff: Chapter 10 — Inanna and Enki

Every change made to `10-inanna-and-enki.resolved.adoc` to produce `10-inanna-and-enki.grammar-checked.adoc`. Each entry shows the original and corrected text with a short rationale. No factual content, footnotes, EVIDENCE comments, COMPARATIVE-HOOK comments, AsciiDoc structure, or marker-resolved passages were altered.

## Change 1 — Faulty "As X did Y" construction (Line 14)

**Original:**
> As Kramer devoted extensive analysis to demonstrating, the _me_ are the cosmic blueprints that make civilisation possible.

**Corrected:**
> As Kramer's extensive analysis demonstrates, the _me_ are the cosmic blueprints that make civilisation possible.

**Rationale:** The "As X devoted analysis to demonstrating, Y" construction is ungrammatical. The subordinator "as" requires a clause whose predicate matches or contextualises the main clause; "devoted extensive analysis to demonstrating" is an action, not a demonstration. Reframing the subordinate clause so that the subject is "Kramer's extensive analysis" and the verb is "demonstrates" makes the relationship between subordinate and main clause grammatical without changing the factual claim (that Kramer's analysis establishes this reading of the _me_).

## Change 2 — Overlong sentence with nested/redundant em-dash parentheticals (Line 25)

**Original (one sentence, ~75 words, four stacked appositive phrases describing Eridu, two of which are redundant):**
> Inanna -- goddess of love, war, and the morning and evening star -- resolves to travel from Uruk, great walled city of southern Mesopotamia (Sumerian: Unug), to the city of Eridu -- the oldest city in Sumerian tradition, seat of Enki's temple the E-abzu -- the most ancient of Sumerian cities and the dwelling place of Enki, god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath Eridu.

**Corrected (three sentences; no nested em-dash chains; redundant "oldest city / most ancient of Sumerian cities" collapsed into a single statement):**
> Inanna -- goddess of love, war, and the morning and evening star -- resolves to travel from Uruk, the great walled city of southern Mesopotamia (Sumerian: Unug), to Eridu. Eridu is the oldest city in Sumerian tradition and the seat of Enki's temple, the E-abzu. It is the dwelling place of Enki, god of wisdom, fresh water, and cunning, lord of the _abzu_ beneath the city.

**Rationale:** The original sentence violates three readability rules at once: it exceeds 50 words, it stacks nested/serial em-dash parentheticals (one set around Inanna's epithets, two more around Eridu), and it contains three or more subordinate/appositive clauses the reader must hold simultaneously. The two Eridu appositives ("the oldest city in Sumerian tradition, seat of Enki's temple the E-abzu" and "the most ancient of Sumerian cities and the dwelling place of Enki…") are functionally redundant. The fix splits the sentence into three, flattens the parentheticals, and removes the duplicated "oldest city" description while preserving every factual claim: Inanna's epithets, Uruk's character, Eridu's antiquity, the E-abzu, Enki's domains, and the _abzu_'s location. A definite article ("the great walled city") was inserted because "great walled city of southern Mesopotamia" reads as a singular identifying description and normally takes a determiner in English. No content was added or removed; only presentation was clarified.

## Change 3 — Missing serial comma (Line 88)

**Original:**
> Every _me_ that Enki offered and Inanna accepted -- every office, every craft, every emotion, every virtue and every vice -- is now installed in the E-ana.

**Corrected:**
> Every _me_ that Enki offered and Inanna accepted -- every office, every craft, every emotion, every virtue, and every vice -- is now installed in the E-ana.

**Rationale:** The skill mandates the serial (Oxford) comma. The penultimate list item was missing its serial comma before "and every vice." Inserted; no meaning change.

---

## Self-check

- **Factual content:** Unchanged. Every cited fact (catalogue of Inanna's epithets, the identity and location of Eridu, the E-abzu, Enki's attributes, the _abzu_, Kramer's scholarly claim about the _me_, the list of items in the E-ana) is preserved.
- **Footnotes:** All footnote markers and text, and all EVIDENCE comments and COMPARATIVE-HOOK comments, are unchanged. Footnote count is identical.
- **Marker-resolved passages:** The italic bracketed lacuna blocks (lines 23 and 45 of the input) and the italic parenthetical inference blocks (input lines 50 and 94) were left untouched, including the intentional ".." marker punctuation inside them.
- **AsciiDoc structure:** Heading, section breaks (`'''`), italic/emphasis markup, and all line breaks around evidence comments are intact.
- **No silent changes.** Only the three changes above were made.
