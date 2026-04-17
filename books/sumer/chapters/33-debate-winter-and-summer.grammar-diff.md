# Grammar-check diff: 33-debate-winter-and-summer

Stage: 14b grammar-check
Input: `chapters/33-debate-winter-and-summer.resolved.adoc`
Output: `chapters/33-debate-winter-and-summer.grammar-checked.adoc`

Every mechanical change is listed below as `original → corrected` with a rationale. No factual, stylistic, or footnote-content changes were made. AsciiDoc structure, footnote count, EVIDENCE markers, and COMPARATIVE-HOOK markers are preserved verbatim.

---

## Change 1 — Line 3 (opening paragraph): misattached modifier and verbless fragment

**Original:**
> The composition known as "The Debate between Winter and Summer" is catalogued as ETCSL 5.3.3 and survives on Old Babylonian tablets, frequent in Nippur scribal school sites.footnote:[ETCSL 5.3.3, bibliography.] Mostly complete at 318 lines.footnote:[ETCSL 5.3.3, composite text.]

**Corrected:**
> The composition known as "The Debate between Winter and Summer" is catalogued as ETCSL 5.3.3 and survives on Old Babylonian tablets, with frequent copies from Nippur scribal school sites.footnote:[ETCSL 5.3.3, bibliography.] It is mostly complete at 318 lines.footnote:[ETCSL 5.3.3, composite text.]

**Rationale:** Two mechanical problems in a single passage.

(a) "tablets, frequent in Nippur scribal school sites" misattaches the adjective "frequent" to "tablets". Read literally, the modifier says the individual tablets are "frequent" at those sites, which is not what the clause intends. The intended meaning — that frequent copies of the composition are found at those sites — is supplied by expanding the appositive to "with frequent copies from Nippur scribal school sites". This matches the same phrasing used verbatim at line 11 ("survives in frequent Old Babylonian copies from Nippur scribal school sites"), so no new fact is introduced.

(b) "Mostly complete at 318 lines." is a verbless fragment: it lacks a subject and a finite verb. Supplying the elided "It is" yields a complete declarative sentence ("It is mostly complete at 318 lines.") that refers back to the composition named in the immediately preceding sentence, which is the only available referent. No factual content changed: the tablets are still Old Babylonian, still associated with Nippur scribal school sites, and the 318-line extent is preserved. Both footnote macros are unchanged and remain in their original positions.

---

## Change 2 — Line 47 (editorial inset after the tablet-break marker): missing copula

**Original:**
> _[At this point the tablet breaks. Several lines in the central exchange partially broken (lines 140--155). Overlapping Nippur school tablets restore the passage in large part.]_

**Corrected:**
> _[At this point the tablet breaks. Several lines in the central exchange are partially broken (lines 140--155). Overlapping Nippur school tablets restore the passage in large part.]_

**Rationale:** Grammar fix (subject without finite verb). "Several lines in the central exchange partially broken" lacks a predicate — "partially broken" is a past-participial phrase, not a finite verb, so the clause has no predication. Inserting the copula "are" produces the only grammatically complete reading ("Several lines … are partially broken"), and is the parallel construction the author used in the sister composition's editorial inset at the same stage (chapter 32, line 47: "Some lines … are partially damaged" after the same fix). The surrounding sentences in this inset use finite verbs ("the tablet breaks", "manuscripts restore"), so the missing copula is the only structurally deviant element. No factual content changed: the inset still reports a tablet break, still identifies the damaged range as lines 140–155 of the central exchange, and still notes that overlapping Nippur school tablets restore the passage in large part. This inset is an editorial apparatus sentence in the `_[ … ]_` form (not the `_( … )_` resolved-marker inference form), so the marker-resolved lock does not apply.

---

## Flagged — not fixed

### Flag 1 — Line 83 (comparative paragraph): over-50-word sentence with three subordinate clauses

**Text:**
> Whether the medieval form descends from the Sumerian through channels of transmission that the evidence does not allow us to trace, or whether the structure emerged independently wherever literate cultures confronted the fact that seasons alternate and someone had to decide which one mattered more, is a question scholars have raised without settling.

**Issue:** The sentence runs to roughly 53 words and stacks at least three levels of subordination: a "whether … or whether" disjunction as grammatical subject, inside which each arm carries its own restrictive clause ("that the evidence does not allow us to trace" inside the first; "wherever literate cultures confronted the fact that seasons alternate and someone had to decide which one mattered more" inside the second). Under the readability rule it is a candidate for splitting.

**Why not fixed:** The sentence's meaning depends on holding both disjunctive possibilities open under a single question-subject resolved by the main predicate ("is a question scholars have raised without settling"). Splitting the disjunction at either "or whether" or at "is a question" changes the rhetorical relation between the two alternatives: the original presents them as co-equal arms of one open question, and any split converts them into separately asserted propositions. Rewording the second arm (for example, by promoting "someone had to decide which one mattered more" to a separate sentence) would remove the joint conditional "seasons alternate AND someone had to decide", which is the content of what the text says literate cultures confronted. Because every available split risks re-weighting an argumentative claim, this is flagged for human review at line-edit rather than mechanically restructured. The length is therefore treated as essential to meaning under the skill's exception.

### Flag 2 — Line 85 (comparative paragraph): compound subject with singular verb

**Text:**
> The Greek Demeter/Persephone myth provides a different structural solution to the same problem -- the goddess's descent to the underworld and annual return explains the alternation of seasons through a story of loss and reunion rather than through a competitive debate.

**Issue:** The subject of "explains" is the coordinate noun phrase "the goddess's descent to the underworld and annual return". Under strict subject-verb agreement, a compound subject joined by "and" takes a plural verb ("explain"), which would yield "the goddess's descent … and annual return explain the alternation of seasons".

**Why not fixed:** This is a borderline case. "Descent and return" can be read either as two events (strict plural) or as a single cyclical unit (notional singular, as with "bread and butter is a staple"). The adjacent COMPARATIVE-HOOK comment at line 89 uses the same singular construction verbatim ("the goddess's descent and return explains the alternation of seasons"), which indicates a consistent authorial reading of the phrase as a single cyclical event rather than two separate events. Changing the verb number in the body text without changing the metadata would create an inconsistency with the hook, and changing both would amount to a stylistic call about whether the phrase names a cycle or two events — a judgement properly made at line-edit, not at grammar-check. Flagged for human review.

### Flag 3 — Line 49 (debate section): potential zero-object verb ambiguity

**Text:**
> At each stage, the relevant season steps forward to claim credit, and the other objects.

**Issue:** "the other objects" uses "objects" as an intransitive verb (to raise an objection), but the parallel structure with the preceding "the relevant season steps forward to claim credit" can briefly mislead the reader into parsing "objects" as a plural noun ("the other [one's] objects") before the absence of any further continuation forces a re-parse to the verb reading.

**Why not fixed:** The sentence is grammatically well-formed. "Objects" as an intransitive present-tense verb is standard English, and the subject "the other" (ellipsis for "the other season") is recoverable from the preceding clause. The momentary re-parse is a stylistic matter (sentence rhythm, word choice), not a grammar error, and the skill explicitly excludes word choice from grammar-check. Flagged here only so that line-edit can consider whether to substitute a less briefly ambiguous verb (e.g., "and the other raises objections") if it chooses.

---

## Self-check

1. **No factual content changed.** Every claim about ETCSL 5.3.3, the Old Babylonian manuscript witnesses from Nippur scribal school sites, the 318-line extent, the supplementation by Black et al. 2004 (pp. 226–233), the two disputants (Enten / Winter and Emesh / Summer), the cosmogonic prologue and Enlil's creation of the seasons, Enten's assignment to rains-floods-soil fertility, Emesh's assignment to ripening-harvest-abundance, the offerings at Enlil's temple, Emesh's harvest boast, Enten's foundation argument, the tablet damage at lines 140–155, the comprehensive agricultural survey (lines 50–280), the parasite accusation, Emesh's heat/ripening counter, Enlil's verdict for Enten, the seasonal reconciliation, the _edubba_ curricular function, the inversion of northern seasonal symbolism, and the comparative material (_Conflictus Veris et Hiemis_, Demeter/Persephone, northern European traditions) is preserved verbatim. Source attributions (ETCSL, Black et al. 2004, Kramer 1961, Civil 1994) are unchanged.
2. **Footnote count and content unchanged.** All footnote macros and their text are preserved verbatim; no footnotes added, removed, or edited. The resolved-marker inference footnote in the `_( … )_` note at the end of the "verdict" section is preserved verbatim.
3. **EVIDENCE and COMPARATIVE-HOOK tokens preserved verbatim** in all positions (22 EVIDENCE tokens and 3 COMPARATIVE-HOOK tokens, unchanged in text and line placement).
4. **Resolved-marker passage untouched.** The italicised inference note `_( … )_` at the end of the "verdict" section (line 65) is preserved verbatim, including its Inference/Risk footnote.
5. **AsciiDoc structure intact:** chapter heading `==`, section headings `===`, section breaks `'''`, italic emphasis (`_edubba_`), italicised editorial inset `_[ … ]_`, and the italicised inference note `_( … )_` are all in place and position. EVIDENCE and COMPARATIVE-HOOK comment lines remain at their original line positions.
6. **Every change logged above.** No silent edits.
