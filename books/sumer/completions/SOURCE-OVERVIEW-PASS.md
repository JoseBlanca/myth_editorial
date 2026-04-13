# Source Overview Pass

After claims-factcheck is complete and findings are applied, run a separate pass
to add `=== Source overview` sections to all 36 claims files.

## When to run
After: claims-factcheck + human review + post-human-normalize
Before: chapter-draft

## What to do
For each `chapters/NN-<slug>.claims.approved.adoc`, prepend a `=== Source overview`
section with 3-6 claims about the physical artifacts, drawing from the brief's
`sources` and `lacunae` fields. Each claim cited with footnote + evidence token.

## Can be batched
Same batching strategy as claims-factcheck (6 batches of 6 chapters).
