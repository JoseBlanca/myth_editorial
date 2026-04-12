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

### `[INFERENCE: claim | basis: X | risk: Y]`
Render as an italicized parenthetical with a footnote containing the basis and risk:
```
_(The text does not state this explicitly, but the following episode requires it.footnote:[Inference: <basis>. Risk: <risk>.])_
```

### `[LACUNA: what | source: ref | scholarly_reconstruction: X]`
Render as a bracketed editorial note, italicized:
```
_[At this point the tablet breaks. Approximately 20 lines are lost. Scholars such as <ref> have proposed the narrative resumed with <reconstruction>.]_
```
If no scholarly reconstruction is given, omit the second sentence.

### `[RECONSTRUCTION: content | gap_source: X | fill_source: Y | confidence: Z]`
Render the content in prose, with a footnote flagging it as reconstruction:
```
<content rendered as normal prose>.footnote:[This passage reconstructs the lacuna at <gap_source> from the parallel account in <fill_source>; confidence: <Z>.]
```

### `[VARIANT: primary=A | alt=B | chosen: A | reason: R]`
Only appears in single-prevalent cases (co-equal variants are already inline without markers). Render as the prevalent version in body, with a footnote giving the alternate:
```
<prevalent version text>.footnote:[An alternate tradition in <B source> gives: "<alt phrase>". The prevalent version is chosen here because <reason>.]
```

### `[SPECULATION: claim | basis: X | counterargument: Y]`
Only appears in the comparative chapter. Render as the claim in prose, with a footnote presenting both sides:
```
<claim rendered as normal prose>.footnote:[This parallel is speculative. Basis: <basis>. The main counterargument: <counterargument>.]
```

## Output

- Story chapters: `chapters/NN-<slug>.resolved.adoc`
- Intro chapter: `chapters/00-introduction.resolved.adoc`
- Comparative chapter: `comparative.resolved.adoc`

## Self-check
- Grep all output files for `[INFERENCE:`, `[LACUNA:`, `[RECONSTRUCTION:`, `[VARIANT:`, `[SPECULATION:` — must be zero matches.
- No prose outside of marker-replaced sections has changed.

## Handoff
To `line-edit`.
