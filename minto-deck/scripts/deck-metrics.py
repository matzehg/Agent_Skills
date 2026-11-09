#!/usr/bin/env python3
"""deck-metrics.py: text budget and exhibit ratio for a finished deck.

Usage:
  python3 scripts/deck-metrics.py deck.pptx [--mode speaker|reading]
  python3 scripts/deck-metrics.py path/to/slides/ [--mode speaker|reading]   (Slides artifact type: one .html per slide, deck.json beside it)

Reports, per slide: body words (title, tracker, source, slide number and notes
excluded), whether an exhibit is present (chart, table, or three or more
shapes), and the kind detected. Then: mean body words over content slides,
the exhibit ratio, and the slides over the budget of the mode
(references/exhibits.md section 6: speaker-led up to 40 body words,
reading-first 75 to 250). Heuristics, not judgement: a slide flagged here is
a slide to look at, not a verdict.
"""
import json, os, re, sys

BUDGET = {"speaker": (0, 40), "reading": (75, 250)}

def words(text):
    text = re.sub(r"\[PLATZHALTER:[^\]]*\]", "", text or "")
    return len([w for w in re.split(r"\s+", text) if w.strip()])

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
        out.append({"slide": f.replace(".html", ""), "title_words": words(re.sub(r"<[^>]+>", " ", title)), "body_words": bw, "exhibit": exhibit, "kind": ", ".join(kinds) or "text", "is_content": not re.search(r'id="(cover|title|close|closing|section)', html)})
    return out

def pptx_slides(path):
    try:
        from pptx import Presentation
        from pptx.util import Emu
    except ImportError:
        sys.exit("python-pptx is not installed: pip install python-pptx")
    prs = Presentation(path)
    out = []
    for i, sl in enumerate(prs.slides, 1):
        body, title_w, shapes, kinds = 0, 0, 0, []
        for sh in sl.shapes:
            name = (sh.name or "").lower()
            if sh.is_placeholder and sh.placeholder_format.type is not None and "TITLE" in str(sh.placeholder_format.type):
                title_w += words(sh.text_frame.text if sh.has_text_frame else "")
                continue
            if name in ("source", "tracker") or name.startswith("slide-number"):
                continue
            if sh.has_chart if hasattr(sh, "has_chart") else False:
                kinds.append("chart")
            if sh.has_table if hasattr(sh, "has_table") else False:
                kinds.append("table")
                for r in sh.table.rows:
                    for c in r.cells:
                        body += words(c.text)
                continue
            if sh.has_text_frame:
                body += words(sh.text_frame.text)
            if sh.shape_type is not None and not sh.has_text_frame:
                shapes += 1
            if any(k in name for k in ("chevron", "cycle-node", "timeline-marker", "matrix-cell", "continuum-marker", "stat-box")):
                shapes += 1
        if shapes >= 3: kinds.append(f"{shapes} shapes" if body <= 15 * shapes else f"{shapes} text cards")
        exhibit = any(k in ("chart", "table") or k.endswith("shapes") for k in kinds)
        layout = (sl.slide_layout.name or "").upper()
        out.append({"slide": i, "title_words": title_w, "body_words": body, "exhibit": exhibit, "kind": ", ".join(dict.fromkeys(kinds)) or "text", "is_content": "CONTENT" in layout or layout == ""})
    return out

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    target = sys.argv[1]
    mode = "speaker"
    if "--mode" in sys.argv:
        mode = sys.argv[sys.argv.index("--mode") + 1]
    lo, hi = BUDGET.get(mode, BUDGET["speaker"])
    rows = pptx_slides(target) if target.lower().endswith(".pptx") else html_slides(target)
    content = [r for r in rows if r["is_content"]]
    print(f"{'slide':<10}{'title':>6}{'body':>6}  exhibit")
    for r in rows:
        flag = ""
        if r["is_content"] and (r["body_words"] > hi or (lo and r["body_words"] < lo)):
            flag = "  <- over budget" if r["body_words"] > hi else "  <- under budget"
        print(f"{str(r['slide']):<10}{r['title_words']:>6}{r['body_words']:>6}  {r['kind']}{flag}")
    if content:
        mean = sum(r["body_words"] for r in content) / len(content)
        ratio = sum(1 for r in content if r["exhibit"]) / len(content)
        over = [str(r["slide"]) for r in content if r["body_words"] > hi]
        print(f"\nmode: {mode} (budget {lo}-{hi} body words) | content slides: {len(content)} | mean body words: {mean:.0f} | exhibit ratio: {ratio:.0%} | over budget: {', '.join(over) or 'none'}")

if __name__ == "__main__":
    main()
