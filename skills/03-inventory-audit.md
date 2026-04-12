---
name: inventory-audit
description: Checks the story inventory for errors before any writing begins. Must be run by a different AI model than the one that produced the inventory, in a fresh conversation. Catches material from wrong cultures, made-up references, missing well-known stories, and silently merged variants.
---

# inventory-audit

## For the human

This is the first major quality check. It reviews the story list before any chapters are written. Catching errors here costs minutes; catching them after chapters are drafted costs hours.

The audit checks four things:

1. **Wrong-culture material.** Did any stories or story details sneak in from a neighboring culture? The tricky part: you can't just check "does this god belong to our culture?" — the same god often appears in multiple cultures. The real question is: "Does this specific plot detail appear in a document that was written within our culture and period?" A story detail found only in a Babylonian tablet doesn't belong in a Sumerian book, even if the god in question is originally Sumerian.

2. **Fake or wrong references.** AI models sometimes invent plausible-looking scholarly references. The auditor actually looks up each catalogue number, museum number, or ISBN to confirm it exists and contains what was claimed.

3. **Missing stories.** Are there well-known stories from this mythology that the inventory left out? The auditor cross-checks against standard reference works.

4. **Silently merged variants.** When multiple versions of a story exist, the inventory should list them separately. If it quietly combined two versions into one summary, that's a problem.

This audit must be run by a different AI model than the one that produced the inventory, in a fresh conversation (so the auditor has no memory of the work it's checking). An AI reviewing its own work in the same conversation catches almost nothing.

## Hard rule
If you are the model that produced `inventory.yaml`, or if you are in the same conversation in which it was produced, refuse and tell the user to start a fresh conversation with a different model.

## Inputs
- `scope.md`, `sources.yaml`
- `inventory.yaml`
- Web search tool (required — you will use it)

## The four checks

### 1. Contamination (document-provenance method)
For each story entry and each specific plot detail within it, ask: **is this detail attested in a document whose physical composition falls within the scope's date range and culture?**

Not "is the entity from this culture." The entity may span millennia. The question is whether the specific narrative element — a plot event, a ritual detail, a named object, a piece of dialogue — appears in a document that is in-scope.

A detail attested only in out-of-scope documents (e.g., a Neo-Assyrian tablet when the scope is Old Babylonian Sumerian) is CONTAMINATION-HIGH, regardless of whether the entity is "originally" from the scope culture.

For each HIGH contamination finding, provide a verbatim quote from the out-of-scope source showing where the detail actually comes from.

### 2. Unsupported entries and fabricated identifiers
For each story, verify that:
- The cited source exists (search for the identifier — DOI, ISBN, museum number, corpus ID).
- The cited source actually attests the story as described.

If the identifier does not resolve, or resolves to something that does not contain the described story, flag HIGH. Include the URL of your verification search so the human can replicate it.

### 3. Missing canonical stories
Consult scholarly surveys of the scope mythology (whitelisted reference works) for stories that belong in the inventory but are absent. Propose additions with full source identifiers. Severity MEDIUM — the human decides inclusion.

### 4. Internal variants handling
Where a story has multiple attested in-scope versions, check that the inventory's `variants` field acknowledges this. If the inventory silently conflates variants into a single summary, flag MEDIUM.

**Do not flag internal variants themselves as problems.** Multiple in-scope sources disagreeing is normal and is part of the corpus. The flag is for silent conflation, not for variance itself.

## Quote-to-evidence requirement
For every HIGH finding (contamination, fabricated identifier, unsupported claim), you must paste a verbatim quote from a source showing the problem. Either:
- A quote from an out-of-scope source showing where the contaminating detail actually comes from, OR
- A screenshot/URL of a database search showing an identifier does not resolve, OR
- A quote from the cited source showing it does not contain what was claimed.

Findings without quoted evidence are not valid HIGH findings; downgrade to MEDIUM and say so.

## Output: `inventory-audit.yaml`

```yaml
meta:
  auditor_model: <model name and version>
  entries_reviewed: <n>
  triangulations_performed: <n>
  time_to_review_estimate_minutes: <n>

summary:
  high: <n>
  medium: <n>
  low: <n>

findings:
  - severity: HIGH | MEDIUM | LOW
    kind: CONTAMINATION | UNSUPPORTED | FABRICATED-IDENTIFIER | MISSING | SILENT-CONFLATION
    story_id: <id, or "NEW" for missing>
    entity_or_detail: <what specifically>
    issue: <one sentence>
    evidence_quote: "<verbatim from source>"
    evidence_source: <id + loc, or verification URL>
    recommended_action: <concrete>

clean_entries: [<list of story_ids that passed all checks>]
```

## Honesty self-check
Answer these in `meta` explicitly:
1. Did I actually resolve each cited identifier, or did I assume well-known sources are correct? Name any I assumed.
2. Did I check every plot detail for provenance, or did I check only major ones? Name what I skipped.
3. For every HIGH finding, did I include a verbatim evidence quote? If any are missing, list them.
4. Am I the same model that produced the inventory? If yes, the audit is invalid.

## Human review protocol
Tell the user: review HIGH findings (~10 minutes), skim MEDIUM, ignore LOW unless maximum rigor is desired. Mark each finding's `recommended_action` field as `ACCEPTED` or `REJECTED`. Apply accepted changes to produce `inventory.approved.yaml` for the next stage.

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
`inventory.approved.yaml` to `post-human-normalize`, then to `chapter-briefs`.
