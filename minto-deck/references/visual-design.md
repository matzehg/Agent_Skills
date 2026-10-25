# Visual design for consulting-style slides

How a deck looks once the argument stands. Rules in the skill author's own
words, distilled from the sources listed at the end; no template, slide or text
from any source is reproduced. Read in Stage 2 before building slide bodies,
and in Audit mode for the form checks (G-section of the checklist).

The order matters: message, then layout, then design. A slide whose title is
not yet a claim has no layout problem worth solving.

## 1. Message first, layout second

Write the slide title as a full claim. Then ask which comparison or relation
the body has to show to prove it. Only then pick the layout. Picking the
layout first produces accurate slides that argue nothing. The title is the
chart's job description: the chart exists to prove that sentence and nothing
else.

Before finalising any body element:

- Does the title say what the body actually shows? A title "grew 40 %" over a
  chart with three mixed years contradicts itself.
- Is the most important element the most visible one? Colour, contrast or a
  callout mark the one data point the title rests on; everything else recedes.
- Can anything be cut without weakening the proof? Cut it or move it to backup.
- Would a simpler form say the same? Fewer lines, fewer stacks, a bar instead
  of a stacked bar, a sentence instead of a chart with two numbers.

## 2. Layout catalogue

Almost every consulting slide is one of these patterns. Decide which one the
title needs; the pattern then fixes what information belongs on the slide.

| Pattern | Use when the title… | Build | Trap |
|---|---|---|---|
| **Big number** | rests on one figure | the figure large, one line of context, nothing else | adding a chart or bullets beside it kills the number |
| **Column or bar chart** | compares items, ranks, or shows change over few periods | columns side by side, direct labels, highlight one | pie charts; stacked bars when a plain bar works |
| **Chart with insight callout** | needs the reader to draw one conclusion from data | chart left two-thirds, takeaway box right third, arrow to the exact data point | leaving the chart to "speak for itself" |
| **Two-column comparison** | contrasts before/after, A/B, current/target | identical row structure on both sides, differences coloured | asymmetric rows; a table where contrast is the point |
| **Three (or n) pillars** | names the parts of a strategy or the reasons for a claim | equal cards across the middle, label plus one line each, optional icon per pillar reused later as navigation | forcing three when there are two or four |
| **Process flow** | explains how something works or will happen | four to five chevrons or boxes with label and one line; owners, dates or deliverables beneath | twelve steps with paragraphs; group into phases instead |
| **Waterfall / bridge** | shows how a start value becomes an end value through named levers | bars that add and subtract to the total | levers that do not sum; overlapping effects |
| **Funnel** | shows drop-off along stages | narrowing bars, the problem stage coloured, callout on the largest drop | explaining every stage; the gap is the story |
| **2x2 / framework grid** | prioritises items on two dimensions | labelled axes, items as bubbles, quadrant labels as implications | two axes that are merely the easiest to measure |
| **Harvey-ball scorecard** | compares options on several criteria where "mostly meets" is the honest precision | criteria as rows, options as columns, filled circles; recommended option highlighted | scores out of ten that invite arguments about decimals |
| **Quote plus evidence** | makes a research finding human and representative at once | one specific quote with a number in it, the supporting statistic beside it | generic quotes; quotes without data |
| **Timeline / roadmap** | shows milestones over time | milestones on the line, phase bars above, risks or dependencies below, the end milestone emphasised | a Gantt chart pasted onto a slide |
| **Dashboard** | reports status on several metrics at once | four to six tiles with number, trend and sparkline; one or two panels on what needs attention | twelve tiles; everything green |
| **Executive summary** | compresses the whole deck | see section 8 | writing it before the thinking is finished |

Two patterns from this skill's own practice: the **options table** (criteria as
rows, options as columns, marks instead of words, recommended option
highlighted) and the **decision proposal** (what is decided, consequence of no
decision, what is needed today).

## 3. Slide zones and grid

Every content slide has the same zones in the same place: title zone at the
top, tracker top right, body zone, footer zone with source and page number.
Fixing the zones once is what makes a deck look like one deck.

- One grid for the whole deck. Twelve columns or a fixed set of column widths
  (halves, thirds, quarters, fifths), one gutter width.
- Peers are equal: same width, same height, same padding, same type size.
- Everything aligns to something: left edges to the title's left edge, tops of
  a row to one line, bottoms of a row to one line.
- Whitespace is structure, not leftover. It groups what belongs together and
  separates what does not. It is distributed around elements, never pooled in
  one corner.
- The body fills the body zone. If a speaker-led slide has little content,
  scale type and shapes up rather than leaving a third of the slide empty.
- Proximity carries meaning: a label near an element belongs to it; a label
  equidistant from two elements belongs to neither and is removed or attached.

## 4. Typography

- One type family, two weights (regular, bold). A second family only when the
  template prescribes it.
- A size system, fixed per deck and used on every slide: title, body, label,
  source. Nothing in between. The same element has the same size on every
  slide.
- Speaker-led decks: body 16 pt and up, titles 22 to 28 pt, source 10 pt.
  Reading-first decks: body 12 to 14 pt, titles 18 to 22 pt, source 9 to 10 pt.
  Nothing below 10 pt anywhere. The body text size never shrinks to make a
  layout fit; the layout changes instead.
- Full-sentence action titles may take two lines. Three lines means the title
  is too long or the type too large; shorten the title first.
- Hierarchy by size and weight, not by colour or italics. Bold marks the
  element the eye should land on first; bolding everything marks nothing.
- Left-aligned text throughout; centred text only inside boxes and chevrons;
  right-aligned numbers in tables.
- Small caps or letter-spaced labels for zone names (tracker, section labels
  inside cards) distinguish them from content without a second colour.

## 5. Colour

Three roles, assigned once per deck:

1. **Base**: dark text colour, white or near-white background, one or two
   greys for containers and secondary text.
2. **Accent**: one colour that marks what the title is about: the highlighted
   bar, the recommended column, the gap boxes, the current phase.
3. **Signal**: one colour for a second meaning when the deck needs it, usually
   warning or gap (a red or brick) against the accent's positive meaning.

Rules:

- Grey is for containers, rules and secondary text, never for the message.
  More than two greys on a slide reads as unfinished.
- Colour means the same thing on every slide. If the accent marks "recommended"
  on slide 8, it does not mark "phase 1" on slide 11 with the same shade.
- No gradients, shadows, 3D or decorative colour blocks. A filled band is
  acceptable when it carries a role (the board bar that everything points to).
- Contrast: body text on its background at least 4.5:1; large text 3:1. Avoid
  red/green as the only distinction; pair colour with position, a mark or a
  label so the slide works in greyscale.
- Firm palettes (navy and electric blue, green over a double rule, black,
  warm) are reference points for restraint, not for imitation. The user's
  template palette wins when one exists.

## 6. Charts

Charts are evidence, not decoration. Start from the comparison the title makes
(Zelazny's five): component (parts of a whole), item (ranking), time series
(change over time), frequency distribution, correlation.

| Comparison | Chart | Note |
|---|---|---|
| component | stacked bar or column; pie only when one part exceeds half and that dominance is the message | even then a column usually works better |
| item | horizontal bar, sorted by value | highlight the one the title is about |
| time series | line for many periods, columns for few | one to three lines; six lines means the message is unclear |
| frequency | column chart (histogram) | |
| correlation | dot (scatter) chart | the one case for a less common form |

Bar, column and line cover almost everything. Waterfalls for bridges, funnels
for drop-offs, Harvey balls for scorecards; Mekko, bubble and radar charts only
when nothing simpler proves the title. Time series run horizontally, structural
comparisons vertically as bars. Where actuals, plans, forecasts or previous
periods appear, use the scenario fills and variance notation of
`ibcs-notation.md` section 8.

The same data tells different stories depending on the axis and the
highlight. Stacked bars with companies on the axis argue "different mix";
grouped columns with regions on the axis argue "different by region"; one bar
highlighted argues "this company leads here". Pick the arrangement that proves
the title, not the first one the tool offers.

Chart craft:

- The slide's action title carries the message. The chart's own title is
  descriptive (measure, unit, dimension, period) so the chart stands alone when
  copied out; see `ibcs-notation.md` section 1. A chart without an action
  title above it gets the message as a sentence directly above the chart.
- Label data directly; drop the legend when one series is shown.
- Highlight the element the title is about; grey the rest.
- Sort bars by value unless the order has meaning (time, process).
- Start value axes at zero for bars and columns.
- Remove gridlines, borders, tick clutter, 3D.
- Units, period, source and sample on every chart.
- Keep charts native and editable; never a pasted image.

## 6a. Decluttering a chart, in order

A fixed sequence, after Cole Nussbaumer Knaflic's practice, applied to every
chart before it goes on a slide. Each step removes or adds one thing; stop
when the chart proves the title and nothing else.

1. Name the one point the chart must make (the slide title or, without one,
   a sentence above the chart).
2. Pick the simplest form that shows that comparison (section 6).
3. Remove: chart border, gridlines, tick marks, background fill, 3D, drop
   shadows, the legend when series can be labelled directly, data labels on
   points the message is not about, trailing zeros and excess decimals,
   diagonal text.
4. Align: labels left, numbers right, one axis label orientation, the same
   font and size as the slide body.
5. Grey everything, then colour only the element the point rests on. If two
   elements must be compared, colour both and nothing else.
6. Add what directs attention: a direct label on the highlighted element, a
   thin reference line (target, average, previous year) if the comparison
   needs one, a short annotation in a sentence where the chart alone would
   leave a question.
7. Check the result against the title: can a reader state the title from the
   chart alone?

Preattentive attributes do the work in step 5 and 6: colour, size, position
and enclosure are seen before reading starts; use one or two, never all.

## 6b. Tables that are read, not looked up

For tables in reading decks and backup, after Stephen Few's rules for tables
that support comparison:

- Rows and columns ordered for the comparison the reader will make (by size,
  by time, by category), not alphabetically unless lookup is the purpose.
- Numbers right-aligned with equal decimals; units in the header; thousands
  separators; negative values with a sign, not in parentheses, unless the
  template says otherwise.
- Group columns with white space, not rules; one thin rule under the header,
  totals set off by a rule above and bold.
- Highlight one row or column by light fill; mark one or two cells by a
  bolder weight or a small symbol. Never alternate row bands and a highlight
  on the same table.
- Delete columns the message does not need; move the rest to backup.
- A table longer than eight rows on a projected slide is a backup table.

## 7. Tables, scorecards, callouts

- Tables follow the list style in `consulting-practices.md` section 16: no
  vertical rules, thin horizontal rules, header as bold text over a rule, one
  highlighted column or row at most.
- Scorecards use marks (●, ◐, ○, ✓, ✗) instead of words or decimals; the
  pattern of marks is the argument.
- The insight callout is the most reliable consulting device: a short box with
  the takeaway, placed beside the evidence, with an arrow or highlight to the
  exact element. Use it whenever the title states the finding and the
  implication still needs saying.
- Pills or small filled labels for owners, status and dates; one shape, one
  size, used consistently.

## 8. The executive summary slide

Written last, placed second. Formats by density mode:

- **Speaker-led**: governing thought as title, key-line claims as three to five
  lines, the ask in a box. Nothing else; the presenter carries the rest.
- **Reading-first**: three columns (situation and complication | findings |
  recommendation and next steps), or bold key-line sentences each followed by
  one to three evidence bullets with numbers. The bold sentences alone must
  read as the storyline; a reader with only this slide knows what is proposed,
  why, and what it costs.

A draft exists from Stage 1 (governing thought plus key line); the final
version is written after every other slide, when the numbers are known, and is
checked against the slides it summarises.

## 9. Section lead slides

A divider that carries only a title costs a slide and says nothing. When a
section has three or more evidence slides, open it with a section lead slide:
the key-line claim as title, the section's evidence in compressed form (the
titles of the following slides as bullets, or a mini version of the key
exhibit), and the tracker set to the section. With one or two evidence slides,
no lead slide; the tracker and the management summary carry the structure.

## 10. Icons and images

- An icon earns its place by doing a job: identifying a pillar and reappearing
  on later slides that belong to it (navigation), or replacing a word that
  would otherwise repeat (an owner, a system). One icon set, one weight, one
  size.
- Decorative icons beside bullets, stock photos, illustrations and background
  graphics are noise. A photo belongs on a slide only when the photo is the
  evidence (a site, a product, a screen).
- Diagrams are built from the deck's shapes and colours, not pasted from
  elsewhere, so they stay editable and consistent.

## 11. Consistency as a system

Define page types once and give each stable rules: title slide, executive
summary, section lead, chart slide, table slide, comparison, framework,
timeline, decision proposal, next steps, appendix. Same zones, same type
sizes, same colour roles. Consistency does not mean every slide looks alike;
it means every slide of the same type looks alike, and nothing on any slide is
there by accident.

## 12. Visual check before delivery

Render every slide at full size and look at it, one by one.

1. Does the layout pattern match what the title claims?
2. Is the one element the title rests on the most visible thing on the slide?
3. Are peers equal, edges aligned, connectors attached, labels adjacent?
4. Is whitespace distributed, with the body zone used?
5. Are type sizes from the deck's size system, nothing below 10 pt, titles at
   most two lines?
6. Are colours in their roles: one accent, one signal, grey only for
   containers?
7. Do tables follow the list style; do charts state their message, label
   directly, highlight one element, start at zero?
8. Is anything on the slide decorative? Remove it.

## Sources

Paraphrased, no content reproduced. Add further sources as new entries and
note which rules they changed.

- Gene Zelazny, *Say It With Charts* (McGraw-Hill): five comparison types,
  chart selection, message-first titles. Sections 1, 6.
- Nancy Duarte, *slide:ology* (O'Reilly): whitespace as breathing room, the
  three-second glance for presented slides, contrast, hierarchy, restraint.
  Sections 3, 4, 10.
- Garr Reynolds, *Presentation Zen* (New Riders): signal-to-noise, restraint,
  one idea per slide for presented decks. Sections 3, 10.
- Barbara Minto, *The Pyramid Principle*: the argument the design serves; see
  `minto-pyramid.md`.
- StrategyU, "The 14 Slide Layouts That Consulting Firms Use for Everything"
  (Paul Millerd, 2026): layout catalogue, executive summary written last.
  Section 2, 8. https://strategyu.co/slide-layouts
- StrategyU, "Think Before You Chart" (2026): message before chart, bar/column/
  line default, pie-chart rule, same data four stories, chart checklist.
  Sections 1, 6. https://strategyu.co/think-before-you-chart
- Slidescience, course summary and "What is an action title?": top-down
  structure, SCR storyline, action-title practice (quantify, avoid the
  obviously true), chart insight types, executive summary format.
  Sections 6, 8, 9. https://slidescience.co
- thinkinsights.net, "Designing Effective Slides": Duarte's principles applied
  to consulting decks. Sections 3, 4.
- Cole Nussbaumer Knaflic, *Storytelling with Data* (Wiley, 2015): context
  first, appropriate display, eliminate clutter, focus attention with
  preattentive attributes, think like a designer, tell a story. Section 6a,
  from the author's prior knowledge of the book, not re-read for this file.
- Stephen Few, *Show Me the Numbers* (Analytics Press, 2nd ed. 2012): table
  and graph design for business communication. Section 6b, from the author's
  prior knowledge of the book, not re-read for this file.
- IBCS Standards, see `ibcs-notation.md`: scenario notation, time horizontal
  and structure vertical, data labels over axes, descriptive chart titles.
  Sections 6, 6a.
- General visual-design principles (Gestalt proximity and similarity, WCAG
  contrast ratios): sections 3, 5.
