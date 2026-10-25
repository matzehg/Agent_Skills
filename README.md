# Agent Skills

Portable skills in the open Agent Skills format: one folder per skill, each with
a `SKILL.md` (frontmatter plus instructions) and optional `references/`,
`assets/`, `scripts/` and `evals/`. The same folder runs in Claude.ai (upload as
zip under Customize > Skills), Claude for PowerPoint, Cowork and Claude Code.

## Skills

| Skill | Purpose | Status |
|---|---|---|
| `minto-deck` | Build and audit slide decks after the Pyramid Principle and consulting practice: two-stage workflow (ghost deck with register for approval, then deck with speaker notes, timing plan, Q&A, backup, handout) and an audit mode for existing decks | v0.5, in test |

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

- v0.5: quick checklist at the top of every reference; `references/stage-2-checklist.md` as the page ticked before delivery; worked examples (register and gap list, speaker-notes block, audit findings, management summary before/after, chart declutter before/after, IBCS chart before/after); `scripts/pptx-helpers.js` with example build and README for the sandbox rendering path; frontmatter metadata with version; description excludes transcription and summarising of existing talks; critic-subagent pattern for hosts with subagents.

- v0.4: `references/ibcs-notation.md` (IBCS rules and scenario notation, reconciled with the skill: density by mode, action title as message plus descriptive chart title); `references/reading-decks.md` (pre-reads and handouts after Slidedocs principles, conversion rules, audit checks); `references/sources.md` (every source with status and effect); decluttering sequence (Knaflic) and comparison tables (Few) in `visual-design.md`; audit checks G13, G14; deck types Leitungsvorlage and decision briefing (BLUF) as proposals; IBCS notation as default with opt-out and one-slide preview; multiple templates under `assets/templates/`, kept out of public repos.

- v0.3.1: glossary terms from v0.2 and v0.3; slide references by number plus title and regenerated after renumbering; handout evidence line defined; eval expectation includes register and gap list; validation step in this README.

- v0.3: `references/visual-design.md` (layout catalogue, grid, type, colour, Zelazny chart rules, executive summary formats, visual check); section lead slides; evidence check and gap list in the ghost deck; executive summary drafted first and finalised last; revision loop via PowerPoint comments; audit checks F7, F8, G11, G12.
- v0.2: register of named entities in the ghost deck and consistency pass; layout and geometry rules; list-style tables; colour discipline; selections name their universe; decision slide as proposal; options before detail; full-size slide inspection; audit checks B7, B8, E5, G7 to G10.
- v0.1: initial skill: two-stage workflow, Minto reference, consulting practices, speaker notes, timing plan, Q&A preparation, handout, audit checklist, glossary, one eval case.
