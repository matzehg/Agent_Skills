# Agent Skills

Portable skills in the open Agent Skills format: one folder per skill, each with
a `SKILL.md` (frontmatter plus instructions) and optional `references/`,
`assets/`, `scripts/` and `evals/`. The same folder runs in Claude.ai (upload as
zip under Customize > Skills), Claude for PowerPoint, Cowork and Claude Code.

## Skills

| Skill | Purpose | Status |
|---|---|---|
| `minto-deck` | Build, write and audit after the Pyramid Principle and consulting practice: two-stage deck workflow (ghost deck with register for approval, then deck with speaker notes, timing plan, Q&A, backup, handout), a memo mode for answer-first prose (management summaries, Vermerke, event reports, thesis of a day) with a storyline gate, and an audit mode for existing decks and memos | v0.7.1, in test |

## Layout of a skill

```
<skill>/
  SKILL.md            what the skill does, when it triggers, the workflow
  references/         methodology, one file per source or topic; loaded on demand
  scripts/            rendering helpers for hosts without a native PowerPoint capability
  assets/             templates and the approved reference example
  evals/              test cases: prompt, expected outcome, graders
```

## Working on a skill

1. Change files in the skill folder; keep `SKILL.md` short and move detail to
   `references/`.
2. Run the eval prompt in `evals/` against the changed skill and compare with
   `expected_outcome`.
3. Validate before packaging: frontmatter must be valid YAML (quote the
   description, no unquoted `: ` inside it) and `description` at most 1024
   characters. The skill-creator's `quick_validate.py` checks both.
4. Bump the version note in this table, add a changelog line, commit.
5. Re-zip the skill folder and re-upload in Claude.ai; other hosts read the
   folder directly. Upload only the zip and the README, never single files
   into the repository root.

## License

Apache 2.0, see `LICENSE`.

## Changelog

- v0.7.1: stabilisation after the v0.7 review: word counts include tables, groups and the handout key box and exclude HTML styles; `--skip` for slide roles in deck-metrics.py; six-node cycle geometry fixed (nodes fit the chord); bigStat sizes its label from the text and rejects cards that are too small; four orders of work for talk, pre-read, both and late handout; table criterion by content, not row count; audit applicability table for deck, long memo and short prose, A5 and B1 aligned; text budgets as guardrails; memo example keeps mention and evidence apart.

- v0.7: exhibits wave. Form mark per title at the gate (chart, table, concept visual, text with a reason); text budgets by density mode (speaker-led about 40 body words, reading-first 75 to 250) and the rule that "both" is two decks from one storyline; new `references/exhibits.md` with a catalogue of 17 concept visuals, exhibit brief, alignment and cleaning rules, host constraints; Stage 2 builds exhibits first; audit group H with words per slide and exhibit ratio; catch-all rule; renderer gains cycle, continuum, timeline, matrix and `wordsPerSlide`; `scripts/deck-metrics.py`; Memo stage details moved into memo-format.md; new sources (Zelazny Presentations, Duarte Diagrammer, Mayer, Tufte PowerPoint); eval `deck-speaker-density`.

- v0.6.2: evidence fidelity (calibrated claims instead of a hedge ban, fictional worked examples with full sources, weigh-not-count rule for single sources, cuts keep conditions and dissent); short prose delivered directly; the gate defined once with approval-with-changes and carry-over; rule gaps proposed, persisted only in maintenance; Chatham House only by explicit agreement; renderer fixes (colours from T.colors, chevron sub lines, section timing, handout filter and 11 pt minimum, bigStat geometry) with a smoke test; graders aligned and four eval cases added; full-sentence titles only.

- v0.6.1: Memo-mode fixes from the first real run: SCQA opening with Question and Answer in memo and ghost-deck storylines; Sets line in the memo register; evidence marks per key-line claim; dissent and implications lines in the storyline; Implications step in Stage 2; heading length rule; list rule for enumerated items.

- v0.6: Memo mode (`references/memo-format.md`): memo types with mandatory elements, storyline gate, writing rules, deriving a thesis from source material, attribution settings, bridge from memo to ghost deck; audit mode extended to memos; description trimmed under 1,000 characters with memo triggers in EN and DE; glossary pairs for memo terms; eval case `memo-event-report`.

- v0.5: quick checklist at the top of every reference; `references/stage-2-checklist.md` as the page ticked before delivery; worked examples (register and gap list, speaker-notes block, audit findings, management summary before/after, chart declutter before/after, IBCS chart before/after); `scripts/pptx-helpers.js` with example build and README for the sandbox rendering path; frontmatter metadata with version; description excludes transcription and summarising of existing talks; critic-subagent pattern for hosts with subagents.

- v0.4: `references/ibcs-notation.md` (IBCS rules and scenario notation, reconciled with the skill: density by mode, action title as message plus descriptive chart title); `references/reading-decks.md` (pre-reads and handouts after Slidedocs principles, conversion rules, audit checks); `references/sources.md` (every source with status and effect); decluttering sequence (Knaflic) and comparison tables (Few) in `visual-design.md`; audit checks G13, G14; deck types Leitungsvorlage and decision briefing (BLUF) as proposals; IBCS notation as default with opt-out and one-slide preview; multiple templates under `assets/templates/`, kept out of public repos.

- v0.3.1: glossary terms from v0.2 and v0.3; slide references by number plus title and regenerated after renumbering; handout evidence line defined; eval expectation includes register and gap list; validation step in this README.

- v0.3: `references/visual-design.md` (layout catalogue, grid, type, colour, Zelazny chart rules, executive summary formats, visual check); section lead slides; evidence check and gap list in the ghost deck; executive summary drafted first and finalised last; revision loop via PowerPoint comments; audit checks F7, F8, G11, G12.
- v0.2: register of named entities in the ghost deck and consistency pass; layout and geometry rules; list-style tables; colour discipline; selections name their universe; decision slide as proposal; options before detail; full-size slide inspection; audit checks B7, B8, E5, G7 to G10.
- v0.1: initial skill: two-stage workflow, Minto reference, consulting practices, speaker notes, timing plan, Q&A preparation, handout, audit checklist, glossary, one eval case.
