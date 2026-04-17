# Grammar-check diff — Chapter 14: Inanna's Descent to the Nether World

Stage: 14b grammar-check
Input: `chapters/14-inannas-descent.resolved.adoc`
Output: `chapters/14-inannas-descent.grammar-checked.adoc`

## Changes

### 1. Long sentence with four coordinated `who`-clauses split at the em-dash (body, Enki's engineered couriers paragraph)

- Original: `The _kurgarra_ and _galatur_ are understood by some scholars as asexual or transgender cultic functionaries, connecting the text to the broader Mesopotamian tradition of liminal ritual personnel — beings who exist between categories, who are neither one thing nor the other, and who therefore can pass through boundaries that would stop anyone with a fixed identity.`
- Corrected: `The _kurgarra_ and _galatur_ are understood by some scholars as asexual or transgender cultic functionaries, connecting the text to the broader Mesopotamian tradition of liminal ritual personnel. These are beings who exist between categories, who are neither one thing nor the other, and who therefore can pass through boundaries that would stop anyone with a fixed identity.`
- Rationale: The original sentence ran to roughly 55 words and piled three coordinated `who`-clauses after an em-dash appositive, which the skill flags under both "Sentences over 50 words: split or restructure" and "Three or more subordinate clauses in a single sentence: simplify." The em-dash was replaced by a period, and the appositive phrase `beings who...` was promoted to a pointer-demonstrative subject (`These are beings who...`). Nothing was added or removed; the referent is explicit because the previous sentence ends on `liminal ritual personnel`. No factual, footnote, or word-choice change.

### 2. Long final sentence in comparative paragraph split at `where` (parallels paragraph)

- Original: `The descent to the land of the dead to retrieve a lost person, the encounter with an implacable ruler of the underworld, the conditions imposed on the return — these elements recur in traditions as distant as the Japanese account of Izanagi's descent to Yomi to retrieve Izanami, where the prohibition against looking, the rotting corpse, and the establishment of death's permanence echo themes found here.`
- Corrected: `The descent to the land of the dead to retrieve a lost person, the encounter with an implacable ruler of the underworld, the conditions imposed on the return — these elements recur in traditions as distant as the Japanese account of Izanagi's descent to Yomi to retrieve Izanami. There, the prohibition against looking, the rotting corpse, and the establishment of death's permanence echo themes found here.`
- Rationale: The original sentence was roughly 65 words and stacked a three-item list, an em-dash clause, and a following `where`-clause containing a second three-item list. The skill flags both the length (>50 words) and the multiple-subordinate-clause structure. Replacing the comma-plus-`where` pivot with a period-plus-`There,` splits it into two readable sentences (~45 words and ~26 words) while keeping the same anaphoric reference to the Japanese account. No content added or removed.

## Not fixed (flagged for human / downstream stages)

- **Source-overview register and length** (paragraphs 1–5) — Paragraphs are dense and academic; per the skill's "What NOT to fix" list, the academic tone of source overviews is a deliberate register choice and is out of scope for grammar-check.
- **Long nested-parenthetical sentence at "Inanna specifies the order of appeal..."** — Roughly 70 words and uses em-dash asides plus a parenthetical `(Sumerian: Nibru)` plus a trailing appositive `the religious capital of Sumer`. The three-item structure is clearly delimited by semicolons, so the reader does not have to re-parse; restructuring would require additional connective wording (word choice), which belongs to line-edit. Flagged for line-edit.
- **Appositive redundancy at "The _galla_ demons — the _galla_, underworld demons who enforce the laws of the dead — accompany Inanna..."** — The em-dash aside re-names the just-named subject, a marker-resolution artefact left from stage 13 gloss insertion. Fixing it cleanly requires a word-choice decision (drop one instance of "the _galla_", or reshape the gloss). Flagged for line-edit.
- **Sentence fragment "ETCSL 1.4.1, \"snake\" transformation in some manuscripts.footnote:[...]"** — The leading prose is a fragment produced by marker resolution. The attached footnote contains double-dot and nested-quote artefacts. Because the clause and its footnote are part of a resolved variant-manuscript marker (parallel to the `_[An alternate tradition gives...]_` pattern elsewhere in the book) and because the skill's hard rules forbid footnote modification and content changes to resolved-marker passages, it is left untouched. Flagged for line-edit or editorial review.
- **Apparent duplication between unlocked prose (paragraph ending "...whether her motivation is left deliberately ambiguous.") and the immediately following locked inference block (`_(Whether Inanna's stated reason — funeral rites for Gugalanna...)_`)** — The two passages carry overlapping content. Removing the duplication is a content/style decision, not a grammar fix. Flagged for line-edit.
- **`Dumuzid, in the time that his consort — his wife, the goddess who chose him — was dead on a hook in the underworld, dressed himself magnificently...`** — ~40 words with a nested appositive inside a subordinate temporal clause. Under 50 words and parsable on one read; leaving for line-edit if rhythm adjustment is desired.
- **`As psychological drama, it traces the intersecting trajectories of four distinct characters — Inanna's ambition, Ereshkigal's rage and suffering, Dumuzid's complacency, Geshtinanna's selflessness — each of whom acts...`** — The em-dash list names traits, but `each of whom` refers to the four characters named before the em-dash. The possessive forms link the two, so the construction is grammatical; tightening it would be word-choice work.
- **Marker-resolved passages** (lines 50, 84, 135, 179, 188, 201, 213) — contain `..footnote:[...]`, `..])_`, and `_[... ..]_` double-dot artefacts, nested double quotes, and leading-period fragments. Per hard rules 2 and 4 ("No footnote changes" and "No content changes to resolved marker passages"), these were left exactly as received.
- **Singular/plural "eye(s) of death"** — `"eyes of death"` (plural, line with the seven Annunaki judges) versus `"eye of death"` (singular, line where Inanna casts it on Dumuzid). This is textually correct, not a grammar error: multiple judges multiple eyes, one goddess one eye. Not fixed.

## Self-check

- Factual content: unchanged (no proper nouns, dates, line numbers, footnotes, EVIDENCE tokens, or citation strings altered).
- Sentence count: two multi-clause sentences were split into four; overall meaning unchanged.
- Footnote count: unchanged — 54 `footnote:[` instances in both files.
- EVIDENCE tokens: unchanged — 60 `// EVIDENCE:` lines in both files.
- COMPARATIVE-HOOK tokens: unchanged — 5 `// COMPARATIVE-HOOK:` lines in both files.
- Line count: 231 in both files (the two in-prose changes did not add or remove newlines).
- AsciiDoc structure: unchanged — section heading `== Inanna's Descent to the Nether World`, all `'''` thematic breaks, all `footnote:[...]` macros, all `_italic_` markers, all `_( ... ..])_` and `_[ ... ..]_` marker-resolution blocks intact.
- All changes logged above; no silent edits.
