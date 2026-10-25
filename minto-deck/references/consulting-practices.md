# Consulting practice for slides

Conventions that strategy consultancies use on top of the Pyramid Principle.
They are craft rules, not brand property; do not claim affiliation with any
firm and do not imitate a firm's template.

## Quick checklist

- [ ] Slide anatomy fixed: action title, body with one dominant element, source line, tracker, page number
- [ ] Every action title passes disagreement, cover, one-claim, specificity, verb and parallelism tests
- [ ] One message per slide; density mode fixed once and kept
- [ ] Management summary states conclusions, drafted from the ghost deck, finalised last
- [ ] Numbers carry unit, period, denominator, source; nothing invented, placeholders marked
- [ ] Chart chosen by the comparison the title makes; tables in list style; two or three rows become cards or a list
- [ ] Subsets name their universe and criterion; entities from the register, same name and order everywhere
- [ ] Decision slide worded as a proposal; options shown before the recommended option's detail; next steps with owner and date
- [ ] Dividers only in long decks; section lead slide for sections with three or more evidence slides
- [ ] Layout: body fills the zone, peers equal, connectors attached, no orphan labels, no wrapped key-value lines

Detail follows; the checklist is what gets ticked before delivery.

## 1. Slide anatomy

Every content slide has the same parts in the same places:

- **Action title** (top): the one claim the slide proves. Full sentence, one to
  two lines, same position and size on every slide.
- **Body**: the evidence. One dominant element: a chart, a table, a diagram or a
  short text block. Two competing elements means two slides, unless the slide's
  job is the comparison.
- **Takeaway or "so what" box** (optional, bottom right or beside the chart):
  one line that says what the evidence means for the decision. Use it when the
  title states the fact and the implication still needs saying.
- **Source line** (bottom left, small): source, year, sample, unit. Every
  external number has one.
- **Tracker** (top or side): which section of the key line this slide belongs
  to. The tracker uses the key-line wording, shortened.
- **Page number** and classification where required.

The title says what, the body shows why, the source line says where from.

## 2. Action titles

The title is the claim; the body is the proof. Tests, in order:

1. **Disagreement test**: can the audience disagree with it? If not, rewrite.
2. **Cover test**: hide the body. Does the title still carry the point? If the
   chart carries the argument and the title only names it, rewrite.
3. **One-claim test**: does the title make exactly one point? Split otherwise.
4. **Specificity test**: numbers, counts, named causes instead of "significant",
   "various", "a number of".
5. **Verb test**: a dynamic verb (cut, doubled, blocks, drives, misses) beats a
   linking verb (is, has, shows). Keep a linking verb only for a static fact.
6. **Parallelism test**: inside a section, all titles share one grammatical
   form.

| Topic title | Action title |
|---|---|
| Ticket volumes 2023-2025 | Ticket volume grew 40 % while headcount stayed flat |
| Risk overview | Two of the five risks need a decision this quarter; three are covered |
| Options | Option B meets all three criteria; A and C each miss one |
| Next steps | Approval today keeps the Q1 start date |

## 3. Horizontal flow: the dot-dash storyline

Before building slides, write the storyline as dots and dashes: each dot is a
slide title, each dash under it is a body point. Reading the dots alone must
give the argument; reading the dashes under one dot must prove that dot and
nothing else. The ghost deck is the dot layer; Stage 2 adds the dashes before
any visual work.

Checks on the flow:

- No two adjacent slides make the same claim.
- No jump from finding to recommendation without the slide that connects them.
- Every section boundary has a transition the notes can speak.
- The closing restates the governing thought in the words of slide 2.

## 4. One message per slide

A slide with two messages gets half the attention for each. Symptoms: a title
with "and", a body with two charts, a slide that needs two minutes of talk to
explain. Fix by splitting, or by promoting one message to the title and moving
the other to the notes or backup.

The audience should grasp the slide in a few seconds (glance test) when the
deck is presented. For reading decks the test is different: does the slide make
sense when forwarded without any context?

## 5. Density modes

Decide once per deck. Do not blend.

| | Speaker-led | Reading-first |
|---|---|---|
| Words on slide | few; the presenter carries the detail | enough to stand alone |
| Type size | large (body 18 pt and up) | smaller (body 12 to 14 pt) |
| Slide count | higher, one idea per slide | lower, denser slides |
| Sources | source line | source line plus footnotes |
| Notes | full speaker notes | optional, short |
| Typical use | board meeting, talk | pre-read, email, handout |

A handout variant converts a speaker-led deck to reading-first: the key points
from the notes move onto the slide, delivery cues are removed, sources stay.

## 6. Management summary

Slide 2 in almost every deck type. Contents, in this order:

1. The governing thought as the slide title.
2. The key line as three to five bullets, same wording as the section headers.
3. The ask, if the deck type has one: decision, budget, approval, next step.
4. Key numbers where they make the claim concrete.

It summarises conclusions, never topics. "We looked at costs, risks and
timeline" is an agenda, not a summary. The summary must survive on its own:
a reader with only this slide knows what is proposed and why.

Before and after:

```
Before (agenda in disguise)            After (conclusions)
Management Summary                     Ein Board plus drei bestehende Prozesse erfüllen die KI-VO fristgerecht ohne neue Stellen
- Ausgangslage und Rechtsrahmen        - Die KI-VO verpflichtet die Behörde als Betreiberin; heute ist niemand zuständig.
- Analyse der Prozesse                 - Drei Prozesse, die jedes KI-System durchläuft, tragen [x] der [n] Pflichten.
- Governance-Optionen                  - Ein Governance-Board übernimmt Inventar, Einstufung und Freigabe.
- Umsetzung und nächste Schritte       - Umsetzung in [x] Monaten mit vorhandenem Personal.
                                       Beschlussvorschlag: Board einsetzen, Umsetzungsplan freigeben.
```

Draft it from the ghost deck, finalise it last: after every other slide exists,
rewrite it against them so that each line is a claim a slide proves and each
number matches. Format follows the density mode (`visual-design.md` section 8):
lean for speaker-led decks; for reading decks bold key-line sentences with
evidence bullets, or the three-column form situation and complication,
findings, recommendation.

## 7. Evidence discipline

- Distinguish facts, calculations, interpretations and hypotheses. Label a
  hypothesis as such on the slide and in the notes.
- Every number carries unit, period and denominator. "Costs fell 20 %" needs
  "of what, from when to when".
- Do not invent numbers, examples, quotes or sources. Insert
  `[PLACEHOLDER: …]` and list it in the delivery note.
- Old data presented as current is a blocker.
- A calculation on a slide is reproducible from the source line.

## 8. Charts

The chart's job is to show one comparison that proves the title. First name
the comparison the title makes (component, item, time series, frequency,
correlation; or in the four-type shorthand: composition, comparison,
distribution, relationship), then choose the chart. Detail and craft rules in
`visual-design.md` section 6. Summary:

| Comparison in the title | Chart |
|---|---|
| parts of a whole (share, composition) | stacked bar or pie (pie only for one series, few parts) |
| items ranked against each other | horizontal bar |
| change over time | line (many periods) or column (few periods) |
| distribution (how many fall into each range) | histogram or column |
| relationship between two variables | scatter |
| flow or sequence | process diagram, waterfall for bridges |

Rules:

- The chart title states the message, not the metric ("Resolution time doubled
  since 2023", not "Resolution time 2023-2025").
- Label data directly; drop the legend when one series is shown.
- Highlight the element the message is about; grey the rest.
- Remove grid clutter, 3D, decorative colour.
- Units, period, source, sample on every chart.
- Keep charts native and editable; never paste a screenshot of a chart.
- A table replaces a chart when the audience needs the exact values; a sentence
  replaces both when the comparison has two numbers.

## 9. Diagrams and frameworks

Use a framework only when it structures the argument (options matrix,
timeline, issue tree, process). An empty 2x2 with four buzzwords is decoration.
Every box in a diagram is a claim or a step the title needs.

## 10. Backup and appendix

Goes to backup: detail that supports a slide but is not needed to follow the
argument; evidence for anticipated questions; method, data definitions,
alternative scenarios; anything with "could" cut priority.

Does not go to backup: a slide the argument needs. A thin main deck with a fat
appendix usually hides a storyline problem.

Each backup slide follows the same anatomy and has an action title. The Q&A
document references backup slides by number.

## 11. Decision and next-steps slides

A decision paper ends with a proposal the audience decides on, not an order
the presenter issues. Title the slide as a proposal ("Beschlussvorschlag",
"Proposed decision") and word the body as what the body is asked to decide
("Die Leitungsrunde beschließt: 1. … 2. …"). The directive form ("Entscheidung
heute: …") is for presenters with the authority to direct; everyone else
proposes. The slide carries: the decision in one sentence, the options with the
recommended one marked (or a pointer to the options slide), what is needed from
the audience today, and what happens if nothing is decided. The next-steps
slide lists actions with owner and date for every line. A talk ends with the
restated governing thought and what the audience can do with it.

## 12. Consistency

- Same term for the same thing throughout; the glossary fixes the pairs.
- Named entities (processes, bodies, roles, systems, options) come from the
  ghost deck's register: same name, same order, same category on every slide
  where the set appears. A member that appears on one slide and not on the
  next needs a stated reason.
- Number format, units, date format consistent across slides.
- Titles at the same height and size; trackers in the same place.
- Parallel grammar inside each peer set.
- Colour carries meaning or is absent. One accent colour marks the element the
  title is about; a second accent only for a second meaning (e.g. gap vs.
  recommendation). Grey is for containers and secondary text, never for the
  message. More than two greys on a slide reads as unfinished.

## 13. Selections: name the universe

When a slide or section works with a subset (three of the agency's processes,
two of five risks, the top three options), the audience will ask "why these?".
Answer before they ask: name the universe ("of the n processes every AI system
passes through"), the selection criterion, and where the rest is documented
(backup). A subset without a universe looks arbitrary even when it is right.

## 14. Section dividers and section lead slides

A bare divider costs a slide and says nothing. Three cases:

- Section with one or two evidence slides: no divider, no lead slide. The
  tracker, the management summary and the section wording carry the structure.
- Section with three or more evidence slides: a **section lead slide** that
  carries the key-line claim as title and the section's evidence in compressed
  form (the following titles as bullets, or a mini version of the key exhibit).
  The reader can stop after the lead slide and still have the argument.
- Decks of roughly 20 slides and more, or sections presented by different
  people: dividers are acceptable in addition, with the key-line claim as title
  and nothing else. No images unless the image is an argument.

One divider before the backup is always fine.

## 15. Layout and geometry

The pyramid is argued in the titles; the body still has to look deliberate.

- **Fill and balance.** The body uses the content area. Whitespace is
  distributed around elements, not pooled at the bottom or right. If a
  speaker-led slide has little text, scale type and shapes up; do not leave
  a quarter of the slide empty.
- **Grid.** One column grid per deck (12 columns or a fixed set of widths),
  one gutter width, elements aligned to it. Equal peers have equal widths.
- **Size follows content.** Boxes are as tall as their text plus padding, not
  taller; a row of peer boxes shares the tallest height. Big numbers are sized
  so the label beneath them still fits.
- **Connectors attach.** Every arrow or line starts and ends on a shape edge.
  A box that other shapes point to spans the width of what points to it.
- **No orphan labels.** A caption or note belongs visually to the element it
  describes; a label floating between two elements is removed or attached.
- **Key-value lines.** Several "label: value" pairs never share one line;
  they become columns or a small list. A wrapped line of pairs is an error.
- **Check in full size.** Thumbnails hide overlaps, floating connectors and
  wrapped lines. Render every slide at full size and look at it before
  delivery.

## 16. Tables

A consulting table is a list with alignment, not a spreadsheet.

- No vertical rules. Thin horizontal rules between rows, a slightly stronger
  one under the header.
- Header as bold text over a rule, not a dark filled band.
- Left-aligned text, right-aligned numbers, centred marks.
- Row height with air: at least 1.6 times the text height.
- Highlight one column (the recommendation) or one row with a light fill;
  never alternate row bands and a highlight at once.
- Marks instead of words where a mark is enough: ●, ○, ✓, ✗, Harvey balls.
- Two or three rows are not a table. Use cards (risks), a list with a rule
  per row (next steps), or a timeline (dates).
- Tables longer than eight rows go to backup or get split by the key line.

## 17. Length guidance

| Deck type | Typical main deck | Notes |
|---|---|---|
| Decision paper, 30 min | 8 to 12 slides | plus backup |
| Status report, 15 min | 4 to 7 slides | management summary mandatory |
| Proposal or pitch, 45 min | 12 to 20 slides | includes team, approach, price |
| Expert talk, 20 min | 10 to 15 slides, speaker-led | low density |
| Reading deck, pre-read | 6 to 15 slides, reading-first | no notes needed |

Fewer slides with sharper titles beat more slides with weaker ones. Cut slides
to fit the slot; do not shrink type.

## 18. Anti-patterns

- Agenda slide that lists topics instead of the key line.
- "Overview", "Background", "Analysis" as titles.
- A chart with a title that names the metric.
- Three bullets of context before the first claim on a slide.
- Slides that only exist because the material was there.
- Appendix used to avoid cutting.
- Framework labels on slides ("Situation", "Complication", "MECE").
- Decorative icons, stock photos, gradients, animations that carry no meaning.
- Spreadsheet-style tables with dark headers and vertical rules.
- A row of peers where one member belongs to a different category (two
  documents and a function; three processes and a committee).
- A subset shown without naming what it was selected from.
- Dividers in a twelve-slide deck.
