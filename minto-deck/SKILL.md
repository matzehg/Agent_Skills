---
name: minto-deck
description: Build and audit presentation decks that follow Barbara Minto's Pyramid Principle and strategy-consulting practice (governing thought, SCQA opening, MECE key line, one message per slide, full-sentence action titles) in a two-stage workflow. Stage 1 delivers a ghost deck (the storyline as a numbered list of action titles plus a timing skeleton) and stops for approval; Stage 2 builds the full deck with speaker notes in the notes pane, a timing plan, Q&A preparation, backup slides, a management summary and a handout variant. Audit mode reviews an existing deck against the same rules and reports missing elements, weak titles and broken logic with concrete rewrites. Use this skill whenever the user asks for slides, a deck, a presentation, a pitch, a talk, a storyline, a ghost deck, speaker notes, or wants an existing deck reviewed, critiqued, checked, made "Minto-conform" or "consulting-grade". Also trigger on the German words Folien, Präsentation, Vortrag, Entscheidungsvorlage, Sprechzettel, Storyline, Deck prüfen, Deck gegenprüfen. Trigger even when the user does not mention Minto. Works in German and English.
---

# Minto Deck

A deck is an argument the audience can follow from the titles alone. This skill
makes every deck answer-first, builds it in two stages so the argument gets
approved before any slide is produced, and reviews existing decks against the
same standard. The methodology lives in `references/`, independent of any
rendering tool, so the skill behaves the same in Claude.ai, Cowork, Claude Code
or any Agent-Skills-compatible host.

## Two modes

Choose exactly one mode per request and name it in the first line of the reply.

- **Build**: the user wants a new deck, a storyline, a ghost deck, speaker notes
  for a deck that does not exist yet, or a rework of material into slides.
- **Audit**: the user has a deck (file, link, pasted outline, exported text) and
  wants it reviewed, checked, critiqued or scored. Do not change the deck in
  Audit mode unless the user asks for a rewrite; then report first, rewrite second.

A request like "fix my deck" is Audit followed by Build Stage 1 on the corrected
storyline. Say so before starting.

## Language

Reply, titles, notes and all artefacts in the language of the briefing. If the
briefing is mixed, ask once. Keep methodology terms in English with the German
gloss on first use when the deck is German, for example "Governing Thought
(Kernbotschaft)". `references/glossary.md` holds the fixed pairs; use them so
that decks stay consistent across projects.

## Build mode

### Stage 0: the briefing contract

Before writing a single title, establish the items below. Take them from the
request, attached material and conversation history first. Ask only for an item
that is missing and would change the storyline; otherwise state the assumption
in the Stage 1 output and carry on. Do not ask more than three questions at once.

1. Audience and their question: who sits in the room and what must they
   understand, decide or do when the deck ends.
2. Purpose and deck type: decision paper, status report, proposal or pitch,
   expert talk, reading deck. `references/audit-checklist.md` lists the mandatory
   elements per type; the type decides what Stage 2 has to contain.
3. Governing thought the user already has, if any. If the user has none, derive
   one from the material and label it as derived.
4. Setting: presented live or read without a presenter. This fixes the density
   mode (speaker-led or reading-first) and whether a handout variant is needed.
5. Duration, including discussion time, and the slide budget that follows.
6. Material and sources: what evidence exists, what is missing, what may not be
   invented. Numbers, quotes and examples come from the user's material or are
   clearly marked as placeholders.
7. Constraints: template, corporate design, confidentiality, slide limits,
   mandatory slides.

### Stage 1: the ghost deck

Read `references/minto-pyramid.md` and `references/storyline-ghost-deck.md`
before building. The ghost deck is the complete argument with no slide bodies.

Build it in this order:

1. Write the governing thought: one sentence that answers the audience's
   question and that a reasonable person could disagree with.
2. Write the opening as SCQA. Keep only the situation and complication the
   audience does not already share. Decide where the governing thought appears
   (slide 2 as management summary is the default).
3. Write the key line: the three to five claims that together prove the
   governing thought. Test them as a set: same kind of idea, no overlap, together
   sufficient, one logical order.
4. Expand each key-line claim into its supporting slides. Every slide title is a
   full sentence that states one claim. Group peers with parallel grammar.
5. Add the closing: governing thought restated, decision or next steps, and the
   explicit ask if the deck type has one.
6. Derive the timing skeleton from the duration and mark cut priorities.
7. Run the read-through test: read the titles alone, top to bottom. If the
   argument has a gap, a repeat or a jump, fix the titles, not the bodies.

Output exactly the ghost-deck format in `references/storyline-ghost-deck.md`:
numbered titles grouped by section, timing skeleton, assumptions, open points,
and at most one alternative key line if the material supports a different
structure. Then stop. End the reply with the approval question. Do not produce
slides, notes or files in the same turn, even if the user asked for "the deck":
the gate is the point of the method, and a storyline change costs minutes now and
hours later. If the user explicitly asked for a one-shot run, say that the gate
is being skipped at their request and continue.

When the user edits titles, regenerate only the affected part of the storyline
and re-run the read-through test. Do not re-open approved sections.

### Stage 2: the full deck

Start only from an approved ghost deck. Read `references/consulting-practices.md`,
`references/speaker-notes.md` and `references/timing-qa-handout.md`.

Produce, in this order:

1. **Slide bodies.** One message per slide; the body proves the title. Choose the
   evidence form (chart, table, diagram, text) by the comparison the message
   makes, per the chart rules in `consulting-practices.md`. Every external
   claim gets a source line; every number gets unit, period and denominator.
   Density follows the mode fixed in Stage 0.
2. **Management summary** on slide 2: governing thought, key line, ask. One slide.
3. **Speaker notes** for every slide in the notes pane, structured as in
   `speaker-notes.md`: key point, opening line, talk track, evidence to point at,
   transition, time budget. Prompts, not a script.
4. **Timing plan** as a separate table: slide, minutes, cumulative, cut priority.
5. **Q&A preparation** as a separate document: the questions the audience will
   ask, grouped by what they attack, each with a short answer and a pointer to the
   slide or backup that carries the evidence.
6. **Backup slides** for the evidence that answers anticipated questions but
   does not carry the main argument. Reference them from the Q&A document.
7. **Handout variant** when the deck will also be read without the presenter:
   same storyline, reading-first density, sources on the slide, no delivery cues.
8. **Self-check** against `references/audit-checklist.md` before delivery. Fix
   blockers; list warnings in the delivery note.

### Rendering

The methodology is tool-independent; the file is produced by whatever the host
offers, in this order of preference:

1. The host's native PowerPoint capability (Anthropic's `pptx` skill, a
   PowerPoint connector, or an equivalent slides tool), because it keeps text,
   tables and charts editable and puts notes in the notes pane.
2. `python-pptx` or `pptxgenjs` in a sandbox when no such capability exists.
3. A Markdown outline with notes when no file can be produced at all; say so.

Deliver an editable `.pptx`. Keynote and Google Slides import it; do not produce
a Keynote-native file. Keep charts native. Put speaker notes in the notes pane,
never in a text box on the slide. Apply the user's template when they supplied
one; otherwise stay neutral and say so. Before delivery, dump the deck text and
check titles, order, notes presence and leftover placeholders.

## Audit mode

Read `references/audit-checklist.md` and `references/minto-pyramid.md`.

1. Extract the deck: titles, bodies, notes, slide count, sources. For a `.pptx`
   use the host's reading tool or `markitdown`; for a PDF extract text; for a
   pasted outline work with what is there and say what could not be checked
   (visual layout, notes, charts).
2. Identify or ask for the deck type, audience and setting. The completeness
   check needs a target.
3. Run the checks in the order of the checklist: governing thought, key line,
   titles, read-through, slide-level logic, completeness per deck type,
   didactics (notes, transitions, timing, Q&A), form.
4. Report in the checklist's report format: verdict in one sentence, the title
   read-through with each title flagged, findings by severity (blocker, warning,
   advisory) with slide numbers and a concrete rewrite for every title finding,
   missing elements for the deck type, and the three changes with the largest
   effect.
5. Quote the user's titles verbatim when flagging them; propose the rewritten
   title next to each. Do not rewrite the whole deck unless asked.

## What this skill does not do

- Invent numbers, quotes, company examples or sources. Mark placeholders as
  `[PLACEHOLDER: what is needed]` and list them in the delivery note.
- Write topic titles ("Market overview", "Risks") or hedged titles ("Results
  may indicate…"). A title states a claim.
- Mix logical orders inside a peer set, or mix speaker-led and reading-first
  density inside one deck.
- Skip the Stage 1 gate silently.
- Write speaker notes as a verbatim script, or put notes on the slide.
- Output framework labels (SCQA, key line, MECE) inside the deck. They belong
  in the ghost-deck commentary and the notes, not on slides.

## References

Read the file when its stage starts; do not load all of them up front.

| File | Read when |
|---|---|
| `references/minto-pyramid.md` | Stage 1, and every Audit |
| `references/storyline-ghost-deck.md` | Stage 1: process, output format, timing skeleton, gate |
| `references/consulting-practices.md` | Stage 2: slide anatomy, action titles, charts, density, backup |
| `references/speaker-notes.md` | Stage 2, step 3 |
| `references/timing-qa-handout.md` | Stage 2, steps 4 to 7 |
| `references/audit-checklist.md` | Stage 2 self-check, and every Audit: deck types, checks, severity, report format |
| `references/glossary.md` | Any German deck |

`assets/` holds the approved reference deck once one exists; use it as a pattern
for format and density, never as a source of content.
