# Chapter 7 — The Toil of Babylon — Narrative Fidelity Report

**Stage**: 10e narrative-fidelity (per skill `12-narrative-fidelity.md`)
**Auditor**: fresh-conversation review, Claude Opus 4.7 (1M context)
**Claims file**: `chapters/07-toil-of-babylon.claims.approved.adoc` (87 lines)
**Draft file**: `chapters/07-toil-of-babylon.adoc` (77 lines)
**Brief**: `briefs/07-toil-of-babylon.yaml` (corrected brief, 2026-05-07)

---

## Verdict

**PASS**

The draft faithfully realizes the approved claims. Every claim is represented; no claim is added; every footnote, EVIDENCE token, COMPARATIVE-HOOK comment, LACUNA / RECONSTRUCTION / INFERENCE / VARIANT marker is preserved byte-for-byte. Glossary discipline holds. Damkina full first-mention gloss is given and the gloss-ledger is updated. Lugaldukuga inline gloss is given. No padding. No Sumerian-form leakage. No body-prose `*asterisk-bold*` typography errors.

---

## Mechanical preservation checks

### EVIDENCE tokens — PASS

21 tokens in claims; 21 tokens in draft; all match byte-for-byte (`source_id` and `loc` strings). All are at column 0. Diff with `grep "EVIDENCE:"` between draft and claims returns zero differences. All `source_id` values resolve to entries in `sources.yaml` (lambert-2013, foster-2007, black-green-1992, bottero-2001).

### Footnotes — PASS

14 footnotes in claims; 14 in draft. `grep -oE 'footnote:\[[^]]*\]'` diff returns zero differences. Every footnote string matches exactly.

### Markers — PASS

All markers preserved byte-for-byte (verified by grepping marker lines from both files and diffing — zero differences):

- `[LACUNA: …]` x1 — claims line 27 / draft line 17. Subfields `source:`, `scholarly_reconstruction:` preserved with ` | ` separator.
- `[RECONSTRUCTION: …]` x1 — claims line 29 / draft line 19. Subfields `gap_source:`, `fill_source:`, `confidence:` preserved with ` | ` separator.
- `[INFERENCE: …]` x3 — claims lines 43, 55, 65 / draft lines 33, 45, 55. Subfields `basis:`, `risk:` preserved with ` | ` separator.
- `[VARIANT: …]` x1 — claims line 69 / draft line 59. Subfields `primary=`, `alt=`, `chosen:`, `reason:` preserved with ` | ` separator.

### COMPARATIVE-HOOK comments — PASS

3 hooks in claims (lines 85–87); 3 in draft (lines 75–77). All at column 0. Text matches byte-for-byte.

---

## Claim-by-claim mapping (Check 1: completeness)

Every substantive claim in the approved doc is mapped to the corresponding passage in the draft. No CLAIM-DROPPED, no CLAIM-PARTIAL.

| # | Claim summary | Claims line | Draft line | Status |
|---|---|---|---|---|
| 1 | Lambert 2013 standard edition; witness lineage Boscawen 1877 → King 1902 → Lambert 2013 | 14 | 4 | MAPPED |
| 2 | No preserved ancient title; modern title editorial, taken from toil on populace | 17 | 7 | MAPPED |
| 3 | No anthology translation (Foster, Dalley); Lambert 2013 sole modern critical edition | 20 | 10 | MAPPED |
| 4 | Single Neo-Babylonian manuscript; 3 of 5 columns partly legible; none complete; Lambert reconstructs only what is preserved/restorable | 24 | 14 | MAPPED |
| LACUNA | (witness, missing material, no parallel manuscripts) | 27 | 17 | IDENTICAL |
| RECONSTRUCTION | (Lambert's continuous translation; *Atra-ḫasīs* thematic comparandum; confidence: low) | 29 | 19 | IDENTICAL |
| 5 | Opening on divine alienation; Col. I.1–2 quoted; register of estrangement | 33 | 23 | MAPPED |
| 6 | Col. I.5–6 quoted; populace conscripted; modern title taken from these lines | 37 | 27 | MAPPED |
| 7 | Col. I.13 escalation; Marduk most natural subject; pronoun chain quoted; "dynasty" lost in breaks; Col. II shifts register | 40 | 30 | MAPPED |
| INFERENCE-1 | (Atra-ḫasīs Igigi-rebellion frame as comparandum; not Enūma Eliš VI) | 43 | 33 | IDENTICAL |
| 8 | Col. II divine politics; Enlil exultant; Lugaldukuga bitter, descends to Apsû; death-sentence motif with Damkina + "my son" address (Col. II.16–17); figure "escaped swiftly" (Col. II.19); ambiguity of Damkina's role | 47 | 37 | MAPPED |
| 9 | Lugaldukuga's bitterness contextually weighted; Duku = holy mound of creation, place where destinies are decreed | 51 | 41 | MAPPED |
| INFERENCE-2 | (Lugaldukuga's bitterness as cosmogonic disorder vs. Enlil's exultation) | 55 | 45 | IDENTICAL |
| 10 | Col. V latest surviving column; line 9 quoted; decree collective/irreversible; gods' verdict on populace | 59 | 49 | MAPPED |
| 11 | Closing lines preserve gods in mourning; Col. V.17–19 quoted; gods grieving over Babylon | 62 | 52 | MAPPED |
| INFERENCE-3 | (Toil of Babylon as dark counterpart to Enūma Eliš's triumphal Marduk-cosmogony) | 65 | 55 | IDENTICAL |
| VARIANT | (single Neo-Babylonian tablet, Boscawen→King→Lambert, no alternates) | 69 | 59 | IDENTICAL |
| 12 | No parallel manuscripts; single Neo-Babylonian tablet; textual history Boscawen 1877 → King 1902 → Lambert 2013 | 71 | 61 | MAPPED |
| 13 | Marginal in attestation; no recensional/liturgical footprint; significance as node in late-Babylonian Marduk dossier alongside Enūma Eliš, Enmešarra's Defeat, Marduk Ordeal text, Atra-ḫasīs tradition; darker register | 76 | 66 | MAPPED |
| 14 | Narrative obscurity from fragmentary preservation + tonal distance from triumphal Marduk-cosmogony of Enūma Eliš; survives because temple-scholarly apparatus preserved it | 81 | 71 | MAPPED |
| HOOK x3 | (Genesis 11; Atra-ḫasīs internal; Enūma Eliš + Enmešarra's Defeat triumphal pole) | 85–87 | 75–77 | IDENTICAL |

Total: 14 substantive claims, all mapped; 3 INFERENCE / 1 LACUNA / 1 RECONSTRUCTION / 1 VARIANT marker, all preserved byte-for-byte; 3 COMPARATIVE-HOOK comments, all preserved byte-for-byte.

---

## Additions check (Check 2)

Walked the draft paragraph by paragraph. The draft adds only the kinds of material the brief permits: brief glossary reminders, narrative connective tissue, and editorial juxtaposition. No factual claim is asserted in body prose without an underlying claim. Findings:

### Permitted additions (no flag)

- **Draft line 23** "The Anunnaki — the ruling order of gods —": brief reminder using the brief's `first_mention_gloss_candidate` for Anunnaki ("the ruling order of gods, here hostile to the father of the gods at the narrative's opening"). Permitted.
- **Draft line 37** "Enlil — the high-god of the older Mesopotamian pantheon —": brief reminder mirroring the brief's `first_mention_gloss_candidate` for Enlil ("Mesopotamian high-god…"). Permitted.
- **Draft line 37** "the freshwater abyss beneath the earth" (gloss-reminder for Apsû): brief reminder of locked glossary `first_mention_gloss` ("the cosmic freshwater deep beneath the earth, dwelling of Ea"). Permitted.
- **Draft line 37** "Lugaldukuga, a primordial deity associated with the Duku (the holy mound of creation in Babylonian theology, the place where divine destinies are decreed)": required descriptive inline first-mention gloss for a deity not in the locked glossary. Faithful to claims line 51.
- **Draft line 37** "Damkina — Marduk's mother, consort of Ea —": full first-mention gloss for Damkina. Glossary `first_mention_gloss` is "consort of Ea, mother of Marduk"; the draft inverts the order but conveys the same two facts. Acceptable; gloss-ledger.yaml correctly records `Damkina: full_gloss_in: "07"` (line 99).
- **Draft line 49** "The gods who opened the narrative in alienation now close it as judges; the populace whose toil set the composition in motion is the verdict's object." — paraphrastic juxtaposition of claims 5+10 (the same gods alienated then judging, the same populace toiling then judged). No new fact.
- **Draft line 52** "the city named 'the pure' precisely as it is consigned to extinguishing" — juxtaposes the "Babylon the pure" epithet (within the verbatim Col. V.17–19 quote) with the extinguishing decree (claim 10). No new fact.
- **Draft line 71** "The dossier's editorial logic is the reason _The Toil of Babylon_ exists at all: a city's priestly scholars kept the dark text alongside the bright one, and a single Neo-Babylonian copyist transmitted both." — paraphrastic restatement of claim 14's temple-scholarly transmission, with the "dark/bright" juxtaposition picking up the dossier framing already in claims 13 and INFERENCE-3. No new fact.

### One borderline finding (LOW severity, not blocking)

- **Finding F-1**: kind = IMPLICIT-ADDITION; severity = LOW; draft line 41.
  - **Issue**: The sentence "He is, by ritual association, an apparatus-figure of the cosmogonic order itself." asserts a structural-cosmogonic claim about Lugaldukuga in body prose that the claims defer to the next-paragraph INFERENCE marker (claims line 55: "Lugaldukuga's primordial / Duku-mound associations… make his disposition cosmogonically marked").
  - **Detail**: The claims-doc structure puts the "cosmogonically marked" reading inside an INFERENCE marker with explicit `basis:` and `risk:` fields. The draft promotes a paraphrase of that inference into body prose, then immediately follows with the INFERENCE marker (line 45). Because the marker is right there and the body sentence is a softer paraphrase ("apparatus-figure of the cosmogonic order"), the inferential framing is preserved in close proximity — but the body sentence reads slightly more declaratively than the marker.
  - **Recommended fix (optional)**: tighten draft line 41 to stay closer to claim 9's wording, e.g., replace "He is, by ritual association, an apparatus-figure of the cosmogonic order itself." with a more neutral sentence like "His ritual associations bind him to the cosmogonic order." Or simply drop the sentence; the INFERENCE marker on line 45 carries the load. This is LOW severity and does not block PASS.

No CLAIM-ADDED at HIGH severity. No other IMPLICIT-ADDITION findings.

---

## Distortion check (Check 3)

For each mapped claim, compared meaning, scope, certainty, and causal direction. No distortions found.

- Inferential framings ("most naturally Marduk himself", "cannot be decided from the surviving lines", "cannot be securely identified") preserved in the draft with the same hedging.
- Quoted lines (Col. I.1–2; Col. I.5–6; Col. I.13; Col. I.9–13 pronoun chain; Col. V.9; Col. V.17–19) reproduced verbatim from the claims.
- The "subject most naturally Marduk" attribution at draft line 30 preserves claims line 40's identical hedging.
- The "agent and patient cannot be securely identified" hedge for the Damkina death-sentence motif preserved at draft line 37 / claims line 47.
- The "dark counterpart" framing for Toil-vs.-Enūma-Eliš is housed in INFERENCE-3 in both files, not asserted in body prose.

---

## Glossary discipline — PASS

- Locked Akkadian forms used throughout: Marduk, Anunnaki, Babylon, Enlil, Apsû, Damkina, Atra-ḫasīs, Enūma Eliš, Enmešarra's Defeat. No `never_use` violations.
- No Sumerian-form leakage: zero hits for Enki, Damgalnuna, abzu, Bilgames, Ningirsu, Anzud, Utnapishtim, Tammuz, Dumuzid in body prose.
- Damkina full first-mention gloss given (draft line 37: "Marduk's mother, consort of Ea") — equivalent to glossary `first_mention_gloss` "consort of Ea, mother of Marduk". `gloss-ledger.yaml` correctly records `Damkina: full_gloss_in: "07"`, `last_mention_in: "07"`, `chapters_used: ["00", "01", "07"]`.
- Lugaldukuga inline first-mention gloss given (draft line 37: "a primordial deity associated with the Duku (the holy mound of creation in Babylonian theology, the place where divine destinies are decreed)"). Lugaldukuga is not in `glossary.yaml` (a chapter-7-introduced figure); the gloss-ledger entry at line 110 records `Lugaldukuga: full_gloss_in: "07"`, `chapters_used: ["07"]`, with a comment noting that a glossary.yaml entry should be opened if Lugaldukuga reappears in a later chapter.

---

## Body-prose typography — PASS

- All `*asterisk-bold*` instances in the draft live inside footnote bodies, marker bodies (`[LACUNA: …]`, `[RECONSTRUCTION: …]`, `[INFERENCE: …]`, `[VARIANT: …]`), or `// COMPARATIVE-HOOK` comments. Permitted use.
- Body prose uses `_underscore-italic_` for book titles and italicized Akkadian terms: `_The Toil of Babylon_`, `_Babylonian Creation Myths_`, `_Transactions of the Society of Biblical Archaeology_`, `_The Seven Tablets of Creation_`, `_Before the Muses_`, `_Myths from Mesopotamia_`, `_Apsû_`, `_Enūma Eliš_`, `_Atra-ḫasīs_`. Correct.
- Zero body-prose `*asterisk-bold*` violations.

---

## Padding check — PASS

The draft is short (77 lines vs. 87 lines for claims). The draft is appropriately tight for a fragmentary composition preserved on a single tablet with three of five columns partly legible. There is no padding beyond the claims. Brief glossary reminders and editorial juxtapositional sentences add a small amount of connective prose, all within the brief's `special_instructions` envelope ("the chapter should be tight, not padded").

---

## Honesty self-check

1. **Did I map every claim, or skip some?** Every substantive claim was mapped. The claims doc has 14 prose claims (across 6 sections — source overview, setting, Damkina/death-sentence/flight, decreed destiny, variants, place in corpus) plus 3 INFERENCE markers, 1 LACUNA, 1 RECONSTRUCTION, 1 VARIANT, and 3 COMPARATIVE-HOOKs. All 23 elements were checked individually. None skipped.
2. **Did I check every narrative paragraph for additions?** Yes — every paragraph of the draft was walked. The borderline finding F-1 was identified by line-by-line comparison. No spot-checking; full traversal.
3. **For distortion checks, did I compare precise meaning?** Yes. Quoted lines were checked verbatim against the claims; inferential hedges ("most naturally", "cannot be decided", "cannot be securely identified") were checked for preservation; the location of the "dark counterpart" framing inside an INFERENCE marker (rather than body prose) was specifically verified.
4. **Am I the same model that produced the narrative?** This audit is a fresh-conversation review with no prior context on the draft. I have no memory of producing the narrative.

---

## Summary line

**VERDICT: PASS** — chapter 7 draft faithfully realizes the approved claims; all markers, footnotes, and EVIDENCE tokens preserved byte-for-byte; one LOW-severity IMPLICIT-ADDITION (draft line 41) noted but non-blocking.
