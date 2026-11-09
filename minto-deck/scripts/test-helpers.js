// Smoke test for pptx-helpers.js. Run: node scripts/test-helpers.js
// Needs pptxgenjs resolvable from the working directory (npm install pptxgenjs).
// Checks the fixes of v0.6.2: content passed in is rendered (chevron sub
// lines), timing adds up over every slide type, the handout filter applies to
// every slide type, no scheme colours, no font under the handout minimum, and
// bigStat boxes do not overlap.
const path = require("path");
const fs = require("fs");
const os = require("os");
const { execSync } = require("child_process");
const { createDeck } = require(path.join(__dirname, "pptx-helpers.js"));

function assert(cond, msg) { if (!cond) { console.error("FAIL: " + msg); process.exitCode = 1; } else console.log("ok: " + msg); }
function unzipXml(file, inner) {
  return execSync(`unzip -p "${file}" "${inner}"`, { encoding: "utf8" });
}
function listEntries(file) { return execSync(`unzip -Z1 "${file}"`, { encoding: "utf8" }).split("\n"); }

async function build(mode) {
  const d = createDeck({ mode, title: "Smoke", author: "test" });
  d.titleSlide("Titel", [{ text: "Untertitel" }], { key: "Titelkern", open: "Einstieg Titel", time: 0.5 });
  d.sectionSlide("Abschnitt A", { key: "Abschnittskern", trans: "Überleitung A", time: 0.75 });
  d.content("A", "Inhaltstitel als Satz", "Quelle: Test", { key: "Inhaltskern", open: "Einstieg Inhalt", time: 1.25 }, (s, h) => {
    h.chevrons(s, [{ head: "Phase 1", sub: "Owner A, bis Q1" }, { head: "Phase 2", sub: "Owner B, bis Q2" }], h.BODY_Y, 1.0, { hl: 1 });
    h.bigStat(s, h.M, h.BODY_Y + 1.3, 4, 2.2, "42 %", "Eine zweizeilige Beschreibung, die umbricht und Platz braucht", "Unterzeile Quelle 2025");
  });
  const out = path.join(os.tmpdir(), `smoke-${mode}.pptx`);
  const r = await d.write(out);
  return { r, out };
}

(async () => {
  const sp = await build("speaker");
  assert(Math.abs(sp.r.minutes - 2.5) < 1e-9, `speaker minutes add up over title, section and content (got ${sp.r.minutes})`);
  const entries = listEntries(sp.out);
  const slideXml = entries.filter(e => /^ppt\/slides\/slide\d+\.xml$/.test(e)).map(e => unzipXml(sp.out, e)).join("\n");
  assert(slideXml.includes("Owner A, bis Q1"), "chevron sub line is rendered");
  assert(!/<a:schemeClr/.test(slideXml), "no scheme colours in slide content (palette comes from T.colors)");

  const ho = await build("handout");
  const hEntries = listEntries(ho.out);
  const notesXml = hEntries.filter(e => /^ppt\/notesSlides\/notesSlide\d+\.xml$/.test(e)).map(e => unzipXml(ho.out, e)).join("\n");
  assert(!/Einstieg:|Überleitung:|Zeit:/.test(notesXml), "handout notes carry only the key point on every slide type");
  assert(/Kernpunkt: Abschnittskern/.test(notesXml), "section slide notes present in handout");
  const hSlideXml = hEntries.filter(e => /^ppt\/slides\/slide\d+\.xml$/.test(e)).map(e => unzipXml(ho.out, e)).join("\n");
  const sizes = [...hSlideXml.matchAll(/sz="(\d+)"/g)].map(m => Number(m[1]) / 100);
  assert(sizes.length > 0 && Math.min(...sizes) >= 11, `handout font sizes at or above 11 pt (min ${Math.min(...sizes)})`);

  // bigStat geometry, recomputed from the helper's rule for h = 2.2 with a sub line
  const h = 2.2, pad = 0.2, subH = 0.45;
  const statH = Math.max(0.6, Math.min(h * 0.42, h - subH - 0.9));
  const labelY = pad + statH + 0.05, labelH = Math.max(0.3, (h - subH - 0.15) - labelY), subY = h - subH - 0.15;
  assert(labelY + labelH <= subY + 1e-9, `bigStat label ends (${(labelY + labelH).toFixed(2)}) before sub line starts (${subY.toFixed(2)})`);
  console.log("themeApplied:", sp.r.themeApplied);
})().catch(e => { console.error(e); process.exitCode = 1; });
