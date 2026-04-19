# Validation Report — Spanish Edition (Pass 5)

Date: 2026-04-19

## Build results

| Target | Command | Exit | Warnings/Errors |
|---|---|---|---|
| PDF | `asciidoctor-pdf --verbose --failure-level=WARN -o book.es.pdf book.es.adoc` | 0 | none |
| EPUB | `asciidoctor-epub3 --verbose --failure-level=WARN -o book.es.epub book.es.adoc` | 0 | none (only informational DEBUG line) |

PDF log contained zero lines; EPUB log contained a single `DEBUG: Wrote to ... book.es.epub` informational line. No WARN or ERROR emitted by either builder.

## Output sizes

| File | Size | Lines |
|---|---|---|
| book.es.adoc | 2,549 B | 99 |
| book.es.pdf | 6,455,731 B | — |
| book.es.epub | 1,293,457 B | — |
| frontmatter.es.adoc | 895 B | 22 |
| note-on-making.es.adoc | 4,129 B | 16 |

## Self-check findings

1. **Mirror check (book.adoc vs book.es.adoc)**: every English `include::` path has a matching `.es.adoc` include in the Spanish master, in identical order. Verified by diff on the mapped path set — no divergence.
2. **Include target existence**: every include target file exists on disk (verified by scripted file-existence check over the `include::` list).
3. **Marker leak check**: no `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:` markers found anywhere in the Spanish tree (top-level `.es.adoc` files plus `chapters/*.es.adoc`).
4. **Inline-comment leak check**: no ` // EVIDENCE:` or ` // COMPARATIVE-HOOK:` trailing inline markers (leading space, as specified) found anywhere in the Spanish tree.
5. **Asciidoctor dry runs**: both PDF and EPUB exit clean with `--failure-level=WARN`.
6. **Cover image**: `:front-cover-image: image:cover/myth_sumer_cover_es.jpg[]` — file exists at `cover/myth_sumer_cover_es.jpg` (466,435 B). (A previous build referenced the English cover; fixed before this build.)
7. **Document attributes**: `:doctype: book`, `:toc: left`, `:sectnums:`, `:toc-title: Índice`, `:appendix-caption: Apéndice`, `:figure-caption: Figura`, `:table-caption: Tabla`, `:note-caption: Nota`, `:important-caption: Importante`, `:caution-caption: Precaución`, `:warning-caption: Advertencia`, `:lang: es`, `:bibtex-file: bibliography.bib`, `:bibtex-style: chicago-author-date` — all present.
8. **Bibliography reuse**: `bibliography.bib` is reused unchanged (same file, same BibTeX keys) — no `bibliography.es.bib` was produced or needed.

## Borderline decisions

- **Copyright / licence wording (frontmatter.es.adoc)**: used the Spanish boilerplate for CC BY-NC-SA 4.0 (“Atribución-NoComercial-CompartirIgual 4.0 Internacional”) and pointed the URL to the Spanish-language deed (`/deed.es`), keeping the canonical licence URL intact. "Nerd Heaven Publishing" left in English as a proper noun, per the stage instructions.
- **Title rendering**: "The Myths of Sumer: Stories from the First Scribes" → "Los mitos de Sumer: historias de los primeros escribas". Register kept parallel to the original; capitalisation follows Spanish conventions (only the first word and proper nouns in the main title, lowercase after the colon for the subtitle).
- **AI-authorship preface heading**: "A Note on How This Book Was Made" → "Nota sobre la elaboración de este libro". Chose `elaboración` over `realización`/`preparación`/`fabricación`: `elaboración` reads as natural popular-science register without nominalisation drift, and tracks the slightly reflective tone of the English heading.
- **`se estamparon`** in preface sentence 1: kept the slight passive for rhythm, as in the English original ("were first pressed into clay"). The sentence is narrative colour, not agentless academic register.
- **Em-dash asides with closing dashes mid-sentence**: Spanish RAE convention often requires closing the dash when it is not sentence-final; preserved those closings in the preface where the English original left them open.

## Status

Pass 4 (assembly) and Pass 5 (validation) complete. The Spanish edition builds cleanly; no warnings or errors.
