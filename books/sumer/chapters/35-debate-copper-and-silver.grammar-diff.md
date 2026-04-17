# Grammar-check diff — Chapter 35: The Debate between Copper and Silver

Source: `35-debate-copper-and-silver.resolved.adoc`
Output: `35-debate-copper-and-silver.grammar-checked.adoc`

Every mechanical change below is logged with the original text, the corrected text, and the rationale. Word choice, rhythm, nominalizations, footnote content, resolved-marker passages, and AsciiDoc structure were left untouched per the skill's "What NOT to fix" list.

---

## Change 1 — Opening paragraph, 50-word sentence with nested comparison

**Original:**
> Fewer copies survive than for any other debate poem -- CDLI records only eleven manuscript witnesses, all from Nippur, compared with sixty or seventy for Hoe and Plough or Ewe and Grain -- suggesting more limited circulation in the _edubba_, the scribal school where these texts were copied and taught.footnote:[ETCSL 5.3.6, manuscript list; CDLI P478959.]

**Corrected:**
> Fewer copies survive than for any other debate poem. CDLI records only eleven manuscript witnesses, all from Nippur, compared with sixty or seventy for Hoe and Plough or Ewe and Grain. This suggests more limited circulation in the _edubba_, the scribal school where these texts were copied and taught.footnote:[ETCSL 5.3.6, manuscript list; CDLI P478959.]

**Rationale:** The original sentence is exactly 50 words and contains a long em-dash aside that itself includes an embedded comparison clause ("compared with sixty or seventy..."), pushing the reader to juggle several elements at once. Split into three sentences: the headline claim, the manuscript-count evidence, and the inference. Footnote remains attached to the final sentence. No factual content or footnote text was altered.

---

## Change 2 — Second paragraph, nested parentheticals and stacked appositives

**Original:**
> The text belongs to the Sumerian debate genre and features two personified metals -- Copper (Sumerian _urudu_) and Silver (Sumerian _ku-babbar_) -- who argue their relative merits before Enlil, king of the gods, lord of wind and command, supreme authority in Nippur (Sumerian: Nibru).footnote:[ETCSL 5.3.6, composite text, Segments A--I.]

**Corrected:**
> The text belongs to the Sumerian debate genre and features two personified metals -- Copper (Sumerian _urudu_) and Silver (Sumerian _ku-babbar_) -- who argue their relative merits before Enlil. Enlil is king of the gods, lord of wind and command, supreme authority in Nippur (Sumerian: Nibru).footnote:[ETCSL 5.3.6, composite text, Segments A--I.]

**Rationale:** The original contains an em-dash aside that itself holds two inline parentheticals (`(Sumerian _urudu_)`, `(Sumerian _ku-babbar_)`), plus a third parenthetical (`(Sumerian: Nibru)`) at the end, plus three stacked appositives describing Enlil — a readability violation under "nested parenthetical asides" and "three or more subordinate clauses". Split at the subject "Enlil" so the appositive chain about Enlil starts a fresh sentence. No facts changed; footnote text and placement preserved.

---

## Self-check

1. **No factual content changed.** All names, numbers, citations, and claims are identical between versions. The only substantive words added are the copular verb ("This suggests" in Change 1, "Enlil is" in Change 2), which restore grammatical subjects after splitting.
2. **Footnote count and content unchanged.** All six inline `footnote:[...]` calls and all EVIDENCE comments appear in the same order and with identical text.
3. **AsciiDoc structure intact.** Section headings (`==`, `===`), thematic breaks (`'''`), italicised inline markup (`_..._`), and COMPARATIVE-HOOK comments are unchanged.
4. **Resolved-marker passages untouched.** The bracketed gap-notice paragraph and the italicised inference aside in Copper's reply are unchanged.
5. **No silent changes.** Every modification is listed above.

## Items considered and not changed

- "Silver is beautiful, Silver adorns the palace, Silver graces the banquet table -- but the fields must be ploughed, the weeds must be chopped, the grain must be reaped, and for all of these tasks, the civilisation of southern Mesopotamia required copper." (42 words, many parallel clauses) — the parallelism is anaphoric and intentional; splitting would destroy the rhetorical structure. Rhythm is line-edit's concern.
- "Despite its fragmentary state and limited manuscript attestation, the surviving portions reveal a composition with a distinctive economic theme -- the tension between the metal of daily labour and the metal of ceremonial display, a question that was not abstract in Mesopotamian life." (43 words) — single em-dash aside that expands naturally; no nesting; under 50 words.
- "The composition receives less scholarly treatment than the major debates -- Hoe and Plough, Ewe and Grain, Winter and Summer -- but it is noted for this unusual focus on material value." — em-dash aside holds a clean three-item list; readable.
- "It turns on Silver with contempt: the palace is Silver's station, and banquets are Silver's assigned task -- but what happens to Silver when the banquet is over?" — colon plus em-dash is idiomatic here; the rhetorical question lands cleanly.
- Serial commas, em-dash vs. hyphen usage, apostrophes in Sumerian terms, and italics conventions are already consistent.
