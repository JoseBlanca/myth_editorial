# Factcheck — Chapter 7: The Toil of Babylon

```yaml
meta:
  auditor_model: "Claude Opus 4.7 (1M context)"
  auditor_conversation_id: "fresh conversation; no memory of producing the claims"
  input_file: "chapters/07-toil-of-babylon.claims.adoc"
  brief_file: "briefs/07-toil-of-babylon.yaml"
  claims_identified: 14 (paragraphs/markers, including INFERENCEs and VARIANT/RECONSTRUCTION/LACUNA blocks)
  triangulations_performed: 12 (web searches + ToC fetches against de Gruyter, Internet Archive, Academia.edu, eatthefruit, Britannica/Britsh Museum)
  verdict: BLOCK / MAJOR-REVISE
```

## Verdict

**MAJOR-REVISE** — verging on BLOCK. The chapter has at least four HIGH-severity findings:
(1) the page range used by every Lambert-2013 EVIDENCE token is wrong (the cited pp. 366–375 fall inside *The Slaying of Labbu*, not *The Toil of Babylon*, which is on pp. 301–310); (2) the manuscript number BM 47860 is unverified and does not appear in the BSOAS review's witness-trail (which gives the older publications TSBA 5, 303 ff. and STC 1, 219–20); (3) the central narrative reading is the OPPOSITE of what surviving translations show — the surviving columns describe Marduk as despondent, the Anunnaki as hating the father of the gods, the populace conscripted into onerous toil, a figure determined to overthrow the dynasty, and Babylon decreed for "extinguishing" — not a celebratory Marduk-builds-Esagil cosmogony with cooperative Anunnaki and human labour; (4) the ‘third theogonic foundation’ INFERENCE rests on that misreading and so is unsalvageable in its present form.

Because the brief itself carries the wrong page range and the wrong content gist, **upstream brief errors must be corrected before the chapter is rewritten**. This is the kind of fix that should propagate back to `briefs/07-toil-of-babylon.yaml`.

---

## Tallies

```yaml
tallies:
  supported: 1     # Existence and editorial-authority of Lambert 2013 as the standard edition
  internal_variance: 0
  unverified: 6
  citation_wrong: 9   # every loc=pp. 366-375 / 369-372 / 372-375 / 369-374 / p. 374 reference
  contamination: 0
  fabrication: 2     # narrative content overwhelmingly contradicts surviving translation
  silent_bridges: 0
  marker_issues: 2   # both INFERENCE markers rest on misreadings; LACUNA loc is wrong
  glossary_violations: 0
```

---

## Supported claims

```yaml
supported_claims:
  - claim_number: 3
    claim: "The standard critical edition is W. G. Lambert's treatment in *Babylonian Creation Myths* (Mesopotamian Civilizations 16, Eisenbrauns 2013)."
    source_id: lambert-2013
    source_loc: "pp. 301-310 (the actual range; not pp. 366-375 as claimed)"
    verbatim_quote: "Lambert 2013 *Babylonian Creation Myths* contains 'The Toil of Babylon' as one of the 'Further Babylonian Creation Tales' in Part III." (de Gruyter ToC; BSOAS review by Frans van Koppen 2014)
    note: "The general fact that Lambert 2013 is the standard edition is correct. Page range and contents-summary are not."
```

---

## Findings

### HIGH severity

```yaml
- claim_number: 1
  kind: CITATION-WRONG
  severity: HIGH
  claim: "Preserved on a single Late Babylonian (Hellenistic-period) manuscript: BM 47860, in the British Museum. Lambert 2013, pp. 366–375."
  issue: |
    Two errors in the same line:
    (a) The page range pp. 366–375 is wrong. The de Gruyter Brill table of contents
        for Lambert 2013 places "The Toil of Babylon" at pp. 301–310. The cited range
        pp. 366–375 falls inside Lambert's edition of *The Slaying of Labbu*
        (pp. 361–375 in the same Part III).
    (b) The manuscript identifier BM 47860 is unverified. The BSOAS review
        (van Koppen 2014, on Academia.edu) records the witness for *The Toil of
        Babylon* at "TSBA 5, 303 ff. and STC 1, 219–20" — the older publication
        history (Boscawen, *Trans. Soc. Bibl. Arch.* vol. 5, 1876; King, *STC* I,
        1902). No web-locatable source corroborates BM 47860 as the BCM-edition
        witness, and BM 47860 is independently associated with a Late Babylonian
        Chronicle for 616–609 BCE (the Fall of Nineveh), which is not a creation text.
  evidence: |
    de Gruyter Brill ToC (https://www.degruyterbrill.com/document/doi/10.1515/9781575068619/html):
    "The Toil of Babylon: pp. 301–310 ... The Slaying of Labbu (two entries): pp. 361–375"
    BSOAS review (van Koppen): "the manuscript reference cited as 'TSBA 5, 303 ff. and STC 1, 219–20'."
  recommended_fix: |
    Change every "loc=pp. 366-375" / "pp. 369-372" / "pp. 372-375" / "p. 374" /
    "p. 366" reference in this claims document to the correct Lambert-2013 range
    (pp. 301–310, with sub-page references inside that range).
    For the manuscript identifier, do NOT assert "BM 47860"; either (i) verify the
    actual BM number against Lambert 2013 directly (if a print copy is available),
    or (ii) state "the British Museum tablet edited by Lambert 2013" without giving
    a specific BM number until verified.
    The brief (briefs/07-toil-of-babylon.yaml) carries the same wrong page range and
    must also be corrected; this is an upstream-propagation error.

- claim_number: 9
  kind: FABRICATION (content-overreach grounded in misread loc)
  severity: HIGH
  claim: |
    "*The Toil of Babylon* foregrounds Babylon as the cosmic centre — the place
    where divine and human labour together founds the inhabited world. The city is
    not just a place that exists in the cosmos; it is the cosmos's foundational
    construction project. ... The composition's central focus is the construction
    of Esagil — Marduk's temple at the heart of Babylon. Esagil's foundation is
    presented as the cosmogonic moment proper: the gods establish their permanent
    dwelling on earth, and the act of construction is itself the creation of the
    cosmic order."
  issue: |
    The surviving columns of *The Toil of Babylon* — as quoted on the basis of
    Lambert's translation in publicly accessible summaries that draw on Lambert
    2013 (eatthefruit.com transcription quoting Lambert/Boscawen/Smith) — do not
    present this celebratory Marduk-as-builder narrative.

    What the surviving columns actually show:
    - Col. I, lines 1-2: "All the Anunnaki hated the father of all the gods, /
      And Marduk, in his temple, was despondent."
    - Col. I, lines 5-6: "The people of Babylon were impressed into forced labor, /
      Small and great had to bear the toil."
    - Col. I, line 13: a figure "determined to overthrow the dynasty."
    - Col. I, line 16: he brought "shrines into ruins."
    - Col. V, line 9: "For eternity they decreed extinguishing as the destiny of the peoples."
    - Col. V, lines 17-19: "The gods prostrated themselves, letting tears flow, /
      And weeping in much agitation for Babylon the pure."

    This is a rebellion / divine-disfavour / urban-doom narrative — closer to the
    Igigi-rebellion register of *Atra-ḫasīs* than to the Esagil-construction
    triumph of *Enūma Eliš* VI. The text uses the language of *toil* (the title
    is editorial precisely because the labour is heavy and resented), not of
    foundational triumph.
  evidence: |
    eatthefruit.com transcription of Lambert/Boscawen/Smith translation of the
    text columns of BM-tablet-edited-by-Lambert (https://www.eatthefruit.com/the-toil-of-babylon/).
    BSOAS review (van Koppen 2014) confirms the witness lineage to TSBA 5 and STC I.
  recommended_fix: |
    Rewrite the entire "Setting" section. The chapter cannot claim that the
    composition presents a celebratory cosmogonic Marduk-builds-Babylon narrative
    when the surviving lines show the opposite: divine resentment, populace
    conscripted into onerous toil, a figure overthrowing the dynasty, gods weeping
    for Babylon, and Babylon's destiny decreed as "extinguishing".

    A more accurate framing: *The Toil of Babylon* is a fragmentary composition
    that picks up the *Atra-ḫasīs*-style toil-and-rebellion register and applies
    it to the people (and gods) of Babylon. The surviving columns describe a
    Babylon under labour-rebellion conditions, with Marduk despondent in his
    temple while the Anunnaki are hostile to the father of the gods and the
    populace is in revolt. The cosmogonic-celebration reading must be retracted.

- claim_number: 10
  kind: FABRICATION (content-overreach)
  severity: HIGH
  claim: |
    "In the surviving text, Marduk directs the construction. He is the divine
    builder, designer, and patron of the project — Babylon and its temple are his
    personal foundation. ... The Anunnaki — the ruling order of gods — also
    participate in the construction. The divine workforce and the human workforce
    labour together on the project under Marduk's direction."
  issue: |
    The surviving columns show Marduk DESPONDENT in his temple — not directing
    construction — and the Anunnaki HATING the father of the gods, not labouring
    cooperatively under Marduk's direction. The construction-leader / Anunnaki-
    workforce / human-co-labourers framing appears to be lifted from *Enūma Eliš*
    VI and projected onto *The Toil of Babylon*.

    There is no public scholarly summary I can locate that supports the claim that
    Marduk directs construction in *The Toil of Babylon*. The BSOAS review's
    catalog entry does not assert it; the eatthefruit transcription, drawing on
    Lambert's translation, contradicts it.
  evidence: |
    Col. I lines 1-2 (above): "All the Anunnaki hated the father of all the gods, /
    And Marduk, in his temple, was despondent."
  recommended_fix: |
    Drop both the Marduk-as-builder claim and the Anunnaki-workforce claim.
    The chapter must be rewritten on the basis of what the surviving columns
    actually contain. If Lambert 2013's commentary does include construction-
    direction material in lacunae or restored sections, that must be flagged with
    a [RECONSTRUCTION:] marker that names which fragmentary lines are being
    interpreted that way; it cannot be presented as straightforward narrative.

- claim_number: 11 (LACUNA marker)
  kind: MARKER-FABRICATED / CITATION-WRONG
  severity: HIGH
  claim: |
    "[LACUNA: BM 47860, multiple breaks throughout. Several columns of the
    late-Babylonian manuscript are heavily damaged; the precise sequence of
    construction labours and the identity of the divine builder in some passages
    are partly lost. | source: Lambert 2013, pp. 366–375 (manuscript score) | ..."
  issue: |
    The LACUNA references BM 47860 (unverified — see Finding 1) and Lambert 2013
    pp. 366–375 (wrong — see Finding 1). It also describes the missing material in
    terms of "construction labours" and "divine builder", which presumes the
    chapter's misreading (Findings 9–10). The actual lacunae of the text are real
    (the eatthefruit summary notes only three of five columns are legible, none
    complete) — but they're lacunae in a rebellion / toil-and-doom narrative,
    not lacunae in a construction sequence.
  recommended_fix: |
    Rewrite the LACUNA marker to reflect the actual content (3 of 5 columns
    legible, none complete; missing material includes the framing of the toil,
    the identity of the rebellion-leader, the role of Marduk, the resolution of
    the conflict). Reference Lambert 2013 pp. 301-310, not pp. 366-375.
```

### MEDIUM severity

```yaml
- claim_number: 12 (RECONSTRUCTION marker)
  kind: MARKER-MISUSED
  severity: MEDIUM
  claim: |
    "[RECONSTRUCTION: Lambert 2013's running text restores breaks within the
    single manuscript; alternative readings for damaged sections are proposed in
    the apparatus. | gap_source: breaks within BM 47860 | fill_source: limited;
    no parallel Akkadian witnesses; Lambert's restorations are internal-context
    proposals constrained by surviving syntax and by parallels to other late-
    Babylonian Marduk-dossier compositions (notably *Enūma Eliš* VI's Esagil
    construction sequence) | confidence: low]"
  issue: |
    The fill_source clause's invocation of *Enūma Eliš* VI as a parallel source
    of restoration assumes the chapter's misreading (that *The Toil of Babylon*
    narrates an Esagil-construction sequence parallel to *Enūma Eliš* VI). On the
    actual content, *Atra-ḫasīs*'s Igigi-rebellion register is the closer
    parallel; *Enūma Eliš* VI is the WRONG comparandum.
  recommended_fix: |
    Rewrite the fill_source clause to name the actually-relevant comparandum
    (*Atra-ḫasīs*'s Igigi-rebellion sequence) for those lines that involve
    populace-toil / divine-rebellion language, and to flag that no parallel
    Akkadian witness fills the construction-related gaps because there are no
    construction-related gaps to fill — the construction-narrative reading is
    being projected by the chapter author, not preserved in the source.

- claim_number: 7
  kind: UNVERIFIED
  severity: MEDIUM
  claim: |
    "The single manuscript dates to the Late Babylonian (Hellenistic) period."
  issue: |
    The eatthefruit summary calls the witness "Neo Babylonian" rather than
    "Late Babylonian (Hellenistic)". I cannot independently verify the dating
    without access to Lambert 2013 directly. The brief states Hellenistic; the
    accessible secondary descriptions are looser. Until verified against the
    actual Lambert 2013 page (now p. 301 ff., not p. 366), the claim
    "Hellenistic-period" should be treated as unverified.

    Note: "Late Babylonian" in Assyriological dating overlaps with the
    Achaemenid through Hellenistic periods; "Neo-Babylonian" properly refers to
    the 7th–6th c. BCE dynasty. Conflating the two is a real error of
    Assyriological taxonomy.
  recommended_fix: |
    Verify the dating against Lambert 2013 pp. 301-310 directly. If the manuscript
    is in fact Hellenistic, retain (with a more precise gloss). If it is in fact
    Neo-Babylonian (7th–6th c.), the chapter's framing as "late-Babylonian
    temple-scholarly milieu" would also need re-tuning, since the Marduk-dossier
    crystallisation Lambert et al. assign mostly to the 1st-millennium temple-
    scholarly apparatus is broader than just Hellenistic Babylon.

- claim_number: 13 (lullû/awīlu paragraph)
  kind: UNVERIFIED
  severity: MEDIUM
  claim: |
    "The text refers to a primeval, savage human — *lullû* — and to the standard
    Akkadian word for 'human', *awīlu*. The construction labour involves both
    divine workers and human workers, and the text uses the *lullû / awīlu*
    terminology to position the human contribution."
  issue: |
    None of the publicly accessible summaries of *The Toil of Babylon* (the
    BSOAS review, the de Gruyter chapter abstract, the eatthefruit.com
    Lambert-translation transcription) record either *lullû* or *awīlu* in the
    surviving columns. The surviving columns refer to "the people of Babylon"
    (presumably *nišū* / *Bābilāya*) being conscripted, not to *lullû*.

    The lullû/awīlu reading appears to be a projection from *Atra-ḫasīs*'s
    creation-of-humanity terminology, where it is genuinely present, onto
    *The Toil of Babylon*, where the public evidence does not support it.
  recommended_fix: |
    Either (a) verify *lullû* or *awīlu* in Lambert 2013's actual text /
    transliteration on the correct pages (301-310) and retain the claim with
    line numbers, or (b) drop the claim and the subsequent INFERENCE block
    that builds on it.

- claim_number: 14 (INFERENCE marker — Atra-ḫasīs connection)
  kind: MARKER-MISUSED
  severity: MEDIUM
  claim: |
    "[INFERENCE: The lullû reference in *The Toil of Babylon* signals a deliberate
    connection to the *Atra-ḫasīs* tradition — the construction of Babylon is
    presented as part of the same logic that creates humans for divine labour. ...
    | basis: the lullû terminology is shared with *Atra-ḫasīs* and is unusual in
    Akkadian outside the creation-of-humanity context; ...]"
  issue: |
    Builds on Finding above. If the lullû reference is unverified in the actual
    text, the INFERENCE has no factual base. Even if a *lullû* attestation is
    present, the basis still slides into "construction of Babylon" framing
    (Findings 9–10) which is itself unsupported.

    There IS a real and interesting structural parallel between *The Toil of
    Babylon* and *Atra-ḫasīs* — but it runs through the labour-resentment / divine-
    rebellion / decreed-doom motifs, not through the lullû-as-substitute-workforce
    motif. The current INFERENCE points at the wrong link.
  recommended_fix: |
    Reframe the INFERENCE around the actual link: *The Toil of Babylon*'s
    surviving columns share with *Atra-ḫasīs* the pattern of unbearable toil,
    divine-rebellion, and a punitive divine response. The Atra-ḫasīs link is real
    but not via *lullû*; it's via the toil-and-rebellion frame.

- claim_number: 15 (construction sequence claim)
  kind: CITATION-WRONG / FABRICATION
  severity: MEDIUM-to-HIGH
  claim: |
    "The surviving text describes the construction sequence in fragmentary detail.
    Foundations are laid; bricks are made; walls are raised; the temple structure
    rises. The sequence parallels — in shorter form — the Esagil construction
    described in *Enūma Eliš* Tablet VI. footnote: Lambert 2013, pp. 369–374
    (the construction sequence)."
  issue: |
    Page range wrong (Slaying of Labbu, not Toil of Babylon). The construction-
    sequence content described (foundations, bricks, walls, temple-rising)
    matches *Enūma Eliš* VI at lines 57–66, not the surviving columns of *The
    Toil of Babylon*. There is no public evidence that *The Toil of Babylon*
    contains a brick-laying / wall-raising sequence; the eatthefruit transcription
    of the surviving columns shows none.
  recommended_fix: |
    Drop the claim that *The Toil of Babylon* contains a construction-sequence
    parallel to *Enūma Eliš* VI. The structural relationship between the two
    texts is closer to the contrast between *Atra-ḫasīs* (toil + divine rebellion)
    and *Enūma Eliš* VI (cooperative construction triumph). If the chapter wants
    to discuss *Enūma Eliš* VI, it must do so as comparandum from outside *The
    Toil of Babylon*, not as a parallel within the text.

- claim_number: 16 (INFERENCE marker — third theogonic foundation)
  kind: MARKER-MISUSED / OVERREACH
  severity: MEDIUM
  claim: |
    "[INFERENCE: *The Toil of Babylon* offers a third theogonic foundation for
    Marduk's cosmic kingship, alongside the combat in *Enūma Eliš* (defeat of
    Tiamat) and the displacement-and-execution in *Enmešarra's Defeat* (defeat of
    the elder chthonic order). Here the foundation is constructive rather than
    violent: Marduk's authority is grounded in the founding of his city and his
    temple. ..."
  issue: |
    The INFERENCE rests on the misreading: that the text presents constructive
    foundation. The surviving columns show the OPPOSITE — Marduk despondent,
    Babylon under labour-rebellion, the populace decreed for "extinguishing".
    This is not a constructive-foundation cosmogony; if anything it's a
    pessimistic counterpart to *Enūma Eliš* VI's triumphal construction.

    The "third theogonic foundation" structural reading might still be defensible
    in a different form (e.g., framing the Toil as a darker / pessimistic /
    rebellion-cycle Marduk tradition that sits in tension with *Enūma Eliš*'s
    triumphal cosmogony) — but as stated it is unsupportable.
  recommended_fix: |
    Either retract the INFERENCE entirely, or rewrite it around a defensible
    structural claim: that the late-Babylonian Marduk dossier is more diverse
    than the *Enūma Eliš* triumph alone suggests, with *Enmešarra's Defeat* and
    *The Toil of Babylon* opening different theological registers (one dark/
    chthonic-displacement, the other dark/labour-rebellion). The "constructive
    rather than violent" framing must go.

- claim_number: 17 (Bāb-ilī etymology / cosmic-centre theology)
  kind: UNVERIFIED
  severity: MEDIUM
  claim: |
    "Babylon's name in Akkadian — *Bāb-ilī*, 'Gate of the Gods' — is taken as a
    literal description of the city's cosmological function: the place where
    divine and human worlds meet. footnote: Lambert 2013, p. 374 commentary;
    Black & Green 1992, s.v. Babylon, Esagil; Bottéro 2001, on Babylon's
    cosmic-centrality."
  issue: |
    (a) The "Bāb-ilī = Gate of the Gods" folk-etymology is real and well attested
    in Assyriological scholarship, so the gloss itself is unobjectionable.
    (b) The citation Lambert 2013 p. 374 is wrong (Slaying of Labbu, not Toil
    of Babylon).
    (c) Whether Lambert's *Toil of Babylon* commentary makes this etymology
    central to the cosmic-centre theology of the composition is unverified —
    given the actual content (rebellion, doom, toil), the etymology is more
    likely treated ironically or in tension, not as straightforward literal
    description.
  recommended_fix: |
    Move the etymology gloss to a footnote on the city Babylon (broad scholarly
    point) and drop the framing that it is invoked by *The Toil of Babylon*'s
    own theology. Correct the page citation if the chapter author wants to cite
    Lambert 2013's actual Toil-of-Babylon commentary (i.e., somewhere in
    pp. 301-310, not p. 374).

- claim_number: 18 (royal-legitimation reading)
  kind: UNVERIFIED
  severity: MEDIUM
  claim: |
    "The divine origin of Babylon — its foundation by Marduk and the Anunnaki,
    with human participation only as labour — provides theological support for
    the city's first-millennium status as the cosmic centre. The composition
    functions as royal-legitimation: the king of Babylon rules a city the gods
    themselves built. footnote: Lambert 2013, p. 374 (royal-legitimation reading)"
  issue: |
    Page citation wrong (Slaying of Labbu range). The royal-legitimation reading
    presupposes the construction-celebration framing that the surviving text
    contradicts. A text that ends with the gods weeping over Babylon and decreeing
    "extinguishing" as the peoples' destiny is a poor candidate for royal-
    legitimation literature in the conventional sense; it might serve a different
    theological function (e.g., explanation of divine displeasure, or cyclical-
    rebellion-and-reconstitution typology).
  recommended_fix: |
    Drop the royal-legitimation function as an attributed reading unless Lambert
    2013 pp. 301-310 explicitly proposes it. If the chapter wants a function-
    claim, anchor it to the text's actually surviving content.

- claim_number: 19 (sole witness / VARIANT marker)
  kind: UNVERIFIED
  severity: MEDIUM
  claim: |
    "[VARIANT: primary=BM 47860, Late Babylonian (Hellenistic), the sole witness
    | alt=none extant — no parallel manuscripts known | ...]
    The Toil of Babylon has no parallel manuscripts. BM 47860 is the only
    surviving copy of the composition. footnote: Lambert 2013, p. 366
    (single-manuscript transmission)."
  issue: |
    Page citation wrong (Slaying of Labbu range — and within Slaying of Labbu,
    Lambert in fact treats two manuscripts as "two entries"; the "single-
    manuscript" claim attached to p. 366 may have been confused with material
    elsewhere).
    BM 47860 unverified (Finding 1).
    The sole-witness claim itself may well be correct for *The Toil of Babylon*,
    but the supporting reference is wrong.
  recommended_fix: |
    Verify against Lambert 2013 pp. 301-310 whether (i) the BM number, and
    (ii) the sole-witness status, are confirmed. Update the VARIANT marker and
    the footnote with the correct page reference.
```

### LOW severity

```yaml
- claim_number: 4
  kind: CITATION-WRONG
  severity: LOW
  claim: |
    "There is no widely-used English-language anthology translation; Lambert's
    edition stands alone."
  issue: |
    Substantively correct. Foster 2005 (*Before the Muses*, 3rd ed.) does not
    contain *The Toil of Babylon* (its mythological-and-creation contents are
    *Enūma Eliš*, *Atra-ḫasīs*, *Adapa*, *Anzû*, *Etana*, *Erra and Išum*,
    Marduk-creator-of-the-world incantation prologues, etc., per the Eisenbrauns
    description and dokumen.pub transcription — *Toil of Babylon* is not on the
    list). Dalley 2008 (*Myths from Mesopotamia*, rev. ed.) does not contain it
    either (its contents per the Oxford World's Classics back-matter and the
    Internet Archive ToC are *Atrahasis*, *Gilgamesh* SB and OB, *Descent of
    Ishtar*, *Nergal and Ereshkigal* SB and Amarna, *Adapa*, *Etana*, *Anzû* SB
    and OB, the *Epic of Creation*, *Theogony of Dunnu*, and *Erra and Ishum*).
    The footnote citation here ("Lambert 2013, pp. 366-375") is the wrong page
    range as in Finding 1, but the underlying claim about anthology coverage is
    correct.
  recommended_fix: |
    Correct the page range; retain the claim. Adding "(see Foster 2005 contents,
    pp. xv-xvi; Dalley 2008 contents, pp. v-vi)" to the footnote would
    strengthen it.

- claim_number: 5
  kind: CITATION-WRONG
  severity: LOW
  claim: |
    "Foster 2007, *Akkadian Literature of the Late Period*, on the late-Babylonian
    cosmogonic dossier."
  issue: |
    Foster 2007 is a real survey of late-period Akkadian literature; the broad
    claim that it situates compositions in their compositional / recensional
    context is supported by the source registry's notes. The specific claim
    that Foster 2007 treats *The Toil of Babylon* in particular within a
    "late-Babylonian cosmogonic dossier" cannot be verified from publicly
    accessible material; the loc=passim is suspicious — passim is a placeholder
    for "I have not actually located the discussion".
  recommended_fix: |
    Either verify a specific page in Foster 2007 where *The Toil of Babylon* is
    treated, or downgrade the citation to a generic "for the late-period
    cosmogonic dossier in general, see Foster 2007".

- claim_number: 6
  kind: NOTE
  severity: LOW
  claim: |
    "// COMPARATIVE-HOOK: Hebrew Bible Genesis 11 — the Tower of Babel narrative ..."
  issue: |
    This is correctly handled as a COMPARATIVE-HOOK with deferral to the
    influences chapter. No body-prose claim asserts a Tower of Babel relationship
    as established fact (good). However, the rephrasing inside the hook —
    "in *The Toil of Babylon* the city's completion is divine sanction for the
    same project" — is itself the chapter's misreading projected forward. The
    hook should be reworded once the body misreading is corrected: the Toil's
    actual register (divine displeasure, doom, weeping over Babylon) is
    arguably *closer* to Genesis 11's punitive-frustration framing than the
    chapter currently realises, which is a more interesting comparative point.
  recommended_fix: |
    After the body is rewritten, revise the COMPARATIVE-HOOK to reflect the
    actual content of *The Toil of Babylon* and its more complex relation to
    Genesis 11.

- claim_number: 8
  kind: CITATION-WRONG
  severity: LOW
  claim: |
    "footnote: Lambert 2013, pp. 369–372 (the lullû/awīlu human labour)"
  issue: |
    Page range wrong (Slaying of Labbu). See Finding 1.
  recommended_fix: |
    Correct the range. See also Findings 13–14 on the unverified content.
```

---

## EVIDENCE-token spot-check

Every EVIDENCE token in the claims that points at Lambert 2013 with `loc=pp. 366-375`, `pp. 369-372`, `pp. 369-374`, `pp. 372-375`, `p. 366`, `p. 374`, or `pp. 366, 374` is wrong: the correct range for *The Toil of Babylon* is pp. 301–310. Affected lines (numbered by the source-document line):

- Line 10: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 366-375` → should be `pp. 301-310`
- Line 13: `EVIDENCE: source_id=lambert-2013 ; loc=p. 366` → should be `p. 301`
- Line 16: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 366-375` → should be `pp. 301-310`
- Line 19: `EVIDENCE: source_id=lambert-2013 ; loc=p. 366` → should be `p. 301`
- Line 29: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 366-369` → should be in `pp. 301-305` range (TBD)
- Line 33: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 369-372` → should be in `pp. 305-308` range (TBD)
- Line 37: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 369-372` → should be in `pp. 305-308` range (TBD)
- Line 41: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 369-372` → should be in `pp. 305-308` range (TBD)
- Line 47: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 369-372` → should be in `pp. 305-308` range (TBD)
- Line 52: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 369-372` → should be in `pp. 305-308` range (TBD)
- Line 59: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 369-374` → should be in `pp. 305-309` range (TBD)
- Line 62: `EVIDENCE: source_id=lambert-2013 ; loc=p. 374` → should be in `p. 308 or 309` range (TBD)
- Line 66: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 372-375` → should be in `pp. 308-310` range (TBD)
- Line 74: `EVIDENCE: source_id=lambert-2013 ; loc=p. 374` → should be in `p. 308 or 309` range (TBD)
- Line 79: `EVIDENCE: source_id=lambert-2013 ; loc=p. 374` → should be in `p. 308 or 309` range (TBD)
- Line 87: `EVIDENCE: source_id=lambert-2013 ; loc=p. 366` → should be `p. 301`
- Line 92: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 366-375` → should be `pp. 301-310`
- Line 96: `EVIDENCE: source_id=lambert-2013 ; loc=pp. 366, 374` → should be `pp. 301, 309` (or similar within 301-310)

The brief itself (briefs/07-toil-of-babylon.yaml lines 9, 27, 53, 56, 60, 63) carries the same wrong range and is the proximate cause of the propagation. The brief must be corrected as part of this revision cycle.

---

## Honesty self-check

1. **Did I open every cited primary source?** No. I could not access Lambert 2013's actual text directly (Google Books preview redirected to a paywall; archive.org's text was not browseable in the harness; the Eisenbrauns / Penn State and de Gruyter Brill chapter pages are paywalled). I relied on:
   - The de Gruyter Brill table-of-contents page for page ranges (authoritative for ToC, not for content).
   - The BSOAS review by Frans van Koppen (Academia.edu) for the witness lineage.
   - The eatthefruit.com transcription (NOT a scholarly source on its own; cites Lambert/Boscawen/Smith) for the actual translated content.
   - The Eisenbrauns / dokumen.pub / Internet Archive metadata for cross-checks.
   The eatthefruit transcription is the primary evidence for Findings 9–10's content claims; if Lambert 2013 itself contains substantial commentary or restored sections that paint a different picture, I would not have seen it. **However**, the evidence that the surviving columns of the text describe Marduk-despondent / Anunnaki-hostile / populace-conscripted is strong enough across the multiple summaries (eatthefruit + the BSOAS review's silence on construction-celebration content) that the chapter's central reading is at minimum severely under-supported.
2. **Did I triangulate every reference?** Yes for the page-range error (multiple ToC sources agree). Partial for the manuscript-number error — I have positive evidence (BSOAS review pointing to TSBA 5 and STC I) and negative evidence (BM 47860 not appearing in any web-locatable Toil-of-Babylon discussion; BM 47860 separately associated with a Late Babylonian Chronicle), but I could not look at Lambert's manuscript-list page directly. **A human checker with access to the Lambert 2013 print copy must verify the manuscript number on pp. 301-310.**
3. **For every ✓, did I paste a real quote or pattern-match?** I marked only one claim ✓ supported (the existence-and-authority of Lambert 2013 as the standard edition); the supporting evidence for that is the de Gruyter Brill catalog plus the BSOAS review.
4. **Did I distinguish internal variance from contamination?** N/A — no contamination suspected; one source (single witness).
5. **Am I the same model that produced the claims?** I have no memory of producing the claims; I came into this conversation fresh, as required.

---

## Recommended next actions

1. **Fix the brief.** `briefs/07-toil-of-babylon.yaml` has the same wrong page range (pp. 366–375). Update to pp. 301–310 (and verify the manuscript number against a print copy of Lambert 2013 before recording it).
2. **Verify the actual content of Lambert 2013 pp. 301–310 against a print copy.** The eatthefruit transcription strongly suggests the chapter's central reading is wrong, but a Lambert-2013-page-301 print verification is the only way to confirm Findings 9–10 with full confidence.
3. **Rewrite the claims document** around the actual content of the surviving columns:
   - Setting: Babylon under labour conditions; the populace conscripted; gods in tension.
   - Marduk: despondent in his temple, not directing.
   - Anunnaki: hostile to the father of the gods, not cooperative workforce.
   - The construction-sequence claim and the Esagil-construction parallel to *Enūma Eliš* VI: drop or replace.
   - The lullû/awīlu connection: verify in the actual text or drop.
   - The "third theogonic foundation" INFERENCE: rewrite around a defensible structural claim (e.g., the rebellion-and-doom register as a darker counterpart to *Enūma Eliš*'s triumph), or retract.
   - The Bāb-ilī etymology / cosmic-centre theology: keep as a generic Babylon-theology framing, decouple from the specific Toil-of-Babylon claim until verified.
4. **The Genesis 11 COMPARATIVE-HOOK is currently OK** in that no body-prose makes the comparison as established fact. After the body is rewritten, the hook itself should be revisited because the actual Toil content (gods weeping for Babylon, decreed extinguishing) is a more nuanced foil to Genesis 11 than the current "celebration-vs-condemnation" framing implies.

---

## Verdict

**MAJOR-REVISE / BLOCK.** Four HIGH-severity findings and nine MEDIUM-severity findings. Every Lambert-2013 page citation in the document is wrong; the central narrative reading of the composition appears to be the opposite of what the surviving columns contain; the manuscript identifier is unverified; both INFERENCE markers and the LACUNA marker rest on the misreading. The chapter cannot be drafted from this claims document; it must be rewritten on a corrected brief and a fresh re-reading of Lambert 2013 pp. 301–310.
