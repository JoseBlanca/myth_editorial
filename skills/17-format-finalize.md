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
- `comparative.edited.adoc` (comparative chapter)
- `character-appendix.adoc` (fact-checked — this is a reference appendix and does not go through marker-resolve or line-edit)
- `sources.yaml`
- `cover.jpg` or `cover.png` — the cover image, provided by the user. Used by Asciidoctor-PDF for the front cover and by Asciidoctor-EPUB3 for the EPUB cover.
- `front-matter.adoc` and `back-matter.adoc` (dedication, preface, index, etc. — optional; if absent, omit the corresponding `include::` directives from `book.adoc`)

## Agent instructions

### 1. Bibliography extraction
Scan all files for `// EVIDENCE: source_id=<id> ; loc=<loc>` tokens. Collect all unique `source_id` values. For each, look up the entry in `sources.yaml` registry and produce a BibTeX entry using the `full_citation`, `author`, `title`, `year`, and `identifier_value` fields. Use the `id` from `sources.yaml` as the citation key.

Cross-check: any `source_id` in an evidence token that does not resolve to a `sources.yaml` registry entry is a HIGH finding — stop and report. Any registry entry never referenced by any evidence token is noted (unused source — not an error, but worth flagging).

### 2. Master assembly
Produce `book.adoc`:
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

include::chapters/01-<slug>.edited.adoc[]
include::chapters/02-<slug>.edited.adoc[]
// ... in toc.yaml order ...

include::comparative.edited.adoc[]

include::character-appendix.adoc[]

// include::back-matter.adoc[]    ← include only if file exists
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
- No `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:` markers remain anywhere. (Grep all `.edited.adoc` files, `comparative.edited.adoc`, and `character-appendix.adoc`.)
- Every footnote citation resolves to a bibliography entry.
- Every bibliography entry is on the whitelist.
- Every `<<chapter-anchor>>` cross-reference in `character-appendix.adoc` resolves to an actual anchor in the chapter files.
- Cover image file exists and is referenced correctly in `:front-cover-image:`.
- `front-matter.adoc` and `back-matter.adoc`: if referenced in `book.adoc`, confirm the files exist. If absent, confirm the include directives are removed.
- Asciidoctor dry runs exit clean.
