---
name: minto-deck
description: "Build, write and audit after Barbara Minto's Pyramid Principle and consulting practice: governing thought, SCQA opening, MECE key line, full-sentence claims. Build mode makes slide decks in two stages: ghost deck for approval, then deck with speaker notes, timing, Q&A, backup, handout. Memo mode writes answer-first prose: management summaries, briefing notes, event or meeting reports, the thesis of a day, after a short storyline gate. Audit mode reviews a deck or memo and reports weak claims, broken logic and missing elements, with rewrites. Use whenever the user asks for slides, a deck, presentation, pitch, talk, storyline, ghost deck, speaker notes, management summary, Kernbotschaft, These, Vermerk, Veranstaltungsbericht, an answer-first or Minto summary, or wants a deck or memo reviewed; also on Folien, Praesentation, Vortrag, Entscheidungsvorlage, Sprechzettel, Deck pruefen. Trigger even without the word Minto. Not for transcription, translation or plain recaps. German, English."
metadata:
  version: "0.7.2"
  updated: "2026-11-09"
  language: "en, de"
---

# Minto Deck

A deck or a memo is an argument the audience can follow from the headings
alone. This skill makes every deck and every memo answer-first, builds the
storyline first so the argument gets approved while changing it is cheap, and
reviews existing decks and memos against the same standard. The methodology
lives in `references/`, independent of any rendering tool, so the skill behaves
the same in Claude.ai, Cowork, Claude Code or any Agent-Skills-compatible host.

## Three modes

Choose the starting mode for the request and name it in the first line of the
reply; a combined request runs modes in sequence, each named when it starts.
The one exception is short prose (see "Short prose" under Memo mode), which
carries no mode label.

- **Build**: the user wants a new deck, a storyline, a ghost deck, speaker notes
  for a deck that does not exist yet, or a rework of material into slides.
- **Memo**: the user wants prose that argues answer-first: a management summary,
  a briefing note or Vermerk, an event or meeting report, the thesis of a day
  or a meeting, a decision memo, a status note, or a summary that should lead
  with the conclusion rather than retell the source. Output is text (chat, doc
  or file), never slides.
- **Audit**: the user has a deck or a memo (file, link, pasted outline, exported
  text) and wants it reviewed, checked, critiqued or scored. Do not change it in
  Audit mode unless the user asks for a rewrite; then report first, rewrite second.

A request like "fix my deck" is Audit followed by Build Stage 1 on the corrected
storyline. Say so before starting. The gate between stages is defined once,
in "The gate" below; the references point there. "Summarise these notes" with no further wish
is a plain summary and outside this skill; "summarise so the key message comes
first", "what is the thesis of the day", "write the management summary" is Memo
mode. When a memo and a deck are both wanted, run Memo first: the approved memo
storyline becomes the ghost deck's governing thought and key line (see "Bridge
to Build" under Memo mode).

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
   mandatory slides. Templates live in `assets/templates/`, one folder per
   template with the file and a short note on its layouts; pick the one the
   briefing names, or ask when several fit. Templates are the user's or their
   employer's property: keep them out of public repositories.
8. Notation: when the material contains actuals, plans, forecasts, previous
   periods or variances, the deck uses IBCS notation by default. Say so in the
   register and list "without IBCS notation" as an open point at the gate, so
   the user can decline.

### Stage 1: the ghost deck

Read `references/minto-pyramid.md` and `references/storyline-ghost-deck.md`
before building. The ghost deck is the complete argument with no slide bodies.

Build it in this order:

1. Write the governing thought: one sentence that answers the audience's
   question and that a reasonable person could disagree with, short enough
   for a two-line slide title (about 20 words in German, 16 in English);
   a longer thought gets a short form for the title and the long form in
   the notes.
2. Write the opening as SCQA. Keep only the situation and complication the
   audience does not already share. The title slide is "T" and not counted;
   the management summary is the first slide after the title. That makes
   the Direct variant (answer, then situation and complication) the default
   for decision papers and Leitungsvorlagen; Standard only when the audience
   needs the context before it can hear the answer.
3. Write the key line: the three to five claims that together prove the
   governing thought. Test them as a set: same kind of idea, no overlap, together
   sufficient, one logical order.
4. Expand each key-line claim into its supporting slides. Every slide title is a
   full sentence that states one claim. Group peers with parallel grammar.
   Give every title an evidence mark and a form mark (chart with its
   comparison type, table, concept visual with its type from
   `references/exhibits.md` section 3, or text with a reason): the form of
   the exhibit is decided at the gate, not while building, and "text" is
   reviewed like a claim. Declare the density mode (speaker-led or
   reading-first) and the text budget per slide from `exhibits.md` section 6
   in the header; "both" means the reading deck is built first and the
   speaker deck is derived from it.
5. Add the closing: governing thought restated, decision or next steps as a
   proposal the audience decides on, and the explicit ask if the deck type has
   one.
6. Build the register: every named entity (process, body, role, system,
   option, criterion) with the exact name that will appear on every slide, its
   category, definition and status (from briefing or hypothesis). Test each set
   for one category and one naming pattern. The register is the user's edit
   point for names, members and order; Stage 2 uses it as the only source.
7. Derive the timing skeleton from the duration and mark cut priorities.
   Section dividers only from roughly 20 slides; shorter decks use the tracker.
8. Run the read-through test: read the titles alone, top to bottom. If the
   argument has a gap, a repeat or a jump, fix the titles, not the bodies.

Output exactly the ghost-deck format in `references/storyline-ghost-deck.md`:
numbered titles grouped by section, register, timing skeleton, assumptions,
open points, and at most one alternative key line if the material supports a different
structure. Then stop and end the reply with the approval question, as "The
gate" below defines it. Do not produce slides, notes or files in the same
turn, even if the user asked for "the deck": the gate is the point of the
method, and a storyline change costs minutes now and hours later.

When the user edits titles, regenerate only the affected part of the storyline
and re-run the read-through test. Do not re-open approved sections.

Notation preview: if the user is unsure about IBCS notation, build one chart
slide in both variants before Stage 2 proper and let them choose. Two complete
decks in two notations only on explicit request.

### Stage 2: the full deck

Start only from an approved ghost deck. Read `references/stage-2-checklist.md`
first; it is the page that gets ticked before delivery. Then read `references/consulting-practices.md`,
`references/visual-design.md`, `references/exhibits.md`, `references/speaker-notes.md` and
`references/timing-qa-handout.md`. When the material contains actuals, plans,
forecasts, previous periods or variances, also read `references/ibcs-notation.md`.
For a reading-first deck or the handout step, read `references/reading-decks.md`.

Produce, in this order:

1. **Exhibits first.** For every slide with a chart, table or concept form
   mark, write the five-line exhibit brief (`exhibits.md` section 2) and build
   the exhibit, in key-line order, before any text slide: the subject of the
   title is the highlighted element, order and reading direction follow
   `exhibits.md` section 4, register names and colours inside the exhibit,
   cleaning sequence and the cover and headline tests from section 5. Native
   shapes, never raster images. Then the text slides, within the text budget
   of the declared density mode (section 6): in a speaker-led deck the detail
   goes to the notes, not onto the slide. Every external claim gets a source
   line; every number gets unit, period and denominator. In a decision paper,
   show the options before the detail of the recommended one, and signpost
   them as options in the title. Every entity comes from the register, in the
   register's name and order.
2. **Management summary** on the first slide after the title: draft from the ghost deck (governing
   thought, key line, ask); the final version is written in step 8, after all
   other slides exist and the numbers are known. Format by density mode per
   `visual-design.md` section 8.
3. **Speaker notes** for every slide in the notes pane, structured as in
   `speaker-notes.md`: key point, opening line, talk track, evidence to point at,
   transition, time budget. Prompts, not a script.
4. **Timing plan** as a separate table: slide, minutes, cumulative, cut priority.
5. **Q&A preparation** as a separate document: the questions the audience will
   ask, grouped by what they attack, each with a short answer and a pointer to the
   slide or backup that carries the evidence.
6. **Backup slides** for the evidence that answers anticipated questions but
   does not carry the main argument. Reference them from the Q&A document.
7. **Second density, by order.** Four cases, decided in Stage 0: talk only,
   build the speaker deck; pre-read only, build the reading deck; both from
   the start, build the reading deck first and derive the speaker deck by
   cutting each slide to its exhibit and labels (`exhibits.md` section 6);
   a handout for a speaker deck that already exists, extend that deck to
   reading-first density per `reading-decks.md` section 6. Storyline,
   register and exhibits are shared; only the text layer differs.
8. **Management summary, final.** Rewrite the management summary against the finished slides:
   every bold line is a claim a slide proves, every number matches its slide.
9. **Consistency pass.** Dump the deck text and check every set from the
   register: same members, same names, same order on every slide where it
   appears; a member that appears or disappears has a stated reason on the
   slide or in the notes. Check that subsets name their universe and
   criterion. Check the evidence column of the ghost deck: every title marked
   "missing" is now a placeholder on the slide and in the delivery note.
10. **Self-check** against `references/audit-checklist.md` before delivery,
    including group H (exhibits and text budget) and the visual check in
    `visual-design.md` section 12. Where the host does not allow rendering
    the slides from the build environment (the Slides artifact type), run
    the text-dump check and an element count instead and say so in the
    delivery note, naming the densest slides. Fix blockers; list warnings in
    the delivery note.

### Rendering

The methodology is tool-independent; the file is produced by whatever the host
offers, in this order of preference:

1. The host's native PowerPoint capability (Anthropic's `pptx` skill, a
   PowerPoint connector, or an equivalent slides tool), because it keeps text,
   tables and charts editable and puts notes in the notes pane.
2. `pptxgenjs` with `scripts/pptx-helpers.js` in a sandbox when no such
   capability exists; the helpers encode zones, grid, type scale, list-style
   tables, cards, chevrons and the notes pane, so a build file holds only the
   deck's content (see `scripts/README.md` and `scripts/example-build.js`).
3. A Markdown outline with notes when no file can be produced at all; say so.

Where the host's PowerPoint capability is itself `pptxgenjs` (claude.ai with
Anthropic's `pptx` skill), paths 1 and 2 are one path: the helpers carry the
layout rules, the `pptx` skill carries theme writer, validation and the
render check.

Deliver an editable `.pptx`. Keynote and Google Slides import it; do not produce
a Keynote-native file. Keep charts native. Put speaker notes in the notes pane,
never in a text box on the slide. Apply the user's template when they supplied
one; otherwise stay neutral and say so. Before delivery, dump the deck text and
check titles, order, notes presence and leftover placeholders. Then render every
slide at full size and look at each one: overlaps, floating connectors, boxes
narrower than what points to them, wrapped key-value lines, pooled whitespace,
spreadsheet-style tables. Thumbnails do not show these.

## Memo mode

Read `references/memo-format.md` and `references/minto-pyramid.md` before
starting. A memo applies the same pyramid as a deck, flattened into prose: the
governing thought leads, the section headings are the key-line claims, every
paragraph proves its heading. Two stages, one light gate; what goes into the
key line is decided by relevance to the reader's question and the quality of
the evidence, not by how many sources repeat a point (memo-format.md section 4).

### Stages in brief

Details for all three stages are in `memo-format.md` section 0; this is the
short form.

- **Stage 0, briefing.** Audience and their question; memo type (section 1 of
  `memo-format.md`); governing thought from the user or derived and labelled
  as such; length budget and destination; material, sources and the
  attribution setting ("none" only with an explicit agreement such as the
  Chatham House Rule); whether a deck follows. Ask only for what would change
  the storyline, at most three questions.
- **Stage 1, storyline.** The format in `memo-format.md` section 2: governing
  thought; SCQA with question and answer; key line of two to five claims
  (three to five the norm), by theme, never in source order, each with an
  evidence mark; order and criterion; dissent and where it is argued;
  implications where the type has them; register with a Sets line;
  assumptions and open points. Read-through on the key line. One approval
  question, then stop, as "The gate" defines it.
- **Stage 2, the memo.** Lead with the governing thought; one section per
  claim with the claim as heading (up to roughly 20 words, otherwise a short
  form with the full claim as first sentence); claim-first paragraphs of at
  most three sentences, lists for three or more parallel items; implications
  where the type calls for them; closing with the governing thought
  restated and the ask; evidence with unit, period, source and the attribution
  settled in Stage 0; placeholders marked; annex for source material;
  consistency pass against the register; self-check against the quick
  checklist in `memo-format.md` and checks A to D of `audit-checklist.md`.
  No framework labels in the text. Over budget: narrow claims and evidence
  together; conditions, counter-positions and attributions survive every cut.

### Short prose

For a text of roughly 300 words or less (a thesis of a day, a short summary,
a paragraph for an email), run the Stage 0 and Stage 1 checks internally and
deliver the finished text directly, in the format the user asked for. No mode
label, no separate storyline, no headings, no repeated conclusion, unless the
user asked for them or the format needs them. The text still leads with the
governing thought and still keeps attribution, uncertainty and dissent. If
the user later wants changes, treat the delivered text as the storyline.

### Rendering

A short memo goes in the chat reply. Anything the user will share or keep goes
in a doc or Markdown file; a Word file only on request. The structure is
independent of the host.

### Bridge to Build

An approved memo storyline is a ghost deck in waiting. Governing thought and
key line carry over verbatim; memo sections become deck sections; each
paragraph claim becomes a candidate slide title; the memo's register is the
deck's register. Start Build Stage 1 from the memo, add the evidence marks and
the timing skeleton, and gate again only on what changed. In the other
direction, the management summary and the handout of a finished deck are memos
and follow this mode's writing rules.

## The gate

One definition for Build and Memo; `storyline-ghost-deck.md` and
`memo-format.md` point here.

- Default: Stage 1 ends with exactly one question, whether the storyline (and
  the register) is approved as is or which lines to change, and the reply
  stops there. Stage 2 never starts in the same turn.
- Approval with changes: a reply that names changes and says to continue
  ("change claim 2 to …, then go on", "approved except the title of slide 7")
  is an approval. Apply the changes, show the changed lines in one block, and
  continue into Stage 2 in the same turn, without a second question. A reply
  with changes and no instruction to continue gets the changed lines and the
  question again.
- Carry-over: an approved memo storyline carries into the ghost deck and an
  approved ghost deck into a handout; the gate opens again only for what
  changed in the carry-over.
- Exceptions: the user explicitly asked for a one-shot run (say in the reply
  that the gate is skipped at their request); a revision that does not touch
  the key line (deck fixes, wording, layout; say so briefly). Short prose
  under roughly 300 words has no gate and no storyline, and the reply does
  not announce that either: the text is the whole reply (see Memo mode).
- A revision that changes the key line re-opens the gate.

## Hosts with subagents

Where the host offers subagents (Cowork, Claude Code), run the Stage 2
self-check as a separate critic agent: it receives the rendered slide images,
the text dump, the register and `references/audit-checklist.md`, and returns
findings by severity without changing anything. The builder fixes blockers and
rebuilds; one round, then delivery with the remaining warnings in the note.
Without subagents the builder runs the same check itself.

## Revision loop

Feedback on a delivered deck comes in three ways; handle each the same way.

- **Comments in the file.** The user comments in PowerPoint (or another tool
  that writes comments into the .pptx) and uploads the file. Extract the
  comments per slide (`ppt/comments/*.xml` or the host's reading tool) and
  quote each before answering it.
- **Annotated PDF.** Extract the annotations per page.
- **List in the chat.** Slide numbers as printed on the slides.

Sort every item into two classes before changing anything: a deck fix (wrong
on this deck only) or a rule gap (the skill would make the same mistake again).
Deck fixes go into the deck. Rule gaps are reported to the user as proposed
skill changes, in a list separate from the deck changes; they are written into
`SKILL.md`, a reference or the glossary only in a skill-maintenance task the
user has asked for, never as a side effect of a deck revision. A project's
own names and terms live in that project's register, not in the glossary.
Report the sorting to the user, apply title changes through the ghost deck and
the register, and rebuild from the approved storyline. A revision that changes
the key line re-opens the gate.

## Audit mode

Read `references/audit-checklist.md` and `references/minto-pyramid.md`.

1. Extract the deck: titles, bodies, notes, slide count, sources. For a `.pptx`
   use the host's reading tool or `markitdown`; for a PDF extract text; for a
   pasted outline work with what is there and say what could not be checked
   (visual layout, notes, charts). When the deck uses a font the render
   environment does not have, overflow and wrapping in the preview are not
   findings: list them under "Not checked" with the font name and the
   advice to check in PowerPoint. For a memo extract lead, headings, first
   sentences of paragraphs, closing and sources.
2. Identify or ask for the deck type, audience, setting and density mode.
   The completeness check needs a target, and the text budget (group H) needs
   the mode. For a memo, the type comes from the table in `memo-format.md`
   section 1; checks on timing, notes, visuals and exhibits do not apply and
   the report says so.
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
  `[PLACEHOLDER: what is needed]` in an English deck and `[PLATZHALTER: was
  fehlt]` in a German deck, one form per deck, and list them in the delivery
  note. The scripts recognise both forms.
- Write topic titles ("Market overview", "Risks") or filler hedges ("Results
  may indicate various effects"). A title states the strongest claim the
  evidence supports, and keeps the uncertainty, attribution, condition or
  scope that accuracy requires: "Pilot data from six volunteers point to
  shorter search times" is a precise claim, "The assistant cuts search time"
  overclaims it. Calibration is not hedging.
- Mix logical orders inside a peer set, or mix speaker-led and reading-first
  density inside one deck.
- Skip the Stage 1 gate silently, in Build or in Memo mode.
- Fill a speaker-led slide with reading-deck text, or ship one deck for
  "both". Density is declared once, text budgets per mode are in
  `exhibits.md` section 6, and "both" is two decks from one storyline.
- Draw to decorate. An exhibit proves a relation the title claims; an icon,
  arrow or diagram that illustrates a word is removed.
- Retell a source in its own order. A Memo-mode summary reorders the material
  under the answer; a chronological recap, a transcript or a translation is not
  this skill's job.
- Write speaker notes as a verbatim script, or put notes on the slide.
- Output framework labels (SCQA, key line, MECE) inside the deck. They belong
  in the ghost-deck commentary and the notes, not on slides.

## References

Read the file when its stage starts; do not load all of them up front.

| File | Read when |
|---|---|
| `references/stage-2-checklist.md` | Stage 2 start and before delivery: the compact list that gets ticked |
| `references/minto-pyramid.md` | Stage 1, and every Audit |
| `references/storyline-ghost-deck.md` | Stage 1: process, output format, timing skeleton, gate |
| `references/memo-format.md` | Memo mode, all stages (section 0 holds the stage details), and Audit of a memo: memo types and mandatory elements, storyline format, writing rules, length budgets, deriving a thesis from source material, attribution |
| `references/exhibits.md` | Stage 1 form marks and Stage 2 exhibits: shape-to-form table, exhibit brief, catalogue of 17 concept visuals, alignment to the message, cleaning sequence, text budgets by density mode, host constraints |
| `references/consulting-practices.md` | Stage 2: slide anatomy, action titles, density, tables, backup, decision wording |
| `references/visual-design.md` | Stage 2: layout patterns, grid, type, colour, charts, decluttering, tables, executive summary format, visual check; Audit: form checks |
| `references/ibcs-notation.md` | Stage 2 and Audit, whenever numbers with scenarios or variances appear: IBCS rules and notation |
| `references/reading-decks.md` | Stage 2 handout step and any reading-first deck; Audit of pre-reads |
| `references/sources.md` | Maintenance: every source, its status and what it changed |
| `references/speaker-notes.md` | Stage 2, step 3 |
| `references/timing-qa-handout.md` | Stage 2, steps 4 to 7 |
| `references/audit-checklist.md` | Stage 2 self-check, and every Audit: deck types, checks, severity, report format |
| `references/glossary.md` | Any German deck |

Every reference opens with a quick checklist of its rules; the rest of the file
is detail to look up.

`assets/` holds the approved reference deck once one exists and user templates;
use them as patterns for format and density, never as a source of content.
`scripts/` holds the pptxgenjs helpers for the sandbox rendering path.
