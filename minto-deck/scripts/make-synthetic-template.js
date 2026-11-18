// make-synthetic-template.js — builds assets/synthetic-corp.pptx, a
// stand-in for a corporate template: own theme palette and fonts, a logo mark,
// footer and slide number on every layout, and four layouts (Cover, Section,
// Content, Content 2 Columns). The eval `template-build-forms` and the Python
// helper tests use it, so no company template has to enter the repository.
//
//   npm install pptxgenjs   (once)
//   node scripts/make-synthetic-template.js [out.pptx]
//
// The 2-column layout carries two body placeholders on purpose: the template
// path must delete them, never fill them (template-mode.md, rule T1).
const path = require("path");
const fs = require("fs");
const PptxGenJS = require("pptxgenjs");
let applyTheme = null;
try { ({ applyTheme } = require("/mnt/skills/public/pptx/scripts/apply_theme.js")); } catch (e) { applyTheme = null; }

const OUT = process.argv[2] || path.join(__dirname, "..", "assets", "synthetic-corp.pptx");
const PAL = { dk1: "1B1F2A", lt1: "FFFFFF", dk2: "123C69", lt2: "EEF1F5", accent1: "E8702A", accent2: "2A9D8F", accent3: "8D99AE", accent4: "F4A261", accent5: "264653", accent6: "6C757D", hlink: "123C69", folHlink: "6C757D" };

const pres = new PptxGenJS();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5 in
pres.theme = { headFontFace: "Georgia", bodyFontFace: "Verdana" };
const W = 13.33, H = 7.5;

const chrome = (dark) => [
  { rect: { x: W - 1.6, y: 0.3, w: 0.35, h: 0.35, fill: { color: PAL.accent1 }, objectName: "logo-mark" } },
  { text: { text: "ACME", options: { x: W - 1.2, y: 0.25, w: 1.0, h: 0.45, fontSize: 14, bold: true, fontFace: "Georgia", color: dark ? PAL.lt1 : PAL.dk2, objectName: "logo-text" } } },
  { text: { text: "ACME Group · Confidential", options: { x: 0.5, y: H - 0.45, w: 6, h: 0.3, fontSize: 9, fontFace: "Verdana", color: dark ? PAL.lt2 : PAL.accent6, objectName: "footer-text" } } },
  { line: { x: 0.5, y: H - 0.55, w: W - 1.0, h: 0, line: { color: dark ? PAL.lt2 : PAL.accent3, width: 0.75 }, objectName: "footer-rule" } },
];
const slideNumber = (dark) => ({ x: W - 1.2, y: H - 0.45, w: 0.7, h: 0.3, fontSize: 9, fontFace: "Verdana", color: dark ? PAL.lt2 : PAL.accent6, align: "right" });

pres.defineSlideMaster({ title: "Cover", background: { color: PAL.dk2 }, slideNumber: slideNumber(true), objects: [
  ...chrome(true),
  { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.6, w: 11.0, h: 1.4, fontSize: 36, bold: true, fontFace: "Georgia", color: PAL.lt1 }, text: "" } },
  { placeholder: { options: { name: "subtitle", type: "body", x: 0.8, y: 4.1, w: 11.0, h: 1.0, fontSize: 18, fontFace: "Verdana", color: PAL.lt2 }, text: "" } },
] });
pres.defineSlideMaster({ title: "Section", background: { color: PAL.lt2 }, slideNumber: slideNumber(false), objects: [
  ...chrome(false),
  { rect: { x: 0.8, y: 3.2, w: 0.12, h: 1.2, fill: { color: PAL.accent1 }, objectName: "section-bar" } },
  { placeholder: { options: { name: "title", type: "title", x: 1.1, y: 3.0, w: 10.5, h: 1.6, fontSize: 32, bold: true, fontFace: "Georgia", color: PAL.dk2 }, text: "" } },
] });
pres.defineSlideMaster({ title: "Content", background: { color: PAL.lt1 }, slideNumber: slideNumber(false), objects: [
  ...chrome(false),
  { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.4, w: 10.9, h: 1.0, fontSize: 22, bold: true, fontFace: "Georgia", color: PAL.dk2, valign: "top" }, text: "" } },
] });
pres.defineSlideMaster({ title: "Content 2 Columns", background: { color: PAL.lt1 }, slideNumber: slideNumber(false), objects: [
  ...chrome(false),
  { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.4, w: 10.9, h: 1.0, fontSize: 22, bold: true, fontFace: "Georgia", color: PAL.dk2, valign: "top" }, text: "" } },
  { placeholder: { options: { name: "body-left", type: "body", x: 0.5, y: 1.7, w: 6.0, h: 4.8, fontSize: 14, fontFace: "Verdana", color: PAL.dk1 }, text: "" } },
  { placeholder: { options: { name: "body-right", type: "body", x: 6.8, y: 1.7, w: 6.0, h: 4.8, fontSize: 14, fontFace: "Verdana", color: PAL.dk1 }, text: "" } },
] });

// one sample slide per layout so every layout is written into the file
for (const m of ["Cover", "Section", "Content", "Content 2 Columns"]) {
  const s = pres.addSlide({ masterName: m });
  s.addText(m + " layout (sample slide, delete)", { placeholder: "title" });
}

fs.mkdirSync(path.dirname(OUT), { recursive: true });
pres.writeFile({ fileName: OUT }).then(async () => {
  let themed = false;
  if (applyTheme) { try { await applyTheme(OUT, { name: "ACME Synthetic", colors: PAL }); themed = true; } catch (e) { themed = false; } }
  console.log(JSON.stringify({ path: OUT, layouts: ["Cover", "Section", "Content", "Content 2 Columns"], themeApplied: themed }));
}).catch(e => { console.error(e); process.exit(1); });
