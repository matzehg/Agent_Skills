#!/usr/bin/env python3
"""template-probe.py — inventory a corporate template and draft the template brief.

  python3 scripts/template-probe.py template.pptx|template.potx [--json out.json] [--md out.md]

Reads slide size, every layout with its placeholders (type, index, position),
the chrome each layout carries (logo, lines, footer text), the theme palette
(dk1 … accent6) and the theme fonts. From that it proposes the three layouts
the template path needs (cover, section, content base) and the free body zone
on the content layout, and drafts the colour-role mapping (message, signal,
neutral) for the Stage 0 template brief. Everything proposed is marked
"confirm"; the user settles it once and keeps the answer in a private
companion skill (template-mode.md section 5).

Needs python-pptx. Output: a Markdown brief on stdout (or --md) and a JSON
file the Python helpers read (--json). Nothing in the template is changed.
"""
import json
import re
import sys
import zipfile

try:
    from pptx import Presentation
    from pptx.enum.shapes import PP_PLACEHOLDER, MSO_SHAPE_TYPE
except ImportError:
    sys.exit("python-pptx is required: pip install python-pptx")

EMU = 914400.0
CHROME_PH = {PP_PLACEHOLDER.SLIDE_NUMBER, PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.DATE}
COVER_WORDS = ("title slide", "cover", "deckblatt", "titelfolie", "fläche titel", "titelseite")
COVER_EXCLUDE = ("inhalt", "content", "und")
SECTION_WORDS = ("section", "kapitel", "trenner", "divider", "abschnitt", "zwischentitel", "zwischenüberschrift", "zwischenueberschrift")
CONTENT_WORDS = ("title only", "nur titel", "grafik", "chart", "diagramm", "blank with title", "leer mit titel", "1sp", "content", "inhalt")


def inches(v):
    return round((v or 0) / EMU, 2)


def ph_kind(ph):
    t = ph.placeholder_format.type
    return str(t).split(".")[-1].split(" ")[0] if t is not None else "NONE"


def layout_info(layout, slide_w, slide_h):
    phs, chrome = [], []
    for sh in layout.shapes:
        if sh.is_placeholder:
            k = ph_kind(sh)
            phs.append({"idx": sh.placeholder_format.idx, "type": k, "name": sh.name,
                        "x": inches(sh.left), "y": inches(sh.top), "w": inches(sh.width), "h": inches(sh.height)})
        else:
            kind = "picture" if sh.shape_type == MSO_SHAPE_TYPE.PICTURE else ("line" if sh.shape_type == MSO_SHAPE_TYPE.LINE else "shape")
            text = sh.text_frame.text.strip() if sh.has_text_frame else ""
            chrome.append({"name": sh.name, "kind": kind, "text": text[:40],
                           "x": inches(sh.left), "y": inches(sh.top), "w": inches(sh.width), "h": inches(sh.height)})
    titles = [p for p in phs if p["type"] in ("TITLE", "CENTER_TITLE")]
    bodies = [p for p in phs if p["type"] in ("BODY", "OBJECT", "SUBTITLE", "CHART", "TABLE", "PICTURE", "MEDIA")]
    # chrome placeholders by type or by name (templates built by tools often write them as OBJECT)
    chrome_phs = [p for p in phs if p["type"] in ("SLIDE_NUMBER", "FOOTER", "DATE")
                  or re.search(r"slide.?number|foliennummer|footer|fu[sß]zeile|date|datum", p["name"], re.I)
                  or (p["y"] > slide_h * 0.85 and p["h"] < 0.6)]  # small placeholder in the footer band
    bodies = [b for b in bodies if b not in chrome_phs]
    name = layout.name or ""
    low = name.lower()
    role = None
    is_cover_name = (any(w in low for w in COVER_WORDS) or re.search(r"\btitel\b", low)) and not any(w in low for w in COVER_EXCLUDE)
    if is_cover_name or any(p["type"] == "CENTER_TITLE" for p in phs) or any(p["type"] == "SUBTITLE" for p in phs):
        role = "cover"
    elif any(w in low for w in SECTION_WORDS):
        role = "section"
    elif titles and not bodies:
        role = "content-base"
    elif titles and bodies:
        role = "content-with-body-placeholders"
    elif not titles and not bodies:
        role = "blank"
    # free body zone on a content-base layout: below the title, above the lowest chrome element
    zone = None
    if titles:
        t = titles[0]
        top = t["y"] + t["h"] + 0.2
        low_chrome = [c for c in chrome + chrome_phs if c["y"] > slide_h * 0.75]
        bottom = min([c["y"] for c in low_chrome], default=slide_h - 0.4) - 0.2
        right_chrome = [c for c in chrome if c["y"] < top and c["x"] > slide_w * 0.7]
        zone = {"x": round(t["x"], 2), "y": round(top, 2), "w": round(slide_w - 2 * t["x"], 2), "h": round(bottom - top, 2),
                "title": t, "top_right_chrome": bool(right_chrome)}
    return {"name": name, "role": role, "placeholders": phs, "body_placeholders": bodies, "chrome": chrome, "body_zone": zone}


def theme_info(path):
    z = zipfile.ZipFile(path)
    names = [n for n in z.namelist() if re.match(r"ppt/theme/theme\d+\.xml", n)]
    out = {"colors": {}, "fonts": {}}
    if not names:
        return out
    t = z.read(sorted(names)[0]).decode("utf-8", "ignore")
    for slot in ("dk1", "lt1", "dk2", "lt2", "accent1", "accent2", "accent3", "accent4", "accent5", "accent6"):
        m = re.search(r"<a:%s>.*?(?:val|lastClr)=\"([0-9A-Fa-f]{6})\"" % slot, t, re.S)
        if m:
            out["colors"][slot] = m.group(1).upper()
    fonts = re.findall(r"<a:(major|minor)Font>.*?<a:latin typeface=\"([^\"]*)\"", t, re.S)
    for which, face in fonts:
        out["fonts"]["heading" if which == "major" else "body"] = face
    m = re.search(r"<a:clrScheme name=\"([^\"]*)\"", t)
    out["name"] = m.group(1) if m else ""
    return out


def probe(path):
    prs = Presentation(path)
    sw, sh = prs.slide_width / EMU, prs.slide_height / EMU
    layouts = []
    for m in prs.slide_masters:
        for l in m.slide_layouts:
            layouts.append(layout_info(l, sw, sh))
    th = theme_info(path)
    pick = lambda role, words: next((l for l in layouts if l["role"] == role and any(w in l["name"].lower() for w in words)), None) or next((l for l in layouts if l["role"] == role), None)
    cover = pick("cover", COVER_WORDS)
    section = pick("section", SECTION_WORDS)
    content = pick("content-base", CONTENT_WORDS)
    fallback = None
    if not content:
        cands = [l for l in layouts if l["role"] == "content-with-body-placeholders"]
        # fewest body placeholders first, then a name that sounds like a chart or title-only layout
        cands.sort(key=lambda l: (len(l["body_placeholders"]), 0 if any(w in l["name"].lower() for w in CONTENT_WORDS) else 1))
        fallback = cands[0] if cands else None
    c = th["colors"]
    roles = {
        "message": {"slot": "accent1", "hex": c.get("accent1")},
        "signal": {"slot": "accent2", "hex": c.get("accent2")},
        "neutral": {"slot": "dk2", "hex": c.get("dk2")},
        "muted": {"slot": "accent6" if "accent6" in c else "accent3", "hex": c.get("accent6", c.get("accent3"))},
        "text": {"slot": "dk1", "hex": c.get("dk1")},
        "background": {"slot": "lt1", "hex": c.get("lt1")},
        "tint": {"slot": "lt2", "hex": c.get("lt2")},
    }
    return {
        "template": path, "slide_size": {"w": round(sw, 2), "h": round(sh, 2)},
        "sample_slides": len(prs.slides),
        "layouts": layouts,
        "recommended": {"cover": cover["name"] if cover else None, "section": section["name"] if section else None,
                        "content": content["name"] if content else (fallback["name"] if fallback else None),
                        "content_needs_placeholder_removal": bool(fallback and not content),
                        "body_zone": (content or fallback or {}).get("body_zone")},
        "theme": th, "roles": roles,
    }


def brief(p):
    r, z = p["recommended"], p["recommended"]["body_zone"]
    lines = [f"# Template brief (draft): {p['template']}", "",
             f"Slide size: {p['slide_size']['w']} x {p['slide_size']['h']} in | sample slides in file: {p['sample_slides']} (removed on use) | theme: {p['theme'].get('name') or 'unnamed'}", "",
             "## Layouts", "", "| Layout | Role | Placeholders (type:idx) | Chrome | Body placeholders |", "|---|---|---|---|---|"]
    for l in p["layouts"]:
        phs = ", ".join(f"{x['type'].lower()}:{x['idx']}" for x in l["placeholders"]) or "none"
        chrome = ", ".join(f"{c['kind']} {c['name']}" for c in l["chrome"]) or "none"
        lines.append(f"| {l['name']} | {l['role'] or 'unclear'} | {phs} | {chrome} | {len(l['body_placeholders'])} |")
    lines += ["", "## Proposed use (confirm)", "",
              f"- cover: {r['cover'] or '[not found: name it]'}",
              f"- section: {r['section'] or '[not found: name it, or none and the deck uses lead slides]'}",
              f"- content base: {r['content'] or '[not found: name the layout with title and chrome only]'}" + (" (has body placeholders: the helpers delete them, never fill them)" if r["content_needs_placeholder_removal"] else ""),
              f"- body zone on the content base: x {z['x']} y {z['y']} w {z['w']} h {z['h']} in" + ("; top-right is chrome, tracker goes left of it" if z and z.get("top_right_chrome") else "") if z else "- body zone: not derivable, set by hand",
              "", "## Theme", "",
              "fonts: heading " + str(p["theme"]["fonts"].get("heading")) + ", body " + str(p["theme"]["fonts"].get("body")),
              "palette: " + ", ".join(f"{k} {v}" for k, v in p["theme"]["colors"].items()),
              "", "## Colour roles (draft, confirm)", "", "| Role | Theme slot | Hex | Used for |", "|---|---|---|---|",
              f"| message | {p['roles']['message']['slot']} | {p['roles']['message']['hex']} | the one highlight per exhibit, recommended option |",
              f"| signal | {p['roles']['signal']['slot']} | {p['roles']['signal']['hex']} | warning marks, caveat boxes |",
              f"| neutral | {p['roles']['neutral']['slot']} | {p['roles']['neutral']['hex']} | everything else in exhibits |",
              f"| muted | {p['roles']['muted']['slot']} | {p['roles']['muted']['hex']} | sources, labels, rules |",
              "", "Open before Stage 2: confirm the three layouts, the colour roles and whether the footer text and slide number come from the layout (they usually do: never redraw them)."]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    p = probe(path)
    md = brief(p)
    if "--json" in sys.argv:
        with open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8") as f:
            json.dump(p, f, indent=1, ensure_ascii=False)
    if "--md" in sys.argv:
        with open(sys.argv[sys.argv.index("--md") + 1], "w", encoding="utf-8") as f:
            f.write(md + "\n")
    else:
        print(md)


if __name__ == "__main__":
    main()
