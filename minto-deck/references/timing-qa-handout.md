# Timing plan, Q&A preparation, backup, handout

The deck is one artefact of a presentation. These four complete it. Produce
them in Stage 2 after the slides and notes exist; they depend on both.

## Quick checklist

- [ ] Timing plan totals the slot; discussion reserved; half-time checkpoint; short version listed
- [ ] Minutes per slide identical in plan and notes
- [ ] Q&A grouped by what it attacks; answer first; evidence pointer per answer; hardest question first per group
- [ ] Section for questions that cannot be answered yet, with the holding answer
- [ ] Every backup slide referenced from a question or a main slide
- [ ] Handout: same storyline, reading-first density, key point and evidence in reader form, no cues, sources on the slide, PDF exported
- [ ] Slide references as number plus short title; regenerated after any renumbering
- [ ] Delivery note: files, open placeholders, unfixed warnings, what to rehearse

Detail follows; the checklist is what gets ticked before delivery.

## 1. Timing plan

A table, delivered as a separate document (Markdown or a sheet), not on a slide:

```
| # | Title (shortened) | Min | Cum. | Cut priority | Note |
|---|---|---|---|---|---|
| 1 | Title | 0.5 | 0.5 | must | |
| 2 | Management summary | 2 | 2.5 | must | |
| 3 | … | | | | |
| – | Discussion | 10 | 30 | must | reserved, not a buffer |
```

Rules:

- The total equals the slot. If it does not, cut "could" slides first, then
  one "should" per section. Never cut the discussion.
- Mark the slide at which the presenter must be when half the time is gone.
  That is the one checkpoint a presenter can actually use.
- Add a "short version" row set: which slides to show if the slot shrinks to
  half (typically opening, management summary, one slide per key-line claim,
  decision).
- Time per slide follows the notes' `Time:` line; the plan and the notes must
  agree.

## 2. Q&A preparation

A separate document. The audience attacks a deck at predictable points; prepare
those, not every conceivable question.

Group the questions by what they attack:

1. **The governing thought**: "Why this and not the alternative?", "What if we
   do nothing?"
2. **The evidence**: "Where does the number come from?", "Is the sample
   representative?", "How old is the data?"
3. **The scope**: "What about X, which you left out?", "Does this apply to
   our unit?"
4. **Cost, risk, feasibility**: "What does it really cost?", "What breaks if
   it fails?", "Who has done this before?"
5. **Implementation**: "Who owns it?", "When do we see results?", "What do you
   need from us?"
6. **The presenter's position**: "Why should we trust this analysis?",
   "What are you not telling us?"

For each question:

```
Q: <question as the audience would phrase it>
A: <two to three sentences, answer first>
Evidence: slide <n> / backup <Bn> / not in deck
```

Rules:

- Eight to twelve questions for a decision paper; four to six for a status
  report; the hardest question first in each group.
- Include a section "Questions we cannot answer yet" with the honest holding
  answer ("We have not measured that; we can within two weeks").
- Every answer that cites evidence points to a slide or backup number. If the
  evidence exists nowhere, either create a backup slide or mark the gap.
- Note which questions should be pre-empted in the talk track of the relevant
  slide; the hardest objection is often better named by the presenter than
  waited for.
- Slide references break when slides are renumbered. Write them as number plus
  short title ("slide 8, options") so a stale number is visible, and regenerate
  all references after any change in slide order as part of the consistency
  pass. The same holds for the timing plan and for cross-references inside
  the notes.

## 3. Backup slides

Criteria for a backup slide: it answers a question in the Q&A document, or it
holds detail a "could" slide lost in the cut, or it documents method and data
definitions. Each backup slide:

- has an action title like any other slide;
- is referenced from at least one Q&A answer or main slide ("detail in B3");
- follows the main deck's anatomy and density mode;
- is numbered B1, B2, … in the deck and in the documents.

A backup section without a referencing question is a sign that the main deck
cut the wrong slide.

## 4. Handout variant

Produce one when the deck will be read without the presenter: pre-read,
circulation after the meeting, email to absentees. Rules:

- Same storyline, same titles, same order. The handout is not a second deck.
- Reading-first density: the `Key point` from each slide's notes moves onto the
  slide as one short line, plus the evidence in reader form: the number and
  its source, not the presenter's pointing cue ("Point at:" lines never go on
  a slide). Sources and footnotes stay or expand; delivery cues disappear.
- Type may shrink one step; nothing below 11 pt.
- Add the management summary as the first page after the title and the
  next-steps page at the end even when the presented deck had them split.
- Export as PDF in addition to the editable file when the host can.
- Name the file so it cannot be confused with the presented deck
  (`…_handout.pptx`, `…_handout.pdf`).

## 5. Management summary as a standalone

When the user asks for a one-page summary for people who will see neither the
deck nor the talk, export slide 2 with the source lines of the numbers it
quotes. If slide 2 cannot stand alone, slide 2 is wrong; fix it there.

## 6. Delivery note

End Stage 2 with a short delivery note in the chat:

- files delivered (deck, handout, timing plan, Q&A document) with their paths;
- placeholders still open, by slide;
- warnings from the self-check that were not fixed and why;
- the one thing the presenter should rehearse (usually the management summary
  and the decision slide).
