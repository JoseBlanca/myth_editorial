# Grammar-check diff: Chapter 11 — Inanna and Ebih

Every change made to `11-inanna-and-ebih.resolved.adoc` to produce `11-inanna-and-ebih.grammar-checked.adoc`. Each entry shows the original and corrected text with a short rationale. No factual content, footnotes, EVIDENCE comments, COMPARATIVE-HOOK comments, AsciiDoc structure, or marker-resolved passages were altered.

## Change 1 — Dangling participial modifier on "classifying" (Line 3)

**Original:**
> The numerous consistent Old Babylonian copies produce a stable composite text with minimal significant variation, classifying it as single-prevalent.

**Corrected:**
> The numerous consistent Old Babylonian copies produce a stable composite text with minimal significant variation, and the text is classified as single-prevalent.

**Rationale:** The participle "classifying" dangles — its implied subject is the main-clause subject ("copies"), but copies do not classify a text; scholarly convention does. The existing companion-chapter construction ("The text is classified as single-prevalent-reconstructed", chapter 10) uses exactly this passive. The fix converts the trailing participial phrase into a coordinate clause with an explicit subject ("the text is classified"), removing the dangling modifier without changing any factual content: the chain of claims (stable composite text → single-prevalent classification) is preserved in the same order and with the same agency.

## Change 2 — Appositive attached to the wrong noun (Line 92)

**Original:**
> In the Greek tradition, Athena's martial independence -- the goddess who defies patriarchal counsel and triumphs through her own power and judgment -- offers a structural parallel to Inanna's rejection of An's authority, though again the cultural frameworks diverge.

**Corrected:**
> In the Greek tradition, Athena -- the goddess who defies patriarchal counsel and triumphs through her own power and judgment -- displays a martial independence that offers a structural parallel to Inanna's rejection of An's authority, though again the cultural frameworks diverge.

**Rationale:** The em-dashed appositive "the goddess who defies patriarchal counsel…" describes a goddess, but in the original it sits immediately after "Athena's martial independence" — i.e., it is grammatically attached to "independence" (an abstraction), not to Athena. The reader must re-parse to route the appositive to its logical antecedent. The fix promotes "Athena" to head noun of the subject and demotes "martial independence" to the predicate ("displays a martial independence that…"), so the appositive now sits next to the correct antecedent. Every factual claim is preserved: Athena defies patriarchal counsel, triumphs through her own power and judgment, and her martial independence offers a structural parallel to Inanna's rejection of An's authority. The concessive tail about cultural frameworks is unchanged.

---

## Self-check

- **Factual content:** Unchanged. The classification of ETCSL 1.3.2 as single-prevalent, the character of its Old Babylonian copy tradition, Athena's defiance of patriarchal counsel, her reliance on her own power and judgment, and the structural parallel to Inanna's rejection of An's authority all survive intact.
- **Footnotes:** All 22 `footnote:[…]` markers preserved with identical content. All 25 EVIDENCE comments and all 3 COMPARATIVE-HOOK comments preserved verbatim.
- **Marker-resolved passages:** The italic parenthetical inference block on line 50 (Inanna's defiance of An / inference + risk statement, including the intentional ".." marker punctuation) and the italic bracketed lacuna block on line 65 (tablet break at lines 140–155) were left untouched.
- **AsciiDoc structure:** The `==` heading, all `'''` section breaks, italic/emphasis markup (`_me_`, `_me-lam_`, `_edubba_`, `_abzu_`), em-dash punctuation, and all line breaks around evidence comments are intact. Line count is identical (98 lines) in input and output.
- **No silent changes.** Only the two changes above were made.
