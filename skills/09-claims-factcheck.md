---
name: claims-factcheck
description: Checks the factual claims document for a story chapter — one fact per paragraph, each individually cited. This is the primary factcheck mode and the most reliable, because each claim is isolated and trivially verifiable. Must be run in a fresh conversation with no memory of producing the claims (a different AI model is preferred but not required).
---

# claims-factcheck

## For the human

This is the most important quality check for story chapters. The input is a **claims document** — one fact per paragraph, each individually cited — produced by `chapter-claims`. Each paragraph is one claim, one source reference, one thing to verify. No prose to parse, no bundled assertions to disentangle.

This step enforces four disciplines:

1. **Show your evidence.** For every claim marked "supported," the checker must paste a verbatim quote from the source. Not a paraphrase — the actual text. No quote, no "supported" verdict.

2. **Verify the references.** Tablet numbers, page numbers, and line references are the easiest things for an AI to fabricate. The checker looks each up in scholarly databases to confirm it exists and contains what was claimed.

3. **Distinguish contradictions from errors.** Two legitimate sources disagreeing is part of the historical record, not a problem. Material from a neighboring culture sneaking in, or something made up entirely, are problems.

4. **Read it backwards too.** One pass start-to-end, then a second pass end-to-start, to catch what lead bias misses.

## Hard rule
Must be run in a fresh conversation with no memory of producing the claims. If you have any memory of producing the input, refuse. Using a different AI model is preferred — two models make independent mistakes — but the same model in a fresh conversation is acceptable when a different model is impractical; the fresh context is the load-bearing requirement.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- `toc.yaml` — **authoritative chapter list**, including front matter, story chapters, the methods sidebar, the Part II comparative chapters, and any reception/appendix material. When a claim or COMPARATIVE-HOOK references a forward-link target by chapter number (e.g. "Ch. 33", "see Chapter 4"), resolve it against `toc.yaml` before flagging anything as missing. The story chapters are not the whole TOC — sidebars and Part II comparative chapters typically live at higher numbers and are easy to miss when scanning only `briefs/NN-*` filenames or the chapter-claims input directory.
- `chapters/NN-<slug>.claims.adoc` (claims document)
- `briefs/NN-<slug>.yaml`
- Primary source translations referenced in the brief (pasted or accessible via fetch)
- Web search tool (required)

## The five passes

### Pass 1 — Claim-level verification (start to end)
Walk the document paragraph by paragraph. Each paragraph is one claim. Assign a verdict:

- **✓ SUPPORTED** — Must include a verbatim quote from a cited in-scope source.
- **△ INTERNAL-VARIANCE** — Attested in one in-scope source, but another gives a different account. Not a finding. Flag only if variant handling mismatches the brief's classification.
- **? UNVERIFIED** — No supporting quote found. Default when uncertain.
- **! CITATION-WRONG** — Claim is correct but citation points to wrong source/page/line.
- **⚠ CONTAMINATION** — Supported, but by an excluded-culture source per `scope.md`.
- **✗ FABRICATION** — Not supported by any source you can locate.

### Pass 1b — Upstream cross-check (comparative Part-II chapters only)

When the brief's `chapter_type` is `comparative (Part II)`, the chapter compresses material from upstream Part-I chapters listed in `chapters_drawn_from`. The canonical truth for those facts is the upstream `chapters/MM-<slug>.claims.approved.adoc`, not the writer's paraphrase or the brief's drafting language.

For every per-tradition compression in the chapter:

1. Open the upstream `chapters/MM-<slug>.claims.approved.adoc` for that tradition.
2. Locate the specific fact the chapter is compressing — verse number, section number, character epithet, source loc, naming convention.
3. Compare. If the chapter's `source_id` or `loc` differs from the upstream, flag CITATION-WRONG (severity LOW for digit-transposition or near-misses, MEDIUM for substantive differences such as wrong verse number or wrong section number). If a character name, epithet, or terminology drifts from the upstream's locked rendering, flag ATTRIBUTION-DRIFT (MEDIUM).
4. Record the disposition with a verbatim-substitutable fix from the upstream file.

This pass catches the recurring failure mode in which the writer paraphrases per-tradition material from memory or from the brief's drafting language rather than from the upstream chapter — Hoffner section numbers, Vedic verse numbers, Hittite-vs-Hurrian storm-god names, character epithets, and corpus-listing conventions are the canonical examples.

### Pass 2 — Triangulation of references
Verify each citation's tablet number, line range, or page reference resolves in a `triangulation_databases` entry. Non-resolving: CITATION-WRONG, HIGH severity, with verification URL.

For cross-chapter references inside the book (claims that say "see Ch. N", COMPARATIVE-HOOK targets like "Part II C5", forward-links to the methods sidebar): resolve against `toc.yaml`, not against the directory of `briefs/NN-*` files. The TOC is authoritative; the briefs directory is not exhaustive (Part II comparative chapters and the methods sidebar live at numbers above the last story chapter). Only flag a forward-link as missing when `toc.yaml` does not list a chapter at that number or with that anchor.

**Identifier verification on recently-pinned sources.** When `sources.yaml` shows a source added or last edited recently (typically a chapter-briefs source-pinning round), web-verify the published identifier against AbeBooks / WorldCat / publisher catalogue / archive.org. Common failure modes:
- ISBN digit-transposition (e.g. `9789561109315` for what should be `9789561109124`).
- ISBN belongs to a different edition of the same work (hardcover vs. paperback; reprint vs. first printing).
- ISBN/publisher mismatch — ISBN comes from publisher A but the entry attributes the work to publisher B.
- OCLC number guessed rather than verified; correct value is a different WorldCat record.
- archive.org URL slug malformed; correct slug is different.
- For older works without ISBNs (pre-1970, especially): year, publisher, and series number all need print-copy or library-catalogue verification.

Flag mismatches as CITATION-WRONG, severity LOW (digit-transposition) to MEDIUM (wrong edition / wrong publisher / wrong year). Include the verified-correct value in the `recommended_fix`. These are actionable at `post-human-normalize` via identifier-correction-in-place — do NOT defer to inventory-audit.

### Pass 3 — Document-provenance contamination scan
For each factual detail: is this detail attested in a document within the scope's date range and culture? Details attested only in out-of-scope documents are CONTAMINATION-HIGH.

### Pass 4 — Marker integrity
- `[INFERENCE:]` — genuinely inferential? If a source directly attests it, flag MARKER-MISUSED. Schema: `[INFERENCE: <claim> | basis: ... | risk: ...]`.
- `[SPECULATION:]` — genuinely the chapter author's interpretive reading (not a derivation from the upstream that should be `[INFERENCE:]`)? Schema is locked: `[SPECULATION: <claim> | basis: ... | counterargument: ...]`. Third pipe-field must be `counterargument:` with a substantive opposing position — if labelled `warrant`, `risk`, `speculative_basis`, or any synonym, flag MARKER-SCHEMA-WRONG (MEDIUM). If the `counterargument:` field carries only a methodological caveat or a restatement of the basis, flag MARKER-COUNTERARGUMENT-WEAK (LOW or MEDIUM depending on materiality).
- `[LACUNA:]` — source actually has the claimed gap?
- `[RECONSTRUCTION:]` — fill source is in-tradition per `scope.md`?
- `[VARIANT:]` — both quoted phrases present in cited sources?
- `[APPROPRIATION-FLAG:]` — when present, verify all four required components: substance of the area-specialist objection; named specialists framing the material outside the comparative typology; tier-implication clause; forwards-to clause naming the comparative chapter(s) where the objection is engaged at length. Verify named specialists are either in `sources.yaml` OR handled via the named-but-flagged pattern (no EVIDENCE token routes through them, and they are flagged in the writer's completion record for inventory-audit). The marker is required only when `scope.md`'s appropriation protocol applies; if present in a chapter that doesn't trigger the protocol, flag MARKER-MISUSED.
- **Silent bridges** — uncited claims not under a marker. Flag SILENT-BRIDGE, HIGH.

**Named-but-flagged pattern verification.** When body prose or marker text names a scholar (e.g. "Hale, Bird, and Levtzion read the cycle within the registers of Mande oral-epic performance") whose specific publication is not in `sources.yaml`, the pattern is acceptable IF AND ONLY IF no EVIDENCE token routes through that scholar's work. Verify: walk every EVIDENCE token's `source_id` against the named scholars; any match is a finding (the scholar IS load-bearing on a specific claim and must be added to `sources.yaml` rather than named-but-flagged). Acceptable named-but-flagged usage is captured as NOTE in the factcheck output and forwarded to the writer's completion record for inventory-audit follow-up — not flagged as a finding.

### Pass 5 — Reverse-order second pass
Walk from last claim to first. Add any new findings.

**Glossary**: check consistency. **Style**: not checked — there is no prose yet.

## Output: `chapters/NN-<slug>.claims.factcheck.yaml`

```yaml
meta:
  auditor_model: <name and version>
  auditor_conversation_id: <conversation ID if available>
  input_file: <path>
  claims_identified: <n>
  triangulations_performed: <n>
  verdict: PASS | REVISE | MAJOR-REVISE

tallies:
  supported: <n>
  internal_variance: <n>
  unverified: <n>
  citation_wrong: <n>
  contamination: <n>
  fabrication: <n>
  silent_bridges: <n>
  marker_issues: <n>
  glossary_violations: <n>

supported_claims:
  - claim_number: <n>
    claim: "<the claim>"
    source_id: <from sources.yaml>
    source_loc: <tablet/line/page>
    verbatim_quote: "<exact text from source>"

findings:
  - claim_number: <n>
    kind: UNVERIFIED | CITATION-WRONG | CONTAMINATION | FABRICATION | SILENT-BRIDGE | MARKER-MISUSED | MARKER-FABRICATED | GLOSSARY-VIOLATION | VARIANT-HANDLING-MISMATCH
    severity: HIGH | MEDIUM | LOW
    claim: "<the claim>"
    issue: <one sentence>
    evidence: <verbatim quote or triangulation URL>
    recommended_fix: <concrete>
```

## Verdict rules

Apply in order (first match wins):
- **MAJOR-REVISE**: ≥ 3 HIGH findings, or any contamination, or triangulation failures indicating fabricated references.
- **REVISE**: 1–2 HIGH, or > 3 MEDIUM, or any silent bridge.
- **PASS**: zero HIGH, zero silent bridges, ≤ 3 MEDIUM.

## Honesty self-check
Answer in `meta`:
1. Did I open every cited primary source, or skim? Name any I skimmed.
2. Did I triangulate every reference, or assume some? Name any assumed.
3. For every ✓, did I paste a real quote or pattern-match? Downgrade any pattern-matched.
4. Did I distinguish internal variance from contamination?
5. Am I the same model that produced the claims? If yes, this audit is invalid.

## Human review protocol
Review HIGH findings (~10 minutes), skim MEDIUM. Apply accepted fixes to produce `chapters/NN-<slug>.claims.approved.adoc`. Run `post-human-normalize` before proceeding to `chapter-draft`.

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
After human review and normalization: `chapters/NN-<slug>.claims.approved.adoc` to `chapter-draft`.
