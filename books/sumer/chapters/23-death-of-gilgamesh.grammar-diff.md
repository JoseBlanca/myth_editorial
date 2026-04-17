# Grammar-check diff: Chapter 23 — The Death of Gilgamesh

Input: `23-death-of-gilgamesh.resolved.adoc`
Output: `23-death-of-gilgamesh.grammar-checked.adoc`

Changes logged below in "original → corrected" format with rationale. Changes restricted to grammar, punctuation, and readability (per stage 14b rules). No factual, stylistic, footnote-content, or AsciiDoc-structural changes.

---

## 1. Line 12 — double periods inside italic editorial bracket note (damage summary)

**Original:**
> _[At this point the tablet breaks. The Nippur manuscripts are extensively damaged, with multiple large gaps throughout. Funeral preparations and underworld reception sequences are heavily broken.. Partial; the Tell Haddad version provides significant new material not available from Nippur witnesses, but the two versions do not fully overlap, leaving substantial gaps in both..]_

**Corrected:**
> _[At this point the tablet breaks. The Nippur manuscripts are extensively damaged, with multiple large gaps throughout. Funeral preparations and underworld reception sequences are heavily broken. Partial; the Tell Haddad version provides significant new material not available from Nippur witnesses, but the two versions do not fully overlap, leaving substantial gaps in both.]_

**Rationale:** Two doubled-period typos (`heavily broken..` and `leaving substantial gaps in both..`) reduced to single periods. The bracketed block is an editorial damage note in running italic prose (not a `footnote:[]` macro), so routine punctuation correction applies. Consistent with chapter 19 grammar-diff #3, chapter 20 grammar-diff #1, chapter 21 grammar-diff #3/#4, and chapter 22 grammar-diff #4/#6. No content change.

---

## 2. Line 14 — double periods inside italic editorial bracket note (damage summary)

**Original:**
> _[At this point the tablet breaks. Ritual content in the Tell Haddad version (columns ii–iv) is partially damaged. The divine judgement scene is incomplete.. None; the Tell Haddad version is the only witness for its distinctive ritual content..]_

**Corrected:**
> _[At this point the tablet breaks. Ritual content in the Tell Haddad version (columns ii–iv) is partially damaged. The divine judgement scene is incomplete. None; the Tell Haddad version is the only witness for its distinctive ritual content.]_

**Rationale:** Same class of error as change 1. Two doubled-period typos (`incomplete..` and `distinctive ritual content..`) reduced to single periods. Editorial bracket note in running prose, not a `footnote:[]` macro. No content change.

---

## 3. Line 35 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(The divine decree against Gilgamesh's immortality echoes the theme expressed in other Sumerian Gilgamesh compositions -- particularly Gilgamesh and Huwawa -- that fame, not eternal life, is the only compensation for mortality..footnote:[Inference: The thematic continuity across the Sumerian Gilgamesh poems is widely noted by scholars.. Risk: Given the fragmentary state of the text, the precise formulation of the decree and its relationship to other compositions cannot be fully established..])_

**Corrected:**
> _(The divine decree against Gilgamesh's immortality echoes the theme expressed in other Sumerian Gilgamesh compositions -- particularly Gilgamesh and Huwawa -- that fame, not eternal life, is the only compensation for mortality.footnote:[Inference: The thematic continuity across the Sumerian Gilgamesh poems is widely noted by scholars.. Risk: Given the fragmentary state of the text, the precise formulation of the decree and its relationship to other compositions cannot be fully established..])_

**Rationale:** Doubled sentence-terminating period (`mortality..`) immediately before the `footnote:[...]` macro reduced to a single period. Same class of marker-resolve punctuation artefact fixed in chapter 19 grammar-diff #2, chapter 20 grammar-diff #3, chapter 21 grammar-diff #5/#6, and chapter 22 grammar-diff #2/#3/#7. The double periods *inside* the footnote interior (`widely noted by scholars..`, `fully established..`) are left untouched per hard rule 2 (no footnote changes).

---

## 4. Line 44 — overlong sentence (62 words) with cascading em-dash appositives

**Original:**
> The Tell Haddad version preserves substantially more detail about the funerary ritual: offerings are presented to major underworld deities including Ereshkigal -- queen of the underworld, elder sister of Inanna -- Ningishzida -- god of the underworld, a judge among the dead -- and other divine figures, in what appears to be a formal protocol for the reception of a dead king.

**Corrected:**
> The Tell Haddad version preserves substantially more detail about the funerary ritual. Offerings are presented to major underworld deities -- Ereshkigal, queen of the underworld and elder sister of Inanna; Ningishzida, god of the underworld and a judge among the dead; and other divine figures -- in what appears to be a formal protocol for the reception of a dead king.

**Rationale:** Two overlapping issues. (a) The original sentence runs 62 words, above the 50-word threshold. (b) The enumeration of deities uses cascading em-dash appositives (`Ereshkigal -- [gloss] -- Ningishzida -- [gloss] -- and other divine figures`) where the medial em-dash between "Inanna" and "Ningishzida" functions ambiguously (closing Ereshkigal's appositive *and* opening the Ningishzida item). On first reading the eye is liable to mis-track which dash pair belongs to which deity.

Split the original at the colon into two sentences: the first states the claim (12 words), the second presents the list (48 words). Within the list, regularised the cascading em-dashes to a single em-dash-delimited block whose interior uses semicolons to separate the three list items ("Ereshkigal, X; Ningishzida, Y; and other divine figures"). Each deity's gloss is given as a comma-appositive within its list item, with the two sub-glosses joined by "and" rather than by an internal comma, which eliminates the earlier ambiguity about whether "elder sister of Inanna" and "a judge among the dead" are sub-appositives or coordinate items. Sentence-final `-- in what appears to be a formal protocol...` retains its original dash-offset framing.

Factual content preserved exactly: same three list elements (Ereshkigal with her two epithets, Ningishzida with his two epithets, "and other divine figures"), same framing phrase, same footnote attachment. No lexical additions except the coordinating "and" joining each deity's paired epithets (replacing the interior comma that previously joined them).

---

## 5. Line 58 — double period before `footnote:[...]` macro in italic parenthetical note

**Original:**
> _(The elevation of Gilgamesh to underworld judge functions as a form of apotheosis -- a partial divinisation that grants the dead hero a role surpassing that of ordinary mortals while still confining him to the nether world..footnote:[Inference: George 2003 identifies this elevation as consistent with the Sumerian cult of dead kings, in which deceased rulers received ongoing offerings and were treated as semi-divine intercessors.. Risk: The fragmentary state of the text means the precise nature and extent of Gilgamesh's underworld authority cannot be fully determined..])_

**Corrected:**
> _(The elevation of Gilgamesh to underworld judge functions as a form of apotheosis -- a partial divinisation that grants the dead hero a role surpassing that of ordinary mortals while still confining him to the nether world.footnote:[Inference: George 2003 identifies this elevation as consistent with the Sumerian cult of dead kings, in which deceased rulers received ongoing offerings and were treated as semi-divine intercessors.. Risk: The fragmentary state of the text means the precise nature and extent of Gilgamesh's underworld authority cannot be fully determined..])_

**Rationale:** Same class of error as change 3. Doubled sentence-terminating period (`nether world..`) before the `footnote:[...]` macro reduced to one. Double periods *inside* this footnote's interior (`semi-divine intercessors..`, `fully determined..`) are left untouched per hard rule 2.

---

## Sentences reviewed for length/complexity but NOT changed

The following long or clause-heavy sentences were evaluated against the >50-word / 3+-subordinate-clause / nested-parenthetical tests and judged clear enough (or stylistically essential enough) to retain as written. Logged here so the human can spot-check:

- Line 8: "The text survives in two co-equal witnesses: a Nippur version known from fragmentary Old Babylonian tablets, and a Tell Haddad version published and analysed by George." (~28 words; colon-introduced two-part parallel appositive, clear).
- Line 8 (final sentence): "The discovery of the Tell Haddad tablets significantly expanded scholarly knowledge of this composition, adding ritual and funerary content not attested in the Nippur fragments." (~25 words; single participial tail, clear).
- Line 20: "The composition ETCSL 1.8.1.3 narrates the death of Gilgamesh (Sumerian: Bilgames) -- king of Uruk who confronts his mortality and is received as a judge among the dead -- and his reception in the nether world." (~36 words; short glossing parenthetical `(Sumerian: Bilgames)` followed by a single dash-offset appositive whose restrictive relative clause names the two key actions of the composition. Same structural pattern as chapter 22 line 20 which was retained; not truly nested because the parenthetical closes before the dash-offset opens).
- Line 29 (opening): "Gilgamesh, having achieved great deeds during his life, is confronted with the inevitability of his own death -- the gods have decreed that even the greatest hero must die." (~30 words; one participial opener plus dash-offset gloss with one subordinate `that`-clause, clear).
- Line 29 (second sentence): "Gilgamesh has slain Huwawa in the Cedar Forest, has crossed mountains and rivers, has done everything that a mortal can do to distinguish himself -- and none of it changes the fundamental arithmetic." (~33 words; three parallel perfect-tense predicates with polysyndetic dash-offset tail, rhetorical tricolon, parses linearly).
- Line 32: "The text appears to include a dream or divine communication in which Gilgamesh is told that immortality is not granted to mortals, however great their accomplishments -- the gods have reserved eternal life for themselves." (~35 words; one `in which`-relative clause containing one `that`-complement, dash-offset paraphrase; clear).
- Line 35 (after change 3, the resolved-marker `_(...)_` block): "The divine decree against Gilgamesh's immortality echoes the theme expressed in other Sumerian Gilgamesh compositions -- particularly Gilgamesh and Huwawa -- that fame, not eternal life, is the only compensation for mortality." (~32 words; one dash-offset gloss plus one sentence-level `that`-clause; clear).
- Line 44 (after change 4, the `The ritual follows a sequence` sentence): "The ritual follows a sequence -- deity by deity, gift by gift -- that suggests a well-established liturgical tradition." (~19 words; clear).
- Line 47: "Gilgamesh presents gifts to the underworld deities -- a ritual sequence that parallels the gift-giving protocols attested in other Sumerian literary and liturgical texts concerning the nether world." (~28 words; single dash-offset appositive with one restrictive relative clause, clear).
- Line 52: "After death, Gilgamesh is received in the nether world not as an ordinary shade but as a figure of authority: he is granted the status of a judge among the dead." (~31 words; `not X but Y` balanced construction, colon-introduced restatement, clear).
- Line 52 (third sentence): "Less, because Gilgamesh is still dead -- he does not return to the world of the living, does not sit among the gods in heaven." (~26 words; elliptical `Less, because ...` paralleled by the next sentence `More, because ...`, dash-offset elaboration of "still dead"; intentional rhetorical parallelism, clear).
- Line 55: "Gilgamesh's elevation to judge of the dead places him alongside Ningishzida and other underworld deities, transforming him from a mortal hero into a figure with a permanent divine function in the afterlife." (~32 words; single participial tail, clear).
- Line 55 (second sentence): "In life, he was two-thirds divine and one-third mortal -- a fraction that made him the greatest of heroes but did not save him from the arithmetic of death." (~30 words; single dash-offset appositive with balanced `but` contrast, clear).
- Line 55 (fourth sentence): "Death took everything from him except his merit, and his merit has earned him a role that will last as long as the dead keep coming -- which is to say, forever." (~32 words; semicolon-style `-- which is to say` gloss; two main clauses joined by `and`, each with one embedded clause; parses linearly).
- Line 58 (after change 5): "The elevation of Gilgamesh to underworld judge functions as a form of apotheosis -- a partial divinisation that grants the dead hero a role surpassing that of ordinary mortals while still confining him to the nether world." (~36 words; one dash-offset gloss with a restrictive relative + concessive `while`-participial; clear).
- Line 66: "The composition's eschatological function is to assert that even for the greatest hero, death is absolute -- but that extraordinary merit can earn an elevated status within death's domain, as a judge and authority among the dead rather than a mere shade." (~42 words; balanced dash-offset second `that`-clause parallel to the first, `not X but Y` at the item level echoed at the clause level; reads as a single deliberate balanced proposition).
- Line 69: "The royal-legitimation function is significant: by showing Gilgamesh received as a divine judge in the nether world, the text legitimises the cult of dead kings and the ongoing ritual obligations of the living toward deceased rulers." (~36 words; colon-introduced `by -ing` gerundial adjunct leading into the main clause, coordinate double object, clear).
- Line 69 (final sentence): "If Gilgamesh exercises divine authority in the underworld, then all dead kings participate in that reflected authority, and the living owe them something -- offerings, rituals, the ongoing maintenance of their cult." (~31 words; single `if-then` conditional plus coordinate `and`, dash-offset tricolon tail, clear).
- Line 78: "His people prepared his funeral with the care a dead king required -- offerings to Ereshkigal, gifts to Ningishzida, a protocol that acknowledged the hierarchies of the underworld as precisely as any court protocol acknowledged the hierarchies of the living." (~40 words; single dash-offset tricolon with symmetric `as precisely as` comparison, parses linearly).
- Line 80: "But it is the next best thing, and the fact that these poets -- writing four thousand years ago, in a language that would itself die -- understood the difference between eternal life and eternal significance may be the most durable thing about this broken, fragmentary, indispensable text." (~49 words, just under the 50-word threshold; dash-offset participial aside interrupts the `the fact that [subject] ... [verb] may be` scaffold, but the aside is short and the grammatical spine (`the fact ... may be the most durable thing`) is recoverable on first reading. The aside's temporal-and-linguistic framing is rhetorically essential to the chapter's closing cadence).

After the changes above, no remaining sentence exceeds the 50-word threshold. No remaining nested parentheticals. No subject-verb, tense, or article errors identified.

---

## Items deliberately NOT fixed (per hard rules)

- **Double periods *inside* `footnote:[...]` interiors** on lines 35 and 58 (e.g., `widely noted by scholars..`, `fully established..`, `semi-divine intercessors..`, `fully determined..`) — hard rule 2 forbids footnote changes.
- **Missing sentence-terminal period before the closing bracket of two footnote macros** at line 32 (`ETCSL 1.8.1.3, surviving fragments]`) and line 56 (`George 1999, pp. 206–208]`) — hard rule 2 forbids footnote-content changes, and adding a terminal period alters footnote content.
- **Line 25 (marker-resolved `VERSION` passage):** "ETCSL 1.8.1.3, Nippur version, which has been known longer and forms the basis of the ETCSL composite." — this reads as a sentence fragment (nominal phrase with a trailing relative clause, no finite main verb), and the following footnote interior (`because The Nippur...`) has a capital `T` mid-sentence after `because`. Both are artefacts of the marker-resolve stage for the `VERSION` selection and are locked marker-resolved content per hard rule 4. Flagged for human / line-edit review but not altered here.
- **Line 3 (marker-resolved `VERSION` passage):** "The present retelling follows the ETCSL composite text, supplemented by ETCSL composite text." — the tautological "supplemented by ETCSL composite text" appears to be a marker-resolve artefact (the supplement field collapsed to the same source). Locked marker-resolved content; hard rule 4. Flagged for line-edit / human review.
- **Sentence fragments used intentionally for rhetorical emphasis and retained:**
  - Line 23: "Death is absolute. Even for Gilgamesh." (short punch-fragments after the balanced claim).
  - Line 29: "Mortals die. He is mortal. Therefore he will die." (syllogism-as-three-fragments, deliberate cadence).
  - Line 32: "The gods live forever. Men do not." (two-line balanced fragments).
  - Line 37: "The name will be spoken. The hero will not be there to hear it." (paired short sentences; second is full clause but in the same rhetorical pattern).
  - Line 44: "Ereshkigal receives her offerings first. Ningishzida receives his." (parallel short sentences cataloguing the deity-by-deity procedure).
  - Line 44: "A dead king does not simply arrive in the underworld. He is processed." (two-sentence unit; the second is a full clause, retained for emphasis).
  - Line 47: "Inanna went alive and unwilling. Gilgamesh goes dead and, if not willing, at least prepared." (parallel-pair closing the Inanna/Gilgamesh comparison; full clauses but in the chapter's characteristic short-sentence register).
  - Line 52: "He has a function. He has authority. He judges." (tricolon of short declaratives).
  - Line 66: "Gilgamesh is dead, but he is not merely dead. He is dead and judging." (paired contrastive short clauses).
  - Line 78: "He died." (three-word sentence immediately after "The gods decreed that Gilgamesh must die."; deliberate short-sentence punch).
- **Academic / overview register in the opening source-summary paragraphs** (lines 3, 8, 16, 25) — per hard rule 3 and the `What NOT to fix` list, the academic tone of source overview sections is a deliberate register choice.
- **Word choice, sentence rhythm, paragraph transitions, nominalizations** (e.g., "cosmic law", "reflected authority", "the fundamental arithmetic") — deferred to line-edit (stage 15).
- **British -ise / -ize spelling consistency** (chapter uses "analysed", "legitimises", "divinisation" — British; no mixed spellings detected in this chapter, but consistency across the book is a line-edit concern).

---

## Self-check

1. **Factual content**: unchanged. No claim about texts, dates, people, places, deities (Ereshkigal, Ningishzida, Inanna, Huwawa, Gilgamesh), manuscript provenance (Nippur, Tell Haddad), page ranges (pp. 195–208, pp. 196–200, pp. 200–204, pp. 200–206, pp. 202–206, pp. 206–208), or events was altered. The list of underworld deities receiving offerings at line 44 (Ereshkigal, Ningishzida, and other divine figures, each with the same paired epithets as in the input) is preserved verbatim in content; only the internal punctuation and sentence boundary were restructured for readability.
2. **Footnote count**: unchanged (18 `footnote:[...]` macros in input; 18 in output; interior text preserved verbatim including all internal `..` marker punctuation).
3. **EVIDENCE tokens**: unchanged (15 `// EVIDENCE:` comments in input; 15 in output; identical).
4. **COMPARATIVE-HOOK comments**: unchanged (4 in input; 4 in output; identical).
5. **AsciiDoc structure**: unchanged. The single `== The Death of Gilgamesh` chapter heading, all six `'''` section-break markers, all italic markup `_..._` (including the two `_[...]_` editorial bracket notes at lines 12 and 14 and the two `_(...)_` parenthetical inference blocks at lines 35 and 58), and all `--` em-dashes are preserved. File line count is 80 in both input and output.
6. Every change is logged above. No silent changes.
