# Mythology Book Pipeline — Full Pack for Review

This document contains the full pipeline: the README (overview and principles), the CHANGELOG, and all 19 skill files (step-by-step instructions for each stage). Each section is marked with a `FILE N of 21` header. This bundle is a HEAD snapshot as of 2026-04-23.

---

# FILE 1 of 21: README.md

# Mythology Book Pipeline

A step-by-step process for producing mythology books in the style of Isaac Asimov's non-fiction: clear, plain-English retellings of myths, one culture per book, with every factual claim traced to a scholarly source. The process uses AI agents (Claude, GPT, Gemini, etc.) working in sequence, each doing one job and checked in a fresh conversation with no memory of the writing — ideally by a different AI model, but the same model is acceptable when running a different one is impractical. It handles the hard parts of mythology writing: gaps in ancient texts, contradictory versions of the same story, and the constant risk of mixing up material from neighboring cultures.

## Core principles

1. **The checker must have no memory of the writing.** Every check runs in a fresh conversation (or a fresh process, for autonomous runs) so the checker cannot rely on anything but the artefacts in front of it. Using a different AI model for the check is preferred — two models make independent mistakes — but the same model in a fresh conversation is acceptable when a second model is not available. What never works is self-review in the same conversation: it catches almost nothing.

2. **Three files govern the entire book.** Three files are created early and must be read by every AI and every human before starting any later stage:
   - `scope.md` — what culture, period, and sources the book covers, and what it explicitly excludes.
   - `sources.yaml` — the approved list of scholarly sources (whitelist) and banned popularizations (blacklist).
   - `glossary.yaml` — the locked English translations for key terms (created after the scope, before any writing begins).

   These are the single source of truth. If an AI or human is unsure whether something belongs in the book, these files have the answer.

3. **Cite only sources you can see.** When writing, the AI may only cite sources whose text has been pasted into the conversation or retrieved during it. No citing from the AI's training memory, even for famous texts. This is the main defense against fabricated references — a common AI failure mode.

4. **Contradictions between sources are normal, not errors.** Ancient mythologies have multiple versions of the same story. Two legitimate sources disagreeing is part of the record, not a mistake. The pipeline handles this explicitly: when one version dominates the scholarly record, it goes in the main text with alternatives in footnotes. When versions are roughly equal, they are presented side by side. The key is to never silently pick one and ignore the others.

5. **Check the document, not the deity.** When checking whether something belongs in the book, the question is: "Does this specific story detail appear in a document from within our scope?" — not "Does this god belong to our culture?" Gods and heroes cross cultural boundaries; specific narrative details are tied to specific texts. A detail found only in a Babylonian tablet does not belong in a Sumerian book, even if the god is originally Sumerian.

6. **Chapter length follows the evidence.** A myth preserved on a single broken tablet gets a short chapter. A richly-documented cycle gets a long one. Chapters are never padded to reach a target length.

7. **Human edits are validated before proceeding.** Every time a human reviews and modifies a file, the result must pass a validation step (`post-human-normalize`) before it becomes input for the next stage. Human edits are one of the main ways that the pipeline's structural guarantees can break — merged claims, removed markers, altered citations. The validator catches these before they propagate.

8. **Comparison metadata is not comparison prose.** Cross-cultural notes may exist in planning files and comments throughout the pipeline, but reader-facing comparison prose is confined to the comparative chapter. This distinction — noting a parallel vs. writing about it — must be enforced.

## Global contracts

These rules apply across all stages. They are not repeated in each skill, but every skill must comply.

**Provenance metadata.** Every machine-generated file must include a metadata block recording: the stage that produced it, the AI model used, and a timestamp. For YAML files, use a `meta:` section. For AsciiDoc files, use a comment block at the top. This makes model-separation auditable rather than trust-based.

**Canonical anchors.** Every chapter has a stable anchor ID defined in its brief (e.g., `ch-01-descent-of-inanna`). All cross-references use this anchor, never auto-generated section IDs. Anchors survive marker-resolve and line-edit unchanged.

**Evidence tokens.** Every factual claim carries both a reader-facing AsciiDoc footnote AND a machine-readable evidence token in a comment. The token format is: `// EVIDENCE: source_id=<id> ; loc=<tablet/line/page>`. The `format-finalize` stage builds the bibliography from these tokens (not from parsing footnote prose), which eliminates ambiguity between bibliographic and editorial footnotes.

**Negative-evidence discipline.** When a source does not attest something (e.g., no physical description survives), this must be stated explicitly and scoped: "No physical description survives in the in-scope sources" — not "No description exists." Absence of evidence in the in-scope corpus is not the same as universal absence.

**Template discipline.** Any skill that tells an agent to render a marker, claim, footnote, or other structured element into prose using a template with `<placeholder>` slots must follow three rules:

1. *Every template ships with at least one worked input→output example.* A template without an example is a specification, not an instruction — agents will guess at the slot-filling rule and guess differently each time.
2. *Every template specifies a trailing-punctuation rule.* If a slot value may end with `.`, `?`, `!`, or `…`, the template must say explicitly whether to suppress its own following separator. Past runs have shipped "..]_" and ".. Risk:" into the final PDF because this was implicit.
3. *Every template specifies fallback behaviour for empty, missing, or sentinel-valued slots* (`none`, `n/a`, `—`, etc.). The renderer must never emit a literal `<placeholder>` token, an empty paren `(. [n])`, or a leaked sentinel word. When a required slot is missing, the skill must describe a concrete fallback (e.g. "render the claim as plain prose without a footnote") rather than letting the agent improvise.

The corresponding skill's self-check must include grep-based anti-pattern checks for each of the three failure modes (placeholder leaks, empty slots, sentinel leaks), and the downstream stage that assembles final artefacts must mirror those checks as a safety net.

## Stage order

The book is built in stages. Each stage produces a file that the next stage consumes. `[HUMAN]` marks points where you review and approve before continuing. The arrows show what feeds into what:

```
scope-lock → story-inventory → inventory-audit →
  [HUMAN] → post-human-normalize(inventory) →
  chapter-briefs → glossary-lock →
  intro-chapter → prose-factcheck(intro) →
  [HUMAN] → post-human-normalize(intro) →
  [per chapter:
    chapter-claims → claims-factcheck →
    [HUMAN] → post-human-normalize(claims) →
    chapter-draft → narrative-fidelity →
    [HUMAN if REVISE] → post-human-normalize(narrative if revised)] →
  comparative-chapter → prose-factcheck(comparative) →
  [HUMAN] → post-human-normalize(comparative) →
  marker-resolve → line-edit →
  character-appendix → prose-factcheck(appendix) →
  [HUMAN] → post-human-normalize(appendix) →
  format-finalize
```

**In plain English:** First you define what the book covers and what sources are allowed (scope-lock). Then an AI researches all the stories (story-inventory), and the list is checked in a fresh conversation (inventory-audit) — ideally by a different AI, but the same model in a fresh conversation is fine. You review, the result is validated (post-human-normalize), then turned into one planning document per chapter (chapter-briefs) and a locked glossary (glossary-lock). An introductory chapter on cultural context is written and fact-checked in a fresh conversation (prose-factcheck); you review; the result is validated. Then, for each story chapter: the facts are written out one by one (chapter-claims), checked in a fresh conversation (claims-factcheck), you review, the result is validated, then the facts are turned into narrative prose (chapter-draft), and a fresh conversation confirms the prose faithfully represents the facts (narrative-fidelity) — if it finds problems, you review and the result is validated. After all story chapters are done, a cross-cultural comparison chapter is written and fact-checked (prose-factcheck); you review; validated. Then all chapters get their placeholder markers converted to final text (marker-resolve) and a prose-quality polish (line-edit). A character reference appendix is compiled and fact-checked (prose-factcheck); you review; validated. Finally, everything is assembled into a book with a bibliography and validated (format-finalize).

## Artifact layout per book

```
<book-name>/
  cover.jpg                          (provided by user — JPG or PNG)
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
  comparative.adoc                   (drafted)
  comparative.factcheck.yaml         (audited)
  comparative.resolved.adoc          (markers resolved)
  comparative.edited.adoc            (line-edited)
  comparative.diff.md                (line-edit diff)
  character-appendix.adoc            (character reference)
  character-appendix.factcheck.yaml  (audited)
  book.adoc                          (master)
  bibliography.bib
  validation-report.md
```

## Output format

AsciiDoc, rendered via Asciidoctor (not Pandoc) to PDF and EPUB. Pandoc is still useful for DOCX export if needed.

## What changed from v1

See `CHANGELOG.md`.

---

# FILE 2 of 21: CHANGELOG.md

# Changelog

## v2.1

**New skills (from external review)**
- `post-human-normalize` — validates human-edited files before they become downstream inputs. Catches broken schemas, merged claims, removed markers, and altered citations. Runs after every `[HUMAN]` checkpoint.
- `claims-factcheck` — dedicated factcheck for isolated claims documents (one claim per paragraph). Split from the former unified `chapter-factcheck`.
- `prose-factcheck` — dedicated factcheck for prose content (intro, comparative, character appendix). Includes an explicit claim-extraction pass (Pass 0) before verification. Split from the former unified `chapter-factcheck`.

**Structural improvements (from external review)**
- `sources.yaml` expanded from simple whitelist into a full source registry with `full_citation`, `short_citation`, `source_tier`, `identifier_type`, and `identifier_value` fields. Supports automated bibliography generation.
- Machine-readable evidence tokens (`// EVIDENCE: source_id=X ; loc=Y`) added alongside reader-facing footnotes. `format-finalize` builds bibliography from tokens, not from parsing footnote prose.
- Canonical chapter anchors defined in briefs (`chapter_anchor` field). Cross-references use these, never auto-generated section IDs.
- Provenance metadata blocks required on all machine-generated files (`auditor_model`, `auditor_conversation_id`).
- Variant classification expanded from 2 to 4 categories: `single-prevalent`, `single-prevalent-reconstructed`, `co-equal`, `composite-editorial`.
- Global contracts section added to README: provenance metadata, canonical anchors, evidence tokens, negative-evidence discipline, human-review re-entry rule.
- Comparison-metadata vs comparison-prose distinction made explicit as core principle 8.

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

# FILE 3 of 21: skills/01-scope-lock.md

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

This file is a real source registry, not just a whitelist. Later stages use it for citation normalization, bibliography generation, and disambiguation. Every field marked (required) must be present.

```yaml
registry:
  - id: <short_id>                              # (required) unique key, used in all citations
    source_tier: primary | primary-translation | secondary | reference | comparative
    in_scope: true | false                       # false for comparative-only sources
    author: <last, first>                        # (required)
    title: <title>                               # (required)
    year: <year>                                 # (required)
    translator_editor: <name, if applicable>
    container_title: <journal or edited volume, if applicable>
    full_citation: <complete bibliographic string>  # (required) — used in first footnote mention
    short_citation: <author year>                   # (required) — used in subsequent footnote mentions
    identifier_type: DOI | ISBN | corpus-id | museum-number | stable-url
    identifier_value: <the identifier>              # (required)
    access_url: <where to retrieve the text, if online>
    notes: <any caveats — e.g., "translation only, no original-language text">

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

The `full_citation` and `short_citation` fields are used directly by `format-finalize` to build the bibliography — no parsing of free-text footnotes required.

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
Pass `scope.md` and `sources.yaml` to `story-inventory`. These files are re-read by every subsequent skill.

---

# FILE 4 of 21: skills/02-story-inventory.md

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
To `inventory-audit`, which must be run in a fresh conversation — preferably with a different AI model, but the same model in a fresh conversation is acceptable if a different one is impractical.

---

# FILE 5 of 21: skills/03-inventory-audit.md

---
name: inventory-audit
description: Checks the story inventory for errors before any writing begins. Must be run in a fresh conversation with no memory of producing the inventory — preferably by a different AI model, but the same model in a fresh conversation is acceptable if a different one is impractical. Catches material from wrong cultures, made-up references, missing well-known stories, and silently merged variants.
---

# inventory-audit

## For the human

This is the first major quality check. It reviews the story list before any chapters are written. Catching errors here costs minutes; catching them after chapters are drafted costs hours.

The audit checks four things:

1. **Wrong-culture material.** Did any stories or story details sneak in from a neighboring culture? The tricky part: you can't just check "does this god belong to our culture?" — the same god often appears in multiple cultures. The real question is: "Does this specific plot detail appear in a document that was written within our culture and period?" A story detail found only in a Babylonian tablet doesn't belong in a Sumerian book, even if the god in question is originally Sumerian.

2. **Fake or wrong references.** AI models sometimes invent plausible-looking scholarly references. The auditor actually looks up each catalogue number, museum number, or ISBN to confirm it exists and contains what was claimed.

3. **Missing stories.** Are there well-known stories from this mythology that the inventory left out? The auditor cross-checks against standard reference works.

4. **Silently merged variants.** When multiple versions of a story exist, the inventory should list them separately. If it quietly combined two versions into one summary, that's a problem.

This audit must be run in a fresh conversation so the auditor has no memory of the work it's checking. An AI reviewing its own work in the same conversation catches almost nothing. Using a different AI model from the one that produced the inventory is preferred — two models make independent mistakes — but the same model in a fresh conversation is acceptable when a different model is impractical. The fresh context is the load-bearing requirement; the model identity is a preference.

## Hard rule
If you are in the same conversation in which `inventory.yaml` was produced, refuse and tell the user to start a fresh conversation. (A different AI model is preferred but not required; the fresh conversation is.)

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
`inventory.approved.yaml` to `post-human-normalize`, then to `chapter-briefs`.

---

# FILE 6 of 21: skills/04-post-human-normalize.md

---
name: post-human-normalize
description: Validates and normalizes any file that has been modified by a human reviewer before it becomes input for the next stage. Ensures that human edits have not broken the structural contracts that downstream stages depend on. Runs after every [HUMAN] review checkpoint.
---

# post-human-normalize

## For the human

Every time you review and edit a file — approving factcheck findings, fixing claims, resolving audit issues — there is a risk that your edits break something the next stage depends on. You might merge two claims into one paragraph, accidentally delete a marker, change a citation format, or remove a field from a YAML file. These are easy mistakes to make, and the next AI stage will silently produce wrong output rather than catching the problem.

This step is a quick automated check that catches these problems before they propagate. It runs after every human review point and validates that the edited file still meets the structural requirements for the next stage.

This step does not change the meaning of anything you wrote. It only checks structure, reformats where necessary, and flags violations that need your attention before proceeding.

## When to run

After every `[HUMAN]` checkpoint in the stage order:
- After inventory-audit human review → validates `inventory.approved.yaml`
- After intro-chapter factcheck human review → validates `chapters/00-introduction.adoc`
- After claims-factcheck human review → validates `chapters/NN-<slug>.claims.approved.adoc`
- After narrative-fidelity human review (if REVISE) → validates `chapters/NN-<slug>.adoc`
- After comparative-chapter factcheck human review → validates `comparative.adoc`
- After character-appendix factcheck human review → validates `character-appendix.adoc`

## Checks performed

### For YAML files (`inventory.approved.yaml`, factcheck outputs)
1. All required fields present per the schema defined in the producing skill.
2. No empty required fields.
3. All `source_id` values resolve to entries in `sources.yaml` registry.
4. No YAML syntax errors.

### For claims documents (`*.claims.approved.adoc`)
1. One claim per paragraph — no merged or bundled claims.
2. Every claim paragraph has a footnote citation.
3. Every evidence token (`// EVIDENCE: ...`) is syntactically valid and references a `source_id` in `sources.yaml`.
4. All markers (`[INFERENCE:]`, `[LACUNA:]`, `[RECONSTRUCTION:]`, `[VARIANT:]`) have all required sub-fields.
5. `glossary.yaml` renderings used consistently.

### For prose documents (intro, comparative, character-appendix, narrative chapters)
1. All markers syntactically valid with required sub-fields.
2. All evidence tokens syntactically valid.
3. Canonical chapter anchors present and unchanged.
4. `glossary.yaml` renderings used consistently.
5. No `never_use` glossary terms present.

## Output

The validated file, with a provenance comment block appended:
```
// Validated by post-human-normalize
// Timestamp: <UTC>
// Checks passed: <list>
// Warnings: <any non-blocking issues>
```

If any check fails, the file is returned to the human with a specific error report. The pipeline does not proceed until all checks pass.

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
The validated file proceeds to the next stage as defined in the stage order.

---

# FILE 7 of 21: skills/05-chapter-briefs.md

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

---

# FILE 8 of 21: skills/06-glossary-lock.md

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

## Mid-pipeline glossary updates

If a later stage (e.g., `chapter-claims`) encounters a recurring term that should be in the glossary but isn't, the AI should stop and flag it. The human then adds the term to `glossary.yaml` using the same process (survey renderings, pick one, add `never_use` entries). This does not require re-running `glossary-lock` from scratch — just append the new entry and confirm consistency with existing entries.

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
`glossary.yaml` to `intro-chapter` and `chapter-claims`.

---

# FILE 9 of 21: skills/07-intro-chapter.md

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

This chapter makes factual claims about cultural significance, so it goes through the same fact-checking process as any other chapter: every claim is checked against sources in a fresh conversation (ideally by a different AI model, but the same model in a fresh conversation is acceptable if a different one is impractical).

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

**Marker placement — MUST be on its own line.** Both `// EVIDENCE: ...` and `// COMPARATIVE-HOOK: ...` must start at column 0 on a line by themselves, not appended after paragraph text. AsciiDoc only treats `//` as a comment when it starts the line; a marker appended after `footnote:[...]` renders as literal text in the output. Same rule as `chapter-claims` and `chapter-draft`.

```
Correct:

The composition is catalogued as ETCSL 1.1.1.footnote:[ETCSL 1.1.1.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1

Wrong (marker renders as visible text):

The composition is catalogued as ETCSL 1.1.1.footnote:[ETCSL 1.1.1.] // EVIDENCE: source_id=etcsl ; loc=1.1.1
```

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
9. Every `// EVIDENCE:` and `// COMPARATIVE-HOOK:` marker starts at column 0 on its own line. None appended to paragraph lines.

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
To `prose-factcheck`, in a fresh conversation (a different AI model is preferred but not required).

---

# FILE 10 of 21: skills/08-chapter-claims.md

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
2. **The citation** — AsciiDoc footnote for the reader, pointing to the specific source, location, and (where possible) a verbatim quote or close paraphrase from the source.
3. **The evidence token** — a machine-readable comment on the line after the claim, for automated bibliography building and validation.

```
Enlil separated heaven (An) from earth (Ki), creating the space in which the atmosphere exists.footnote:[Black et al. 2004, ETCSL 1.1.2, lines 1–5: "After heaven had been moved away from earth, after earth had been separated from heaven, after the name of man had been fixed..."]
// EVIDENCE: source_id=black2004 ; loc=ETCSL 1.1.2, lines 1-5
```

The footnote is for the reader. The evidence token is for the machine. `format-finalize` builds the bibliography from evidence tokens, not from parsing footnote prose — this avoids ambiguity between bibliographic and editorial footnotes.

## Source overview section

Before the narrative claims, begin with a `=== Source overview` section. This grounds the reader in the physical evidence — the actual artifacts, documents, or traditions through which we know this story. Each claim in this section is a factual assertion about a source, not about the myth's content.

Include claims covering:
1. **What survives.** Name the specific tablets, manuscripts, or attestations (with museum numbers or corpus IDs where known). How many witnesses exist? From which sites?
2. **State of preservation.** Is the text complete, fragmentary, or heavily damaged? Where are the major gaps?
3. **Composite or single witness?** Is the "text" scholars read a composite stitched from many tablets, or does it survive on a single artifact?
4. **Discovery context.** When and where was the primary tablet found, if known? (e.g., "recovered from the Nippur scribal quarter during the University of Pennsylvania excavations")
5. **Scholarly edition.** Which critical edition or translation is the basis for this chapter?

This section is factual and citeable — every claim about a tablet's provenance, museum number, or preservation state must have a footnote. It feeds directly into the chapter-draft's opening passage, which orients the reader before the story begins.

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

=== Source overview

<Claim about physical artifacts — tablets, museum numbers, sites of discovery.>

<Claim about state of preservation — complete, fragmentary, lacunae.>

<Claim about the composite nature of the text, if applicable.>

<Claim about the critical edition or translation used as basis.>

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
1. The `=== Source overview` section is present and contains at least 3 claims about the physical artifacts, preservation state, and scholarly edition.
2. Every claim is a single factual assertion — no bundled claims, no narrative connective tissue.
3. Every claim has footnote coverage citing a source provided in this conversation. Nothing from memory.
4. Claims follow the narrative order of the myth.
4. The claims skeleton is complete — everything the narrative will need is here.
5. Every marker has all required sub-fields.
6. No out-of-scope material.
7. Variant handling matches the brief's classification.
8. `glossary.yaml` renderings used throughout.

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
To `claims-factcheck`, in a fresh conversation (a different AI model is preferred but not required). The fact-checker's job is dramatically simplified: each claim is isolated and individually cited.

---

# FILE 11 of 21: skills/09-claims-factcheck.md

---
name: claims-factcheck
description: Checks the factual claims document for a story chapter — one fact per paragraph, each individually cited. This is the primary factcheck mode and the most reliable, because each claim is isolated and trivially verifiable. Must be run in a fresh conversation with no memory of producing the claims (a different AI model is preferred but not required).
---

# claims-factcheck

## For the human

This is the most important quality check for story chapters. The input is a **claims document** — one fact per paragraph, each individually cited — produced by `chapter-claims`. Each paragraph is one claim, one source reference, one thing to verify. No prose to parse, no bundled assertions to disentangle.

This step enforces four disciplines:

1. **Show your evidence.** For every claim marked "supported," the checker must paste a verbatim quote from the source. Not a paraphrase — the actual text. No quote, no "supported" verdict.

2. **Verify the references.** Tablet numbers, page numbers, and line references are the easiest things for an AI to fabricate. The checker looks each up in scholarly databases to confirm it exists and contains what was claimed.

3. **Distinguish contradictions from errors.** Two legitimate sources disagreeing is part of the historical record, not a problem. Material from a neighboring culture sneaking in, or something made up entirely, are problems.

4. **Read it backwards too.** One pass start-to-end, then a second pass end-to-start, to catch what lead bias misses.

## Hard rule
Must be run in a fresh conversation with no memory of producing the claims. If you have any memory of producing the input, refuse. Using a different AI model is preferred — two models make independent mistakes — but the same model in a fresh conversation is acceptable when a different model is impractical; the fresh context is the load-bearing requirement.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- `chapters/NN-<slug>.claims.adoc` (claims document)
- `briefs/NN-<slug>.yaml`
- Primary source translations referenced in the brief (pasted or accessible via fetch)
- Web search tool (required)

## The five passes

### Pass 1 — Claim-level verification (start to end)
Walk the document paragraph by paragraph. Each paragraph is one claim. Assign a verdict:

- **✓ SUPPORTED** — Must include a verbatim quote from a cited in-scope source.
- **△ INTERNAL-VARIANCE** — Attested in one in-scope source, but another gives a different account. Not a finding. Flag only if variant handling mismatches the brief's classification.
- **? UNVERIFIED** — No supporting quote found. Default when uncertain.
- **! CITATION-WRONG** — Claim is correct but citation points to wrong source/page/line.
- **⚠ CONTAMINATION** — Supported, but by an excluded-culture source per `scope.md`.
- **✗ FABRICATION** — Not supported by any source you can locate.

### Pass 2 — Triangulation of references
Verify each citation's tablet number, line range, or page reference resolves in a `triangulation_databases` entry. Non-resolving: CITATION-WRONG, HIGH severity, with verification URL.

### Pass 3 — Document-provenance contamination scan
For each factual detail: is this detail attested in a document within the scope's date range and culture? Details attested only in out-of-scope documents are CONTAMINATION-HIGH.

### Pass 4 — Marker integrity
- `[INFERENCE:]` — genuinely inferential? If a source directly attests it, flag MARKER-MISUSED.
- `[LACUNA:]` — source actually has the claimed gap?
- `[RECONSTRUCTION:]` — fill source is in-tradition per `scope.md`?
- `[VARIANT:]` — both quoted phrases present in cited sources?
- **Silent bridges** — uncited claims not under a marker. Flag SILENT-BRIDGE, HIGH.

### Pass 5 — Reverse-order second pass
Walk from last claim to first. Add any new findings.

**Glossary**: check consistency. **Style**: not checked — there is no prose yet.

## Output: `chapters/NN-<slug>.claims.factcheck.yaml`

```yaml
meta:
  auditor_model: <name and version>
  auditor_conversation_id: <conversation ID if available>
  input_file: <path>
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
  - claim_number: <n>
    claim: "<the claim>"
    source_id: <from sources.yaml>
    source_loc: <tablet/line/page>
    verbatim_quote: "<exact text from source>"

findings:
  - claim_number: <n>
    kind: UNVERIFIED | CITATION-WRONG | CONTAMINATION | FABRICATION | SILENT-BRIDGE | MARKER-MISUSED | MARKER-FABRICATED | GLOSSARY-VIOLATION | VARIANT-HANDLING-MISMATCH
    severity: HIGH | MEDIUM | LOW
    claim: "<the claim>"
    issue: <one sentence>
    evidence: <verbatim quote or triangulation URL>
    recommended_fix: <concrete>
```

## Verdict rules

Apply in order (first match wins):
- **MAJOR-REVISE**: ≥ 3 HIGH findings, or any contamination, or triangulation failures indicating fabricated references.
- **REVISE**: 1–2 HIGH, or > 3 MEDIUM, or any silent bridge.
- **PASS**: zero HIGH, zero silent bridges, ≤ 3 MEDIUM.

## Honesty self-check
Answer in `meta`:
1. Did I open every cited primary source, or skim? Name any I skimmed.
2. Did I triangulate every reference, or assume some? Name any assumed.
3. For every ✓, did I paste a real quote or pattern-match? Downgrade any pattern-matched.
4. Did I distinguish internal variance from contamination?
5. Am I the same model that produced the claims? If yes, this audit is invalid.

## Human review protocol
Review HIGH findings (~10 minutes), skim MEDIUM. Apply accepted fixes to produce `chapters/NN-<slug>.claims.approved.adoc`. Run `post-human-normalize` before proceeding to `chapter-draft`.

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
After human review and normalization: `chapters/NN-<slug>.claims.approved.adoc` to `chapter-draft`.

---

# FILE 12 of 21: skills/10-prose-factcheck.md

---
name: prose-factcheck
description: Checks factual claims embedded in prose — for the intro chapter, comparative chapter, and character appendix. Unlike claims-factcheck which operates on isolated claims, this skill must first extract claims from flowing prose before verifying them. Must be run in a fresh conversation with no memory of producing the content (a different AI model is preferred but not required).
---

# prose-factcheck

## For the human

This is the factcheck for prose content that wasn't written through the claims-first process: the intro chapter, the comparative chapter, and the character appendix. Unlike `claims-factcheck` (where each paragraph is one isolated, individually cited claim), here the checker must first extract the factual claims from flowing prose — a harder task that requires judgment about what constitutes a claim vs. connective tissue.

The same four disciplines apply (show evidence, verify references, distinguish contradictions from errors, read backwards), but with an added initial step: claim extraction.

## Hard rule
Must be run in a fresh conversation with no memory of producing the content. A different AI model is preferred — two models make independent mistakes — but the same model in a fresh conversation is acceptable when a different model is impractical; the fresh context is the load-bearing requirement.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- The prose document to check:
  - `chapters/00-introduction.adoc` (intro chapter)
  - `comparative.adoc` (comparative chapter)
  - `character-appendix.adoc` (character appendix)
- Primary source translations (pasted or accessible via fetch)
- Web search tool (required)

## The six passes

### Pass 0 — Claim extraction
Walk the prose document and extract every factual claim into a numbered list. A claim is any assertion about the myth, character, or culture — not transitions, opinions, or reader-orienting context. This extraction is the foundation for all subsequent passes. Record each extracted claim with its paragraph location.

This pass is what makes prose-factcheck harder than claims-factcheck. The quality of the entire audit depends on thorough extraction.

### Pass 1 — Claim-level verification (start to end)
For each extracted claim, assign a verdict using the same six verdicts as `claims-factcheck` (✓ SUPPORTED, △ INTERNAL-VARIANCE, ? UNVERIFIED, ! CITATION-WRONG, ⚠ CONTAMINATION, ✗ FABRICATION).

### Pass 2 — Triangulation of references
Same as `claims-factcheck`.

### Pass 3 — Document-provenance contamination scan
Same as `claims-factcheck`.

### Pass 4 — Marker and glossary integrity
- Check all markers have required sub-fields.
- For comparative chapter: verify `[SPECULATION:]` markers have both basis and counterargument.
- Check `glossary.yaml` renderings and `never_use` terms.
- For character appendix: flag any physical-description language without a source citation (the primary fabrication risk).

### Pass 5 — Reverse-order second pass
Same as `claims-factcheck`.

## Output

- `chapters/00-introduction.factcheck.yaml`
- `comparative.factcheck.yaml`
- `character-appendix.factcheck.yaml`

Same YAML schema as `claims-factcheck`, plus:

```yaml
meta:
  claims_extracted: <n>   # from Pass 0 — if this is low, extraction was lazy
```

## Verdict rules
Same as `claims-factcheck`.

## Honesty self-check
Same as `claims-factcheck`, plus:
6. Did I extract every factual claim in Pass 0, or only the prominent ones? Name any sections I under-extracted.

## Human review protocol
Review HIGH findings. Apply accepted fixes directly to the prose file. Run `post-human-normalize` before proceeding.

- **Intro chapter** → corrected `chapters/00-introduction.adoc` proceeds to `post-human-normalize`, then `marker-resolve`.
- **Comparative chapter** → corrected `comparative.adoc` proceeds to `post-human-normalize`, then `marker-resolve`.
- **Character appendix** → corrected `character-appendix.adoc` proceeds to `post-human-normalize`, then `format-finalize`.

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
After human review and normalization: the corrected file proceeds to the next stage as defined in the stage order.

---

# FILE 13 of 21: skills/11-chapter-draft.md

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

## Source overview opening

Every chapter begins with a short prose passage (2–5 paragraphs) that orients the reader in the physical evidence before the story begins. This passage is built from the `=== Source overview` claims in the approved claims document and covers:

- **What we have**: the tablets, fragments, or manuscripts — named by museum number or corpus ID where possible — and where they were found.
- **What condition it is in**: complete, fragmentary, or composite. Where the major gaps are.
- **How we read it**: which critical edition or translation the retelling follows.

This passage sets the Asimov register immediately: the reader understands they are about to hear a story reconstructed from physical artifacts, not received from some mystical tradition. It is the scholarly equivalent of "here is the evidence, now here is the story it tells."

The source overview is separated from the narrative body by a blank line or a section transition (e.g., "The story, as the tablets preserve it, goes as follows."). It is not a dry bibliography — it is narrative prose about artifacts, written in the same Asimov register as the rest of the chapter.

## Output: `chapters/NN-<slug>.adoc`

```asciidoc
== <Chapter Title>

<Source overview — 2-5 paragraphs on the physical evidence: tablets, sites, preservation, edition. Built from the Source overview claims.>

<Transition to narrative.>

<Body — the verified claims, woven into narrative prose. Every claim present, no claims added.>

<Closing — brief note on the story's place in the culture's corpus. No cross-cultural comparison. Carry over `// COMPARATIVE-HOOK:` comments from claims document.>
```

## Self-check before returning
1. **Source overview present**: the chapter opens with 2–5 paragraphs on the physical evidence, built from the Source overview claims. No source overview = incomplete chapter.
2. **Completeness**: walk the approved claims document claim by claim — including Source overview claims. Is every claim represented in the narrative? List any you cannot find — they are bugs.
3. **No additions**: scan the narrative for any factual assertion that does not correspond to a claim in the approved document. Flag it.
3. Scan for forbidden words — each hit is a drift signal; revise.
4. Every proper noun was glossed on first mention using `glossary.yaml`.
5. Variant handling matches the brief's classification.
6. Every marker has survived from claims to narrative.
7. All footnotes carried over unchanged.
8. Length matches the brief's target. Not padded.
9. `// COMPARATIVE-HOOK:` comments carried over.

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
To `narrative-fidelity`, in a fresh conversation (a different AI model is preferred but not required).

---

# FILE 14 of 21: skills/12-narrative-fidelity.md

---
name: narrative-fidelity
description: Checks that the narrative prose faithfully represents the verified facts — nothing dropped, nothing added, nothing distorted. Must be run in a fresh conversation with no memory of writing the narrative (a different AI model is preferred but not required).
---

# narrative-fidelity

## For the human

The facts have been verified. The narrative has been written from those verified facts. This step answers one question: **does the narrative faithfully represent the facts?**

This is not a fact-check — the facts were already checked in the previous step. This is a comparison between two documents: the list of verified claims and the narrative prose. It catches three problems:

1. **Dropped facts.** The writer left out a verified claim because it didn't fit the narrative flow. The reader loses information.
2. **Added facts.** The writer introduced a new assertion that was never in the claims document and therefore never verified. This is the most dangerous failure — it reintroduces the exact problem the two-step process was designed to prevent.
3. **Distorted facts.** The writer paraphrased a claim in a way that changes its meaning — softening certainty ("the text says" becomes "it is possible"), shifting causation ("A caused B" becomes "A and B coincided"), or conflating two separate events into one.

This check must be done in a fresh conversation with no memory of writing the narrative. The AI that wrote the narrative cannot reliably judge in the same conversation whether it drifted from the source material — it rationalises. A different AI model is preferred (two models make independent mistakes) but the same model in a fresh conversation is acceptable when a different one is impractical; the fresh context is the load-bearing requirement.

## Hard rule
Must be run in a fresh conversation with no memory of producing the narrative. If you produced the narrative, refuse. (A different AI model is preferred but not required.)

## Inputs
- `chapters/NN-<slug>.claims.approved.adoc` (the verified claims — the ground truth)
- `chapters/NN-<slug>.adoc` (the narrative)
- `briefs/NN-<slug>.yaml` (for variant classification reference)
- `glossary.yaml`

**Not** primary sources. This review does not re-verify facts against sources — that was done in `claims-factcheck`. This review compares narrative against claims only.

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

## Human review protocol

If the verdict is **PASS**: the chapter proceeds to `marker-resolve` (after all chapters are done and the comparative chapter is written and fact-checked).

If the verdict is **REVISE**: review the findings. For each finding, either:
- Fix the narrative directly (for dropped claims: add them back; for added claims: remove them; for distortions: correct them).
- Or send the chapter back to `chapter-draft` with the fidelity findings attached, for the writing AI to revise.

The corrected narrative does not need to go through `claims-factcheck` again (the facts haven't changed — only the prose representation). But it should go through `narrative-fidelity` again to confirm the fixes resolved the findings.

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
After PASS (or PASS on re-review): the chapter waits until all story chapters are complete, then proceeds with the comparative chapter and marker-resolve.

---

# FILE 15 of 21: skills/13-marker-resolve.md

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
- Story chapters after narrative-fidelity has passed (`chapters/NN-<slug>.adoc`)
- Intro chapter after factcheck and human review (`chapters/00-introduction.adoc`)
- Comparative chapter after factcheck and human review (`comparative.adoc`)
- `scope.md` (for marker-rendering preferences)

## Agent instructions

Resolve each marker per these rules. Do not alter any other prose.

### Universal rendering rules

These four rules apply to every marker type below. They exist because past runs of this stage have shipped broken prose to readers — literal `none` labels, empty parentheses that print as `(. [n])` in the PDF, double periods, and placeholder tokens like `<basis>` leaking into the final text. Follow them without exception.

1. **Placeholder values must be rendered as prose, never as literals.** The templates use `<placeholder>` notation (e.g. `<claim>`, `<basis>`, `<reconstruction>`, `<what>`). These are **slots to be filled from the marker's input, as natural prose**. If you find yourself emitting the literal string `<basis>` or `<reconstruction>` in the output, stop — you have misread the template. Every `<...>` token must be replaced with the value from the input marker.

2. **No empty or sentinel-valued slots.** A slot cannot be rendered as empty, as a bare period, as `none`, as `n/a`, or as any other sentinel. If the input marker does not supply a value for a mandatory slot, do **not** fit it into the template — flag the marker in the stage report so upstream can be tightened, and render a fallback that does not produce broken prose. Each marker section below specifies its own fallback.

3. **Do not double up terminal punctuation.** If a placeholder value ends with `.`, `?`, `!`, or `…`, the template's following `.` separator is redundant. Use the existing terminator instead of appending another period. Never emit `..` inside a rendered bracket or paragraph. Never emit `..]_` at the close of a bracket. If a slot ends with a comma or semicolon, convert it to a period before the next sentence boundary.

4. **Sentinel hedges (e.g. `none`, `n/a`, `partial,`, `insufficient`, `—`) must never leak into reader-facing text.** Some input fields (notably `scholarly_reconstruction`) accept meta-notes that start with a hedge. Strip the hedge, capitalise the informative tail if any, and render the tail as a stand-alone sentence — or drop the sentence entirely if the tail is empty. See LACUNA Shape B below for the canonical worked examples.

When in doubt, **prefer under-rendering (omit a slot / drop a sentence) over broken-rendering (leaked sentinel / empty paren / double period)**. It is always safer to lose one sentence than to ship text that reads as a bug to the reader.

### `[INFERENCE: claim | basis: X | risk: Y]`
Render as an italicized parenthetical whose body is the **claim rendered as prose**, followed by a footnote carrying the basis and risk:
```
_(<claim rendered as prose>.footnote:[Inference: <basis>. Risk: <risk>.])_
```

All three slots — claim, basis, risk — are **mandatory** in the output. None may be empty, a lone period, or a copy of the template placeholder text.

**Worked example.**

Input (in `chapters/NN.adoc`):
```
[INFERENCE: The redistribution of Huwawa's auras to the natural world after his death suggests an aetiological function: the text explains why certain natural phenomena possess a numinous, fearsome quality. | basis: The list of recipients — field, river, lion, forest — corresponds to naturally fearsome aspects of the Mesopotamian landscape. | risk: The aetiological reading is plausible but not explicitly stated in the text.]
```

Output (in `chapters/NN.resolved.adoc`):
```
_(The redistribution of Huwawa's auras to the natural world after his death suggests an aetiological function: the text explains why certain natural phenomena possess a numinous, fearsome quality.footnote:[Inference: The list of recipients — field, river, lion, forest — corresponds to naturally fearsome aspects of the Mesopotamian landscape. Risk: The aetiological reading is plausible but not explicitly stated in the text.])_
```

Note that the claim text sits between `_(` and `.footnote:[`. A rendering that produces `_(.footnote:[...])_` (open paren, bare period, footnote) is a **bug** — it prints as `(. [n])` in the PDF and must never be emitted.

**Short form.** If the marker arrives with no `| basis:` / `| risk:` segments (i.e. `[INFERENCE: claim]` only), do **not** fit it into the template above. Render the claim as plain prose with no parenthetical and no footnote — the basis/risk slots would be empty and would produce the `(. [n])` bug. Flag the missing basis/risk in the stage report so upstream (stage 11) can be tightened.

### `[LACUNA: what | source: ref | scholarly_reconstruction: X]`
Render as a bracketed editorial note, italicized. The `<what>` field is rendered first, as a prose description of the gap. How `<X>` is rendered depends on what it describes.

**Shape A — `X` is a real proposed reading.** A concrete statement of what scholars think was in the gap. Use the full template frame:

```
_[At this point the tablet breaks. <what rendered as prose>. Scholars such as <ref> have proposed the narrative resumed with <X rendered as prose>.]_
```

**Shape B — `X` is a meta-note about the absence, inadequacy, or partial nature of reconstructions.** It begins with one of the following sentinel hedges (case-insensitive):

- `none`, `n/a`, `N/A`, `—` (em-dash)
- `none available`, `none sufficient`, `none suffices`
- `no <word>` — e.g. `no parallels`, `no witnesses`, `no reconstruction`
- `insufficient`, `limited`
- `partial,`, `partial;`, `partial ` (followed by a descriptor)
- `Partial,`, `Partial;`, `Partial ` (same, capitalised)

The sentinel may be followed by a dash (`—` or `--`), semicolon, or comma and an **informative tail** describing what (if anything) *is* known. Render:

```
_[At this point the tablet breaks. <what>. <Informative tail of X rendered as prose, capitalised>.]_
```

If the informative tail is empty (the value is just `none available` or `n/a` or similar with nothing else), drop the second sentence entirely:

```
_[At this point the tablet breaks. <what>.]_
```

**Hard rules for Shape B:**

1. The literal sentinel words — `none`, `n/a`, `partial,`, `insufficient`, etc. — must **never** appear in the rendered text. Strip them and capitalise what follows.
2. Do not emit `..` (double period). If `<what>` already ends with a period, do not append another before the second sentence.
3. Never output an empty `<what>` (a bracket that starts with `_[At this point the tablet breaks. .`). If the input `<what>` is empty or unclear, flag the marker in the stage report rather than render something broken.

**Worked examples.**

Example 1 — Shape A (real reconstruction):

Input:
```
[LACUNA: Lines 80–95 are lost | source: etcsl 1.2.3 | scholarly_reconstruction: the pursuit sequence continued with three further encounters, as preserved in the Ur III duplicate]
```
Output:
```
_[At this point the tablet breaks. Lines 80–95 are lost. Scholars such as etcsl 1.2.3 have proposed the narrative resumed with the pursuit sequence continuing through three further encounters, as preserved in the Ur III duplicate.]_
```

Example 2 — Shape B, tail after em-dash:

Input:
```
[LACUNA: Approximately nine lines (68–76) damaged in the middle of the impaired-humans sequence | source: etcsl 1.1.2 | scholarly_reconstruction: none — no parallel witnesses fill this gap]
```
Output:
```
_[At this point the tablet breaks. Approximately nine lines (68–76) damaged in the middle of the impaired-humans sequence. No parallel witnesses fill this gap.]_
```

Example 3 — Shape B, tail after semicolon:

Input:
```
[LACUNA: Several lines damaged | source: etcsl 1.3.3 | scholarly_reconstruction: none sufficient; Black et al. mark these sections as heavily fragmentary and offer only cautious partial translation]
```
Output:
```
_[At this point the tablet breaks. Several lines damaged. Black et al. mark these sections as heavily fragmentary and offer only cautious partial translation.]_
```

Example 4 — Shape B, "partial" hedge with tail after comma:

Input:
```
[LACUNA: Opening lines 1–15 damaged | source: etcsl 1.3.3 | scholarly_reconstruction: partial, some manuscripts preserve fragments of the opening]
```
Output:
```
_[At this point the tablet breaks. Opening lines 1–15 damaged. Some manuscripts preserve fragments of the opening.]_
```

Example 5 — Shape B, empty tail:

Input:
```
[LACUNA: Conclusion is fragmentary | source: etcsl 1.3.4 | scholarly_reconstruction: none available]
```
Output:
```
_[At this point the tablet breaks. Conclusion is fragmentary.]_
```

### `[RECONSTRUCTION: content | gap_source: X | fill_source: Y | confidence: Z]`
Render the content as normal prose, followed by a footnote flagging the reconstruction:
```
<content rendered as prose>.footnote:[This passage reconstructs the lacuna at <gap_source> from the parallel account in <fill_source>; confidence: <Z>.]
```

All four slots — content, gap_source, fill_source, confidence — are **mandatory**. If any is missing or empty, flag the marker and render only the content in prose (no footnote) rather than emit `<gap_source>` / `<fill_source>` / `<Z>` as literals.

Per rule 3, if `<content>` ends with a period, do not add another before `.footnote:[`.

**Worked example.**

Input:
```
[RECONSTRUCTION: Inanna asked her minister Ninshubur to go to Enlil for help, then to Nanna, then to Enki. | gap_source: ETCSL 1.4.1, lines 180–195 (Nippur) | fill_source: UM 29-16-37 fragment | confidence: high]
```

Output:
```
Inanna asked her minister Ninshubur to go to Enlil for help, then to Nanna, then to Enki.footnote:[This passage reconstructs the lacuna at ETCSL 1.4.1, lines 180–195 (Nippur) from the parallel account in UM 29-16-37 fragment; confidence: high.]
```

Note that `<content>` here ended with a period, so the template's leading `.` before `.footnote:[` is dropped — the existing period serves.

### `[VARIANT: primary=A | alt=B | chosen: A | reason: R]`
Only appears in single-prevalent cases (co-equal variants are already inline without markers). The marker's four fields map to the rendering as follows:

- `primary` — the prevalent version, rendered in the body as prose.
- `alt` — an object with a source name and the alternate phrase (typically `alt=<source>: "<phrase>"` or similar; read as `<B source>` and `<alt phrase>`).
- `chosen` — which of `primary`/`alt` is in the body. In this stage `chosen` is always `A` (`primary`); if the input says `chosen: B`, swap the semantics so `primary` becomes the body and `alt` the footnote.
- `reason` — why the chosen version is in the body.

Rendering:
```
<prevalent version text rendered as prose>.footnote:[An alternate tradition in <B source> gives: "<alt phrase>". The prevalent version is chosen here because <reason rendered as prose>.]
```

All four fields are **mandatory**. If `<reason>` is missing, flag the marker and render only the prevalent version in prose (no footnote). Never emit the literal `<B source>`, `<alt phrase>`, or `<reason>` in the output.

Per rule 3, if `<prevalent version text>` ends with a period, drop the template's leading `.` before `.footnote:[`. If `<alt phrase>` already ends with a terminator, do not add another before `"` closes. If `<reason>` ends with a period, do not add another before `]`.

**Worked example.**

Input:
```
[VARIANT: primary=Nippur | alt=Ur: "the bull drank water from the Tigris and Euphrates" | chosen: A | reason: Nippur manuscripts are older and more widely attested]
```

Output (assuming the prevalent version as rendered in the body reads "The bull drank water from the Tigris"):
```
The bull drank water from the Tigris.footnote:[An alternate tradition in the Ur manuscript gives: "the bull drank water from the Tigris and Euphrates". The prevalent version is chosen here because Nippur manuscripts are older and more widely attested.]
```

### `[SPECULATION: claim | basis: X | counterargument: Y]`
Only appears in the comparative chapter. Render as the claim in prose, followed by a footnote presenting both sides:
```
<claim rendered as prose>.footnote:[This parallel is speculative. Basis: <basis>. The main counterargument: <counterargument>.]
```

All three slots — claim, basis, counterargument — are **mandatory**. If `<basis>` or `<counterargument>` is missing, flag the marker and render the claim as plain prose without a footnote (do not emit empty `Basis:` / `counterargument:` slots).

Per rule 3:

- If `<claim>` ends with a period, drop the template's leading `.` before `.footnote:[`.
- If `<basis>` ends with a period, do not add another before ` The main counterargument:`.
- If `<counterargument>` ends with a period, do not add another before `]`.

**Worked example.**

Input:
```
[SPECULATION: The Gilgamesh-Enkidu friendship may reflect a wider ancient-Near-Eastern motif of the "hero and his wild double" also seen in Samson-and-Delilah and early Greek narratives. | basis: Structural parallel of a civilised hero paired with an untamed companion who civilises through contact with the hero. | counterargument: The parallels are structurally loose and could arise independently in any heroic tradition.]
```

Output:
```
The Gilgamesh-Enkidu friendship may reflect a wider ancient-Near-Eastern motif of the "hero and his wild double" also seen in Samson-and-Delilah and early Greek narratives.footnote:[This parallel is speculative. Basis: Structural parallel of a civilised hero paired with an untamed companion who civilises through contact with the hero. The main counterargument: The parallels are structurally loose and could arise independently in any heroic tradition.]
```

Note how the trailing periods of `<claim>`, `<basis>`, and `<counterargument>` serve double duty — they terminate their own content and stand in for the template's separator periods, so no `..` appears anywhere.

## Output

- Story chapters: `chapters/NN-<slug>.resolved.adoc`
- Intro chapter: `chapters/00-introduction.resolved.adoc`
- Comparative chapter: `comparative.resolved.adoc`

## Self-check

Every check below must return zero matches on every output file. If any match, stop and fix before handoff — the cost of shipping a broken rendering into the next stage is much higher than the cost of re-running this one.

**Raw markers.** Zero matches for `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:`.

**Placeholder-literal leaks** (rule 1). These indicate the renderer emitted the template's `<…>` token instead of filling it from the input. Zero matches for any of:

`<claim>`, `<basis>`, `<risk>`, `<reconstruction>`, `<what>`, `<ref>`, `<content>`, `<gap_source>`, `<fill_source>`, `<Z>`, `<confidence>`, `<prevalent version text>`, `<alt phrase>`, `<B source>`, `<reason>`, `<counterargument>`

**Empty-slot artefacts** (rule 2). These indicate a mandatory slot was rendered as empty or as a bare period.

- `_(\.footnote:` — INFERENCE rendered with an empty claim; prints as `(. [n])` in the PDF.
- `Inference: *\.` — empty INFERENCE basis.
- `Risk: *\.` — empty INFERENCE risk.
- `Basis: *\.` — empty SPECULATION basis.
- `counterargument: *\.` — empty SPECULATION counterargument.
- `_\[At this point the tablet breaks\. *\.` — LACUNA rendered with an empty `<what>`.
- `An alternate tradition in  gives:` (note the double space) — VARIANT with an empty `<B source>`.
- `reconstructs the lacuna at  from the parallel account in` — RECONSTRUCTION with an empty `<gap_source>`.

**Leaked sentinel hedges** (rule 4). Zero matches inside any rendered italic bracket `_[...]_` or `_(...)_` for:

- `none —`, `none --`, `none-`, `none—`
- `none available`, `none sufficient`, `none suffices`, `none yet`
- `n/a —`, `n/a -`, `N/A —`
- `partial,` or `partial;` at the start of a clause (after `. `)
- `Partial,` or `Partial;` at the start of a clause
- `insufficient;` at the start of a clause
- `no reconstruction —`, `no witnesses —`, `no parallels —`

**Double-period artefacts** (rule 3). Zero matches for:

- `..footnote:` — placeholder value ended in `.` and the template's separator `.` was appended.
- `.. Risk:` — INFERENCE basis ended in `.` and the template's separator was appended.
- `.. The main counterargument:` — SPECULATION basis ended in `.`.
- `.. Scholars such as` — LACUNA `<what>` ended in `.` before the Shape A suffix.
- `..]_` — any italic bracket closing with two periods.
- `.. —` — any double period followed by an em-dash inside rendered prose.
- `..])_` — INFERENCE or SPECULATION risk/counterargument ended in `.`, doubling at the bracket close.

**Per-marker round-trip count.** For every `[INFERENCE: ...]`, `[LACUNA: ...]`, `[RECONSTRUCTION: ...]`, `[VARIANT: ...]`, `[SPECULATION: ...]` in the input `.adoc`, confirm exactly one rendered equivalent appears in the corresponding `.resolved.adoc`. Mismatches — input markers with no output, or outputs with no input — are findings.

For every INFERENCE input whose claim is non-empty, confirm the `.resolved.adoc` contains non-trivial prose between `_(` and `.footnote:[`. If the input was a short-form `[INFERENCE: claim]` (no `| basis:` / `| risk:`), confirm the output renders the claim as plain prose instead (no paren, no footnote).

**Prose boundary.** No prose outside of marker-replaced sections has changed. A line-by-line diff against the input should show changes only on lines that held markers.

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
To `line-edit`.

---

# FILE 16 of 21: skills/14-comparative-chapter.md

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
- All story chapters after narrative-fidelity has passed (`chapters/NN-<slug>.adoc`) — the factual content is locked, though markers have not yet been resolved and prose has not yet been polished. The comparative chapter needs the factual content, not the final formatting.
- `chapters/00-introduction.adoc` (the intro chapter, post-factcheck)
- All briefs (for `comparative_hooks`) and all `// COMPARATIVE-HOOK:` comments left in chapter drafts
- `scope.md`, `sources.yaml`
- Optional comparative-mythology whitelist (Dumézil, Puhvel, Watkins, West, Witzel, Lincoln — add to `sources.yaml` before this stage)

## Rules
- Every comparison cites both the in-scope source and the out-of-scope source.
- Structural parallels (tripartite function, sky-father motif, etc.) cite scholarly methodology, not invented frameworks.
- Speculation is allowed but must be marked: `[SPECULATION: claim | basis: X | counterargument: Y]`.
- Do not retell out-of-scope myths at length — one-paragraph summaries, then the comparison.
- `// EVIDENCE: source_id=X ; loc=Y` tokens go on their own line (column 0), never appended after paragraph text. AsciiDoc only treats `//` as a comment at line start — a trailing marker renders as literal text in the final PDF/EPUB. Same rule as `chapter-claims`.

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
To `prose-factcheck` in a fresh conversation (a different AI model is preferred but not required). After factcheck, human review, and `post-human-normalize`, to `marker-resolve` along with all other chapters.

---

# FILE 17 of 21: skills/14b-grammar-check.md

---
name: grammar-check
description: Catches grammar errors, awkward sentence constructions, and readability issues before the line-edit stage. Fixes only mechanical problems — does not change style, tone, or content. Runs after marker-resolve, before line-edit.
---

# grammar-check

## For the human

This step catches mechanical writing problems that slip through the drafting process: subject-verb disagreement, dangling modifiers, run-on sentences, ambiguous pronoun references, missing articles, and sentences that are grammatically correct but hard to parse on first reading.

It does not change the book's style or tone — that is the line-edit stage's job. It does not change facts — those are locked. It fixes only the kind of errors a copy editor catches: grammar, syntax, punctuation, and sentence clarity.

The AI tends to produce sentences that are technically correct but overloaded — too many subordinate clauses, too many parenthetical asides, or too many items in a single sentence. This step simplifies those without changing meaning.

## When to run

After `marker-resolve` (stage 13), before `line-edit` (stage 15). The input is the resolved text — all markers have been converted to final prose, so the grammar checker sees what the reader will see.

## Hard rules

1. **No factual changes.** If a grammar fix would change the meaning of a sentence, flag it for human review instead of fixing it.
2. **No footnote changes.** Do not modify, add, or remove footnotes or EVIDENCE tokens.
3. **No style changes.** Do not change the Asimov register. Do not add formality or informality. Do not rewrite sentences that are clear but plain.
4. **No content changes to resolved marker passages.** These were reviewed and locked.
5. **Preserve AsciiDoc structure** (headings, section breaks, include directives).

## What to fix

### Grammar errors
- Subject-verb agreement
- Tense consistency within paragraphs
- Dangling or misplaced modifiers
- Incorrect pronoun reference (ambiguous "it", "they", "this")
- Missing or incorrect articles (a/an/the)
- Comma splices and run-on sentences
- Sentence fragments (unless clearly intentional for effect)

### Readability issues
- Sentences over 50 words: split or restructure unless the length is essential for meaning
- Nested parenthetical asides: flatten (move to a separate sentence or footnote)
- Three or more subordinate clauses in a single sentence: simplify
- Ambiguous sentence structure where the reader must re-read to parse correctly
- Lists embedded in prose that would be clearer as an actual list or as separate sentences

### Punctuation
- Correct em-dash, en-dash, and hyphen usage
- Consistent serial comma (use it)
- Quotation marks and apostrophes in non-English terms

## What NOT to fix

- Word choice (that is line-edit's job)
- Sentence rhythm and flow (line-edit)
- Paragraph transitions (line-edit)
- Nominalizations and zombie nouns (line-edit)
- The academic tone of source overview sections (this is a deliberate register choice)

## Output

For each chapter:
- `chapters/NN-<slug>.grammar-checked.adoc` — the corrected text
- `chapters/NN-<slug>.grammar-diff.md` — a list of every change, showing original and corrected sentence

The diff file allows the human to skim and approve in bulk.

## Self-check

1. No factual content has changed — compare factual claims between original and corrected.
2. Footnote count and content unchanged.
3. All AsciiDoc structure intact.
4. Every change is logged in the diff file — no silent changes.

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
To `line-edit`, which handles style polish after grammar is clean.

---

# FILE 18 of 21: skills/15-line-edit.md

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
- Marker-resolved story chapters (`chapters/NN-<slug>.resolved.adoc`)
- Marker-resolved intro chapter (`chapters/00-introduction.resolved.adoc`)
- Marker-resolved comparative chapter (`comparative.resolved.adoc`)
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

For each chapter:
- `chapters/NN-<slug>.edited.adoc` plus `chapters/NN-<slug>.diff.md`
- `chapters/00-introduction.edited.adoc` plus `chapters/00-introduction.diff.md`
- `comparative.edited.adoc` plus `comparative.diff.md`

Each diff file shows original sentence vs edited sentence for every non-trivial change. The human skims the diffs to approve in bulk.

## Self-check
- Extract all factual claims from original and edited versions; compare. Any difference is a bug.
- Footnote count and content unchanged.
- Resolved marker passages unchanged.

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
To `character-appendix` and `format-finalize`.

---

# FILE 19 of 21: skills/16-character-appendix.md

---
name: character-appendix
description: Produces a reference appendix listing every named character in the book — who they are, where they appear, what they look like (only if the sources actually say so), and how important they are. Runs after all chapters are finished. Goes through fact-checking before the book is assembled.
---

# character-appendix

## For the human

This appendix is the reader's reference companion. Halfway through a chapter on Gilgamesh, the reader encounters Siduri and wants to know: who is she, where else does she appear, what does she look like? This appendix answers that — and only what the sources actually say.

The hardest discipline here is restraint on physical descriptions. AI models asked to describe a mythological character will readily produce vivid physical portraits drawn from cultural stereotypes, later artistic traditions, or pure invention. For most ancient characters, the sources say very little about physical appearance — sometimes nothing at all. The correct entry is an honest "No physical description survives in the in-scope sources," not a fabricated portrait. Accuracy is more important than completeness: it is better to leave a field empty than to fill it with something the sources don't support.

This step runs after all chapters are finalized because it needs the final text to build accurate cross-references ("Siduri appears in Chapter 5, where she..."). It goes through fact-checking in a fresh conversation (ideally a different AI model, but the same model in a fresh conversation is acceptable if a different one is impractical) before the book is assembled.

**Note on markers and line-edit:** The character appendix is a reference section, not narrative prose. It does not use `[INFERENCE:]`, `[LACUNA:]`, or other markers — all claims must be directly sourced or explicitly noted as absent. It does not go through `marker-resolve` or `line-edit`. The Asimov register and citation discipline are enforced at writing time; the factcheck catches any problems.

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
To `prose-factcheck` in a fresh conversation (a different AI model is preferred but not required) for a factcheck pass focused on:
- Fabricated or unsourced physical descriptions (the primary risk).
- Cross-reference accuracy.
- Claims about mythological relevance.

After factcheck passes, to `format-finalize`.

---

# FILE 20 of 21: skills/17-format-finalize.md

---
name: format-finalize
description: Final mechanical assembly. Compiles the bibliography, assembles all chapters into the master book file, and runs a test build to PDF and EPUB to catch formatting errors. No prose is changed at this stage — all writing is finished.
---

# format-finalize

## For the human

This is a purely mechanical step — no writing, no editing, no judgment calls. All prose is final. This step:

- **Builds the bibliography.** Scans every footnote across all chapters and produces a single bibliography file listing every source cited in the book. If any footnote cites a source that isn't on the approved list (`sources.yaml`), this is flagged as a problem.
- **Assembles the book.** Combines the introduction, all story chapters, the comparative chapter, and the character appendix into one master file (`<book-slug>.adoc`) in the correct order.
- **Renders the final artifacts.** Builds the final PDF and EPUB into `output/` and writes any warnings from the build to `reports/validation-report.md`.

No prose is changed. If this step finds a problem that requires changing text (e.g., a broken cross-reference), it reports the problem and stops — it does not attempt to fix it.

## Book slug

The outputs of this stage are named after the book, not `book.*`. Determine the slug once, at the start of the stage, and reuse it consistently.

- If `scope.md` defines a `slug:` field, use it verbatim.
- Otherwise, derive the slug from the book title (the first `= <Book Title>` line of what will become the master adoc). Take the portion before any `:`, lowercase it, strip punctuation, replace runs of non-alphanumeric characters with a single `_`, and trim leading/trailing `_`.
  - Example: `= The Myths of Sumer: Stories from the First Scribes` → `the_myths_of_sumer`.
- The slug must match `^[a-z0-9][a-z0-9_]*$`. If the derived slug is awkward or collides with pipeline filenames (`book`, `comparative`, `character-appendix`, `frontmatter`, `note-on-making`), stop and ask the human to set `slug:` in `scope.md` explicitly.

Throughout this document, `<slug>` refers to the book slug.

## Inputs
- `chapters/00-introduction.edited.adoc` (intro chapter)
- All `chapters/NN-<chapter-slug>.edited.adoc` (story chapters)
- `comparative.edited.adoc` (comparative chapter)
- `character-appendix.adoc` (fact-checked — this is a reference appendix and does not go through marker-resolve or line-edit)
- `sources.yaml`
- `scope.md` (may carry an explicit `slug:` field — see "Book slug" above)
- `cover.jpg` or `cover.png` — the cover image, provided by the user. Used by Asciidoctor-PDF for the front cover and by Asciidoctor-EPUB3 for the EPUB cover.
- `front-matter.adoc` and `back-matter.adoc` (dedication, preface, index, etc. — optional; if absent, omit the corresponding `include::` directives from the master adoc)

## Agent instructions

### 1. Bibliography extraction
Scan all files for `// EVIDENCE: source_id=<id> ; loc=<loc>` tokens. Collect all unique `source_id` values. For each, look up the entry in `sources.yaml` registry and produce a BibTeX entry using the `full_citation`, `author`, `title`, `year`, and `identifier_value` fields. Use the `id` from `sources.yaml` as the citation key.

Cross-check: any `source_id` in an evidence token that does not resolve to a `sources.yaml` registry entry is a HIGH finding — stop and report. Any registry entry never referenced by any evidence token is noted (unused source — not an error, but worth flagging).

### 2. Marker strip (critical — do this AFTER bibliography extraction, BEFORE assembly)

The `// EVIDENCE:` and `// COMPARATIVE-HOOK:` markers are production metadata for the pipeline, not for readers. AsciiDoc only treats `//` as a comment when it starts the line — any marker appended to a paragraph line (e.g., after `footnote:[...]`) renders as literal text in the final PDF/EPUB. This has happened before; do not skip this step.

For each of `chapters/00-introduction.edited.adoc`, every `chapters/NN-<slug>.edited.adoc`, and `comparative.edited.adoc`:

- Strip everything matching the regex `\s*//\s*(EVIDENCE|COMPARATIVE-HOOK):.*$` from every line.
- If the strip empties a line (whole-line marker), delete the line.
- If the strip leaves content (mid-line marker), keep the preceding content.

Upstream `.resolved.adoc` and `.grammar-checked.adoc` files preserve the markers as an audit trail — the strip is safe.

After stripping, grep each target file for `EVIDENCE` and `COMPARATIVE-HOOK`. Zero matches expected. If any remain, stop and report.

### 3. Master assembly
Produce `<slug>.adoc` at the book root. Keep it at the book root (not under `output/`) so the relative `include::chapters/...`, `:bibtex-file:`, and cover-image paths resolve without `../` rewrites.

```asciidoc
= <Book Title>
<Author>
:doctype: book
:toc: left
:sectnums:
:front-cover-image: image:cover.jpg[]
:bibtex-file: bibliography.bib
:bibtex-style: chicago-author-date

// include::front-matter.adoc[]   ← include only if file exists

include::chapters/00-introduction.edited.adoc[]

include::chapters/01-<chapter-slug>.edited.adoc[]
include::chapters/02-<chapter-slug>.edited.adoc[]
// ... in toc.yaml order ...

include::comparative.edited.adoc[]

include::character-appendix.adoc[]

// include::back-matter.adoc[]    ← include only if file exists
```

### 4. Render
Render via the container helper, invoked from the repo root:

```
./container/render_book.sh <book-dir> <slug>
```

The helper creates `<book-dir>/output/` and `<book-dir>/reports/` if they do not exist, runs both asciidoctor commands inside the myth-claude container (where `asciidoctor-bibtex` is installed), captures stdout/stderr from both runs into `<book-dir>/reports/validation-report.md` (with a stage/slug/timestamp header), then unzips the EPUB and greps the `.xhtml` files for `EVIDENCE`, `COMPARATIVE-HOOK`, the empty-paren `(. ` artefact, and the `_(.footnote` stage-13 artefact. It exits non-zero on any WARN/ERROR from asciidoctor or any anti-pattern hit — treat a non-zero exit as a finding and stop.

The underlying commands (for local debugging without the container, assuming `asciidoctor-bibtex` is available on the host) are:

```
asciidoctor-pdf   -r asciidoctor-bibtex --verbose --failure-level=WARN -o output/<slug>.pdf  <slug>.adoc
asciidoctor-epub3 -r asciidoctor-bibtex --verbose --failure-level=WARN -o output/<slug>.epub <slug>.adoc
```

Both commands must be run from `<book-dir>` (not from the repo root) — `asciidoctor-bibtex` resolves the `:bibtex-file:` attribute relative to the current working directory, not the source document's directory.

### 5. Output
Final deliverables (the reader-facing artifacts) are gathered under `output/`. Build logs are written to `reports/`. Everything else stays at the book root.

- `<slug>.adoc` — master, at book root.
- `bibliography.bib` — at book root (referenced by the master adoc).
- `output/<slug>.pdf` — rendered PDF.
- `output/<slug>.epub` — rendered EPUB.
- `reports/validation-report.md` — asciidoctor build log, any findings.

## Self-check

The marker-resolve stage (13) is the upstream producer of the rendered brackets and parentheticals. The checks below are a safety net for bugs that stage missed. Each must return zero matches on every `.edited.adoc` file at the book root. If any match, stop and re-run stage 13 — do not attempt to patch the output in this stage.

- No `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:` markers remain anywhere. (Grep all `.edited.adoc` files, `comparative.edited.adoc`, and `character-appendix.adoc`.)
- No `// EVIDENCE:` or `// COMPARATIVE-HOOK:` remain in the `.edited.adoc` files after step 2. Grep the rendered EPUB's `.xhtml` contents for both strings — must be zero.
- No placeholder-literal leaks from stage 13: zero matches for `<claim>`, `<basis>`, `<risk>`, `<reconstruction>`, `<what>`, `<ref>`, `<content>`, `<gap_source>`, `<fill_source>`, `<Z>`, `<confidence>`, `<prevalent version text>`, `<alt phrase>`, `<B source>`, `<reason>`, `<counterargument>`. These indicate the renderer copied the template verbatim instead of filling a slot.
- No empty-slot artefacts. Grep for `_(\.footnote:` (empty INFERENCE claim — prints as `(. [n])` in the PDF), `Inference: *\.`, `Risk: *\.`, `Basis: *\.`, `counterargument: *\.`, `_\[At this point the tablet breaks\. *\.` (empty LACUNA `<what>`).
- No leaked sentinels (case-insensitive) anywhere inside italic brackets `_[…]_` or `_(…)_`: `none —`, `none --`, `none-`, `none—`, `none available`, `none sufficient`, `n/a —`, `n/a -`, `Partial,` or `Partial;` at the start of a clause, `partial,` or `partial;` at the start of a clause, `insufficient;` at the start of a clause.
- No double-period artefacts. Grep for `..]_`, `.. —`, `..footnote:`, `.. Risk:`, `.. The main counterargument:`, `.. Scholars such as`, `..])_`. These indicate a placeholder value ended with `.` and the template's separator `.` was appended.
- Every footnote citation resolves to a bibliography entry.
- Every bibliography entry is on the whitelist.
- Every `<<chapter-anchor>>` cross-reference in `character-appendix.adoc` resolves to an actual anchor in the chapter files.
- Cover image file exists and is referenced correctly in `:front-cover-image:`.
- `front-matter.adoc` and `back-matter.adoc`: if referenced in `<slug>.adoc`, confirm the files exist. If absent, confirm the include directives are removed.
- `output/<slug>.pdf` and `output/<slug>.epub` exist and are non-empty.
- `reports/validation-report.md` exists. Asciidoctor runs exit clean (no WARN/ERROR recorded).
- No legacy `book.adoc`, `book.pdf`, `book.epub` at the book root left over from prior runs — either remove or rename them before starting.

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
This is the final stage. The book is complete.

---

# FILE 21 of 21: skills/18-translate-spanish.md

---
name: translate-spanish
description: Produces a parallel Spanish edition of the finished book. Three-pass reflection workflow (translate → critique → revise) per chapter. Runs after format-finalize. AsciiDoc structure, footnotes, anchors, xrefs, EVIDENCE tokens, and include paths are preserved byte-for-byte; only visible prose is translated.
---

# translate-spanish

## For the human

This is the final stage. The English book is done — every chapter is fact-checked, line-edited, formatted, and built into `output/<slug>.pdf` / `output/<slug>.epub`. This step produces a parallel Spanish edition: `<slug>.es.adoc` → `output/<slug>.es.pdf` / `output/<slug>.es.epub`. The slug is the one fixed in `format-finalize` (stage 17); do not re-derive it.

Translation of a non-fiction book by LLM has a few characteristic failure modes that this skill is designed around:

- **AsciiDoc collateral damage.** An LLM will "helpfully" translate an anchor like `[[dilmun-section]]` to `[[seccion-dilmun]]`, silently breaking every cross-reference elsewhere. The hard rules below forbid this, and the self-check does a regex diff to catch it.
- **Terminology drift across chapters.** The same deity or technical term can end up rendered three different ways across 36 chapters. The fix is to lock a Spanish glossary (`glossary.es.yaml`) before any prose is translated, in the same spirit as `glossary-lock`.
- **Academic Spanish creep.** Spanish popular-science prose is prone to nominalization pile-ups, passive "se ha observado que…" constructions, and latinate vocabulary that turn an Asimov-voice English original into a stiff treatise. The register section below keeps the divulgación tone.
- **False friends.** *Eventually*, *actually*, *realize*, *library*, *assist*, *sensible*, *sympathetic* — the usual suspects. Checklist below.
- **Chunk-too-small translation.** Translating paragraph-by-paragraph destroys pronoun chains ("the god" / "this composition" / "she") that span paragraphs. Translate chapter-by-chapter.

The method follows Andrew Ng's `translation-agent` reflection workflow: draft, self-critique, apply critique. Per chapter, not per paragraph.

## When to run

After `format-finalize` (stage 17). The inputs are the finished, fact-checked, line-edited chapters plus the assembled `<slug>.adoc` and `bibliography.bib`. This is the final stage.

## Target dialect and register

**Dialect**: Peninsular Spanish (uses *vosotros*, *ordenador*, *vale*). Register-neutral enough for Latin American readers in an academic/popular-science context, but do not mix dialects within the book.

**Register**: divulgación científica, Asimov-style. Plain, clear, lightly conversational. Active voice by default. Concrete verbs. Avoid:

- Nominalization chains ("la realización de la verificación de" → "verificar").
- Agentless passives where an active form is natural ("se ha observado" → "observamos" or reword).
- Latinate register pile-ups ("con el objeto de proceder a" → "para").
- Formal throat-clearing ("Cabe destacar que" — cut unless it carries meaning).

Punctuation conventions:

- Em-dash for asides: `—así—` (no inner spaces, outer spaces). Same character as the English em-dash.
- Quotes: prefer RAE guillemets «...» for quoted speech and titles; accept "curly quotes" only if already used consistently in the source and their swap would create ambiguity.
- Spanish opens questions and exclamations with `¿` and `¡`.
- Italicize transliterated foreign terms (*me*, *edubba*, *abzu*, *en*, *ensi*, *lugal*).

If the user specifies a different dialect (e.g., español neutro internacional) before the stage runs, switch and stay consistent throughout.

## Hard rules

1. **No factual changes.** If a rendering would alter a factual claim, choose a different rendering. Never edit content.
2. **No AsciiDoc structure changes.** The translated file must have the same anchors, xref targets, include paths, footnote structure, image paths, attribute names, and block delimiters as the source.
3. **Never translate machine-readable identifiers.** This includes:
   - `[[anchor-id]]`, `[#section-id]` — the ID stays in English.
   - `<<xref-target>>` — the target stays in English; if there is visible text `<<target, text>>`, translate only the text after the comma.
   - `xref:other.adoc#id[text]` — path and ID unchanged; translate bracketed text only.
   - `include::path/file.adoc[]` — unchanged. Paths stay English (see §Output for how Spanish chapter files are named and included).
   - `// EVIDENCE: source_id=... ; loc=...` — comment lines unchanged. These are pipeline machinery.
   - `footnote:name[...]` — the `name` ref ID unchanged; translate the content inside `[...]`.
   - `image::path[alt]` — path unchanged; translate `alt` text.
   - Attribute entries like `:doctype:`, `:toc:`, `:sectnums:` — names unchanged; values translated only where the value is user-facing text (e.g., `:author:`).
   - BibTeX citation keys in `bibliography.bib` — unchanged.
4. **No footnote content changes beyond translation.** Do not add, remove, merge, or renumber footnotes.
5. **No changes inside resolved marker passages' factual content.** These were reviewed and locked upstream. Translate the prose, do not reinterpret.
6. **Bibliography titles stay in the original language.** Chicago-author-date convention: do not translate the titles of cited works. Only translate publisher-location strings if absolutely necessary for clarity (usually leave untouched).

## Inputs

- `glossary.yaml` (English glossary — basis for the Spanish glossary)
- `scope.md`, `sources.yaml`
- All `chapters/NN-<slug>.edited.adoc` (story chapters)
- `chapters/00-introduction.edited.adoc`
- `comparative.edited.adoc`
- `character-appendix.adoc`
- `<slug>.adoc` (master assembly — gives include order)
- `bibliography.bib`

## Method

### Pass 0 — Spanish glossary (interactive, once)

Before any prose is translated, produce `glossary.es.yaml`.

For every entry in `glossary.yaml`, propose a Spanish rendering plus alternatives, applying the conventions from Spanish academic Sumerology:

| Term type | Spanish convention |
|---|---|
| Sumerian deity names (Enki, Enlil, Inanna, Utu, Nanna, Ninhursaja, Ninlil, Ninmah) | Unchanged. Never substitute Akkadian equivalents (Ea, Anu) unless the source explicitly does. |
| Sumerian place names that have a standard Akkadian/modern form (Nibru → Nippur, Unug → Uruk, Eridug → Eridu, Urim → Ur, Zimbir → Sippar) | Prefer the Akkadian/standard form for reader recognition; gloss the Sumerian form in italics on first mention. |
| Sumerian place names without a widespread Spanish form (Keš, Kuara, Šuruppak) | Transliterate with standard diacritics (š, ĝ). |
| Technical terms (*me*, *edubba*, *abzu*, *giguna*, *kur*) | Keep in italics, untranslated. Gloss on first mention. Plural forms: *los me*, *los edubba* (invariable). |
| Titles (*en*, *ensi*, *lugal*, *abgal*, *lukur*) | Keep in italics, untranslated. Gloss on first mention. |
| Scholar names (Kramer, Jacobsen, Black, Bottéro) | Unchanged. |
| Scholarly-edition titles in footnotes | Unchanged (original language). |

Present the proposed `glossary.es.yaml` to the user. For each entry the user accepts, picks an alternate, or supplies their own. No silent choices.

Format:

```yaml
terms:
  - native: <transliteration>
    english_chosen: <from glossary.yaml>
    spanish_renderings_considered:
      - { form: <rendering>, rationale: <source/precedent> }
    spanish_chosen: <final locked rendering>
    first_mention_gloss_es: <short functional gloss in Spanish, Asimov-style>
    never_use_es: [<Spanish forms that must never appear — e.g., Akkadian substitutions>]
```

### Pass 1 — Draft translation (per chapter)

For each chapter file, produce `chapters/NN-<slug>.es.draft.adoc` (intermediate — not a final output; may be discarded after Pass 3).

Instructions to follow during Pass 1:

- Translate the entire chapter in a single pass, keeping the full chapter in context. Do not split into paragraphs.
- Apply the Spanish glossary: every term with a `spanish_chosen` entry must use that rendering.
- Preserve every `[[anchor]]`, `<<xref>>`, `include::`, `footnote:[...]`, `// EVIDENCE:` token, `image::`, and attribute line byte-for-byte in its position.
- Italicize transliterated foreign terms using AsciiDoc `_italics_` or `+++<em>...</em>+++` per the source's convention.
- Handle direct quotations of primary source translations: if the English quotes a scholar's translation (e.g., Black/Cunningham/Robson/Zólyomi), translate the quotation into Spanish and add a translator's note in a footnote of the form `footnote:[Traducción propia del inglés de <author> <year>.]` — unless a published Spanish translation of that exact passage exists in `glossary.es.yaml`'s `published_translations:` section (see Pass 0 if applicable).
- Do not translate BibTeX keys in footnote citations; `cite:[kramer1961]` stays `cite:[kramer1961]`.

### Pass 2 — Reflection (per chapter)

On the Pass 1 draft, produce a structured self-critique. Do not rewrite yet. Cover, in order:

1. **Accuracy.** Sentence-by-sentence, are there any factual shifts, omissions, or additions? List each as `line N: <issue>`.
2. **AsciiDoc integrity.** List every anchor, xref, include, footnote ref ID, EVIDENCE token, and image path in the draft. Compare against the source. Any divergence is a finding.
3. **Terminology.** Every glossary term used — is the Spanish rendering the locked one? Any drift? Any English term leaked (untranslated noun phrase still in English)?
4. **Register.** Flag nominalization chains, agentless passives where active is natural, latinate pile-ups, throat-clearing, and calques of English idiom.
5. **False friends.** Check at minimum: *eventually*, *actually*, *eventually*, *actually*, *actually*, *realize*, *library*, *assist*, *sensible*, *sympathetic*, *fabric*, *discuss*, *pretend*, *argument*, *apology*, *attend*, *character* (people vs letters), *support* (endorse vs stand under), *exit*, *fact* (≠ *facto*). Search and verify each occurrence.
6. **Punctuation.** ¿/¡ on questions/exclamations. Em-dashes rendered correctly. Italics preserved on transliterated terms.
7. **Anaphora and cohesion.** Pronoun chains, "the god", "this composition" — do they resolve correctly across paragraphs in the Spanish version?

### Pass 3 — Apply reflections (per chapter)

Rewrite the chapter applying every accepted reflection. Produce the final output `chapters/NN-<slug>.es.adoc` and a `chapters/NN-<slug>.es-diff.md` showing original English sentence vs Spanish sentence for a representative sample plus every non-trivial rendering decision (glossary terms on first mention, ambiguous passages, translator-note footnotes). The human skims the diff to approve in bulk.

Repeat Pass 1 → Pass 2 → Pass 3 for each chapter. Also for: `chapters/00-introduction.edited.adoc` → `chapters/00-introduction.es.adoc`, `comparative.edited.adoc` → `comparative.es.adoc`, `character-appendix.adoc` → `character-appendix.es.adoc`.

### Pass 4 — Assembly

Produce `<slug>.es.adoc` at the book root, a mirror of `<slug>.adoc` with:

- Translated title, author, subtitle.
- Spanish document attributes where user-facing (`:doctype: book` stays; `:toc-title: Índice` added; `:appendix-caption: Apéndice`; `:figure-caption: Figura`; `:table-caption: Tabla`; `:note-caption: Nota`; `:tip-caption: Consejo`; `:important-caption: Importante`; `:caution-caption: Precaución`; `:warning-caption: Advertencia`; `:lang: es`; `:locale: es_ES` — or `es` for neutro).
- `include::` directives pointing at the `.es.adoc` files, in the same order as `<slug>.adoc`.
- `:bibtex-file: bibliography.bib` unchanged (same bib file, same keys).

Produce `bibliography.es.bib` (at book root) only if translator-note footnotes add any new citations; otherwise reuse `bibliography.bib` as-is.

### Pass 5 — Render

Render the Spanish variant via the container helper (same wrapper used by stage 17, with `--es`):

```
./container/render_book.sh <book-dir> <slug> --es
```

The helper writes `<book-dir>/output/<slug>.es.pdf`, `<book-dir>/output/<slug>.es.epub`, and `<book-dir>/reports/validation-report.es.md`. It runs the same anti-pattern scan on the produced EPUB as stage 17 (EVIDENCE/COMPARATIVE-HOOK leftovers, `(. ` empty-paren artefact, `_(.footnote` artefact) and exits non-zero on any WARN/ERROR or hit — treat a non-zero exit as a finding and stop.

## Output

Per chapter:
- `chapters/NN-<chapter-slug>.es.adoc`
- `chapters/NN-<chapter-slug>.es-diff.md`

At book root:
- `chapters/00-introduction.es.adoc` + `.es-diff.md`
- `comparative.es.adoc` + `comparative.es-diff.md`
- `character-appendix.es.adoc` + `character-appendix.es-diff.md`
- `glossary.es.yaml`
- `<slug>.es.adoc` (master)
- `bibliography.es.bib` (only if new citations were introduced)

Under `output/` (final deliverables):
- `output/<slug>.es.pdf`
- `output/<slug>.es.epub`

Under `reports/` (build logs):
- `reports/validation-report.es.md`

## Self-check

1. **ID/anchor/path diff.** For every source chapter and its translation, extract the set of `[[anchors]]`, `<<xref targets>>`, `include::` paths, `footnote:name[...]` ref IDs, `// EVIDENCE:` tokens, `image::` paths, and `cite:[key]` keys. The two sets must be identical. Any divergence is a HIGH finding.
2. **Footnote count match.** Per chapter, number of footnote definitions and number of footnote references must match between source and translation.
3. **No English paragraphs leaked.** Sample every chapter; no paragraph should remain in English (except unchanged machine-readable lines and bibliography titles).
4. **Glossary compliance.** Every term in `glossary.es.yaml` — its `spanish_chosen` rendering appears in the translated corpus; its `never_use_es` forms do not.
5. **Asciidoctor dry-runs exit clean** (no WARN/ERROR).
6. **No `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:` markers** have been reintroduced (marker-resolve already removed them from the English source; they must not come back).
7. **Bibliography keys unchanged.** `cite:[...]` keys in Spanish files match those in English files.

## Failure modes and recovery

- **Context overflow on a long chapter.** Split the chapter at a natural section break (`==` heading) for Pass 1 only; stitch before Pass 2. Never split mid-paragraph.
- **Glossary term missing from `glossary.es.yaml`.** If Pass 1 encounters a recurring term not in the Spanish glossary, stop and flag. The user adds the entry using the Pass 0 procedure. Do not silently invent a rendering.
- **AsciiDoc structure diff fails.** Do not "fix" by reverting — report the specific anchor/xref/path that diverged and which chapter. The user decides.
- **Register regression** (output reads as academic Spanish). Re-run Pass 2 with the register checklist as the primary focus, and apply in Pass 3.

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

This is the final stage. The Spanish edition is complete.

