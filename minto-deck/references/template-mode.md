# Template mode: building on a corporate template

Quick checklist:
- [ ] Three layers kept apart: the template supplies the shell (master, theme, fonts, chrome, layouts); the skill supplies the information design (which form proves the title); the briefing supplies the content
- [ ] Template brief in Stage 0: three layouts named (cover, section, content base), free body zone measured, colour roles mapped, footer and slide number confirmed as layout chrome; drafted by `scripts/template-probe.py`, confirmed by the user
- [ ] Every content slide sits on the content base layout; body placeholders are deleted, never filled (T1)
- [ ] Every exhibit drawn as native shapes in the body zone, in the approved form; approved form equals built form on every content slide (T2, `deck-metrics.py --forms`)
- [ ] No content slide whose free text containers cover more than 60 % of the body zone without an exhibit (T3)
- [ ] Every slide rendered at full size and looked at; the delivery note lists the slides checked and what was fixed (T4)
- [ ] Nothing of the template redrawn by hand: no second logo, footer or slide number
- [ ] Company-specific values (layout names, colour roles) in a private companion skill, never in this public skill

## 1. Why this page exists

A template invites one shortcut: pick a layout that has text placeholders and
pour the content into them. The result is branded and dead. The first test of
this skill on a corporate master produced exactly that: a contrast, a cycle
and a flow, all approved as form marks, all delivered as text columns. Every
rule that forbids it already existed (message first, exhibits first, native
shapes, render review). What was missing is this page: what a template may
decide, what it may not, and three checks that make the shortcut fail before
delivery.

## 2. Three layers

| Layer | Supplies | Decided by | Never decides |
|---|---|---|---|
| Corporate shell | slide size, master, theme colours and fonts, logo, footer, slide number, the three layouts | the template, confirmed in the template brief | the form of an exhibit, the text budget, the storyline |
| Information design | which form proves the title (contrast, cycle, flow, table, chart, …), reading direction, the one highlight, text budget by density mode | this skill: form marks at the gate, `exhibits.md`, `visual-design.md` | colours, fonts, chrome |
| Content | what the exhibit says: register names, numbers, sources, placeholders | the briefing and the approved ghost deck | layout or form |

The template says how the deck looks. The skill says how the argument is
drawn. The briefing says what it says. A decision that crosses a line (a
layout chosen because it exists, a form changed because a placeholder is
there) is wrong by construction.

## 3. Template brief (Stage 0)

Run `python3 scripts/template-probe.py <template> --json probe.json --md brief.md`.
The brief is a draft; the user confirms it once, and the confirmed values go
into the private companion skill (section 5), so the next deck starts from
them. The brief holds:

- **Three layouts.** Cover (title slide), section (divider, optional) and the
  content base: the layout with a title placeholder and the chrome and nothing
  else. When no such layout exists, the one with the fewest body placeholders
  is the base and the helpers delete its body placeholders on every slide.
  Agenda, two-column, picture-left and quote layouts are never the base.
- **Body zone.** The free rectangle under the title band and above the footer
  band on the content base, measured in inches. Every exhibit is drawn inside
  it; the last 0.35 in carry the source line (left) and the tracker (right).
- **Colour roles.** The theme palette mapped to the skill's three roles:
  message (the one highlight per exhibit, the recommended option), signal
  (warnings, caveat boxes), neutral (everything else), plus muted for sources
  and labels, text, background and tint. The probe proposes accent1, accent2,
  dk2; brand palettes differ, so the user confirms. One deck, one mapping.
- **Fonts.** Inherited from the theme; the helpers never set a font name.
  Sizes follow the density mode (`exhibits.md` section 6, `visual-design.md`
  section 4), not the template's placeholder sizes.
- **Chrome.** Footer text, slide number, logo and rules come from the layout.
  Nothing of them is redrawn on a slide. When the template's chrome occupies
  the top right, the tracker moves to the bottom line.
- **Not available.** Say which of the three layouts is missing and what the
  deck does instead (a section lead slide instead of a divider; a neutral
  cover when the template has none).

## 4. The gates (Stage 2 and Audit)

| Id | Gate | How it is checked | Severity |
|---|---|---|---|
| T1 | The template never decides the form. Content slides use the content base; body placeholders are deleted, never filled; the approved form mark is built with native shapes on that slide. | `pptx_template_helpers.py` deletes body placeholders on every new slide; the Audit lists any slide whose body is a filled placeholder | blocker |
| T2 | Approved form equals built form. The build declares the form mark per content slide; the finished file shows a chart, a table, a concept drawn from shapes, a picture or text accordingly. | `deck-metrics.py --forms <deck>.forms.json`; both helper paths write the sidecar | blocker on any mismatch |
| T3 | No text-block slides. On a content slide without an exhibit, free text containers (text boxes, cards, filled placeholders; tables excluded) may not cover more than 60 % of the body zone. Management summary and decision slide are exempt. | `deck-metrics.py` reports `text-block` per slide | blocker in a speaker-led deck, warning in a reading-first deck |
| T4 | Render review with evidence. Every slide rendered at full size and looked at before delivery. | The delivery note lists the slides reviewed and the fixes made; a delivery note without the list is incomplete | warning; blocker when a reported fix is visibly absent |

T2 and T3 are machine checks: run them before the self-check and paste the
summary lines into the delivery note. T1 and T4 are read off the file and the
note. The gates apply to every host and every rendering path, not only to
decks built on a template: a neutral deck can die the same death.

## 5. The private companion skill

This skill stays generic. Company values go into a small private skill the
user keeps outside public repositories, with one file per template:

```
---
name: deck-templates-<company>
description: Template briefs for <company> decks; read when a deck is built on a <company> template.
---
# <Company> standard template
- file: <path or OneDrive name>
- layouts: cover "…", section "…", content base "…"
- body zone: x … y … w … h … in
- colour roles: message <slot/hex>, signal <slot/hex>, neutral <slot/hex>, muted <slot/hex>
- chrome: footer and slide number from the layout; tracker bottom right
- house rules: <anything the brand guide adds: no full-bleed colour, logo clear zone, …>
```

When both skills are loaded, the template brief is read from the companion
skill and only confirmed; the probe runs again only when the template changed.

## 6. Which helper, which host

| Host has | Path | Notes |
|---|---|---|
| Python with python-pptx | `scripts/pptx_template_helpers.py` on the template | the only path that opens a foreign master; works in claude.ai, Claude Code, Cowork, Copilot and Codex sandboxes |
| Node with pptxgenjs, no template | `scripts/pptx-helpers.js` | neutral design; pptxgenjs cannot load a template |
| neither | Markdown outline with notes | say so; the template is applied by hand later |

A host tool that fills template placeholders (an Office add-in, a slides
connector) is never the path for content slides: it is the shortcut this page
forbids. It may still open, preview or deliver the file the helpers wrote.

## 7. Worked pattern

Briefing: expert talk on a corporate master, forms approved at the gate as
contrast (slide 3), cycle (slide 4), linear flow with human gates (slide 5).

1. Probe the template; confirm cover, section, content base, body zone and
   colour roles with the user; store them in the companion skill.
2. Build: `TemplateDeck(template, probe)`; `content(..., form="concept:contrast", build=contrast(...))`,
   `content(..., form="concept:cycle", build=cycle(...))`,
   `content(..., form="concept:linear-flow", build=chevrons(...) + gate bar)`.
3. `deck-metrics.py deck.pptx --forms deck.forms.json`: "3 of 3 slides match
   their approved form", no text-block slides. Paste the two lines into the
   delivery note.
4. Render every slide, look, fix, list the fixes.

What the first test did instead: step 2 used the template's two-column layout
and filled both placeholders on all three slides. Under this page that fails
T1 on sight and T2 and T3 by machine, and the deck is not delivered.
