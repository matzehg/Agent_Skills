# Sources

Every source the skill draws on, what it contributed, and how it was read.
"Read" means the text was read in full or in the parts cited during skill
development; "prior knowledge" means the author worked from training
knowledge of the work without re-reading it; "not read" means the source was
identified but not accessed. No source is reproduced in the skill; all rules
are paraphrased. Maintainers add a line here for every new source and note
which reference file it changed.

## Books

| Source | Status | Contributed to |
|---|---|---|
| Barbara Minto, *The Pyramid Principle* (Pearson, English ed.) | prior knowledge; the user owns the book | `minto-pyramid.md`: SCQA, pyramid rules, vertical and horizontal logic, orders, MECE, key line, problem definition |
| Gene Zelazny, *Say It With Charts* (McGraw-Hill) | prior knowledge, plus the public summary in StrategyU's "Think Before You Chart" | `visual-design.md` sections 1 and 6: five comparison types, message-first charting |
| Nancy Duarte, *slide:ology* (O'Reilly, 2008) | prior knowledge, plus thinkinsights.net summary | `visual-design.md` sections 3, 4, 10: whitespace, glance test, hierarchy, restraint |
| Nancy Duarte, *Slidedocs* (Duarte Press, 2014, free e-book) | not read: registration form; public summaries and guide pages used | `reading-decks.md` |
| Garr Reynolds, *Presentation Zen* (New Riders, 2008) | prior knowledge | `visual-design.md` sections 3, 10; `reading-decks.md` (slideument critique) |
| Cole Nussbaumer Knaflic, *Storytelling with Data* (Wiley, 2015) | prior knowledge | `visual-design.md` section 6a: decluttering sequence, preattentive attributes |
| Stephen Few, *Show Me the Numbers* (Analytics Press, 2nd ed. 2012) | prior knowledge | `visual-design.md` section 6b: tables for comparison |
| Hichert, Faisst et al., *IBCS Standards* (book edition of the online text) | online text read in full for SAY, STRUCTURE, EXPRESS, SIMPLIFY, CONDENSE, CHECK, UNIFY | `ibcs-notation.md` |
| Edward Tufte, *The Visual Display of Quantitative Information* | prior knowledge; not used directly | referenced via IBCS (data-ink ratio) and Knaflic; no separate rules |

## Standards and public rule sets

| Source | Status | Contributed to |
|---|---|---|
| IBCS Standards 1.1/1.2, online, https://www.ibcs.com/standards/ | read, October 2026 | `ibcs-notation.md`; adjustments in `visual-design.md` (chart titles, scenario fills) |
| IBCS Standards 2.0 release note, aligned with ISO 24896, https://www.ibcs.com/ibcs-version-2-0/ | read | `ibcs-notation.md` header (version status) |
| IBCS working group papers: mandatory vs optional semantic rules (2018); more scenarios per scenario type (2019) | skimmed via search excerpts | `ibcs-notation.md` section 8 |
| WCAG contrast ratios (W3C) | prior knowledge | `visual-design.md` section 5 |
| Agent Skills format and Anthropic skill-creator guidance | read | skill structure, `SKILL.md` conventions, eval format |

## Articles and web guides

| Source | Status | Contributed to |
|---|---|---|
| StrategyU (Paul Millerd), "The 14 Slide Layouts That Consulting Firms Use for Everything", 2026, https://strategyu.co/slide-layouts | read in full | `visual-design.md` section 2 (layout catalogue), section 8 (executive summary written last) |
| StrategyU, "Think Before You Chart: Why McKinsey Bans Pie Charts", 2026, https://strategyu.co/think-before-you-chart | read in full | `visual-design.md` sections 1, 6; chart checklist |
| Slidescience, course summary (five steps: top-down structure, SCR storyline, action titles, charts by insight type, executive summary last) | read, supplied by the user | `consulting-practices.md` sections 6, 8, 14; `storyline-ghost-deck.md` evidence check and gap list; `visual-design.md` sections 8, 9 |
| Slidescience, "What is an action title?", https://slidescience.co | search excerpt | `consulting-practices.md` section 2 (quantify, avoid the obviously true) |
| thinkinsights.net, "Designing Effective Slides" (Duarte applied to consulting) | search excerpts | `visual-design.md` sections 3, 4 |
| Duarte, "How to improve dense slides with Slidedocs" (guide page) | page read; downloadable guide not accessed | `reading-decks.md` |
| Nancy Duarte, "A presentation isn't always the right way to communicate", HBR, March 2014 | prior knowledge | `reading-decks.md` section 1 |
| Zen Faulkes, review of *Slidedocs*, Better Posters, 2014 | read | `reading-decks.md` (structure of the e-book) |
| zebrabi.com and other IBCS software vendors' explainers | search excerpts, used only to confirm the notation summary | `ibcs-notation.md` section 8 |

## Reference skills reviewed (structure only, no content reused)

| Skill | What was learned |
|---|---|
| zairuilab/consulting-deck (GitHub) | routing into modes, briefing contract, density modes, severity levels for findings |
| tyroneross/pyramid-principle (GitHub) | rule-indexed audit checklist, headline tests (disagreement, cover, verb), direct-language rules |
| mblode/agent-skills, presentation-creator (GitHub) | speaker-notes structure (key point, opening, talk track, transition), notes as prompts not script |

## Not used, and why

| Source | Reason |
|---|---|
| Slidescience and similar paid template packs | copyrighted slides; the skill works from rules, not examples; the public deck archives they resell are freely linked elsewhere |
| Ethan Rasiel, *The McKinsey Way* | MECE and hypothesis-driven work already covered by Minto and IBCS |
| Generic SEO articles from slide-tool vendors (deckary, slidespeak, chatslide, decktopus, presentations.ai and similar) | restate the above without added precision; skipped |

## Open: sources that need the user

- German public-sector submission formats (Leitungsvorlage: Betreff, Anlass,
  Votum, Sachstand, Bewertung; Gemeinsame Geschäftsordnung der
  Bundesministerien) as a deck type with mandatory elements.
- Military decision briefing formats (Lagevortrag zur Entscheidung, BLUF) as a
  variant, if relevant to the user's audiences.
- The user's own house rules and corporate template.
