---
name: note-on-making
description: Produces note-on-making.adoc — a short preface that explains, in plain prose, how the book was actually made. The reader needs to know that the text was written by AI working under human direction, what role the human played, what tools were used, and how to weigh the result.
---

# note-on-making

## For the human

This preface is the most important non-narrative section of the book. The frontmatter has a one-line AI-authorship disclosure; this preface unpacks it. Without it, a reader can plausibly mistake the author of this pipeline for the author of the prose. The author of this pipeline does not want that mistake.

The note must do four things, in this order:

1. State plainly that the prose was written by AI, almost from first word to last, under human direction.
2. Explain the structure of the work — the pipeline of discrete stages, fresh conversations between stages, fact-checking against named primary sources, an audit trail tied to specific tablets or texts.
3. Name the tech stack honestly. Which models were actually used at which stages. Whether the cross-model discipline was held to or not. The Python harness, AsciiDoc, Asciidoctor, the bibliography pipeline.
4. Spell out exactly what the human author did. Choosing the project, reading audit reports, correcting findings at human-review gates, pressing the button for the next stage. Not the prose, not the scholarship, not the comparative judgements.

The model is the `note-on-making.adoc` in `books/sumer/` — read it before drafting. Do not copy it verbatim; the new book may differ in which models were used, whether the cross-model discipline was actually enforced, and how heavy the human's correction passes were. Tell the truth about *this* book.

## Inputs

- `scope.md` (for the book topic — what culture, what corpus)
- `books/<book>/completions/*.done.yaml` (records of which stages ran and the agent model that ran them — the source of truth for which AI did what)
- The `books/sumer/note-on-making.adoc` template, as a structural model only
- Anything the human says about deviations from the standard pipeline (e.g., "Gemini did the research stage, Claude did everything else")

## Agent instructions

1. Read the completion records under `books/<book>/completions/`. Each `.done.yaml` carries an `agent_model` field. Tally which models ran which stages. This is the ground truth for the tech-stack paragraph.
2. Read the sumer note-on-making for structure. Note that it has five paragraphs: (a) framing — ancient stories, AI prose, human role; (b) the experiment — what the project is; (c) the pipeline — discrete stages, fact-checking, audit gates; (d) the actual models used and whether cross-model discipline was held; (e) the machinery — Python harness, AsciiDoc, bibliography from evidence tokens; (f) what the human actually did.
3. Draft the new note-on-making with the same structural beats but write it freshly for this book. The voice is the same Asimov-style register as the rest of the book — clear, plain, not chatty.
4. The tone is honest, not defensive. The reader should come away knowing what they are reading and able to judge it on those terms. Do not apologize for the use of AI; do not oversell it either.
5. Do not use markers (`[INFERENCE:]`, `[LACUNA:]`, evidence tokens). This preface is meta-commentary about the project, not narrative prose with citations to primary sources.

## Output: `note-on-making.adoc`

```asciidoc
[preface]
== A Note on How This Book Was Made

<Paragraph 1: Framing. The stories are ancient; the prose that retells them was written by AI; the human role was small and specific.>

<Paragraph 2: The experiment. What this project is and why this culture / topic was chosen.>

<Paragraph 3: The pipeline. Discrete stages, fresh conversations between stages, claims fact-checked against named sources, human-review gates between major stages.>

<Paragraph 4: The actual tech stack. Which AI models ran which stages, on this book. Whether the cross-model discipline was enforced or not. Be honest — if Claude did almost everything, say so.>

<Paragraph 5: The machinery. Python prompt-assembly harness; evidence tokens that anchor every factual claim to a primary source; bibliography built mechanically from those tokens; AsciiDoc rendered to PDF and EPUB through Asciidoctor.>

<Paragraph 6: What the human author did. Choose the topic, read the scope and inventory, skim audit reports, correct findings at review gates, press the button for the next stage. Not the prose, not the scholarly judgement, not the sentence rhythm.>

<Paragraph 7: How the reader should weigh the result. The scholarship is real; each claim is tied to a published source; the stories are the stories on the tablets / in the manuscripts. But the voice is not a human voice.>
```

## Self-check

- The preface names the AI models that actually ran the stages, drawn from the `completions/*.done.yaml` records. No vague "an AI" where a model name is known.
- If the cross-model discipline (different model for writer vs. checker) was *not* held in practice, the preface says so explicitly. Do not paper over it.
- The "what the human did" paragraph lists only the human's actual decisions and review actions. It does not credit the human with the prose, the comparative judgements, or the scholarship.
- The preface points the reader at the bibliography and the in-text citations as the verifiable layer of the book.
- No marketing language. No "powered by", no "cutting-edge", no "revolutionary".
- No markers (`[INFERENCE:]`, `// EVIDENCE:`, `[LACUNA:]`) anywhere — this is meta-commentary.

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
summary: "<one-line description of what was produced>"
```

**Rules**:
1. Write this file only after ALL outputs are complete and verified.
2. The `lines` count must be the actual line count of each file at the time of writing — do not estimate.
3. If you were unable to complete all outputs, write the file with `status: "partial"` and list which outputs are missing in a `missing` field.
4. Never write `status: "completed"` if any output file is missing or truncated.

## Handoff

To `format-finalize`. The note-on-making is included by the master adoc immediately after `frontmatter.adoc` and before the introduction chapter.
