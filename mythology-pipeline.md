# Mythology Book Pipeline — Full Pack for Review

This document contains the full pipeline: the README (overview and principles), the CHANGELOG, and all fifteen skill files (step-by-step instructions for each stage). Each section is marked with a `FILE N of 17` header.

---

# FILE 1 of 17: README.md

# Mythology Book Pipeline

A step-by-step process for producing mythology books in the style of Isaac Asimov's non-fiction: clear, plain-English retellings of myths, one culture per book, with every factual claim traced to a scholarly source. The process uses multiple AI agents (Claude, GPT, Gemini, etc.) working in sequence, each doing one job and being checked by a different AI. It handles the hard parts of mythology writing: gaps in ancient texts, contradictory versions of the same story, and the constant risk of mixing up material from neighboring cultures.

## Core principles

1. **The writer and the checker must be different AIs.** The AI that writes a chapter must not be the one that checks it. Use a different AI model (e.g., Claude writes, GPT checks), and start a fresh conversation for the check so the checker has no memory of the writing process. Self-review catches almost nothing.

2. **Three files govern the entire book.** Three files are created early and must be read by every AI and every human before starting any later stage:
   - `scope.md` — what culture, period, and sources the book covers, and what it explicitly excludes.
   - `sources.yaml` — the approved list of scholarly sources (whitelist) and banned popularizations (blacklist).
   - `glossary.yaml` — the locked English translations for key terms (created after the scope, before any writing begins).

   These are the single source of truth. If an AI or human is unsure whether something belongs in the book, these files have the answer.

3. **Cite only sources you can see.** When writing, the AI may only cite sources whose text has been pasted into the conversation or retrieved during it. No citing from the AI's training memory, even for famous texts. This is the main defense against fabricated references — a common AI failure mode.

4. **Contradictions between sources are normal, not errors.** Ancient mythologies have multiple versions of the same story. Two legitimate sources disagreeing is part of the record, not a mistake. The pipeline handles this explicitly: when one version dominates the scholarly record, it goes in the main text with alternatives in footnotes. When versions are roughly equal, they are presented side by side. The key is to never silently pick one and ignore the others.

5. **Check the document, not the deity.** When checking whether something belongs in the book, the question is: "Does this specific story detail appear in a document from within our scope?" — not "Does this god belong to our culture?" Gods and heroes cross cultural boundaries; specific narrative details are tied to specific texts. A detail found only in a Babylonian tablet does not belong in a Sumerian book, even if the god is originally Sumerian.

6. **Chapter length follows the evidence.** A myth preserved on a single broken tablet gets a short chapter. A richly-documented cycle gets a long one. Chapters are never padded to reach a target length.

## Stage order

The book is built in stages. Each stage produces a file that the next stage consumes. `[HUMAN]` marks points where you review and approve before continuing. The arrows show what feeds into what:

```
scope-lock → story-inventory → inventory-audit → [HUMAN ~15min] →
  chapter-briefs → glossary-lock →
  intro-chapter → chapter-factcheck(intro) →
  [per chapter:
    chapter-claims → chapter-factcheck(claims) → [HUMAN resolves findings] →
    chapter-draft → narrative-fidelity] →
  comparative-chapter → marker-resolve → line-edit →
  character-appendix → chapter-factcheck(appendix) →
  format-finalize
```

**In plain English:** First you define what the book covers and what sources are allowed (scope-lock). Then an AI researches all the stories in that mythology (story-inventory), and a different AI checks the list (inventory-audit). You review, then the approved list is turned into one planning document per chapter (chapter-briefs) and a locked glossary of key terms (glossary-lock). An introductory chapter on cultural context is written and fact-checked. Then, for each story chapter: the facts are written out one by one (chapter-claims), checked (chapter-factcheck), you review, then the facts are turned into narrative prose (chapter-draft), and a different AI confirms the prose faithfully represents the facts (narrative-fidelity). After all chapters are done, a cross-cultural comparison chapter is written. All chapters get their placeholder markers converted to final text (marker-resolve), then a prose-quality polish (line-edit). A character reference appendix is compiled and fact-checked. Finally, everything is assembled into a book with a bibliography and validated (format-finalize).

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
    00-introduction.adoc          (intro chapter — cultural relevance)
    00-introduction.factcheck.yaml
    00-introduction.resolved.adoc
    00-introduction.edited.adoc
    00-introduction.diff.md
    01-<slug>.claims.adoc         (factual skeleton — one claim per paragraph)
    01-<slug>.claims.factcheck.yaml (claims audited)
    01-<slug>.claims.approved.adoc  (after human review)
    01-<slug>.adoc                (Asimov narrative from verified claims)
    01-<slug>.fidelity.yaml       (narrative-vs-claims fidelity review)
    01-<slug>.resolved.adoc       (markers resolved)
    01-<slug>.edited.adoc         (line-edited)
    01-<slug>.diff.md             (line-edit diff for review)
    ...
  comparative.adoc
  character-appendix.adoc           (character reference)
  character-appendix.factcheck.yaml
  book.adoc                         (master)
  bibliography.bib
  validation-report.md
```

## Output format

AsciiDoc, rendered via Asciidoctor (not Pandoc) to PDF and EPUB. Pandoc is still useful for DOCX export if needed.

## What changed from v1

See `CHANGELOG.md`.

---

# FILE 2 of 17: CHANGELOG.md

# Changelog

## v2

**New skills**
- `chapter-claims` — produces a factual skeleton for each story chapter: one claim per paragraph, each individually cited. This is the first step of a two-step drafting process that separates factual research from prose craft, making fact-checking dramatically more reliable.
- `narrative-fidelity` — audits that the Asimov-style narrative faithfully represents the fact-checked claims: nothing dropped, nothing added, nothing distorted. Runs after `chapter-draft`, different model.
- `intro-chapter` — produces an introductory chapter framing the cultural relevance of every myth: centrality (central/significant/marginal, with evidence), function in the culture (cosmological, ritual, political, etc.), and cross-cultural resonance (preview of comparative chapter). Runs after `glossary-lock`, goes through `chapter-factcheck` like any other chapter.
- `character-appendix` — produces a back-matter appendix cataloguing every named character in the book. Each entry includes cross-references to chapters, physical description (only if attested in in-scope sources — never fabricated), myths in which the character appears, and relevance in the mythology. Runs after `line-edit`, goes through factcheck before `format-finalize`.
- `glossary-lock` — locks English renderings of recurring terms before drafting.
- `marker-resolve` — resolves inline markers into final AsciiDoc constructs before line-editing (split from v1 `format-finalize`).

**Two-step drafting (claims → narrative)**
- The former single `chapter-draft` stage is now split into `chapter-claims` (factual skeleton) → `chapter-factcheck` (verify isolated claims) → `chapter-draft` (Asimov narrative from verified claims) → `narrative-fidelity` (confirm nothing dropped or added). Fact-checking operates on isolated, individually cited claims rather than claims embedded in flowing prose — eliminating the hardest part of the old audit (extracting claims from narrative).

**New marker**
- `[RECONSTRUCTION:]` — content filled from another in-tradition source per scope's reconstruction policy, distinct from uncited `[INFERENCE:]`.

**Stronger audits**
- `chapter-factcheck`: quote-to-claim requirement (every ✓ needs a verbatim quote); triangulation against scholarly databases; reverse-order second pass; three-way distinction between internal variance (not a finding), contamination (finding), and fabrication (finding); verification unit moved from sentence to claim. Now operates on claims documents (one claim per paragraph) for story chapters, making verification straightforward.
- `inventory-audit`: document-provenance contamination (not entity-provenance); quote-to-evidence on every HIGH finding; identifier verification.

**Draft discipline**
- `chapter-draft`: now takes verified claims as input rather than raw sources; forbidden from introducing new factual claims; provided-sources-only rule enforced at claims stage; forbidden-words list; concrete Asimov exemplar passage; required sub-fields on all markers; explicit variant-handling rule (single-prevalent → footnotes; co-equal → inline).

**Brief enrichment**
- `chapter-briefs`: new `cultural_relevance` section per story — centrality classification with evidence, function attributions with sources, and cross-cultural parallel pointers. Feeds `intro-chapter`.

**Scope explicitness**
- `scope-lock`: requires explicit contamination-risk list with user confirmation; requires reconstruction policy defining what counts as "in-tradition" fill source; requires variant presentation policy.

**Inventory rigor**
- `story-inventory`: verifiable identifiers (DOI / ISBN / museum number / corpus ID) required, not just URLs.

**Format stage split**
- Former `format-finalize` split into `marker-resolve` (prose-level, runs before line-edit) and `format-finalize` (mechanical assembly only, runs after line-edit).

## v1
Initial pipeline: scope-lock, story-inventory, inventory-audit, chapter-briefs, chapter-draft, chapter-factcheck, comparative-chapter, line-edit, format-finalize.

---

# FILE 3 of 17: skills/scope-lock/SKILL.md

---
name: scope-lock
description: Interactive conversation run once at the start of each book. Produces scope.md and sources.yaml — the two files that define what belongs in the book and what doesn't. Every later stage reads them.
---

# scope-lock

## For the human

This is where you define what the book is and, equally importantly, what it is not. A Sumerian book is not a Mesopotamian book. A Norse book is not a Germanic book. Without a locked scope, the research, drafting, and checking stages drift: material from neighboring cultures seeps in, and by the time anyone notices, it's woven through every chapter.

This step runs once, at the very start. It produces two files — `scope.md` (what the book covers and excludes) and `sources.yaml` (which scholarly sources are approved and which are banned). Every AI working on every later stage reads these two files before doing anything. They are the rulebook for the entire book.

This step is a conversation between you and the AI. The AI will ask you questions about the book's boundaries. Don't accept vague answers from yourself — the more specific you are here, the fewer problems you'll have later. Three decisions matter most:

1. **Which neighboring cultures to exclude.** For a Sumerian book, the main risk is Akkadian/Babylonian material leaking in. For a Norse book, it's continental Germanic and Christianized sagas. The AI will propose specific exclusions with reasons; you confirm or adjust.

2. **What counts as a legitimate gap-fill.** Ancient texts have physical gaps — broken tablets, lost pages. The pipeline allows filling those gaps from other texts in the same tradition, clearly marked. You need to define what "same tradition" means for this book (e.g., "any Sumerian literary text from within 400 years of the damaged one").

3. **Which sources are approved.** The AI will propose 8–15 scholarly sources (critical editions, standard reference works) and a blacklist of popularizations that should never be cited. You approve or edit the lists.

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

# FILE 4 of 17: skills/story-inventory/SKILL.md

---
name: story-inventory
description: Produces a structured list of every story the book will cover, each with verifiable scholarly references. Best run with a research-capable AI (Gemini Deep Research or equivalent) that can search many sources at once. Output is inventory.yaml.
---

# story-inventory

## For the human

This step produces what is essentially the book's table of contents — the list of stories it will cover. All the research happens here, not during writing. Everything that follows depends on this list being accurate and staying within the book's scope.

The main risk is invented stories: the AI producing entries for stories that sound plausible for the culture but aren't actually documented in real sources, or confusing stories from one culture with those of a neighboring one. (AI models do this regularly — they "know" enough about a mythology to produce convincing-sounding entries that don't correspond to any real text.)

The defense is strict sourcing. Every story in the list must carry a verifiable reference — not a generic web link (which can be a dead link or a homepage), but something a scholar could look up: a catalogue number (like ETCSL 1.4.1), a museum tablet number (like BM 92687), an ISBN, or a DOI. Entries where no such reference can be found are flagged as uncertain rather than silently included or dropped.

Best run with a research-capable AI (like Gemini Deep Research) that can search many scholarly databases in one pass.

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

# FILE 5 of 17: skills/inventory-audit/SKILL.md

---
name: inventory-audit
description: Checks the story inventory for errors before any writing begins. Must be run by a different AI model than the one that produced the inventory, in a fresh conversation. Catches material from wrong cultures, made-up references, missing well-known stories, and silently merged variants.
---

# inventory-audit

## For the human

This is the first major quality check. It reviews the story list before any chapters are written. Catching errors here costs minutes; catching them after chapters are drafted costs hours.

The audit checks four things:

1. **Wrong-culture material.** Did any stories or story details sneak in from a neighboring culture? The tricky part: you can't just check "does this god belong to our culture?" — the same god often appears in multiple cultures. The real question is: "Does this specific plot detail appear in a document that was written within our culture and period?" A story detail found only in a Babylonian tablet doesn't belong in a Sumerian book, even if the god in question is originally Sumerian.

2. **Fake or wrong references.** AI models sometimes invent plausible-looking scholarly references. The auditor actually looks up each catalogue number, museum number, or ISBN to confirm it exists and contains what was claimed.

3. **Missing stories.** Are there well-known stories from this mythology that the inventory left out? The auditor cross-checks against standard reference works.

4. **Silently merged variants.** When multiple versions of a story exist, the inventory should list them separately. If it quietly combined two versions into one summary, that's a problem.

This audit must be run by a different AI model than the one that produced the inventory, in a fresh conversation (so the auditor has no memory of the work it's checking). An AI reviewing its own work in the same conversation catches almost nothing.

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

# FILE 6 of 17: skills/chapter-briefs/SKILL.md

---
name: chapter-briefs
description: Converts the approved story list into one planning document per chapter. Each brief specifies what sources to use, what gaps exist in the text, how to handle variant versions, how important the story was in its culture, and how long the chapter should be.
---

# chapter-briefs

## For the human

This step produces a planning document (a "brief") for each chapter. No actual prose is written yet — the brief is a structured dossier that tells the AI everything it needs to know before writing. Getting the brief right means the writing AI has everything it needs and doesn't have to improvise or guess.

Three things the brief must get right:

1. **How to handle different versions.** Many myths exist in multiple versions. For each story, the brief records what the known versions are and whether one clearly dominates the scholarly record. This directly determines how the chapter will be written: if one version dominates, it goes in the main text with alternatives in footnotes. If versions are roughly equal, they're presented side by side in the text.

2. **Chapter length.** The brief sets a target word count based on how much primary source material actually exists for this story — not based on how "important" the story feels. A myth preserved on a single broken tablet gets a short chapter (600–1200 words). A richly-documented multi-tablet cycle gets a long one (up to 15,000 words). The AI is told not to pad.

3. **Cultural relevance.** For the introductory chapter, the brief records how important this story was in its culture (central, significant, or marginal — with evidence), what function it served (religious, political, educational, etc.), and what parallels exist in other cultures.

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

### Cultural relevance assessment
For each story, gather evidence for three aspects that will feed the introductory chapter:

**Centrality**: How important was this story in the culture? Look for:
- Number of surviving copies or attestations.
- Ritual or festival contexts in which the story was recited or performed.
- Iconographic evidence (seals, reliefs, pottery).
- Royal inscriptions that invoke or reference the story.
- Volume of scholarly attention.

Classify as **central**, **significant**, or **marginal**. Cite the evidence. If evidence is thin, say so — do not inflate.

**Function**: What role did the story serve? Common categories: cosmological, theogonic, royal-legitimation, ritual-aetiological, didactic, eschatological, entertainment/literary. A story may serve multiple functions. Cite basis.

**Cross-cultural parallels (brief)**: Note the 1–3 most striking parallels in other traditions, with source pointers. These feed both the introductory chapter (preview) and the comparative chapter (full analysis). Keep to 1–2 sentences each.

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

cultural_relevance:
  centrality: central | significant | marginal
  centrality_evidence:
    - kind: attestation-volume | ritual-context | iconography | royal-inscription | scholarly-attention
      detail: <one sentence>
      source: <id + loc>
  function:
    - role: cosmological | theogonic | royal-legitimation | ritual-aetiological | didactic | eschatological | literary
      basis: <one sentence>
      source: <id + loc>
  cross_cultural_parallels:
    # Brief pointers — expanded in intro-chapter and comparative-chapter
    - other_culture: <name>
      parallel: <one sentence>
      source: <id>

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
- Every brief has a `cultural_relevance` section with centrality, function, and cross-cultural parallels — none blank.
- Every centrality classification cites at least one piece of evidence.
- Every function attribution cites a source.
- Every brief has a triangulation database list (at least one).
- `toc.yaml` contains all chapters in order, starting with `00-introduction`.

## Handoff
To `glossary-lock`, which runs once over all briefs before any drafting. The `cultural_relevance` fields also feed `intro-chapter`.

---

# FILE 7 of 17: skills/glossary-lock/SKILL.md

---
name: glossary-lock
description: Locks the English translation for recurring terms and proper nouns before any chapter is written. Prevents inconsistency across chapters and false contradictions during fact-checking. Interactive — the AI proposes, you decide.
---

# glossary-lock

## For the human

Scholars translate key terms differently. For example, the Sumerian word *me* is translated as "divine powers" (Kramer), "cosmic ordinances" (Jacobsen), or left untranslated (Black). If the writing AI picks one translation and the fact-checking AI is reading a source that uses a different one, the fact-checker will flag a false contradiction — the claim is correct, it's just using a different translation of the same word. And if different chapters use different translations of the same term, the book reads as if multiple people wrote it without coordinating.

This step solves both problems by locking in a single English translation for each recurring term before any chapter is written. Usually 10–30 terms per book. It's interactive: the AI proposes options for each term (with reasons), and you pick the one you prefer or supply your own.

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
`glossary.yaml` to `intro-chapter` and `chapter-draft`.

---

# FILE 8 of 17: skills/intro-chapter/SKILL.md

---
name: intro-chapter
description: Produces the introductory chapter that frames the cultural relevance of every myth covered in the book. For each myth: was it central or marginal? What function did it serve? How does it resonate across cultures?
---

# intro-chapter

## For the human

This chapter is the reader's first encounter with the mythology as a living cultural system — not yet the stories themselves, but the frame that makes them intelligible. Without it, the reader goes into a retelling of, say, the Descent of Inanna without knowing whether Sumerians treated this as a central cosmological narrative or a minor literary curiosity. That context changes how the retelling lands.

The chapter answers three questions for each myth, based on scholarly evidence:

1. **How important was it?** A creation myth recited at the New Year festival is not the same as a scribal exercise preserved in one school tablet. The evidence comes from: how many copies survive, whether it was used in rituals, whether it shows up in art (cylinder seals, reliefs), whether kings invoked it, and how much scholarly attention it has received.

2. **What did it do?** Myths are not just stories — they legitimate kingship, explain rituals, encode how the world works, teach students, mark seasonal transitions. Knowing that a myth was recited at a political ceremony changes how you read it. The reader should know this before encountering the retelling.

3. **Where else does this theme appear?** A brief preview — not the full analysis, which comes in the comparative chapter at the end — of where this myth's themes show up in other cultures. This gives the reader something to watch for as they read, and prepares them for the cross-cultural discussion later.

This chapter makes factual claims about cultural significance, so it goes through the same fact-checking process as any other chapter: a different AI checks every claim against sources.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- All `briefs/*.yaml` (especially the `cultural_relevance` fields)
- `toc.yaml`
- Primary and secondary sources — pasted into the conversation or accessible via fetch

## Agent instructions

### Structure

The chapter opens with a brief overview of the culture's mythological corpus as a whole — its size, state of preservation, and the scholarly tradition around it. Then one section per myth (or per cycle, if the book groups stories into cycles), following `toc.yaml` order. A closing section synthesizes patterns: which types of myth were most important to this culture, what that reveals about its worldview, and a forward pointer to the comparative chapter.

### Per-myth section

For each myth or cycle, address three questions:

**1. Centrality in the culture**
How important was this myth? Evidence types, in order of strength:
- **Attestation volume**: how many copies survive? A myth preserved on dozens of tablets was widely copied; one preserved on a single fragment was not.
- **Ritual context**: was the myth recited, performed, or enacted in known rituals? (e.g., the Enuma Elish at the Akitu festival)
- **Iconographic record**: does the myth appear in visual art — cylinder seals, reliefs, pottery?
- **Royal appropriation**: did kings cite or invoke the myth in inscriptions?
- **Scholarly discussion**: how much attention has the myth received in the academic literature?

Classify as **central**, **significant**, or **marginal**, with explicit evidence. Do not guess — if the evidence is thin, say so.

**2. Function in the culture**
What role did the myth serve? Common functions (adapt to the culture):
- **Cosmological**: explains the origin or structure of the world.
- **Theogonic**: establishes the divine hierarchy.
- **Royal-legitimation**: grounds political authority in divine action.
- **Ritual-aetiological**: explains the origin of a rite or festival.
- **Didactic**: teaches moral or social norms (common in scribal-school contexts).
- **Eschatological**: addresses death, the afterlife, or cosmic endings.
- **Entertainment/literary**: valued primarily as narrative art.

A myth may serve multiple functions. Cite the scholarly basis for each attribution.

**3. Cross-cultural resonance (preview)**
In 2–4 sentences, note the most striking parallels in other traditions. This is a preview, not the analysis — the comparative chapter handles depth. The goal is to plant a seed: "When you read this retelling, notice X, because you will encounter something remarkably similar in Y tradition."

Cite both the in-scope source and the out-of-scope parallel. Use `// COMPARATIVE-HOOK:` comments for anything that should be expanded in the comparative chapter.

### Style

Asimov register, same as the rest of the book. The reader is intelligent and uninformed. No reverence, no mystification. Plain, clear prose that treats mythology as evidence about a culture, not as sacred text.

Same forbidden-words list as `chapter-draft`. Same glossary discipline: use `glossary.yaml` renderings, gloss on first mention.

### Citations

Same rules as `chapter-draft`: cite only sources provided in the conversation or fetched via tool use. AsciiDoc footnotes. Every claim about centrality, function, or cross-cultural resonance needs a citation.

### Markers

Same marker discipline as `chapter-draft`:
- `[INFERENCE:]` for claims about function or centrality that go beyond what sources explicitly state.
- `[LACUNA:]` if evidence for a myth's cultural role is missing due to gaps in the record.
- No `[RECONSTRUCTION:]` or `[VARIANT:]` — these apply to narrative content, not to cultural-relevance framing.

### Length

Scale to the number of myths. For a book with 8–12 chapters: 3000–6000 words. For a larger book (15+ chapters): 6000–10000 words. Do not pad.

## Output: `chapters/00-introduction.adoc`

```asciidoc
== Introduction: The Myths and Their World

<Opening — the mythology as a corpus: size, preservation, scholarly tradition.>

=== <Myth/Cycle Title>

<Centrality — evidence-based assessment.>

<Function — what role it served, with citations.>

<Cross-cultural resonance — brief preview, 2–4 sentences.>

// COMPARATIVE-HOOK: <detail for comparative chapter>

=== <Next Myth/Cycle Title>
...

=== Patterns and Worldview

<Synthesis — what the distribution of central vs marginal myths reveals about this culture. Forward pointer to comparative chapter.>
```

## Self-check before returning
1. Every centrality claim cites evidence (attestation count, ritual context, iconography, or scholarship).
2. Every function attribution cites a scholarly source. No function assigned by vibes.
3. Cross-cultural previews cite both the in-scope and out-of-scope source.
4. Glossary renderings match `glossary.yaml`. First-mention glosses present.
5. No forbidden words. No reverence. Asimov register throughout.
6. Length proportional to the number of myths — not padded, not skeletal.
7. Every marker has all required sub-fields.
8. `// COMPARATIVE-HOOK:` comments present for every cross-cultural note.

## Handoff
To `chapter-factcheck`, fresh conversation, different model — same as any chapter.

---

# FILE 9 of 17: skills/chapter-claims/SKILL.md

---
name: chapter-claims
description: Produces the factual skeleton of a single chapter — one fact per paragraph, each with its own citation. This is step 1 of a two-step writing process: first the facts are written and verified, then the narrative prose is created from the verified facts.
---

# chapter-claims

## For the human

This is the first half of a deliberate split between "getting the facts right" and "writing beautiful prose."

Instead of asking the AI to write flowing Asimov-style narrative and then trying to check the facts buried inside it, we write the facts first — one per paragraph, each with its own source reference — and only write the narrative after the facts have been verified.

Why this matters: when an AI writes a beautiful paragraph of narrative prose, it is simultaneously researching, citing, connecting, and styling. These tasks interfere with each other. The AI fills gaps to smooth transitions, reaches for evocative phrasing that drifts from the source, and buries factual claims in connective tissue that makes them hard to check. By separating the factual skeleton from the prose, we let the AI do one job at a time, and we give the fact-checker a document where each paragraph is a single, individually cited claim — trivially easy to verify compared to extracting claims from flowing prose.

The output of this stage is not text the reader will ever see. It is a verified blueprint — a list of numbered facts — that the next stage (`chapter-draft`) will transform into the final narrative.

## Hard rules
1. Cite only sources whose text has been provided to you in this conversation or fetched by you via tool use. No citing from memory, even confidently.
2. Use exactly the English renderings locked in `glossary.yaml`. If a needed term is missing, stop and ask.
3. Omit material from excluded cultures. Note the temptation in a `// COMPARATIVE-HOOK:` comment for the comparative chapter.
4. One claim per paragraph. No bundling. No narrative connective tissue.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- One chapter brief (`briefs/NN-<slug>.yaml`)
- Primary source translations — pasted into the conversation or accessible via fetch

## What is a claim?

A claim is a single factual assertion about the myth: who did what, when, why, in what order, with what consequence. Each of the following is a separate claim:

- An event ("Inanna descended to the underworld")
- A character identification ("Ereshkigal was Inanna's sister and queen of the underworld")
- A causal relationship ("Inanna was detained because she violated the laws of the underworld")
- A physical description ("The text describes Enkidu as hairy-bodied")
- A ritual or cultural detail ("The myth was recited during the Akitu festival")
- A scholarly observation ("The tablet is broken at this point; approximately 20 lines are lost")

A narrative transition ("Having secured the divine powers, Inanna turned her attention to the underworld") is **not** a claim — it is connective tissue that belongs in `chapter-draft`, not here.

## Structure of a claim paragraph

Each paragraph contains exactly:
1. **The claim** — one factual assertion, in plain language.
2. **The citation** — AsciiDoc footnote pointing to the specific source, location, and (where possible) a verbatim quote or close paraphrase from the source.

```
Enlil separated heaven (An) from earth (Ki), creating the space in which the atmosphere exists.footnote:[Black et al. 2004, ETCSL 1.1.2, lines 1–5: "After heaven had been moved away from earth, after earth had been separated from heaven, after the name of man had been fixed..."]
```

## Ordering

Follow the narrative order of the myth as attested in the primary source(s). Where the brief specifies an ordering (e.g., following the tablet sequence), follow it. The claims should form a complete, ordered skeleton of the story — everything the narrative will need.

## Variant handling (from brief)

- If `variants.classification` is **single-prevalent**: list claims from the prevalent version. Add separate claims for each significant alternate, marked with `[VARIANT:]`.
- If **co-equal**: list claims from each version in sequence, each attributed to its source.

## Markers (required sub-fields)

Same markers as the rest of the pipeline, but used at the claim level:

- `[INFERENCE: <claim> | basis: <why this bridge is reasonable> | risk: <what is speculative>]`
  — A claim that bridges two attested claims. Needed to make the story skeleton coherent, but not directly attested. The fact-checker will verify the inference is genuinely inferential (not secretly attested) and that the basis is sound.
- `[LACUNA: <what is missing> | source: <exact ref> | scholarly_reconstruction: <if any, with citation>]`
  — A documented physical gap in the source.
- `[RECONSTRUCTION: <filled content> | gap_source: <where the lacuna is> | fill_source: <which in-tradition source supplies the content, per scope.md's reconstruction policy> | confidence: high|medium|low]`
  — Content filled from another in-tradition source per the reconstruction policy.
- `[VARIANT: primary=<source A, short quote> | alt=<source B, short quote> | chosen: A|B | reason: <why>]`
  — For single-prevalent cases. Co-equal variants are listed as separate attributed claims without a marker.

## Comparative hooks

End the claims document with a section of `// COMPARATIVE-HOOK:` comments collecting cross-cultural parallels noticed during the claim extraction. These are not claims — they are notes for the comparative chapter.

## Output: `chapters/NN-<slug>.claims.adoc`

```asciidoc
== <Chapter Title> — Claims

// This is a claims document, not final prose. Each paragraph is one verifiable claim.
// After fact-check and human review, chapter-draft will transform this into narrative.

=== Setting and context

<Claim 1 — one paragraph, one citation.>

<Claim 2 — one paragraph, one citation.>

=== Narrative sequence

<Claim 3>

[LACUNA: <...>]

<Claim 4>

[INFERENCE: <...>]

<Claim 5>

=== Variants

[VARIANT: <...>]

<Alternate claim from different source>

// COMPARATIVE-HOOK: <detail for comparative chapter>
// COMPARATIVE-HOOK: <detail for comparative chapter>
```

## Self-check before returning
1. Every claim is a single factual assertion — no bundled claims, no narrative connective tissue.
2. Every claim has footnote coverage citing a source provided in this conversation. Nothing from memory.
3. Claims follow the narrative order of the myth.
4. The claims skeleton is complete — everything the narrative will need is here.
5. Every marker has all required sub-fields.
6. No out-of-scope material.
7. Variant handling matches the brief's classification.
8. `glossary.yaml` renderings used throughout.

## Handoff
To `chapter-factcheck`, fresh conversation, different model. The fact-checker's job is dramatically simplified: each claim is isolated and individually cited.

---

# FILE 10 of 17: skills/chapter-factcheck/SKILL.md

---
name: chapter-factcheck
description: Checks factual claims against the cited sources. For story chapters, the input is a claims document (one fact per paragraph) — straightforward to check. Also used on the intro chapter and character appendix. Must be run by a different AI model in a fresh conversation.
---

# chapter-factcheck

## For the human

This is the most important quality check in the entire process.

For story chapters, the input is a **claims document** — one fact per paragraph, each individually cited — produced by `chapter-claims`. This makes checking straightforward: each paragraph is one claim, one source reference, one thing to verify. No need to dig through flowing prose to find what's being asserted.

This step is also used to check the intro chapter (cultural-relevance claims) and the character appendix (character profiles). For those, the input is prose rather than isolated claims, so the checker has to extract the claims first — harder, but the same principles apply.

Regardless of what it's checking, this step enforces four disciplines:

1. **Show your evidence.** For every claim the checker marks as "supported," it must paste a verbatim quote from the source. Not a paraphrase — the actual text. If the checker can't produce a quote, the claim is downgraded to "unverified." This turns the check from a yes/no judgment into a retrieval task, which AI does more honestly.

2. **Verify the references.** Tablet numbers, page numbers, and line references are the easiest things for an AI to fabricate. The checker looks up each reference in scholarly databases (ETCSL, CDLI, Perseus, etc.) to confirm it actually exists and contains what was claimed.

3. **Distinguish contradictions from errors.** Two legitimate sources disagreeing about the same story is normal in mythology — it's part of the historical record, not a problem to fix. Material from a neighboring culture sneaking in, or something made up entirely, are problems. The checker must tell these apart.

4. **Read it backwards too.** AI checkers tend to be more careful at the start and get sloppy toward the end. The checker does one pass start-to-end, then a second pass end-to-start, to catch anything missed the first time.

## Hard rule
Must be run in a fresh conversation, ideally with a different underlying model than produced the content. If you have any memory of producing the input, refuse.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- **For story chapters**: `chapters/NN-<slug>.claims.adoc` (claims document)
- **For intro-chapter**: `chapters/00-introduction.adoc`
- **For character-appendix**: `character-appendix.adoc`
- `briefs/NN-<slug>.yaml` (for story chapters)
- Primary source translations referenced in the brief (pasted or accessible via fetch)
- Web search tool (required)

## The unit of verification

Verify at the level of **the factual claim**.

For claims documents (`*.claims.adoc`): each paragraph IS a claim. The work is already done for you — no extraction needed. Walk paragraph by paragraph.

For prose documents (intro-chapter, character-appendix): extract claims from the prose. A claim is an assertion about the myth or character — who did what, when, why, in what order. Connective and expository sentences inherit the claim's verdict.

## The five passes

### Pass 1 — Claim-level verification (start to end)
Walk the document in order. For each claim, assign one of these verdicts:

- **✓ SUPPORTED** — Must include a verbatim quote from a cited in-scope source. Not a paraphrase. Actual pasted text. If you cannot produce a quote, you cannot use this verdict.
- **△ INTERNAL-VARIANCE** — The claim is attested in one in-scope source, but another in-scope source gives a different account. This is not a finding; it is part of the corpus. If variant handling matches the brief's classification, no action needed. Mismatch is MEDIUM.
- **? UNVERIFIED** — No supporting quote found in provided sources. Default when uncertain.
- **! CITATION-WRONG** — Claim is correct but the citation points to a wrong source, page, or line number.
- **⚠ CONTAMINATION** — Claim is supported, but the supporting source is from an excluded culture per `scope.md`. Include the out-of-scope quote as evidence.
- **✗ FABRICATION** — Claim is not supported by any source, in-scope or out-of-scope, that you can locate.

### Pass 2 — Triangulation of references
For every citation with a specific tablet number, line range, manuscript folio, or page reference, verify it resolves in a `triangulation_databases` entry. Non-resolving references: CITATION-WRONG, HIGH severity, with verification URL.

### Pass 3 — Document-provenance contamination scan
For each specific factual detail, ask: is this detail attested in a document whose physical composition falls within the scope's date range and culture?

Attestation of the *entity* across cultures is not enough. The question is whether *this narrative detail* appears in an in-scope document. Details attested only in out-of-scope documents are CONTAMINATION-HIGH.

### Pass 4 — Marker integrity
- `[INFERENCE:]` — check the inference is genuinely inferential. If an in-scope source directly attests the claim, flag MARKER-MISUSED.
- `[LACUNA:]` — check the source actually has the claimed gap. If the source is complete at that point, flag MARKER-FABRICATED.
- `[RECONSTRUCTION:]` — verify the `fill_source` is in-tradition per `scope.md`'s reconstruction policy.
- `[VARIANT:]` — verify both quoted phrases are present in their cited sources.
- **Silent bridges** — claims presented as fact that aren't in any source and aren't under a marker. In claims documents these are easy to spot (each paragraph is one claim — is it cited?). Flag SILENT-BRIDGE with HIGH severity.

### Pass 5 — Reverse-order second pass
Walk the document from last claim to first, hunting for anything Pass 1 missed due to lead bias. Pay particular attention to the final third. Add any new findings.

**Note on glossary and style**: For claims documents, glossary consistency is checked but style is not — there is no prose to style-check yet. Style review happens in `narrative-fidelity` after `chapter-draft`. For prose documents (intro-chapter, character-appendix), check glossary renderings and `never_use` terms.

## Output

**For story chapters**: `chapters/NN-<slug>.claims.factcheck.yaml`
**For intro-chapter**: `chapters/00-introduction.factcheck.yaml`
**For character-appendix**: `character-appendix.factcheck.yaml`

```yaml
meta:
  auditor_model: <name and version>
  input_file: <path to audited file>
  input_format: claims-document | prose
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

supported_claims:
  # Every ✓ verdict with its verbatim quote. If this list is short, you didn't do the work.
  - claim_number: <n>
    claim: "<the claim, in your words>"
    source_id: <from sources.yaml>
    source_loc: <tablet/line/page>
    verbatim_quote: "<exact text from source>"

findings:
  - claim_number: <n>
    kind: UNVERIFIED | CITATION-WRONG | CONTAMINATION | FABRICATION | SILENT-BRIDGE | MARKER-MISUSED | MARKER-FABRICATED | GLOSSARY-VIOLATION | VARIANT-HANDLING-MISMATCH
    severity: HIGH | MEDIUM | LOW
    claim: "<the claim>"
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
5. Am I the same model that produced the input? If yes, this audit is not valid.

A partial honest audit is more useful than a complete dishonest one. If you cut corners, say so.

## Human review protocol
Review HIGH findings (~10 minutes), skim MEDIUM, ignore LOW unless maximum rigor is desired. For story chapter claims: apply accepted fixes to produce `chapters/NN-<slug>.claims.approved.adoc` for `chapter-draft`.

---

# FILE 11 of 17: skills/chapter-draft/SKILL.md

---
name: chapter-draft
description: Transforms the verified facts into Asimov-style narrative prose. The AI's only job is writing — the facts are already checked. No new facts may be introduced. Every verified claim must appear in the narrative, and nothing unverified may be added.
---

# chapter-draft

## For the human

This is the creative stage — and it is much safer now that the facts are already locked. The AI is not simultaneously researching, citing, and writing. It is only writing. The factual skeleton has already been written and verified. The AI's job is to turn a list of numbered, checked facts into a narrative that reads like Asimov at his best.

The main risk is no longer inventing facts (those are locked) but **drift during the prose transformation**: dropping a verified fact because it doesn't fit the narrative flow, softening a claim until its meaning changes, or inserting a "helpful" detail that was never in the verified facts. The next step (`narrative-fidelity`) will catch these, but the writing AI should work to prevent them.

Importantly, the writing AI does **not** receive the original source texts. It only receives the verified claims document. This is deliberate: giving it the sources would tempt it to "improve" the chapter with additional details that were never fact-checked.

## Hard rules
1. **Every factual assertion in the narrative must correspond to a claim in the approved claims document.** No new facts, no new citations, no "I happen to know" additions.
2. **Every claim in the approved document must appear in the narrative.** Do not silently drop claims because they are inconvenient for the prose flow. If a claim is genuinely irrelevant, flag it rather than omitting it.
3. Use exactly the English renderings locked in `glossary.yaml`.
4. All markers from the claims document survive into the narrative. Do not paraphrase them away.
5. Citations carry over from the claims document. Do not add, remove, or reassign footnotes.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- `chapters/NN-<slug>.claims.approved.adoc` (fact-checked, human-reviewed claims)
- `briefs/NN-<slug>.yaml` (for variant classification, target length, special instructions)

**Not** primary source translations. The drafter does not need the sources — the claims document already contains everything verified. Providing sources would tempt the drafter to "improve" claims with additional details.

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

## Narrative transitions

The claims document has no connective tissue — that is your job. You may add:
- **Transitional sentences** that connect one claim to the next ("Having established the cosmic order, the narrative turns to...")
- **Orienting context** that helps the reader follow the story ("At this point in the text, the setting shifts to...")
- **Explanatory asides** that help the reader understand why something matters ("This is worth pausing on, because...")

These are **not** factual claims — they are prose scaffolding. They must not introduce new information about the myth. If a transition requires a factual bridge, that bridge should already be in the claims document as an `[INFERENCE:]` marker.

## Length

Per brief's `target_length_words`, driven by source volume. If you find yourself padding, stop and return the shorter version with a note.

## Output: `chapters/NN-<slug>.adoc`

```asciidoc
== <Chapter Title>

<Opening — orient the reader in time, place, and source situation.>

<Body — the verified claims, woven into narrative prose. Every claim present, no claims added.>

<Closing — brief note on the story's place in the culture's corpus. No cross-cultural comparison. Carry over `// COMPARATIVE-HOOK:` comments from claims document.>
```

## Self-check before returning
1. **Completeness**: walk the approved claims document claim by claim. Is every claim represented in the narrative? List any you cannot find — they are bugs.
2. **No additions**: scan the narrative for any factual assertion that does not correspond to a claim in the approved document. Flag it.
3. Scan for forbidden words — each hit is a drift signal; revise.
4. Every proper noun was glossed on first mention using `glossary.yaml`.
5. Variant handling matches the brief's classification.
6. Every marker has survived from claims to narrative.
7. All footnotes carried over unchanged.
8. Length matches the brief's target. Not padded.
9. `// COMPARATIVE-HOOK:` comments carried over.

## Handoff
To `narrative-fidelity`, fresh conversation, different model.

---

# FILE 12 of 17: skills/narrative-fidelity/SKILL.md

---
name: narrative-fidelity
description: Checks that the narrative prose faithfully represents the verified facts — nothing dropped, nothing added, nothing distorted. Must be run by a different AI model in a fresh conversation.
---

# narrative-fidelity

## For the human

The facts have been verified. The narrative has been written from those verified facts. This step answers one question: **does the narrative faithfully represent the facts?**

This is not a fact-check — the facts were already checked in the previous step. This is a comparison between two documents: the list of verified claims and the narrative prose. It catches three problems:

1. **Dropped facts.** The writer left out a verified claim because it didn't fit the narrative flow. The reader loses information.
2. **Added facts.** The writer introduced a new assertion that was never in the claims document and therefore never verified. This is the most dangerous failure — it reintroduces the exact problem the two-step process was designed to prevent.
3. **Distorted facts.** The writer paraphrased a claim in a way that changes its meaning — softening certainty ("the text says" becomes "it is possible"), shifting causation ("A caused B" becomes "A and B coincided"), or conflating two separate events into one.

This check must be done by a different AI model in a fresh conversation. The AI that wrote the narrative cannot reliably judge whether it drifted from the source material.

## Hard rule
Must be run in a fresh conversation with a different model than produced the narrative. If you produced the narrative, refuse.

## Inputs
- `chapters/NN-<slug>.claims.approved.adoc` (the verified claims — the ground truth)
- `chapters/NN-<slug>.adoc` (the narrative)
- `briefs/NN-<slug>.yaml` (for variant classification reference)
- `glossary.yaml`

**Not** primary sources. This review does not re-verify facts against sources — that was done in `chapter-factcheck`. This review compares narrative against claims only.

## The three checks

### Check 1 — Completeness (nothing dropped)

Walk the claims document claim by claim, in order. For each claim, locate where it appears in the narrative. Record the mapping:

```
Claim N → Narrative paragraph P / sentence S
```

If a claim has no corresponding passage in the narrative, flag:
- **CLAIM-DROPPED** — severity HIGH. The verified claim is missing from the narrative.

If a claim is only partially represented (e.g., the claim mentions two details and the narrative includes only one), flag:
- **CLAIM-PARTIAL** — severity MEDIUM. Specify what was dropped.

### Check 2 — No additions (nothing invented)

Walk the narrative paragraph by paragraph. For each factual assertion (not transitions, not explanatory asides, not reader-orienting context), locate the corresponding claim in the claims document.

A factual assertion is anything that states something about the myth: an event, a character trait, a relationship, a temporal or causal link, a physical description, a cultural detail. Transitional phrases ("Having established the cosmic order...") are not assertions unless they introduce new information.

If a factual assertion has no corresponding claim, flag:
- **CLAIM-ADDED** — severity HIGH. An unverified factual assertion has been introduced.

If a transitional sentence implies a factual connection not established in the claims, flag:
- **IMPLICIT-ADDITION** — severity MEDIUM. The transition suggests something the claims don't support.

### Check 3 — Fidelity (nothing distorted)

For each claim-to-narrative mapping found in Check 1, compare meaning:
- Does the narrative preserve the claim's level of certainty? (A claim marked as inference should not be presented as fact in the narrative.)
- Does the narrative preserve causal direction? ("A caused B" should not become "B caused A" or "A and B coincided.")
- Does the narrative preserve scope? ("Some scholars argue" should not become "Scholars agree.")
- Are markers preserved? Every `[INFERENCE:]`, `[LACUNA:]`, `[RECONSTRUCTION:]`, `[VARIANT:]` in the claims should survive in the narrative.

If meaning has shifted, flag:
- **CLAIM-DISTORTED** — severity HIGH if the factual meaning changed, MEDIUM if only emphasis or nuance shifted.

### Additional checks

- **Glossary fidelity**: confirm `glossary.yaml` renderings are used consistently. Any `never_use` terms: GLOSSARY-VIOLATION.
- **Forbidden words**: flag hits from the forbidden-words list.
- **Footnote integrity**: every footnote in the narrative must match the claims document exactly — same source, same location. No additions, removals, or reassignments. Flag FOOTNOTE-MISMATCH if different.

## Output: `chapters/NN-<slug>.fidelity.yaml`

```yaml
meta:
  auditor_model: <name and version>
  claims_file: chapters/NN-<slug>.claims.approved.adoc
  narrative_file: chapters/NN-<slug>.adoc
  total_claims: <n>
  claims_mapped: <n>
  verdict: PASS | REVISE

claim_mapping:
  # Every claim with its narrative location
  - claim_number: <n>
    claim_text: "<brief summary>"
    narrative_location: "<paragraph number or adoc line>"
    status: MAPPED | PARTIAL | DROPPED

findings:
  - kind: CLAIM-DROPPED | CLAIM-PARTIAL | CLAIM-ADDED | IMPLICIT-ADDITION | CLAIM-DISTORTED | GLOSSARY-VIOLATION | FORBIDDEN-WORD | FOOTNOTE-MISMATCH
    severity: HIGH | MEDIUM | LOW
    claim_number: <n, if applicable>
    narrative_location: "<paragraph or line>"
    issue: <one sentence>
    detail: "<specific text comparison — claim says X, narrative says Y>"
    recommended_fix: <concrete>
```

## Verdict rules
- **PASS**: zero CLAIM-DROPPED, zero CLAIM-ADDED, zero HIGH CLAIM-DISTORTED, ≤ 2 MEDIUM findings.
- **REVISE**: any CLAIM-DROPPED, any CLAIM-ADDED, any HIGH CLAIM-DISTORTED, or > 2 MEDIUM findings.

## Honesty self-check
Answer in `meta`:
1. Did I map every claim, or skip some that seemed obvious? List any I skipped.
2. Did I check every narrative paragraph for additions, or only spot-check? Be specific.
3. For distortion checks, did I compare precise meaning or just topic? Any I only topic-matched are noted here.
4. Am I the same model that produced the narrative? If yes, this review is not valid.

---

# FILE 13 of 17: skills/marker-resolve/SKILL.md

---
name: marker-resolve
description: Converts placeholder markers ([INFERENCE:], [LACUNA:], etc.) into the final reader-facing text — italicized notes, editorial brackets, footnotes. Runs before the prose polish so the editor sees the actual final text.
---

# marker-resolve

## For the human

Throughout the earlier stages, the text contains placeholder markers — tagged notes like `[LACUNA: 20 lines lost here]` or `[INFERENCE: this bridge is not in the source]`. These are useful during writing and fact-checking because they make the status of every claim explicit. But the reader shouldn't see raw markers.

This step converts each marker into the final text the reader will see: an italicized editorial note ("_At this point the tablet breaks..._"), a footnote explaining a reconstruction, or a parenthetical acknowledging an inference. This must happen before the prose-quality polish (line-edit), because expanding a marker changes the rhythm of a sentence, and the editor needs to see the actual final text.

This step does not change any prose outside the markers. It is a mechanical conversion, not an editorial pass.

## Inputs
- Fidelity-reviewed chapters (`chapters/NN-<slug>.adoc`)
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

# FILE 14 of 17: skills/comparative-chapter/SKILL.md

---
name: comparative-chapter
description: Produces the single chapter where cross-cultural comparison is allowed. All the "this is similar to Greek/Norse/Egyptian mythology" observations are confined here, keeping the story chapters focused on one culture. Runs after all story chapters are finished.
---

# comparative-chapter

## For the human

Every story chapter in the book stays strictly within its own culture — no "this is similar to the Greek myth of..." asides. All cross-cultural observation is confined to this single chapter at the end. This separation keeps the story chapters clean and focused, while still giving the reader the comparative perspective that makes mythology fascinating.

Throughout the earlier stages, the AI has been collecting notes on cross-cultural parallels (tagged as `COMPARATIVE-HOOK` comments). This chapter draws on those notes, plus comparative-mythology scholarship, to explore the parallels in depth.

This chapter is inherently more speculative than the story chapters. It uses an additional marker, `[SPECULATION:]`, for hypotheses that are plausible but not established scholarly consensus — each with both the evidence for it and the main argument against it.

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

# FILE 15 of 17: skills/line-edit/SKILL.md

---
name: line-edit
description: Final prose-quality polish. All facts are locked — this step only improves clarity, sentence rhythm, and transitions. It cannot add, remove, or change any factual content. Based on Steven Pinker's *The Sense of Style*.
---

# line-edit

## For the human

This is the final prose polish. By this point, all facts are verified, all markers have been converted to final text, all citations are in place. This step only improves how the text reads — sentence rhythm, word choice, paragraph transitions, removing unnecessary jargon or throat-clearing. It cannot add, remove, or change any factual content. If an edit would change the meaning of a sentence, the editor must revert it.

This step runs after `marker-resolve` (which converts placeholder markers into final text) so the editor sees and polishes the actual prose the reader will read, not a version full of placeholders.

The editor produces a diff file showing every change it made, so you can skim and approve in bulk rather than comparing full documents line by line.

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
To `character-appendix` and `format-finalize`.

---

# FILE 16 of 17: skills/character-appendix/SKILL.md

---
name: character-appendix
description: Produces a reference appendix listing every named character in the book — who they are, where they appear, what they look like (only if the sources actually say so), and how important they are. Runs after all chapters are finished. Goes through fact-checking before the book is assembled.
---

# character-appendix

## For the human

This appendix is the reader's reference companion. Halfway through a chapter on Gilgamesh, the reader encounters Siduri and wants to know: who is she, where else does she appear, what does she look like? This appendix answers that — and only what the sources actually say.

The hardest discipline here is restraint on physical descriptions. AI models asked to describe a mythological character will readily produce vivid physical portraits drawn from cultural stereotypes, later artistic traditions, or pure invention. For most ancient characters, the sources say very little about physical appearance — sometimes nothing at all. The correct entry is an honest "No physical description survives in the in-scope sources," not a fabricated portrait. Accuracy is more important than completeness: it is better to leave a field empty than to fill it with something the sources don't support.

This step runs after all chapters are finalized because it needs the final text to build accurate cross-references ("Siduri appears in Chapter 5, where she..."). It goes through fact-checking by a different AI before the book is assembled.

## Cardinal rule

**Never fabricate or infer physical descriptions.** If no in-scope source describes a character's appearance, the entry says so explicitly. Later artistic depictions, out-of-scope literary traditions, and modern illustrations are not evidence for how the culture described the character. A missing physical description is not a gap to fill — it is information about what the sources contain.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- All `chapters/NN-<slug>.edited.adoc` (final prose, for cross-referencing)
- `chapters/00-introduction.edited.adoc`
- `comparative.adoc` (edited)
- All `briefs/*.yaml` (for source pointers)
- Primary source translations — pasted or accessible via fetch

## Agent instructions

### Step 1: Character extraction

Scan all edited chapters (including introduction and comparative chapter) for every named character. A character is any named entity that acts or is acted upon in the narrative: deities, heroes, creatures, notable mortals, personified concepts. Places and artifacts are excluded (they belong in the glossary).

For each character, record every chapter in which they appear and the AsciiDoc section anchor or heading under which they appear.

### Step 2: Entry composition

For each character, compose an entry with these fields:

**1. Name and identification**
- Use the `glossary.yaml` rendering. If the character is in the glossary, use the locked form. If not, use the most common scholarly transliteration and note it.
- One-sentence identification: role (deity, hero, mortal, creature), domain or function, and relationship to other characters. Sourced.

**2. Physical description**
This is the most audit-sensitive field. Rules:
- **Include only** descriptions explicitly attested in in-scope primary sources. Quote or closely paraphrase the source, with a footnote citation.
- **Acceptable evidence**: direct textual description ("Enkidu was hairy-bodied, with hair like a woman's"), iconographic conventions described in scholarly sources ("Consistently depicted with horned crown in Ur III cylinder seals, per Collon 1987"), or epithets that imply physical traits ("the wild bull" — note this is an epithet, not a literal description).
- **Not acceptable**: descriptions from out-of-scope traditions, later artistic traditions, modern illustrations, inferences from the character's role ("as a sun god, he was likely depicted as radiant"), or generic cultural assumptions.
- **If no physical description survives**: write exactly: "No physical description survives in the in-scope sources." Do not soften this ("little is known about...") — the absence is the fact.
- **Partial descriptions**: if the sources describe one aspect (e.g., a distinctive garment or attribute) but not the full figure, report what exists and note what is absent.

**3. Myths and appearances**
A list of every myth/story in which the character appears, cross-referenced to the chapter where the reader can find it. For each appearance, one sentence on the character's role in that story. Use AsciiDoc cross-references (`<<anchor, display text>>`) to link to chapters.

Order: by narrative chronology within the mythology (cosmogonic appearances first, then theogonic, heroic, etc.), not by chapter number — though chapter numbers should be noted.

**4. Relevance in the mythology**
2–4 sentences on the character's overall importance: how central they are to the mythological corpus, whether they appear across many stories or only one, what scholarly consensus says about their significance. Cite sources. This overlaps with the introduction chapter's centrality assessment but is focused on the individual character rather than the story.

### Step 3: Organization

Sort entries alphabetically by the `glossary.yaml` English rendering (or by scholarly transliteration for characters not in the glossary).

Group into sections if the character count warrants it:
- **Deities** (subdivide by rank/domain if the culture has a clear hierarchy)
- **Heroes and mortals**
- **Creatures and monsters**
- **Personified concepts** (if applicable — e.g., Sumerian *me*, personified Fate)

If the book has fewer than ~20 characters, a single alphabetical list is cleaner than forced categories.

### Style

Same Asimov register as the rest of the book. Entries should be readable as standalone mini-profiles, not dry catalogue entries. But brevity matters — this is a reference appendix, not a chapter. Each entry should be 80–300 words depending on the character's prominence.

### Citations

Same rules as the rest of the pipeline: cite only sources provided in the conversation or fetched via tool use. AsciiDoc footnotes. Every factual claim — especially every physical description — needs a citation.

## Output: `character-appendix.adoc`

```asciidoc
[appendix]
== Characters

A reference guide to the named characters who appear in this book. Physical descriptions are included only where attested in the in-scope sources; where the sources are silent, this is noted explicitly.

=== Deities

[[char-<slug>]]
==== <Character Name>

<One-sentence identification with role and relationships.>

*Physical description.* <Attested description with citation, OR "No physical description survives in the in-scope sources." OR partial description noting what is and is not attested.>

*Appears in:*

* <<chapter-anchor, _Chapter Title_>> — <one-sentence role in that story.>
* <<chapter-anchor, _Chapter Title_>> — <one-sentence role.>

*Relevance.* <2–4 sentences on importance in the mythology, with citations.>

=== Heroes and Mortals

...

=== Creatures and Monsters

...
```

## Self-check before returning
1. Every physical description cites an in-scope primary source. No exceptions. Grep for any physical-appearance language without a footnote — that is a fabrication risk.
2. No entry contains the phrases "likely appeared", "was probably depicted", "would have looked", "may have been described as", or similar hedged fabrications. If the source doesn't describe it, the entry says so flatly.
3. Every chapter cross-reference resolves to an actual chapter anchor.
4. Every character who appears in any chapter is in the appendix. Grep all chapter files for proper nouns and compare against the appendix entry list.
5. Glossary renderings match `glossary.yaml`.
6. Entries are sorted alphabetically within their category.
7. No out-of-scope source cited for physical descriptions or character details.

## Handoff
To `chapter-factcheck` (fresh conversation, different model) for a factcheck pass focused on:
- Fabricated or unsourced physical descriptions (the primary risk).
- Cross-reference accuracy.
- Claims about mythological relevance.

After factcheck passes, to `format-finalize`.

---

# FILE 17 of 17: skills/format-finalize/SKILL.md

---
name: format-finalize
description: Final mechanical assembly. Compiles the bibliography, assembles all chapters into the master book file, and runs a test build to PDF and EPUB to catch formatting errors. No prose is changed at this stage — all writing is finished.
---

# format-finalize

## For the human

This is a purely mechanical step — no writing, no editing, no judgment calls. All prose is final. This step:

- **Builds the bibliography.** Scans every footnote across all chapters and produces a single bibliography file listing every source cited in the book. If any footnote cites a source that isn't on the approved list (`sources.yaml`), this is flagged as a problem.
- **Assembles the book.** Combines the introduction, all story chapters, the comparative chapter, and the character appendix into one master file (`book.adoc`) in the correct order.
- **Runs a test build.** Generates a test PDF and EPUB to catch formatting errors (broken cross-references, missing files, syntax problems) before the final render.

No prose is changed. If this step finds a problem that requires changing text (e.g., a broken cross-reference), it reports the problem and stops — it does not attempt to fix it.

## Inputs
- `chapters/00-introduction.edited.adoc` (intro chapter)
- All `chapters/NN-<slug>.edited.adoc` (story chapters)
- `comparative.adoc` (edited)
- `character-appendix.adoc` (fact-checked)
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

include::chapters/00-introduction.edited.adoc[]

include::chapters/01-<slug>.edited.adoc[]
include::chapters/02-<slug>.edited.adoc[]
// ... in toc.yaml order ...

include::comparative.adoc[]

include::character-appendix.adoc[]

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
- Every `<<chapter-anchor>>` cross-reference in `character-appendix.adoc` resolves to an actual anchor in the chapter files.
- Asciidoctor dry runs exit clean.

---

