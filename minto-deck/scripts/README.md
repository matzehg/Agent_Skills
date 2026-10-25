# scripts/

Rendering helpers for the sandbox path (no native PowerPoint capability in
the host). When Anthropic's `pptx` skill or a PowerPoint connector is
available, prefer that; these helpers exist so that a pptxgenjs build does
not reinvent the layout rules on every run.

- `pptx-helpers.js`: `createDeck({ mode, title, author, theme })` returns an
  API with fixed zones and grid (`BODY_Y`, `BODY_H`, `cols(n)`), the type
  scale per density mode (`F`), masters for title, section and content
  slides, and primitives that encode the design rules: `content()` (title,
  tracker, source line, notes in the notes pane, key-point strip in handout
  mode), `ltable()` (list-style table: no vertical rules, header over a rule,
  one highlighted column), `card()`, `bigStat()`, `chevrons()`, `pill()`,
  `label()`, `MARK()` for ✓ ✗ ● marks, `PH()` for placeholders. `write(path)`
  writes the file, applies the theme and returns slide count and total
  minutes from the notes.
- `example-build.js`: three slides showing the pattern. Copy its structure
  into a per-deck build file; never reuse its content.

Build workflow: write `build.js` from the approved ghost deck and register,
run it twice (`speaker`, `handout`), validate with the pptx skill's
`validate.py` if present, convert to PDF, render every slide and look at it,
dump the text with `markitdown` and run the consistency pass. Deliver the
`.pptx` files; keep `build.js` with the deliverables so the user can rebuild.

The default theme is neutral (dark slate, petrol accent, brick signal). A
user template replaces it: pass `theme` colours that match the template, or,
better, build on the template file with the pptx skill's template workflow.
