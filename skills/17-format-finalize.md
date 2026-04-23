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
- No `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:` markers remain anywhere. (Grep all `.edited.adoc` files, `comparative.edited.adoc`, and `character-appendix.adoc`.)
- No `// EVIDENCE:` or `// COMPARATIVE-HOOK:` remain in the `.edited.adoc` files after step 2. Grep the rendered EPUB's `.xhtml` contents for both strings — must be zero.
- No empty-claim resolution artefacts remain from stage 13. Grep all `.edited.adoc` files for `_(\.footnote:` (INFERENCE rendered without its claim — prints as `(. [n])` in the PDF), `Inference: *\.`, and `Risk: *\.`. Zero matches expected. If any remain, stop and report — the upstream marker-resolve stage produced bad output and must be re-run.
- No leaked LACUNA sentinels remain from stage 13. Grep all `.edited.adoc` files (case-insensitive) for `none —`, `none --`, `none-`, `none available`, `none sufficient`, `n/a —`, `n/a -`, and (inside italic `_[…]_` brackets) `partial,`, `partial;`, `insufficient;`. Zero matches expected. If any remain, stop and report — the marker-resolve stage dropped a `scholarly_reconstruction:` sentinel value verbatim into the rendered prose instead of converting it per the rule.
- No double-period artefact (`..]_`, `.. —`, `.. ]`) appears in any `.edited.adoc` file. Zero matches expected.
- No empty-what LACUNAs (`_\[At this point the tablet breaks\. \.`) appear in any `.edited.adoc` file. Zero matches expected.
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
