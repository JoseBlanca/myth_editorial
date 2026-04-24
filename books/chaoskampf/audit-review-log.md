# Audit review log — inventory audit (2026-04-23)

The `inventory-audit.yaml` produced on 2026-04-23 flagged 6 HIGH, 9 MEDIUM, 5 LOW findings across 42 story entries. The user was not available to review the findings; this log records what was accepted, applied, and deferred per the standing instruction to proceed autonomously.

## HIGH findings — all accepted and applied (mechanical ISBN / URL corrections)

| Finding | Where fixed | Change |
|---|---|---|
| Aune *Revelation* WBC — wrong ISBN | `inventory.approved.yaml` revelation-12-dragon entry; `sources.yaml` aune-revelation | `9780849902536` → `9780849902512` |
| Matos Moctezuma *Great Temple* — wrong ISBN | `inventory.approved.yaml` huitzilopochtli-coatepec entry; `sources.yaml` matos-moctezuma-templo-mayor | `9780500390160` → `9780500390245` |
| López Austin *Myths of the Opossum* — wrong ISBN (affects 3 story entries) | `inventory.approved.yaml` cipactli, quetzalcoatl-tezcatlipoca, huitzilopochtli-coatepec; `sources.yaml` lopez-austin-myths | `9780826313980` → `9780826313942` |
| Annus 2001 *Anzu Epic* — wrong ISBN | `inventory.approved.yaml` ninurta-anzu entry; `sources.yaml` annus-2001-anzu | `9789514590535` → `9789514590511` |
| Siikala 2002 FFC 280 — wrong ISBN | `inventory.approved.yaml` vainamoinen-iku-turso entry; `sources.yaml` siikala-finnish | `9789514110214` → `9789514109027` (hardback ISBN) |
| Scurlock & Beal 2013 — wrong ISBN | `sources.yaml` scurlock-beal-2013 | `9781575062532` → `9781575062792` |

## MEDIUM findings — applied where mechanical; deferred where design

| Finding | Action | Rationale |
|---|---|---|
| Wakeman 1973 ISBN wrong (`9789004035973` → `9789004037526`) | Applied in `inventory.approved.yaml` and `sources.yaml` | Mechanical correction; same-day fix rather than deferring. |
| Beckman 1982 JANES PDF URL 404s | Changed to `https://janes.scholasticahq.com/` (stable journal root) in both files | The specific PDF path is no longer served by JTSA; the journal archive root is stable. A direct DOI can be pinned at chapter-briefs. |
| Missing: Song of Hedammu (Hurro-Hittite) | Explicit sub-variant of kumarbi-ullikummi, not a new entry | Per scope.md §"variant presentation" and the "family chapter" design: Hedammu is a companion text within the Kumarbi Cycle. Naming it in `variants` resolves the silent-conflation concern without inflating CORE. |
| Missing: Song of the Sea (Hurro-Hittite) | Same as above | Same rationale. Both songs are now named in the kumarbi-ullikummi `variants` field with a note that the chapter treats them as side-by-side sub-sections, not as a single undifferentiated narrative. |
| Silent-conflation warning on yhwh-leviathan-rahab | Existing `variants` field already names the Pss/Isa/Job/Hab sub-corpus. No change. | The scope.md variant-presentation policy explicitly supports bundling a single-tradition corpus when one tier is clearly primary. The chapter will present sub-corpus attestations side by side. |
| Silent-conflation warning on ra-apep | Existing `variants` field already names the BoD / Amduat / Book of Gates / Bremner-Rhind strata. No change. | Same as above: the breadth across 2000 years is the point of the cyclical-maintenance subtype, not a conflation. |
| Inclusion-test marginal: horus-seth (non-serpentine adversary) | Kept RELATED; added `[INCLUSION-MARGINAL]` framing marker in notes. Chapter must flag the edge-case status explicitly. | te Velde is the scholarly anchor for treating Horus/Seth alongside Ra/Apep. Dropping it would lose the Egyptian family-chapter's internal comparison. |
| Inclusion-test marginal: erlik-ulgen (non-serpentine adversary) | Kept RELATED; added `[INCLUSION-MARGINAL]` framing marker. | Eliade/Harva treat it as a dualistic-cosmology comparandum; useful counterpoint in the IE-reflexes cluster. Framing as "not strictly a serpent-combat" is load-bearing for the chapter. |
| Hallowell 1960 ISBN (LOW) | Not fixed in this round | LOW severity; per the skill's human-review protocol, LOW findings are ignored unless maximum rigor is demanded. Flagged for chapter-briefs pass. |

## User-judgment questions from the auditor — autonomous answers

| Question | Decision | Rationale |
|---|---|---|
| Split kumarbi-ullikummi so Hedammu / Song of the Sea become CORE? | Keep bundled. | The scope's "family chapter" structure and the Hittite cycle's internal coherence argue for one CORE chapter on the Kumarbi Cycle with Hedammu and Song of the Sea as named sub-sections. Splitting would produce three thin CORE chapters that duplicate framing. User can reverse this at chapter-briefs if they prefer. |
| Retain horus-seth in RELATED, or move to contrastive/sidebar? | RELATED with framing marker. | te Velde's treatment is explicitly inside the Egyptian chaoskampf discussion; demoting it would lose the scholarly anchor. Framing marker is sufficient. |
| Retain erlik-ulgen in RELATED, or move? | RELATED with framing marker. | Eliade and Harva are the only serious scholarly anchors; the RELATED tier is the correct home with an inclusion-marginal flag. |
| Split yhwh-leviathan-rahab by sub-corpus (Pss 74, Isa 27, Job 26, Job 41)? | Keep bundled. | Day 1985 (the scholarly anchor) treats them as a single tradition with sub-witnesses. One CORE chapter that presents the sub-corpus side by side matches the scope's variant-presentation policy. |

## Open items flagged for the user (soft — no blocking)

- None of the accepted changes alter the book's structure. All remain within the scope.md locked 2026-04-23.
- If the user returns and wants Kumarbi Cycle or YHWH/Leviathan-Rahab split, it is a 10-minute edit at chapter-briefs time.
- Hallowell 1960 ISBN and a few other LOW-severity points remain flagged in `inventory-audit.yaml`.

## Next pipeline steps triggered

1. `post-human-normalize` on `inventory.approved.yaml` (validates yaml structure, required fields, source references).
2. `chapter-briefs` — producing one brief per chapter + `toc.yaml`.
3. Pause before `glossary-lock` (interactive with the user) — I will leave a draft `glossary.yaml` seeded with the recurring technical terms pulled from the research notes, ready for the user to confirm on return.
