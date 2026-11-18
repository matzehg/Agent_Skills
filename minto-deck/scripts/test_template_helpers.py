#!/usr/bin/env python3
"""test_template_helpers.py — smoke test for the template path.

    python3 scripts/make-synthetic-template.js is NOT needed: the template ships
    in assets/. Run:  python3 scripts/test_template_helpers.py

Checks: sample slides dropped, no body placeholder survives on a content slide
(gate T1), slide-number field copied, theme fonts inherited (none set), chevron
text behind the notch, cycle arrows long enough, narrow-column warning, words
without marks, PH() per language, forms sidecar written, deck-metrics.py
confirms every form (gate T2), and a text-block slide fails gates T2 and T3.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pptx_template_helpers import TemplateDeck, words_of  # noqa: E402
from pptx import Presentation  # noqa: E402
from pptx.enum.shapes import PP_PLACEHOLDER  # noqa: E402

TEMPLATE = os.path.join(HERE, "..", "assets", "synthetic-corp.pptx")
EMU = 914400.0
fails = 0


def check(cond, msg):
    global fails
    print(("ok: " if cond else "FAIL: ") + msg)
    if not cond:
        fails += 1


tmp = tempfile.mkdtemp()
probe_json = os.path.join(tmp, "probe.json")
subprocess.run([sys.executable, os.path.join(HERE, "template-probe.py"), TEMPLATE, "--json", probe_json, "--md", os.path.join(tmp, "brief.md")], check=True)
probe = json.load(open(probe_json, encoding="utf-8"))
check(probe["recommended"]["content"] == "Content" and probe["recommended"]["cover"] == "Cover", "probe recommends Cover and Content layouts")
check(probe["theme"]["fonts"].get("heading") == "Georgia" and probe["theme"]["colors"].get("accent1") == "E8702A", "probe reads theme fonts and palette")

d = TemplateDeck(TEMPLATE, probe=probe_json, mode="speaker", lang="de")
Z = d.Z
d.title_slide("Titel", ["Untertitel"], notes={"key": "k", "time": 0.5})
d.content("Fluss", "Chevron-Test als Satz", "Quelle: Test", notes={"key": "k", "time": 1}, form="concept:linear-flow",
          build=lambda s, h: h.chevrons(s, [{"head": "Meldung", "sub": "a"}, {"head": "Einstufung", "sub": "b"}, {"head": "Freigabe", "sub": "c"}], Z.y + 0.5, 1.4, hl=1))
d.content("Kreis", "Kreislauf-Test als Satz", "Quelle: Test", notes={"key": "k", "time": 1}, form="concept:cycle",
          build=lambda s, h: h.cycle(s, ["Üben", "Beobachten", "Auswerten", "Anpassen", "Ausbilden", "Prüfen"], Z.x + Z.w / 2, Z.y + Z.h / 2 - 0.2, 1.9, hl=2))
d.content("Tabelle", "Tabellen-Test als Satz", "Quelle: Test", notes={"key": "k", "time": 1}, form="table",
          build=lambda s, h: (h.ltable(s, Z.x, Z.y, 4.0, [["Phase", "Personentage"], ["Phase 1", h.PH("PT")]], [2.8, 1.2]),
                              h.txt(s, "● ◐ ○  ✓ ✗", Z.x, Z.y + 2, 4, 0.4)))
r = d.write(os.path.join(tmp, "good.pptx"))
check(r["slides"] == 4, f"sample slides dropped, four built ({r['slides']})")

prs = Presentation(r["path"])
content_slides = list(prs.slides)[1:]
body_left = [ph.placeholder_format.type for s in content_slides for ph in s.placeholders if ph.placeholder_format.type not in (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE, PP_PLACEHOLDER.SLIDE_NUMBER, PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.DATE)]
check(not body_left, f"no body placeholder survives on a content slide (gate T1) {body_left}")
z = zipfile.ZipFile(r["path"])
s2 = z.read("ppt/slides/slide2.xml").decode("utf-8")
check('type="slidenum"' in s2, "slide-number field copied from the layout")
free_text_fonts = [run.font.name for s in content_slides for sh in s.shapes if sh.has_text_frame and (sh.name or "") in ("text", "label", "source", "tracker") for p in sh.text_frame.paragraphs for run in p.runs if run.font.name]
check(not free_text_fonts, f"theme fonts inherited, none set on free text {free_text_fonts[:3]}")

sp = list(prs.slides)[1]
chev = [sh for sh in sp.shapes if sh.name == "chevron"]
texts = [sh for sh in sp.shapes if sh.name == "text"]
behind = all(any(abs(t.left - c.left) < EMU * 5 and t.left >= c.left + c.height / 2 - 100 and t.left + t.width <= c.left + c.width + 100 for c in chev) for t in texts if any(abs(t.left - c.left) < EMU * 5 for c in chev))
check(len(chev) == 3 and behind, "chevron text starts behind the h/2 notch (1.4 in chevron)")
check(not any(w["kind"] == "cycle-arrow-short" for w in r["warnings"]), f"six-node cycle keeps arrows of at least 0.25 in ({[w for w in r['warnings'] if w['kind'] == 'cycle-arrow-short']})")
check(any(w["kind"] == "narrow-column" and w["slide"] == 4 for w in r["warnings"]), f"narrow-column warning fires for a 1.2 in placeholder column ({[w for w in r['warnings'] if w['kind'] == 'narrow-column']})")
check(words_of("● ◐ ○ ✓ ✗") == 0 and words_of("[PLACEHOLDER: x] a b") == 2 and words_of("[PLATZHALTER: PT] 42 %") == 1, "marks and placeholders are not counted as words")
check(TemplateDeck(TEMPLATE, probe=probe_json, lang="en").PH("x") == "[PLACEHOLDER: x]" and d.PH("x") == "[PLATZHALTER: x]", "PH() follows the deck language")
check(os.path.exists(r["forms_path"]) and len(json.load(open(r["forms_path"]))) == 3, "forms sidecar written with one entry per content slide")

out = subprocess.run([sys.executable, os.path.join(HERE, "deck-metrics.py"), r["path"], "--mode", "speaker", "--skip", "1", "--forms", r["forms_path"]], capture_output=True, text=True).stdout
check("3 of 3 slides match their approved form" in out, "deck-metrics confirms every approved form (gate T2)")

# negative: a "cycle" built as four text boxes must fail T2 and T3
b = TemplateDeck(TEMPLATE, probe=probe_json)
b.content("Kreis", "Kreislauf als Textfriedhof", "Quelle: Test", notes={"key": "k", "time": 1}, form="concept:cycle",
          build=lambda s, h: [h.txt(s, f"Station {i + 1}: Text, Text, Text, Text, Text", c.x, Z.y + 0.3, c.w, 3.5) for i, c in enumerate(h.cols(4))])
rb = b.write(os.path.join(tmp, "bad.pptx"))
outb = subprocess.run([sys.executable, os.path.join(HERE, "deck-metrics.py"), rb["path"], "--mode", "speaker", "--forms", rb["forms_path"]], capture_output=True, text=True).stdout
check("BLOCKER form mismatch" in outb and "text-block" in outb, "a text-box 'cycle' fails the form check (T2) and the text-block check (T3)")

print(f"\n{'all checks passed' if not fails else str(fails) + ' check(s) failed'}; files in {tmp}")
sys.exit(1 if fails else 0)
