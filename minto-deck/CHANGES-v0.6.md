# minto-deck v0.6 (2026-11-05)

Memo mode added: the pyramid applied to prose (management summaries, Vermerke,
event and meeting reports, thesis of a day, decision memos, status notes), with
a light storyline gate and a bridge into Build mode.

## Changed files

| File | Change |
|---|---|
| `SKILL.md` | description rewritten (997 characters, under 1,000): three modes, memo triggers in EN and DE, exclusion narrowed to transcription, translation and chronological recap; version 0.6; "Two modes" is now "Three modes" with the routing rule for summaries; new section "Memo mode" (Stage 0 briefing, Stage 1 storyline, Stage 2 memo, rendering, bridge to Build); Audit mode extended to memos; "What this skill does not do" gains the recap exclusion; references table gains `memo-format.md` |
| `references/memo-format.md` | new: quick checklist, memo types with mandatory elements and length, storyline output format, writing rules with before/after, deriving a thesis from source material, attribution settings, the gate, bridge table memo to deck, frequent failures |
| `references/glossary.md` | 13 new EN/DE pairs for memo terms |
| `references/sources.md` | Minto row extended: `memo-format.md` draws on the book's original subject, prose |
| `evals/memo-event-report/` | new eval case: event report from notes of four talks, mixed audience, attribution open, deck to follow |

## Unchanged

Build mode, Audit checks A to G, all other references, scripts, assets.

## To do after merging

- Upload v0.6 to Claude.ai under Customize > Skills (replaces v0.5).
- Run the new eval once the skill-creator eval runner is available (Claude Code or Cowork).
- Decide whether `audit-checklist.md` should carry a memo column of its own; for now Audit of a memo uses checks A to D plus the type table in `memo-format.md`.
