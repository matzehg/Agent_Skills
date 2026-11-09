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
    h.ltable(s, h.M + 4.4, h.BODY_Y + 1.3, 5.5, [["Hürde", "Heute", "Vertragliche Lösung"], ["Akzeptanzkriterien", "nicht messbar formuliert", "Zielkorridore im Vertrag"], ["Testdaten", "erst nach Vertragsschluss", "Sandbox vor Vertragsschluss"], ["Schwellenwerte", "nicht vereinbart", "Schwellenwerte für Updates"]], [1.6, 1.9, 2.0]);
  });
  // six-node cycle, the case the catalogue allows and v0.7 got wrong
  d.content("D", "Sechser-Kreislauf als Satz", "Quelle: Test", { key: "Sechser", time: 0.5 }, (s, h) => {
    h.cycle(s, ["Eins", "Zwei", "Drei", "Vier", "Fünf", "Sechs"], 6.0, h.BODY_Y + 2.3, 1.5, { hl: 5 });
  });
  d.content("B", "Konzeptgrafiken als Satz", "Quelle: Test", { key: "Konzeptkern", time: 1 }, (s, h) => {
    h.cycle(s, ["Anforderung", "Abnahme", "Betrieb", "Revalidierung"], 3.2, h.BODY_Y + 2.3, 1.5, { hl: 3 });
    h.continuum(s, ["Gesetz", "Vertrag"], [{ pos: 0.1, label: "AA" }, { pos: 0.8, label: "BMVg" }, { pos: 0.95, label: "Podium" }], h.BODY_Y + 4.4, { hl: 2 });
  });
  d.content("C", "Zeit und Matrix als Satz", "Quelle: Test", { key: "Zeitkern", time: 1 }, (s, h) => {
    h.timeline(s, [{ date: "2019", label: "AG Technikverantwortung" }, { date: "2023", label: "Impulspapier" }, { date: "03.11.2026", label: "Sandbox-Konzept" }, { date: "2027", label: "AIMD-Dialog" }], h.BODY_Y + 0.8, { hl: 2, now: 2 });
    h.matrix(s, ["gering", "hoch"], ["gering", "hoch"], [{ head: "Beobachten" }, { head: "Pilotieren", items: ["Sandbox"] }, { head: "Ignorieren" }, { head: "Umsetzen" }], h.M, h.BODY_Y + 2.0, 6.2, 2.7, { hl: 1 });
  });
  const out = path.join(os.tmpdir(), `smoke-${mode}.pptx`);
  const r = await d.write(out);
  return { r, out };
}

(async () => {
  const sp = await build("speaker");
  assert(Math.abs(sp.r.minutes - 5.0) < 1e-9, `speaker minutes add up over title, section and content (got ${sp.r.minutes})`);
  assert(Array.isArray(sp.r.wordsPerSlide) && sp.r.wordsPerSlide.length === 6, `wordsPerSlide reported per slide (${JSON.stringify(sp.r.wordsPerSlide)})`);
  assert(sp.r.wordsPerSlide[2].words >= 25 + 24, `table words are counted in wordsPerSlide (slide 3: ${sp.r.wordsPerSlide[2].words}, expected text plus 24 table words)`);
  const entries = listEntries(sp.out);
  const slideXml = entries.filter(e => /^ppt\/slides\/slide\d+\.xml$/.test(e)).map(e => unzipXml(sp.out, e)).join("\n");
  assert(slideXml.includes("Owner A, bis Q1"), "chevron sub line is rendered");
  assert(slideXml.includes("Revalidierung") && slideXml.includes("Sandbox-Konzept") && slideXml.includes("Pilotieren") && slideXml.includes("Vertrag"), "cycle, timeline, matrix and continuum render their labels");
  assert((slideXml.match(/cycle-node/g) || []).length === 10 && (slideXml.match(/timeline-marker/g) || []).length === 4 && (slideXml.match(/matrix-cell/g) || []).length === 4 && (slideXml.match(/continuum-marker/g) || []).length === 3, "concept visuals create the expected number of shapes");
  assert(!/<a:schemeClr/.test(slideXml), "no scheme colours in slide content (palette comes from T.colors)");

  const ho = await build("handout");
  const hEntries = listEntries(ho.out);
  const notesXml = hEntries.filter(e => /^ppt\/notesSlides\/notesSlide\d+\.xml$/.test(e)).map(e => unzipXml(ho.out, e)).join("\n");
  assert(!/Einstieg:|Überleitung:|Zeit:/.test(notesXml), "handout notes carry only the key point on every slide type");
  assert(/Kernpunkt: Abschnittskern/.test(notesXml), "section slide notes present in handout");
  const hSlideXml = hEntries.filter(e => /^ppt\/slides\/slide\d+\.xml$/.test(e)).map(e => unzipXml(ho.out, e)).join("\n");
  const sizes = [...hSlideXml.matchAll(/sz="(\d+)"/g)].map(m => Number(m[1]) / 100);
  assert(sizes.length > 0 && Math.min(...sizes) >= 11, `handout font sizes at or above 11 pt (min ${Math.min(...sizes)})`);

  // bigStat: layout from the helper itself; label box must hold its lines and end before the sub line
  const dk = createDeck({ mode: "speaker" });
  const L = dk.bigStatLayout(2.2, 4, "Eine zweizeilige Beschreibung, die umbricht und Platz braucht", "Unterzeile Quelle 2025");
  const linesFit = (L.labelH * 72) / (L.labelFont * 1.2) >= 2 - 1e-9;
  assert(linesFit && L.labelY + L.labelH <= L.subY + 1e-9, `bigStat 2.2 in: label box holds two lines at ${L.labelFont} pt and ends (${(L.labelY + L.labelH).toFixed(2)}) before the sub line (${L.subY.toFixed(2)})`);
  let threw = false;
  try { dk.bigStatLayout(1.6, 4, "Eine zweizeilige Beschreibung, die umbricht und Platz braucht", "Unterzeile Quelle 2025"); } catch (e) { threw = /too small/.test(e.message); }
  assert(threw, "bigStat rejects a 1.6 in card that cannot hold a two-line label and a sub line");
  // cycle: six nodes, every arrow keeps its direction and a visible length
  const g = dk.cycleGeometry(6, 6, 4, 1.5, 2.0, 0.7);
  const okDir = g.arrows.every(ar => ((ar.b.x - ar.a.x) * (ar.q.x - ar.p.x) + (ar.b.y - ar.a.y) * (ar.q.y - ar.p.y)) > 0);
  const okLen = g.arrows.every(ar => Math.hypot(ar.b.x - ar.a.x, ar.b.y - ar.a.y) >= 0.25);
  assert(okDir && okLen, `six-node cycle: all arrows point forward and are at least 0.25 in long (node ${g.nodeW.toFixed(2)} x ${g.nodeH.toFixed(2)}, chord ${g.chord.toFixed(2)})`);
  const g4 = dk.cycleGeometry(4, 3.2, 4, 1.5, 2.0, 0.7);
  assert(g4.arrows.every(ar => Math.hypot(ar.b.x - ar.a.x, ar.b.y - ar.a.y) >= 0.25), "four-node cycle keeps visible arrows");
  console.log("themeApplied:", sp.r.themeApplied);
})().catch(e => { console.error(e); process.exitCode = 1; });
