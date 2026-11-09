# Exhibits: deciding, building, aligning and cleaning the visual on a slide

An exhibit is whatever proves the title: a chart, a table, a concept visual
or, when nothing else fits, text. This file decides which, before any text is
written, and sets the rules that keep a speaker-led deck from turning into a
reading deck with a presenter in front of it. `visual-design.md` keeps the
grid, the type scale, the chart rules and the layout catalogue; this file
adds the decision, the catalogue of concept visuals, the alignment to the
message, the cleaning sequence and the text budgets.

## Quick checklist

- [ ] Every ghost-deck title carries a form mark: chart (comparison type), table, concept (type from section 3) or text with a reason
- [ ] Density mode declared for the whole deck; text budget per slide from section 6 kept; "both" means reading deck first, speaker deck by cutting
- [ ] Exhibit brief (section 2) written before each exhibit is built; exhibits built before text slides
- [ ] The subject of the title is the highlighted element; everything else is grey
- [ ] Order inside the exhibit follows the message; reading direction as in section 4; equal scales across compared charts
- [ ] Register names, order and colours used inside the exhibit (axes, legends, nodes)
- [ ] Cleaning sequence run (section 5): no element without a job; caps kept; direct labels
- [ ] Cover test and headline test passed (section 5)
- [ ] No invented data; placeholder data marked inside the exhibit
- [ ] Host constraints applied (section 7): native shapes, no images for diagrams; where rendering cannot be checked, text dump and element count instead, and the delivery note says so

Detail follows; the checklist is what gets ticked before delivery.

## 1. Deciding the form

Decide the form of every exhibit at the gate, in the ghost deck, not while
building. The form mark sits next to the evidence mark of each title:

```
[evidence: available; source | form: chart:time-series | table | concept:cycle | text, because …]
```

"Text" needs a reason; the reason is reviewed at the gate like a claim.
Acceptable reasons: the evidence is a single number or a quotation; the
content is a definition or a legal text that must be read verbatim; the
slide is a title or a section divider.

### From the shape of the body to the form

What the body of a slide would be as a list decides the form. Read the left
column, pick from the right.

| The body is… | Form | Section |
|---|---|---|
| numbers compared by item, time, share, distribution or correlation | chart, type by Zelazny's comparison (`visual-design.md` section 1) | 1 |
| items compared on several attributes, some words, some marks | table (list-style) or scorecard | 3.11 |
| two positions, two options, before and after | contrast (two columns) | 3.9 |
| positions or options placed between two poles | continuum | 3.12 |
| steps in order, each depending on the one before | linear flow; cycle when the last step feeds the first | 3.1, 3.2 |
| one input, several outcomes, or several inputs, one outcome | branching or convergence; funnel when the point is the reduction | 3.3, 3.4 |
| who reports to whom, what contains what | hierarchy or tree | 3.5 |
| parts that make up a whole | parts-whole segmentation; stacked bar when parts have values | 3.6 |
| things that rest on a common base or support a common goal | pillars | 3.7 |
| levels that build on each other (maturity, capability) | layers | 3.8 |
| options placed on two criteria | matrix (2 x 2 or 3 x 3) | 3.10 |
| dated events or milestones | timeline; roadmap when work streams run in parallel | 3.13, 3.14 |
| actors or elements that influence each other | network; hub when one element connects all others | 3.15 |
| sets that overlap | overlapping sets (Venn) | 3.16 |
| causes and an effect, forces for and against, a lever | cause-effect, forces, leverage | 3.17 |
| one claim, no structure, no numbers | text: one sentence, large; or move the claim into the title and show its source | 6 |

### When not to draw

- Fewer than three data points: say the number in the title or as one big
  number, do not chart it.
- Positions nobody measured: a continuum or a matrix implies measurement.
  When the placement is opinion, say so on the slide ("Einschätzung des
  Verfassers") or use a contrast instead.
- A diagram that takes longer to read than the sentence it replaces.
- Decoration: icons, arrows or shapes that illustrate a word rather than
  prove a relation. The test: remove the element, does the slide lose a claim?
  If not, it goes.

### Exhibit ratio

Minto's and Zelazny's practice is roughly two exhibit slides for every text
slide. The Audit reports the ratio of the content slides (title, section and
closing slides excluded) as information, not as a blocker: a deck of
qualitative findings may sit below two thirds and still be right if every
"text" mark carries a reason.

## 2. The exhibit brief

Five lines before anything is drawn. They go into the Stage 2 working notes,
not onto the slide.

```
Exhibit for slide <n>
Reader and question: <who looks at this, what they must see>
Message: <one sentence, with the number or the relation it must show>
Form: <chart:<comparison> | table | concept:<type>> because <the shape of the body>
Highlight: <the one element the title's subject names>
Source and status: <source; available | placeholder | derived>
```

The brief is checked against the title: the message sentence and the title
say the same thing. If they do not, one of them is wrong. Build exhibits in
the order of the key line, all of them, before writing text slides; text
written first fills the space an exhibit should have taken.

## 3. Catalogue of concept visuals

Seventeen types in six families, checked against Zelazny's "Say It With
Charts" (concept visuals: flows, interaction, forces at work, leverage,
barriers, filters, interrelationships, segmentation) and Duarte's diagram
taxonomy in "slide:ology" (flow, structure, cluster, radiate; the Diagrammer
families flow, network, stack, segment, join). Each type: when it carries,
the trap, reading direction, caps, text budget, rendering. Caps are per
exhibit; split across two slides when exceeded.

Rendering notes name the two paths: the Slides artifact type (native
`x-shape`, `x-connector`, flex and grid boxes, inline SVG) and the pptx path
(`scripts/pptx-helpers.js`, functions in brackets).

### Family A: process (Prozess)

**3.1 Linear flow (Fluss).** Carries when steps follow in time or logic and
each depends on the one before. Trap: a list dressed as a flow; if the order
does not matter, use a list or pillars. Direction: left to right, one row;
at most eight steps, otherwise two rows with a clear return or two slides.
Text: one label per step, one line; detail in a row under the chevrons or in
notes. Barriers (Hindernisse) are a variant: a marked step or a wall across
the flow. Rendering: chevrons or boxes with arrows (`chevrons`,
`x-shape kind="arrow-right"`).

**3.2 Cycle (Kreislauf).** Carries when the last step feeds the first
(lifecycle, PDCA, continuous verification). Trap: drawing a cycle for steps
that end; a cycle promises repetition. Direction: clockwise from twelve
o'clock; at most six steps. Text: one label per node; the loop-back step is
named, not implied. Rendering: nodes on a circle with arcs or curved arrows
(`cycle`); in the Slides type as SVG or four to six boxes with `x-connector`.

**3.3 Branching and convergence (Verzweigung, Konvergenz).** Carries when
one input splits into options or several inputs meet in one outcome.
Trap: the four-way star that tells nothing; two or three branches are the
limit, more is a table. Direction: left to right; the trunk on the left for
branching, on the right for convergence. Text: label per branch, criterion
of the split named once. Rendering: boxes and connectors (`x-connector`;
pptx: boxes and `line` shapes).

**3.4 Funnel and filter (Trichter, Filter).** Carries when the point is the
reduction: many candidates, few survivors, named criteria at each stage.
Trap: a funnel without numbers or criteria is a triangle. Direction: top
to bottom or left to right, wide to narrow; at most five stages. Text:
count or share at each stage plus the criterion. Rendering: trapezoids or
nested bars (`funnel` is not provided; use `ltable` with a count column or
stacked boxes of decreasing width).

### Family B: structure (Struktur)

**3.5 Hierarchy and tree (Hierarchie, Baum).** Carries for reporting lines,
decompositions, issue trees, taxonomies. Trap: three levels on one slide
with more than twelve leaves. Direction: top to bottom; left to right for
issue trees. Text: one label per node, same grammar per level (plural-noun
test applies per level). Rendering: boxes and elbow connectors; the Slides
type has a tree recipe in its diagram references; pptx: boxes plus lines.

**3.6 Parts and whole (Teile-Ganzes, Segmentierung).** Carries when the
parts are MECE and the whole is named. Trap: parts that overlap, a
"Sonstiges" segment without a reason. Direction: left to right or clockwise
by size or by the order the message needs. Text: part names plus share when
known; with values, a stacked bar beats a pie. Rendering: segmented bar,
nested rectangles (`box` grid); pie only with five or fewer parts.

**3.7 Pillars (Säulen).** Carries when several elements support one goal and
rest on one base, with no order among the pillars. Trap: pillars used for a
sequence (that is a flow). Direction: left to right, the goal above, the
base below; three to five pillars. Text: pillar name plus one line each;
goal and base as full sentences. Rendering: cards between two bars
(`card` plus `box`).

**3.8 Layers (Schichten, Stufen).** Carries for maturity levels, capability
stacks, architectures where each layer rests on the one below. Trap: layers
that are really peers (that is pillars). Direction: bottom to top for
maturity and architecture, the highest level on top; three to five layers.
Text: level name plus a one-line criterion for reaching it. Rendering:
stacked bars of equal width or a staircase (`box` stack; stairs as offset
boxes).

### Family C: comparison (Vergleich)

**3.9 Contrast (Gegenüberstellung).** Carries for two positions, two
options, before and after, today and target. Trap: more than two columns
(that is a table); unequal depth per side. Direction: left to right, the
status quo or the weaker case left, the recommended or new case right.
Text: parallel rows, same attributes on both sides, three to five rows.
Rendering: two cards or a two-column table (`card`, `ltable`).

**3.10 Matrix (Matrix, 2 x 2).** Carries when options or items are placed on
two independent criteria and the placement is measured or explicitly
judged. Trap: axes that correlate (then it is a continuum); unmeasured
placement sold as analysis. Direction: the good corner top right; axes
named with the criterion and the scale. Text: item labels in the cells,
the quadrants named only when the names add meaning. Rendering: four
boxes with axis labels (`matrix`); dots or labels inside.

**3.11 Scorecard (Scorecard, Harvey Balls).** Carries when items are rated on
several criteria with the same scale. Trap: ratings without a stated scale
or source. Direction: items as rows, criteria as columns, the recommended
item highlighted; at most eight rows and six columns. Text: marks
(✓ ✗ ● ◐ ○) or short words, legend on the slide. Rendering: list-style
table (`ltable`, `MARK`).

**3.12 Continuum (Kontinuum, Skala).** Carries when positions sit between two
named poles (law versus contract, centralised versus local). Trap: implied
precision; the position of each item needs a source or a stated judgement.
Direction: left to right, the poles labelled at both ends; at most six
items. Text: pole names, item labels, one line on what places each item.
Rendering: a bar with markers (`continuum`); in the Slides type a flex row
with positioned labels.

### Family D: time (Zeit)

**3.13 Timeline (Zeitstrahl).** Carries for dated events in order, past and
planned. Trap: events without dates; uneven spacing that misleads about
time. Direction: left to right, time to scale or explicitly not to scale
(say so); at most eight events. Text: date plus one line per event; the
present marked. Rendering: a line with markers (`timeline`); Slides type:
flex row with a rule and labels above and below.

**3.14 Roadmap (Roadmap, Gantt).** Carries when several work streams run in
parallel over a period. Trap: more than six streams or twelve bars. Direction:
time left to right, streams as rows, milestones as diamonds. Text: stream
name plus milestone labels; owners in the row label. Rendering: bars in a
grid (`box` per bar over a `ltable`-style frame); the Slides type as a grid.

### Family E: relation (Beziehung)

**3.15 Network and hub (Netz, Wechselwirkung, Nabe).** Carries when actors or
elements influence each other and the pattern of connections is the point.
Trap: everything connected to everything, which says nothing. Direction:
the hub in the centre when one element connects all; otherwise actors
placed by their role (state left, industry right, or by level). At most
seven nodes and twelve edges. Text: node labels, edges labelled only when
the relation differs per edge. Rendering: inline SVG in the Slides type;
pptx: boxes plus lines, or `card` grid with arrows.

**3.16 Overlapping sets (Mengen, Venn).** Carries when the overlap itself is
the claim (what falls under both regulation and contract). Trap: three
circles with every intersection labelled; label only the intersections the
message needs. Direction: two or three circles, the shared region
highlighted. Text: set names plus the labelled intersections. Rendering:
SVG circles in the Slides type; pptx: `ellipse` shapes with transparency.

**3.17 Cause, effect, forces, leverage (Ursache-Wirkung, Kräfte, Hebel).**
Carries when the message is "this drives that", forces for and against a
change, or a small input with a large effect. Trap: arrows that assert
causality the evidence does not support; a fishbone with twenty bones.
Direction: causes left, effect right; forces for above or left, against
below or right; at most six causes or forces. Text: each cause one line, the
effect as a full sentence. Rendering: boxes with arrows into one box
(`chevrons` or `card` row plus `x-shape arrow-right`); fishbone as SVG.

### Variants, not types

Process maps with swim lanes (a flow with rows), the visual metaphor
(targets, bridges, puzzles): both allowed, both rare. A metaphor needs a
reason in the brief, and it never replaces the evidence.

## 4. Aligning the exhibit to the message

**The subject of the title is the highlighted element.** If the title says
"Prüfverfahren", the bar, node or row called Prüfverfahren carries the
accent colour and everything else is grey. One highlight per exhibit; two
when the message is a contrast between exactly two elements.

**Sort order follows the message.** By value when the message is a rank; by
time only for time series and timelines; by the order of the key line when
the exhibit mirrors it; never alphabetical, never in the order of the
source. The register fixes the order of a set; the exhibit uses it.

**Reading direction is fixed.** Flow and time run left to right; hierarchy
runs top to bottom; cycles run clockwise; cause sits left, effect right;
the good corner of a matrix is top right; layers grow upward. A deviation
needs a reason in the brief.

**Two titles.** The slide title states the message; the exhibit title
describes the content with measure, unit and period ("Anteil der Verfahren
mit Hochrisiko-Einstufung, 2026, in Prozent"). Never the same sentence twice.

**Scale honesty.** Zero baseline on bars; equal scales on charts shown side
by side or in a series; a broken axis is marked; a continuum or matrix with
judged placement says so on the slide.

**Direct labels.** Label the elements on the exhibit; a legend only when
direct labels would overlap. The one number the title needs sits at its
data point with a line to it, not in a box beside the chart.

**Register inside the exhibit.** Axis labels, legend entries and node names
use the register's names, order and, where defined, colours. The same
entity has the same colour on every slide of the deck.

**Gestalt in one paragraph.** Elements near each other are read as one
group; elements that look alike are read as related; a frame separates;
a line asserts a relation. Use proximity and similarity before frames and
lines, and draw a line only where the claim is "these two are related".

## 5. Cleaning

Run the sequence on every exhibit after it is built, in this order. For
charts, `visual-design.md` section 6a (Knaflic) applies first; this is the
sequence for concept visuals and for what the chart sequence does not cover.

1. Remove icons that illustrate a word instead of proving a relation.
2. Remove frames around text that is already grouped by position.
3. Remove shadows, gradients, 3D, rounded decorations that carry no meaning.
4. Merge duplicate arrows; one arrow per asserted relation.
5. One label per node, one line; a second line moves to notes or to the body.
6. Equalise stroke widths and box sizes; snap to the grid.
7. Replace a legend by direct labels where they fit.
8. Only now apply colour: grey for structure, one accent for the highlight,
   the signal colour for a gap or warning.

**Caps.** Five to seven nodes per diagram; one comparison type per chart;
one highlight; one exhibit per slide (two only as a deliberate contrast).

**Squint test.** View the slide blurred or from a distance: exactly one
element stays dominant, and it is the one the title names. If two compete
or none stands out, go back to step 8.

**Cover test and headline test.** Cover the title: can a reader state the
message from the exhibit? Cover the exhibit: does the title stand without
it? If the first fails, the exhibit does not prove the title; if the second
fails, the title is a caption, not a claim. If both fail, the slide is cut.

**Text inside exhibits.** No rotated text; no abbreviation that is not in
the register; type at least as large as body text in the current density
mode; one number format for the whole deck.

## 6. Text budgets by density mode

The density mode is declared once per deck in the ghost deck header and never
mixed within a deck. Words are counted on the slide body (title and footer
excluded); the audit counts them.

| Mode | Body words per content slide | Dominant element | Where the detail lives |
|---|---|---|---|
| speaker-led (Vortrag) | up to about 40; a single sentence of 15 to 25 words when the exhibit is text | one exhibit, labels only | speaker notes |
| reading-first (Lesedeck, handout) | 75 to 250 | one exhibit plus explanatory text | on the slide, with sources |

**"Both" (Vortrag und Lesefassung).** Build the reading deck first from the
approved ghost deck; then derive the speaker deck by cutting each slide to
its exhibit and the labels, moving the explanatory text into the notes. The
two decks share titles, register and exhibits; only the text layer differs.
Never ship one deck that tries to be both.

**Cutting to budget.** Cut explanatory sentences before labels, labels before
the exhibit, and the exhibit never. If the exhibit alone exceeds the budget
(a table with long cells), the exhibit is wrong for a speaker deck: shorten
the cells or move the table to the reading deck and show its one message as
a big number or a contrast.

## 7. Host constraints

**Slides artifact type (claude.ai).** Build diagrams with native elements
(`x-shape`, `x-connector`, flex and grid boxes, inline SVG), never as raster
images, so they stay editable. The type does not allow a render check from
the build environment; run the text-dump check (words per slide, register
names) and an element count (nodes, edges, highlights) instead, and say in
the delivery note that the visual check was not run and which slides are the
densest. Design System artifacts carry colours and type; the catalogue's
shapes are built inside each slide.

**pptx path (`scripts/pptx-helpers.js`).** Primitives for flow (`chevrons`),
cards, list tables, big numbers, cycle (`cycle`), continuum (`continuum`),
timeline (`timeline`) and matrix (`matrix`). Diagrams the helpers do not
cover are built from `box` and line shapes, never as images. `write()`
returns `wordsPerSlide` for the budget check; `scripts/deck-metrics.py`
reports words, exhibit ratio and highlights for a finished `.pptx` or for a
Slides-type `slides/` folder.

**Markdown fallback.** When neither path exists, the exhibit is described in
one line under the title ("Exhibit: Kreislauf mit vier Knoten, Knoten 3
hervorgehoben") so that whoever renders it later knows what to draw.

## 8. Frequent failures and the fix

| Failure | Looks like | Fix |
|---|---|---|
| Reading deck in speaker clothes | 100 words of body text under a two-line title in a "speaker-led" deck | declare the mode honestly, or cut to the exhibit and move text to notes |
| Text decided before form | cards with three sentences each | form mark at the gate; exhibits built before text |
| Decorative diagram | arrows between nouns, icons per bullet | remove-and-test: no lost claim, no element |
| Wrong family | a sequence drawn as pillars, peers drawn as layers | the shape-to-form table in section 1 |
| No highlight | all bars, all nodes the same colour | the title's subject gets the accent |
| Source order | items in the order the speaker said them | sort by the message |
| Implied precision | options placed on a 2 x 2 by feel | say "Einschätzung" on the slide, or use a contrast |
| Overcrowded | nine nodes, twenty edges | split, or raise the level of abstraction and move detail to backup |
| Legend hunting | a legend in the corner for four series | direct labels |
| Catch-all segment | "Sonstiges" as a peer | name it, merge it, or justify it on the slide |
