---
name: chapter-claims
description: Produces the factual skeleton of a single chapter — one fact per paragraph, each with its own citation. This is step 1 of a two-step writing process: first the facts are written and verified, then the narrative prose is created from the verified facts.
---

# chapter-claims

## For the human

This is the first half of a deliberate split between "getting the facts right" and "writing beautiful prose."

Instead of asking the AI to write flowing Asimov-style narrative and then trying to check the facts buried inside it, we write the facts first — one per paragraph, each with its own source reference — and only write the narrative after the facts have been verified.

Why this matters: when an AI writes a beautiful paragraph of narrative prose, it is simultaneously researching, citing, connecting, and styling. These tasks interfere with each other. The AI fills gaps to smooth transitions, reaches for evocative phrasing that drifts from the source, and buries factual claims in connective tissue that makes them hard to check. By separating the factual skeleton from the prose, we let the AI do one job at a time, and we give the fact-checker a document where each paragraph is a single, individually cited claim — trivially easy to verify compared to extracting claims from flowing prose.

The output of this stage is not text the reader will ever see. It is a verified blueprint — a list of numbered facts — that the next stage (`chapter-draft`) will transform into the final narrative.

## Hard rules
1. Cite only sources whose text has been provided to you in this conversation or fetched by you via tool use. No citing from memory, even confidently.
2. **Never invent a source ID.** Every `source_id` in an EVIDENCE token must resolve to an existing entry in `sources.yaml`. If the brief's `sources.primary` list is empty or names sources that aren't in `sources.yaml`, run the pre-flight check below and STOP. Do not work around the block by routing EVIDENCE tokens through the brief filename, an inventory entry, or a placeholder ID. (For scholars who need to be credited but have no `sources.yaml` entry yet, use the named-but-flagged pattern below — that is the supported workaround.)
3. Use exactly the English renderings locked in `glossary.yaml`. Before italicising any foreign-language common noun or using any glossed proper noun, grep `glossary.yaml` for the locked rendering — body-prose terminology drifts from the glossary easily and the grep takes a second. If a needed term is missing, stop and ask.
4. Omit material from excluded cultures. Note the temptation in a `// COMPARATIVE-HOOK:` comment for the comparative chapter.
5. One claim per paragraph. No bundling. No narrative connective tissue.

## Pre-flight check

Before producing any claims, verify the brief is complete:

1. `briefs/NN-<slug>.yaml` exists and is structurally valid.
2. `sources.primary` is non-empty AND every entry has an `id` that resolves to `sources.yaml`.
3. There is no `primary_sources_to_pin_at_glossary_lock` block, no `# identifier_missing: true` comment in the sources block, and no other deferral language saying the brief is in a partially-pinned state.

If any of these fails, STOP. Do NOT proceed. Surface the block to the human with a one-paragraph diagnostic naming which check failed and what would unblock it (typically: chapter-briefs needs to do its source-pinning step). The chapter-claims stage is downstream of source-pinning and cannot do its own; attempting to work around the block by inventing source IDs is the canonical failure mode and produces output that must be discarded.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- One chapter brief (`briefs/NN-<slug>.yaml`)
- Primary source translations — pasted into the conversation or accessible via fetch

## What is a claim?

A claim is a single factual assertion about the myth: who did what, when, why, in what order, with what consequence. Each of the following is a separate claim:

- An event ("Inanna descended to the underworld")
- A character identification ("Ereshkigal was Inanna's sister and queen of the underworld")
- A causal relationship ("Inanna was detained because she violated the laws of the underworld")
- A physical description ("The text describes Enkidu as hairy-bodied")
- A ritual or cultural detail ("The myth was recited during the Akitu festival")
- A scholarly observation ("The tablet is broken at this point; approximately 20 lines are lost")

A narrative transition ("Having secured the divine powers, Inanna turned her attention to the underworld") is **not** a claim — it is connective tissue that belongs in `chapter-draft`, not here.

## Structure of a claim paragraph

Each paragraph contains exactly:
1. **The claim** — one factual assertion, in plain language.
2. **The citation** — AsciiDoc footnote for the reader, pointing to the specific source, location, and (where possible) a verbatim quote or close paraphrase from the source.
3. **The evidence token** — a machine-readable comment on the line after the claim, for automated bibliography building and validation.

```
Enlil separated heaven (An) from earth (Ki), creating the space in which the atmosphere exists.footnote:[Black et al. 2004, ETCSL 1.1.2, lines 1–5: "After heaven had been moved away from earth, after earth had been separated from heaven, after the name of man had been fixed..."]
// EVIDENCE: source_id=black2004 ; loc=ETCSL 1.1.2, lines 1-5
```

The footnote is for the reader. The evidence token is for the machine. `format-finalize` builds the bibliography from evidence tokens, not from parsing footnote prose — this avoids ambiguity between bibliographic and editorial footnotes.

## Source overview section

Before the narrative claims, begin with a `=== Source overview` section. This grounds the reader in the physical evidence — the actual artifacts, documents, or traditions through which we know this story. Each claim in this section is a factual assertion about a source, not about the myth's content.

Include claims covering:
1. **What survives.** Name the specific tablets, manuscripts, or attestations (with museum numbers or corpus IDs where known). How many witnesses exist? From which sites?
2. **State of preservation.** Is the text complete, fragmentary, or heavily damaged? Where are the major gaps?
3. **Composite or single witness?** Is the "text" scholars read a composite stitched from many tablets, or does it survive on a single artifact?
4. **Discovery context.** When and where was the primary tablet found, if known? (e.g., "recovered from the Nippur scribal quarter during the University of Pennsylvania excavations")
5. **Scholarly edition.** Which critical edition or translation is the basis for this chapter?

This section is factual and citeable — every claim about a tablet's provenance, museum number, or preservation state must have a footnote. It feeds directly into the chapter-draft's opening passage, which orients the reader before the story begins.

## Comparative chapters (Part II)

When the brief's `chapter_type` is `comparative (Part II)`, the chapter compresses material from upstream Part-I chapters listed in the brief's `chapters_drawn_from`. Two disciplines apply on top of the rest of this skill:

### Upstream-lookup rule

For every per-tradition compression in §I, §II, §III, or anywhere material is paraphrased from an upstream Part-I chapter:

1. Open the upstream `chapters/MM-<slug>.claims.approved.adoc` for that tradition.
2. Locate the specific fact you are about to compress — verse number, section number, character epithet, source loc, naming convention, etc.
3. Route the EVIDENCE token through the same `source_id` and the same `loc` value the upstream uses.
4. Use the upstream's character names, epithets, and terminology verbatim. The brief may use loose terminology and the upstream is canonical: e.g., the Hittite storm-god of CTH 321 is **Tarḫunna** (Hittite), not Teshub (the Hurrian counterpart used in non-Illuyanka material); the Vedic *áhann áhim* formula falls in **RV 1.32.2** (the second verse), not 1.32.1; Ninurta is the **warrior-god of Nippur**, not its lord (which is Enlil's title).

This rule prevents the compression-from-memory failure mode (verse-number errors, section-number errors, epithet drift, terminology slips) that the factcheck stage would otherwise have to clean up.

### Doubled-token discipline

Comparative claims that bridge in-scope and out-of-scope material — transmission claims, structural-parallel claims, IE-inheritance claims, "as established in Ch. M" cross-references — should carry **two EVIDENCE tokens** on the same paragraph: an area-specialist anchor for the per-tradition fact and a comparative-mythology anchor for the typological reading. Single-token paragraphs are appropriate where a single source genuinely covers the claim (the chapter's own framing claims, brief-references, methodology anchors).

## Ordering

Follow the narrative order of the myth as attested in the primary source(s). Where the brief specifies an ordering (e.g., following the tablet sequence), follow it. The claims should form a complete, ordered skeleton of the story — everything the narrative will need.

## Variant handling (from brief)

- If `variants.classification` is **single-prevalent**: list claims from the prevalent version. Add separate claims for each significant alternate, marked with `[VARIANT:]`.
- If **co-equal**: list claims from each version in sequence, each attributed to its source.

## Markers (required sub-fields)

Same markers as the rest of the pipeline, but used at the claim level:

- `[INFERENCE: <claim> | basis: <why this bridge is reasonable> | risk: <what is speculative>]`
  — A claim that bridges two attested claims. Needed to make the story skeleton coherent, but not directly attested. The fact-checker will verify the inference is genuinely inferential (not secretly attested) and that the basis is sound.
- `[SPECULATION: <claim> | basis: <evidence supporting the reading> | counterargument: <substantive opposing position>]`
  — A reading the chapter advances as its own analytical framing, distinct from `[INFERENCE:]` (which bridges between upstream attestations). Used principally in comparative (Part II) chapters where the chapter offers a typological reading or transmission-vs-typology judgement that goes beyond what any single upstream source attests. The `counterargument:` field must carry a substantive opposing position, not a methodological caveat or a restatement of the basis. Schema is locked: `basis:` / `counterargument:` — not `warrant`, `risk`, or `speculative_basis`.
- `[LACUNA: <what is missing> | source: <exact ref> | scholarly_reconstruction: <if any, with citation>]`
  — A documented physical gap in the source.
- `[RECONSTRUCTION: <filled content> | gap_source: <where the lacuna is> | fill_source: <which in-tradition source supplies the content, per scope.md's reconstruction policy> | confidence: high|medium|low]`
  — Content filled from another in-tradition source per the reconstruction policy.
- `[VARIANT: primary=<source A, short quote> | alt=<source B, short quote> | chosen: A|B | reason: <why>]`
  — For single-prevalent cases. Co-equal variants are listed as separate attributed claims without a marker.
- `[APPROPRIATION-FLAG: <substance of the area-specialist objection> | named_specialists: <scholars who frame the material outside the comparative typology being applied> | tier_implication: <how the objection bears on the chapter's tier classification — e.g., "milder than Ch23 Naumann objection; comparable to Ch26 wak'a-succession reading"> | forwards_to: <comparative chapter(s) where the objection is engaged at length, with explicit ordinal numbers>]`
  — For non-Eurasian or area-specialist-contested cases where the comparative framing being imposed by the book is itself questioned by the area's scholarly tradition. Used when the chapter must hold its comparative engagement with the typology ALONGSIDE the area-specialist objection, rather than imposing the typology unilaterally. Required only when `scope.md`'s appropriation protocol applies to the chapter (typically signaled by the brief's `chapter_type` being non-Eurasian related-tier or contrastive-tier, or by the brief explicitly naming an area-specialist tradition that resists the framing). Use the named-but-flagged pattern (below) for specialists named in the marker who are not in `sources.yaml`.

## Named-but-flagged pattern (for non-anchored scholars)

Sometimes the chapter needs to NAME a scholar in body prose or inside a marker — for credit, for area-specialist disclosure, or to register that a particular reading has multiple proponents — without anchoring an EVIDENCE token through their work because their specific publication is not (yet) in `sources.yaml`.

The supported pattern:
1. Name the scholar in body prose or inside the marker. Do not route any EVIDENCE token through them.
2. Anchor the substantive claim through an existing source whose work covers it.
3. In the completion record's `notes`, list every named-but-flagged scholar with the publication that should be added at inventory-audit (title + year + publisher if known).

This is the explicit alternative to inventing a source ID. Inventing source IDs is forbidden (see Hard rules); naming-without-anchoring is the supported workaround. It is appropriate for: (a) area-specialists named at an APPROPRIATION-FLAG marker; (b) precursor or supplementary scholars named alongside the principal anchor in a footnote; (c) scholars whose work covers the material but whose specific edition cannot be confirmed at this stage.

## Comparative hooks

End the claims document with a section of `// COMPARATIVE-HOOK:` comments collecting cross-cultural parallels noticed during the claim extraction. These are not claims — they are notes for the comparative chapter.

## Output: `chapters/NN-<slug>.claims.adoc`

```asciidoc
== <Chapter Title> — Claims

// This is a claims document, not final prose. Each paragraph is one verifiable claim.
// After fact-check and human review, chapter-draft will transform this into narrative.

=== Source overview

<Claim about physical artifacts — tablets, museum numbers, sites of discovery.>

<Claim about state of preservation — complete, fragmentary, lacunae.>

<Claim about the composite nature of the text, if applicable.>

<Claim about the critical edition or translation used as basis.>

=== Setting and context

<Claim 1 — one paragraph, one citation.>

<Claim 2 — one paragraph, one citation.>

=== Narrative sequence

<Claim 3>

[LACUNA: <...>]

<Claim 4>

[INFERENCE: <...>]

<Claim 5>

=== Variants

[VARIANT: <...>]

<Alternate claim from different source>

=== Typology and area-specialist framing  // only when scope.md's appropriation protocol applies

[APPROPRIATION-FLAG: <...>]

// COMPARATIVE-HOOK: <detail for comparative chapter>
// COMPARATIVE-HOOK: <detail for comparative chapter>
```

## Self-check before returning
1. The pre-flight check passed (brief complete; no source-pinning deferral).
2. Every `source_id` in every EVIDENCE token resolves to an existing entry in `sources.yaml`. Zero invented IDs.
3. The `=== Source overview` section is present and contains at least 3 claims about the physical artifacts, preservation state, and scholarly edition.
4. Every claim is a single factual assertion — no bundled claims, no narrative connective tissue.
5. Every claim has footnote coverage citing a source provided in this conversation. Nothing from memory.
6. Claims follow the narrative order of the myth.
7. The claims skeleton is complete — everything the narrative will need is here.
8. Every marker has all required sub-fields. If an `[APPROPRIATION-FLAG:]` is present, all four required components are filled.
9. Any scholar named in body prose or inside a marker without a corresponding `sources.yaml` entry is handled via the named-but-flagged pattern (no EVIDENCE token routes through them) and listed in the completion record's `notes` for inventory-audit follow-up.
10. No out-of-scope material.
11. Variant handling matches the brief's classification.
12. `glossary.yaml` renderings used throughout — verified by grepping the glossary for every foreign term that appears italicised in body prose.
13. Foreign-language common nouns in body prose use AsciiDoc italic (`_term_`), not bold (`*term*`). Asterisk-bold occurrences are acceptable only inside footnotes, EVIDENCE tokens, COMPARATIVE-HOOK comments, and marker contents (which carry through later stages verbatim).
14. Every `[SPECULATION:]` block uses the locked schema `[SPECULATION: <claim> | basis: <text> | counterargument: <text>]`. The third pipe-field is `counterargument:` — not `warrant`, `risk`, `speculative_basis`, or any synonym — and supplies a substantive opposing position rather than a methodological caveat.
15. (Comparative Part II chapters only.) Every per-tradition compression has been verified against the corresponding upstream `chapters/MM-<slug>.claims.approved.adoc` — character names, epithets, verse numbers, section numbers, and source locs match the upstream verbatim. Doubled-token paragraphs cover transmission and structural-parallel claims.

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
To `claims-factcheck`, in a fresh conversation (a different AI model is preferred but not required). The fact-checker's job is dramatically simplified: each claim is isolated and individually cited.
