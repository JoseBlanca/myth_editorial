---
name: chapter-draft
description: Transforms the verified facts into Asimov-style narrative prose. The AI's only job is writing — the facts are already checked. No new facts may be introduced. Every verified claim must appear in the narrative, and nothing unverified may be added.
---

# chapter-draft

## For the human

This is the creative stage — and it is much safer now that the facts are already locked. The AI is not simultaneously researching, citing, and writing. It is only writing. The factual skeleton has already been written and verified. The AI's job is to turn a list of numbered, checked facts into a narrative that reads like Asimov at his best.

The main risk is no longer inventing facts (those are locked) but **drift during the prose transformation**: dropping a verified fact because it doesn't fit the narrative flow, softening a claim until its meaning changes, or inserting a "helpful" detail that was never in the verified facts. The next step (`narrative-fidelity`) will catch these, but the writing AI should work to prevent them.

Importantly, the writing AI does **not** receive the original source texts. It only receives the verified claims document. This is deliberate: giving it the sources would tempt it to "improve" the chapter with additional details that were never fact-checked.

## Hard rules
1. **Every factual assertion in the narrative must correspond to a claim in the approved claims document.** No new facts, no new citations, no "I happen to know" additions.
2. **Every claim in the approved document must appear in the narrative.** Do not silently drop claims because they are inconvenient for the prose flow. If a claim is genuinely irrelevant, flag it rather than omitting it.
3. Use exactly the English renderings locked in `glossary.yaml`.
4. All markers from the claims document survive into the narrative. Do not paraphrase them away.
5. Citations carry over from the claims document. Do not add, remove, or reassign footnotes.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- `chapters/NN-<slug>.claims.approved.adoc` (fact-checked, human-reviewed claims)
- `briefs/NN-<slug>.yaml` (for variant classification, target length, special instructions)

**Not** primary source translations. The drafter does not need the sources — the claims document already contains everything verified. Providing sources would tempt the drafter to "improve" claims with additional details.

## Style: the Asimov method

Treat the reader as intelligent and uninformed. Gloss proper nouns with functional roles, not poetic epithets. Short paragraphs, one idea each. Plain modern English. Where the source is ambiguous, say so. Where scholars disagree, name it briefly. Use etymology and geography when they illuminate a specific point, never as mandatory ornament.

### Exemplar passage

> The Sumerians believed that before anything else existed, there was a primeval sea. They called her Nammu, and she seems to have been thought of as a kind of cosmic mother — though the texts that survive are maddeningly brief on this point. From Nammu came heaven and earth, conceived of as a single mountain with the sky (An) on top and the earth (Ki) below. An and Ki were the first divine couple, and their union produced Enlil, the god of the air.
>
> Enlil then did something that requires explanation. He separated his father An from his mother Ki, pushing the sky upward and leaving the earth below. This is a motif found in many mythologies — the violent separation of sky and earth by a younger god — but the Sumerian version is unusually matter-of-fact about it. There is no battle, no castration, no cosmic drama. Enlil simply separates them, and the world as we know it comes into being.

### Forbidden words

Do not use, in this register: *shimmering, ancient* (as ornament), *mystical, unfathomable, primordial* (as ornament), *ineffable, sacred* (as filler), *mighty, fearsome, dread, eternal, boundless, infinite, veiled, shrouded*. Avoid openings like "Long ago...", "In the time before time...", "It is said that...". These mark imitation-sacred prose, not Asimov.

## Variant handling (from brief)

- If `variants.classification` is **single-prevalent**: present the prevalent version in the body. Put alternate versions in AsciiDoc footnotes.
- If **co-equal**: present the variants inline in the body, each introduced with its source ("One tradition, preserved in [source], describes... Another, in [source], gives a different account...").

## Narrative transitions

The claims document has no connective tissue — that is your job. You may add:
- **Transitional sentences** that connect one claim to the next ("Having established the cosmic order, the narrative turns to...")
- **Orienting context** that helps the reader follow the story ("At this point in the text, the setting shifts to...")
- **Explanatory asides** that help the reader understand why something matters ("This is worth pausing on, because...")

These are **not** factual claims — they are prose scaffolding. They must not introduce new information about the myth. If a transition requires a factual bridge, that bridge should already be in the claims document as an `[INFERENCE:]` marker.

## Length

Per brief's `target_length_words`, driven by source volume. If you find yourself padding, stop and return the shorter version with a note.

## Output: `chapters/NN-<slug>.adoc`

```asciidoc
== <Chapter Title>

<Opening — orient the reader in time, place, and source situation.>

<Body — the verified claims, woven into narrative prose. Every claim present, no claims added.>

<Closing — brief note on the story's place in the culture's corpus. No cross-cultural comparison. Carry over `// COMPARATIVE-HOOK:` comments from claims document.>
```

## Self-check before returning
1. **Completeness**: walk the approved claims document claim by claim. Is every claim represented in the narrative? List any you cannot find — they are bugs.
2. **No additions**: scan the narrative for any factual assertion that does not correspond to a claim in the approved document. Flag it.
3. Scan for forbidden words — each hit is a drift signal; revise.
4. Every proper noun was glossed on first mention using `glossary.yaml`.
5. Variant handling matches the brief's classification.
6. Every marker has survived from claims to narrative.
7. All footnotes carried over unchanged.
8. Length matches the brief's target. Not padded.
9. `// COMPARATIVE-HOOK:` comments carried over.

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
To `narrative-fidelity`, fresh conversation, different model.
