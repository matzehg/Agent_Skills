# Assets

Holds the approved reference deck and any user-supplied templates.

- `reference-deck/`: the first approved test run (ghost deck, deck, notes,
  timing plan, Q&A document, handout). Use it as a pattern for format and
  density only; never reuse its content.
- `templates/<name>/`: user-supplied `.potx` or `.pptx` templates, one folder
  per organisation or purpose, each with a `notes.md` naming its layouts,
  placeholders and colour roles. Apply the one the briefing names; several
  templates can coexist. Templates are proprietary: add
  `minto-deck/assets/templates/` to `.gitignore` in public repositories and
  keep the files local or in a private location.

Empty until the first test run is approved.
