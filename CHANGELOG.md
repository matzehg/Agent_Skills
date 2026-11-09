# Changelog

Detail tables per version, newest first. The one-line summaries live in README.md.
Changes below v0.6 are listed in README.md only.

# minto-deck v0.7.2 (2026-11-09)

Patch after the first end-to-end runs in Claude.ai: a Build run on the eval case
`decision-paper-ai-governance` (Stage 1 ghost deck, gate, Stage 2 to .pptx with
notes, timing plan and Q&A, 20 slides) and an Audit run on a real 21-slide expert
talk with a corporate font. Findings sorted as rule gaps (below) and deck fixes
(kept with the deck); fixes tested where code changed.

| # | Finding | Fix | Files |
|---|---|---|---|
| 1 | Placeholder convention inconsistent: SKILL.md, consulting-practices, glossary and memo-format said `[PLACEHOLDER: …]`, stage-2-checklist and all three scripts knew only `[PLATZHALTER: …]`; in an English deck placeholders counted as body words and `PH()` wrote German markers | One form per deck: `[PLACEHOLDER: …]` in English, `[PLATZHALTER: …]` in German decks; `createDeck({ lang })` drives `PH()`; the word counters in the helpers and in `deck-metrics.py` strip both forms | `SKILL.md`, `consulting-practices.md` §7, `memo-format.md`, `glossary.md`, `stage-2-checklist.md`, `scripts/pptx-helpers.js`, `scripts/deck-metrics.py` |
| 2 | Ghost-deck format numbered from the situation, the audit demanded the management summary "on slide 2"; with a title slide the two could not both hold | Title slide "T" in the format, outside the numbering; "first slide after the title" replaces "slide 2" throughout; SCQA variant Direct (answer, then situation and complication) is the default for decision papers and Leitungsvorlagen, Standard only when the audience needs the context first | `SKILL.md` Stage 1 and 2, `storyline-ghost-deck.md`, `minto-pyramid.md`, `consulting-practices.md` §6, `visual-design.md` §8, `audit-checklist.md` A1, A2, example, `glossary.md`, `memo-format.md` bridge, `timing-qa-handout.md` §5 |
| 3 | A 31-word governing thought passed the gate; the management-summary title allows about 20 words, so Stage 2 had to shorten an approved sentence | Length test in the Stage 1 checklist and the title rules: governing thought and every key-line claim fit a two-line title (about 20 words German, 16 English); longer thoughts get a short form for the title, the long form in the notes; `deck-metrics.py` flags titles over 20 words | `SKILL.md` Stage 1, `storyline-ghost-deck.md` checklist and title rules, `scripts/deck-metrics.py` |
| 4 | The 40-word speaker budget collided structurally with the management summary (key line verbatim) and the decision slide (decision, consequence, what is needed today); both sat at 77 to 80 words, at the blocker edge | Own budget of about 80 body words for both slides, excluded from the mean; `deck-metrics.py` takes them from `--special` or detects them by title (Management Summary, Executive Summary, Beschlussvorschlag, Proposed decision) or by an `ask-box` object | `exhibits.md` §6, `audit-checklist.md` H1 and severity, `stage-2-checklist.md`, `scripts/deck-metrics.py` |
| 5 | Scorecard axes contradicted each other: `exhibits.md` 3.11 said items as rows, `visual-design.md` §2 said criteria as rows | One convention: criteria as rows, options as columns, the recommended option highlighted as a column (matches `ltable` `hl`); flip only above four options | `exhibits.md` §3.11 |
| 6 | Rendering paths 1 and 2 collapse in claude.ai: the host's PowerPoint capability is itself pptxgenjs | One sentence in Rendering: helpers carry the layout rules, the pptx skill carries theme writer, validation and render check | `SKILL.md` Rendering |
| 7 | Audit had no rule for fonts missing in the render environment; overflow in the preview read as findings | Missing fonts suspend overflow and wrapping findings and go under "Not checked" with the font name and the advice to check in PowerPoint | `SKILL.md` Audit step 1, `audit-checklist.md` report format |
| 8 | Mixed German and English in titles had no check; G3 covered terminology only | G3: one language per deck in titles and labels, loanwords aside | `audit-checklist.md` G3 |
| 9 | Expert talk demanded "one concrete example per section" but not what concrete means; "what the audience can do" was satisfied by two aphorisms | A named case, project, date or number counts, a generic illustration does not; audience actions as actions | `audit-checklist.md` §1 |
| 10 | `chevrons()` placed text at a fixed 0.55 in inset; the notch of a pptxgenjs chevron is h/2, so from 1.1 in height the first letters disappeared | Text starts at h/2 + 0.1 and may run into the solid right point; test checks the inset on a 1.4 in chevron; rendered and inspected | `scripts/pptx-helpers.js`, `scripts/test-helpers.js` |
| 11 | `ltable()` let placeholders wrap inside the word in narrow columns, silently | `longestWordWidth()` (0.45 em plus margins, placeholder as one unit) reports a `narrow-column` warning per slide and column in `write().warnings`; calibrated on the rendered deck: fires for the broken columns, not for the fixed ones | `scripts/pptx-helpers.js`, `scripts/test-helpers.js`, `scripts/README.md` |
| 12 | Marks (● ◐ ○ ✓ ✗) and legend lines counted as words: the scorecard read 46 with 16 real words; counts in the helpers and in `deck-metrics.py` differed | A token is a word only with a letter or digit; shapes named label, key-box, tracker, source skipped; both counters agree | `scripts/pptx-helpers.js`, `scripts/deck-metrics.py` |
| 13 | `deck-metrics.py` classed a box-and-line hierarchy as "text" (text-bearing boxes counted as text boxes) and ignored pictures; exhibit ratio of the audited deck read 29 % | Shapes and connectors without text count as geometry, boxes by name (node, card, pill, box) count, pictures smaller than the slide count as exhibit; audited deck now 64 %, hierarchy slide "13 shapes" | `scripts/deck-metrics.py` |
| 14 | `card()` always drew bullets; numbered decision points needed "1." in the text, giving a bullet and a number | `bullets()` and `card()` take `numbered: true` (list numbering, never a literal number in the text) | `scripts/pptx-helpers.js`, `scripts/test-helpers.js` |
| 15 | Evals carried placeholder graders only and no results; the Audit mode had no regression case | Ten graders for `decision-paper-ai-governance` written from the run (ghost deck only, marks on every title, one approval question, title slide T, length test, process set, assumption marked, pptx with notes and mandatory elements, placeholders and metrics, timing and Q&A); new case `audit-expert-talk-outline`: synthetic German expert talk as a pasted outline with planted faults (agenda instead of thesis, label titles, 95 to 200 body words on speaker slides, unsourced number, repeated title, leftover divider notes, two durations, chart as background image, mixed languages, orphan slide), six graders | `evals/decision-paper-ai-governance/`, `evals/audit-expert-talk-outline/` |

Smoke test: 19 checks (was 14), passing with pptxgenjs 4.0.1. Regression caught
in the retest and fixed: the first chevron fix also narrowed the text box and
wrapped "Überwachung"; now only the left inset moves. Retest on the 20-slide
decision deck: validation passed, management summary and decision slide
detected as special, mean 34 body words (was 40), scorecard 31 (was 46).
Not retested: Memo mode, the evals themselves (no runner in claude.ai).

---

# minto-deck v0.7.1 (2026-11-09)

Stabilisation after an external review of v0.7 (commit 366fe0a). All findings
verified against the code and the files; fixes tested where code changed.

| # | Finding | Fix | Files |
|---|---|---|---|
| 1 | `wordsPerSlide` counted only text written through `txt()`: a 48-word `ltable()` reported 0 | Shared `countWords()` used by `txt()`, `ltable()` (every cell) and the handout key box; test asserts table words are counted | `scripts/pptx-helpers.js`, `scripts/test-helpers.js` |
| 2 | `deck-metrics.py`: text inside PowerPoint groups ignored; content slides guessed from a layout name ("Blank" excluded); HTML `<style>` counted as words | Groups walked recursively; `--skip` names non-content slides explicitly, default excludes only TITLE, SECTION, COVER layouts and cover/section/closing ids; `style`, `script`, `noscript` and comments stripped before counting | `scripts/deck-metrics.py` |
| 3 | `cycle()` with six nodes: shortening exceeded the chord, four of six arrows reversed and hidden | `cycleGeometry()` fits node size to the chord (nodes shrink), clamps shortening to 40 % per end, rejects fewer than three or more than six nodes; test checks direction and length for four and six nodes; six-node slide rendered and inspected | `scripts/pptx-helpers.js`, `scripts/test-helpers.js` |
| 4 | `bigStat()` still overlapped: 1.6 in cards by 0.15 in, and the 2.2 in example with a two-line label in the rendering | `bigStatLayout()` sizes the label box from the text (lines x font x 1.2), shrinks the label font once, and throws with the height needed when the card is too small; test covers the fitting 2.2 in case and the rejected 1.6 in case; rendered and inspected | `scripts/pptx-helpers.js`, `scripts/test-helpers.js` |
| 5 | "Both" had two workflows: new rule (reading deck first) versus Stage 2 step 7 (handout from the speaker deck) | Four cases: talk only; pre-read only; both from the start (reading deck first, speaker deck derived); handout for an existing speaker deck (extend per reading-decks 6) | `SKILL.md` Stage 2 step 7, `exhibits.md` §6 |
| 6 | New eval expected a three-row table; the old rule said two or three rows are never a table | Content criterion: a table when several attributes or clear mappings are compared, cards or list for single-attribute items; eval wording aligned | `consulting-practices.md` §16 and checklist, `visual-design.md` pointer, `stage-2-checklist.md`, `audit-checklist.md` G9, `evals/deck-speaker-density` |
| 7 | Short prose allowed two claims and no restated closing, but audit A5 and B1 demanded three to five claims and a verbatim restatement; the gate rule asked to announce the short-prose exception | A5 and B1 reworded; applicability table (deck, long memo, short prose) added to the audit checklist; gate exceptions: short prose is delivered without any announcement | `audit-checklist.md`, `SKILL.md` "The gate" |
| 8 | Text budgets read as hard gates; H1 a blocker in all cases | Budgets as guardrails: blocker only for a speaker-led deck over budget on average or any slide at twice the budget; under the lower bound in a reading deck is advisory | `exhibits.md` §6, `audit-checklist.md` H severity |
| 9 | Memo example turned a mention into evidence ("Als Beleg nennt er") | "Außerdem erwähnt er"; rule added that connectives (weil, deshalb, als Beleg, führt zu) need the source to carry the relation | `memo-format.md` §3 |

Smoke test: 14 checks, passing with pptxgenjs 4.0.1. Rendered and inspected:
the 2.2 in stat card with table beside it, and the six-node cycle.

---

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
