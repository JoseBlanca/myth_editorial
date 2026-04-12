---
name: glossary-lock
description: Locks the English translation for recurring terms and proper nouns before any chapter is written. Prevents inconsistency across chapters and false contradictions during fact-checking. Interactive — the AI proposes, you decide.
---

# glossary-lock

## For the human

Scholars translate key terms differently. For example, the Sumerian word *me* is translated as "divine powers" (Kramer), "cosmic ordinances" (Jacobsen), or left untranslated (Black). If the writing AI picks one translation and the fact-checking AI is reading a source that uses a different one, the fact-checker will flag a false contradiction — the claim is correct, it's just using a different translation of the same word. And if different chapters use different translations of the same term, the book reads as if multiple people wrote it without coordinating.

This step solves both problems by locking in a single English translation for each recurring term before any chapter is written. Usually 10–30 terms per book. It's interactive: the AI proposes options for each term (with reasons), and you pick the one you prefer or supply your own.

## Inputs
- `scope.md`, `sources.yaml`
- All `briefs/*.yaml`

## Agent instructions

### Step 1: extract candidate terms
Scan all briefs' `entities_glossary` fields and source-text samples. Identify:
- Proper nouns appearing in 2+ chapters (deities, heroes, places, artifacts).
- Technical terms with no one-to-one English equivalent.
- Ritual, political, and cosmological vocabulary that translators render inconsistently.

### Step 2: survey renderings
For each candidate, report:
- Native form (transliterated with standard diacritics).
- 2–4 rendering options, each attributed to a specific translator/edition.
- Your recommendation with a one-sentence reason.
- Any rendering that would be wrong (e.g., an out-of-scope culture's equivalent).

### Step 3: interactive confirmation
Present the proposed glossary. For each entry the user either accepts, picks an alternate, or supplies their own. Do not skip entries silently.

## Output: `glossary.yaml`

```yaml
terms:
  - native: <transliteration>
    renderings_considered:
      - { form: <rendering>, source: <translator/edition> }
    chosen: <final locked rendering>
    rationale: <one line>
    first_mention_gloss: <short functional gloss, Asimov-style>
    never_use: [<list of out-of-scope equivalents that must never appear>]
```

## Self-check
- Every term appearing in 2+ briefs is included.
- Every `never_use` entry is a real out-of-scope equivalent (e.g., Akkadian for a Sumerian book), not just a synonym.
- First-mention glosses are functional, not poetic (no "mighty", "ancient", etc.).

## Mid-pipeline glossary updates

If a later stage (e.g., `chapter-claims`) encounters a recurring term that should be in the glossary but isn't, the AI should stop and flag it. The human then adds the term to `glossary.yaml` using the same process (survey renderings, pick one, add `never_use` entries). This does not require re-running `glossary-lock` from scratch — just append the new entry and confirm consistency with existing entries.

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
`glossary.yaml` to `intro-chapter` and `chapter-claims`.
