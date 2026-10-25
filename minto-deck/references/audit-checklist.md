# Audit checklist

Used twice: as the Stage 2 self-check before delivery, and as the full review
in Audit mode. The checks are the same; only the report differs (self-check:
fix blockers, list warnings; Audit: full report, no changes).

## 1. Deck types and mandatory elements

A completeness check needs a target. Identify the type first; ask if the user
has not said and the deck does not make it obvious.

| Deck type | Mandatory elements |
|---|---|
| **Decision paper** (Entscheidungsvorlage) | title with decision date; management summary with the ask; SCQA opening; options with explicit criteria, shown before the detail of the recommended one; recommended option marked; cost and benefit with period; risks with owners and mitigations; decision slide worded as a proposal (Beschlussvorschlag: what is decided, consequence of no decision, what is needed today); next steps with owners and dates; sources; backup for the Q&A |
| **Status report** (Statusbericht) | management summary with overall status in one sentence; progress against plan (what was planned, what happened); deviations with cause; decisions or support needed from the audience; next period's plan; risks that changed since last report |
| **Proposal or pitch** (Angebot) | management summary with the offer in one sentence; understanding of the client's question (SCQA); approach and phases; deliverables; team and roles; timeline; price or effort with assumptions; why this team; next steps and decision needed from the client; references where allowed |
| **Expert talk** (Fachvortrag) | title with speaker and date; the one claim of the talk on slide 2; three to five sections that prove it; at least one concrete example per section; what the audience can do with it; contact or further reading |
| **Reading deck** (Lesedeck, pre-read) | management summary that stands alone; every slide self-explanatory; sources and footnotes on the slide; glossary or definitions where terms are new; no delivery cues; page numbers |

Elements that every type needs: action titles throughout, a governing thought
before the evidence, a visible key line (sections, tracker or agenda in the
same wording), source lines on external numbers, consistent terminology.

## 2. Checks

Run in this order; each level depends on the one above.

### A. Governing thought

| # | Check | Red flag |
|---|---|---|
| A1 | A governing thought exists as a claim | title of slide 2 is a noun phrase; the only claim appears at the end |
| A2 | It appears before the evidence | first substantive claim after the midpoint |
| A3 | It answers the audience's question | audience asks "what should we do?", deck answers "what happened" |
| A4 | It can be disagreed with | platitude ("digitalisation is important") |
| A5 | The closing restates it in the same words | ending introduces a new claim or none |

### B. Key line and structure

| # | Check | Red flag |
|---|---|---|
| B1 | Three to five key-line claims, each a full sentence | agenda of topics; seven sections |
| B2 | Same kind (plural-noun test) | reasons and steps mixed |
| B3 | No overlap; scope named and covered | same evidence under two sections |
| B4 | One logical order per set, visible in wording | order cannot be named |
| B5 | Sections, tracker, agenda, management summary use the same wording | three versions of the key line |
| B6 | Deductive chains have at most four steps | five "therefore" steps |
| B7 | Named sets are consistent: same members, names, order and category on every slide | a committee listed among processes; a fourth member appearing on one slide only |
| B8 | Subsets name their universe and selection criterion | "three processes" with no word on which others were considered |

### C. Titles

| # | Check | Red flag |
|---|---|---|
| C1 | Every title is a claim (disagreement test) | "Overview", "Analysis", "Risks" |
| C2 | Every title survives the cover test | chart carries the point, title names it |
| C3 | One claim per title | "and" joining two claims |
| C4 | Specific, no hedges | "may", "various", "significant" |
| C5 | Parallel grammar within each section | full sentences mixed with fragments |
| C6 | Read-through of all titles forms the argument | gaps, repeats, jumps |

### D. Slide level

| # | Check | Red flag |
|---|---|---|
| D1 | Body answers exactly the question the title raises | body proves a different claim |
| D2 | One dominant evidence element | two charts competing |
| D3 | Chart type matches the comparison; chart title states the message | pie for a time series; metric as chart title |
| D4 | Units, period, denominator, source on every number | "costs fell 20 %" with nothing else |
| D5 | Facts, estimates, hypotheses distinguished | hypothesis presented as fact |
| D6 | Density consistent with the mode | one slide with 90 words next to one with 6 |
| D7 | No framework labels or internal notes on the slide | "SCQA", "TBD", "draft" |

### E. Completeness

| # | Check |
|---|---|
| E1 | All mandatory elements of the deck type present (section 1) |
| E2 | Decision or ask explicit where the type requires it |
| E3 | Next steps have owners and dates |
| E4 | Backup exists for the evidence the Q&A will need |
| E5 | Options are shown as options (title names count and criteria) before the detail of the recommended one; the decision is worded as a proposal |

### F. Didactics

| # | Check | Red flag |
|---|---|---|
| F1 | Speaker notes exist for every slide (presented decks) | empty notes pane |
| F2 | Notes are prompts with key point and transition, not a script | 300-word paragraphs |
| F3 | Transitions at section boundaries are spoken | section dividers with no bridge |
| F4 | Timing fits the slot with discussion reserved | 25 slides for 20 minutes |
| F5 | Q&A preparation exists and points to slides | none, or answers without evidence |
| F6 | Opening matches the audience's knowledge | three slides explaining what the room knows |

### G. Form

| # | Check |
|---|---|
| G1 | Titles same position and size on every slide |
| G2 | Tracker and page numbers present and consistent |
| G3 | Terminology consistent (glossary) |
| G4 | Number and date formats consistent |
| G5 | No text overflow, overlap, leftover placeholders |
| G6 | Charts editable, not pasted images |
| G7 | Geometry: connectors attach to shapes, boxes span what points to them, peers have equal size, no orphan labels |
| G8 | Whitespace distributed, not pooled; type and shapes scaled to the density mode |
| G9 | Tables in list style (no vertical rules, no dark header band); two or three rows shown as cards or list, not table |
| G10 | Section dividers only in long decks; one before backup at most |

## 3. Severity

- **Blocker**: the deck fails its purpose. Missing or buried governing thought,
  key line not a set, mandatory element of the deck type missing, invented or
  unsourced material numbers, titles that are topic labels throughout.
- **Warning**: the argument holds but loses force. Single weak titles, mixed
  grammar, missing notes on some slides, timing over by less than 20 %, chart
  type mismatch.
- **Advisory**: craft. Formatting, consistency, length, decorative elements.

In the Stage 2 self-check, fix every blocker before delivery and list the
warnings in the delivery note. In Audit mode, report all three levels.

## 4. Audit report format

```
# Audit: <deck name>

Verdict: <one sentence: does the deck do its job, and what is the main fix>
Deck type assumed: … | Audience: … | Setting: … | Slides: n (+ backup m)
Not checked: <what the input did not allow, e.g. notes, layout, charts>

## Title read-through
| # | Title (verbatim) | Flag | Proposed title |
|---|---|---|---|
| 2 | "…" | topic label | "…" |
| 5 | "…" | ok | |

## Findings
### Blockers
- [A1] Slide 2: … → fix: …
### Warnings
- [C4] Slide 7: … → fix: …
### Advisory
- [G2] …

## Missing elements for a <deck type>
- …

## Three changes with the largest effect
1. …
2. …
3. …
```

Rules for the report:

- Quote titles verbatim; propose the rewrite next to each flagged one.
- Reference the check ID so the user can look it up.
- Say what could not be checked instead of guessing (a pasted outline has no
  notes; a PDF has no notes pane).
- Do not rewrite the deck. Offer Build Stage 1 on the corrected storyline as
  the next step.
- Keep the report under two pages for a fifteen-slide deck; detail beyond that
  goes into an appendix table.
