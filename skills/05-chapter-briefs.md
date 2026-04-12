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
For each story, assess in-scope variants and classify into one of four categories:
- **single-prevalent**: one variant is clearly dominant in the scholarly corpus. Others are minor. → body presents the prevalent version, footnotes carry variants.
- **single-prevalent-reconstructed**: one variant dominates but its text is incomplete — the base text has physical gaps filled from other witnesses or scholarly reconstruction. → body presents the reconstructed base text with `[RECONSTRUCTION:]` markers, footnotes carry variants.
- **co-equal**: multiple variants are roughly equally attested, or no scholarly consensus on prevalence. → body presents variants inline, each with its source.
- **composite-editorial**: no single source contains the complete narrative — the scholarly standard is a composite text assembled from multiple witnesses (common for multi-tablet cycles). → body follows the standard editorial composite, footnotes note where individual witnesses diverge.

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

## Outputs: `briefs/NN-<slug>.yaml` and `toc.yaml`

One brief per chapter, plus `toc.yaml` recording the final chapter order (used by `intro-chapter`, `format-finalize`, and other downstream stages).

```yaml
chapter_number: <n>
slug: <slug>
title: "<editorial chapter title>"
chapter_anchor: "ch-<NN>-<slug>"   # Canonical anchor ID — used in all cross-references, never auto-generated

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
  classification: single-prevalent | single-prevalent-reconstructed | co-equal | composite-editorial
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
    # Surface-level parallels for the intro chapter's "cross-cultural resonance" preview.
    # Keep to 1–2 sentences each. These orient the reader, not analyze the parallel.
    - other_culture: <name>
      parallel: <one sentence>
      source: <id>

comparative_hooks:
  # Deeper or more specific parallels for the comparative chapter's full analysis.
  # These may overlap with cross_cultural_parallels but go into more detail
  # (e.g., specific motifs, structural parallels, scholarly debate).
  - other_culture: <name>
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

## Completion protocol

As your very last action — after all output files are written and all self-checks pass — write a completion record. This allows the pipeline runner to verify that no stage was truncated by a timeout, rate limit, or context overflow.

**File**: `books/<book>/completions/<NN>-<stage-name>.done.yaml`

Create the `completions/` directory if it does not exist.

**Format**:
```yaml
stage: "<stage-name>"
timestamp: "<UTC ISO 8601>"
status: "completed"
agent_model: "<your model name>"
outputs:
  - file: "<relative path from book dir>"
    lines: <line count>
  # repeat for each output file
summary: "<one-line description of what was produced>"
```

**Rules**:
1. Write this file only after ALL outputs are complete and verified.
2. The `lines` count must be the actual line count of each file at the time of writing — do not estimate.
3. If you were unable to complete all outputs, write the file with `status: "partial"` and list which outputs are missing in a `missing` field.
4. Never write `status: "completed"` if any output file is missing or truncated.

## Handoff
To `glossary-lock`, which runs once over all briefs before any drafting. The `cultural_relevance` fields also feed `intro-chapter`.
