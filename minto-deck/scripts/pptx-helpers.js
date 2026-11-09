// pptx-helpers.js — rendering helpers for minto-deck when the host has no
// native PowerPoint capability and the deck is built with pptxgenjs.
//
// Encodes the layout rules of references/visual-design.md and
// references/consulting-practices.md: fixed zones, one grid, list-style
// tables, cards, big numbers, chevrons, notes in the notes pane, a key-point
// strip for the handout variant. Content stays in the per-deck build file;
// this file never contains deck content.
//
// Usage (see scripts/README.md and scripts/example-build.js):
//   const { createDeck } = require("./pptx-helpers.js");
//   const d = createDeck({ mode: "speaker" | "handout", title, author, theme });
//   d.titleSlide(...); d.content(tracker, title, source, notes, (s, h) => { ... });
//   await d.write("/mnt/user-data/outputs/deck.pptx");
//
// Requires pptxgenjs in the environment. If Anthropic's pptx skill is present,
// its apply_theme.js is used to write a proper theme into the file.

const pptxgen = require("pptxgenjs");
// Optional: Anthropic's pptx skill can write the palette into the file's theme
// so that Office's colour menus show it. Rendering never depends on it: every
// element below takes its colour from T.colors as a hex value. write() reports
// whether the theme writer ran.
let applyTheme = null;
try { ({ applyTheme } = require("/mnt/skills/public/pptx/scripts/apply_theme.js")); } catch (e) { applyTheme = null; }

const DEFAULT_THEME = {
  name: "Minto Neutral",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1F2A33", lt1: "FFFFFF", dk2: "3A4A57", lt2: "F3F4F6",
    accent1: "A33F2B",   // signal (gap, warning, negative)
    accent2: "1F6F78",   // accent (message, recommendation, positive)
    accent3: "C9A227", accent4: "7A8A99", accent5: "DCE3E8", accent6: "5B6770",
    hlink: "1F6F78", folHlink: "5B6770",
  },
};

function createDeck(opts = {}) {
  const MODE = opts.mode || "speaker";
  const HANDOUT = MODE === "handout";
  const T = Object.assign({}, DEFAULT_THEME, opts.theme || {});
  T.colors = Object.assign({}, DEFAULT_THEME.colors, (opts.theme && opts.theme.colors) || {});
  const TINT = opts.tint || "E3EEF0", TINT_SIGNAL = opts.tintSignal || "F6E7E3", RULE = "C9D1D8";

  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.theme = { headFontFace: T.headFontFace, bodyFontFace: T.bodyFontFace };
  pres.author = opts.author || "";
  pres.title = opts.title || "";
  // Colour roles as hex from T.colors. Scheme colours (pres.SchemeColor) would
  // resolve against the file's theme, which is Office's default palette unless
  // a theme writer runs; that mixed two palettes in one deck.
  const C = {
    text1: T.colors.dk1, text2: T.colors.dk2, background1: T.colors.lt1, background2: T.colors.lt2,
    accent1: T.colors.accent1, accent2: T.colors.accent2, accent3: T.colors.accent3,
    accent4: T.colors.accent4, accent5: T.colors.accent5, accent6: T.colors.accent6,
  };

  // ---- grid and zones (inches) ----
  const W = 13.33, M = 0.5, CW = W - 2 * M, G = 0.25;
  const TITLE_Y = 0.42, TITLE_H = 1.0, BODY_Y = 1.7;
  const BODY_H = HANDOUT ? 3.85 : 4.85;
  const KEY_Y = 5.7, KEY_H = 0.8, SRC_Y = 6.85;
  // type scale by density mode (visual-design.md section 4)
  const F = HANDOUT ? { body: 14, head: 16, big: 50, small: 11, tbl: 12, title: 20 }
                    : { body: 16, head: 18, big: 62, small: 12, tbl: 14, title: 22 };
  const cols = (n, g = G) => { const w = (CW - (n - 1) * g) / n; return Array.from({ length: n }, (_, i) => ({ x: M + i * (w + g), w })); };
  const PH = (t) => `[PLATZHALTER: ${t}]`;

  // ---- masters ----
  pres.defineSlideMaster({ title: "TITLE", background: { color: T.colors.dk1 }, objects: [
    { placeholder: { options: { name: "title", type: "title", x: M, y: 2.3, w: CW, h: 1.6, fontSize: 40, bold: true, color: T.colors.lt1, align: "left", valign: "bottom", margin: 0 } } },
    { placeholder: { options: { name: "body", type: "body", x: M, y: 4.05, w: CW, h: 1.6, fontSize: 20, color: T.colors.accent5, align: "left", valign: "top", margin: 0 } } },
  ] });
  pres.defineSlideMaster({ title: "SECTION", background: { color: T.colors.lt2 }, objects: [
    { placeholder: { options: { name: "title", type: "title", x: M, y: 2.9, w: CW, h: 1.4, fontSize: 30, bold: true, color: T.colors.dk1, align: "left", valign: "middle", margin: 0 } } },
  ] });
  pres.defineSlideMaster({ title: "CONTENT", background: { color: T.colors.lt1 }, objects: [
    { placeholder: { options: { name: "title", type: "title", x: M, y: TITLE_Y, w: CW - 2.2, h: TITLE_H, fontSize: F.title, bold: true, color: T.colors.dk1, align: "left", valign: "top", margin: 0 } } },
  ], slideNumber: { x: W - M - 0.6, y: SRC_Y, w: 0.6, h: 0.3, fontSize: F.small, color: T.colors.accent6, align: "right" } });

  // ---- notes (speaker-notes.md) ----
  const timeStr = (t) => String(t).replace(".", ",");
  function speakerNotes(n) {
    const L = [`Kernpunkt: ${n.key}`];
    if (n.open) L.push(`Einstieg: ${n.open}`);
    if (n.track) { L.push("Sprechverlauf:"); n.track.forEach(t => L.push(`- ${t}`)); }
    if (n.point) L.push(`Zeigen auf: ${n.point}`);
    if (n.trans) L.push(`Überleitung: ${n.trans}`);
    if (n.time !== undefined) L.push(`Zeit: ${timeStr(n.time)} min`);
    if (n.watch) L.push(`Achtung: ${n.watch}`);
    return L.join("\n");
  }
  const handoutNotes = (n) => `Kernpunkt: ${n.key}`;
  const notesLog = [];
  // One registration for every slide type: the handout filter and the timing
  // log apply alike to title, section and content slides.
  function registerNotes(s, title, notes) {
    if (!notes) return null;
    const n = typeof notes === "string" ? { key: notes } : notes;
    s.addNotes(HANDOUT ? handoutNotes(n) : speakerNotes(n));
    notesLog.push({ title, time: n.time });
    return n;
  }

  // ---- primitives ----
  const box = (s, x, y, w, h, fill, name = "box") =>
    s.addShape(pres.ShapeType.rect, { x, y, w, h, fill: { color: fill }, line: { color: fill, width: 0 }, objectName: name });
  const txt = (s, text, x, y, w, h, o = {}) =>
    s.addText(text, Object.assign({ x, y, w, h, fontSize: F.body, color: C.text1, margin: 0, isTextBox: true, valign: "top", objectName: "text" }, o));
  function bullets(s, items, x, y, w, h, o = {}) {
    const runs = items.map((t, i) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1, paraSpaceAfter: o.gap || 8 } }));
    txt(s, runs, x, y, w, h, Object.assign({ fontSize: F.body, color: C.text2 }, o));
  }
  function card(s, x, y, w, h, head, items, o = {}) {
    box(s, x, y, w, h, o.fill || C.background2, "card");
    txt(s, head, x + 0.25, y + 0.22, w - 0.5, 0.5, { fontSize: F.head, bold: true, color: o.headColor || C.text1 });
    bullets(s, items, x + 0.25, y + 0.85, w - 0.5, h - 1.05, { fontSize: o.size || F.body, gap: o.gap });
  }
  function bigStat(s, x, y, w, h, stat, label, sub) {
    // Reserve the sub line first, then give the label the space that is left;
    // the three boxes never overlap (card height of 1.6 in or more).
    box(s, x, y, w, h, C.background2, "stat-box");
    const pad = 0.2, subH = sub ? 0.45 : 0;
    const statH = Math.max(0.6, Math.min(h * 0.42, h - subH - 0.9));
    const labelY = y + pad + statH + 0.05;
    const labelH = Math.max(0.3, (y + h - subH - 0.15) - labelY);
    txt(s, stat, x + 0.3, y + pad, w - 0.6, statH, { fontSize: F.big, bold: true, color: C.accent1, valign: "middle" });
    txt(s, label, x + 0.3, labelY, w - 0.6, labelH, { fontSize: F.head, color: C.text1 });
    if (sub) txt(s, sub, x + 0.3, y + h - subH - 0.15, w - 0.6, subH, { fontSize: F.small, color: C.accent6 });
  }
  function label(s, text, x, y, w, o = {}) {
    txt(s, text, x, y, w, 0.35, Object.assign({ fontSize: F.small, color: C.accent6, charSpacing: 1 }, o));
  }
  // list-style table (consulting-practices.md section 16, visual-design.md 6b)
  function ltable(s, x, y, w, rows, colW, o = {}) {
    const B = (pt, color) => ({ type: "solid", pt, color }); const NONE = { type: "none" };
    const fillFor = (ci) => (o.hl !== undefined && ci === o.hl) ? { color: TINT } : { color: T.colors.lt1 };
    const alignFor = (ci) => (o.center && o.center.includes(ci)) ? "center" : (o.right && o.right.includes(ci)) ? "right" : "left";
    const hdr = rows[0].map((t, ci) => ({ text: t, options: { bold: true, color: T.colors.dk1, fontSize: o.hSize || F.tbl - 1, valign: "bottom", border: [NONE, NONE, B(1.25, T.colors.dk2), NONE], fill: fillFor(ci), align: alignFor(ci) } }));
    const body = rows.slice(1).map((r) => r.map((t, ci) => {
      const base = { fontSize: o.size || F.tbl, color: T.colors.dk1, valign: "middle", border: [NONE, NONE, B(0.5, RULE), NONE], fill: fillFor(ci), align: alignFor(ci) };
      if (t && typeof t === "object") return { text: t.text, options: Object.assign(base, t.options) };
      return { text: t, options: base };
    }));
    s.addTable([hdr, ...body], { x, y, w, colW, rowH: o.rowH || 0.42, margin: [0.04, 0.1, 0.04, 0.1], fontFace: T.bodyFontFace });
  }
  const MARK = (color, ch = "●", size) => ({ text: ch, options: { color, bold: true, fontSize: size || F.tbl + 2 } });
  function chevrons(s, items, y, h, o = {}) {
    // items: [{head, sub}] ; highlight index via o.hl. A sub line (owner, date,
    // deliverable) renders under the head; nothing passed in is dropped.
    const hasSub = items.some(it => it && it.sub);
    cols(items.length).forEach((c, i) => {
      s.addShape(pres.ShapeType.chevron, { x: c.x, y, w: c.w, h, fill: { color: i === o.hl ? T.colors.accent2 : T.colors.dk2 }, line: { color: T.colors.lt1, width: 0 }, objectName: "chevron" });
      if (hasSub) {
        txt(s, items[i].head, c.x + 0.55, y + 0.08, c.w - 0.95, h * 0.5, { fontSize: F.body, bold: true, color: C.background1, valign: "bottom" });
        if (items[i].sub) txt(s, items[i].sub, c.x + 0.55, y + h * 0.56, c.w - 0.95, h * 0.4, { fontSize: F.small, color: C.accent5, valign: "top" });
      } else {
        txt(s, items[i].head, c.x + 0.55, y, c.w - 0.95, h, { fontSize: F.body, bold: true, color: C.background1, valign: "middle" });
      }
    });
  }
  function pill(s, text, x, y, w, o = {}) {
    s.addShape(pres.ShapeType.roundRect, { x, y, w, h: 0.42, fill: { color: o.fill || T.colors.dk2 }, line: { color: o.fill || T.colors.dk2, width: 0 }, rectRadius: 0.2, objectName: "pill" });
    txt(s, text, x, y, w, 0.42, { fontSize: F.small, color: C.background1, align: "center", valign: "middle" });
  }

  // ---- slide types ----
  function titleSlide(title, lines, notes) {
    const s = pres.addSlide({ masterName: "TITLE" });
    s.addText(title, { placeholder: "title" });
    s.addText(lines.map((l, i) => ({ text: l.text, options: Object.assign({ breakLine: i < lines.length - 1 }, l.options || {}) })), { placeholder: "body" });
    registerNotes(s, title, notes);
    return s;
  }
  function sectionSlide(title, notes) {
    const s = pres.addSlide({ masterName: "SECTION" });
    s.addText(title, { placeholder: "title" });
    registerNotes(s, title, notes);
    return s;
  }
  // content(tracker, title, source, notes, build(slide, h)) — h exposes geometry and primitives
  function content(tracker, title, source, notes, build) {
    const s = pres.addSlide({ masterName: "CONTENT" });
    s.addText(title, { placeholder: "title" });
    if (tracker) s.addText(String(tracker).toUpperCase(), { x: W - M - 2.1, y: TITLE_Y, w: 2.1, h: 0.3, fontSize: F.small, color: C.accent6, align: "right", charSpacing: 1, margin: 0, isTextBox: true, objectName: "tracker" });
    build(s, api);
    if (HANDOUT && notes) {
      box(s, M, KEY_Y, CW, KEY_H, C.background2, "key-box");
      s.addText([{ text: "Kernpunkt: ", options: { bold: true } }, { text: notes.key }], { x: M + 0.2, y: KEY_Y, w: CW - 0.4, h: KEY_H, fontSize: 12, color: C.text1, valign: "middle", margin: 0, isTextBox: true, objectName: "key-text" });
    }
    if (source) s.addText(source, { x: M, y: SRC_Y, w: CW - 0.8, h: 0.3, fontSize: F.small, color: C.accent6, margin: 0, isTextBox: true, objectName: "source" });
    registerNotes(s, title, notes);
    return s;
  }
  async function write(path) {
    await pres.writeFile({ fileName: path });
    let themeApplied = false;
    if (applyTheme) { await applyTheme(path, T); themeApplied = true; }
    return { path, slides: pres.slides.length, minutes: notesLog.reduce((a, n) => a + (Number(n.time) || 0), 0), notesLog, themeApplied };
  }

  const api = { pres, C, T, F, MODE, HANDOUT, W, M, CW, G, TITLE_Y, TITLE_H, BODY_Y, BODY_H, KEY_Y, KEY_H, SRC_Y, TINT, TINT_SIGNAL, RULE,
    cols, PH, box, txt, bullets, card, bigStat, label, ltable, MARK, chevrons, pill, titleSlide, sectionSlide, content, write, speakerNotes };
  return api;
}

module.exports = { createDeck, DEFAULT_THEME };
