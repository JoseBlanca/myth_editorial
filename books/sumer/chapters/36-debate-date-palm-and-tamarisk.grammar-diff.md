# Grammar-check diff — Chapter 36: The Debate between Date Palm and Tamarisk

Source: `36-debate-date-palm-and-tamarisk.resolved.adoc`
Output: `36-debate-date-palm-and-tamarisk.grammar-checked.adoc`

Every mechanical change below is logged with the original text, the corrected text, and the rationale. Word choice, rhythm, nominalizations, footnote content, resolved-marker passages, and AsciiDoc structure were left untouched per the skill's "What NOT to fix" list.

---

## Change 1 — Opening paragraph, dangling modifier after em-dash

**Original:**
> The composition known as "The Debate between Date Palm and Tamarisk" is catalogued as ETCSL 5.3.7 and survives on a single witness tablet, Sb 12354 (CDLI P357265), from Susa -- published by Cavigneaux in 2003.footnote:[ETCSL 5.3.7, bibliography.]

**Corrected:**
> The composition known as "The Debate between Date Palm and Tamarisk" is catalogued as ETCSL 5.3.7 and survives on a single witness tablet, Sb 12354 (CDLI P357265), from Susa. The tablet was published by Cavigneaux in 2003.footnote:[ETCSL 5.3.7, bibliography.]

**Rationale:** The past-participial phrase "published by Cavigneaux in 2003" dangles at the end of an em-dash aside attached to a sentence whose main subject is "The composition"; a reader cannot tell on first pass whether the composition, the tablet, or Susa was what Cavigneaux published. Splitting into a separate sentence with an explicit subject ("The tablet was published...") removes the ambiguity. Factual content, citation, and footnote placement unchanged.

---

## Change 2 — Second paragraph, run-on with two independent inferences

**Original:**
> The composition is catalogued among the debate poems and survives in a fragmentary state, with fewer copies than the major debate poems, indicating more limited circulation in Old Babylonian scribal schools.footnote:[ETCSL 5.3.7, composite text, fragmentary; Black et al. 2004, pp. 244--246.]

**Corrected:**
> The composition is catalogued among the debate poems and survives in a fragmentary state. Fewer copies survive than for the major debate poems, indicating more limited circulation in Old Babylonian scribal schools.footnote:[ETCSL 5.3.7, composite text, fragmentary; Black et al. 2004, pp. 244--246.]

**Rationale:** The original piles three ideas onto one subject ("is catalogued", "survives in a fragmentary state", "with fewer copies...indicating...") with three stacked modifying phrases — a readability violation under "three or more subordinate clauses in a single sentence". Splitting produces a clean factual sentence followed by the comparative-inference sentence. The "with fewer copies than the major debate poems" phrase is rewritten as its own clause ("Fewer copies survive than for the major debate poems") so the absolute-phrase modifier "indicating..." attaches unambiguously. No facts or footnote content changed.

---

## Change 3 — Third paragraph, em-dash used where colon is grammatically cleaner

**Original:**
> The debate stages a tension between cultivated and wild nature -- between the domesticated tree that provides fruit, syrup, and fibre, and the wild tree that grows without human care and serves ritual and practical functions.footnote:[ETCSL 5.3.7, surviving lines; Black et al. 2004, pp. 244--245.]

**Corrected:**
> The debate stages a tension between cultivated and wild nature: between the domesticated tree that provides fruit, syrup, and fibre, and the wild tree that grows without human care and serves ritual and practical functions.footnote:[ETCSL 5.3.7, surviving lines; Black et al. 2004, pp. 244--245.]

**Rationale:** The sentence uses an em-dash to introduce an appositive "between..." phrase that explains — rather than interrupts — the preceding noun. A colon better signals the expository relationship and avoids visual confusion later in the same paragraph sequence where em-dashes carry genuine interruption duty. Punctuation-only change; no words added or removed; meaning identical.

---

## Change 4 — Penultimate section, garden-path sentence with misplaced em-dash aside

**Original:**
> The composition belongs to a broader Ancient Near Eastern tree-debate tradition that includes Akkadian parallels -- debates between trees, cultivated versus wild, productive versus ornamental, appear in later Akkadian wisdom literature, suggesting a deep and persistent literary lineage.footnote:[Black et al. 2004, pp. 244--246; Kramer 1961, pp. 72--73.]

**Corrected:**
> The composition belongs to a broader Ancient Near Eastern tree-debate tradition that includes Akkadian parallels. Debates between trees -- cultivated versus wild, productive versus ornamental -- appear in later Akkadian wisdom literature, suggesting a deep and persistent literary lineage.footnote:[Black et al. 2004, pp. 244--246; Kramer 1961, pp. 72--73.]

**Rationale:** In the original, the em-dash looks like it opens an appositive on "Akkadian parallels", but the clause that follows has its own subject and verb ("debates... appear in later Akkadian wisdom literature"), making this effectively a run-on sentence that a reader must back up to parse. Split into two sentences: the first states the claim; the second describes the Akkadian parallels. The inner pair ("cultivated versus wild, productive versus ornamental") becomes a proper parenthetical aside set off by em-dashes within the second sentence, matching its grammatical role as a modifier of "between trees". Citation and footnote unchanged.

---

## Self-check

1. **No factual content changed.** Every named composition, tablet number, line count, author citation, date, page range, and claim appears identically in both versions. The only lexical additions are "The tablet was" (Change 1) and "survive than for" (Change 2), which restore grammatical subjects and predicates after splitting; and "Debates" capitalised as the new sentence head (Change 4).
2. **Footnote count and content unchanged.** All eight inline `footnote:[...]` calls and all nine `EVIDENCE` comments appear in the same order and with identical text.
3. **AsciiDoc structure intact.** Section heading (`==`), subsection headings (`===`), thematic breaks (`'''`), italicised inline markup (`_..._`), bracketed marker-resolved passages, and `COMPARATIVE-HOOK` / `EVIDENCE` comments are unchanged.
4. **Resolved-marker passages untouched.** The two bracketed "tablet breaks" paragraphs and the italicised inference paragraph (`_(The cultivated-vs-wild opposition...)_`) are byte-for-byte identical to the source.
5. **No silent changes.** Every modification is listed above.

## Items considered and not changed

- "Date Palm argues its superiority on the grounds of its immense economic value: it provides dates -- a dietary staple -- date syrup, palm wine, fibre for rope-making, and wood for construction, making it the most productive tree in the Mesopotamian landscape." (43 words) — the colon introduces a coherent list; the inner em-dash aside on "a dietary staple" is a single, shallow parenthetical; under 50 words; reads cleanly in one pass.
- "The claim is not merely that Date Palm is useful but that Date Palm is civilised: it exists because human beings chose to plant it, water it, and tend it, and the products it yields are the products of that partnership between tree and cultivator." (46 words) — the "not merely...but that..." scaffold is a single logical unit; the post-colon expansion is an anaphoric parallel series ("plant it, water it, and tend it") that would lose its rhetorical cadence if broken. Under 50 words; grammatically clean.
- "Tamarisk counters by emphasising its hardiness, its independence from human cultivation, and its ritual purity -- the tamarisk is used in purification rites and its wood serves as fuel and building material." — the em-dash here introduces an explanatory extension, not a nested aside; reads cleanly.
- "But the question itself -- whether civilisation's dependence on human labour is a strength or a vulnerability, whether self-sufficiency counts for more than productivity -- is one that has not lost its force." — the em-dash aside holds a two-part appositive that parallels the sentence's noun ("the question"); readable in one pass; under 50 words.
- The final paragraph's three comparative sentences ("The same tension appears in the Greek tradition...", "It appears in the Hebrew Bible...", "It is a question that the first agriculturalists posed...") — grammatically clean; the anaphoric "It appears..." / "It is..." pattern is deliberate parallelism, which is line-edit's territory.
- Serial commas, em-dash vs. hyphen vs. en-dash usage, apostrophes in Sumerian terms (_gišimmar_, _šinig_, _edubba_), and italics conventions are already consistent.
- The academic register of the opening source overview is preserved per the skill's "What NOT to fix" list (deliberate register choice).
