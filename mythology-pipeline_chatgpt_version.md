# Mythology Book Pipeline — Revised v2.1 for External Review

<!--
REVIEWER NOTE TO CLAUDE OR OTHER REVIEWING AI

This revision keeps the original architecture on purpose.
The main changes are structural, not conceptual:

1. Stronger machine-readable contracts between stages.
2. Separation of claim-checking from prose-checking.
3. A normalization/validation step after every human intervention.
4. Stronger source registry and citation normalization.
5. Explicit chapter anchors and provenance metadata.
6. Tighter control of reconstruction and cross-cultural leakage.

Please review this as a production workflow, not merely as writing guidance.
Focus especially on whether any stage still relies on assumptions that are not guaranteed
by the upstream artifact schemas.
-->

This document is a revised, more operational version of the mythology-book pipeline. It preserves the original design goal: produce clear, readable mythology books, one culture per book, while minimizing hallucination, cross-cultural contamination, fabricated references, and stylistic drift from the evidence base.

The central idea remains unchanged: different AIs should do different jobs, and critical stages should be checked by a different model in a fresh conversation. What changes in v2.1 is that the contracts between stages are made explicit enough that the pipeline can survive human edits, multiple AI models, and mechanical assembly without silently breaking.

---

## Core principles

1. **Writer and checker must be different AIs.**  
   The model that writes a stage must not be the model that audits it. The audit should happen in a fresh conversation with a different model family if possible.

2. **Three early control files govern the whole book.**  
   Every later stage must read:
   - `scope.md`
   - `sources.yaml`
   - `glossary.yaml`

3. **Cite only sources actually available in the current working context.**  
   No citations from training memory. A source is citable only if its text or reliable metadata has been pasted, fetched, or otherwise made available during the stage.

4. **Contradictions between in-scope sources are part of the record.**  
   Internal variance is not an error. Silent conflation is.

5. **Check the document, not the deity.**  
   Scope decisions are made at the level of attested textual detail, not the broad cultural ownership of a figure.

6. **Chapters follow the evidence.**  
   Length, emphasis, and confidence are determined by preservation and attestation, not by modern expectations of narrative completeness.

7. **Human edits are first-class failure points and must be normalized.**  
   Any file edited after an audit or review checkpoint must pass schema and contract validation before becoming the next stage’s canonical input.

8. **Planning metadata is not prose.**  
   Comparative notes, unresolved issues, and reconstruction logic may exist in planning files, but they do not automatically authorize reader-facing prose.

---

## Stage order

```text
scope-lock
  → story-inventory
  → inventory-audit
  → [HUMAN review]
  → post-human-normalize(inventory)
  → chapter-briefs
  → glossary-lock
  → intro-chapter
  → prose-factcheck(intro)
  → [HUMAN review]
  → post-human-normalize(intro)
  → [per story chapter:
       chapter-claims
       → claims-factcheck
       → [HUMAN review]
       → post-human-normalize(claims)
       → chapter-draft
       → narrative-fidelity
       → [HUMAN if REVISE]
       → post-human-normalize(narrative if revised)
    ]
  → comparative-chapter
  → prose-factcheck(comparative)
  → [HUMAN review]
  → post-human-normalize(comparative)
  → marker-resolve
  → line-edit
  → character-appendix
  → prose-factcheck(appendix)
  → [HUMAN review]
  → post-human-normalize(appendix)
  → format-finalize
```

### Why this differs from v2
The most important new stage is `post-human-normalize`. Human review is necessary, but it breaks machine assumptions unless the next-stage input is revalidated and rewritten into canonical form.

The former `chapter-factcheck` stage is split into:
- `claims-factcheck` — for one-claim-per-paragraph files.
- `prose-factcheck` — for intro/comparative/appendix prose.

This is not cosmetic. Those are different tasks and require different audit logic.

---

## Artifact layout per book

```text
<book-name>/
  scope.md
  sources.yaml
  inventory.yaml
  inventory-audit.yaml
  inventory.approved.yaml
  toc.yaml
  glossary.yaml

  briefs/
    01-<slug>.yaml
    ...

  chapters/
    00-introduction.adoc
    00-introduction.factcheck.yaml
    00-introduction.approved.adoc
    00-introduction.resolved.adoc
    00-introduction.edited.adoc
    00-introduction.diff.md

    01-<slug>.claims.adoc
    01-<slug>.claims.factcheck.yaml
    01-<slug>.claims.approved.adoc
    01-<slug>.adoc
    01-<slug>.fidelity.yaml
    01-<slug>.approved.adoc
    01-<slug>.resolved.adoc
    01-<slug>.edited.adoc
    01-<slug>.diff.md
    ...

  comparative.adoc
  comparative.factcheck.yaml
  comparative.approved.adoc
  comparative.resolved.adoc
  comparative.edited.adoc
  comparative.diff.md

  character-appendix.adoc
  character-appendix.factcheck.yaml
  character-appendix.approved.adoc

  book.adoc
  bibliography.bib
  validation-report.md
```

---

## Global contracts

These apply to every stage unless a later section narrows them further.

### 1. Provenance header required on every generated artifact

Every machine-generated YAML or prose file must begin with a metadata block stating:

```yaml
meta:
  stage: <stage-name>
  produced_by_model: <model name/version if known>
  conversation_id: <if available, else "unknown">
  created_utc: <ISO timestamp>
  input_files:
    - <relative path>
  input_hashes:
    <relative path>: <sha256 or "not-recorded">
```

For prose files in AsciiDoc, place the same information in comments at the top.

This is partly for traceability and partly to force explicit discipline around “fresh conversation” assumptions.

### 2. Canonical anchors
Every chapter brief must define:
- `chapter_anchor`
- `chapter_short_id`

Every chapter output must include an explicit anchor at the top:
```asciidoc
[[ch-01-descent-of-inanna]]
== The Descent of Inanna
```

No later stage may rely on auto-generated heading IDs for cross-references.

### 3. Citation normalization
Reader-facing prose may use footnotes, but stage contracts must not depend on parsing free-form footnote prose.

Every factual claim must carry:
- a reader-facing footnote, and
- a machine-readable evidence token in comment form immediately after the claim.

Example:
```asciidoc
Inanna descends to the underworld.footnote:[Black et al. 2004, ETCSL 1.4.1, lines 1–10.]
//// EVIDENCE: source_id=black2004 ; loc=ETCSL 1.4.1 lines 1-10 ; source_kind=primary-translation ////
```

Generated editorial footnotes from marker resolution are not treated as bibliography inputs.

### 4. Negative-evidence discipline
Any statement of absence must be explicit about its scope.

Allowed:
- “No physical description survives in the in-scope sources.”
- “No ritual context is attested in the sources used for this book.”

Not allowed:
- “The culture did not describe X.”
unless the evidence really supports that stronger claim.

### 5. Human-review re-entry rule
Any artifact modified after a human review must pass `post-human-normalize` before serving as canonical input downstream.

---

# FILE 1: README.md

## What changed from v2

- `sources.yaml` is now a structured source registry, not merely a whitelist.
- `chapter-factcheck` is split into `claims-factcheck` and `prose-factcheck`.
- `post-human-normalize` is inserted after every human checkpoint.
- Explicit chapter anchors are required.
- Machine-readable evidence tokens are required for every factual claim.
- Reconstruction use is quantified and reportable.
- Comparative material is permitted in planning metadata but quarantined from story prose until the comparative chapter.

---

# FILE 2: CHANGELOG.md

## v2.1

### Added
- `post-human-normalize` stage after every human review.
- Explicit provenance headers on all artifacts.
- Canonical chapter anchors in `toc.yaml` and briefs.
- Machine-readable evidence tokens in claims and prose.
- Source-registry expansion in `sources.yaml`.
- Reconstruction count reporting at chapter level.

### Changed
- `chapter-factcheck` split into:
  - `claims-factcheck`
  - `prose-factcheck`
- Intro chapter narrowed: less comparative burden, more corpus framing.
- Variant handling expanded beyond a strict binary.
- Comparative leakage rules clarified.
- `format-finalize` now builds bibliography from normalized source IDs and evidence tokens, not free-form footnote text.

### Removed
- Implicit dependence on auto-generated AsciiDoc IDs.
- Reliance on bibliography extraction from arbitrary footnote prose.

---

# FILE 3: skills/scope-lock/SKILL.md

---
name: scope-lock
description: Interactive start-of-book conversation that defines scope.md and sources.yaml. Establishes the culture, chronology, exclusions, reconstruction policy, source registry, and comparison policy for the whole book.
---

# scope-lock

## Purpose

This stage defines the book’s formal scope and builds the approved source registry. Every later stage depends on this. If the scope is vague here, later stages will compensate by guessing, which is exactly what the pipeline is designed to prevent.

## Inputs
- Target mythology or tradition
- User goals
- Any hard exclusions already known

## Agent instructions

Run an interactive dialogue. Do not accept vague scope if it can be sharpened. Resolve at least the following:

1. **Culture definition**
   - self-designation if applicable
   - geography
   - temporal limits
   - language(s) of composition

2. **Excluded adjacent cultures**
   Propose at least three likely contamination risks and explain each.

3. **Reconstruction policy**
   Define:
   - what counts as in-tradition
   - temporal tolerance
   - language tolerance
   - whether fills may come only from parallel witnesses of the same composition, or from other compositions in the same tradition
   - whether scholarly reconstruction is required or merely preferred

4. **Comparison policy**
   Define whether comparative scholarship is allowed at all, and if so:
   - in which stage(s)
   - from which approved comparative scholars
   - with what standard of confidence

5. **Source registry approval**
   Propose 8–15 in-scope sources minimum, plus blacklisted contaminating sources or source types.

## Output: `scope.md`

```markdown
# Scope: <Mythology Name>

## Culture
<name, self-designation if relevant, region>

## Period
<earliest in-scope composition> — <latest in-scope composition>

## Languages of primary sources
- <language>

## Excluded adjacent cultures (contamination risks)
- **<culture>**: <reason>
- **<culture>**: <reason>
- **<culture>**: <reason>

## Reconstruction policy
- In-tradition means: <definition>
- Permitted fill sources: <definition>
- Temporal tolerance: <definition>
- Language tolerance: <definition>
- Scholarly reconstruction required: yes|no
- Every reconstruction must be flagged and footnoted.

## Comparison policy
- Comparative discussion allowed only in: <stages>
- Approved comparative source tier: <definition>
- Speculative parallels require explicit marker and counterargument.

## In-scope corpus (broad)
<collections, series, corpora, manuscript traditions>

## Explicitly out of scope
<texts, periods, traditions a careless researcher might include>

## Variant presentation policy
- <rules>

## Book register
Asimov-style explanatory prose. Clear, modern English. No imitation-sacred diction.
```

## Output: `sources.yaml`

This is now a registry, not just a whitelist.

```yaml
meta:
  stage: scope-lock

registry:
  - id: black2004
    source_tier: primary-translation
    in_scope_default: true
    type: book
    author: "Black, Jeremy et al."
    title: "The Literature of Ancient Sumer"
    year: 2004
    translator: ""
    editor: ""
    container_title: ""
    publisher: ""
    place: ""
    full_citation: "<full bibliography string>"
    short_citation: "Black et al. 2004"
    identifier_type: isbn
    identifier_value: "<isbn>"
    access_url: "<stable url if any>"
    notes: ""

blacklist:
  - pattern: "<pattern>"
    reason: "<reason>"

triangulation_databases:
  - id: ETCSL
    url: "https://etcsl.orinst.ox.ac.uk/"
    covers: "Sumerian literary texts"

comparative_registry:
  - id: west2007
    source_tier: comparative-secondary
    in_scope_default: false
    ...
```

## Handoff
`scope.md` and `sources.yaml` to `story-inventory`.

---

# FILE 4: skills/story-inventory/SKILL.md

---
name: story-inventory
description: Produces an inventory of candidate stories and cycles that belong in the book, with verifiable source identifiers and explicit scope-confidence notes.
---

# story-inventory

## Purpose

Create the book’s evidence-based story inventory. This is not free brainstorming. Every entry must be grounded in a verifiable attestation and linked to the approved source registry.

## Inputs
- `scope.md`
- `sources.yaml`

## Agent instructions

Using only approved or otherwise explicitly reviewable sources, enumerate the major story cycles and individual stories in scope.

### Required fields per story
Each story must include:
- stable ID
- English working title
- native title if applicable
- primary attestation(s)
- source registry IDs
- identifier(s)
- date range
- short summary
- scope confidence
- variant note if relevant
- contamination note if relevant

### Inventory confidence
Each story must carry:
- `inventory_confidence: high|medium|low`
- `scope_uncertain: true|false`
- `identifier_missing: true|false`

### Important rule
A culturally famous figure is not enough. The inventory is built from attested narratives, not from deity encyclopedias.

## Output: `inventory.yaml`

```yaml
meta:
  stage: story-inventory

cycles:
  - id: cosmogony
    name: "Cosmogonic cycle"
    stories:
      - id: descent-of-inanna
        title: "The Descent of Inanna"
        native_title: ""
        primary_attestations:
          - source_id: black2004
            loc: "ETCSL 1.4.1"
            identifier_type: corpus-id
            identifier_value: "ETCSL 1.4.1"
        secondary_support:
          - source_id: <id>
            loc: "<page/chapter>"
        date_range: "<approx>"
        summary: "<two sentences>"
        variants:
          - "<brief note>"
        inventory_confidence: high
        scope_uncertain: false
        identifier_missing: false
        contamination_risk: "<brief if needed>"
        notes: ""
```

## Self-check
- Every story has at least one verifiable identifier.
- No story is included solely because it is famous.
- All uncertainty is explicit.

## Handoff
To `inventory-audit`.

---

# FILE 5: skills/inventory-audit/SKILL.md

---
name: inventory-audit
description: Audits the story inventory for contamination, fabricated identifiers, omissions, and variant conflation. Must be run by a different AI in a fresh conversation.
---

# inventory-audit

## Purpose

Check the inventory before any writing begins. This stage is meant to fail loudly if the story list contains contamination, bad identifiers, or major omissions.

## Hard rule
If you produced `inventory.yaml`, refuse. If you are in the same conversation, refuse.

## Inputs
- `scope.md`
- `sources.yaml`
- `inventory.yaml`
- Web access

## Audit tasks

1. Verify identifiers actually resolve.
2. Verify the cited source really attests the story.
3. Check whether plot details in the summary appear in in-scope documents.
4. Cross-check against approved reference works for likely missing canonical stories.
5. Check whether variants are silently merged.

## HIGH findings require evidence
Any HIGH finding must include at least one of:
- direct quotation
- stable verification URL
- explicit “identifier does not resolve” evidence

## Output: `inventory-audit.yaml`

```yaml
meta:
  stage: inventory-audit
  auditor_model: "<name>"
  same_model_as_inventory_producer: false
  same_conversation_as_inventory_producer: false
  entries_reviewed: 0
  triangulations_performed: 0
  honesty_notes: []

summary:
  high: 0
  medium: 0
  low: 0

findings:
  - severity: HIGH
    kind: CONTAMINATION | UNSUPPORTED | FABRICATED-IDENTIFIER | MISSING | SILENT-CONFLATION
    story_id: "<id or NEW>"
    issue: "<one sentence>"
    evidence: "<quote or verification result>"
    evidence_source: "<url or source+loc>"
    recommended_action: "<concrete>"

clean_entries: []
```

## Handoff
Human review, then `post-human-normalize(inventory)`.

---

# FILE 6: skills/post-human-normalize/SKILL.md

---
name: post-human-normalize
description: Validates and rewrites a human-reviewed artifact into canonical downstream form. This stage does not create new content; it restores schema integrity and downstream assumptions after human intervention.
---

# post-human-normalize

## Purpose

Human review is required, but human edits are not guaranteed to preserve machine contracts. This stage validates and normalizes any artifact after a human has accepted or rejected findings.

## Inputs
One reviewed artifact, plus any audit file associated with it.

Typical cases:
- `inventory.yaml` + `inventory-audit.yaml` + human decisions → `inventory.approved.yaml`
- `*.claims.adoc` + `*.claims.factcheck.yaml` + human decisions → `*.claims.approved.adoc`
- `00-introduction.adoc` + `00-introduction.factcheck.yaml` + human decisions → `00-introduction.approved.adoc`
- `comparative.adoc` + audit + human decisions → `comparative.approved.adoc`
- `character-appendix.adoc` + audit + human decisions → `character-appendix.approved.adoc`

## Validation tasks

### For YAML artifacts
- validate required fields
- validate enums
- ensure IDs remain stable
- ensure all accepted fixes are reflected
- ensure rejected findings are recorded, not silently dropped

### For claims documents
- one claim per paragraph
- every claim still has a reader-facing footnote
- every claim still has an evidence token
- markers, if present, remain syntactically valid
- no merged claims
- no orphaned comparative hooks

### For prose documents
- explicit chapter anchor present
- no unresolved placeholder markers unless stage allows them
- evidence tokens still attached where required
- headings and section order preserved if downstream depends on them

## Output
Canonical `*.approved.*` artifact suitable for downstream use, plus a short normalization report if anything had to be repaired.

## Handoff
Depends on artifact type.

---

# FILE 7: skills/chapter-briefs/SKILL.md

---
name: chapter-briefs
description: Produces one planning file per chapter. The brief is the contract for writing, variant handling, anchor identity, target length, and source set.
---

# chapter-briefs

## Purpose

Convert the approved inventory into one structured brief per chapter. No prose is written here.

## Inputs
- `scope.md`
- `sources.yaml`
- `inventory.approved.yaml`

## Agent instructions

For each chapter, produce a brief with:

- chapter numbering
- canonical anchor
- chapter source base
- variant strategy
- cultural relevance summary
- comparative metadata
- reconstruction conditions
- target length
- unresolved questions

### Variant classification
Use one of:
- `single-prevalent-complete`
- `single-prevalent-reconstructed`
- `co-equal`
- `composite-editorial-base`
- `diachronic-variants`

Do not force a simple binary if the evidence does not justify it.

### Comparative control
Comparative observations may appear in:
- `cross_cultural_parallels`
- `comparative_hooks`

These are planning metadata only. They do not authorize comparative prose in story chapters.

## Output: `briefs/NN-<slug>.yaml`

```yaml
meta:
  stage: chapter-briefs

chapter_number: 1
chapter_short_id: "01"
chapter_anchor: "ch-01-descent-of-inanna"
slug: "descent-of-inanna"
title: "The Descent of Inanna"

sources:
  primary:
    - source_id: black2004
      loc: "ETCSL 1.4.1"
      identifier_type: corpus-id
      identifier_value: "ETCSL 1.4.1"
      translator_edition: "Black et al. 2004"
      access_url: "<url or file>"
  secondary:
    - source_id: "<id>"
      loc: "<loc>"

variant_strategy:
  classification: single-prevalent-complete
  rationale: "<one sentence>"
  base_version:
    source_id: "<id>"
    reason: "<one sentence>"
  alternates:
    - source_id: "<id>"
      difference: "<one sentence>"

reconstruction_policy_for_chapter:
  allowed: true
  allowed_only_if: "<conditions>"
  expected_reconstruction_points: 0

entities_glossary:
  - native: "<form>"
    role: deity
    first_mention_gloss_candidate: "<gloss>"

cultural_relevance:
  centrality: central | significant | marginal
  centrality_evidence:
    - kind: attestation-volume
      detail: "<one sentence>"
      source_id: "<id>"
      loc: "<loc>"
  function:
    - role: cosmological
      basis: "<one sentence>"
      source_id: "<id>"
      loc: "<loc>"

cross_cultural_parallels:
  - other_culture: "<name>"
    note: "<brief>"
    source_id: "<id>"

comparative_hooks:
  - hook: "<brief>"
    in_scope_basis:
      source_id: "<id>"
      loc: "<loc>"
    out_of_scope_pointer:
      source_id: "<id>"

triangulation_databases:
  - ETCSL

target_length_words: 3000
special_instructions: ""
unresolved_questions: []
```

## Output: `toc.yaml`

```yaml
meta:
  stage: chapter-briefs

book_title: "<title>"
chapters:
  - chapter_number: 0
    chapter_anchor: "ch-00-introduction"
    path: "chapters/00-introduction.adoc"
    title: "Introduction: The Myths and Their World"
  - chapter_number: 1
    chapter_anchor: "ch-01-descent-of-inanna"
    path: "chapters/01-descent-of-inanna.adoc"
    title: "The Descent of Inanna"
```

## Handoff
To `glossary-lock` and `intro-chapter`.

---

# FILE 8: skills/glossary-lock/SKILL.md

---
name: glossary-lock
description: Locks recurring renderings before drafting begins and records forbidden equivalents.
---

# glossary-lock

## Purpose

Prevent false contradictions and stylistic drift caused by inconsistent rendering of names and technical terms.

## Inputs
- `scope.md`
- `sources.yaml`
- all chapter briefs

## Agent instructions

Extract recurring terms, survey renderings, and propose a locked form. Require explicit user confirmation for each entry.

## Output: `glossary.yaml`

```yaml
meta:
  stage: glossary-lock

terms:
  - native: "<transliteration>"
    applies_to_roles: [deity, place]
    renderings_considered:
      - form: "<rendering>"
        source_id: "<id>"
      - form: "<rendering>"
        source_id: "<id>"
    chosen: "<final form>"
    rationale: "<one sentence>"
    first_mention_gloss: "<functional gloss>"
    never_use:
      - "<out-of-scope equivalent>"
```

## Additional rule
If a later stage needs a recurring term not yet in the glossary, pause and append it formally. Do not improvise.

## Handoff
To `intro-chapter` and `chapter-claims`.

---

# FILE 9: skills/intro-chapter/SKILL.md

---
name: intro-chapter
description: Produces a restrained introductory chapter that frames the corpus, preservation, organization, and the broad cultural role of the myths without overloading the opening with speculative comparative work.
---

# intro-chapter

## Purpose

Introduce the mythology as a corpus and prepare the reader to understand the chapters that follow.

## Important narrowing from v2
This chapter should not try to do the full intellectual work of the comparative chapter. It may preview patterns and broad functions, but its primary job is to orient the reader:
- what corpus survives,
- how it survives,
- what genres and cycles structure it,
- what kinds of cultural work the myths appear to do.

## Inputs
- `scope.md`
- `sources.yaml`
- `glossary.yaml`
- `briefs/*.yaml`
- `toc.yaml`

## Allowed content
- corpus overview
- preservation state
- broad organization of myth types
- cautious summary of centrality and function
- brief forward pointers to later themes

## Restricted content
- no substantial comparative analysis
- no extended out-of-scope myth summaries
- no strong consensus claims unless sourced

## Output: `chapters/00-introduction.adoc`

```asciidoc
//// meta: stage=intro-chapter ////
[[ch-00-introduction]]
== Introduction: The Myths and Their World

<overview of corpus and preservation>

<organization of major myth types>

<what these myths seem to do in the culture, with citations>

<brief forward pointer to later comparative discussion, if needed>
```

## Handoff
To `prose-factcheck`.

---

# FILE 10: skills/chapter-claims/SKILL.md

---
name: chapter-claims
description: Produces the factual skeleton of one chapter. One claim per paragraph, one evidence token per claim, one reader-facing footnote per claim.
---

# chapter-claims

## Purpose

Isolate factual content before prose writing.

## Inputs
- `scope.md`
- `sources.yaml`
- `glossary.yaml`
- one chapter brief
- source texts actually available in context

## Hard rules
1. One factual claim per paragraph.
2. Every claim must have:
   - reader-facing footnote
   - machine-readable evidence token
3. No new comparative prose.
4. No source cited from memory.
5. If a needed glossary term is missing, stop.

## Markers
Allowed markers:
- `[INFERENCE: ...]`
- `[LACUNA: ...]`
- `[RECONSTRUCTION: ...]`
- `[VARIANT: ...]`

Every marker must remain syntactically machine-parseable.

## Output: `chapters/NN-<slug>.claims.adoc`

```asciidoc
//// meta: stage=chapter-claims ////
[[ch-01-descent-of-inanna]]
== The Descent of Inanna — Claims

Inanna descends to the underworld.footnote:[Black et al. 2004, ETCSL 1.4.1, lines 1–10.]
//// EVIDENCE: source_id=black2004 ; loc=ETCSL 1.4.1 lines 1-10 ; source_kind=primary-translation ////

Ereshkigal rules the underworld.footnote:[Black et al. 2004, ETCSL 1.4.1, lines 20–24.]
//// EVIDENCE: source_id=black2004 ; loc=ETCSL 1.4.1 lines 20-24 ; source_kind=primary-translation ////

// COMPARATIVE-HOOK: descent motif with later traditions; planning note only.
```

## Chapter-level metadata
At the end of the file, report:
- total claims
- marker counts by type
- reconstruction count

## Handoff
To `claims-factcheck`.

---

# FILE 11: skills/claims-factcheck/SKILL.md

---
name: claims-factcheck
description: Audits a claims document claim by claim. Must be run by a different AI in a fresh conversation.
---

# claims-factcheck

## Purpose

Verify isolated claims, not flowing prose.

## Hard rule
If you wrote the claims document, refuse.

## Inputs
- `scope.md`
- `sources.yaml`
- `glossary.yaml`
- one `*.claims.adoc`
- corresponding brief
- source texts
- web access if needed for triangulation

## Audit passes

1. Claim verification
2. Reference triangulation
3. Contamination scan by document provenance
4. Marker integrity
5. Reverse-order second pass

## Supported means quoted
Every SUPPORTED verdict requires a verbatim quote or exact retrieved passage.

## Output: `chapters/NN-<slug>.claims.factcheck.yaml`

```yaml
meta:
  stage: claims-factcheck
  auditor_model: "<name>"
  same_model_as_claims_producer: false
  same_conversation_as_claims_producer: false
  input_file: "chapters/01-example.claims.adoc"
  claims_identified: 0
  triangulations_performed: 0
  verdict: PASS | REVISE | MAJOR-REVISE
  honesty_notes: []

tallies:
  supported: 0
  internal_variance: 0
  unverified: 0
  citation_wrong: 0
  contamination: 0
  fabrication: 0
  silent_bridges: 0
  marker_issues: 0
  glossary_violations: 0

supported_claims:
  - claim_number: 1
    claim: "<summary>"
    source_id: "<id>"
    loc: "<loc>"
    verbatim_quote: "<quote>"

findings:
  - claim_number: 3
    kind: CONTAMINATION | UNVERIFIED | CITATION-WRONG | FABRICATION | SILENT-BRIDGE | MARKER-MISUSED | MARKER-FABRICATED | GLOSSARY-VIOLATION
    severity: HIGH | MEDIUM | LOW
    issue: "<one sentence>"
    evidence: "<quote or URL>"
    recommended_fix: "<concrete>"
```

## Handoff
Human review, then `post-human-normalize(claims)`.

---

# FILE 12: skills/chapter-draft/SKILL.md

---
name: chapter-draft
description: Converts approved claims into narrative prose. It is forbidden from adding factual content.
---

# chapter-draft

## Purpose

Write readable narrative from verified claims only.

## Inputs
- `scope.md`
- `sources.yaml`
- `glossary.yaml`
- `*.claims.approved.adoc`
- corresponding brief

Do not provide original sources to this stage.

## Hard rules
1. Every factual assertion must map to an approved claim.
2. No approved claim may be silently dropped.
3. No footnote or evidence token may be reassigned.
4. Comparative metadata does not authorize comparative prose.
5. Marker-bearing content must remain marked.

## Output
`chapters/NN-<slug>.adoc`

Include:
- explicit chapter anchor
- carried-over footnotes
- carried-over evidence tokens attached to the factual sentence they support
- chapter footer metadata:
  - total approved claims
  - claims represented
  - reconstruction count

## Handoff
To `narrative-fidelity`.

---

# FILE 13: skills/narrative-fidelity/SKILL.md

---
name: narrative-fidelity
description: Compares narrative prose against the approved claims and checks for dropped, added, or distorted content.
---

# narrative-fidelity

## Purpose

This is a comparison audit, not a source audit.

## Inputs
- `*.claims.approved.adoc`
- `*.adoc`
- brief
- glossary

## Required checks
1. claim-to-narrative mapping
2. no new factual additions
3. no distortions of certainty, causality, scope, or marker status
4. glossary fidelity
5. footnote and evidence-token integrity

## Output: `chapters/NN-<slug>.fidelity.yaml`

```yaml
meta:
  stage: narrative-fidelity
  auditor_model: "<name>"
  same_model_as_narrative_producer: false
  same_conversation_as_narrative_producer: false
  total_claims: 0
  claims_mapped: 0
  verdict: PASS | REVISE
  honesty_notes: []

claim_mapping:
  - claim_number: 1
    narrative_location: "<para/line>"
    status: MAPPED | PARTIAL | DROPPED

findings:
  - kind: CLAIM-DROPPED | CLAIM-PARTIAL | CLAIM-ADDED | IMPLICIT-ADDITION | CLAIM-DISTORTED | GLOSSARY-VIOLATION | FORBIDDEN-WORD | FOOTNOTE-MISMATCH | EVIDENCE-TOKEN-MISMATCH
    severity: HIGH | MEDIUM | LOW
    issue: "<one sentence>"
    detail: "<comparison>"
    recommended_fix: "<concrete>"
```

## Handoff
If PASS, chapter waits for later assembly.
If REVISE, human or drafter revises, then `post-human-normalize(narrative if manually changed)` and re-run fidelity.

---

# FILE 14: skills/comparative-chapter/SKILL.md

---
name: comparative-chapter
description: Produces the only chapter in which sustained cross-cultural comparison is allowed.
---

# comparative-chapter

## Purpose

Concentrate comparison in one place.

## Inputs
- approved story chapters
- approved introduction
- all briefs
- comparative hooks
- `scope.md`
- `sources.yaml`

## Rules
- Every comparative claim cites both in-scope and out-of-scope sources.
- Comparative scholarship must come from approved comparative sources.
- Speculation must be marked.
- Do not retell out-of-scope myths at length.
- Distinguish:
  - structural parallel
  - motif parallel
  - possible contact
  - speculative genealogy

## Marker
```text
[SPECULATION: claim | basis: X | counterargument: Y]
```

## Output
`comparative.adoc`

## Handoff
To `prose-factcheck`, then human review, then `post-human-normalize(comparative)`.

---

# FILE 15: skills/prose-factcheck/SKILL.md

---
name: prose-factcheck
description: Audits prose artifacts such as the introduction, comparative chapter, and character appendix. Unlike claims-factcheck, it must first extract claims from prose.
---

# prose-factcheck

## Purpose

Audit prose files whose claims are embedded in paragraphs.

## Inputs
- `scope.md`
- `sources.yaml`
- `glossary.yaml`
- one prose artifact:
  - `00-introduction.adoc`
  - `comparative.adoc`
  - `character-appendix.adoc` or approved equivalent
- source texts
- web access if needed

## Method

### Pass 0 — Claim extraction
Extract each factual assertion into a temporary audit list before verifying. The audit must not pretend prose can be checked reliably without this step.

### Pass 1 — Source verification
Verify extracted claims against cited sources.

### Pass 2 — Triangulation
Check identifiers, pages, tablets, anchors, and source registry IDs.

### Pass 3 — Scope and contamination
Check whether narrative details or comparative claims cross scope boundaries improperly.

### Pass 4 — Glossary and forbidden terms
Check glossary renderings and forbidden terms where style matters.

## Output
For intro:
- `chapters/00-introduction.factcheck.yaml`

For comparative:
- `comparative.factcheck.yaml`

For appendix:
- `character-appendix.factcheck.yaml`

```yaml
meta:
  stage: prose-factcheck
  auditor_model: "<name>"
  input_file: "<path>"
  extracted_claims: 0
  triangulations_performed: 0
  verdict: PASS | REVISE | MAJOR-REVISE
  honesty_notes: []

findings:
  - location: "<section/line>"
    extracted_claim: "<claim>"
    kind: UNVERIFIED | CITATION-WRONG | CONTAMINATION | FABRICATION | GLOSSARY-VIOLATION | CROSSREF-BROKEN | OVERSTATED-CONSENSUS
    severity: HIGH | MEDIUM | LOW
    evidence: "<quote or verification result>"
    recommended_fix: "<concrete>"
```

## Handoff
Human review, then `post-human-normalize(...)`.

---

# FILE 16: skills/marker-resolve/SKILL.md

---
name: marker-resolve
description: Mechanically converts markers into reader-facing prose and editorial notes.
---

# marker-resolve

## Purpose

Convert placeholder markers into final prose without altering any surrounding sentence that is not part of the marker itself.

## Inputs
- approved story chapters
- approved intro
- approved comparative
- `scope.md`

## Rules
- Only replace marker spans.
- Do not change other prose.
- Preserve evidence-token alignment where possible.
- After replacement, no unresolved markers may remain.

## Marker outputs

### INFERENCE
Render as explicit editorial note with footnote.

### LACUNA
Render as italicized editorial interruption.

### RECONSTRUCTION
Render reconstructed prose with explicit reconstruction footnote.

### VARIANT
Render chosen version in body with alternate in footnote.

### SPECULATION
Render the claim with explicit speculative footnote.

## Output
- `*.resolved.adoc`

## Handoff
To `line-edit`.

---

# FILE 17: skills/line-edit/SKILL.md

---
name: line-edit
description: Final style polish after marker resolution. No factual meaning may change.
---

# line-edit

## Purpose

Improve clarity, rhythm, and transitions without altering facts, source assignments, anchors, or resolved marker passages.

## Inputs
- resolved intro
- resolved story chapters
- resolved comparative
- glossary

## Hard rules
- no factual additions
- no deletions of factual content
- no footnote changes
- no anchor changes
- no edits inside resolved-marker passages
- evidence tokens must remain aligned with the sentence they support

## Output
- `*.edited.adoc`
- `*.diff.md`

Diff format must show each non-trivial change as original vs edited.

## Handoff
To `character-appendix` and then `format-finalize`.

---

# FILE 18: skills/character-appendix/SKILL.md

---
name: character-appendix
description: Builds a reference appendix of named characters using final chapter text and approved sources.
---

# character-appendix

## Purpose

Provide a reference appendix without fabricating descriptive detail.

## Inputs
- `scope.md`
- `sources.yaml`
- `glossary.yaml`
- edited chapters
- edited intro
- edited comparative
- briefs
- source texts

## Hard rule
Never invent physical description.

## Important clarification
The appendix may cite:
- in-scope primary sources
- approved in-scope secondary/iconographic sources

But it must label the basis of physical-description claims explicitly:
- `textual`
- `iconographic-secondary`
- `epithet-only`
- `none`

## Output
`character-appendix.adoc`

Each entry should include:
- name
- identification
- physical description status
- appearances with stable chapter anchors
- relevance

Example phrase when absent:
> No physical description survives in the in-scope sources used for this book.

## Handoff
To `prose-factcheck`, then human review, then `post-human-normalize(appendix)`.

---

# FILE 19: skills/format-finalize/SKILL.md

---
name: format-finalize
description: Mechanical assembly, bibliography compilation, validation, and build.
---

# format-finalize

## Purpose

Assemble the finished book without changing prose.

## Inputs
- edited intro
- edited story chapters
- edited comparative
- approved character appendix
- `sources.yaml`
- `toc.yaml`
- optional front/back matter

## Important change from v2
Bibliography is built from:
- source registry IDs in `sources.yaml`
- machine-readable evidence tokens
not from arbitrary footnote prose

## Tasks

### 1. Source use extraction
Extract all `source_id` values from evidence tokens and resolved editorial notes that cite a registry source.

### 2. Bibliography build
For each used `source_id`, emit the BibTeX entry from the registry metadata.

### 3. Assembly
Build `book.adoc` in `toc.yaml` order using explicit chapter paths.

### 4. Validation
Check:
- no unresolved markers
- all anchors resolve
- all cross-references resolve
- all cited `source_id`s exist in the registry
- all includes exist
- Asciidoctor builds succeed

## Output
- `book.adoc`
- `bibliography.bib`
- `validation-report.md`
- rendered PDF/EPUB

## Validation report minimum contents

```markdown
# Validation Report

## Marker scan
<results>

## Source registry resolution
<results>

## Anchor and cross-reference validation
<results>

## Asciidoctor PDF build
<results>

## Asciidoctor EPUB build
<results>
```

---

## Closing note to reviewer AI

<!--
REVIEWER NOTE

This revision intentionally strengthens the pipeline in procedural ways that make it less elegant on paper but more reliable in practice.

The main design bet is that the quality bottleneck is not in prompt wording but in weak artifact contracts. If you disagree, please identify which of the newly added contracts are unnecessary and why they could be safely removed without reintroducing hallucination, contamination, or assembly fragility.
-->
