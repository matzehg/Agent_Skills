#!/usr/bin/env python3
"""example-template-build.py — builds a seven-slide deck on the synthetic template.

    python3 scripts/template-probe.py assets/synthetic-corp.pptx --json /tmp/probe.json
    python3 scripts/example-template-build.py /tmp/probe.json out.pptx [speaker|handout]

Every content slide declares its approved form mark (form=...), so
deck-metrics.py --forms out.forms.json can check gate T2. The deck shows the
forms the template path must produce with native shapes: contrast, cycle,
linear flow with a gate bar, scorecard table, numbered decision cards.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pptx_template_helpers import TemplateDeck  # noqa: E402

probe = sys.argv[1] if len(sys.argv) > 1 else "/tmp/probe.json"
out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/example-template.pptx"
mode = sys.argv[3] if len(sys.argv) > 3 else "speaker"
TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "synthetic-corp.pptx")

d = TemplateDeck(TEMPLATE, probe=probe, mode=mode, lang="de")
PH, Z = d.PH, d.Z

d.title_slide("Ausbildung mit KI: Lernschleife statt Lehrplan", ["Entscheidungsvorlage für die Leitungsrunde", PH("Datum") + " · " + PH("Vortragende")],
              notes={"key": "Die Leitung entscheidet heute über die Lernschleife.", "time": 0.5})

d.content("Management Summary", "Eine geschlossene Lernschleife mit menschlichen Freigaben ersetzt den starren Lehrplan, ohne neue Stellen",
          "Quelle: Briefing; „ohne neue Stellen“ ist eine Annahme", form="text",
          notes={"key": "Lernschleife statt Lehrplan; Annahme offen benennen.", "time": 1.5},
          build=lambda s, h: (
              h.bullets(s, ["Der heutige Lehrplan bricht unter Belastung, weil er Soll-Prozesse ohne Rückkopplung vorgibt.",
                            "Eine Lernschleife aus sechs Stationen schließt die Lücke zwischen Übung und Einsatz.",
                            "KI übernimmt drei Phasen der Schleife; vier menschliche Freigaben bleiben."], Z.x, Z.y, Z.w, 3.0, size=18, gap=20),
              h.box(s, Z.x, Z.y + 3.3, Z.w, 1.1, h.C["tint"], name="ask-box"),
              h.txt(s, [{"text": "Beschlussvorschlag: ", "bold": True}, {"text": "Lernschleife einführen, Freigaben besetzen."}], Z.x + 0.25, Z.y + 3.3, Z.w - 0.5, 1.1, valign="middle")))

d.content("Ausbildungslücke", "Der Soll-Prozess hält im Lehrsaal; unter Belastung handeln die Teams anders als ausgebildet",
          "Quelle: Übungsauswertung " + PH("Jahr") + "; Beobachtung des Verfassers", form="concept:contrast",
          notes={"key": "Links der Plan, rechts die Realität; der Bruch ist die Lücke.", "time": 1.5},
          build=lambda s, h: h.contrast(s, {"head": "Soll-Prozess (Lehrsaal)", "items": ["Schritt für Schritt nach Vorschrift", "volle Information, keine Zeitnot", "Fehler werden nachbesprochen"]},
                                        {"head": "Stressrealität (Übung)", "items": ["Abkürzungen nach Erfahrung", "Lücken in Lage und Zeit", "Fehler bleiben unbemerkt"]}, hl="right"))

d.content("Lernschleife", "Sechs Stationen schließen den Kreis von der Übung zurück in die Ausbildung",
          "Quelle: Entwurf des Verfassers", form="concept:cycle",
          notes={"key": "Ein geschlossener Kreislauf, keine Liste; Auswertung ist der Hebel.", "time": 2.0},
          build=lambda s, h: h.cycle(s, ["Üben", "Beobachten", "Auswerten", "Anpassen", "Ausbilden", "Prüfen"], Z.x + Z.w / 2, Z.y + Z.h / 2 - 0.1, 1.9, hl=2))

def flow_with_gates(s, h):
    h.chevrons(s, [{"head": "Erfassen", "sub": "KI: Übungsdaten"}, {"head": "Auswerten", "sub": "KI: Muster"}, {"head": "Vorschlagen", "sub": "KI: Anpassung"}], Z.y + 0.4, 1.0, hl=1)
    h.box(s, Z.x, Z.y + 1.9, Z.w, 0.9, h.C["tint"], name="gate-bar")
    for i, c in enumerate(h.cols(4)):
        gate = ["Freigabe Daten", "Freigabe Deutung", "Freigabe Änderung", "Freigabe Lehrplan"][i]
        h.box(s, c.x + c.w / 2 - 0.2, Z.y + 1.65, 0.4, 0.4, h.C["signal"], name="gate-marker", shape=h._gate_shape())
        h.txt(s, gate, c.x, Z.y + 2.1, c.w, 0.6, size=h.F["small"], bold=True, align="center")
    h.label(s, "Durchgehende Leiste: vier menschliche Freigaben, keine davon automatisierbar", Z.x, Z.y + 3.1, Z.w)

from pptx.enum.shapes import MSO_SHAPE  # noqa: E402
TemplateDeck._gate_shape = lambda self: MSO_SHAPE.DIAMOND
d.content("Rolle der KI", "KI übernimmt drei Phasen der Schleife; vier menschliche Freigaben bleiben an festen Stellen",
          "Quelle: Entwurf des Verfassers", form="concept:linear-flow",
          notes={"key": "Drei KI-Phasen oben, vier Freigaben unten; die Leiste ist das Argument.", "time": 2.0}, build=flow_with_gates)

d.content("Optionen", "Nur die Lernschleife erfüllt Wirksamkeit, Aufwand und Akzeptanz zugleich",
          "Quelle: Einschätzung des Verfassers", form="table",
          notes={"key": "Drei Optionen, drei Kriterien; die Schleife ist die einzige mit drei Punkten.", "time": 1.5},
          build=lambda s, h: h.ltable(s, Z.x, Z.y, Z.w, [["Kriterium", "Lernschleife", "Lehrplan erweitern", "Externe Schulung"],
                                                          ["Wirksamkeit", "●", "◐", "◐"], ["Aufwand (keine Stellen)", "●", "●", "○"], ["Akzeptanz der Teams", "●", "○", "◐"]],
                                      [4.3, 2.7, 2.7, 2.63], row_h=0.8, hl=1, center=(1, 2, 3), size=16))

d.content("Beschluss", "Beschlussvorschlag: Die Leitungsrunde führt die Lernschleife ein und besetzt die vier Freigaben",
          "Quelle: Briefing", form="text",
          notes={"key": "Zwei Beschlusspunkte, dann Pause.", "time": 1.0},
          build=lambda s, h: [h.card(s, c.x, Z.y, c.w, 3.2, head, items, numbered=(i == 0))
                              for i, (c, head, items) in enumerate(zip(h.cols(3), ["Die Leitungsrunde beschließt", "Ohne Beschluss", "Heute nötig"],
                                                                        [["Einführung der Lernschleife", "Besetzung der vier Freigaben"], ["Lücke bleibt", "nächste Übung ohne Auswertung"], ["Beschluss zu 1 und 2", "Benennung der Freigabe-Inhaber"]]))])

r = d.write(out)
print({k: r[k] for k in ("path", "slides", "minutes", "words_per_slide", "forms_path")})
print("warnings", r["warnings"])
