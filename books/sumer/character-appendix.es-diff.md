# Diff — character-appendix.adoc → character-appendix.es.adoc

Reference appendix, 79 character entries across four categories. Below is a
representative sample of rendering decisions, plus notes on the non-trivial
choices that recur across the appendix.

## Structural totals

| Metric                | Source | Translation |
|-----------------------|-------:|------------:|
| Lines                 |   1142 |        1142 |
| `footnote:[...]`      |    363 |         363 |
| `[[char-...]]` anchors|     79 |          79 |
| `=== Section` headers |      4 |           4 |
| `<<ch-NN-...,` xrefs  |    182 |         182 |

All anchor IDs and xref targets are byte-identical between source and
translation. Section-header visible text, entry headings, bold labels, and
cross-reference display text are the only strings translated.

## Fixed-form renderings (applied consistently across every entry)

- `=== Deities` → `=== Deidades`
- `=== Heroes and Mortals` → `=== Héroes y mortales`
- `=== Creatures and Monsters` → `=== Criaturas y monstruos`
- `=== Personified Concepts` → `=== Conceptos personificados`
- `*Physical description.*` → `*Descripción física.*`
- `*Appears in:*` → `*Aparece en:*`
- `*Relevance.*` → `*Relevancia.*`
- "No physical description survives in the in-scope sources." → «No se conserva
  descripción física alguna en las fuentes del corpus considerado.»
  (used verbatim in every entry that repeats the formula; extended forms such
  as "No physical description survives in the in-scope sources beyond…" are
  rendered as «No se conserva descripción física alguna en las fuentes del
  corpus considerado, más allá de…».)

## Entry-heading decisions (visible names)

- Most character names (`==== An`, `==== Inanna`, `==== Ninurta`, etc.) are
  unchanged from the glossary locks.
- `==== Lord of Aratta` → `==== Señor de Aratta` (rendered with lowercase
  `señor` in cross-reference display text to match the chapter title).
- `==== Bull of Heaven` → `==== Toro del Cielo`.
- `==== Galla demons` → `==== Los galla` (glossary-locked: invariable
  italicised plural; "demons" redundant once the gloss is in place).
- `==== Phantom maid (ki-sikil-lil-la)` → `==== La doncella fantasma
  (ki-sikil-lil-la)` (Sumerian term preserved as an italicised transliteration
  inside the body when referenced; the heading keeps parentheses intact).
- `==== Bird (Mušen)`, `==== Fish (Ku₆)`, `==== Copper (Urudu)`, `==== Silver
  (Ku-babbar)`, `==== Hoe (Al)`, `==== Plough (Apin)`, `==== Date Palm
  (Gišimmar)`, `==== Tamarisk (Šinig)` → parenthesised Sumerian preserved
  unchanged; head nouns translated (`Ave`, `Pez`, `Cobre`, `Plata`, `Azada`,
  `Arado`, `Palmera datilera`, `Tamarisco`).

## Chapter-title display text (locked from `.es.adoc` headings)

Every `<<ch-NN-slug, _Chapter Title_>>` uses the Spanish `==` title from the
corresponding `.es.adoc` file, verbatim. Examples:

- `ch-07-lugal-e` → _Las hazañas de Ninurta: la batalla contra Asag_
- `ch-11-inanna-and-ebih` → _Inanna y Ebih: la destrucción de la montaña_
- `ch-19-gilgamesh-and-aga` → _Gilgamesh y Aga: el asedio de Uruk_
- `ch-22-gilgamesh-enkidu-and-the-nether-world` →
  _Gilgamesh, Enkidu y el inframundo_
- `ch-28-eridu-flood-story` → _El relato del Diluvio: el Génesis de Eridu_

## Sample sentence-level renderings

- EN: "A reference guide to the named characters who appear in this book."
  ES: «Guía de referencia de los personajes con nombre propio que aparecen en
  este libro.» — drops the nominalised "A reference guide to…" opener in
  favour of a plain genitive construction.

- EN: "the organising administrator of the cosmos and the most narratively
  productive deity in the pantheon."
  ES: «administrador organizador del cosmos y la deidad más productiva, en
  términos narrativos, de todo el panteón.» — "narratively productive" spelled
  out with a parenthetical «en términos narrativos» to avoid the calque
  «narrativamente productiva», which does not read naturally in Spanish
  divulgación.

- EN: "Enki's characteristic method of engineering around cosmic law rather
  than breaking it: a category-defying being can pass where gods cannot, and
  empathy exploited can deliver what force never could."
  ES: «el método característico de Enki para esquivar la ley cósmica sin
  quebrantarla: un ser que desafía las categorías puede pasar por donde los
  dioses no pueden, y la empatía explotada puede lograr lo que la fuerza
  jamás conseguiría.»

- EN: "his wailing cult is directly attested in Ur III and Old Babylonian
  ritual practice"
  ES: «Su culto de plañidos está atestiguado directamente en la práctica
  ritual de Ur III y del periodo paleobabilónico» — "Old Babylonian"
  consistently rendered as «paleobabilónico», the standard Spanish
  Assyriological term.

- EN: "the lord of Aratta is a worthy adversary whose articulate resistance is
  the reason the composition is a contest rather than a proclamation."
  ES: «El señor de Aratta es un adversario a la altura cuya resistencia
  articulada es la razón de que la composición sea una contienda y no una
  proclama.»

- EN: "corvée labour"
  ES: «prestaciones personales de trabajo» — the technical French loan
  *corvée* was replaced with a plain paraphrase to keep the register
  accessible (Asimov-style divulgación).

## Glossary compliance

All glossary-locked terms appear in their chosen Spanish form:
`Inanna`, `Enki`, `Enlil`, `Ninurta`, `Ereshkigal`, `Ninhursaja`, `Dumuzid`,
`Nanna-Suen`, `Geshtinanna`, `Ningishzida`, `Ninlil`, `Gilgamesh`, `Enkidu`,
`Enmerkar`, `Lugalbanda`, `Huwawa`, `Nippur`, `Uruk`, `Eridu`, `Dilmun`,
`Aratta`, `Kish`, `Anzud`.

Italicised transliterated terms kept consistently in italics without
translation, glossed where needed: *me*, *kur*, *abzu*, *me-lam*, *edubba*,
*galla*, *huluppu*, *sukkal*, *pukku*, *mekku*, *kurgarra*, *galatur*,
*dul-kug*, *kur-gal*, *pala*, *shugurra*, *gud an-na*.

Forbidden renderings (`Ishtar`, `Ea`, `Sin`, `Tammuz`, `Ningirsu`,
`Ninhursag`, `Humbaba`, `Anzu`, `abismo`, `aura` for *me-lam*,
`ordenanzas cósmicas` for *me*) do not appear.

## False-friends audited

No occurrences of the usual English-to-Spanish calques were introduced:
*eventually* → «al final» / «en última instancia» / «más tarde» (not
«eventualmente»); *actually* → «de hecho» / «en realidad» (not «actualmente»);
*realize* → «darse cuenta» (not «realizar»); *fabric* / *argument* / *attend*
/ *support* / *character* / *fact* / *sensible* all checked; no false-cognate
renderings leaked.

## Register notes

- Active voice preferred throughout; agentless passives avoided except where
  they read most naturally in Spanish (e.g., «se conserva descripción»).
- Em-dashes used for asides, with outer spaces and no inner spaces, matching
  the English source's punctuation.
- «» (RAE guillemets) used for every quoted English phrase inside the prose
  (e.g., «agua de la vida», «Padre Enki», «como un recipiente roto»,
  «esplendor físico y presencia aterradora»).
- Footnote citation content kept in Chicago-author-date form, with "lines"
  → «líneas» and "columns" → «columnas»; bibliography titles untouched.
