// example-build.js — minimal build file using pptx-helpers.js.
// Run: node example-build.js speaker out.pptx   |   node example-build.js handout out_handout.pptx
// Content below is a pattern, not a template to reuse: every real deck writes
// its own build file from the approved ghost deck and register.
const path = require("path");
const { createDeck } = require(path.join(__dirname, "pptx-helpers.js"));

const MODE = process.argv[2] || "speaker";
const OUT = process.argv[3] || `example_${MODE}.pptx`;
const d = createDeck({ mode: MODE, title: "Example deck", author: "[Vortragende/r]" });
const { PH, cols, BODY_Y, BODY_H, TINT, T, C } = d;

// 1 title
d.titleSlide("Example: three slides that follow the skill",
  [{ text: "Decision paper pattern", options: { fontSize: 22 } }, { text: `${PH("Datum")} · ${PH("Vortragende/r")}`, options: { fontSize: 14, color: T.colors.accent4 } }],
  { key: "What the audience takes from the deck in one sentence.", open: "First spoken sentence.", trans: "To the summary.", time: 0.5 });

// 2 management summary: key line left, ask right
d.content("Management Summary", "Governing thought as a full sentence that the audience could disagree with",
  "Management Summary · details in sections A to C",
  { key: "The one sentence to remember.", open: "This slide is the whole deck.", track: ["A …", "B …", "C …"], point: "Lines left, then the box right.", trans: "Section A.", time: 2 },
  (s, h) => {
    const lines = [["A", "Key-line claim one as a full sentence."], ["B", "Key-line claim two as a full sentence."], ["C", "Key-line claim three as a full sentence."]];
    const leftW = h.CW - 3.9 - h.G, rowH = BODY_H / 3;
    lines.forEach((l, i) => {
      const y = BODY_Y + i * rowH;
      s.addShape(h.pres.ShapeType.ellipse, { x: h.M, y: y + 0.08, w: 0.5, h: 0.5, fill: { color: C.accent2 }, line: { color: C.accent2, width: 0 } });
      h.txt(s, l[0], h.M, y + 0.08, 0.5, 0.5, { fontSize: 14, bold: true, color: C.background1, align: "center", valign: "middle" });
      h.txt(s, l[1], h.M + 0.7, y, leftW - 0.7, rowH - 0.1, { fontSize: h.F.head });
    });
    h.card(s, h.W - h.M - 3.9, BODY_Y, 3.9, BODY_H, "Proposed decision", ["Decision point one", "Decision point two"], { fill: TINT, headColor: C.accent2, size: h.F.head, gap: 12 });
  });

// 3 options table in list style, recommended column highlighted
d.content("C · Options", "Of three options examined only option A meets all three criteria: scope, cost, time",
  `Assessment: preliminary, ${PH("Autor")}`,
  { key: "Three options, three criteria, one winner.", open: "Before the detail: what we compared.", track: ["Option B fails on cost.", "Option C fails on time.", "Option A meets all three."], point: "Highlighted column.", trans: "How option A works.", time: 1.5 },
  (s, h) => {
    const Y = h.MARK(T.colors.accent2, "✓", h.F.tbl + 4), N = h.MARK(T.colors.accent1, "✗", h.F.tbl + 4);
    h.label(s, "Options compared", h.M, BODY_Y, h.CW);
    h.ltable(s, h.M, BODY_Y + 0.45, h.CW, [
      ["Criterion", "Option A (recommended)", "Option B", "Option C"],
      ["Scope covered", Y, Y, N], ["Within budget", Y, N, Y], ["Ready before deadline", Y, Y, N],
      ["Main drawback", "needs two owners", `${PH("x")} over budget`, "ready late"],
    ], [3.93, 2.8, 2.8, 2.8], { rowH: (BODY_H - 0.45) / 5, hl: 1, center: [1, 2, 3] });
  });

d.write(OUT).then(r => console.log("written", r.path, "slides:", r.slides, "minutes:", r.minutes));
