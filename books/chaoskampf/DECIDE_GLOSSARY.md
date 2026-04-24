# DECIDE_GLOSSARY — Chaoskampf Across Cultures

**Status (2026-04-24):** All items resolved by user. `glossary.yaml` has been updated to reflect these decisions (version bumped to `v1-locked`, status `user-confirmed`). The original analysis for each item is preserved below with the final decision appended as **DECISION** at the end of each section.

---

## Summary of decisions

1. **Strict reading** — "combat myth" in body prose; "Chaoskampf" only in headings, quotations, and Gunkel-thesis discussions.
2. **Aži Dahāka** (option A, draft) — diacritical form throughout; Zahhāk only flagged in Shāhnāmeh contexts.
3. **Yahweh** — vocalised form in body prose (reader-friendly for sustained narrative); YHWH may still appear in direct quotation.
4. **Ea / Enki** (option A, draft) — language-context-conditional; form follows the language of the primary text.
5. **Mishipeshu** (draft) — most common in current English-language scholarship.
6. **Nanabozho** (draft, Hallowell) — stick to one; follow the lead specialist for the chapter.
7. **wak'a** — modern Quechua orthography; reader unfamiliarity with the older "huaca" is not a blocker.
8. **Krishna** (draft) — reader familiarity; Kṛṣṇa reserved for philological footnotes.
9. **Apep** (draft) — Egyptian-language form in body prose; Apophis noted as Greek-reception form at first mention.
10. **Pinyin** (draft) — current scholarly standard.
11. **Sigurd / Siegfried split** (draft) — Sigurd in Old-Norse contexts; Siegfried preserved when the Nibelungenlied is discussed.
12. **Lôtan** (draft) — circumflex preserved; load-bearing for the Ugaritic–Hebrew cognancy argument.
13. **tehôm** kept italicised throughout body prose (option B) — consistency across the Gunkel-cognancy passages outweighs the "the deep" variant.
14. **'basic myth'** (draft recommendation) — quotation marks retained on every use as a technical term.
15. **Adversary-category term:** "the adversary" (neutral default); "the dragon" only for morphologically draconic figures; "chaos-figure" banned.

**Meta-diacritics policy:** option A — **full scholarly diacritics** across the glossary; footnoted explanations where needed.

---

## 1. "combat myth" vs. "Chaoskampf" in body prose

**Status:** Scope.md §"Terminology default (locked)" says headings use "Chaoskampf" and body prose defaults to "combat myth". The draft glossary reflects that. But the enforcement rule has a trade-off:

- **Strict reading:** "combat myth" everywhere in body prose except in quotations and in passages specifically discussing Gunkel's term.
- **Loose reading:** "Chaoskampf" remains available in body prose wherever precision is wanted (e.g., discussing the scholarly debate, or disambiguating from dragon-combats that are NOT order-making).

The draft locks the strict reading. If the user wants the loose reading, the `never_use` field of the "Chaoskampf" entry should be relaxed.

**DECISION:** Strict reading (draft choice). Use the current preferred scholar term "combat myth" in body prose; reserve "Chaoskampf" for headings, quotations, and discussions of Gunkel's thesis.

## 2. Aži Dahāka — which name across the chapter?

The figure has four names across four language strata: Avestan *Aži Dahāka*, Middle Persian *Dahāg*, New Persian *Zahhāk* (Shāhnāmeh), and non-diacritical *Azhi Dahaka* in older scholarship. The draft uses **Aži Dahāka** with diacritics as the primary form and flags Zahhāk for Shāhnāmeh contexts only. Reader-friendliness and scholarly precision pull in opposite directions:

- (A, draft choice) **Aži Dahāka** throughout — scholarly precision, somewhat hostile to lay readers.
- (B) **Zahhāk** throughout — reader-friendly (Shāhnāmeh is the most widely known form) but distorts the Avestan register.
- (C) Use both: **Aži Dahāka** in philological/Avestan contexts, **Zahhāk** in body prose.

A single decision will ripple across Ch. 13 and wherever the chapter references the Shāhnāmeh reception. Scope.md's "translation-mediated" policy recommends (A); reader expectations may recommend (C).

**DECISION:** (A) **Aži Dahāka** throughout — follow the current scholar consensus. Zahhāk may be noted only when the Shāhnāmeh is specifically under discussion.

## 3. YHWH vs. Yahweh

The draft uses the unvocalized **YHWH** throughout. The alternative **Yahweh** is the vocalized reconstruction and is more common in some academic strands (Day 1985 uses Yahweh). The difference matters because:

- Some readers (especially religious readers) will find "YHWH" more respectful of the tetragrammaton's unvocalized status.
- Others will find "Yahweh" more natural in narrative prose about the deity as a character.

A single decision locks the rendering across Ch. 8, Ch. 9, the reception coda, and the appendix. The draft's choice is defensible but contested.

**DECISION:** **Yahweh** — the vocalised form is common enough in academic and general English that reading the unvocalised "YHWH" through sustained body prose becomes awkward. YHWH may still appear where a direct quotation uses the tetragrammaton.

## 4. Ea / Enki (and Apsû / Abzu; Tarḫunna / Teshub)

The draft locks a **language-context-conditional** rule: use the Akkadian form when the primary text is Akkadian (Anzû, Enūma Eliš, Kumarbi Cycle), the Sumerian form when it is Sumerian (Lugal-e). This is linguistically principled but creates a rendering that switches across chapters. The alternative is:

- (A, draft choice) Language-conditional: Ea / Apsû in Akkadian; Enki / Abzu in Sumerian.
- (B) Always use the Sumerian form (Enki, Abzu) as the "more original".
- (C) Always use the Akkadian form (Ea, Apsû) as the "more widely recognized".

Note that the Sumer book's glossary uses **Enki** and explicitly `never_use: [Ea]`. This book is different — it spans the whole Mesopotamian tradition, not just Sumer, and the switching is (arguably) a feature. **But** the user should confirm that this is what's wanted, because (B) or (C) would be easier for readers.

**DECISION:** (A) language-context-conditional — the form follows the language used in the culture / primary text: Ea and Apsû in Akkadian contexts (Anzû, Enūma Eliš, Kumarbi Cycle), Enki and Abzu in Sumerian contexts (Lugal-e). Same rule applies to Tarḫunna / Teshub and to the other language-pair entries.

## 5. Mishipeshu — which spelling?

Anishinaabe studies has at least three standard spellings for the underwater manitou:

- **Mishipeshu** (draft choice; most common in current English-language scholarship).
- **Mishebeshu** (Theresa S. Smith 1995).
- **Mishipizheu** (other academic usage; sometimes preferred as closer to Anishinaabemowin pronunciation).

Because Ch. 32 foregrounds area specialists (Hallowell, Johnston, T. Smith, Vizenor) and because Theresa S. Smith uses Mishebeshu, the draft's choice of **Mishipeshu** may need adjustment. The user should decide based on (a) which specialist the chapter leans on most, and (b) whether an Anishinaabe-language consultant has been engaged to confirm.

This is the most appropriation-sensitive choice in the glossary.

**DECISION:** **Mishipeshu** — the spelling most common in current English-language Anishinaabe scholarship. If an Anishinaabe-language consultant is engaged at a later stage, this is one of the first items to revisit.

## 6. Nanabozho — which variant?

Regional Anishinaabe spellings: **Nanabozho** (draft choice, Hallowell), **Nanabush**, **Wenabozho**, **Nanabushu**, and others. Each reflects a regional dialect of Anishinaabemowin. The draft defaults to Hallowell's spelling because Ch. 32 is built on Hallowell 1960, but if the chapter expands its specialist base, the spelling may need to shift.

Same underlying issue as #5. These two are methodologically linked — commit together.

**DECISION:** Use whichever spelling is preferred by the lead specialist on whom the chapter draws, **but stick to one** across the chapter to avoid reader confusion. Draft choice **Nanabozho** (Hallowell) stands for Ch. 32 as currently scoped; revisit if the specialist base changes.

## 7. huaca vs. wak'a

Andean studies is split:

- **huaca** — Huarochirí-Manuscript-era Spanish-derived spelling, used by Salomon & Urioste 1991 (the book's anchor source); familiar to English readers.
- **wak'a** — modern Quechua orthography, increasingly used in decolonising Andean scholarship.

The draft chooses **huaca** because the book's primary source is the 1608 manuscript. But if the user wants to align with post-2010 Andean decolonial practice, **wak'a** is the alternative. This is parallel to the Mishipeshu/Nanabozho question.

**DECISION:** **wak'a** — lay English readers are not heavily invested in the older "huaca" form, so reader unfamiliarity is not a real obstacle. Adopting the modern Quechua orthography aligns with decolonising Andean scholarship at low reader cost. First-mention parenthetical may note the older Spanish-derived spelling for readers consulting Salomon & Urioste 1991.

## 8. Krishna vs. Kṛṣṇa (and related Sanskrit diacritics)

The draft locks **Krishna** in body prose and **Kṛṣṇa** in philological footnotes. The alternative is using Kṛṣṇa throughout for consistency with other Sanskrit terms that do carry diacritics (Vṛtra, Tvaṣṭṛ, Kāliya). The argument for Krishna-without-diacritic is reader recognition; the argument for Kṛṣṇa is philological consistency with the rest of the Vedic/Sanskrit inventory.

A coupled question: should **Viṣṇu** appear with diacritic or as **Vishnu** in body prose? (Draft is silent; implied "Vishnu" but inconsistent with Kṛṣṇa if that's chosen.)

**DECISION:** **Krishna** in body prose (draft choice) — previous familiarity to English readers is decisive; Kṛṣṇa reserved for strict philological footnotes. By consistency with the full-scholarly-diacritics meta-policy, **Viṣṇu** retains its diacritics in body prose (it is not familiar enough to earn a diacritic-stripped form on reader-recognition grounds).

## 9. Apep vs. Apophis

The draft locks **Apep** (Egyptian-language form) in body prose and notes **Apophis** (Greek-reception form) at first mention. The alternative — using **Apophis** as body-prose default — is reasonable because (a) Apophis is more widely recognized in English reception, and (b) the book's reception coda engages the Hellenistic-and-later afterlife. The draft's choice reflects scope.md's preference for the tradition-internal form.

**DECISION:** **Apep** (draft choice).

## 10. Chinese: Pinyin vs. Wade-Giles

The draft uses **Pinyin** throughout (Gonggong, Zhuanxu, Nüwa, Mount Buzhou, Hou Yi, Yu the Great with the "the Great" preserved in English). The only reason to consider Wade-Giles (Kung-kung, Chuan-hsü, Yü, etc.) would be to match older scholarly sources. The draft's Pinyin choice is the current standard and is recommended; flagging here only because some readers have long-standing familiarity with Wade-Giles-era Birrell/Lewis discussions.

**DECISION:** **Pinyin** (draft choice).

## 11. Siegfried / Sigurd

Draft splits: **Sigurd** in Old-Norse-text contexts, **Siegfried** where the Nibelungenlied is discussed. If the book treats the Nibelungenlied only in passing (likely, given it's primarily reception), **Sigurd** could just be the universal form. User to decide whether the Germanic (MHG) distinction is worth preserving in a few places.

**DECISION:** Keep the split (draft choice). **Sigurd** in Old-Norse contexts; **Siegfried** preserved when the Nibelungenlied is under discussion.

## 12. Lôtan — the circumflex

**Lôtan** (with circumflex) preserves vowel length in modern Ugaritic scholarship; **Lotan** (without) is common in popular writing. The circumflex is load-bearing because the book makes the Ugaritic-Hebrew (Lôtan ↔ Leviathan) cognancy argument explicit. Draft locks **Lôtan**; confirm.

**DECISION:** **Lôtan** (draft choice; circumflex preserved).

## 13. Tehôm — when to italicise

Hebrew *tehôm* is locked as italicised + circumflex on first mention. In subsequent body prose should it be:

- (A, draft) translated as "the deep" (roman).
- (B) kept as *tehôm* (italic) throughout.

Genesis 1:2 is quoted multiple times across Ch. 8, the introduction, and the Gunkel-Ballentine discussions. Consistency matters.

**DECISION:** (B) Keep *tehôm* (italic) throughout body prose. "The deep" is reserved only for direct biblical quotations where the English translation is required.

## 14. "basic myth" — when to drop the quotation marks

The draft locks `'basic myth' (in quotation marks on first mention)` for the Ivanov-Toporov reconstruction. The quotation marks flag the contested status. Beyond Ch. 20 and Ch. 38 (C5), is the user comfortable dropping the marks in body prose? Draft is silent on this; recommend keeping the quotation marks every time the term is used as a technical name.

**DECISION:** Keep the quotation marks on every technical use of 'basic myth' (draft recommendation).

## 15. The Chaoskampf adversary-category term

A subtle vocabulary choice: what does the book call the class of adversary — "the monstrous adversary", "the dragon", "the chaos-figure", "the adversary"? The draft doesn't lock this because the terms are common English. But cross-chapter consistency would benefit from a choice. **Recommended:** "the adversary" (neutral); "the dragon" only where the figure is visually / morphologically draconic; avoid "chaos-figure" (begs the question the book is precisely about).

**DECISION:** Adopt the recommendation. "The adversary" is the default neutral category term; "the dragon" only where the figure is morphologically draconic; "chaos-figure" banned. A new glossary entry "the adversary (category term)" has been added to CATEGORY TERMS to lock this.

---

## Meta-note: diacritics consistency

The draft is diacritical-forward (Aži Dahāka, Kərəsāspa, Vṛtra, Tvaṣṭṛ, Šarur, Enūma Eliš, maʿat, ʿAnat, Lôtan, Tiamat-without-length-mark-but-Ṣapānu-with). This is the current scholarly norm across the primary-source language strata, but it is hostile to lay readers who may stumble on unfamiliar glyphs. The user should decide the register:

- (A, draft) **Full scholarly diacritics** across the glossary; footnoted explanations where needed.
- (B) **Simplified** (no ḫ, no ṛ, no ʿ) in body prose; full diacritics reserved for first-mention and footnotes.
- (C) **Mixed per language** — Sanskrit and Avestan retain diacritics (they are intelligible without), Sumerian and Akkadian simplify (ḫ and š are visually alarming).

Scope.md §"Book register" says "Plain-English register — no unexplained technical terms on first use." This slightly favours (B) or (C). But a maximalist reading of "translation-mediated" favours (A). The user must choose, and the choice will cascade across all ~120 terms.

**DECISION:** (A) **Full scholarly diacritics** across the glossary (draft choice). Footnoted explanations where needed. Scope.md's "plain-English register" is satisfied by first-mention glosses, not by diacritic-stripping.
