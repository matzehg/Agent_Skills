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
  `--forms <deck>.forms.json` compares the approved form mark per slide with
  what the file contains (gate T2, mismatch reported as BLOCKER) and the
  text-block check (gate T3) flags content slides whose free text covers more
  than 60 % of the body zone without an exhibit. Heuristics for the audit
  groups H and T and the delivery note; needs python-pptx for `.pptx`.
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

## Template path (v0.8)

- `template-probe.py`: `python3 scripts/template-probe.py template.pptx --json probe.json --md brief.md`
  inventories a corporate template (layouts with placeholders and chrome,
  theme palette and fonts, slide size), proposes the three layouts and the
  free body zone, drafts the colour roles. Output is the Stage 0 template
  brief (`template-mode.md` section 3); the user confirms it once.
- `pptx_template_helpers.py`: `TemplateDeck(template, probe=probe.json, mode, lang, layouts={...}, roles={...})`
  opens the template, drops its sample slides, and builds on its layouts with
  python-pptx: `title_slide()`, `section_slide()`, `content(tracker, title, source, notes, build, form=...)`.
  Body placeholders are deleted on every content slide, never filled (gate
  T1); the slide-number, footer and date placeholders are copied from the
  layout so the chrome renders; fonts are never set and come from the theme.
  Primitives mirror `pptx-helpers.js` with the same shape names: `box`,
  `txt`, `label`, `line` (arrow), `bullets`/`card` (`numbered=True`),
  `ltable` (list style, narrow-column warning), `chevrons` (text behind the
  notch), `cycle` (chord arrows cut at the node edge, short-arrow warning),
  `contrast`, `timeline`, `big_stat`, `cols`, `PH()`. `Z` is the body zone
  from the probe; the last 0.35 in carry source (left) and tracker (right).
  `write(path)` returns slides, minutes, words per slide, warnings and the
  forms sidecar path.
- `example-template-build.py`: seven slides on the synthetic template
  (management summary, contrast, cycle, flow with a gate bar, scorecard,
  numbered decision cards), each with its form mark.
- `make-synthetic-template.js`: regenerates `assets/synthetic-corp.pptx`
  (own palette and fonts, logo, footer, slide number, four layouts, one of
  them with two body placeholders on purpose). Needs pptxgenjs.
- `test_template_helpers.py`: 14 checks for the template path, including the
  negative case (a cycle built as text boxes fails T2 and T3).

Both helper paths write `<deck>.forms.json`, the approved form mark per
content slide, from `content(..., form=...)`; `deck-metrics.py --forms` reads
it (gate T2) and reports text-block slides (gate T3).
