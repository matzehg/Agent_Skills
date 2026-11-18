#!/usr/bin/env python3
"""deck-metrics.py: text budget and exhibit ratio for a finished deck.

Usage:
  python3 scripts/deck-metrics.py deck.pptx [--mode speaker|reading] [--skip 1,2,12] [--special 2,14] [--forms deck.forms.json]
  python3 scripts/deck-metrics.py path/to/slides/ [--mode speaker|reading] [--skip cover,close]   (Slides artifact type: one .html per slide, deck.json beside it)

--forms takes the approved form marks per slide (the <deck>.forms.json the
helpers write, or [{"slide": 3, "form": "concept:cycle"}, ...]) and compares
them with what the file contains: chart, table, concept (three or more shapes
or named concept parts), picture or text. A mismatch is gate T2 of
template-mode.md and reported as BLOCKER. Independently, a content slide whose
free text containers cover more than 60 % of the body zone and that carries no
exhibit is reported as text-block (gate T3).

--special names the management summary and the decision slide, which carry
text by design and get their own budget (exhibits.md section 6: up to 80 body
words speaker-led) and stay out of the mean. Without --special they are
detected by title start (Management Summary, Executive Summary,
Beschlussvorschlag, Proposed decision, Decision proposal) or by a tracker
or object named "ask-box".

--skip names the slides that are not content slides (title, section dividers,
closing) by number or id and overrides the default guess: for .pptx the guess
excludes layouts whose name contains TITLE, SECTION or COVER and treats every
other layout, including Blank, as content; for HTML it excludes ids starting
with cover, title, close, closing or section.

Reports, per slide: body words (title, tracker, source, slide number, labels
and notes excluded; symbol-only tokens such as marks are not words; both
placeholder forms are removed), whether an exhibit is present (chart, table,
picture that is not a full-slide background, or three or more shapes and
connectors), and the kind detected. Then: mean body words over content slides,
the exhibit ratio, and the slides over the budget of the mode
(references/exhibits.md section 6: speaker-led up to 40 body words,
reading-first 75 to 250). Heuristics, not judgement: a slide flagged here is
a slide to look at, not a verdict.
"""
import json, os, re, sys

BUDGET = {"speaker": (0, 40), "reading": (75, 250)}
SPECIAL_BUDGET = {"speaker": 80, "reading": 250}
SPECIAL_TITLES = ("management summary", "executive summary", "beschlussvorschlag", "proposed decision", "decision proposal", "entscheidungsvorschlag")
SKIP = set()
SPECIAL = set()
FORMS = {}
BODY_SHARE = 0.62   # body zone as a share of the slide: below the title band, above the footer band
TEXT_SHARE_LIMIT = 0.60
CONCEPT_NAMES = ("chevron", "cycle-node", "cycle-arrow", "timeline-marker", "timeline-axis", "matrix-cell", "continuum-marker", "stat-box", "node-", "contrast-head", "gate-", "pill", "box")

def form_class(mark):
    m = (mark or "").lower()
    if m.startswith("chart"): return "chart"
    if m.startswith("table"): return "table"
    if m.startswith("concept"): return "concept"
    if m.startswith(("picture", "image", "photo")): return "picture"
    return "text"

def words(text):
    text = re.sub(r"\[(PLATZHALTER|PLACEHOLDER):[^\]]*\]", "", text or "")
    # a token counts as a word only when it carries a letter or a digit;
    # marks (● ◐ ○ ✓ ✗), dashes and bullets are not words
    return len([w for w in re.split(r"\s+", text) if re.search(r"[0-9A-Za-zÀ-ÿ]", w)])

def html_slides(folder):
    order = None
    dj = os.path.join(os.path.dirname(folder.rstrip("/")), "deck.json")
    if os.path.exists(dj):
        try:
            order = json.load(open(dj)).get("order")
        except Exception:
            order = None
    files = [f for f in os.listdir(folder) if f.endswith(".html")]
    if order:
        files = [f"{sid}.html" for sid in order if f"{sid}.html" in files]
    else:
        files.sort()
    out = []
    for f in files:
        html = open(os.path.join(folder, f), encoding="utf-8").read()
        html = re.sub(r"<aside>.*?</aside>", "", html, flags=re.S)
        html = re.sub(r"<(style|script|noscript)[^>]*>.*?</\1>", "", html, flags=re.S | re.I)
        html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
        title = " ".join(re.findall(r"<h[12][^>]*>(.*?)</h[12]>", html, flags=re.S))
        # footer: the pinned bottom div
        footer = re.findall(r'<div style="position:absolute;left:[^"]*bottom:[^"]*"[^>]*>.*?</div>\s*</div>', html, flags=re.S)
        body_html = html
        for fo in footer:
            body_html = body_html.replace(fo, "")
        body_html = re.sub(r"<h[12][^>]*>.*?</h[12]>", "", body_html, flags=re.S)
        body_text = re.sub(r"<[^>]+>", " ", body_html)
        kinds = []
        if "<table" in html: kinds.append("table")
        if "<svg" in html: kinds.append("svg")
        if "x-shape" in html or "x-connector" in html: kinds.append("shapes")
        boxes = len(re.findall(r'<div style="[^"]*background:#', html))
        bw = words(body_text)
        if boxes >= 3:
            # boxes carrying labels are an exhibit; boxes carrying sentences are text cards
            kinds.append(f"{boxes} boxes" if bw <= 15 * boxes else f"{boxes} text cards")
        exhibit = any(k.split()[0] in ("table", "svg", "shapes") or k.endswith("boxes") for k in kinds)
        sid = f.replace(".html", "")
        is_content = (sid not in SKIP) if SKIP else not re.search(r'id="(cover|title|close|closing|section)', html)
        special = (sid in SPECIAL) or re.sub(r"<[^>]+>", " ", title).strip().lower().startswith(SPECIAL_TITLES)
        detected = "chart" if "chart" in kinds else "table" if "table" in kinds else "concept" if exhibit else "text"
        out.append({"slide": sid, "title_words": words(re.sub(r"<[^>]+>", " ", title)), "body_words": bw, "exhibit": exhibit, "kind": ", ".join(kinds) or "text", "is_content": is_content, "special": special, "text_share": None, "detected": detected})
    return out

def pptx_slides(path):
    try:
        from pptx import Presentation
        from pptx.util import Emu
    except ImportError:
        sys.exit("python-pptx is not installed: pip install python-pptx")
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    def walk(shapes):
        for sh in shapes:
            if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
                yield from walk(sh.shapes)
            else:
                yield sh
    prs = Presentation(path)
    slide_area = float(prs.slide_width) * float(prs.slide_height)
    out = []
    for i, sl in enumerate(prs.slides, 1):
        body, title_w, shapes, pictures, kinds, title_text, special = 0, 0, 0, 0, [], "", str(i) in SPECIAL
        text_area, concept_parts = 0.0, 0
        for sh in walk(sl.shapes):
            name = (sh.name or "").lower()
            if sh.is_placeholder and sh.placeholder_format.type is not None and "TITLE" in str(sh.placeholder_format.type):
                title_text = sh.text_frame.text if sh.has_text_frame else ""
                title_w += words(title_text)
                continue
            if name in ("source", "tracker", "label", "key-box", "key-text") or name.startswith("slide-number"):
                if name == "tracker" and sh.has_text_frame and sh.text_frame.text.strip().lower().startswith(SPECIAL_TITLES):
                    special = True
                continue
            if name == "ask-box":
                special = True
            if sh.has_chart if hasattr(sh, "has_chart") else False:
                kinds.append("chart")
                continue
            if sh.has_table if hasattr(sh, "has_table") else False:
                kinds.append("table")
                for r in sh.table.rows:
                    for c in r.cells:
                        body += words(c.text)
                continue
            if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
                area = float(sh.width or 0) * float(sh.height or 0)
                if area < 0.7 * slide_area:
                    pictures += 1
                continue
            text = sh.text_frame.text if sh.has_text_frame else ""
            is_concept_part = any(k in name for k in CONCEPT_NAMES)
            if text.strip():
                body += words(text)
                if is_concept_part:
                    shapes += 1; concept_parts += 1
                elif not sh.is_placeholder or True:
                    # a free text container (text box, card body, filled body placeholder)
                    text_area += float(sh.width or 0) * float(sh.height or 0)
            else:
                # a shape, line or connector without text is diagram geometry
                shapes += 1
                if is_concept_part: concept_parts += 1
                continue
            if "card" in name and not is_concept_part:
                shapes += 1
        if shapes >= 3: kinds.append(f"{shapes} shapes" if body <= 15 * shapes else f"{shapes} text cards")
        if pictures: kinds.append(f"{pictures} picture" + ("s" if pictures > 1 else ""))
        exhibit = any(k in ("chart", "table") or k.endswith("shapes") or "picture" in k for k in kinds)
        layout = (sl.slide_layout.name or "").upper()
        is_content = (str(i) not in SKIP) if SKIP else not any(k in layout for k in ("TITLE", "SECTION", "COVER"))
        if title_text.strip().lower().startswith(SPECIAL_TITLES): special = True
        if concept_parts >= 2 and shapes < 3: kinds.append(f"{concept_parts} concept parts")
        exhibit = exhibit or concept_parts >= 2
        share = text_area / (slide_area * BODY_SHARE) if slide_area else 0.0
        detected = "chart" if "chart" in kinds else "table" if "table" in kinds else "picture" if any("picture" in k for k in kinds) else "concept" if exhibit else "text"
        out.append({"slide": i, "title_words": title_w, "body_words": body, "exhibit": exhibit, "kind": ", ".join(dict.fromkeys(kinds)) or "text", "is_content": is_content, "special": special,
                    "text_share": round(min(share, 1.5), 2), "detected": detected})
    return out

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    target = sys.argv[1]
    mode = "speaker"
    if "--mode" in sys.argv:
        mode = sys.argv[sys.argv.index("--mode") + 1]
    global SKIP, SPECIAL
    SKIP = set()
    if "--skip" in sys.argv:
        SKIP = set(x.strip() for x in sys.argv[sys.argv.index("--skip") + 1].split(",") if x.strip())
    SPECIAL = set()
    if "--special" in sys.argv:
        SPECIAL = set(x.strip() for x in sys.argv[sys.argv.index("--special") + 1].split(",") if x.strip())
    global FORMS
    FORMS = {}
    if "--forms" in sys.argv:
        import json
        with open(sys.argv[sys.argv.index("--forms") + 1], encoding="utf-8") as f:
            FORMS = {str(e["slide"]): e.get("form", "") for e in json.load(f) if e.get("form")}
    lo, hi = BUDGET.get(mode, BUDGET["speaker"])
    sp = SPECIAL_BUDGET.get(mode, SPECIAL_BUDGET["speaker"])
    rows = pptx_slides(target) if target.lower().endswith(".pptx") else html_slides(target)
    content = [r for r in rows if r["is_content"] and not r["special"]]
    specials = [r for r in rows if r["is_content"] and r["special"]]
    title_limit = 20
    mismatches, textblocks = [], []
    print(f"{'slide':<10}{'title':>6}{'body':>6}  exhibit")
    for r in rows:
        flag = ""
        if r["is_content"] and r["special"]:
            flag = "  (special budget %d)" % sp + ("  <- over budget" if r["body_words"] > sp else "")
        elif r["is_content"] and (r["body_words"] > hi or (lo and r["body_words"] < lo)):
            flag = "  <- over budget" if r["body_words"] > hi else "  <- under budget"
        if r["title_words"] > title_limit:
            flag += "  <- title over %d words" % title_limit
        approved = FORMS.get(str(r["slide"]))
        if approved:
            want = form_class(approved)
            if want != r["detected"] and not (want == "text" and r["detected"] != "text"):
                flag += f"  <- BLOCKER form mismatch: approved {approved}, built {r['detected']}"
                mismatches.append(str(r["slide"]))
            else:
                flag += f"  (form ok: {approved})"
        if r["is_content"] and r.get("text_share") is not None and r["text_share"] > TEXT_SHARE_LIMIT and not r["exhibit"] and not r["special"]:
            flag += f"  <- text-block: free text covers {r['text_share']:.0%} of the body zone, no exhibit"
            textblocks.append(str(r["slide"]))
        print(f"{str(r['slide']):<10}{r['title_words']:>6}{r['body_words']:>6}  {r['kind']}{flag}")
    if content:
        mean = sum(r["body_words"] for r in content) / len(content)
        allc = content + specials
        ratio = sum(1 for r in allc if r["exhibit"]) / len(allc)
        over = [str(r["slide"]) for r in content if r["body_words"] > hi] + [str(r["slide"]) for r in specials if r["body_words"] > sp]
        print(f"\nmode: {mode} (budget {lo}-{hi} body words; special {sp}) | content slides: {len(allc)} ({len(specials)} special, out of the mean) | mean body words: {mean:.0f} | exhibit ratio: {ratio:.0%} | over budget: {', '.join(over) or 'none'}")
        if FORMS:
            checked = [r for r in rows if str(r["slide"]) in FORMS]
            print(f"form check (gate T2): {len(checked) - len(mismatches)} of {len(checked)} slides match their approved form | mismatches: {', '.join(mismatches) or 'none'}")
        if textblocks:
            print(f"text-block slides (gate T3): {', '.join(textblocks)}")

if __name__ == "__main__":
    main()
