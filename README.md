# Agent Skills

Portable skills in the open Agent Skills format: one folder per skill, each with
a `SKILL.md` (frontmatter plus instructions) and optional `references/`,
`assets/`, `scripts/` and `evals/`. The same folder runs in Claude.ai (upload as
zip under Customize > Skills), Claude for PowerPoint, Cowork and Claude Code.

## Skills

| Skill | Purpose | Status |
|---|---|---|
| `minto-deck` | Build and audit slide decks after the Pyramid Principle and consulting practice: two-stage workflow (ghost deck with register for approval, then deck with speaker notes, timing plan, Q&A, backup, handout) and an audit mode for existing decks | v0.3, in test |

## Layout of a skill

```
<skill>/
  SKILL.md            what the skill does, when it triggers, the workflow
  references/         methodology, one file per source or topic; loaded on demand
  assets/             templates and the approved reference example
  evals/              test cases: prompt, expected outcome, graders
```

## Working on a skill

1. Change files in the skill folder; keep `SKILL.md` short and move detail to
   `references/`.
2. Run the eval prompt in `evals/` against the changed skill and compare with
   `expected_outcome`.
3. Bump the version note in this table and commit.
4. Re-zip the skill folder and re-upload in Claude.ai; other hosts read the
   folder directly.

## License

Apache 2.0, see `LICENSE`.

## Changelog

- v0.3: `references/visual-design.md` (layout catalogue, grid, type, colour, Zelazny chart rules, executive summary formats, visual check); section lead slides; evidence check and gap list in the ghost deck; executive summary drafted first and finalised last; revision loop via PowerPoint comments; audit checks F7, F8, G11, G12.
- v0.2: register of named entities in the ghost deck and consistency pass; layout and geometry rules; list-style tables; colour discipline; selections name their universe; decision slide as proposal; options before detail; full-size slide inspection; audit checks B7, B8, E5, G7 to G10.
- v0.1: initial skill: two-stage workflow, Minto reference, consulting practices, speaker notes, timing plan, Q&A preparation, handout, audit checklist, glossary, one eval case.
