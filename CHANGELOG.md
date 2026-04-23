# Changelog

## v2.2

**New skills**
- `grammar-check` (14b) — a mechanical grammar and readability pass that runs between `marker-resolve` and `line-edit`. Fixes grammar errors, awkward sentences, and readability issues without touching footnotes, EVIDENCE tokens, or marker-resolved brackets. Produces `*.grammar-checked.adoc` + `*.grammar-diff.md` for review.
- `translate-spanish` (18) — produces a parallel Spanish edition of the finished book using a three-pass reflection workflow (translate → critique → revise) per chapter. AsciiDoc structure, anchors, xrefs, EVIDENCE tokens, include paths, and BibTeX keys are preserved byte-for-byte; only visible prose is translated. Runs after `format-finalize`.

**Marker-resolve hardening (stage 13)**
- New **Universal rendering rules** preamble establishing four principles that apply to every marker type:
  1. Placeholder values must be rendered as prose, never leaked as literal `<placeholder>` tokens.
  2. No empty or sentinel-valued slots — flag and fall back rather than ship broken prose.
  3. Do not double up terminal punctuation (`..`, `..]_`, `.. Risk:`).
  4. Sentinel hedges (`none`, `n/a`, `partial,`, `insufficient`, `—`) must never leak into reader-facing text.
- `[INFERENCE:]` rule rewritten with explicit `<claim>` placeholder, a worked input→output example, and a **short-form fallback**: markers that arrive without `| basis: | risk:` are rendered as plain prose, not shoehorned into the footnote template with empty slots. Fixes a class of bug that shipped `(. [n])` into the final PDF.
- `[LACUNA:]` rule rewritten with two explicit shapes: **Shape A** (real reconstruction — use the "Scholars such as …" frame) and **Shape B** (sentinel hedge — strip the hedge, render the informative tail as a capitalised stand-alone sentence, or drop the second sentence entirely if the tail is empty). Sentinel list covers `none`, `n/a`, `none available`, `none sufficient`, `no parallels`, `insufficient`, `partial,`, `partial;`, `limited`, `—`. Five worked examples cover every common variant.
- `[RECONSTRUCTION:]`, `[VARIANT:]`, and `[SPECULATION:]` rules rewritten with explicit placeholders, mandatory-slot lists, fallback behaviour for missing fields, and worked examples — matching the treatment INFERENCE and LACUNA received.
- Expanded self-check with grep-based anti-pattern set: placeholder-literal leaks (`<claim>`, `<basis>`, `<reconstruction>`, etc.), empty-slot artefacts (`_(\.footnote:`, `Inference: *\.`, `_\[At this point the tablet breaks\. *\.`), leaked sentinels (`none —`, `none available`, `Partial;` at clause start, etc.), and double-period artefacts (`..footnote:`, `.. Risk:`, `..])_`, `..]_`).
- Per-marker round-trip count check: every input marker has exactly one rendered equivalent in the output.

**Format-finalize safety net (stage 17)**
- Self-check expanded to mirror the full stage-13 anti-pattern set as a downstream safety net. If the marker-resolve stage slips, format-finalize catches it before the book ships.
- Master adoc is now named `<slug>.adoc` (derived from the book title or `slug:` in `scope.md`), not `book.adoc`. Stays at the book root so relative `include::` / `:bibtex-file:` / cover-image paths resolve without `../` rewrites.
- Final deliverables gathered under `<book-dir>/output/` (`<slug>.pdf`, `<slug>.epub`); build logs gathered under `<book-dir>/reports/` (`validation-report.md`).
- Renders go via `./container/render_book.sh` (see Tooling below).

**New global contract: Template discipline**
- Any skill with a `<placeholder>`-based output template must ship (1) at least one worked input→output example, (2) an explicit trailing-punctuation rule, and (3) a fallback for empty/sentinel-valued slots. The corresponding skill must include anti-pattern greps; the downstream assembly stage must mirror them.

**Relaxed writer/checker rule**
- The cross-AI independence requirement has been relaxed. The load-bearing constraint is now the **fresh conversation** (no memory of the writing). Using a different AI model for the check is still preferred — two models make independent mistakes — but the same model in a fresh conversation is acceptable when a second model is impractical. Hard-rule refusal clauses in `inventory-audit`, `claims-factcheck`, `prose-factcheck`, and `narrative-fidelity` now trigger on same-conversation only. Self-review in the *same* conversation is still forbidden.

**Tooling: containerised execution**
- New `container/` directory with a Podman-based isolation layer. The `myth-claude` image bundles Claude Code, Python, the full Asciidoctor toolchain (including `asciidoctor-bibtex`), Pandoc, and Git, and only sees the project directory as `/workspace`. Entrypoints:
  - `./container/run_claude.sh` — interactive Claude Code session
  - `./container/exec_cmd.sh <cmd> [args…]` — one-off command (e.g. `python assemble_prompt.py …`)
  - `./container/shell.sh` — plain shell inside the container
  - `./container/render_book.sh <book-dir> <slug> [--es]` — canonical book render
- Running inside the container lets Claude Code use `--dangerously-skip-permissions` without risk of touching files outside the project. RUNBOOK now recommends the container as the preferred execution environment.

**Tooling: render_book.sh**
- New host-side wrapper `./container/render_book.sh` and its in-container inner script `_render_book_inner.sh` replace ad-hoc `asciidoctor-pdf` / `asciidoctor-epub3` invocations. The wrapper:
  - creates `<book-dir>/output/` and `<book-dir>/reports/` on demand,
  - runs both renderers with `-r asciidoctor-bibtex --verbose --failure-level=WARN`,
  - captures stdout/stderr from both runs into `<book-dir>/reports/validation-report[.es].md` with a stage/slug/UTC-timestamp header,
  - unzips the rendered EPUB and greps the xhtml for pipeline-metadata leftovers (`EVIDENCE`, `COMPARATIVE-HOOK`), HTML-encoded placeholder literals (`&lt;claim&gt;`, etc.), all known sentinel hedges, and every double-period artefact position,
  - exits non-zero on any asciidoctor WARN/ERROR or any anti-pattern hit.
- Stage 17 and 18 skills now reference the wrapper as the canonical render step.

**Book slug convention**
- The master adoc and every deliverable are named after a book slug fixed in stage 17. The slug is taken from an explicit `slug:` field in `scope.md` if present; otherwise derived from the book title (part before any `:`, lowercased, non-alphanumerics → `_`, trimmed). Example: `= The Myths of Sumer: Stories from the First Scribes` → `the_myths_of_sumer`. Stage 18 reuses the slug fixed in 17 and does not re-derive it.

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
