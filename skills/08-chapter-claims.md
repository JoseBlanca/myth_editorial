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
2. Use exactly the English renderings locked in `glossary.yaml`. If a needed term is missing, stop and ask.
3. Omit material from excluded cultures. Note the temptation in a `// COMPARATIVE-HOOK:` comment for the comparative chapter.
4. One claim per paragraph. No bundling. No narrative connective tissue.

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

## Ordering

Follow the narrative order of the myth as attested in the primary source(s). Where the brief specifies an ordering (e.g., following the tablet sequence), follow it. The claims should form a complete, ordered skeleton of the story — everything the narrative will need.

## Variant handling (from brief)

- If `variants.classification` is **single-prevalent**: list claims from the prevalent version. Add separate claims for each significant alternate, marked with `[VARIANT:]`.
- If **co-equal**: list claims from each version in sequence, each attributed to its source.

## Markers (required sub-fields)

Same markers as the rest of the pipeline, but used at the claim level:

- `[INFERENCE: <claim> | basis: <why this bridge is reasonable> | risk: <what is speculative>]`
  — A claim that bridges two attested claims. Needed to make the story skeleton coherent, but not directly attested. The fact-checker will verify the inference is genuinely inferential (not secretly attested) and that the basis is sound.
- `[LACUNA: <what is missing> | source: <exact ref> | scholarly_reconstruction: <if any, with citation>]`
  — A documented physical gap in the source.
- `[RECONSTRUCTION: <filled content> | gap_source: <where the lacuna is> | fill_source: <which in-tradition source supplies the content, per scope.md's reconstruction policy> | confidence: high|medium|low]`
  — Content filled from another in-tradition source per the reconstruction policy.
- `[VARIANT: primary=<source A, short quote> | alt=<source B, short quote> | chosen: A|B | reason: <why>]`
  — For single-prevalent cases. Co-equal variants are listed as separate attributed claims without a marker.

## Comparative hooks

End the claims document with a section of `// COMPARATIVE-HOOK:` comments collecting cross-cultural parallels noticed during the claim extraction. These are not claims — they are notes for the comparative chapter.

## Output: `chapters/NN-<slug>.claims.adoc`

```asciidoc
== <Chapter Title> — Claims

// This is a claims document, not final prose. Each paragraph is one verifiable claim.
// After fact-check and human review, chapter-draft will transform this into narrative.

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

// COMPARATIVE-HOOK: <detail for comparative chapter>
// COMPARATIVE-HOOK: <detail for comparative chapter>
```

## Self-check before returning
1. Every claim is a single factual assertion — no bundled claims, no narrative connective tissue.
2. Every claim has footnote coverage citing a source provided in this conversation. Nothing from memory.
3. Claims follow the narrative order of the myth.
4. The claims skeleton is complete — everything the narrative will need is here.
5. Every marker has all required sub-fields.
6. No out-of-scope material.
7. Variant handling matches the brief's classification.
8. `glossary.yaml` renderings used throughout.

## Handoff
To `claims-factcheck`, fresh conversation, different model. The fact-checker's job is dramatically simplified: each claim is isolated and individually cited.
