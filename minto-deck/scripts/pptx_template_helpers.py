"""pptx_template_helpers.py — build a deck on a corporate template with native shapes.

Same contract as pptx-helpers.js, for the template path (template-mode.md):
the template supplies master, theme, fonts, chrome and the three layouts; the
helpers draw every exhibit as editable shapes in the free body zone and never
fill a body placeholder. Needs python-pptx (pip install python-pptx).

    from pptx_template_helpers import TemplateDeck
    d = TemplateDeck("template.pptx", probe="probe.json", mode="speaker", lang="de")
    d.title_slide("Title", ["Subtitle", d.PH("date")], notes={...})
    d.content("Tracker", "Action title as a sentence", "Source: …", notes={...},
              build=lambda s, h: h.chevrons(s, [...], h.Z.y + 0.8, 1.0, hl=2),
              form="concept:linear-flow")
    r = d.write("out.pptx")   # dict: slides, minutes, words_per_slide, warnings, forms, forms_path

probe is the JSON written by template-probe.py (--json) or an equivalent dict.
The layouts and colour roles come from the probe's "recommended" and "roles"
blocks; both can be overridden with layouts={...} and roles={...} after the
user has confirmed the template brief. Fonts are never set: text inherits the
template's theme fonts. Every exhibit part carries the same shape names as the
JS helpers (chevron, cycle-node, card, node-*, text, label, tracker, source,
ask-box), so deck-metrics.py reads both paths alike. content(..., form=...)
records the approved form mark per slide; write() stores them beside the deck
as <deck>.forms.json for deck-metrics.py --forms (gate T2).
"""
import copy
import json
import math
import re

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR, PP_PLACEHOLDER
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt, Emu

EMU = 914400.0
PH_RE = re.compile(r"\[(PLATZHALTER|PLACEHOLDER):[^\]]*\]")
TITLE_TYPES = (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE)
CHROME_TYPES = (PP_PLACEHOLDER.DATE, PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.SLIDE_NUMBER)
SIZES = {"speaker": {"body": 16, "small": 12, "tbl": 14, "stat": 44, "head": 18},
         "handout": {"body": 14, "small": 12, "tbl": 12, "stat": 36, "head": 16}}
LABELS = {"de": {"key": "Kernpunkt", "open": "Einstieg", "track": "Sprechverlauf", "point": "Zeigen auf", "trans": "Überleitung", "time": "Zeit", "watch": "Achtung", "source": "Quelle"},
          "en": {"key": "Key point", "open": "Opening", "track": "Track", "point": "Point at", "trans": "Transition", "time": "Time", "watch": "Watch", "source": "Source"}}


def words_of(text):
    """Body words: both placeholder forms removed, symbol-only tokens (marks) not counted."""
    if isinstance(text, (list, tuple)):
        text = " ".join(t if isinstance(t, str) else str(t.get("text", "")) for t in text)
    text = PH_RE.sub("", str(text or ""))
    return len([w for w in re.split(r"\s+", text) if re.search(r"[0-9A-Za-zÀ-ÿ]", w)])


def longest_word_width(text, font_size):
    """Inches the longest token needs on one line (0.45 em average plus cell margins); a signal, not a measure."""
    joined = PH_RE.sub(lambda m: m.group(0).replace(" ", "_"), str(text or ""))
    longest = max((len(t) for t in joined.split()), default=0)
    return longest * font_size * 0.45 / 72 + 0.2


def _rgb(hexstr):
    return RGBColor.from_string(str(hexstr).replace("#", "").upper())


class Zone:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h


class TemplateDeck:
    def __init__(self, template, probe=None, mode="speaker", lang="de", layouts=None, roles=None, gutter=0.25):
        self.prs = Presentation(template)
        self.mode = "handout" if mode == "handout" else "speaker"
        self.lang = "en" if lang == "en" else "de"
        self.L = LABELS[self.lang]
        self.F = SIZES[self.mode]
        self.G = gutter
        if isinstance(probe, str):
            with open(probe, encoding="utf-8") as f:
                probe = json.load(f)
        probe = probe or {}
        rec = probe.get("recommended", {})
        lay = dict(cover=rec.get("cover"), section=rec.get("section"), content=rec.get("content"))
        lay.update(layouts or {})
        self.layouts = {k: self._layout(v) for k, v in lay.items()}
        if self.layouts["content"] is None:
            raise ValueError("no content layout: pass layouts={'content': '<layout name>'} from the template brief")
        pr = probe.get("roles", {})
        pal = probe.get("theme", {}).get("colors", {})
        self.C = {
            "message": pr.get("message", {}).get("hex") or pal.get("accent1", "1F4E79"),
            "signal": pr.get("signal", {}).get("hex") or pal.get("accent2", "C0504D"),
            "neutral": pr.get("neutral", {}).get("hex") or pal.get("dk2", "44546A"),
            "muted": pr.get("muted", {}).get("hex") or pal.get("accent6", "7F7F7F"),
            "text": pr.get("text", {}).get("hex") or pal.get("dk1", "000000"),
            "background": pr.get("background", {}).get("hex") or pal.get("lt1", "FFFFFF"),
            "tint": pr.get("tint", {}).get("hex") or pal.get("lt2", "F2F2F2"),
        }
        self.C.update(roles or {})
        z = rec.get("body_zone") or {}
        sw, sh = self.prs.slide_width / EMU, self.prs.slide_height / EMU
        self.W, self.H = sw, sh
        self.Z = Zone(z.get("x", 0.5), z.get("y", 1.6), z.get("w", sw - 1.0), z.get("h", sh - 2.4))
        self.tracker_left = bool(z.get("top_right_chrome"))
        self._drop_all_slides()
        self.notes_log, self.words_per_slide, self.warnings, self.forms = [], [], [], []

    # ---------- template plumbing ----------
    def _layout(self, name):
        if not name:
            return None
        for m in self.prs.slide_masters:
            for l in m.slide_layouts:
                if l.name == name:
                    return l
        raise ValueError(f"layout {name!r} not in template")

    def _drop_all_slides(self):
        lst = self.prs.slides._sldIdLst
        for sld in list(lst):
            self.prs.part.drop_rel(sld.rId)
            lst.remove(sld)

    def _new_slide(self, layout):
        s = self.prs.slides.add_slide(layout)
        # T1: body placeholders are deleted, never filled; only the title stays
        for ph in list(s.placeholders):
            if ph.placeholder_format.type not in TITLE_TYPES:
                ph._element.getparent().remove(ph._element)
        # python-pptx does not clone date, footer and slide-number placeholders, and a
        # slide number field only renders when the field sits on the slide: copy the
        # layout's chrome placeholders (by type, or by their place in the footer band)
        for ph in layout.placeholders:
            t = ph.placeholder_format.type
            footer_band = ph.top / EMU > self.H * 0.85 and ph.height / EMU < 0.6
            if t in CHROME_TYPES or (footer_band and t not in TITLE_TYPES):
                s.shapes._spTree.append(copy.deepcopy(ph._element))
        return s

    def _set_title(self, s, text):
        for ph in s.placeholders:
            if ph.placeholder_format.type in TITLE_TYPES:
                ph.text_frame.text = text
                return ph
        return None

    def _notes(self, s, n, title):
        if not n:
            return
        L, lines = self.L, []
        if n.get("key"): lines.append(f"{L['key']}: {n['key']}")
        if n.get("open"): lines.append(f"{L['open']}: {n['open']}")
        for t in n.get("track", []): lines.append(f"- {t}")
        if n.get("point"): lines.append(f"{L['point']}: {n['point']}")
        if n.get("trans"): lines.append(f"{L['trans']}: {n['trans']}")
        if n.get("time") is not None: lines.append(f"{L['time']}: {str(n['time']).replace('.', ',') if self.lang == 'de' else n['time']} min")
        if n.get("watch"): lines.append(f"{L['watch']}: {n['watch']}")
        s.notes_slide.notes_text_frame.text = "\n".join(lines)
        self.notes_log.append({"title": title, "time": float(n.get("time") or 0)})

    # ---------- slide kinds ----------
    def title_slide(self, title, sub_lines=None, notes=None):
        s = self._new_slide(self.layouts["cover"] or self.layouts["content"])
        self._set_title(s, title)
        if sub_lines:
            self.txt(s, "\n".join(sub_lines), self.Z.x, self.H * 0.55, self.Z.w, 1.2, size=self.F["head"], color=self.C["background"] if self.layouts["cover"] else self.C["text"], name="subtitle")
        self._notes(s, notes, title)
        self.words_per_slide.append(0)
        return s

    def section_slide(self, title, notes=None):
        s = self._new_slide(self.layouts["section"] or self.layouts["content"])
        self._set_title(s, title)
        self._notes(s, notes, title)
        self.words_per_slide.append(0)
        return s

    def content(self, tracker, title, source, notes=None, build=None, form=None):
        s = self._new_slide(self.layouts["content"])
        self._set_title(s, title)
        z = self.Z
        # the last 0.35 in of the body zone carry source (left) and tracker (right);
        # exhibits stay above z.y + z.h - 0.4
        self.txt(s, source, z.x, z.y + z.h - 0.3, z.w - 3.2, 0.3, size=9, color=self.C["muted"], name="source")
        self.txt(s, tracker, z.x + z.w - 3.0, z.y + z.h - 0.3, 3.0, 0.3, size=9, color=self.C["muted"], align="right", name="tracker", caps=True)
        before = len(s.shapes)
        if build:
            build(s, self)
        self.words_per_slide.append(self._count_words(s))
        self.forms.append({"slide": len(self.prs.slides), "form": form or "", "title": title})
        self._notes(s, notes, title)
        return s

    def _count_words(self, s):
        n = 0
        for sh in s.shapes:
            name = (sh.name or "").lower()
            if sh.is_placeholder and sh.placeholder_format.type in TITLE_TYPES:
                continue
            if name in ("tracker", "source", "label", "key-box", "key-text") or sh.is_placeholder:
                continue
            if sh.has_table:
                for r in sh.table.rows:
                    for c in r.cells:
                        n += words_of(c.text)
            elif sh.has_text_frame:
                n += words_of(sh.text_frame.text)
        return n

    # ---------- primitives ----------
    def PH(self, what):
        return f"[PLACEHOLDER: {what}]" if self.lang == "en" else f"[PLATZHALTER: {what}]"

    def cols(self, n, g=None):
        g = self.G if g is None else g
        w = (self.Z.w - (n - 1) * g) / n
        return [Zone(self.Z.x + i * (w + g), None, w, None) for i in range(n)]

    def box(self, s, x, y, w, h, fill, name="box", shape=MSO_SHAPE.RECTANGLE, line=None):
        sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
        sh.name = name
        sh.fill.solid(); sh.fill.fore_color.rgb = _rgb(fill)
        if line:
            sh.line.color.rgb = _rgb(line); sh.line.width = Pt(0.75)
        else:
            sh.line.fill.background()
        sh.shadow.inherit = False
        sh.text_frame.text = ""
        return sh

    def txt(self, s, text, x, y, w, h, size=None, bold=False, color=None, align="left", valign="top", name="text", caps=False, italic=False):
        tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        tb.name = name
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.05); tf.margin_top = tf.margin_bottom = Inches(0.03)
        tf.vertical_anchor = {"top": MSO_ANCHOR.TOP, "middle": MSO_ANCHOR.MIDDLE, "bottom": MSO_ANCHOR.BOTTOM}[valign]
        runs = text if isinstance(text, list) else [{"text": str(text)}]
        al = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT}[align]
        p = tf.paragraphs[0]; p.alignment = al
        for r in runs:
            r = {"text": r} if isinstance(r, str) else r
            parts = str(r["text"]).split("\n")
            for i, part in enumerate(parts):
                if i > 0:
                    p = tf.add_paragraph(); p.alignment = al
                run = p.add_run(); run.text = part.upper() if caps else part
                f = run.font
                f.size = Pt(r.get("size", size or self.F["body"]))
                f.bold = r.get("bold", bold); f.italic = r.get("italic", italic)
                f.color.rgb = _rgb(r.get("color", color or self.C["text"]))
        return tb

    def label(self, s, text, x, y, w, h=0.3):
        return self.txt(s, text, x, y, w, h, size=self.F["small"], color=self.C["muted"], name="label")

    def line(self, s, x1, y1, x2, y2, color=None, width=1.5, arrow=False, name="line"):
        c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
        c.name = name
        c.line.color.rgb = _rgb(color or self.C["muted"]); c.line.width = Pt(width)
        if arrow:
            ln = c.line._get_or_add_ln()
            tail = ln.makeelement(qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"})
            ln.append(tail)
        return c

    def bullets(self, s, items, x, y, w, h, size=None, gap=8, numbered=False, color=None, name="text"):
        tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        tb.name = name
        tf = tb.text_frame; tf.word_wrap = True
        for i, item in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            run = p.add_run(); run.text = item
            run.font.size = Pt(size or self.F["body"]); run.font.color.rgb = _rgb(color or self.C["text"])
            p.space_after = Pt(gap)
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(int(Inches(0.25)))); pPr.set("indent", str(-int(Inches(0.25))))
            for old in pPr.findall(qn("a:buNone")) + pPr.findall(qn("a:buChar")) + pPr.findall(qn("a:buAutoNum")):
                pPr.remove(old)
            if numbered:
                pPr.append(pPr.makeelement(qn("a:buAutoNum"), {"type": "arabicPeriod"}))
            else:
                pPr.append(pPr.makeelement(qn("a:buChar"), {"char": "•"}))
        return tb

    def card(self, s, x, y, w, h, head, items, fill=None, numbered=False):
        self.box(s, x, y, w, h, fill or self.C["tint"], name="card")
        self.txt(s, head, x + 0.25, y + 0.2, w - 0.5, 0.5, size=self.F["head"], bold=True, name="card-head")
        self.bullets(s, items, x + 0.25, y + 0.85, w - 0.5, h - 1.05, numbered=numbered, name="card-body")

    def _cell_border(self, cell, side, color, width_pt):
        tcPr = cell._tc.get_or_add_tcPr()
        for old in tcPr.findall(qn(f"a:{side}")):
            tcPr.remove(old)
        ln = tcPr.makeelement(qn(f"a:{side}"), {"w": str(int(width_pt * 12700)), "cap": "flat", "cmpd": "sng", "algn": "ctr"})
        fill = ln.makeelement(qn("a:solidFill"), {}); clr = fill.makeelement(qn("a:srgbClr"), {"val": color}); fill.append(clr); ln.append(fill)
        tcPr.append(ln)

    def _cell_nofill(self, cell):
        tcPr = cell._tc.get_or_add_tcPr()
        for old in tcPr.findall(qn("a:solidFill")) + tcPr.findall(qn("a:noFill")):
            tcPr.remove(old)
        tcPr.append(tcPr.makeelement(qn("a:noFill"), {}))

    def ltable(self, s, x, y, w, rows, col_w, row_h=0.6, size=None, hl=None, right=(), center=()):
        """List-style table: header bold with a rule below, hairlines between rows, no vertical lines, no banding."""
        size = size or self.F["tbl"]
        slide_no = len(self.prs.slides)
        for ri, r in enumerate(rows):
            for ci, cell in enumerate(r):
                text = cell.get("text") if isinstance(cell, dict) else cell
                need = longest_word_width(text, size - 1 if ri == 0 else size)
                if ci < len(col_w) and need > col_w[ci] and not any(wn["slide"] == slide_no and wn["column"] == ci for wn in self.warnings):
                    self.warnings.append({"slide": slide_no, "kind": "narrow-column", "column": ci, "width": col_w[ci], "needs": round(need, 2), "text": str(text)[:40]})
        shape = s.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y), Inches(w), Inches(row_h * len(rows)))
        shape.name = "ltable"
        tbl = shape.table
        tblPr = tbl._tbl.tblPr
        for attr in ("firstRow", "bandRow"):
            tblPr.set(attr, "0")
        for ci, cw in enumerate(col_w):
            tbl.columns[ci].width = Inches(cw)
        for ri, r in enumerate(rows):
            tbl.rows[ri].height = Inches(row_h)
            for ci, cell in enumerate(r):
                spec = cell if isinstance(cell, dict) else {"text": cell}
                c = tbl.cell(ri, ci)
                self._cell_nofill(c)
                if hl is not None and ci == hl:
                    c.fill.solid(); c.fill.fore_color.rgb = _rgb(self.C["tint"])
                c.margin_left = c.margin_right = Inches(0.08); c.margin_top = c.margin_bottom = Inches(0.04)
                c.vertical_anchor = MSO_ANCHOR.MIDDLE
                tf = c.text_frame; tf.word_wrap = True
                p = tf.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT if ci in right else (PP_ALIGN.CENTER if ci in center else PP_ALIGN.LEFT)
                run = p.add_run(); run.text = str(spec.get("text", ""))
                run.font.size = Pt(size - 1 if ri == 0 else size)
                run.font.bold = bool(spec.get("bold", ri == 0))
                run.font.color.rgb = _rgb(spec.get("color", self.C["text"]))
                for side in ("lnL", "lnR"):
                    self._cell_border(c, side, self.C["background"], 0)
                self._cell_border(c, "lnT", self.C["text"] if ri == 1 else self.C["background"], 1.0 if ri == 1 else 0)
                self._cell_border(c, "lnB", self.C["muted"] if 0 < ri < len(rows) - 1 else self.C["background"], 0.5 if 0 < ri < len(rows) - 1 else 0)
        return shape

    def chevrons(self, s, items, y, h=1.0, hl=None):
        """Linear flow. items: [{head, sub?}, ...]; the left notch is h/2 deep, text starts behind it."""
        inset = h / 2 + 0.1
        has_sub = any(isinstance(it, dict) and it.get("sub") for it in items)
        for i, c in enumerate(self.cols(len(items))):
            it = items[i] if isinstance(items[i], dict) else {"head": items[i]}
            self.box(s, c.x, y, c.w, h, self.C["message"] if i == hl else self.C["neutral"], name="chevron", shape=MSO_SHAPE.CHEVRON)
            tw = max(0.5, c.w - inset - 0.25)
            if has_sub:
                self.txt(s, it["head"], c.x + inset, y + 0.08, tw, h * 0.5, size=self.F["body"], bold=True, color=self.C["background"], valign="bottom")
                if it.get("sub"):
                    self.txt(s, it["sub"], c.x + inset, y + h * 0.56, tw, h * 0.4, size=self.F["small"], color=self.C["tint"])
            else:
                self.txt(s, it["head"], c.x + inset, y, tw, h, size=self.F["body"], bold=True, color=self.C["background"], valign="middle")

    def cycle(self, s, items, cx, cy, r, node_w=1.5, node_h=0.7, hl=None):
        """Closed loop: nodes on a circle, arrows along the chords, clockwise from the top."""
        n = len(items)
        pos = []
        for i in range(n):
            a = -math.pi / 2 + 2 * math.pi * i / n
            pos.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        def edge(dx, dy):
            # distance from a node centre to its box edge along (dx, dy), plus a gap
            d = math.hypot(dx, dy) or 1
            ux, uy = dx / d, dy / d
            tx = (node_w / 2) / abs(ux) if ux else float("inf")
            ty = (node_h / 2) / abs(uy) if uy else float("inf")
            return min(tx, ty) + 0.08
        for i in range(n):
            (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % n]
            dx, dy = x2 - x1, y2 - y1
            d = math.hypot(dx, dy) or 1
            o1, o2 = edge(dx, dy), edge(-dx, -dy)
            if d - o1 - o2 < 0.25:
                self.warnings.append({"slide": len(self.prs.slides), "kind": "cycle-arrow-short", "between": [items[i], items[(i + 1) % n]], "length": round(d - o1 - o2, 2)})
            self.line(s, x1 + dx / d * o1, y1 + dy / d * o1, x2 - dx / d * o2, y2 - dy / d * o2, arrow=True, name="cycle-arrow")
        for i, (x, y) in enumerate(pos):
            self.box(s, x - node_w / 2, y - node_h / 2, node_w, node_h, self.C["message"] if i == hl else self.C["neutral"], name="cycle-node", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
            self.txt(s, items[i], x - node_w / 2 + 0.05, y - node_h / 2, node_w - 0.1, node_h, size=self.F["small"] + 1, bold=True, color=self.C["background"], align="center", valign="middle")

    def contrast(self, s, left, right, y=None, h=None, hl="right"):
        """Two states side by side: {head, items}; the highlighted side carries the message colour."""
        y = self.Z.y if y is None else y
        h = self.Z.h - 0.6 if h is None else h
        c = self.cols(2, g=0.6)
        for i, (col, side) in enumerate(zip(c, (left, right))):
            on = (hl == "left" and i == 0) or (hl == "right" and i == 1)
            self.box(s, col.x, y, col.w, 0.6, self.C["message"] if on else self.C["neutral"], name="contrast-head")
            self.txt(s, side["head"], col.x + 0.2, y, col.w - 0.4, 0.6, size=self.F["head"], bold=True, color=self.C["background"], valign="middle")
            self.box(s, col.x, y + 0.6, col.w, h - 0.6, self.C["tint"], name="contrast-body")
            self.bullets(s, side["items"], col.x + 0.25, y + 0.85, col.w - 0.5, h - 1.0, gap=10)

    def timeline(self, s, events, y, hl=None):
        n = len(events)
        x0, x1 = self.Z.x + 0.5, self.Z.x + self.Z.w - 0.5
        self.line(s, x0, y, x1, y, color=self.C["muted"], width=1.5, name="timeline-axis")
        for i, e in enumerate(events):
            x = x0 + (x1 - x0) * (i / (n - 1) if n > 1 else 0.5)
            self.box(s, x - 0.11, y - 0.11, 0.22, 0.22, self.C["message"] if i == hl else self.C["neutral"], name="timeline-marker", shape=MSO_SHAPE.OVAL)
            self.txt(s, e["date"], x - 1.2, y - 0.6, 2.4, 0.35, size=self.F["small"], bold=True, align="center", name="timeline-date")
            self.txt(s, e["label"], x - 1.2, y + 0.2 + (0.5 if i % 2 else 0), 2.4, 0.8, size=self.F["small"], color=self.C["message"] if i == hl else self.C["text"], align="center")

    def big_stat(self, s, value, label, x, y, w, color=None):
        self.box(s, x, y, w, 1.6, self.C["tint"], name="stat-box")
        self.txt(s, value, x + 0.2, y + 0.1, w - 0.4, 0.9, size=self.F["stat"], bold=True, color=color or self.C["message"], name="stat-value")
        self.txt(s, label, x + 0.2, y + 1.0, w - 0.4, 0.5, size=self.F["small"], color=self.C["muted"], name="stat-label")

    # ---------- output ----------
    def write(self, path):
        self.prs.save(path)
        forms_path = re.sub(r"\.pptx$", "", path) + ".forms.json"
        with open(forms_path, "w", encoding="utf-8") as f:
            json.dump(self.forms, f, indent=1, ensure_ascii=False)
        return {"path": path, "slides": len(self.prs.slides), "minutes": round(sum(n["time"] for n in self.notes_log), 1),
                "words_per_slide": self.words_per_slide, "warnings": self.warnings, "forms": self.forms, "forms_path": forms_path}
