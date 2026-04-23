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
