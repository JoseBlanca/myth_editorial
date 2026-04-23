---
name: comparative-chapter
description: Produces the single chapter where cross-cultural comparison is allowed. All the "this is similar to Greek/Norse/Egyptian mythology" observations are confined here, keeping the story chapters focused on one culture. Runs after all story chapters are finished.
---

# comparative-chapter

## For the human

Every story chapter in the book stays strictly within its own culture — no "this is similar to the Greek myth of..." asides. All cross-cultural observation is confined to this single chapter at the end. This separation keeps the story chapters clean and focused, while still giving the reader the comparative perspective that makes mythology fascinating.

Throughout the earlier stages, the AI has been collecting notes on cross-cultural parallels (tagged as `COMPARATIVE-HOOK` comments). This chapter draws on those notes, plus comparative-mythology scholarship, to explore the parallels in depth.

This chapter is inherently more speculative than the story chapters. It uses an additional marker, `[SPECULATION:]`, for hypotheses that are plausible but not established scholarly consensus — each with both the evidence for it and the main argument against it.

## Inputs
- All story chapters after narrative-fidelity has passed (`chapters/NN-<slug>.adoc`) — the factual content is locked, though markers have not yet been resolved and prose has not yet been polished. The comparative chapter needs the factual content, not the final formatting.
- `chapters/00-introduction.adoc` (the intro chapter, post-factcheck)
- All briefs (for `comparative_hooks`) and all `// COMPARATIVE-HOOK:` comments left in chapter drafts
- `scope.md`, `sources.yaml`
- Optional comparative-mythology whitelist (Dumézil, Puhvel, Watkins, West, Witzel, Lincoln — add to `sources.yaml` before this stage)

## Rules
- Every comparison cites both the in-scope source and the out-of-scope source.
- Structural parallels (tripartite function, sky-father motif, etc.) cite scholarly methodology, not invented frameworks.
- Speculation is allowed but must be marked: `[SPECULATION: claim | basis: X | counterargument: Y]`.
- Do not retell out-of-scope myths at length — one-paragraph summaries, then the comparison.
- `// EVIDENCE: source_id=X ; loc=Y` tokens go on their own line (column 0), never appended after paragraph text. AsciiDoc only treats `//` as a comment at line start — a trailing marker renders as literal text in the final PDF/EPUB. Same rule as `chapter-claims`.

## Style
Asimov register, extended for comparative nuance. Signal uncertainty: "One might observe...", "Scholars such as X have argued...". Avoid grand unifying claims; stay close to specific parallels.

## Output: `comparative.adoc`

Structured as:
- Intro paragraph on the scope and limits of comparison.
- One section per major parallel type (cosmogonic parallels, heroic parallels, eschatological parallels, etc.), as appropriate.
- Closing that resists overreach.

## Self-check
- Every comparative claim cites both an in-scope source and an out-of-scope source.
- Every `[SPECULATION:]` has both basis and counterargument sub-fields.
- No claim presented as consensus unless it actually is.

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
To `prose-factcheck` in a fresh conversation (a different AI model is preferred but not required). After factcheck, human review, and `post-human-normalize`, to `marker-resolve` along with all other chapters.
