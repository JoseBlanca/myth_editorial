---
name: post-human-normalize
description: Validates and normalizes any file that has been modified by a human reviewer before it becomes input for the next stage. Ensures that human edits have not broken the structural contracts that downstream stages depend on. Runs after every [HUMAN] review checkpoint.
---

# post-human-normalize

## For the human

Every time you review and edit a file — approving factcheck findings, fixing claims, resolving audit issues — there is a risk that your edits break something the next stage depends on. You might merge two claims into one paragraph, accidentally delete a marker, change a citation format, or remove a field from a YAML file. These are easy mistakes to make, and the next AI stage will silently produce wrong output rather than catching the problem.

This step is a quick automated check that catches these problems before they propagate. It runs after every human review point and validates that the edited file still meets the structural requirements for the next stage.

This step does not change the meaning of anything you wrote. It only checks structure, reformats where necessary, and flags violations that need your attention before proceeding.

## When to run

After every `[HUMAN]` checkpoint in the stage order:
- After inventory-audit human review → validates `inventory.approved.yaml`
- After intro-chapter factcheck human review → validates `chapters/00-introduction.adoc`
- After claims-factcheck human review → validates `chapters/NN-<slug>.claims.approved.adoc`
- After narrative-fidelity human review (if REVISE) → validates `chapters/NN-<slug>.adoc`
- After comparative-chapter factcheck human review → validates `comparative.adoc`
- After character-appendix factcheck human review → validates `character-appendix.adoc`

## Checks performed

### For YAML files (`inventory.approved.yaml`, factcheck outputs)
1. All required fields present per the schema defined in the producing skill.
2. No empty required fields.
3. All `source_id` values resolve to entries in `sources.yaml` registry.
4. No YAML syntax errors.

### For claims documents (`*.claims.approved.adoc`)
1. One claim per paragraph — no merged or bundled claims.
2. Every claim paragraph has a footnote citation.
3. Every evidence token (`// EVIDENCE: ...`) is syntactically valid and references a `source_id` in `sources.yaml`.
4. All markers (`[INFERENCE:]`, `[LACUNA:]`, `[RECONSTRUCTION:]`, `[VARIANT:]`) have all required sub-fields.
5. `glossary.yaml` renderings used consistently.

### For prose documents (intro, comparative, character-appendix, narrative chapters)
1. All markers syntactically valid with required sub-fields.
2. All evidence tokens syntactically valid.
3. Canonical chapter anchors present and unchanged.
4. `glossary.yaml` renderings used consistently.
5. No `never_use` glossary terms present.

## Output

The validated file, with a provenance comment block appended:
```
// Validated by post-human-normalize
// Timestamp: <UTC>
// Checks passed: <list>
// Warnings: <any non-blocking issues>
```

If any check fails, the file is returned to the human with a specific error report. The pipeline does not proceed until all checks pass.

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
The validated file proceeds to the next stage as defined in the stage order.
