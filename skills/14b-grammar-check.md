---
name: grammar-check
description: Catches grammar errors, awkward sentence constructions, and readability issues before the line-edit stage. Fixes only mechanical problems — does not change style, tone, or content. Runs after marker-resolve, before line-edit.
---

# grammar-check

## For the human

This step catches mechanical writing problems that slip through the drafting process: subject-verb disagreement, dangling modifiers, run-on sentences, ambiguous pronoun references, missing articles, and sentences that are grammatically correct but hard to parse on first reading.

It does not change the book's style or tone — that is the line-edit stage's job. It does not change facts — those are locked. It fixes only the kind of errors a copy editor catches: grammar, syntax, punctuation, and sentence clarity.

The AI tends to produce sentences that are technically correct but overloaded — too many subordinate clauses, too many parenthetical asides, or too many items in a single sentence. This step simplifies those without changing meaning.

## When to run

After `marker-resolve` (stage 13), before `line-edit` (stage 15). The input is the resolved text — all markers have been converted to final prose, so the grammar checker sees what the reader will see.

## Hard rules

1. **No factual changes.** If a grammar fix would change the meaning of a sentence, flag it for human review instead of fixing it.
2. **No footnote changes.** Do not modify, add, or remove footnotes or EVIDENCE tokens.
3. **No style changes.** Do not change the Asimov register. Do not add formality or informality. Do not rewrite sentences that are clear but plain.
4. **No content changes to resolved marker passages.** These were reviewed and locked.
5. **Preserve AsciiDoc structure** (headings, section breaks, include directives).

## What to fix

### Grammar errors
- Subject-verb agreement
- Tense consistency within paragraphs
- Dangling or misplaced modifiers
- Incorrect pronoun reference (ambiguous "it", "they", "this")
- Missing or incorrect articles (a/an/the)
- Comma splices and run-on sentences
- Sentence fragments (unless clearly intentional for effect)

### Readability issues
- Sentences over 50 words: split or restructure unless the length is essential for meaning
- Nested parenthetical asides: flatten (move to a separate sentence or footnote)
- Three or more subordinate clauses in a single sentence: simplify
- Ambiguous sentence structure where the reader must re-read to parse correctly
- Lists embedded in prose that would be clearer as an actual list or as separate sentences

### Punctuation
- Correct em-dash, en-dash, and hyphen usage
- Consistent serial comma (use it)
- Quotation marks and apostrophes in non-English terms

## What NOT to fix

- Word choice (that is line-edit's job)
- Sentence rhythm and flow (line-edit)
- Paragraph transitions (line-edit)
- Nominalizations and zombie nouns (line-edit)
- The academic tone of source overview sections (this is a deliberate register choice)

## Output

For each chapter:
- `chapters/NN-<slug>.grammar-checked.adoc` — the corrected text
- `chapters/NN-<slug>.grammar-diff.md` — a list of every change, showing original and corrected sentence

The diff file allows the human to skim and approve in bulk.

## Self-check

1. No factual content has changed — compare factual claims between original and corrected.
2. Footnote count and content unchanged.
3. All AsciiDoc structure intact.
4. Every change is logged in the diff file — no silent changes.

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
To `line-edit`, which handles style polish after grammar is clean.
