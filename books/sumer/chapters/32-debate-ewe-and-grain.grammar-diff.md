# Grammar-check diff: 32-debate-ewe-and-grain

Stage: 14b grammar-check
Input: `chapters/32-debate-ewe-and-grain.resolved.adoc`
Output: `chapters/32-debate-ewe-and-grain.grammar-checked.adoc`

Every mechanical change is listed below as `original → corrected` with a rationale. No factual, stylistic, or footnote-content changes were made. AsciiDoc structure, footnote count, EVIDENCE markers, and COMPARATIVE-HOOK markers are preserved verbatim.

---

## Change 1 — Line 3 (opening paragraph): noun-phrase / adjective-phrase fragment

**Original:**
> The composition known as "The Debate between Ewe and Grain" is catalogued as ETCSL 5.3.2 and survives on Old Babylonian tablets from Nippur.footnote:[ETCSL 5.3.2, bibliography.] Generally well-preserved; notable for its cosmogonic prologue.footnote:[ETCSL 5.3.2, composite text.]

**Corrected:**
> The composition known as "The Debate between Ewe and Grain" is catalogued as ETCSL 5.3.2 and survives on Old Babylonian tablets from Nippur.footnote:[ETCSL 5.3.2, bibliography.] It is generally well-preserved and notable for its cosmogonic prologue.footnote:[ETCSL 5.3.2, composite text.]

**Rationale:** Sentence-fragment / punctuation fix. "Generally well-preserved; notable for its cosmogonic prologue." has no subject or main verb — it is two adjectival phrases joined by a semicolon. Semicolons should join independent clauses, and a standalone adjective phrase is not a sentence. Supplying the elided subject and verb ("It is") yields a complete sentence, and replacing the semicolon with "and" joins two parallel predicate adjectives ("well-preserved" / "notable") the way the original clearly intended. No factual content changed: the composition is still described as generally well-preserved and as notable for its cosmogonic prologue. Footnote unchanged.

---

## Change 2 — Line 47 (editorial inset after the first tablet break): missing copula

**Original:**
> _[At this point the tablet breaks. Some lines in the central exchange partially damaged (lines 100--115). Overlapping Nippur manuscripts restore most of the passage.]_

**Corrected:**
> _[At this point the tablet breaks. Some lines in the central exchange are partially damaged (lines 100--115). Overlapping Nippur manuscripts restore most of the passage.]_

**Rationale:** Grammar fix (subject without verb). "Some lines in the central exchange partially damaged" lacks a finite verb — "partially damaged" is a past-participial phrase, not a predicate, so the clause has no predication. Inserting the copula "are" yields a complete clause ("Some lines … are partially damaged"), which is the only grammatically correct reading and is almost certainly what was intended, as the preceding and following sentences ("the tablet breaks", "manuscripts restore") both use finite verbs. No factual content changed: the editorial inset still reports a tablet break, still identifies the damaged range as lines 100–115 of the central exchange, and still notes that overlapping Nippur manuscripts restore most of the passage. This inset is an editorial apparatus sentence, not a resolved-marker inference note (the latter use the `_( … )_` form), so the marker-resolved lock does not apply.

---

## Change 3 — Line 82 (penultimate paragraph): over-50-word sentence with nested parenthetical inside em-dash aside ending in colon

**Original:**
> The most famous parallel appears in Genesis 4, where Cain the farmer kills Abel the shepherd after God accepts Abel's offering and rejects Cain's -- a narrative with the same structural elements (two ways of life, divine preference, a verdict) but a reversed outcome: in the Hebrew tradition, the shepherd is favoured over the farmer.

**Corrected:**
> The most famous parallel appears in Genesis 4, where Cain the farmer kills Abel the shepherd after God accepts Abel's offering and rejects Cain's. The narrative shares the same structural elements -- two ways of life, divine preference, a verdict -- but reverses the outcome: in the Hebrew tradition, the shepherd is favoured over the farmer.

**Rationale:** Readability fix. The original sentence ran to roughly 54 words and layered an em-dash appositive that itself contained a parenthetical list and was then extended by a colon introducing a further independent clause ("in the Hebrew tradition…"). That gives the reader one sentence to hold open across an em-dash, inside parentheses, and across a colon, which violates the rule against stacked asides. Splitting at the natural boundary (ending the first sentence after "Cain's") yields two sentences, each under 35 words. In the second sentence, the parenthetical list ("two ways of life, divine preference, a verdict") is promoted to an em-dash aside — the form normally used for in-line enumerations of this kind in the surrounding prose — which removes the nested `( … )` inside an em-dash aside. The colon-introduced clause ("in the Hebrew tradition, the shepherd is favoured over the farmer") is preserved in its original position at the end of the second sentence. No factual content changed: Genesis 4 is still cited, Cain is still identified as the farmer and Abel as the shepherd, the killing and the divine acceptance/rejection are unchanged, the three structural elements (two ways of life, divine preference, verdict) are preserved verbatim, and the reversed outcome (the Hebrew tradition favours the shepherd over the farmer) is unchanged. No footnote or EVIDENCE token is touched.

---

## Self-check

1. **No factual content changed.** Every claim about ETCSL 5.3.2, the Old Babylonian manuscript witnesses from Nippur, the two disputants (Lahar / Ewe and Ashnan / Grain), the cosmogonic prologue and its forty-line length, the primordial condition of humanity (grass, ditches, nakedness), the creation in the _dul-kug_, the roles of Enlil and Enki, the debate at the drunken feast, Grain's and Ewe's respective arguments, the tablet damage at lines 100–115, the insult exchange, Enki's verdict in favour of Grain, the reconciliation, the _edubba_ curricular function, and the comparative material (Genesis 4, Prometheus, Hesiod, Vedic pre-civilised states) is preserved verbatim. Source attributions (ETCSL, Black et al. 2004, Kramer 1961, Jacobsen 1987) are unchanged.
2. **Footnote count and content unchanged.** All footnote macros and their text are preserved verbatim; no footnotes added, removed, or edited.
3. **EVIDENCE and COMPARATIVE-HOOK tokens preserved verbatim** in all positions (13 EVIDENCE tokens and 3 COMPARATIVE-HOOK tokens, unchanged in text and line placement).
4. **Resolved-marker passages untouched.** The two italicised inference notes `_( … )_` at the end of the "cosmogonic prologue" and "verdict" sections are preserved verbatim, including their internal Inference/Risk footnotes.
5. **AsciiDoc structure intact:** chapter heading `==`, section headings `===`, section breaks `'''`, italic emphasis (`_dul-kug_`, `_abzu_`, `_edubba_`), italicised editorial inset `_[ … ]_`, and the italicised inference notes `_( … )_` are all in place and position. EVIDENCE and COMPARATIVE-HOOK comment lines remain at their original line positions.
6. **Every change logged above.** No silent edits.
