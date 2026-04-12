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
