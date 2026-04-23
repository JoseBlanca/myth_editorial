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
- Grep all output files for the empty-claim/empty-slot anti-patterns below — must be zero matches. These indicate a marker was stripped without its content being carried through.
  - `_(\.footnote:` — INFERENCE rendered with an empty claim (prints as `(. [n])` in the PDF).
  - `Inference: \.` or `Inference: *\.` — empty basis.
  - `Risk: \.` or `Risk: *\.` — empty risk.
  - `Basis: \.` — empty SPECULATION basis.
  - `counterargument: \.` — empty SPECULATION counterargument.
- Grep all output files for leaked LACUNA sentinels — must be zero matches inside italic brackets `_[...]_`. These indicate a `scholarly_reconstruction:` sentinel value was dropped verbatim instead of converted per Shape B above.
  - `none —`, `none --`, `none-`, `none—` (em-dash or hyphen variants)
  - `none available`, `none sufficient`, `none suffices`
  - `n/a —`, `n/a —`, `n/a -`
  - `partial,` or `partial;` appearing mid-sentence inside a `_[At this point…]_` bracket
  - `insufficient;` appearing mid-sentence inside a `_[…]_` bracket
- Grep all output files for the double-period artefact: `..]_`, `.. —`, `.. ]` — must be zero matches. This indicates the renderer appended a period after a `<what>` that already ended in one.
- Grep all output files for empty-what LACUNAs: `_\[At this point the tablet breaks\. \.` — must be zero matches. This indicates the renderer lost the `<what>` field.
- For every `[INFERENCE: ...]` marker in the input `.adoc`, confirm the corresponding line in the `.resolved.adoc` contains non-trivial prose between `_(` and `.footnote:[`. If the input was a short-form `[INFERENCE: claim]` (no basis/risk), confirm the output renders the claim as plain prose instead.
- No prose outside of marker-replaced sections has changed.

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
