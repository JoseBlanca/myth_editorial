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
