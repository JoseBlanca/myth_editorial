# Stage 17 (format-finalize) — Validation Report

Book: Sumer — *The Myths of Sumer: Stories from the First Scribes*
Date: 2026-04-18

## Build invocations

Run from `/home/jose/escritos/myth_editorial/books/sumer/`:

```
/home/jose/.local/share/gem/ruby/3.3.0/bin/asciidoctor-pdf --verbose --failure-level=WARN -o book.pdf book.adoc
/home/jose/.local/share/gem/ruby/3.3.0/bin/asciidoctor-epub3 --verbose --failure-level=WARN -o book.epub book.adoc
```

## Asciidoctor-PDF result

- Exit status: `0`
- stdout/stderr: empty (no warnings, no errors)
- Artifact: `book.pdf` (≈ 6.37 MB)

## Asciidoctor-EPUB3 result

- Exit status: `0`
- stdout/stderr:
  ```
  asciidoctor: DEBUG: Wrote to /home/jose/escritos/myth_editorial/books/sumer/book.epub
  ```
- Artifact: `book.epub` (≈ 1.28 MB)

Both renderers exited clean with no WARN- or ERROR-level messages. `--failure-level=WARN` was set; neither build tripped it.

## Marker sweep

Grep for bracketed authorial markers across all `.edited.adoc` chapter files, `comparative.edited.adoc`, and `character-appendix.adoc`:

| Pattern | Matches |
| --- | --- |
| `[INFERENCE:` | 0 |
| `[LACUNA:` | 0 |
| `[RECONSTRUCTION:` | 0 |
| `[VARIANT:` | 0 |
| `[SPECULATION:` | 0 |

All marker-resolve residue has been cleared. Parenthetical `Inference:` / `Reconstruction:` / similar cues that are part of resolved prose (e.g. "(Inference: …)" inside a sentence) are allowed per skill instructions and were not searched for.

## Cross-reference sweep

- 37 `[[ch-NN-<slug>]]` anchors defined (chapters 00–36) plus `[[ch-comparative]]` — all toc.yaml entries have a corresponding anchor.
- `character-appendix.adoc` contains no `<<ch-…>>` or `xref:` cross-references, so no anchor-resolution validation was required.

## Bibliography / evidence cross-check

- Unique `source_id` values found across all edited files, the comparative chapter, and the character appendix: **55**.
- Of these, **11** are in-scope Sumerological sources registered in `sources.yaml` (etcsl, black-2004, kramer-1961, jacobsen-1987, george-2003, cdli, civil-1994, vanstiphout-2003, alster-1972, sladek-1974, fluckiger-hawker-1999).
- The remaining **44** carry the `external-` prefix and appear only in `comparative.edited.adoc`, which by design cites out-of-scope comparanda from other traditions (Indo-European, Semitic, Egyptian, East Asian, medieval European). These IDs are **not** in `sources.yaml`; full citation data for each was extracted from the footnote text in the comparative chapter and included in `bibliography.bib`. See "Findings" below.
- Registered sources not referenced by any evidence token: `attinger-glossaire` (unused — not an error; flagged for awareness).

## Findings

### HIGH — out-of-scope comparative source_ids not in sources.yaml registry

44 `source_id=external-*` evidence tokens in `comparative.edited.adoc` do not resolve to entries in `sources.yaml`. Per the skill's cross-check rule ("any source_id in an evidence token that does not resolve to a sources.yaml registry entry is a HIGH finding"), this is recorded here.

Interpretation: this is by design, not a defect. The comparative chapter brief (see `completions/14-comparative-chapter.done.yaml`) explicitly instructs that each comparative section pair at least one in-scope Sumerian citation with at least one out-of-scope citation, and the `external-` prefix is the convention that was used to mark those out-of-scope references. Every `external-*` evidence token has a full bibliographic footnote in the comparative chapter prose, so the citation is reader-verifiable even though the ID is not pre-registered. `bibliography.bib` includes a BibTeX entry for each `external-*` ID, reconstructed from the comparative chapter's footnote text.

Recommendation for the human: if the reviewer wishes to formalise the out-of-scope registry, consider adding a `registry_external:` section to `sources.yaml` for future books. For this book, the bibliography is complete and every in-text citation resolves to a `bibliography.bib` entry.

### LOW — unused registered source

`attinger-glossaire` (Attinger 2021, *Glossaire sumérien–français*) is in the registry but is not cited via any evidence token in the finished book. Not an error.

### None — build warnings

Both PDF and EPUB rendering completed without emitting WARN or ERROR diagnostics.

## Build artifacts

| File | Size |
| --- | --- |
| `book.pdf` | 6,370,075 bytes (~6.37 MB) |
| `book.epub` | 1,280,576 bytes (~1.28 MB) |

## Self-check summary

- [x] No `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:` markers remain.
- [x] Every in-text evidence token has a matching BibTeX entry in `bibliography.bib`.
- [x] All `book.adoc` `include::` targets exist and are readable.
- [x] `[[ch-*]]` anchor set is complete; no dangling `<<ch-*>>` references in the appendix.
- [x] Cover image (`cover/myth_sumer_cover.jpg`) exists and is referenced from `:front-cover-image:`.
- [x] `frontmatter.adoc` and `note-on-making.adoc` exist and are included; no `back-matter.adoc` exists so no include directive was added for it.
- [x] Both asciidoctor dry runs exit with status 0 and no WARN/ERROR output.
- [ ] HIGH finding recorded for out-of-scope comparative source_ids (see above); decision deferred to human reviewer.
