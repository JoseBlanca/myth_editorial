# Grammar-check diff — Chapter 15: Dumuzid's Dream

Stage: 14b grammar-check
Input: `chapters/15-dumuzids-dream.resolved.adoc`
Output: `chapters/15-dumuzids-dream.grammar-checked.adoc`

## Changes

### 1. Long sentence with two nested em-dash asides and a parenthetical split at "and" (background paragraph, line 13)

- Original: `The narrative is set against the background of Inanna's Descent (ETCSL 1.4.1): Dumuzid — the shepherd-god and consort of Inanna — has been marked as Inanna's substitute in the underworld, and the _galla_ demons — underworld demons who enforce the laws of the dead — are coming to seize him.footnote:[ETCSL 1.4.3; Black et al. 2004, pp. 71–72.]`
- Corrected: `The narrative is set against the background of Inanna's Descent (ETCSL 1.4.1): Dumuzid — the shepherd-god and consort of Inanna — has been marked as Inanna's substitute in the underworld. The _galla_ demons — underworld demons who enforce the laws of the dead — are coming to seize him.footnote:[ETCSL 1.4.3; Black et al. 2004, pp. 71–72.]`
- Rationale: The original sentence ran to roughly 52 words and stacked three layered asides — a `(ETCSL 1.4.1)` parenthetical, a `— the shepherd-god and consort of Inanna —` em-dash appositive on Dumuzid, and a `— underworld demons who enforce the laws of the dead —` em-dash appositive on the _galla_ — all in one breath. The skill flags this under "Sentences over 50 words: split or restructure" and "Nested parenthetical asides: flatten". Replacing the comma-plus-`and` pivot with a period splits the sentence into two (~25 and ~19 words), each carrying only one em-dash aside. The footnote remains attached to the second sentence, preserving the citation's original anchor point (the announcement that the _galla_ are coming, which is what is cited). No content added or removed.

### 2. Long sentence with internal semicolon-punctuated em-dash aside split at "and" (comparative section, line 78)

- Original: `Greek tragic literature would pursue this question with sustained intensity — Cassandra sees Troy's destruction and cannot prevent it; Oedipus flees the prophecy and runs directly into its fulfilment — and the structural parallel with Dumuzid's situation is close enough to suggest that the question itself is fundamental to the way human beings think about fate, rather than specific to any one culture.footnote:[Jacobsen 1987, pp. 28–55.]`
- Corrected: `Greek tragic literature would pursue this question with sustained intensity — Cassandra sees Troy's destruction and cannot prevent it; Oedipus flees the prophecy and runs directly into its fulfilment. The structural parallel with Dumuzid's situation is close enough to suggest that the question itself is fundamental to the way human beings think about fate, rather than specific to any one culture.footnote:[Jacobsen 1987, pp. 28–55.]`
- Rationale: The original sentence ran to roughly 66 words and contained an em-dash aside that itself used a semicolon to separate two parallel examples (Cassandra, Oedipus), forcing the reader to hold the main clause open across mixed punctuation. The skill flags both the length (>50 words) and "Three or more subordinate clauses in a single sentence: simplify." Replacing the closing em-dash-plus-`and` with a period closes the aside cleanly and promotes the post-dash matter to its own sentence (~33 and ~33 words). The footnote stays on the second sentence, where the scholarly claim about the structural parallel is located. No content added or removed.

## Not fixed (flagged for human / downstream stages)

- **Source-overview register and length** (paragraphs 1–2) — Paragraphs are dense and academic; per the skill's "What NOT to fix" list, the academic tone of source overviews is a deliberate register choice and is out of scope for grammar-check.
- **Marker-resolved tablet-break block on line 30** (`_[At this point the tablet breaks. . Alster 1972 collates multiple witnesses that fill most gaps..]_`) — Contains a `. .` stray-period artefact and a `..]_` double-dot artefact. Per hard rule 4 ("No content changes to resolved marker passages. These were reviewed and locked.") and hard rule 2 ("No footnote changes") the block is left exactly as received. Flagged for editorial review of marker-resolution artefacts.
- **Marker-resolved inference block on line 44** (`_(The transformation motif — Dumuzid becoming a gazelle, then other forms — may reflect an older stratum of the dying-god tradition in which the deity is literally identified with the animals of the steppe..footnote:[Inference: The animal transformations map onto Dumuzid's pastoral identity.. Risk: ... without specific pastoral-theological significance..])_`) — Contains `..footnote:` (double-dot before footnote), `identity..` and `significance..` (double-dot sentence closers) artefacts in both the lead prose and the footnote body. Per hard rules 2 and 4 the block is left exactly as received. Flagged for editorial review of marker-resolution artefacts.
- **`Alster's monograph identified these formulaic repetitions — the catalogue of transformations, the recurring cycle of flight and discovery — as reflecting oral compositional patterns, the kind of incremental structure that allows a performer to extend or compress a narrative while maintaining its rhythmic architecture.`** (line 46) — Roughly 44 words with one em-dash appositive and a trailing appositive extension (`the kind of...`). Under 50 words and parsable on one read; leaving for line-edit if rhythm adjustment is desired.
- **`He summons his sister Geshtinanna — goddess and sister of Dumuzid, who will later share his time in the underworld — and recounts the dream to her, asking her to interpret it.`** (line 20) — The gloss appositive names Geshtinanna as "sister of Dumuzid" after she has just been named "his sister Geshtinanna" in the same sentence. The redundancy is a marker-resolution gloss artefact; removing one of the two "sister" mentions is a word-choice/gloss-reshape decision and belongs to line-edit.
- **`Dumuzid's hands are changed into gazelle hands — hooves — and his feet into gazelle feet, enabling him to run.`** (line 42) — The inline em-dash gloss (`— hooves —`) is a resolved-gloss stylistic choice; punctuation is correct and the sentence is short. Not fixed.
- **`The scribes who copied this text in the Old Babylonian schools copied it because it mattered — because it said something about death that their culture considered worth preserving.`** (line 80) — `copied ... copied` is an intentional rhetorical repetition, not a grammar error. Not fixed.

## Self-check

- Factual content: unchanged (no proper nouns, dates, line numbers, footnotes, EVIDENCE tokens, or citation strings altered).
- Sentence count: two multi-clause sentences were split into four; overall meaning unchanged.
- Footnote count: unchanged — 24 `footnote:[` instances in both files.
- EVIDENCE tokens: unchanged — 7 `// EVIDENCE:` lines in both files.
- COMPARATIVE-HOOK tokens: unchanged — 3 `// COMPARATIVE-HOOK:` lines in both files.
- Line count: 84 in both files (the two in-prose changes did not add or remove newlines).
- AsciiDoc structure: unchanged — section heading `== Dumuzid's Dream`, all `'''` thematic breaks, all `footnote:[...]` macros, all `_italic_` markers, all `_( ... ..])_` and `_[ ... ..]_` marker-resolution blocks intact.
- All changes logged above; no silent edits.
