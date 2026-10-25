# Stage 1: storyline and ghost deck

The ghost deck is the argument without the slides: every title written as a
full sentence, in final order, with sections, a timing skeleton and the
assumptions behind it. Its only purpose is to get the argument approved while
changing it is cheap.

## Process

1. **Restate the briefing** in four lines: audience and their question, deck
   type and setting, duration and slide budget, material available. Mark every
   assumption. The user corrects these before anything else.
2. **Governing thought.** One sentence, specific enough to disagree with,
   answering the audience's question, supported by the material. Weak:
   "AI governance matters for the agency." Strong: "The agency can meet the
   AI Act deadline with one governance board and three existing processes, at
   no additional headcount."
3. **Opening (SCQA).** Pick the variant from `minto-pyramid.md` section 2.
   Write the situation and complication as titles. Drop whatever the audience
   already knows.
4. **Key line.** Three to five claims that together prove the governing
   thought. Run the plural-noun test, the overlap test, the scope test and the
   order test before going further. Write the key line as full sentences; they
   become the section titles and the management-summary lines.
5. **Supporting slides.** Under each key-line claim, the slides that prove it.
   One claim per slide. Parallel grammar inside each set. Stop when the claim is
   proven; do not pad a section to match the others.
6. **Closing.** Restate the governing thought with the confidence the evidence
   earns. Add the decision slide or next steps when the deck type requires them.
   Word the decision as a proposal the audience decides on.
7. **Register.** List every named entity the titles use: processes, bodies,
   roles, systems, options, criteria. One line each: name as it will appear on
   every slide, category, definition or source, status (from briefing /
   hypothesis). Test each set with the plural-noun rule: all members of a set
   share one category and one naming pattern (three processes are named as
   processes, not two documents and a function). Mark what the user has to
   confirm. The register is what the user edits when a name, a member or an
   order is wrong; Stage 2 takes every entity from here and nowhere else.
8. **Evidence check and gap list.** For every title, note whether the evidence
   exists in the material, is missing, or will be a marked placeholder. A title
   without evidence is either an analysis task (listed in the gap list with
   what has to be found and from whom) or a weaker claim. Storyline and
   analysis iterate: the gap list is what goes back to the analysis.
9. **Timing skeleton.** See below.
10. **Read-through.** Titles only, top to bottom. Fix gaps in the titles.
11. **Alternative key line** (optional). If the material supports a second
   structure, show its key line only (three to five lines) and say what it
   trades off. Do not build two full ghost decks.

## Output format

Use this layout and nothing else. No slide bodies, no notes, no design.

```
# Ghost deck: <working title>

Audience: … | Their question: …
Deck type: … | Setting: speaker-led / reading-first | Duration: … min incl. … min discussion
Slide budget: … | Language: …
Material: … | Not available / placeholders: …

Governing thought: <one sentence>

## Opening (SCQA, variant: …)
1. <Situation as a full sentence>
2. <Complication as a full sentence>
3. Management summary: <governing thought> (key line listed as bullets on this slide)

## Section A: <key-line claim 1 as a full sentence>
4. <supporting claim>  [evidence: available | missing | placeholder]
5. <supporting claim>  [evidence: …]

## Section B: <key-line claim 2>
6. …

## Closing
N-1. <governing thought restated / decision required>
N.   <next steps / ask>

## Backup (titles only, optional at this stage)
B1. …

## Register
| Entity (name used on every slide) | Category | Definition / source | Status |
|---|---|---|---|
| DSFA-Prozess | process | … | hypothesis, confirm |
| Governance-Board | body | … | from briefing |
| … | | | |
Sets: <plural noun> = <members in fixed order>; selection universe and criterion
where the set is a subset.

## Gap list (titles whose evidence is missing)
| # | Title | What is needed | From whom / where | Until |
|---|---|---|---|---|
| 5 | … | … | … | … |

## Timing skeleton
| Section | Slides | Minutes | Cut priority |
|---|---|---|---|
| Opening | 1-3 | 3 | must |
| … | | | |
| Discussion | – | 10 | must |

## Assumptions
- …

## Open points for the user
- …

## Alternative key line (only if useful)
- …
```

Every numbered line is a complete sentence with a subject and a verb, in the
deck language. Section headers repeat the key-line claim verbatim; they are the
same sentence that will later appear in the management summary.

## Title rules at this stage

- One claim per title. Two claims means two slides or one sharper claim.
- Specific over hedged: a number, a count, a named cause. No "may", "could
  indicate", "various".
- Active verb, named actor where possible.
- Length: readable in one breath. Around eight to sixteen words in English,
  ten to eighteen in German. Treat the count as a signal, not a rule; a
  precise long title beats a vague short one.
- Parallel grammar inside each peer set: all full sentences, or all
  noun-phrase assertions ("Three steps that cut approval time in half"), never
  mixed.
- No framework labels in titles. "SCQA: Situation" is commentary; the title is
  the situation itself.

## Timing skeleton

Derive from the total duration and the deck type:

- Decision paper, 30 min slot: 3 min opening, 15 min body, 2 min closing,
  10 min discussion. Discussion is never the buffer that gets eaten.
- Expert talk, 20 min plus Q&A: 2 min opening, 15 min body, 1 min closing.
- Status report, 15 min: 1 min opening, 10 min body, 4 min questions.

Rules of thumb: a message slide takes one to two minutes; a chart slide two to
three; a decision slide three to five with the discussion it triggers. If the
skeleton exceeds the slot, cut slides, not minutes per slide. Section dividers
only for decks of roughly 20 slides and more; shorter decks use the tracker.

Cut priorities:

- **must**: the deck does not work without it (opening, management summary,
  key line, decision).
- **should**: proves a key-line claim; cut only one per section if time is short.
- **could**: detail, illustration, second example; first to move to backup.

## The gate

End the Stage 1 reply with exactly one question: whether the ghost deck and
the register are approved as is, or which titles or register lines to change. Do not continue to Stage 2 in the
same turn. When the user replies with changes, apply them to the affected
titles, re-run the read-through, show the changed lines and ask again. When the
user replies "approved" or equivalent, start Stage 2 and say which version of
the ghost deck it builds on.

## Worked pattern (structure only, not content to reuse)

Briefing: city IT director must decide whether to merge three service desks.
Audience question: should we merge, and what does it take?

```
Governing thought: Merging the three service desks into one cuts ticket
resolution time by a third and pays back within two years.

Opening
1. Three service desks handle the same ticket types for 4,000 users with three
   tool stacks and three sets of SLAs.
2. Resolution times have doubled since 2023 while headcount stayed flat.
3. Management summary: one merged desk cuts resolution time by a third and pays
   back in two years.

Section A: One desk removes the double handling that causes most of the delay.
4. 38 % of tickets are passed between desks at least once.
5. Each hand-off adds a median of 1.4 days.

Section B: The merger costs 0.6 M€ once and saves 0.4 M€ a year.
6. One tool stack replaces three licences and two interfaces.
7. Staffing stays flat; two coordinator roles change, none is cut.

Section C: The merger is feasible in nine months with the existing team.
8. Phase 1 merges tooling, phase 2 merges queues, phase 3 merges SLAs.
9. The two known risks, data migration and staff acceptance, have owners and
   mitigations.

Closing
10. Decision required today: approve the merger and the 0.6 M€ budget.
11. Next steps: steering committee in two weeks, phase 1 start in Q1.
```

Key line order: structure (effect, cost, feasibility). Section A is
deductive (hand-offs happen, hand-offs cost time), sections B and C inductive.
The numbers are placeholders for the pattern; a real deck takes them from the
user's material.
