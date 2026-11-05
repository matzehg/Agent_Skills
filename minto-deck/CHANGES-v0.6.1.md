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

README changelog line:
`- v0.6.1: Memo-mode fixes from the first real run: SCQA opening with Question and Answer in memo and ghost-deck storylines; Sets line in the memo register; evidence marks per key-line claim; dissent and implications lines in the storyline; Implications step in Stage 2; heading length rule; list rule for enumerated items.`
