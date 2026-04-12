---
name: prose-factcheck
description: Checks factual claims embedded in prose — for the intro chapter, comparative chapter, and character appendix. Unlike claims-factcheck which operates on isolated claims, this skill must first extract claims from flowing prose before verifying them. Must be run by a different AI model in a fresh conversation.
---

# prose-factcheck

## For the human

This is the factcheck for prose content that wasn't written through the claims-first process: the intro chapter, the comparative chapter, and the character appendix. Unlike `claims-factcheck` (where each paragraph is one isolated, individually cited claim), here the checker must first extract the factual claims from flowing prose — a harder task that requires judgment about what constitutes a claim vs. connective tissue.

The same four disciplines apply (show evidence, verify references, distinguish contradictions from errors, read backwards), but with an added initial step: claim extraction.

## Hard rule
Must be run in a fresh conversation with a different AI model than produced the content.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- The prose document to check:
  - `chapters/00-introduction.adoc` (intro chapter)
  - `comparative.adoc` (comparative chapter)
  - `character-appendix.adoc` (character appendix)
- Primary source translations (pasted or accessible via fetch)
- Web search tool (required)

## The six passes

### Pass 0 — Claim extraction
Walk the prose document and extract every factual claim into a numbered list. A claim is any assertion about the myth, character, or culture — not transitions, opinions, or reader-orienting context. This extraction is the foundation for all subsequent passes. Record each extracted claim with its paragraph location.

This pass is what makes prose-factcheck harder than claims-factcheck. The quality of the entire audit depends on thorough extraction.

### Pass 1 — Claim-level verification (start to end)
For each extracted claim, assign a verdict using the same six verdicts as `claims-factcheck` (✓ SUPPORTED, △ INTERNAL-VARIANCE, ? UNVERIFIED, ! CITATION-WRONG, ⚠ CONTAMINATION, ✗ FABRICATION).

### Pass 2 — Triangulation of references
Same as `claims-factcheck`.

### Pass 3 — Document-provenance contamination scan
Same as `claims-factcheck`.

### Pass 4 — Marker and glossary integrity
- Check all markers have required sub-fields.
- For comparative chapter: verify `[SPECULATION:]` markers have both basis and counterargument.
- Check `glossary.yaml` renderings and `never_use` terms.
- For character appendix: flag any physical-description language without a source citation (the primary fabrication risk).

### Pass 5 — Reverse-order second pass
Same as `claims-factcheck`.

## Output

- `chapters/00-introduction.factcheck.yaml`
- `comparative.factcheck.yaml`
- `character-appendix.factcheck.yaml`

Same YAML schema as `claims-factcheck`, plus:

```yaml
meta:
  claims_extracted: <n>   # from Pass 0 — if this is low, extraction was lazy
```

## Verdict rules
Same as `claims-factcheck`.

## Honesty self-check
Same as `claims-factcheck`, plus:
6. Did I extract every factual claim in Pass 0, or only the prominent ones? Name any sections I under-extracted.

## Human review protocol
Review HIGH findings. Apply accepted fixes directly to the prose file. Run `post-human-normalize` before proceeding.

- **Intro chapter** → corrected `chapters/00-introduction.adoc` proceeds to `post-human-normalize`, then `marker-resolve`.
- **Comparative chapter** → corrected `comparative.adoc` proceeds to `post-human-normalize`, then `marker-resolve`.
- **Character appendix** → corrected `character-appendix.adoc` proceeds to `post-human-normalize`, then `format-finalize`.

## Handoff
After human review and normalization: the corrected file proceeds to the next stage as defined in the stage order.
