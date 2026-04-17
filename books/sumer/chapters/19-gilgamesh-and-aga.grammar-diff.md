# Grammar-check diff: Chapter 19 - Gilgamesh and Aga

Input: `19-gilgamesh-and-aga.resolved.adoc`
Output: `19-gilgamesh-and-aga.grammar-checked.adoc`

Changes logged below in "original → corrected" format with rationale. Changes restricted to grammar, punctuation, and readability (per stage 14b rules). No factual, stylistic, footnote-content, or AsciiDoc-structural changes.

---

## 1. Line 3 — semicolon misuse

**Original:**
> It is mostly complete; the shortest and most cohesive of the Sumerian Gilgamesh poems, and unique in containing no supernatural elements.

**Corrected:**
> It is mostly complete -- the shortest and most cohesive of the Sumerian Gilgamesh poems, and unique in containing no supernatural elements.

**Rationale:** A semicolon must join two independent clauses. The material after the semicolon ("the shortest and most cohesive... and unique...") is an appositive noun phrase, not an independent clause. Replaced the semicolon with an em-dash (AsciiDoc `--`), which correctly introduces the appositive. No change in meaning.

---

## 2. Line 40 — double period before footnote macro in running prose

**Original:**
> ...deliberating separately on a question of war and peace..footnote:[Inference: ...]

**Corrected:**
> ...deliberating separately on a question of war and peace.footnote:[Inference: ...]

**Rationale:** The sentence terminator was a doubled period typo (`..`) immediately before the `footnote:[...]` macro. Reduced to a single period. Punctuation-only fix; meaning unchanged. Double periods *inside* the footnote content (e.g., `institutions..`, `document..`) were left untouched per hard rule 2 (no footnote changes).

---

## 3. Line 61 — double periods inside italic editorial bracket note

**Original:**
> _[At this point the tablet breaks. Portions of the siege climax and Aga's response (approximately lines 85-95) are partially damaged.. Partial; manuscript overlap restores most of the sequence, but the precise mechanics of the climactic moment remain uncertain in places..]_

**Corrected:**
> _[At this point the tablet breaks. Portions of the siege climax and Aga's response (approximately lines 85-95) are partially damaged. Partial; manuscript overlap restores most of the sequence, but the precise mechanics of the climactic moment remain uncertain in places.]_

**Rationale:** Two doubled-period typos (`damaged..` and `places..`) reduced to single periods. The bracketed passage is an editorial damage note in running prose (not a `footnote:[]` macro), so punctuation correction applies. Content preserved in full.

---

## 4. Line 78 — double period before footnote macro in running prose

**Original:**
> ...in which martial victory is tempered by reciprocal obligation..footnote:[Inference: ...]

**Corrected:**
> ...in which martial victory is tempered by reciprocal obligation.footnote:[Inference: ...]

**Rationale:** Same class of error as change 2: doubled sentence-terminating period before the `footnote:[...]` macro. Reduced to one period. Double periods *inside* this footnote's interior text (e.g., `Gilgamesh and Aga..`, `interpretations vary..`) were left untouched per hard rule 2.

---

## Sentences reviewed for length/complexity but NOT changed

The following long or clause-heavy sentences were evaluated against the >50-word / 3+-subordinate-clause / nested-parenthetical tests and judged clear enough to retain as written. Logged here so the human can spot-check:

- Line 42: "A king who consults two assemblies..." (~38 words, two coordinated clauses, parses on first reading).
- Line 46: "The composition is a tightly constructed political narrative..." (~33 words).
- Line 65: "Gilgamesh simply appears on the wall, and the effect of his presence -- his physical stature, his royal bearing, the sheer fact of him standing above the battlements -- is enough." (~31 words; a single embedded parenthetical, not nested).
- Line 75: "The exact nature of the prior obligation is not fully spelled out..." (~33 words).
- Line 89: "It is a text that advocates a specific model of kingship: one in which the king listens before he acts, draws his mandate from the young warriors rather than the cautious elders, defends his city's autonomy against imperial claims, and tempers victory with reciprocal obligation." (~45 words; colon-introduced parallel list of four verb phrases, reads as a list by design).
- Line 95: "The solution it proposes -- consult widely, choose boldly, defend stubbornly, and treat the defeated enemy with a magnanimity that creates obligation rather than resentment -- is a political philosophy, not merely a plot." (~35 words; parallel imperatives in a dash-offset list).

No sentence exceeded the 50-word threshold. No nested parentheticals were found. No subject-verb, tense, pronoun-reference, or article errors identified.

---

## Items deliberately NOT fixed (per hard rules)

- Double periods *inside* `footnote:[...]` interiors on lines 40, 63, and 78 — hard rule 2 forbids footnote changes.
- Line 37 footnote `[George 2003, pp. 141-142]` lacks a terminal period inside, while sibling footnotes include one — footnote-content consistency is out of scope for grammar-check.
- Line 16 footnote `[ETCSL 1.8.1.1, manuscript list]` similarly missing terminal period — out of scope.
- Register and word choice across the chapter — deferred to line-edit (stage 15).

---

## Self-check

1. Factual content: unchanged. No claim about dates, people, texts, or events was altered.
2. Footnote count: unchanged (same number of `footnote:[...]` macros and same interior text).
3. EVIDENCE tokens: unchanged.
4. AsciiDoc structure: unchanged (heading, horizontal rules `'''`, `//` comments, italic markup `_..._`, em-dash `--` all preserved).
5. Every change is logged above. No silent changes.
