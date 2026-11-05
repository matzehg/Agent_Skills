# Memo mode: answer-first prose

A memo is the pyramid written out. The governing thought leads, the key-line
claims are the section headings, each paragraph proves its heading. The method
is the same as for a deck; this file holds what differs: memo types, the
storyline format for the gate, the writing rules, how to derive a thesis from
source material, and how statements are attributed. Read `minto-pyramid.md`
first; it carries the rules this file applies.

## Quick checklist

- [ ] Memo type, audience and their question named; attribution setting settled
- [ ] Governing thought in the first sentence or title, as a claim someone could disagree with; marked "derived" when the user did not supply it
- [ ] SCQA opening with only what the reader does not know; variant named in the storyline
- [ ] Key line of three to five full-sentence claims, grouped by theme or argument, never by source order; one order, criterion named
- [ ] Every heading a full sentence; first sentence of every section and paragraph a claim; at most three sentences per paragraph
- [ ] Closing restates the governing thought; ask or next steps where the type requires
- [ ] Evidence with unit, period and source; attribution as settled; placeholders marked and listed
- [ ] Source material (sessions, documents, speakers) in an annex, not in the body
- [ ] Length within budget; no framework labels in the text
- [ ] Storyline approved before the memo is written, unless one-shot or under 300 words

Detail follows; the checklist is what gets ticked before delivery.

## 1. Memo types and mandatory elements

Identify the type first; the completeness check needs a target.

| Memo type | Mandatory elements | Typical length |
|---|---|---|
| **Management summary** (Zusammenfassung für die Leitung) | governing thought as first line; key line as three to five sentences, bold or as a list; the ask; key numbers that make the claim concrete; stands alone without the underlying deck or report | 150 to 300 words, one page at most |
| **Briefing note** (Vermerk, Sprechzettel in prose) | Betreff; purpose (information, decision, signature); Votum or governing thought first; Anlass (why now, who asked); Sachverhalt as agreed facts; Bewertung with risks and alternatives considered; next steps with owners and dates; attachments listed | one to two pages |
| **Event or meeting report** (Veranstaltungsbericht, Sitzungsbericht, Tagungsbericht) | thesis of the event in the lead; what it means for the reader's organisation or decision; key line by theme, not by session; dissent and open questions named; attribution as settled; session or agenda table with speakers, format, duration and one-sentence message in an annex | 600 to 1,500 words plus annex |
| **Decision memo** (Entscheidungsvermerk) | problem as R1 (today) and R2 (wanted); options with explicit criteria, shown before the detail of the recommended one; recommendation marked; cost, benefit, risk with period and owner; the decision worded as a proposal; consequence of no decision; next steps | one to three pages |
| **Status note** (Statusnotiz) | overall status in one sentence; planned versus achieved; deviations with cause; decisions or support needed; next period; risks that changed | half a page to one page |
| **Thesis of a day** (These des Tages; the shortest form of the event report) | one governing thought; key line of three to five claims; one sentence of evidence per claim; nothing else | 100 to 250 words |

Elements every type needs: a governing thought before the evidence, full-sentence
headings, a visible key line in the same wording in lead, headings and closing,
sources on external numbers, consistent terminology from the register.

## 2. Stage 1 output format (the storyline)

Use this layout and nothing else. No body text yet.

```
# Memo storyline: <working title>

Audience: … | Their question: …
Memo type: … | Length budget: … words | Destination: chat / doc / file | Language: …
Material: … | Not available / placeholders: …
Attribution: named / role only / none (see section 5)
Deck follows: yes / no

Governing thought (<from user | derived>): <one sentence>

Opening (SCQA, variant: …)
- Situation: <one sentence the reader already accepts>
- Complication: <one sentence; what changed or is at stake>

Key line (order: <theme | time | structure | degree | chain>, criterion: …)
1. <claim as a full sentence>
2. <claim as a full sentence>
3. <claim as a full sentence>
(4., 5. only when the material needs them)

Closing: <governing thought restated> | Ask / next steps: <… or "none for this type">

Register (only when names must stay consistent)
| Entity | Category | Definition / source | Status |
|---|---|---|---|

Annex planned: <session table | document list | none>

Assumptions
- …

Open points for the user
- …

Alternative key line (only if the material supports a second structure)
- …
```

Every key-line line is a complete sentence with subject and verb, in the memo
language. The headings in Stage 2 repeat these sentences verbatim.

## 3. Writing rules

**Lead.** The first sentence is the governing thought, or the complication in
the "concerned" SCQA variant with the governing thought in the second sentence.
The lead carries the key line in compressed form when the memo exceeds roughly
500 words, so that a reader who stops after the lead still has the argument.
Two to four sentences. No "This memo summarises", no "In the following".

**Headings.** The key-line claims, verbatim. A heading is a sentence the reader
can disagree with. "Regulierung" is a topic; "Die Regulierungsdebatte hat sich
von Verboten zu Kontrollmaßnahmen verlagert" is a heading. Sub-headings only
when a section exceeds roughly 300 words, and then as claims too.

**Paragraphs.** One idea each. The first sentence states the idea; the following
sentences prove or qualify it. At most three sentences; a fourth sentence is a
new paragraph or belongs in a list. Sentences under 25 words, plain words, the
reader's language.

**Order inside a section.** The paragraphs of a section form one peer set:
same kind, one order, visible in the wording (`minto-pyramid.md` sections 3
and 6). When a section mixes reasons and steps, split it.

**Lists and tables.** A list for three or more parallel items of the same kind,
each item one line, starting with the claim. A table for items compared on
several attributes (options against criteria, sessions with speaker, format
and message). Neither as a substitute for an argument: a list of topics is a
topic heading in disguise.

**Closing.** The governing thought in the same words as the lead, with the
confidence the evidence earned. Then the ask, the next steps with owners and
dates, or the open questions. Nothing new is introduced here.

**Density by audience.** Internal readers accept abbreviations and internal
names; external readers get the full name on first use and no internal
references. A mixed audience is written for the external reader.

**Framework labels.** None in the text. SCQA, key line, governing thought,
MECE belong in the storyline and in the author's commentary.

**Length budget.** Agreed in Stage 0, enforced in Stage 2. Cut evidence before
claims, examples before mechanisms, never the key line.

### Before and after

```
Before (recap)                                  After (answer-first)
## Session 1: Keynote                           ## Ohne eigene Daten und KI-Fähigkeit bleibt eine Armee nicht handlungsfähig
Der Referent sprach über digitale                Daten sind eine strategische Ressource. Wer Zugang zu Rechenleistung und
Kriegstüchtigkeit und stellte sechs              Modellen verliert, verliert Handlungsfähigkeit. Die Bundeswehr nutzt Daten
Dimensionen vor. Danach ging es um               nach zentraler Data Governance und erprobt KI-gestützte Lagebilder seit 2025.
Daten und um die EU-KI-Verordnung.
```

The left column follows the source; the right column states what the source
proved and uses the evidence for that claim only.

## 4. Deriving a thesis from source material

When the user supplies notes, transcripts or several talks and has no governing
thought, derive one. Label it "derived" in the storyline; the gate exists so the
user can replace it.

1. **Collect the claims.** For each source (talk, session, document) write the
   two to four claims it actually made, as full sentences, with the evidence it
   gave. Skip descriptions of what was discussed; keep what was asserted.
2. **Cluster by theme.** Group the claims across sources by what they are about,
   not by where they came from. A cluster that holds claims from one source only
   is a candidate for the annex, not for the key line.
3. **Name each cluster with its insight.** The sentence the claims in the
   cluster share or add up to (`minto-pyramid.md` section 7). "Three talks
   addressed testing" is a count; "Testing replaces explainability as the basis
   for trust" is an insight. These sentences are the key-line candidates.
4. **Find the apex.** What do the cluster sentences prove together? Write it as
   one sentence the reader's organisation could act on or disagree with. It
   answers the reader's question (what does this mean for us), not the
   speakers' questions.
5. **Test.** Disagreement test: could a reasonable reader object? Scope test:
   do the clusters cover the material that matters to the reader? Order test:
   can the order of the clusters be named? Read-through: lead, key line,
   closing, in sequence.
6. **Record dissent.** Where sources contradict each other, the contradiction
   is a finding, not noise. It goes under the claim it concerns or in an
   "open questions" section, with both positions attributed as settled.

Example, derived from a one-day expert event on AI governance with four talks:
clusters "regulation moves from bans to controls", "trust comes from tests, not
explanations", "the state must put its requirements into contracts". Apex:
"Für Behörden entscheidet sich KI-Governance in Beschaffung und Prüfverfahren,
nicht in neuen Gesetzen." A reader can disagree; three clusters prove it; the
order is degree (from the international frame to the local lever).

## 5. Attribution and confidentiality

Settle this in Stage 0 and write it into the storyline; it changes the text.

| Setting | Use when | In the text |
|---|---|---|
| **Named** | public event, speakers listed on the programme, the user confirms | name and organisation on first mention per section; quotes only when the material has them verbatim and the user allows quotes |
| **Role only** | internal meeting, workshop, panel under house rules | "a ministry representative", "the industry side"; no names, no organisations that identify a person |
| **None** (Chatham House) | the user says so, or the material is a transcript of a closed meeting | claims without source; the annex lists the event and its format, not the speakers |

Default when the user has not said: role only, and an open point in the
storyline asking whether names may be used. Transcript uncertainties (a name
the recorder misheard, a first name without surname) are flagged in the open
points, not guessed. The user's own contribution, when the user spoke at the
event, is attributed like everyone else's and not weighted higher.

## 6. The gate

End the Stage 1 reply with exactly one question: whether governing thought and
key line are approved, or which lines to change. Do not write the memo in the
same turn. When the user replies with changes, apply them, re-run the
read-through on the key line, show the changed lines and ask again. When the
user replies "approved" or equivalent, write the memo and say which storyline
version it follows.

Exceptions, both named in the reply: the user asked for a one-shot run; or the
memo is a thesis of a day or under roughly 300 words, where the storyline and
the memo are nearly the same text. Then state governing thought and key line in
two lines, write the memo, and invite changes afterwards.

## 7. Bridge to Build

| Memo element | Deck element |
|---|---|
| governing thought | governing thought; title of slide 2 (management summary) |
| SCQA lead | opening slides 1 to 3 |
| key-line claims (headings) | section titles; bullets of the management summary |
| first sentence of each paragraph | candidate slide title; proven by that paragraph's evidence |
| lists and tables | evidence slides (table, cards, chart by comparison type) |
| closing with ask | closing slide, decision slide or next steps |
| annex (session table, document list) | backup |
| register | register, unchanged |
| open questions and dissent | Q&A preparation; backup |

Start Build Stage 1 from the approved memo storyline, add evidence marks and
the timing skeleton, and gate again only on what changed. The memo is then the
handout or the pre-read of the deck.

## 8. Frequent failures and the fix

| Failure | Looks like | Fix |
|---|---|---|
| Recap | sections follow the agenda or the speakers | regroup by theme; sessions go to the annex |
| Buried thesis | the point appears in the last paragraph | move it to the first sentence; keep the ending as restatement |
| Topic headings | "Regulierung", "Ausblick" | write the claim the section proves |
| Counting lead | "Six sessions covered five themes" | state what the themes add up to |
| Quote collage | the memo strings together what people said | claims first; a quote only as evidence for a claim, attributed as settled |
| Speaker weighting | one talk gets a section because it was long | sections prove claims; a long talk may yield one sentence |
| Hidden dissent | contradictions smoothed into one position | name both positions and what remains open |
| Internal shorthand for external readers | abbreviations and project names unexplained | full name on first use; write for the external reader |
| Budget overrun by evidence | three examples per claim | one example per claim; the rest to the annex or cut |
