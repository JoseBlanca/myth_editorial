# Grammar-check diff: Chapter 21 - Gilgamesh and Huwawa

Input: `21-gilgamesh-and-huwawa.resolved.adoc`
Output: `21-gilgamesh-and-huwawa.grammar-checked.adoc`

Changes logged below in "original → corrected" format with rationale. Changes restricted to grammar, punctuation, and readability (per stage 14b rules). No factual, stylistic, footnote-content, or AsciiDoc-structural changes.

---

## 1. Line 28 — misplaced prepositional phrase (dangling modifier)

**Original:**
> He seeks and receives the approval of the sun god Utu, who has jurisdiction over the Cedar Mountain as a foreign land, for the expedition.

**Corrected:**
> For the expedition, he seeks and receives the approval of the sun god Utu, who has jurisdiction over the Cedar Mountain as a foreign land.

**Rationale:** In the original, the prepositional phrase "for the expedition" attaches to "the approval" but is separated from it by a 15-word relative clause ("who has jurisdiction... as a foreign land"). The reader, on first pass, is apt to parse "for the expedition" as modifying "foreign land" (a foreign land for the expedition), or as a free-floating dangler. Moving the prepositional phrase to sentence-initial position re-anchors it to the verb phrase "seeks and receives the approval... for the expedition" and eliminates the ambiguous attachment. No change in meaning; no lexical change.

---

## 2. Line 40 — ambiguous pronoun reference ("who wields") plus nested parenthetical

**Original:**
> Huwawa (not Humbaba, which is the later Akkadian form of the name) is the fearsome guardian of the Cedar Forest, appointed by Enlil -- king of the gods, lord of wind and command, supreme authority in Nippur (Sumerian: Nibru) -- who wields seven supernatural terrors.

**Corrected:**
> Huwawa (not Humbaba, which is the later Akkadian form of the name), who wields seven supernatural terrors, is the fearsome guardian of the Cedar Forest, appointed by Enlil -- king of the gods, lord of wind and command, supreme authority in Nippur (Sumerian: Nibru).

**Rationale:** Two overlapping issues. (a) Ambiguous pronoun reference: the relative clause "who wields seven supernatural terrors" is placed immediately after "Nippur (Sumerian: Nibru)" and inside the dash-offset appositive for Enlil. By proximity it attaches to Enlil (or worse, to Nibru); by sense it should attach to Huwawa, whose seven auras are the subject of the following sentences. (b) Nested parentheticals: the original threads a parenthesis ("(not Humbaba...)") inside the main clause and then a dash-offset appositive ("-- king of the gods... --") containing a further parenthesis ("(Sumerian: Nibru)"), with the "who wields" relative clause dangling off the end of the nest. Moving "who wields seven supernatural terrors" adjacent to its antecedent "Huwawa" fixes the referential ambiguity, and placing it before the "is the fearsome guardian..." spine removes the dangling tail from the Enlil appositive. The Enlil appositive remains a single dash-offset unit with one internal parenthesis — no longer nested with a trailing clause. Factual content (Huwawa wields the terrors; Enlil appointed him) preserved exactly.

---

## 3. Line 51 — double periods inside italic editorial bracket note (damage summary)

**Original:**
> _[At this point the tablet breaks. Lines 140–160 of Version A contain significant manuscript variation, with different manuscripts preserving different gift-offering sequences. The general trick-and-surrender pattern is secure, but specific content varies between manuscripts.. Overlapping manuscripts for Version A allow reconstruction of most gaps; the aura-surrender trick is secure but individual offerings vary by manuscript..]_

**Corrected:**
> _[At this point the tablet breaks. Lines 140–160 of Version A contain significant manuscript variation, with different manuscripts preserving different gift-offering sequences. The general trick-and-surrender pattern is secure, but specific content varies between manuscripts. Overlapping manuscripts for Version A allow reconstruction of most gaps; the aura-surrender trick is secure but individual offerings vary by manuscript.]_

**Rationale:** Two doubled-period typos (`manuscripts..` and `manuscript..`) reduced to single periods. The bracketed block is an editorial damage note in running italic prose (not a `footnote:[]` macro), so routine punctuation correction applies. Consistent with chapter 19 grammar-diff #3 and chapter 20 grammar-diff #1. No content change.

---

## 4. Line 94 — double periods inside italic editorial bracket note (damage summary)

**Original:**
> _[At this point the tablet breaks. The central section of Version B (approximately lines 80–110), emphasising fear and hesitation before the forest, is partially broken. Fewer manuscripts for Version B leave some lines unrestored.. Partial; the general tenor of the passage is clear, but specific lines remain uncertain..]_

**Corrected:**
> _[At this point the tablet breaks. The central section of Version B (approximately lines 80–110), emphasising fear and hesitation before the forest, is partially broken. Fewer manuscripts for Version B leave some lines unrestored. Partial; the general tenor of the passage is clear, but specific lines remain uncertain.]_

**Rationale:** Same class of error as change 3: two doubled-period typos (`unrestored..` and `uncertain..`) reduced to single periods. Editorial bracket note in running prose, not a `footnote:[]` macro. No content change.

---

## 5. Line 102 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(Version B presumably concluded with a similar decapitation, given the parallel narrative structure, but this section is not preserved in the surviving text — Version B breaks off before the decapitation scene..footnote:[Inference: Parallel narrative structure with Version A.. Risk: The ending may have differed..])_

**Corrected:**
> _(Version B presumably concluded with a similar decapitation, given the parallel narrative structure, but this section is not preserved in the surviving text — Version B breaks off before the decapitation scene.footnote:[Inference: Parallel narrative structure with Version A.. Risk: The ending may have differed..])_

**Rationale:** Doubled sentence-terminating period (`scene..`) immediately before the `footnote:[...]` macro reduced to a single period. Same class of error fixed in chapter 19 grammar-diff #2 and chapter 20 grammar-diff #3. The double periods *inside* the footnote interior (`Version A..`, `differed..`) are left untouched per hard rule 2 (no footnote changes).

---

## 6. Line 104 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(Version B presumably concluded with a similar scene of Enlil's anger, as in Version A, but the ending of Version B is broken and this section is not preserved..footnote:[Inference: Parallel narrative structure with Version A.. Risk: The ending may have differed..])_

**Corrected:**
> _(Version B presumably concluded with a similar scene of Enlil's anger, as in Version A, but the ending of Version B is broken and this section is not preserved.footnote:[Inference: Parallel narrative structure with Version A.. Risk: The ending may have differed..])_

**Rationale:** Same class of error as change 5: doubled sentence-terminating period (`preserved..`) before the `footnote:[...]` macro reduced to one. Double periods *inside* this footnote's interior (`Version A..`, `differed..`) left untouched per hard rule 2.

---

## 7. Line 118 — 57-word sentence with long dash-offset tail split into two

**Original:**
> But the Sumerian versions, composed during the Old Babylonian period and copied in schools across Mesopotamia, may be the earliest literary instances in which the question is posed with this degree of moral complexity -- where the hero wins, the guardian weeps, the god is angry, and the text refuses to tell us who was right.

**Corrected:**
> But the Sumerian versions, composed during the Old Babylonian period and copied in schools across Mesopotamia, may be the earliest literary instances in which the question is posed with this degree of moral complexity. In them the hero wins, the guardian weeps, the god is angry, and the text refuses to tell us who was right.

**Rationale:** The original sentence runs 57 words (over the 50-word threshold). The structure is main clause (39 words, itself containing a participial parenthetical "composed during the Old Babylonian period and copied in schools across Mesopotamia" and a relative clause "in which the question is posed with this degree of moral complexity") followed by a dash-offset four-item parallel tail. Split at the em-dash boundary: the first sentence carries the claim (~37 words), the second the four-part illustrative tail ("In them..." replacing the original dash + "where" connector, ~20 words). The pronoun "them" unambiguously refers to "the Sumerian versions" (plural antecedent, no competing plural). Factual content preserved verbatim; rhetorical sequencing preserved (claim, then illustration).

---

## Sentences reviewed for length/complexity but NOT changed

The following long or clause-heavy sentences were evaluated against the >50-word / 3+-subordinate-clause / nested-parenthetical tests and judged clear enough to retain as written. Logged here so the human can spot-check:

- Line 3: "The story of Gilgamesh's expedition to the Cedar Forest survives in two independent Sumerian compositions: Version A (ETCSL 1.8.1.5, approximately 202 lines) and Version B (ETCSL 1.8.1.5.1, approximately 168 extant lines with additional gaps)." (~34 words; two parallel citation parentheticals, list structure, reads as enumeration).
- Line 7: "Version A is the longer and better preserved, one of the best-attested Gilgamesh poems in the Old Babylonian scribal curriculum, with more surviving copies than nearly any other Gilgamesh composition." (~31 words; single appositive chain, clear).
- Line 12: "George devotes extensive discussion to distinguishing these two Sumerian versions from each other and from the Akkadian Cedar Forest episode (Tablets IV–V of the Standard Babylonian Gilgamesh epic), demonstrating that all three are independent literary treatments of a shared tradition." (~40 words; one embedded parenthetical, one participial tail, clear).
- Line 19: "Gilgamesh (Sumerian: Bilgames), king of Uruk (Sumerian: Unug), announces his determination to journey to the Cedar Forest and establish a lasting name, explicitly citing mortality as his motivation: since death is inevitable, fame is the only enduring legacy." (~38 words; two short gloss parentheticals in apposition, colon-introduced summary).
- Line 40 (after change 2): "These terrors are manifestations of _me-lam_ -- the terrifying divine radiance that emanates from gods, monsters, and sacred objects -- the same category of supernatural power that inheres in kings and sacred objects throughout Sumerian literature." (~36 words; single dash-offset gloss, clear).
- Line 48: "The trick works because each gift appears generous, and Huwawa, accepting, gives away in return one layer of the divine radiance that makes him invulnerable." (~26 words; clear).
- Line 74: "The supreme god of the Sumerian pantheon takes the radiance that Gilgamesh tricked away and scatters it across the landscape, as though to ensure that the terror Huwawa once embodied will persist, distributed now among the natural forces of the world rather than concentrated in a single guardian." (~48 words; three subordinate clauses but each short and sequential, parses linearly on first reading; splitting would fracture the cause-and-consequence arc from "scatters" to "persist, distributed").
- Line 96: "The guardian of the Cedar Forest, the being who wielded seven auras of divine radiance, whose very presence was designed to make the forest unapproachable -- this being cries, and asks to be spared." (~33 words; two appositives setting up the dash-offset subject "this being", rhetorical cadence preserved).
- Line 112: "The two versions share the same narrative kernel -- journey, confrontation, trick, decapitation, Enlil's anger -- but differ in emphasis: Version A foregrounds the cleverness of the trick with the auras and the ethical ambiguity of the killing; Version B foregrounds the psychological experience of fear and the pathos of Huwawa's helplessness." (~52 words; borderline over 50, but structured as a symmetric semicolon-joined parallel — "Version A foregrounds X; Version B foregrounds Y" — after a colon. Splitting would break the paired comparison that is the sentence's whole point, and each sub-clause is itself well under 20 words).

After the changes above, no remaining sentence exceeds the 50-word threshold except line 112 (retained by design). No remaining nested parentheticals. No subject-verb, tense, or article errors identified.

---

## Items deliberately NOT fixed (per hard rules)

- Double periods *inside* `footnote:[...]` interiors on lines 77, 102, and 104 (e.g., `Mesopotamian landscape..`, `punishment of the heroes..`, `narrative structure with Version A..`, `ending may have differed..`) — hard rule 2 forbids footnote changes.
- Line 77 oddity: `_(.footnote:[...])_` — the leading `.` immediately after the opening italic-paren is unusual (the stray period appears to be a marker-resolve artefact, possibly a stranded sentence terminator for an elided main clause). The construct is an AsciiDoc macro sequence inside italic markup; touching it risks changing marker-resolved content and AsciiDoc parsing. Flagged for line-edit / human review rather than altered here. (Hard rules 4 and 5.)
- Repetition "gods, monsters, and sacred objects... kings and sacred objects" (line 40): word-choice redundancy, deferred to line-edit.
- "suggests is not the same as preserves" (line 106) — a stylistic repetition-with-a-twist; grammatically correct, rhetorically intentional, deferred to line-edit.
- Register and word choice across the chapter (e.g., "guardianly", "pitiless and perfectly clear", "pitiful") — deferred to line-edit (stage 15).

---

## Self-check

1. Factual content: unchanged. No claim about texts, dates, people, places, or events was altered.
2. Footnote count: unchanged (26 `footnote:[...]` macros in input and output; interior text preserved verbatim).
3. EVIDENCE tokens: unchanged (29 `// EVIDENCE:` comments, identical).
4. AsciiDoc structure: unchanged (`== Gilgamesh and Huwawa: The Cedar Forest` heading, three `=== ...` sub-headings, four `'''` section breaks, four `// COMPARATIVE-HOOK:` comments, italic markup `_..._`, em-dashes `--` and `—` all preserved).
5. Every change is logged above. No silent changes.
