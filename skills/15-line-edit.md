---
name: line-edit
description: Final prose-quality polish. All facts are locked — this step only improves clarity, sentence rhythm, and transitions. It cannot add, remove, or change any factual content. Based on Steven Pinker's *The Sense of Style*.
---

# line-edit

## For the human

This is the final prose polish. By this point, all facts are verified, all markers have been converted to final text, all citations are in place. This step only improves how the text reads — sentence rhythm, word choice, paragraph transitions, removing unnecessary jargon or throat-clearing. It cannot add, remove, or change any factual content. If an edit would change the meaning of a sentence, the editor must revert it.

This step runs after `marker-resolve` (which converts placeholder markers into final text) so the editor sees and polishes the actual prose the reader will read, not a version full of placeholders.

The editor produces a diff file showing every change it made, so you can skim and approve in bulk rather than comparing full documents line by line.

## Hard rules
1. No new factual claims. If editing changes a sentence's factual meaning, revert.
2. No footnote changes — no additions, removals, or re-assignments.
3. No changes to content inside already-resolved marker passages (italicized parentheticals, bracketed editorial notes, reconstruction footnotes). These were reviewed by fact-check and resolved by marker-resolve — they are locked.
4. AsciiDoc structure (headings, footnote syntax, include directives) is untouched.

## Inputs
- Marker-resolved story chapters (`chapters/NN-<slug>.resolved.adoc`)
- Marker-resolved intro chapter (`chapters/00-introduction.resolved.adoc`)
- Marker-resolved comparative chapter (`comparative.resolved.adoc`)
- `glossary.yaml` (to confirm renderings stay consistent)

## Method (Pinker, *The Sense of Style*)

- **Classic style**: writer and reader looking at the same thing. Remove throat-clearing.
- **Nominalizations**: "made a decision" → "decided".
- **Zombie nouns**: "the implementation of" → "implementing".
- **Subject-verb distance**: keep it short where possible.
- **Parallel structure** in lists and comparisons.
- **Paragraph transitions**: each paragraph's opening connects to the previous paragraph's close.
- **Proper-noun glosses**: confirm first-mention explanations are still present and match `glossary.yaml`.

## Output

For each chapter:
- `chapters/NN-<slug>.edited.adoc` plus `chapters/NN-<slug>.diff.md`
- `chapters/00-introduction.edited.adoc` plus `chapters/00-introduction.diff.md`
- `comparative.edited.adoc` plus `comparative.diff.md`

Each diff file shows original sentence vs edited sentence for every non-trivial change. The human skims the diffs to approve in bulk.

## Self-check
- Extract all factual claims from original and edited versions; compare. Any difference is a bug.
- Footnote count and content unchanged.
- Resolved marker passages unchanged.

## Handoff
To `character-appendix` and `format-finalize`.
