# IBCS: rules and notation for numbers in decks

The International Business Communication Standards (IBCS, Hichert and Faisst)
are a free, Creative-Commons rule set for reports, presentations and
dashboards, built on Minto (content), Zelazny, Tufte and Few (perception) and a
semantic notation of their own. Version 2.0 (June 2026) is aligned with
ISO 24896 "Notation for business reporting" and regroups the rules into
Notation and Composition; this file follows the public text of versions 1.1
and 1.2, whose substance is unchanged. Everything below is paraphrased.

Use this file in Stage 2 whenever a slide shows numbers in a chart or table:
status reports, business cases, anything with actuals, plans, forecasts or
variances. For decks without quantitative content, `visual-design.md` is
enough.

## 1. Where IBCS and this skill agree, and where they differ

Agree: message first, one message per page, precise words, evidence on the
page, sources named, consistent items and wording (MECE), deductive or
inductive groups, no decoration, colour only for meaning, data labels instead
of gridlines, right-aligned numbers, no truncated axes, no pie charts.

Differ, and how the skill resolves it:

- **Density.** IBCS asks for small fonts, narrow margins and high information
  density; it is written for reports and dashboards read at a desk. Duarte and
  consulting practice ask for large type and air on projected slides. The
  skill's density mode decides: reading-first decks and handouts follow IBCS
  density; speaker-led decks follow `visual-design.md` section 4. IBCS itself
  says text slides do not belong in presentations and that sources may be
  omitted on projected slides but never in written material.
- **Title versus message.** IBCS separates the *message* (an evaluative
  sentence, placed in the same spot on every page) from the *title* (a neutral
  description of what the object shows: measure, unit, dimension, period). In
  this skill the slide's action title is the IBCS message; the chart or table
  then carries a descriptive title so that it stands alone when copied out.
  This replaces the earlier rule "chart title states the message": the slide
  title does; the chart title describes.
- **Scenario notation.** IBCS adds a layer the consulting sources do not have:
  fixed fills for actual, plan and forecast. Adopt it whenever such scenarios
  appear; it costs nothing and is understood across the German-speaking
  corporate world.

## 2. SAY: convey a message

- Know the goal (inform, explain, or obtain a decision) and the audience
  (what they know, what they will object to) before writing anything.
- Open with situation, complication and the question; then state the message
  as a complete sentence. Messages detect, explain or suggest; a detection is
  checkable and must be precise.
- Say the message first, then prove it. Exception: bad news in a live setting,
  or cultures where directness offends; then prepare the ground first.
- Prove on the page. A slide should prove the speaker's message itself, not
  wait for the speaker to explain it.
- Precise words. "Relevant", "significant", "various" are not statements.
- Highlight the message in the object: the bar, cell or number the message is
  about carries a visible mark. Pages without a highlight are statistics, not
  reports.
- Name sources in written material; link numbered comments to the elements
  they explain; general comments as footnotes.
- End a presentation by repeating the message in one sentence and stating the
  decision and its consequences. Never end on "thank you for your attention".

## 3. STRUCTURE: organise content

- Items in a group are of one kind (ST 1.1), statements in a list are of one
  type, detections not mixed with suggestions (ST 1.2), wording is
  grammatically parallel (ST 1.3), symbols and pictures in a list share one
  style (ST 1.4). This is the same rule the register in the ghost deck
  enforces.
- Groups are mutually exclusive and collectively exhaustive, in report
  chapters, in measures and in structure dimensions; a remainder element
  ("rest of…") makes a structure exhaustive.
- Deductive chains (statement, comment, conclusion) for controversial
  arguments; inductive groups (homogeneous, exhaustive) for comprehensible
  ones. Same as `minto-pyramid.md` section 5.
- Make the structure visible: outlines, trackers, hierarchical rows and
  columns in tables, structured notes.

## 4. EXPRESS: choose the right object

- Tables are for looking up values; they are neutral and dense. Charts are
  for conveying a message; they are selective by nature. One does not replace
  the other.
- **Time runs horizontally.** Time series use a horizontal category axis, left
  to right, as columns (few periods) or lines (many periods).
- **Structure runs vertically.** Comparisons of products, regions, units use
  horizontal bars on a vertical category axis, top to bottom, sorted by the
  analysis; no lines on structure axes, they imply a trend that does not exist.
- Variances as pins (thin bars) in green and red; bridges as waterfalls
  (growth over time, calculation schemes, variance causes).
- Stacked columns or bars only when all values share a sign and the segments
  vary little; at most five segments. Put the series of interest on the axis.
- Lines only for many data points; more than three crossing lines become
  small multiples instead.
- Scatter and bubble charts for two value axes.
- Replace: pie and ring charts (bars or stacked columns instead; pies only on
  maps), gauges and speedometers (bars or columns), radar and funnel charts
  (bars; funnels mislead when area does not match value), spaghetti lines
  (small multiples), traffic lights except for genuine yes/no states.
- Prefer quantitative objects to conceptual graphics; no text slides and no
  bullet lists on projected slides, text belongs in the handout. A few
  conceptual graphics per hour at most.
- Add comparisons: scenarios (plan, previous year) wherever they exist, and
  the variances between them; a number alone says little.
- Explain causes: tree structures of calculated measures, clusters,
  correlations.

Table anatomy (EX 1.2): row headers left and wide; columns of one type share
one width independent of header length; numbers and their headers
right-aligned, text left-aligned; vertical lines very light or absent, white
gaps separate column groups; light horizontal rules between rows; totals in
bold or on light grey below their group (rows) or right of their group
(columns); "thereof" rows and columns in smaller type, not separated from
their parent; "percent of" rows and columns in smaller type; remainder rows
and columns for the long tail. Time periods, scenarios and variances go in
columns, not rows.

## 5. SIMPLIFY: avoid clutter

- No components without meaning: pictures, backgrounds, logos beyond the
  template minimum, animation other than "appear".
- No borders, shadows, pseudo-3D; no decorative colour; one plain typeface,
  bold and italic reserved for distinctions.
- Data labels replace value axes, tick marks and gridlines; gridlines only
  where reference points are missing (many series, small multiples).
- Right-align numbers to drop vertical lines in tables.
- No redundant words ("total", "sum", "chart", "development"), no repeated
  words across labels ("2017" twelve times); unit and period once, in the
  title.
- No labels on small values unless the message is about them; no numbers
  longer than three digits in charts and four in tables; label extremes, not
  every point.

## 6. CONDENSE: information density (reading-first material)

- Fonts, elements and objects as small as still legible; narrow margins;
  no empty space that carries no meaning.
- More data points and more dimensions reveal relationships a single number
  cannot; thirty-six monthly values read as fast as twelve.
- Combined charts: overlays (columns plus a line on the same category axis),
  multi-tier charts (values with their variances above), extended charts
  (context such as market or competitor beside the primary chart).
- Chart elements inside tables: bars, warning dots, sparklines.
- Small multiples: same type, same scale, side by side. Related charts on one
  page only when they belong together.
- Explanations embedded next to the element they explain, in written
  material.

For speaker-led decks apply this chapter only to backup slides and handouts;
the main deck keeps presentation density.

## 7. CHECK: visual integrity

- Value axes start at zero; no logarithmic axes in business charts; no
  broken or clipped bars; equal class widths in histograms.
- Areas and volumes represent values only when the area or volume is
  proportional; prefer lengths. No coloured map areas for non-area measures;
  columns or bars (or pies) placed on the map instead.
- Identical scale for identical units on one page; size charts to their data
  rather than distorting scales; scaling indicators (a line or bar marking the
  same numerical height in every chart) when scales must differ; outlier
  indicators for unimportant extremes instead of scaling everything to them;
  magnifying-glass insets for zoom.
- Show inflation and currency adjustments on long time series.

## 8. UNIFY: the notation

Apply the same notation across the whole deck and, ideally, across the
organisation.

**Terminology and formats.** One glossary of terms and abbreviations; one
format for numbers, units and dates (thousands separators, decimal places,
unit in the title not behind every number).

**Message and title positions.** Message in the same place on every page (top,
above or beside the title). Descriptive title in up to three lines: what
(measure, unit, scenarios), where (structure dimension), when (period). On a
slide: action title above, descriptive chart title on the chart.

**Scenarios.** Recognisable from the fill alone, without reading labels:

| Scenario | Abbreviation | Fill |
|---|---|---|
| actual (measured) | AC | solid dark |
| previous year or period, used as reference | PY | solid light grey |
| plan or budget (fictitious) | PL, BU | outlined, white inside |
| forecast (expected, partly measured) | FC | hatched, outlined |

Variance axes and reference triangles carry the fill of the reference
scenario. In stacked or multi-line charts the fill may move to the axis.

**Variances.** Absolute variance Δ = primary minus reference (ΔPL, ΔPY);
relative variance Δ% = absolute divided by reference. Positive variances green,
negative red, with explicit "+" and "−" signs; good and bad follow the measure
(a cost overrun is red even though the number is positive). Variances as pins,
in a tier above or beside the values.

**Time.** Left to right; earlier periods left. Flow measures (sales) as
periods, stock measures (headcount) as points in time. Category width can code
the period type (months narrower than years). Scenarios of different periods in
chronological order; scenarios of the same period in the order they were
created (plan, forecast, actual), kept constant throughout.

**Structure.** Top to bottom on a vertical axis; order by the analysis
(ranking, grouping), remainder element last after a wider gap.

**Measures.** Value versus volume, flow versus stock, basic versus calculated
distinguishable by element width or type; calculated ratios in smaller type or
as separate columns.

**Indicators.** Highlighting marks (arrows, circles, difference brackets) in
one consistent style; scaling lines or areas; outlier markers; comment
numbers linked to elements.

## 9. How to apply IBCS inside this skill

1. Stage 0: if the briefing contains scenario data (plan, actual, forecast,
   previous year), note that the deck uses IBCS notation and say so in the
   register ("Notation: IBCS").
2. Stage 2, slide bodies: time series horizontal, structures vertical;
   scenario fills as in the table above; variances as green/red pins with
   signs; descriptive chart title under the action title; unit and period in
   the title, not on every label; data labels instead of axes.
3. Tables per the anatomy in section 4; totals, "thereof" and "percent of"
   rows styled as described.
4. Reading-first decks and handouts: CONDENSE applies; embed explanations
   beside the element they explain.
5. Self-check: add to the visual check in `visual-design.md` section 12:
   axes at zero, same scales on one page, scenario fills correct and
   consistent, variance colours follow meaning, no pies, gauges, radar or
   traffic lights.

## 10. What IBCS does not cover

Storyline craft beyond SCQA, speaker notes, timing, Q&A, decision wording,
deck types and their mandatory elements, layout patterns for non-quantitative
slides. Those remain with the other references.

## Sources

- IBCS Standards, online text of version 1.1/1.2 (SAY, STRUCTURE, EXPRESS,
  SIMPLIFY, CONDENSE, CHECK, UNIFY), https://www.ibcs.com/standards/ , read
  October 2026. Creative Commons; rules paraphrased, figures not reproduced.
- IBCS Standards Version 2.0, aligned with ISO 24896, release note June 2026,
  https://www.ibcs.com/ibcs-version-2-0/ (restructuring into Notation and
  Composition; substance unchanged).
- Hichert, Faisst et al., *International Business Communication Standards*,
  IBCS Version 1.1, 2017 (book edition of the same text).
- IBCS working group paper on mandatory versus optional semantic rules (2018)
  and on more scenarios per scenario type (2019), ibcs.com downloads.
