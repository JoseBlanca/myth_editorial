# Mythology Book Pipeline v2 — Full Pack for Review

This document consolidates the README, CHANGELOG, and all eleven SKILL.md files. Each section is delimited by a clear header.

---

# FILE 1 of 13: README.md

# Mythology Book Pipeline — v2

Multi-agent, multi-stage pipeline for producing Asimov-style mythology retellings with per-culture focus, auditable citations, and explicit handling of lacunae, reconstructions, and variants.

## Core principles

1. **Author ≠ Auditor.** Audit skills (`inventory-audit`, `chapter-factcheck`) must be run in fresh conversations, ideally with a different underlying model than the stage they are auditing. Rotation suggestion: Gemini (inventory) → Claude (audit) → Claude (draft) → GPT (factcheck) → Claude (edit).
2. **Scope is sacred.** `scope.md` + `sources.yaml` + `glossary.yaml` are prepended to every downstream prompt.
3. **Citations only from provided sources.** Drafting stages may cite only sources whose text is in the conversation or fetched in it. No citations from training memory.
4. **Internal variance is not an error.** Ancient mythologies are internally variant. Two in-scope sources disagreeing is part of the corpus, handled per the variant-classification rule.
5. **Contamination is document-level, not entity-level.** The question is whether *this specific narrative detail* appears in an in-scope document — not whether the entity "belongs to" the scope culture.
6. **Length follows source volume.** Chapters are never padded.

## Stage order

```
scope-lock → story-inventory → inventory-audit → [HUMAN ~15min] →
  chapter-briefs → glossary-lock → 
  [per chapter: chapter-draft → chapter-factcheck → [HUMAN resolves findings]] →
  comparative-chapter → marker-resolve → line-edit → format-finalize
```

## Artifact layout per book

```
<book-name>/
  scope.md
  sources.yaml
  inventory.yaml
  inventory-audit.yaml
  inventory.approved.yaml
  briefs/
    01-<slug>.yaml
    ...
  toc.yaml
  glossary.yaml
  chapters/
    01-<slug>.adoc              (drafted)
    01-<slug>.factcheck.yaml    (audited)
    01-<slug>.resolved.adoc     (markers resolved)
    01-<slug>.edited.adoc       (line-edited)
    01-<slug>.diff.md           (line-edit diff for review)
    ...
  comparative.adoc
  book.adoc                     (master)
  bibliography.bib
  validation-report.md
```

## Output format

AsciiDoc, rendered via Asciidoctor (not Pandoc) to PDF and EPUB. Pandoc is still useful for DOCX export if needed.

## What changed from v1

See `CHANGELOG.md`.

---

# FILE 2 of 13: CHANGELOG.md

# Changelog

## v2

**New skills**
- `glossary-lock` — locks English renderings of recurring terms before drafting.
- `marker-resolve` — resolves inline markers into final AsciiDoc constructs before line-editing (split from v1 `format-finalize`).

**New marker**
- `[RECONSTRUCTION:]` — content filled from another in-tradition source per scope's reconstruction policy, distinct from uncited `[INFERENCE:]`.

**Stronger audits**
- `chapter-factcheck`: quote-to-claim requirement (every ✓ needs a verbatim quote); triangulation against scholarly databases; reverse-order second pass; three-way distinction between internal variance (not a finding), contamination (finding), and fabrication (finding); verification unit moved from sentence to claim.
- `inventory-audit`: document-provenance contamination (not entity-provenance); quote-to-evidence on every HIGH finding; identifier verification.

**Draft discipline**
- `chapter-draft`: provided-sources-only citation rule; forbidden-words list; concrete Asimov exemplar passage; required sub-fields on all markers; explicit variant-handling rule (single-prevalent → footnotes; co-equal → inline).

**Scope explicitness**
- `scope-lock`: requires explicit contamination-risk list with user confirmation; requires reconstruction policy defining what counts as "in-tradition" fill source; requires variant presentation policy.

**Inventory rigor**
- `story-inventory`: verifiable identifiers (DOI / ISBN / museum number / corpus ID) required, not just URLs.

**Format stage split**
- Former `format-finalize` split into `marker-resolve` (prose-level, runs before line-edit) and `format-finalize` (mechanical assembly only, runs after line-edit).

## v1
Initial pipeline: scope-lock, story-inventory, inventory-audit, chapter-briefs, chapter-draft, chapter-factcheck, comparative-chapter, line-edit, format-finalize.

---

# FILE 3 of 13: skills/scope-lock/SKILL.md

---
name: scope-lock
description: Interactive skill run once at the start of each book. Produces scope.md and sources.yaml, which are prepended to every downstream skill. Defines cultural, temporal, and source boundaries — the single strongest defense against cultural contamination.
---

# scope-lock

## For the human

This is where you define what the book is and, equally importantly, what it is not. A Sumerian book is not a Mesopotamian book. A Norse book is not a Germanic book. Without a locked scope, the research, drafting, and audit stages drift: material from adjacent cultures seeps in, and by the time anyone notices, it's woven through every chapter.

This skill runs once. Its two outputs — `scope.md` and `sources.yaml` — are prepended to every later prompt in the pipeline. Every downstream agent reads them before doing anything.

The skill is interactive. Don't accept vague answers; press for specifics — especially on which adjacent cultures are most likely to contaminate the book, and on what counts as a legitimate source to fill gaps in the primary corpus.

## Inputs
- Target mythology (e.g., "Sumerian", "Norse", "Yoruba")
- User's goals and any hard exclusions they already have in mind

## Agent instructions

Run an interactive dialogue. Work through the template below with the user, question by question. Propose defaults drawn from scholarly consensus when the user doesn't know, and confirm their choice.

Pay particular attention to three sections that the rest of the pipeline depends on:

**1. Excluded adjacent cultures.** Name the specific cultures most likely to contaminate this book. For Sumerian, this is Akkadian/Babylonian. For Norse, it is continental Germanic and later Christianized sagas. Propose at least three specific contamination risks per book (more if the culture sits in a dense neighborhood), with a one-line rationale for each, and have the user confirm.

**2. Reconstruction policy.** When a primary source has a physical gap (tablet broken, manuscript leaf lost), the chapter-draft stage is allowed to fill that gap from another in-tradition source, flagged with a `[RECONSTRUCTION:]` marker. Ask the user to define precisely what counts as "in-tradition" for this book. Propose a default: same culture, same language of composition, within ±N centuries of the gap-bearing source. The user confirms or narrows.

**3. Source whitelist and blacklist.** Propose 8–15 whitelisted academic sources (critical editions, standard reference works, peer-reviewed corpora) and a blacklist of common contaminating popularizations. The user approves or edits.

## Outputs

### `scope.md`

```markdown
# Scope: <Mythology Name>

## Culture
<Name, self-designation, geographic extent>

## Period
<Earliest attested in-scope source — latest in-scope source>

## Languages of primary sources
<List>

## Excluded adjacent cultures (contamination risks)
- **<Culture A>**: <one-line reason, e.g., "Shares pantheon but distinct literary tradition; covered in separate book.">
- **<Culture B>**: <reason>
- **<Culture C>**: <reason>

## Reconstruction policy
When a primary source has a physical lacuna, content may be reconstructed from:
- <Defined in-tradition corpus, e.g., "Any Sumerian literary composition from the Old Babylonian scribal tradition, ca. 2000–1600 BCE">
- Reconstructions must be flagged with [RECONSTRUCTION:] markers; they are not silent fills.

## In-scope corpus (broad)
<Text collections, tablet series, manuscript traditions>

## Out-of-scope (explicit)
<Specific texts a naive researcher would wrongly include>

## Book register
Asimov-style retelling. Narrative prose in the body. Citations in AsciiDoc footnotes. Inferences, lacunae, reconstructions, and variants flagged inline with explicit markers.

## Variant presentation policy
- If one variant is clearly prevalent in the scholarly corpus: present it in the body, with minor variants in footnotes.
- If several variants are roughly co-equal: present them inline in the chapter body, introducing each with its source.
```

### `sources.yaml`

```yaml
whitelist:
  - id: <short_id>
    full: <full bibliographic citation>
    kind: primary-corpus | critical-translation | reference-work | peer-reviewed-monograph
    url_or_identifier: <DOI, ISBN, corpus identifier>

blacklist:
  - pattern: <URL pattern or citation pattern>
    reason: <why excluded>

triangulation_databases:
  # Culture-appropriate databases for verifying tablet/manuscript references
  - id: ETCSL
    url: https://etcsl.orinst.ox.ac.uk/
    covers: Sumerian literary texts
  # ...
```

## Handoff
Pass `scope.md` and `sources.yaml` to `story-inventory`. These files are re-read by every subsequent skill.

---

# FILE 4 of 13: skills/story-inventory/SKILL.md

---
name: story-inventory
description: Produces a structured inventory of stories attested in the scope mythology, each with verifiable identifiers for primary sources. Best run via Gemini Deep Research or an equivalent research-capable model with web access. Output is inventory.yaml, consumed by inventory-audit.
---

# story-inventory

## For the human

This skill produces the table of contents, in effect — the list of stories the book will cover. The research happens here, not in the drafting stage. Everything downstream depends on this inventory being accurate and in-scope.

The main risk is hallucinated stories: the model producing entries for stories that sound right for the culture but aren't actually attested, or confusing attestations across related cultures. The defense is strict sourcing — every entry carries a verifiable identifier (not a generic URL, which can be a dead link or a homepage), and uncertain entries are flagged rather than silently included or excluded.

Best run with a deep-research model (Gemini Deep Research, or equivalent) that can consult many sources in one pass.

## Inputs
- `scope.md`, `sources.yaml`

## Agent instructions

Using deep research and web search over the whitelisted sources and scholarly surveys, enumerate the major narrative cycles and individual stories of the scope mythology. Group stories by cycle: cosmogony, theogony, major heroic cycles, minor narratives, eschatology, etc. — adjusted to fit the culture (some have no cosmogony, some are organized by hero rather than cycle).

### Sourcing rule
Every story entry must carry at least one verifiable identifier. A verifiable identifier is one of:
- **DOI** (for journal articles or modern books with DOIs).
- **ISBN** (for printed critical editions).
- **Tablet/manuscript museum number** (e.g., BM 92687, CBS 14061).
- **Corpus text identifier** (e.g., ETCSL 1.4.1, Perseus urn:cts:greekLit:...).
- **Stable archival URL** to a scholarly repository (not a generic homepage, not Wikipedia).

Entries lacking any verifiable identifier are flagged `identifier_missing: true` rather than silently omitted.

### Contamination refusal
If a story is attested only in a culture listed under "Excluded adjacent cultures" in `scope.md`, omit it. If it is attested in both the scope culture and an excluded culture, include it but check whether the specific *plot details* you've found come from the scope culture's attestations or the excluded culture's. Flag `scope_uncertain: true` for anything you cannot clearly assign.

### Scope of entries
Aim for comprehensiveness within the scope, not exhaustiveness. Include every story with a recognized scholarly attestation in the culture's major reference works. A story mentioned in one footnote of one monograph does not belong in the inventory; a story covered in Black et al. 2004 or equivalent does.

## Output: `inventory.yaml`

```yaml
cycles:
  - id: cosmogony
    name: "Cosmogonic cycle"
    stories:
      - id: <slug>
        title: "<English working title>"
        native_title: "<if applicable>"
        sources:
          - id: <source_id from sources.yaml whitelist>
            loc: "<tablet/line/page reference>"
            identifier: "<DOI, ISBN, museum number, or corpus identifier>"
        date_range: "<approximate date of composition>"
        summary: "<two sentences>"
        variants: [<brief notes if multiple versions exist within the scope culture>]
        scope_uncertain: false
        identifier_missing: false
        notes: "<lacunae, textual issues, anything the auditor should know>"
```

## Self-check before returning
1. Every entry has at least one `identifier` that could be verified by a third party.
2. No entries rely on Wikipedia as authority (acceptable as lead only, not as `source`).
3. Every `scope_uncertain: true` entry has a note explaining the uncertainty.
4. Internal variants (multiple in-scope sources giving different versions) are recorded in the `variants` field, not flagged as problems.

## Handoff
To `inventory-audit`, which must be run in a fresh conversation with a different model.

---

# FILE 5 of 13: skills/inventory-audit/SKILL.md

---
name: inventory-audit
description: Audits the story inventory. Must be run in a fresh conversation with a different model than story-inventory. Detects contamination (document-provenance method), unsupported entries with fabricated identifiers, missing canonical stories, and internal variants that need explicit handling. Output is severity-ranked for minimal-time human review.
---

# inventory-audit

## For the human

This is the first of the two critical audit skills. It checks the story inventory before any drafting begins. The cost of catching errors here is minutes; the cost of catching them after chapters are drafted is hours.

The hardest check is contamination detection. Gemini's review of an earlier version pointed out that checking "what culture is this entity from?" is too coarse — the same deity exists across cultures, but specific narrative details are culture- and period-bound. The correct check is at the document level: is *this specific plot element* attested in a document from within the scope's period and culture?

This audit must be run in a fresh conversation, ideally with a different underlying model than produced the inventory. Same-model same-conversation self-review catches almost nothing.

## Hard rule
If you are the model that produced `inventory.yaml`, or if you are in the same conversation in which it was produced, refuse and tell the user to start a fresh conversation with a different model.

## Inputs
- `scope.md`, `sources.yaml`
- `inventory.yaml`
- Web search tool (required — you will use it)

## The four checks

### 1. Contamination (document-provenance method)
For each story entry and each specific plot detail within it, ask: **is this detail attested in a document whose physical composition falls within the scope's date range and culture?**

Not "is the entity from this culture." The entity may span millennia. The question is whether the specific narrative element — a plot event, a ritual detail, a named object, a piece of dialogue — appears in a document that is in-scope.

A detail attested only in out-of-scope documents (e.g., a Neo-Assyrian tablet when the scope is Old Babylonian Sumerian) is CONTAMINATION-HIGH, regardless of whether the entity is "originally" from the scope culture.

For each HIGH contamination finding, provide a verbatim quote from the out-of-scope source showing where the detail actually comes from.

### 2. Unsupported entries and fabricated identifiers
For each story, verify that:
- The cited source exists (search for the identifier — DOI, ISBN, museum number, corpus ID).
- The cited source actually attests the story as described.

If the identifier does not resolve, or resolves to something that does not contain the described story, flag HIGH. Include the URL of your verification search so the human can replicate it.

### 3. Missing canonical stories
Consult scholarly surveys of the scope mythology (whitelisted reference works) for stories that belong in the inventory but are absent. Propose additions with full source identifiers. Severity MEDIUM — the human decides inclusion.

### 4. Internal variants handling
Where a story has multiple attested in-scope versions, check that the inventory's `variants` field acknowledges this. If the inventory silently conflates variants into a single summary, flag MEDIUM.

**Do not flag internal variants themselves as problems.** Multiple in-scope sources disagreeing is normal and is part of the corpus. The flag is for silent conflation, not for variance itself.

## Quote-to-evidence requirement
For every HIGH finding (contamination, fabricated identifier, unsupported claim), you must paste a verbatim quote from a source showing the problem. Either:
- A quote from an out-of-scope source showing where the contaminating detail actually comes from, OR
- A screenshot/URL of a database search showing an identifier does not resolve, OR
- A quote from the cited source showing it does not contain what was claimed.

Findings without quoted evidence are not valid HIGH findings; downgrade to MEDIUM and say so.

## Output: `inventory-audit.yaml`

```yaml
meta:
  auditor_model: <model name and version>
  entries_reviewed: <n>
  triangulations_performed: <n>
  time_to_review_estimate_minutes: <n>

summary:
  high: <n>
  medium: <n>
  low: <n>

findings:
  - severity: HIGH | MEDIUM | LOW
    kind: CONTAMINATION | UNSUPPORTED | FABRICATED-IDENTIFIER | MISSING | SILENT-CONFLATION
    story_id: <id, or "NEW" for missing>
    entity_or_detail: <what specifically>
    issue: <one sentence>
    evidence_quote: "<verbatim from source>"
    evidence_source: <id + loc, or verification URL>
    recommended_action: <concrete>

clean_entries: [<list of story_ids that passed all checks>]
```

## Honesty self-check
Answer these in `meta` explicitly:
1. Did I actually resolve each cited identifier, or did I assume well-known sources are correct? Name any I assumed.
2. Did I check every plot detail for provenance, or did I check only major ones? Name what I skipped.
3. For every HIGH finding, did I include a verbatim evidence quote? If any are missing, list them.
4. Am I the same model that produced the inventory? If yes, the audit is invalid.

## Human review protocol
Tell the user: review HIGH findings (~10 minutes), skim MEDIUM, ignore LOW unless maximum rigor is desired. Mark each finding's `recommended_action` field as `ACCEPTED` or `REJECTED`. Apply accepted changes to produce `inventory.approved.yaml` for the next stage.

## Handoff
`inventory.approved.yaml` to `chapter-briefs`.

---

# FILE 6 of 13: skills/chapter-briefs/SKILL.md

---
name: chapter-briefs
description: Converts the approved inventory into one brief per chapter. Each brief specifies primary and secondary sources, known lacunae, in-scope variants with prevalence note, triangulation databases for fact-check, comparative hooks reserved for the comparative chapter, and a source-volume-based target length.
---

# chapter-briefs

## For the human

This skill produces a dossier per chapter. No prose is written at this stage — the brief is a structured plan that the drafter will use. Getting the brief right means the drafter has everything it needs and doesn't have to improvise.

Two things the brief must get right:

1. **Variant handling.** For each story, the brief records what the in-scope variants are and whether one is clearly prevalent. This directly determines how the drafter presents the story — main version in body with variants in footnotes, or several versions inline.

2. **Length sizing.** The brief sets a target length based on how much primary source material actually exists. A fragmentary story gets a short chapter. A richly-attested cycle gets a long one. The drafter is told not to pad.

## Inputs
- `scope.md`, `sources.yaml`
- `inventory.approved.yaml` (post-audit, post-human review)

## Agent instructions

For each story in the approved inventory, produce `briefs/NN-<slug>.yaml` (where NN is chapter number).

### Chapter ordering
Default order: cosmogony → theogony → major heroic cycles → minor heroic → eschatology → miscellaneous. Adapt to the culture. Some cultures have no cosmogony (e.g., Irish); don't force the scheme. Record final order in `toc.yaml`.

### Variant prevalence assessment
For each story, assess in-scope variants and classify:
- **single-prevalent**: one variant is clearly dominant in the scholarly corpus. Others are minor. → body presents the prevalent version, footnotes carry variants.
- **co-equal**: multiple variants are roughly equally attested, or no scholarly consensus on prevalence. → body presents variants inline, each with its source.

This classification is the drafter's instruction.

### Length sizing
Target based on source volume, not narrative length:
- Fragmentary single-source: 600–1200 words.
- Well-preserved single composition: 2000–4000 words.
- Multi-tablet or multi-manuscript cycle: 8000–15000 words.

## Output: `briefs/NN-<slug>.yaml`

```yaml
chapter_number: <n>
slug: <slug>
title: "<editorial chapter title>"

sources:
  primary:
    - id: <from whitelist>
      loc: <tablet/line/page>
      translator_edition: <which edition's translation to use>
      identifier: <DOI/ISBN/museum number/corpus ID>
      url_or_file: <where the text is accessible>
  secondary:
    - { id, loc }

lacunae:
  - source: <id>
    location: <lines>
    what_is_missing: <description>
    in_tradition_fills_available: <yes/no — and if yes, from which in-scope sources>

variants:
  classification: single-prevalent | co-equal
  prevalent_version:
    source: <id>
    why_prevalent: <one line — e.g., "Most complete attestation, used as base text in Black 2004">
  alternates:
    - source: <id>
      difference: <one line>

entities_glossary:
  # Pre-seeds glossary-lock. Glossary-lock will lock the final English renderings.
  - name: <native form>
    role: deity | hero | place | artifact | ritual-term
    first_mention_gloss_candidate: <short functional gloss>

comparative_hooks:
  # Collected here, used only in the comparative chapter. Not for this chapter.
  - other_culture: <n>
    parallel: <brief>
    source: <id>

triangulation_databases:
  # Which external databases fact-check should use to verify citations
  - <e.g., ETCSL, CDLI, Perseus, TITUS>

target_length_words: <integer based on source volume>

special_instructions: <any — e.g., "Preserve the dialogue structure of the original">
```

## Self-check
- Every story in the approved inventory has a brief.
- Every brief's sources list contains only whitelisted sources with verifiable identifiers.
- Every brief has a variant classification (single-prevalent or co-equal), not blank.
- Every brief has a triangulation database list (at least one).
- `toc.yaml` contains all chapters in order.

## Handoff
To `glossary-lock`, which runs once over all briefs before any drafting.

---

# FILE 7 of 13: skills/glossary-lock/SKILL.md

---
name: glossary-lock
description: Locks the English rendering of recurring technical terms and proper nouns before any chapter is drafted. Prevents phantom translation-conflict findings in fact-check and ensures consistency across chapters. Interactive, runs once per book after chapter-briefs.
---

# glossary-lock

## For the human

Scholarly translations disagree on key words. Sumerian *me* is rendered "divine powers" (Kramer), "cosmic ordinances" (Jacobsen), or left untranslated (Black). If the drafter picks one and the fact-checker is reading a source that uses another, the fact-checker will flag phantom contradictions. Across chapters, inconsistent renderings make the book read as if multiple hands wrote it.

This skill short-circuits both problems by having the user lock each recurring term's English form before any chapter is drafted. Usually 10–30 terms per book. Interactive: the skill proposes, you decide.

## Inputs
- `scope.md`, `sources.yaml`
- All `briefs/*.yaml`

## Agent instructions

### Step 1: extract candidate terms
Scan all briefs' `entities_glossary` fields and source-text samples. Identify:
- Proper nouns appearing in 2+ chapters (deities, heroes, places, artifacts).
- Technical terms with no one-to-one English equivalent.
- Ritual, political, and cosmological vocabulary that translators render inconsistently.

### Step 2: survey renderings
For each candidate, report:
- Native form (transliterated with standard diacritics).
- 2–4 rendering options, each attributed to a specific translator/edition.
- Your recommendation with a one-sentence reason.
- Any rendering that would be wrong (e.g., an out-of-scope culture's equivalent).

### Step 3: interactive confirmation
Present the proposed glossary. For each entry the user either accepts, picks an alternate, or supplies their own. Do not skip entries silently.

## Output: `glossary.yaml`

```yaml
terms:
  - native: <transliteration>
    renderings_considered:
      - { form: <rendering>, source: <translator/edition> }
    chosen: <final locked rendering>
    rationale: <one line>
    first_mention_gloss: <short functional gloss, Asimov-style>
    never_use: [<list of out-of-scope equivalents that must never appear>]
```

## Self-check
- Every term appearing in 2+ briefs is included.
- Every `never_use` entry is a real out-of-scope equivalent (e.g., Akkadian for a Sumerian book), not just a synonym.
- First-mention glosses are functional, not poetic (no "mighty", "ancient", etc.).

## Handoff
`glossary.yaml` to `chapter-draft`.

---

# FILE 8 of 13: skills/chapter-draft/SKILL.md

---
name: chapter-draft
description: Produces an Asimov-style retelling of a single story as AsciiDoc with footnote citations. Every factual claim maps to a provided source. Inferences, lacunae, reconstructions, and variants flagged inline. Length follows source volume, never padded.
---

# chapter-draft

## For the human

This is the one creative stage in the pipeline, and therefore the most dangerous. The model's instinct when asked to "retell a myth" is to fill gaps, smooth transitions, and reach for evocative language — all three produce fabrication.

The skill enforces four disciplines:

1. **Provided-sources-only citation.** The drafter may only cite sources whose text has been pasted into the conversation or fetched in it. No citations from training memory, even for famous sources. This kills the most common hallucination pattern.
2. **Asimov method, defined concretely.** Not a vague style note — a concrete exemplar passage plus a list of forbidden words. Models imitate examples far more reliably than they execute style descriptions.
3. **Marker discipline.** Four markers — `[INFERENCE:]`, `[LACUNA:]`, `[RECONSTRUCTION:]`, `[VARIANT:]` — with required sub-fields. These survive to the marker-resolve stage; the drafter does not decide how they render in final prose.
4. **Length follows sources.** A fragmentary story gets a short chapter. Padding is forbidden.

## Hard rules
1. Cite only sources whose text has been provided to you in this conversation or fetched by you via tool use. No citing from memory, even confidently.
2. Use exactly the English renderings locked in `glossary.yaml`. If a needed term is missing, stop and ask.
3. Omit material from excluded cultures. Note the temptation in a `// COMPARATIVE-HOOK:` comment for the comparative chapter.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- One chapter brief (`briefs/NN-<slug>.yaml`)
- Primary source translations — pasted into the conversation or accessible via fetch

## Style: the Asimov method

Treat the reader as intelligent and uninformed. Gloss proper nouns with functional roles, not poetic epithets. Short paragraphs, one idea each. Plain modern English. Where the source is ambiguous, say so. Where scholars disagree, name it briefly. Use etymology and geography when they illuminate a specific point, never as mandatory ornament.

### Exemplar passage

> The Sumerians believed that before anything else existed, there was a primeval sea. They called her Nammu, and she seems to have been thought of as a kind of cosmic mother — though the texts that survive are maddeningly brief on this point. From Nammu came heaven and earth, conceived of as a single mountain with the sky (An) on top and the earth (Ki) below. An and Ki were the first divine couple, and their union produced Enlil, the god of the air.
>
> Enlil then did something that requires explanation. He separated his father An from his mother Ki, pushing the sky upward and leaving the earth below. This is a motif found in many mythologies — the violent separation of sky and earth by a younger god — but the Sumerian version is unusually matter-of-fact about it. There is no battle, no castration, no cosmic drama. Enlil simply separates them, and the world as we know it comes into being.

### Forbidden words

Do not use, in this register: *shimmering, ancient* (as ornament), *mystical, unfathomable, primordial* (as ornament), *ineffable, sacred* (as filler), *mighty, fearsome, dread, eternal, boundless, infinite, veiled, shrouded*. Avoid openings like "Long ago...", "In the time before time...", "It is said that...". These mark imitation-sacred prose, not Asimov.

## Variant handling (from brief)

- If `variants.classification` is **single-prevalent**: present the prevalent version in the body. Put alternate versions in AsciiDoc footnotes.
- If **co-equal**: present the variants inline in the body, each introduced with its source ("One tradition, preserved in [source], describes... Another, in [source], gives a different account...").

## Markers (required sub-fields)

- `[INFERENCE: <claim> | basis: <why this bridge is reasonable> | risk: <what is speculative>]`
  — A narrative bridge not directly attested.
- `[LACUNA: <what is missing> | source: <exact ref> | scholarly_reconstruction: <if any, with citation>]`
  — A documented physical gap in the source (broken tablet, lost manuscript leaf).
- `[RECONSTRUCTION: <filled content> | gap_source: <where the lacuna is> | fill_source: <which in-tradition source supplies the content, per scope.md's reconstruction policy> | confidence: high|medium|low]`
  — Content filled from another in-tradition source per the reconstruction policy.
- `[VARIANT: primary=<source A, short quote> | alt=<source B, short quote> | chosen: A|B | reason: <why>]`
  — Used only when both variants are single-prevalent cases where the alternate is in a footnote. For co-equal cases, variants are narrated inline without a marker.

All markers survive to marker-resolve. Do not paraphrase them away.

## Citations

AsciiDoc footnotes. Every factual claim (typically a paragraph or part of a paragraph — not every connective sentence) must be covered by at least one footnote. First use of a source: full bibliographic form. Subsequent uses: short form.

## Length

Per brief's `target_length_words`, driven by source volume. If you find yourself padding, stop and return the shorter version with a note.

## Output: `chapters/NN-<slug>.adoc`

```asciidoc
== <Chapter Title>

<Opening — orient the reader in time, place, and source situation.>

<Body — retell the narrative, source-ordered, footnoted.>

<Closing — brief note on the story's place in the culture's corpus. No cross-cultural comparison. Append `// COMPARATIVE-HOOK:` comments for the comparative chapter.>
```

## Self-check before returning
1. Every factual claim has footnote coverage. No silent claims.
2. Every footnote cites a source actually provided in this conversation. Nothing from memory.
3. Scan for forbidden words — each hit is a drift signal; revise.
4. Every proper noun was glossed on first mention using `glossary.yaml`.
5. Variant handling matches the brief's classification (single-prevalent → footnotes; co-equal → inline).
6. Every marker has all required sub-fields.
7. No out-of-scope material. Temptations are in `// COMPARATIVE-HOOK:` comments.
8. Length matches the brief's target. Not padded.

## Handoff
To `chapter-factcheck`, fresh conversation, different model.

---

# FILE 9 of 13: skills/chapter-factcheck/SKILL.md

---
name: chapter-factcheck
description: Audits a drafted chapter at claim level against cited sources. Must be run in a fresh conversation with a different model than chapter-draft. Uses quote-to-claim mapping, triangulates citation references, and distinguishes internal variants (not findings) from contamination and fabrication (findings).
---

# chapter-factcheck

## For the human

This is the most important audit in the pipeline. A drafted chapter can look clean — footnotes in place, plausible prose — while containing fabricated references, half-remembered plot points, and silent contamination from adjacent cultures.

The skill enforces four disciplines that make the audit real rather than theatrical:

1. **Quote-to-claim mapping.** Every "supported" verdict requires the auditor to paste a verbatim quote from the source. Without a quote, the verdict downgrades to unverified. This converts yes/no judgments into a retrieval task, which models do more honestly.
2. **Triangulation of citations.** Tablet numbers, line ranges, and page references are the easiest things to fabricate. The auditor verifies each reference against the triangulation databases listed in the brief (ETCSL, CDLI, Perseus, etc.).
3. **Three-way distinction where v1 had a blunt "contradicted" verdict.** Mythologies are internally variant. Two in-scope sources disagreeing is normal — not a finding. The verdicts are now: *contamination* (detail comes from an out-of-scope source), *fabrication* (detail in no source), and *internal variance* (two in-scope sources disagree — acknowledged, not flagged).
4. **Reverse-order second pass.** Long-context audits exhibit lead bias. The auditor does one pass start-to-end, then a second pass end-to-start.

## Hard rule
Must be run in a fresh conversation, ideally with a different underlying model than produced the draft. If you have any memory of drafting this chapter, refuse.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- `chapters/NN-<slug>.adoc`
- `briefs/NN-<slug>.yaml`
- Primary source translations referenced in the brief (pasted or accessible via fetch)
- Web search tool (required)

## The unit of verification

Verify at the level of **the factual claim**, not the sentence. A claim is an assertion about the myth — who did what, when, why, in what order. A claim typically spans a paragraph or part of a paragraph. Connective, transitional, and expository sentences that restate or comment on a claim inherit the claim's verdict; they do not need separate verdicts.

## The six passes

### Pass 1 — Claim-level verification (start to end)
Walk the chapter in order. For each distinct factual claim, assign one of these verdicts:

- **✓ SUPPORTED** — Must include a verbatim quote from a cited in-scope source. Not a paraphrase. Actual pasted text. If you cannot produce a quote, you cannot use this verdict.
- **△ INTERNAL-VARIANCE** — The chapter's claim is attested in one in-scope source, but another in-scope source gives a different account. This is not a finding; it is part of the corpus. Note it so the reader of your audit knows the variance exists. If the chapter's variant handling (footnote vs inline) matches the brief's classification, no action needed. If it doesn't, flag that mismatch as MEDIUM.
- **? UNVERIFIED** — No supporting quote found in provided sources. Default when uncertain.
- **! CITATION-WRONG** — Claim is correct but the footnote points to a wrong source, page, or line number.
- **⚠ CONTAMINATION** — Claim is supported, but the supporting source is from an excluded culture per `scope.md`. Include the out-of-scope quote as evidence.
- **✗ FABRICATION** — Claim is not supported by any source, in-scope or out-of-scope, that you can locate.

### Pass 2 — Triangulation of references
For every footnote citing a specific tablet number, line range, manuscript folio, or page reference, verify the reference resolves in one of the `triangulation_databases` listed in the brief. If the reference does not resolve or resolves to something else, flag CITATION-WRONG with HIGH severity and include the verification URL.

### Pass 3 — Document-provenance contamination scan
For each specific plot detail (not just named entities, but specific narrative elements), ask: is this detail attested in a document whose physical composition falls within the scope's date range and culture?

Attestation of the *entity* across cultures is not enough. The question is whether *this narrative detail* appears in an in-scope document. Details attested only in out-of-scope documents are CONTAMINATION-HIGH, even if the entity is native to the scope culture.

### Pass 4 — Marker integrity
- `[INFERENCE:]` — check the inference is genuinely inferential. If an in-scope source directly attests the claim, flag MARKER-MISUSED.
- `[LACUNA:]` — check the source actually has the claimed gap. If the source is complete at that point, flag MARKER-FABRICATED.
- `[RECONSTRUCTION:]` — verify the `fill_source` is in-tradition per `scope.md`'s reconstruction policy. If the fill comes from an out-of-scope source, flag CONTAMINATION.
- `[VARIANT:]` — verify both quoted phrases are present in their cited sources.
- **Silent bridges** — scan for claims presented as fact that aren't in any source and aren't under a marker. These are the most dangerous failures. Flag SILENT-BRIDGE with HIGH severity.

### Pass 5 — Reverse-order second pass
Walk the chapter from last paragraph to first, hunting for anything Pass 1 missed due to lead bias. Pay particular attention to the final third. Add any new findings.

### Pass 6 — Glossary and style sanity
- Confirm glossary.yaml renderings are used consistently. Any `never_use` terms appearing in the chapter are CONTAMINATION.
- Flag forbidden-words list hits from `chapter-draft`'s style rules. Light touch — line-editing happens later.

## Output: `chapters/NN-<slug>.factcheck.yaml`

```yaml
meta:
  auditor_model: <name and version>
  chapter_file: chapters/NN-<slug>.adoc
  claims_identified: <n>
  triangulations_performed: <n>
  verdict: PASS | REVISE | MAJOR-REVISE

tallies:
  supported: <n>
  internal_variance: <n>
  unverified: <n>
  citation_wrong: <n>
  contamination: <n>
  fabrication: <n>
  silent_bridges: <n>
  marker_issues: <n>
  glossary_violations: <n>
  style_drift: <n>

supported_claims:
  # Every ✓ verdict with its verbatim quote. If this list is short, you didn't do the work.
  - paragraph: <paragraph number or adoc line>
    claim: "<the claim, in your words>"
    source_id: <from sources.yaml>
    source_loc: <tablet/line/page>
    verbatim_quote: "<exact text from source>"

findings:
  - paragraph: <paragraph number or adoc line>
    kind: UNVERIFIED | CITATION-WRONG | CONTAMINATION | FABRICATION | SILENT-BRIDGE | MARKER-MISUSED | MARKER-FABRICATED | GLOSSARY-VIOLATION | VARIANT-HANDLING-MISMATCH | STYLE
    severity: HIGH | MEDIUM | LOW
    claim: "<sentence or paragraph>"
    issue: <one sentence>
    evidence: <verbatim quote if applicable, or triangulation URL>
    recommended_fix: <concrete>
```

## Verdict rules
- **PASS**: zero HIGH findings, zero silent bridges, ≤ 3 MEDIUM.
- **REVISE**: 1–2 HIGH, or > 3 MEDIUM, or any silent bridge.
- **MAJOR-REVISE**: ≥ 3 HIGH, or any contamination finding, or triangulation failures indicating fabricated references.

## Honesty self-check
Answer in `meta` explicitly:
1. Did I open every cited primary source, or skim? Which did I skim?
2. Did I perform triangulation for every tablet/line/page reference, or assume well-known references are correct?
3. For every ✓ SUPPORTED, did I paste a real quote or pattern-match? Any I pattern-matched are downgraded to ? here.
4. Did I distinguish internal variance from contamination, or collapse them?
5. Am I the same model that drafted this chapter? If yes, this audit is not valid.

A partial honest audit is more useful than a complete dishonest one. If you cut corners, say so.

---

# FILE 10 of 13: skills/marker-resolve/SKILL.md

---
name: marker-resolve
description: Resolves [INFERENCE], [LACUNA], [RECONSTRUCTION], and [VARIANT] markers into final AsciiDoc prose constructs. Runs after chapter-factcheck has passed and before line-edit, so that line-edit can polish the actual final prose.
---

# marker-resolve

## For the human

The drafting stage puts markers inline as placeholders. They need to become final prose — italicized parentheticals, editorial notes, footnotes — before line-editing, because marker expansion changes sentence rhythm and line-editing needs to see the actual final text.

Separated from `format-finalize` (which handles mechanical assembly) so that line-edit operates on the true final prose.

## Inputs
- Fact-check-passed chapters (`chapters/NN-<slug>.adoc`)
- `scope.md` (for marker-rendering preferences)

## Agent instructions

Resolve each marker per these rules. Do not alter any other prose.

### `[INFERENCE: claim | basis: X | risk: Y]`
Render as an italicized parenthetical with a footnote containing the basis and risk:
```
_(The text does not state this explicitly, but the following episode requires it.footnote:[Inference: <basis>. Risk: <risk>.])_
```

### `[LACUNA: what | source: ref | scholarly_reconstruction: X]`
Render as a bracketed editorial note, italicized:
```
_[At this point the tablet breaks. Approximately 20 lines are lost. Scholars such as <ref> have proposed the narrative resumed with <reconstruction>.]_
```
If no scholarly reconstruction is given, omit the second sentence.

### `[RECONSTRUCTION: content | gap_source: X | fill_source: Y | confidence: Z]`
Render the content in prose, with a footnote flagging it as reconstruction:
```
<content rendered as normal prose>.footnote:[This passage reconstructs the lacuna at <gap_source> from the parallel account in <fill_source>; confidence: <Z>.]
```

### `[VARIANT: primary=A | alt=B | chosen: A | reason: R]`
Only appears in single-prevalent cases (co-equal variants are already inline without markers). Render as the prevalent version in body, with a footnote giving the alternate:
```
<prevalent version text>.footnote:[An alternate tradition in <B source> gives: "<alt phrase>". The prevalent version is chosen here because <reason>.]
```

## Self-check
- Grep the output for `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:` — must be zero matches.
- No prose outside of marker-replaced sections has changed.

## Handoff
To `line-edit`.

---

# FILE 11 of 13: skills/comparative-chapter/SKILL.md

---
name: comparative-chapter
description: Produces the single comparative-mythology chapter that quarantines all cross-cultural comparison to one place. Runs only after all culture-internal chapters are locked (fact-checked, marker-resolved). Uses comparative_hooks collected in briefs and drafts, plus comparative-mythology scholarship.
---

# comparative-chapter

## For the human

The body of the book is culturally pure — each chapter stays within its own tradition. The comparative chapter is where cross-cultural observation is allowed, and confining it to one place keeps the rest of the book clean.

This chapter is inherently more speculative than the others. It uses an additional marker, `[SPECULATION:]`, for hypotheses that are plausible but not scholarly consensus.

## Inputs
- All locked chapters (post marker-resolve)
- All briefs (for `comparative_hooks`) and all `// COMPARATIVE-HOOK:` comments left in chapter drafts
- `scope.md`, `sources.yaml`
- Optional comparative-mythology whitelist (Dumézil, Puhvel, Watkins, West, Witzel, Lincoln — add to `sources.yaml` before this stage)

## Rules
- Every comparison cites both the in-scope source and the out-of-scope source.
- Structural parallels (tripartite function, sky-father motif, etc.) cite scholarly methodology, not invented frameworks.
- Speculation is allowed but must be marked: `[SPECULATION: claim | basis: X | counterargument: Y]`.
- Do not retell out-of-scope myths at length — one-paragraph summaries, then the comparison.

## Style
Asimov register, extended for comparative nuance. Signal uncertainty: "One might observe...", "Scholars such as X have argued...". Avoid grand unifying claims; stay close to specific parallels.

## Output: `comparative.adoc`

Structured as:
- Intro paragraph on the scope and limits of comparison.
- One section per major parallel type (cosmogonic parallels, heroic parallels, eschatological parallels, etc.), as appropriate.
- Closing that resists overreach.

## Self-check
- Every comparative claim cites both an in-scope source and an out-of-scope source.
- Every `[SPECULATION:]` has both basis and counterargument sub-fields.
- No claim presented as consensus unless it actually is.

## Handoff
To `line-edit` along with all other chapters.

---

# FILE 12 of 13: skills/line-edit/SKILL.md

---
name: line-edit
description: Pinker-style clarity pass on all chapters after marker-resolve. Forbidden from introducing new facts, changing citations, or altering resolved marker content. Improves sentence rhythm, reduces nominalizations, repairs transitions.
---

# line-edit

## For the human

The last prose pass. All facts are locked, all markers resolved, all citations in place. This stage only polishes — it cannot add, remove, or change factual content. A single introduced or removed claim is a bug.

Runs after `marker-resolve` so line-editing operates on the actual final prose the reader will see.

## Hard rules
1. No new factual claims. If editing changes a sentence's factual meaning, revert.
2. No footnote changes — no additions, removals, or re-assignments.
3. No changes to content inside already-resolved marker passages (italicized parentheticals, bracketed editorial notes, reconstruction footnotes). These were reviewed by fact-check and resolved by marker-resolve — they are locked.
4. AsciiDoc structure (headings, footnote syntax, include directives) is untouched.

## Inputs
- Marker-resolved chapters (`chapters/NN-<slug>.resolved.adoc`)
- `glossary.yaml` (to confirm renderings stay consistent)

## Method (Pinker, *The Sense of Style*)

- **Classic style**: writer and reader looking at the same thing. Remove throat-clearing.
- **Nominalizations**: "made a decision" → "decided".
- **Zombie nouns**: "the implementation of" → "implementing".
- **Subject-verb distance**: keep it short where possible.
- **Parallel structure** in lists and comparisons.
- **Paragraph transitions**: each paragraph's opening connects to the previous paragraph's close.
- **Proper-noun glosses**: confirm first-mention explanations are still present and match `glossary.yaml`.

## Output

`chapters/NN-<slug>.edited.adoc` plus a diff file `chapters/NN-<slug>.diff.md` showing original sentence vs edited sentence for every non-trivial change. The human skims the diff to approve in bulk.

## Self-check
- Extract all factual claims from original and edited versions; compare. Any difference is a bug.
- Footnote count and content unchanged.
- Resolved marker passages unchanged.

## Handoff
To `format-finalize`.

---

# FILE 13 of 13: skills/format-finalize/SKILL.md

---
name: format-finalize
description: Final mechanical assembly. Builds bibliography.bib from accumulated footnote citations, assembles the master book.adoc, and validates with asciidoctor dry-run. Does not touch prose — that is line-edit's job, already complete.
---

# format-finalize

## For the human

Pure mechanical stage. All prose is final. This skill:
- Parses every footnote citation across all chapters and the comparative chapter.
- Produces `bibliography.bib` with one entry per unique source.
- Cross-checks against `sources.yaml` whitelist — any cited source not on the whitelist is a finding.
- Assembles the master `book.adoc`.
- Dry-runs Asciidoctor to PDF and EPUB to catch format-level errors.

No prose is changed. If this stage finds a problem requiring prose change, it reports it and stops.

## Inputs
- All `chapters/NN-<slug>.edited.adoc`
- `comparative.adoc` (edited)
- `sources.yaml`
- Front-matter and back-matter text (dedication, preface, index, etc. — optional)

## Agent instructions

### 1. Bibliography extraction
Parse every footnote across all chapters. For each unique source, produce a BibTeX entry. Use the `id` from `sources.yaml` as the citation key. Cross-check: any cited source not in `sources.yaml` whitelist is a HIGH finding — stop and report.

### 2. Master assembly
Produce `book.adoc`:
```asciidoc
= <Book Title>
<Author>
:doctype: book
:toc: left
:sectnums:
:bibtex-file: bibliography.bib
:bibtex-style: chicago-author-date

include::front-matter.adoc[]

include::chapters/01-<slug>.edited.adoc[]
include::chapters/02-<slug>.edited.adoc[]
// ... in toc.yaml order ...

include::comparative.adoc[]

include::back-matter.adoc[]
```

### 3. Validation
Dry-run both rendering paths:
- `asciidoctor-pdf --verbose --failure-level=WARN -o /tmp/validate.pdf book.adoc`
- `asciidoctor-epub3 --verbose --failure-level=WARN -o /tmp/validate.epub book.adoc`

Any warning or error is reported.

### 4. Output
- `book.adoc` (master)
- `bibliography.bib`
- `validation-report.md` (asciidoctor output, any findings)
- Rendered `book.pdf` and `book.epub` as build artifacts.

## Self-check
- No `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:` markers remain anywhere. (Grep all includes.)
- Every footnote citation resolves to a bibliography entry.
- Every bibliography entry is on the whitelist.
- Asciidoctor dry runs exit clean.

---

