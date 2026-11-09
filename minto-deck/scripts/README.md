# scripts/

Rendering helpers for the sandbox path (no native PowerPoint capability in
the host). When Anthropic's `pptx` skill or a PowerPoint connector is
available, prefer that; these helpers exist so that a pptxgenjs build does
not reinvent the layout rules on every run.

- `pptx-helpers.js`: `createDeck({ mode, lang, title, author, theme })` returns an
  API with fixed zones and grid (`BODY_Y`, `BODY_H`, `cols(n)`), the type
  scale per density mode (`F`), masters for title, section and content
  slides, and primitives that encode the design rules: `content()` (title,
  tracker, source line, notes in the notes pane, key-point strip in handout
  mode), `ltable()` (list-style table: no vertical rules, header over a rule,
  one highlighted column), `card()`, `bigStat()`, `chevrons()`, `pill()`,
  `label()`, `MARK()` for ✓ ✗ ● marks, `PH()` for placeholders in the deck
  language (`lang: "de"` writes `[PLATZHALTER: …]`, `"en"` writes
  `[PLACEHOLDER: …]`), `bullets()` and `card()` with `numbered: true` for
  ordered items (never a literal "1." in the text), and the
  concept visuals of `references/exhibits.md` section 3: `cycle()` (nodes on
  a circle, clockwise, arrows node to node), `continuum()` (two poles, markers
  at 0..1), `timeline()` (dated events left to right, not to scale),
  `matrix()` (2 x 2 with axis labels), plus `line()` for direction-safe
  straight lines. `cycle()` shrinks its nodes to the chord so six nodes fit;
  `bigStat()` sizes its label box from the text and throws when the card is
  too small rather than overlapping. Both expose their geometry
  (`cycleGeometry`, `bigStatLayout`) for tests. `write(path)` writes the file, applies the theme when the
  writer is present and returns slide count, total minutes from the notes,
  `themeApplied`, `wordsPerSlide` (body words per slide, for the text
  budget in `exhibits.md` section 6; marks and placeholders are not words) and
  `warnings` (so far `narrow-column`: a table column too narrow for its
  longest token, which would wrap inside the word; widen the column or
  shorten the cell). `chevrons()` starts its text behind the notch (h/2), so
  tall chevrons stay readable.
- `example-build.js`: three slides showing the pattern. Copy its structure
  into a per-deck build file; never reuse its content.
- `deck-metrics.py`: `python3 scripts/deck-metrics.py deck.pptx --mode speaker`
  or `… path/to/slides/ --mode reading` for a Slides-artifact folder. Reports
  body words per slide, exhibit kind, mean words over content slides, exhibit
  ratio and the slides over the mode's budget. `--skip` names non-content
  slides, `--special` the management summary and decision slide (own budget,
  out of the mean; detected by title when not given). Marks and placeholders
  are not counted; shapes and connectors without text, and pictures smaller
  than the slide, count toward the exhibit; titles over 20 words are flagged.
  Heuristics for the audit group H and the delivery note; needs python-pptx
  for `.pptx`.
- `test-helpers.js`: smoke test for the helpers (`node scripts/test-helpers.js`
  with pptxgenjs installed): 19 checks, among them chevron text behind the
  notch, numbered cards, the narrow-column warning, word counting without
  marks and `PH()` per language, including table words in
  `wordsPerSlide`, the `bigStatLayout()` text-height rule (a card too small for
  its label is rejected with the height it needs), and `cycleGeometry()` for
  four and six nodes (every arrow keeps its direction and a visible length). Checks that content passed in is rendered
  (chevron sub lines), that minutes add up over title, section and content
  slides, that the handout filter applies to every slide type, that no scheme
  colours and no font under 11 pt reach a handout, and that `bigStat()` boxes
  do not overlap. Run it after any change to `pptx-helpers.js`.

Colours: every element takes its colour from `T.colors` as a hex value. The
theme writer from Anthropic's pptx skill is optional and only makes the
palette show up in Office's colour menus; `write()` returns `themeApplied`.

Build workflow: write `build.js` from the approved ghost deck and register,
run it twice (`speaker`, `handout`), validate with the pptx skill's
`validate.py` if present, convert to PDF, render every slide and look at it,
dump the text with `markitdown` and run the consistency pass. Deliver the
`.pptx` files; keep `build.js` with the deliverables so the user can rebuild.

The default theme is neutral (dark slate, petrol accent, brick signal). A
user template replaces it: pass `theme` colours that match the template, or,
better, build on the template file with the pptx skill's template workflow.
