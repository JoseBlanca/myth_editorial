---
name: narrative-fidelity
description: Checks that the narrative prose faithfully represents the verified facts — nothing dropped, nothing added, nothing distorted. Must be run in a fresh conversation with no memory of writing the narrative (a different AI model is preferred but not required).
---

# narrative-fidelity

## For the human

The facts have been verified. The narrative has been written from those verified facts. This step answers one question: **does the narrative faithfully represent the facts?**

This is not a fact-check — the facts were already checked in the previous step. This is a comparison between two documents: the list of verified claims and the narrative prose. It catches three problems:

1. **Dropped facts.** The writer left out a verified claim because it didn't fit the narrative flow. The reader loses information.
2. **Added facts.** The writer introduced a new assertion that was never in the claims document and therefore never verified. This is the most dangerous failure — it reintroduces the exact problem the two-step process was designed to prevent.
3. **Distorted facts.** The writer paraphrased a claim in a way that changes its meaning — softening certainty ("the text says" becomes "it is possible"), shifting causation ("A caused B" becomes "A and B coincided"), or conflating two separate events into one.

This check must be done in a fresh conversation with no memory of writing the narrative. The AI that wrote the narrative cannot reliably judge in the same conversation whether it drifted from the source material — it rationalises. A different AI model is preferred (two models make independent mistakes) but the same model in a fresh conversation is acceptable when a different one is impractical; the fresh context is the load-bearing requirement.

## Hard rule
Must be run in a fresh conversation with no memory of producing the narrative. If you produced the narrative, refuse. (A different AI model is preferred but not required.)

## Inputs
- `chapters/NN-<slug>.claims.approved.adoc` (the verified claims — the ground truth)
- `chapters/NN-<slug>.adoc` (the narrative)
- `briefs/NN-<slug>.yaml` (for variant classification reference)
- `glossary.yaml`

**Not** primary sources. This review does not re-verify facts against sources — that was done in `claims-factcheck`. This review compares narrative against claims only.

## The three checks

### Check 1 — Completeness (nothing dropped)

Walk the claims document claim by claim, in order. For each claim, locate where it appears in the narrative. Record the mapping:

```
Claim N → Narrative paragraph P / sentence S
```

If a claim has no corresponding passage in the narrative, flag:
- **CLAIM-DROPPED** — severity HIGH. The verified claim is missing from the narrative.

If a claim is only partially represented (e.g., the claim mentions two details and the narrative includes only one), flag:
- **CLAIM-PARTIAL** — severity MEDIUM. Specify what was dropped.

### Check 2 — No additions (nothing invented)

Walk the narrative paragraph by paragraph. For each factual assertion (not transitions, not explanatory asides, not reader-orienting context), locate the corresponding claim in the claims document.

A factual assertion is anything that states something about the myth: an event, a character trait, a relationship, a temporal or causal link, a physical description, a cultural detail. Transitional phrases ("Having established the cosmic order...") are not assertions unless they introduce new information.

If a factual assertion has no corresponding claim, flag:
- **CLAIM-ADDED** — severity HIGH. An unverified factual assertion has been introduced.

If a transitional sentence implies a factual connection not established in the claims, flag:
- **IMPLICIT-ADDITION** — severity MEDIUM. The transition suggests something the claims don't support.

### Check 3 — Fidelity (nothing distorted)

For each claim-to-narrative mapping found in Check 1, compare meaning:
- Does the narrative preserve the claim's level of certainty? (A claim marked as inference should not be presented as fact in the narrative.)
- Does the narrative preserve causal direction? ("A caused B" should not become "B caused A" or "A and B coincided.")
- Does the narrative preserve scope? ("Some scholars argue" should not become "Scholars agree.")
- Are markers preserved? Every `[INFERENCE:]`, `[LACUNA:]`, `[RECONSTRUCTION:]`, `[VARIANT:]` in the claims should survive in the narrative.

If meaning has shifted, flag:
- **CLAIM-DISTORTED** — severity HIGH if the factual meaning changed, MEDIUM if only emphasis or nuance shifted.

### Additional checks

- **Glossary fidelity**: confirm `glossary.yaml` renderings are used consistently. Any `never_use` terms: GLOSSARY-VIOLATION.
- **Forbidden words**: flag hits from the forbidden-words list.
- **Footnote integrity**: every footnote in the narrative must match the claims document exactly — same source, same location. No additions, removals, or reassignments. Flag FOOTNOTE-MISMATCH if different.

## Output: `chapters/NN-<slug>.fidelity.yaml`

```yaml
meta:
  auditor_model: <name and version>
  claims_file: chapters/NN-<slug>.claims.approved.adoc
  narrative_file: chapters/NN-<slug>.adoc
  total_claims: <n>
  claims_mapped: <n>
  verdict: PASS | REVISE

claim_mapping:
  # Every claim with its narrative location
  - claim_number: <n>
    claim_text: "<brief summary>"
    narrative_location: "<paragraph number or adoc line>"
    status: MAPPED | PARTIAL | DROPPED

findings:
  - kind: CLAIM-DROPPED | CLAIM-PARTIAL | CLAIM-ADDED | IMPLICIT-ADDITION | CLAIM-DISTORTED | GLOSSARY-VIOLATION | FORBIDDEN-WORD | FOOTNOTE-MISMATCH
    severity: HIGH | MEDIUM | LOW
    claim_number: <n, if applicable>
    narrative_location: "<paragraph or line>"
    issue: <one sentence>
    detail: "<specific text comparison — claim says X, narrative says Y>"
    recommended_fix: <concrete>
```

## Verdict rules
- **PASS**: zero CLAIM-DROPPED, zero CLAIM-ADDED, zero HIGH CLAIM-DISTORTED, ≤ 2 MEDIUM findings.
- **REVISE**: any CLAIM-DROPPED, any CLAIM-ADDED, any HIGH CLAIM-DISTORTED, or > 2 MEDIUM findings.

## Honesty self-check
Answer in `meta`:
1. Did I map every claim, or skip some that seemed obvious? List any I skipped.
2. Did I check every narrative paragraph for additions, or only spot-check? Be specific.
3. For distortion checks, did I compare precise meaning or just topic? Any I only topic-matched are noted here.
4. Am I the same model that produced the narrative? If yes, this review is not valid.

## Human review protocol

If the verdict is **PASS**: the chapter proceeds to `marker-resolve` (after all chapters are done and the comparative chapter is written and fact-checked).

If the verdict is **REVISE**: review the findings. For each finding, either:
- Fix the narrative directly (for dropped claims: add them back; for added claims: remove them; for distortions: correct them).
- Or send the chapter back to `chapter-draft` with the fidelity findings attached, for the writing AI to revise.

The corrected narrative does not need to go through `claims-factcheck` again (the facts haven't changed — only the prose representation). But it should go through `narrative-fidelity` again to confirm the fixes resolved the findings.

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
After PASS (or PASS on re-review): the chapter waits until all story chapters are complete, then proceeds with the comparative chapter and marker-resolve.
