# Grammar-check diff — Chapter 27: Lugalbanda and the Anzud Bird

Every mechanical change below is logged as `original → corrected` with a short rationale. No factual content, footnote content, AsciiDoc structure, or marker-resolved passages were altered.

---

## Change 1 — Split overloaded sentence (line 17)

**Original:**
> Lugalbanda was alone in the mountains, separated from Enmerkar's army, which continued its march toward Aratta -- the distant, wealthy city beyond the ranges that was the object of Enmerkar's campaign.

**Corrected:**
> Lugalbanda was alone in the mountains, separated from Enmerkar's army. The army continued its march toward Aratta, the distant, wealthy city beyond the ranges that was the object of Enmerkar's campaign.

**Rationale:** Readability. Original contained three layered relative clauses ("which continued...", "that was the object..."), an em-dash aside, and a participial phrase in a single sentence. Splitting at the comma before the relative clause removes a clause and flattens the em-dash into a straightforward appositive. No meaning change.

---

## Change 2 — Capitalize sentence after period in stage direction (line 20)

**Original:**
> _[At this point the tablet breaks. Opening lines (1--15) partially damaged; initial context for Lugalbanda's separation from the army fragmentary. multiple OB manuscripts overlap to restore most of the opening.]_

**Corrected:**
> _[At this point the tablet breaks. Opening lines (1--15) partially damaged; initial context for Lugalbanda's separation from the army fragmentary. Multiple OB manuscripts overlap to restore most of the opening.]_

**Rationale:** Punctuation / capitalization. "multiple" begins a new sentence after a full stop and must be capitalized.

---

## Change 3 — Split long appositive chain (line 29)

**Original:**
> He discovered a nest -- not the nest of any ordinary bird, but the nest of the Anzud, the divine lion-headed eagle, an enormous creature of terrifying power whose wingspan darkened the mountains.

**Corrected:**
> He discovered a nest -- not the nest of any ordinary bird, but the nest of the Anzud, the divine lion-headed eagle. It was an enormous creature of terrifying power whose wingspan darkened the mountains.

**Rationale:** Readability. Original stacked three successive appositives ("the Anzud", "the divine lion-headed eagle", "an enormous creature...") onto a single noun, forcing the reader to hold four levels of nominal modification at once. The final appositive is promoted to its own sentence. No meaning change.

---

## Change 4 — Split 51-word sentence at a natural coordinating break (line 68)

**Original:**
> Speed was the practical answer to a practical problem, and the fact that Lugalbanda saw this, when a god was offering him anything he wanted, tells us something about the kind of hero the Sumerian scribes wanted him to be.

**Corrected:**
> Speed was the practical answer to a practical problem. The fact that Lugalbanda saw this, when a god was offering him anything he wanted, tells us something about the kind of hero the Sumerian scribes wanted him to be.

**Rationale:** Readability. Original was 41 words but contained three subordinate clauses on the second half after a "fact that" subject; combined with the coordinating "and" in front it crossed the clause-count threshold. A period replaces the comma-plus-"and" to give each clause its own sentence. No meaning change.

---

## Change 5 — Fix double period and nested parenthetical / footnote typo (line 77)

**Original:**
> _(The secrecy condition creates narrative tension for future episodes and establishes a divine taboo -- the gift's power depends on discretion, a common motif in stories of supernatural endowment..footnote:[Inference: The Anzud explicitly commands silence, and Lugalbanda observes the prohibition.. Risk: The narrative function of the secrecy motif is inferred; the text does not explain why secrecy is required..])_

**Corrected:**
> _(The secrecy condition creates narrative tension for future episodes and establishes a divine taboo -- the gift's power depends on discretion, a common motif in stories of supernatural endowment.footnote:[Inference: The Anzud explicitly commands silence, and Lugalbanda observes the prohibition. Risk: The narrative function of the secrecy motif is inferred; the text does not explain why secrecy is required.])_

**Rationale:** Punctuation. Three instances of accidental double periods (`..`) — one before the footnote macro and two inside the footnote body — collapsed to single periods. Footnote macro must not be preceded by `..` or it renders incorrectly. No content change to the footnote text itself beyond removing the duplicated punctuation.

---

## Change 6 — Flatten nested em-dash parenthetical identifying Inanna (line 86)

**Original:**
> He needed a messenger to travel back to Uruk and consult Inanna -- the goddess of love and war, patron of Uruk, whose temple the E-ana stood at the heart of the city -- about how to proceed.

**Corrected:**
> He needed a messenger to travel back to Uruk and consult Inanna about how to proceed. Inanna was the goddess of love and war, patron of Uruk, whose temple the E-ana stood at the heart of the city.

**Rationale:** Readability. The em-dash aside contained a three-item appositive ("goddess...", "patron...", "whose temple...") inserted between the verb "consult" and its complement "about how to proceed", forcing the reader to suspend the verb-complement link across 23 intervening words. Moving the appositive to a follow-on sentence restores a clean verb-complement structure. No meaning change.

---

## Change 7 — Capitalize sentence after period in stage direction (line 94)

**Original:**
> _[At this point the tablet breaks. Minor gaps in lines 350--380 where Lugalbanda delivers Enmerkar's message to Inanna. composite reconstruction from heavily attested manuscripts covers the gaps.]_

**Corrected:**
> _[At this point the tablet breaks. Minor gaps in lines 350--380 where Lugalbanda delivers Enmerkar's message to Inanna. Composite reconstruction from heavily attested manuscripts covers the gaps.]_

**Rationale:** Punctuation / capitalization. "composite" begins a new sentence after a full stop and must be capitalized.

---

## Self-check

1. No factual content changed — all named figures, places, line ranges, page numbers, and source citations are identical between original and corrected versions.
2. Footnote count and content unchanged except for the removal of three duplicate periods in one footnote/macro (Change 5); no footnote text was added, removed, or reworded.
3. AsciiDoc structure intact: heading, `'''` section breaks, `footnote:[...]` macros, `// EVIDENCE:` and `// COMPARATIVE-HOOK:` comment lines, and emphasis (`_..._`) all preserved.
4. All seven changes are logged above; no silent changes were made.
