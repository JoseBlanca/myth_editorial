# 31 — The Debate between Hoe and Plough — diff notes

Representative sentence pairs and non-trivial rendering decisions. Full structural check: anchors, xrefs, footnote count (21), EVIDENCE tokens (0), COMPARATIVE-HOOK tokens (0) all match source byte-for-byte where required.

## Title and glossary first mentions

- EN: `== The Debate between Hoe and Plough`
- ES: `== El debate entre la azada y el arado`
- Chapter-body capitalisation: Spanish capitalises only the first word of a title; the personified tools (*the Hoe*, *the Plough*) are capitalised throughout the body as **la Azada** / **el Arado** to preserve the personification.

- `Nippur (Sumerian: Nibru)` → `Nippur (sumerio: Nibru)` — glossary-locked.
- `edubba` stays in italics; glossed on first mention as «la escuela de escribas, literalmente “casa de tablillas”…», per `glossary.es.yaml`.
- `a-da-min`, `al`, `apin` — italics preserved; untranslated.
- `E-kur` preserved unchanged (deity-temple name).

## Representative sentence-level renderings

- EN: "It was a standard curriculum text."
  ES: «Era un texto habitual del plan de estudios.» — *standard* rendered as *habitual* to avoid the English-calque *estándar* here and sit in the register register; *curriculum* → *plan de estudios* consistently.

- EN: "Nearly complete."
  ES: «Se conserva casi completo.» — added the implicit verb («se conserva») for Spanish fluency; no factual shift.

- EN: "The format will be familiar to anyone who has read a trial transcript, a parliamentary debate, or an undergraduate essay competition -- except that here the participants are farm implements and the judge is the king of the gods."
  ES: «El formato resultará familiar a cualquiera que haya leído la transcripción de un juicio, un debate parlamentario o un concurso universitario de ensayo —salvo que aquí los contendientes son aperos de labranza y el juez es el rey de los dioses—.»
  — The en-dash-bounded aside is rendered with em-dashes and no inner spaces (Spanish convention); the trailing em-dash sits before the period.

- EN: "That fact alone tells us something about how they thought…"
  ES: «Ese solo hecho nos dice algo sobre su manera de pensar…» — *fact* → *hecho* (not the false friend *facto*); *how they thought* unfolded into *su manera de pensar* to preserve the Asimov voice.

- EN: "…the seeder-plough used for large-scale cereal agriculture."
  ES: «…el arado sembrador empleado en la agricultura cerealística a gran escala.» — *seeder-plough* rendered with the standard Spanish Sumerology term *arado sembrador*.

- EN: "…the Plough, by contrast, receives no comparable origin story in the opening lines."
  ES: «El Arado, en cambio, no recibe un relato de origen comparable en los versos iniciales.» — *opening lines* → *versos iniciales* (the composition is verse); *by contrast* → *en cambio* (not *por contraste*, a calque).

- EN: "this is a thumb on the scale"
  ES: «esto es un dedo en la balanza» — idiomatic rendering; same metaphor works in Spanish.

- EN: "the Hoe clears it" (of the canal silting up)
  ES: «la Azada lo despeja» — kept the dramatic present tense cadence.

- EN: "an expensive piece of wood attached to a confused ox."
  ES: «un costoso trozo de madera enganchado a un buey desconcertado.» — literal, preserving the dry humour.

## Lacuna / inference blocks

- `_[At this point the tablet breaks…]_` translated in situ while preserving the italic block delimiters (`_[…]_`).
- The parenthetical `_(Enlil's verdict… risk: …)_` translated with its embedded `footnote:[Inference: … Risk: …]` **kept verbatim in English**, since it is a pipeline-style inference note whose internal markers (`Inference:`, `Risk:`) are pipeline-machinery vocabulary, not user-facing prose. This preserves the existing review-trail semantics. If the house style later dictates translating these, it is a one-line change.

## Footnote policy

- All 21 footnote bodies preserved in English because they consist of scholarly citations (ETCSL IDs, Black et al. 2004, Kramer 1961, Civil 1994 page ranges and descriptors like *composite text*, *passim*, *manuscript list*). Per hard rule 4, bibliography titles stay in original language; these footnote contents are citation strings keyed to the unchanged bibliography.
- No direct scholar-translation quotation appears inline in this chapter, so no *Traducción propia del inglés…* note was added anywhere.

## False-friends audit

- *fact* → *hecho* (not *facto*).
- *discuss* → *discutir*, *debatir* — both used correctly in their rhetorical sense.
- *argument* → *argumento* (rhetorical sense — valid cognate, not the false-friend *discusión-conflict*).
- *character*, *eventually*, *actually*, *realize*, *library*, *assist*, *sensible*, *sympathetic*, *fabric*, *pretend*, *apology*, *attend*, *support*, *exit* — none occur in the source or translation.

## Register and punctuation

- Em-dashes: outer spaces, no inner spaces (e.g. `—la capital religiosa de Sumer—`).
- Guillemets «…» used for the title in the opening sentence and for the quoted question «¿qué herramienta importa más?»; inverted `¿` opens the question, as required.
- No nominalisation pile-ups; active voice throughout («Enlil dicta el veredicto final», «los sumerios… desarrollaron»).
- Verb *zanjar* used for *to decide/settle* where a stronger verb than *decidir* carried the meaning of a single final authority closing the matter.
