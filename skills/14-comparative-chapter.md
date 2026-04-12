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

## Handoff
To `prose-factcheck` (fresh conversation, different model). After factcheck, human review, and `post-human-normalize`, to `marker-resolve` along with all other chapters.
