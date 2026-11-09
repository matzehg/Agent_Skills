# Changelog

Detail tables per version, newest first. The one-line summaries live in README.md.
Changes below v0.6 are listed in README.md only.

# minto-deck v0.7 (2026-11-09)

Exhibits wave. Decks built with v0.6.x were text-heavy (the 05.11. event deck:
106 body words per content slide in a deck declared speaker-led, exhibit ratio
33 %). The cause was structural: the form of the exhibit was decided while
building, after the text existed, and no text budget existed for speaker-led
decks. v0.7 moves the form decision to the gate, adds the catalogue, the
alignment and cleaning rules, and text budgets by density mode, and makes the
numbers measurable. Catalogue checked against Zelazny (concept visuals) and
Duarte (slide:ology taxonomy, Diagrammer families) on the web, 2026-11-09.

| # | Change | Files |
|---|---|---|
| 1 | Text budgets by density mode: speaker-led up to about 40 body words per content slide, reading-first 75 to 250; "both" means reading deck first, speaker deck cut from it; never one deck for both | `exhibits.md` §6, `consulting-practices.md` §5, `SKILL.md` Stage 1, Stage 2, "does not do" |
| 2 | Form mark per ghost-deck title (chart with comparison type, table, concept with type, text with a reason) decided at the gate; density mode and text budget in the ghost-deck header | `storyline-ghost-deck.md` (format, process step 8, checklist), `SKILL.md` Stage 1 |
| 3 | New reference `references/exhibits.md`: shape-to-form table, when not to draw, exhibit ratio; the five-line exhibit brief; catalogue of 17 concept visuals in six families (process, structure, comparison, time, relation, plus variants) with "carries when", trap, reading direction, caps, text, rendering per path; alignment to the message (title subject = highlight, sort by message, fixed reading directions, two titles, scale honesty, direct labels, register inside exhibits, Gestalt); cleaning sequence for concept visuals, caps, squint test, cover and headline tests; host constraints; frequent failures | `references/exhibits.md` |
| 4 | Stage 2 builds exhibits first, in key-line order, then text within budget; self-check includes group H and the host constraint (text dump plus element count where rendering is not possible) | `SKILL.md` Stage 2, `stage-2-checklist.md` |
| 5 | Audit group H "Exhibits and text budget" (H1 to H9, severities); B3 gains the catch-all signal; words per content slide and exhibit ratio reported | `audit-checklist.md` |
| 6 | Catch-all buckets ("Sonstiges", "Weitere", "Other") as a peer only with a visible reason | `minto-pyramid.md` §8, `audit-checklist.md` B3, `exhibits.md` §8 |
| 7 | Renderer: `cycle()`, `continuum()`, `timeline()`, `matrix()`, `line()`; `write()` returns `wordsPerSlide`; smoke test extended (10 checks, passing with pptxgenjs 4.0.1; cycle and timeline rendered and inspected) | `scripts/pptx-helpers.js`, `scripts/test-helpers.js` |
| 8 | `scripts/deck-metrics.py`: body words per slide, exhibit kind, mean, exhibit ratio and over-budget slides for a `.pptx` (python-pptx) or a Slides-artifact `slides/` folder; text cards do not count as exhibits | `scripts/deck-metrics.py`, `scripts/README.md` |
| 9 | SKILL.md trimmed: Memo stage details moved to `memo-format.md` §0, short form stays in SKILL.md (413 lines, was 439 before the additions) | `SKILL.md`, `memo-format.md` |
| 10 | Sources: Zelazny *Say It With Presentations* and the concept-visual chapter, Duarte slide:ology ch. 3 and Diagrammer, Mayer *Multimedia Learning*, Tufte *Cognitive Style of PowerPoint*, Gestalt principles; two web checks listed | `sources.md` |
| 11 | Glossary: form mark, exhibit brief, concept visual, text budget, exhibit ratio, cover and headline test, squint test, reading direction, catch-all bucket, type names | `glossary.md` |
| 12 | Evals: decision-paper case expects form marks and density header; new case `deck-speaker-density` (one-shot speaker deck with cycle, contrast or continuum, timeline, table; budget kept; metrics in the delivery note) | `evals/` |

Not in this wave (agreed for later): template mode (reading a corporate master
for colours, fonts and layouts; reusing toolbox graphics) and a private
companion skill for corporate design.

---

# minto-deck v0.6.2 (2026-11-05)

Second wave of fixes, from an external review of v0.6.1 (evidence fidelity,
short prose, gate consistency, revision loop, attribution, renderer bugs,
evals). Decisions taken by the maintainer: the Build gate stays the default
(exceptions are now defined once); every title is a full sentence (noun-phrase
assertions dropped). The graphics and text-budget work is a separate wave (v0.7).

| # | Finding | Fix | Files |
|---|---|---|---|
| 1 | Hedge ban (SKILL, audit C4, ghost-deck title rules) contradicted D5 (facts, estimates, hypotheses apart) | Calibration rule: strongest claim the evidence supports, filler out, uncertainty, attribution, condition and scope kept; C4 reworded; worked example | `SKILL.md`, `storyline-ghost-deck.md`, `audit-checklist.md` |
| 2 | Teaching examples in memo-format.md added evidence not in the shown source and used an exclusion the material did not cover | Both examples rewritten as fictional with the full source shown; derived vs stated separated; exclusion rule added (step 8 of deriving a thesis) | `memo-format.md` §3, §4 |
| 3 | Single-source clusters sent to the annex; cut rule dropped conditions | Weigh, do not count (new step 3); single source may carry a claim; cuts narrow claim and evidence together; counter-positions, conditions, attributions survive every cut | `memo-format.md` §3, §4; `SKILL.md` Memo Stage 2 |
| 4a | Short prose carried mode label, storyline lines and headings | "Short prose" rule: under roughly 300 words checks run internally, finished text delivered in the requested format, no labels, storyline or headings unless asked; key line two to five, three to five the norm | `SKILL.md` Three modes, Memo mode; `memo-format.md` §1, §6 |
| 4b | Gate defined differently in SKILL.md and the references | One definition: `SKILL.md` "The gate" (default, approval with changes, carry-over, exceptions, re-opening); references point there | `SKILL.md`, `storyline-ghost-deck.md`, `memo-format.md` |
| 4c | "Change X and continue" triggered a new approval question | Approval-with-changes rule in "The gate" | `SKILL.md` |
| 5 | Revision loop wrote rule gaps straight into the skill; glossary grew with project terms | Rule gaps are proposed separately and persisted only in a skill-maintenance task; project terms live in the register | `SKILL.md` Revision loop; `glossary.md` |
| 6 | Closed meeting treated as a Chatham House trigger | "None" only with an explicit agreement; working version keeps traceability | `memo-format.md` §5; `SKILL.md` Memo Stage 0 |
| 7A | Theme writer loaded from a fixed Anthropic path, silent on failure; scheme colours mixed Office's palette into the deck | All colours from `T.colors` as hex; theme writer optional and reported via `write().themeApplied` | `scripts/pptx-helpers.js` |
| 7B | `chevrons()` dropped `sub` | Sub line rendered under the head | `scripts/pptx-helpers.js` |
| 7C | `sectionSlide()` missing from the timing log | `registerNotes()` shared by all slide types | `scripts/pptx-helpers.js` |
| 7D | Handout filter only on content slides; 9 and 10 pt in handouts | Filter in `registerNotes()`; tracker, source and slide number use `F.small` (11 pt in handout) | `scripts/pptx-helpers.js` |
| 7E | `bigStat()` label and sub overlapped at 2.2 in | Sub reserved first, label fills the rest | `scripts/pptx-helpers.js` |
| 7T | No regression test for the renderer | `scripts/test-helpers.js`: six checks, all passing with pptxgenjs 4.0.1 | `scripts/test-helpers.js`, `scripts/README.md` |
| 8 | Memo grader demanded identical headings (0.6.1 allows short forms); unsupported figure and user assumption unchecked | Graders updated; four new cases: audit-weak-pilot-data, memo-unsupported-number, memo-single-source-insight, memo-short-prose | `evals/` |
| M1 | "Exactly one mode" vs mode sequences | Starting mode plus sequence for combined requests | `SKILL.md` |
| M2 | Title grammar: full sentence vs noun-phrase assertions | Full sentences only | `storyline-ghost-deck.md` |
| M3 | Gate, short-prose and heading rules defined in several places | Gate and short prose now defined once in SKILL.md; the heading rule stays in memo-format.md §3 and SKILL.md Stage 2 points at it | `SKILL.md`, references |

---

# minto-deck v0.6.1 (2026-11-05)

Fixes from the first Memo-mode run (event report from six recorded talks).
All eight were found by applying v0.6 to a real case; none changes the method,
all change what the storyline shows at the gate or how Stage 2 writes.

| # | Gap in v0.6 | Fix | Files |
|---|---|---|---|
| 1 | Storyline opening showed only Situation and Complication; Question and Answer were implicit, so the gate could not check that the answer answers the question | Opening has all four lines; Answer = governing thought verbatim. Ghost-deck format gets a "Question the opening raises" line and names slide 3 as the Answer | `memo-format.md` §2, `SKILL.md` Memo Stage 1, `storyline-ghost-deck.md` |
| 2 | Memo register had no "Sets" line, so the plural-noun test was never run (an institute landed in a set of processes) | "Sets" line with one plural noun per set, members in fixed order, one category per set | `memo-format.md` §2, `SKILL.md` Memo Stage 1 |
| 3 | Event report requires "what it means for the reader", but the storyline had no slot for it | "Implications for the reader" line in the storyline; writing rule in §3; bridge row to the deck | `memo-format.md` §2, §3, §7; `SKILL.md` Stage 1 and 2 |
| 4 | Key-line claims carried no evidence mark; the bridge into the ghost deck needs it | `[evidence: available / missing / placeholder; source]` per claim | `memo-format.md` §2, §7; `SKILL.md` Stage 1 |
| 5 | §4 says "argue dissent under the claim it concerns", but the storyline had no line to place it | "Dissent" line naming positions, sources and the claim | `memo-format.md` §2; `SKILL.md` Stage 1 and 2 |
| 6 | Stage 2 writing order went Lead, Sections, Closing; the implications section had no step | New step 3 "Implications" between Sections and Closing | `SKILL.md` Memo Stage 2 |
| 7 | No heading length rule; a 32-word claim became a 32-word heading | Headings up to roughly 20 words; longer claims get a short-form heading and the full claim as first sentence | `memo-format.md` §2, §3; `SKILL.md` Stage 2 |
| 8 | "At most three sentences per paragraph" collided with enumerated questions | Three or more parallel items or questions become a list under a one-sentence lead-in | `memo-format.md` §3; `SKILL.md` Stage 2 |

Also: three glossary pairs (implications, dissent, evidence mark); eval
`memo-event-report` expects the new storyline elements; quick checklist in
`memo-format.md` updated.

---

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
