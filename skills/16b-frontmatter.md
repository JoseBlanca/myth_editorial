---
name: frontmatter
description: Produces frontmatter.adoc — the title page, copyright notice, license terms, and AI-authorship disclosure that opens the book. Runs late in the pipeline, after the title is locked, before format-finalize.
---

# frontmatter

## For the human

The frontmatter is the first thing the reader sees: title, subtitle, author, publisher, copyright, license, and a one-line statement that the prose was written by AI. It is short — a single page — but several of the lines are load-bearing.

The AI-authorship line is the one that matters most. Without it, a reader who flips through the book will assume a human wrote it. The author of this pipeline does not want that. The line at the bottom of the frontmatter says, plainly, that the prose was composed by AI under human direction. The longer story — what the AI did, what the human did, what tools were used — lives in `note-on-making.adoc`, which follows immediately after.

This step runs late in the pipeline because the title can change. The Chaoskampf book was retitled from "Chaoskampf Across Cultures" to "The Slayer and the Dragon: Chaoskampf Across Cultures" after the chapters were written. Generating the frontmatter at scope-lock time would have produced a stale title.

## Inputs

- `scope.md` (for the book title — the `= <Book Title>` line of the master adoc, or whatever title the human has settled on)
- The author name, publisher name, copyright year, and license — these are project-wide defaults the agent can read off `frontmatter.adoc` files in sibling books, or ask the human if no precedent exists.

## Agent instructions

1. Determine the title and subtitle. The title is the part before the `:` in the master adoc's `= <Title>: <Subtitle>` line; the subtitle is the part after. If the master adoc does not yet exist, ask the human for the final title.
2. Determine the author, publisher, copyright year, and license. The defaults across this project are:
   - **Author**: Jose Blanca
   - **Publisher**: Nerd Heaven Publishing
   - **Copyright year**: the current calendar year of publication
   - **License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
   If a sibling book under `books/` has a different value in its `frontmatter.adoc`, use that as the precedent and confirm with the human.
3. Write `frontmatter.adoc` using the template below.
4. Do not invent additional fields (ISBN, edition number beyond "First edition", dedication line). If the human wants those, they will say so.

## Output: `frontmatter.adoc`

```asciidoc
[.text-center]
*<TITLE IN UPPERCASE>* +
_<Subtitle>_

[.text-center]
<Author>

[.text-center]
Published by *<Publisher>*

[.text-center]
First edition, <Year>

'''

Copyright © <Year> <Author>.

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0). To view a copy of this licence, visit https://creativecommons.org/licenses/by-nc-sa/4.0/.

You are free to share the work and to adapt it for non-commercial purposes, provided you credit the author and license any derivative work under the same terms.

The prose of this book was composed by artificial intelligence working under human direction. All scholarly sources consulted are cited in the text and in the bibliography; a fuller account of the process is given in the preface that follows.
```

The closing paragraph (the AI-authorship disclosure) is mandatory. It must point the reader to the `note-on-making.adoc` preface that follows. Do not soften it ("with assistance from", "drafted with the help of") — the prose was written by AI, and the line says so.

## Self-check

- The title and subtitle on the title-page lines match the `= <Title>: <Subtitle>` line of the master adoc (if it exists yet). No drift.
- The copyright year and license terms match the values used in sibling books, unless the human explicitly overrode them.
- The AI-authorship disclosure paragraph is present, verbatim or with only the smallest adaptations (e.g., to point at a differently-named preface).
- No invented metadata (ISBN, edition number "Second edition" without basis, etc.).

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

To `note-on-making`, then to `format-finalize`. The frontmatter and the note-on-making preface are both included by the master adoc, immediately after the title-page block and before the introduction chapter.
