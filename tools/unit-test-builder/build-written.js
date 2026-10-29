// Builds the written turtle-basics test (student sheet + teacher key): node build-written.js <outDir> [a|b]
// Form A reads questions-turtle-a.js, Form B questions-turtle-b.js (its META switches off the grid start arrows, sets the uniform grid and the instruction texts).
const fs = require("fs");
const path = require("path");
const D = require("docx");
const FORM = process.argv[3] || "a";
const mod = require(`./questions-turtle-${FORM}.js`);
const { qs, MIN } = mod, META = mod.META || {};
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, AlignmentType, Footer, PageNumber } = D;

const OUT = process.argv[2];
const FONT = "Arial", CODE = "Consolas", BLUE = "000000";
const HL = ["א", "ב", "ג", "ד", "ה"];

// same text helpers as build.js: «code» markers split into RTL Hebrew runs and LTR code runs
function runs(text, o = {}) {
  return text.split(/(«[^»]*»)/).filter(Boolean).map((p) => p.startsWith("«")
    ? new TextRun({ text: "‎" + p.slice(1, -1) + "‎", font: CODE, size: (o.size || 22) - 2, rightToLeft: false })
    : new TextRun({ text: p, font: FONT, size: o.size || 22, bold: o.bold, rightToLeft: true, color: o.color }));
}
const rtl = (children, o = {}) => new Paragraph({ bidirectional: true, alignment: o.align || AlignmentType.START, spacing: { before: o.before ?? 0, after: o.after ?? 60 }, keepNext: o.keepNext, keepLines: true, indent: o.indent, border: o.border, children });
const bold = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || 22, bold: true, rightToLeft: true, color: o.color });

function codeBlock(code, inCell = false) {
  const lines = code.split("\n");
  return lines.map((ln, i) => new Paragraph({
    bidirectional: false, alignment: AlignmentType.LEFT, keepNext: true, keepLines: true, spacing: { before: 0, after: 0 }, indent: inCell ? { left: 100, right: 100 } : { left: 300, right: 2400 },
    border: { left: { style: BorderStyle.SINGLE, size: 12, color: "000000", space: 4 },
      top: i === 0 ? { style: BorderStyle.SINGLE, size: 6, color: "000000", space: 2 } : undefined,
      bottom: i === lines.length - 1 ? { style: BorderStyle.SINGLE, size: 6, color: "000000", space: 2 } : undefined },
    children: [new TextRun({ text: ln || " ", font: CODE, size: 20 })],
  }));
}
const gap = (n = 80, keep = false) => new Paragraph({ spacing: { after: n }, keepNext: keep, children: [] });

function optionPara(n, text, isCode, last) {
  if (isCode) return new Paragraph({ bidirectional: false, alignment: AlignmentType.LEFT, keepLines: true, keepNext: !last, spacing: { after: last ? 160 : 40 }, indent: { left: 700 },
    children: [new TextRun({ text: n + ")  ", font: FONT, size: 22, bold: true }), new TextRun({ text: text, font: CODE, size: 20 })] });
  return rtl([new TextRun({ text: n + ")  ", font: FONT, size: 22, bold: true, rightToLeft: true }), ...runs(text)], { indent: { start: 700 }, after: last ? 160 : 40, keepNext: !last });
}

// answer area: ruled lines (text answers) or an empty box (code), as one-column tables so borders do not merge
const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const lineB = { style: BorderStyle.DOTTED, size: 6, color: "000000" };
const boxB = { style: BorderStyle.SINGLE, size: 8, color: "000000" };
function answerArea(it) {
  const W = 8800, code = it.kind === "code";
  const rows = code ? 1 : it.lines;
  const rowH = code ? it.lines * 400 : 480;
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], alignment: AlignmentType.LEFT, indent: { size: 300, type: WidthType.DXA },
    rows: Array.from({ length: rows }, (_, ri) => new TableRow({ cantSplit: true, height: { value: rowH, rule: "atLeast" }, children: [new TableCell({ width: { size: W, type: WidthType.DXA },
      borders: code ? { top: boxB, bottom: boxB, left: boxB, right: boxB } : { top: none, left: none, right: none, bottom: lineB },
      children: [new Paragraph({ spacing: { after: 0 }, keepNext: ri < rows - 1, children: [] })] })] })) });
}

// drawing grid: d = { cols, rows, start: [col, row], cell } (cell = turtle steps per square). The start square holds an arrow
// showing where the turtle stands and which way it faces (the turtle always starts facing right).
const gb = { style: BorderStyle.SINGLE, size: 6, color: "000000" };
const ARROW = { right: "→", up: "↑", left: "←", down: "↓" };
const VEC = { right: [1, 0], up: [0, -1], left: [-1, 0], down: [0, 1] };
const LEFT_OF = { right: "up", up: "left", left: "down", down: "right" };
const RIGHT_OF = { right: "down", down: "left", left: "up", up: "right" };

// walks the code on the grid; returns the squares drawn through and where the turtle ends (throws if it leaves the grid or a step is not a whole number of squares)
function walk(code, d) {
  let [c, r] = d.start, head = "right", pen = true;
  const drawn = new Set(), inside = () => c >= 0 && c < d.cols && r >= 0 && r < d.rows;
  for (const ln of code.split("\n")) {
    const [, cmd, n] = ln.match(/^turtle\.(\w+)\((\d*)\)$/);
    if (cmd === "left") head = LEFT_OF[head];
    else if (cmd === "right") head = RIGHT_OF[head];
    else if (cmd === "penup") pen = false;
    else if (cmd === "pendown") pen = true;
    else {
      if (n % d.cell) throw new Error("step not a whole number of squares: " + ln);
      for (let i = 0; i < n / d.cell; i++) {
        if (pen) drawn.add(c + "," + r);
        c += VEC[head][0]; r += VEC[head][1];
        if (!inside()) throw new Error("leaves the grid: " + code);
        if (pen) drawn.add(c + "," + r);
      }
    }
  }
  return { drawn, end: [c, r], head };
}

// key = a walk() result: shades the drawn squares, marks the start with a dot and the end with a red arrow
function grid(d, o = {}) {
  const W = o.W || 560, key = o.key, [sc, sr] = d.start;
  return new Table({ width: { size: W * d.cols, type: WidthType.DXA }, columnWidths: Array(d.cols).fill(W), alignment: AlignmentType.LEFT, indent: { size: o.indent ?? 0, type: WidthType.DXA }, visuallyRightToLeft: true,
    rows: Array.from({ length: d.rows }, (_, r) => new TableRow({ cantSplit: true, height: { value: W, rule: "exact" }, children: Array.from({ length: d.cols }, (_, i) => {
      const c = d.cols - 1 - i; // the table is forced right-to-left (so Word and LibreOffice agree): the first cell is the rightmost column
      let text = "", color = "000000", fill;
      if (!key && !META.noStartArrow && c === sc && r === sr) text = ARROW.right;
      if (key) {
        if (key.drawn.has(c + "," + r)) fill = "BFBFBF";
        if (c === sc && r === sr) text = "●";
        if (c === key.end[0] && r === key.end[1]) { text = ARROW[key.head]; color = "000000"; }
      }
      return new TableCell({ width: { size: W, type: WidthType.DXA }, borders: { top: gb, bottom: gb, left: gb, right: gb }, verticalAlign: "center",
        shading: fill ? { type: ShadingType.CLEAR, fill, color: "auto" } : undefined,
        children: [new Paragraph({ bidirectional: false, alignment: AlignmentType.CENTER, spacing: { after: 0 }, keepNext: r < d.rows - 1, children: [new TextRun({ text, font: FONT, size: o.fs || 32, bold: true, color })] })] });
    }) })) });
}

// code on the right, empty grid on the left (the table is visually right-to-left, so the first cell sits on the right)
const noB = { top: none, bottom: none, left: none, right: none };
function splitBox(it) {
  const d = it.draw, CW = 2900, GW = 6500;
  return new Table({ width: { size: CW + GW, type: WidthType.DXA }, columnWidths: [CW, GW], alignment: AlignmentType.LEFT, indent: { size: 300, type: WidthType.DXA }, visuallyRightToLeft: true,
    rows: [new TableRow({ cantSplit: true, children: [
      new TableCell({ width: { size: CW, type: WidthType.DXA }, borders: noB, verticalAlign: "center", margins: { right: 100 }, children: codeBlock(it.code, true) }),
      new TableCell({ width: { size: GW, type: WidthType.DXA }, borders: noB, margins: { left: 200 }, children: [grid(d, { W: 500 }),
        new Paragraph({ bidirectional: true, spacing: { before: 40, after: 0 }, children: runs(`כל משבצת = ${d.cell} צעדים של הצב`, { size: 19 }) })] }),
    ] })] });
}
const DRAW_NOTE = META.drawNote || "ציירו ברשת את מה שהקוד מצייר, וסיימו בחץ שמראה היכן הצב עומד ולאן הוא פונה.";

// Form B rule: every grid has the same size, and every drawing fits it with room to choose a start (checked on the model walk)
if (META.grid) qs.forEach((q) => q.items.forEach((it) => {
  const d = it.draw; if (!d) return;
  for (const k of ["cols", "rows", "cell"]) if (d[k] !== META.grid[k]) throw new Error(`grid ${k} differs: ${it.t.slice(0, 30)}`);
  const w = walk(it.code, d), cs = [], rs = [];
  w.drawn.forEach((x) => { const [c, r] = x.split(",").map(Number); cs.push(c); rs.push(r); });
  const ww = Math.max(...cs) - Math.min(...cs), hh = Math.max(...rs) - Math.min(...rs);
  if (ww > META.maxMoves.w || hh > META.maxMoves.h) throw new Error(`drawing too big (${ww}x${hh}): ${it.t.slice(0, 30)}`);
}));

const qpts = (q) => q.items.reduce((a, i) => a + i.pts, 0);
const total = qs.reduce((s, q) => s + qpts(q), 0);

// worked example for the instructions page: the code, the empty grid with its start arrow, and the same grid solved (line shaded, big arrow = where the turtle ends)
function workedExample() {
  const ex = META.example, d = ex ? { ...META.grid, start: ex.start } : { cols: 6, rows: 3, start: [1, 0], cell: 50 };
  const code = (ex ? ex.code : ["turtle.forward(100)", "turtle.right(90)", "turtle.forward(50)"]).join("\n"), gw = ex ? 300 : 400, cw = d.cols * gw + 200;
  const cellOf = (w, kids) => new TableCell({ width: { size: w, type: WidthType.DXA }, borders: noB, verticalAlign: "center", margins: { left: 100, right: 100 }, children: kids });
  const cap = (t) => new Paragraph({ bidirectional: true, spacing: { before: 40, after: 0 }, children: runs(t, { size: 19 }) });
  const left = 9300 - 2 * cw;
  return new Table({ width: { size: left + 2 * cw, type: WidthType.DXA }, columnWidths: [left, cw, cw], alignment: AlignmentType.LEFT, indent: { size: 300, type: WidthType.DXA }, visuallyRightToLeft: true,
    rows: [new TableRow({ cantSplit: true, children: [
      cellOf(left, codeBlock(code, true)),
      cellOf(cw, [grid(d, { W: gw, fs: ex ? 20 : 32 }), cap(ex ? "לפני: הרשת שמקבלים (בלי חץ)" : "לפני: הרשת שמקבלים")]),
      cellOf(cw, [grid(d, { W: gw, fs: ex ? 20 : 32, key: walk(code, d) }), cap("אחרי: הציור (הקו באפור)")]),
    ] })] });
}

function buildTest() {
  const kids = [];
  kids.push(rtl([bold("מבחן – פקודות Turtle בסיסיות", { size: 36 })], { align: AlignmentType.CENTER, after: 60 }));
  kids.push(rtl([new TextRun({ text: META.subtitle || "פייתון א׳ · כיתות ז׳–ח׳", font: FONT, size: 24, rightToLeft: true, color: "000000" })], { align: AlignmentType.CENTER, after: 200 }));
  kids.push(rtl(runs("שם: ______________________     כיתה: ________     תאריך: ____________"), { after: 160 }));
  kids.push(rtl([bold("הוראות – קראו לפני שמתחילים")], { after: 60, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "999999", space: 2 } } }));
  const ins = META.ins || [
    "משך המבחן: 60 דקות. יש 6 שאלות, ובכל שאלה כמה סעיפים. סך הכול 100 נקודות. מספר הנקודות כתוב ליד כל סעיף.",
    "כל סעיף עומד בפני עצמו: הוא מביא איתו את הקוד ואת נקודת ההתחלה שלו. אם לא הצלחתם סעיף, עברו לבא אחריו.",
    "אלא אם כתוב אחרת, בכל הקודים הצב מתחיל באמצע החלון, פונה ימינה, והעט למטה (הוא מצייר).",
    "הפקודות במבחן: «turtle.forward(100)», «turtle.left(90)», «turtle.right(90)», «turtle.penup()», «turtle.pendown()». כותבים כל פקודה בשורה נפרדת, ומספרים בלי מרכאות. אין צורך לכתוב «import turtle» ולא «turtle.done()».",
    "רמזים: ימין ושמאל הם של הצב, לא של המסך (כשהצב פונה למטה, «left(90)» מפנה אותו ימינה על המסך). פנייה מסובבת את הצב במקום, בלי לזוז ובלי לצייר. «penup()» מרימה את העט, כך שהצב זז בלי לצייר, ו-«pendown()» מורידה אותו שוב. מותר לשרבט על הדף.",
    "ציור ברשת: החץ שבתוך הרשת הוא הצב בתחילת הסעיף, והוא פונה לכיוון שהחץ מראה. ליד כל רשת כתוב כמה צעדים שווה משבצת אחת. מציירים קווים ממרכז משבצת למרכז משבצת, ובסוף מציירים חץ במקום שבו הצב עומד, בכיוון שאליו הוא פונה. דוגמה בהמשך.",
    "בשאלות בחירה מרובה: סמנו בעיגול מספר אחד. בשאלות כתיבה: אפשר לקבל נקודות גם על קוד חלקי, ולכן כתבו מה שהצלחתם. כל קוד שונה מהמצופה שפותר את המשימה מתקבל.",
  ];
  ins.forEach((t, i) => kids.push(rtl([new TextRun({ text: (i + 1) + ".  ", font: FONT, size: 21, rightToLeft: true }), ...runs(t, { size: 21 })], { indent: { start: 360, hanging: 360 }, after: 50 })));
  kids.push(rtl([bold("דוגמה לציור ברשת (משבצת = 50 צעדים)")], { before: 120, after: 60, keepNext: true }));
  kids.push(workedExample());
  kids.push(rtl(runs(META.exampleText || "«forward(100)» הוא קו של 2 משבצות ימינה. «right(90)» מפנה את הצב למטה. «forward(50)» הוא קו של משבצת אחת למטה. הצב מסיים בחץ שפונה למטה."), { before: 60, indent: { start: 360 } }));

  qs.forEach((q, qi) => {
    kids.push(rtl([bold(`שאלה ${qi + 1}  ·  ${q.title}  (${qpts(q)} נקודות)`, { size: 26, color: BLUE })], { before: 280, after: 120, keepNext: true, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: BLUE, space: 2 } } }));
    q.items.forEach((it, k) => {
      kids.push(rtl([bold(HL[k] + ".  "), ...runs(it.t), bold(`   (${it.pts} נק׳)`, { size: 20, color: "000000" })], { keepNext: true, before: 100, after: 80, indent: { start: 360, hanging: 360 } }));
      if (it.draw && it.kind !== "grid") {
        kids.push(rtl([new TextRun({ text: it.drawNote || DRAW_NOTE, font: FONT, size: 20, rightToLeft: true, bold: true })], { keepNext: true, indent: { start: 360 }, after: 60 }));
        kids.push(splitBox(it)); kids.push(gap(100, true));
      } else if (it.code) kids.push(...codeBlock(it.code));
      if (it.kind === "mc") it.options.forEach((t, j) => kids.push(optionPara(j + 1, t, !!it.codeOpts, j === 3)));
      else if (it.kind === "grid") {
        kids.push(gap(100, true)); kids.push(grid(it.draw, { indent: 300 }));
        kids.push(rtl(runs(`כל משבצת = ${it.draw.cell} צעדים של הצב`, { size: 19 }), { before: 40, indent: { start: 300 } })); kids.push(gap(100));
      }
      else { kids.push(gap(40, true)); kids.push(answerArea(it)); kids.push(gap(120)); }
    });
  });
  kids.push(rtl([bold("בהצלחה!", { size: 24 })], { align: AlignmentType.CENTER, before: 240 }));
  return kids;
}

// ---------------- teacher key ----------------
const cb = { style: BorderStyle.SINGLE, size: 4, color: "BBBBBB" };
function cell(text, w, o = {}) {
  const paras = String(text).split("\n").map((ln) => ln.startsWith("turtle.") && o.code
    ? new Paragraph({ bidirectional: false, alignment: AlignmentType.LEFT, spacing: { after: 0 }, children: [new TextRun({ text: ln, font: CODE, size: 18 })] })
    : new Paragraph({ bidirectional: true, alignment: o.center ? AlignmentType.CENTER : AlignmentType.START, spacing: { after: 0 }, children: runs(ln, { size: o.size || 19, bold: o.bold }) }));
  return new TableCell({ width: { size: w, type: WidthType.DXA }, borders: { top: cb, bottom: cb, left: cb, right: cb }, margins: { top: 50, bottom: 50, left: 80, right: 80 },
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined, children: paras });
}
function table(widths, header, rows, o = {}) {
  return new Table({ width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: widths, visuallyRightToLeft: true,
    rows: [new TableRow({ tableHeader: true, children: header.map((hd, i) => cell(hd, widths[i], { bold: true, fill: "D9D9D9", center: true })) }),
      ...rows.map((r) => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, widths[i], { center: o.centerCols?.includes(i), bold: o.boldCols?.includes(i), code: o.codeCols?.includes(i) })) }))] });
}
const h = (t, s = 28) => rtl([bold(t, { size: s, color: BLUE })], { before: 200, after: 100, keepNext: true });

function buildKey() {
  const kids = [];
  kids.push(rtl([bold(META.keyTitle || "מפתח תשובות ומפרט – מבחן Turtle בסיסי", { size: 34 })], { align: AlignmentType.CENTER, after: 40 }));
  kids.push(rtl([new TextRun({ text: "לשימוש המורה בלבד", font: FONT, size: 22, rightToLeft: true, color: "000000" })], { align: AlignmentType.CENTER, after: 160 }));

  kids.push(h("מפרט המבחן"));
  const types = ["בחירה מרובה", "בחירה מרובה", "ניתוח קוד", "ניתוח קוד", "כתיבת קוד", "כתיבת קוד"];
  kids.push(table([600, 2400, 1700, 1200, 1500, 1600], ["#", "נושא", "סוג", "סעיפים", "נקודות", "זמן מוערך (דקות)"],
    qs.map((q, i) => [i + 1, q.title, types[i], q.items.length, qpts(q), MIN[i]]).concat([["", "סך הכול", "", qs.reduce((a, q) => a + q.items.length, 0), total, MIN.reduce((a, b) => a + b, 0)]]),
    { centerCols: [0, 3, 4, 5] }));
  kids.push(rtl(runs("כל סעיף עומד בפני עצמו (מקבל קוד ונקודת התחלה משלו), כדי שתלמיד שטעה בסעיף אחד עדיין יוכל לצבור נקודות בשאר השאלה. בסעיפי הכתיבה והניתוח הפתוחים מחלקים ניקוד חלקי לפי הטבלאות."), { before: 100, after: 60 }));
  kids.push(rtl(runs("הזמן המוערך הוא לתלמיד ממוצע. ההערכה מבוססת על מבנה המבחן ולא על נתונים, ולכן כדאי לבדוק אותה אחרי המבחן הראשון."), { after: 60 }));
  (META.keyNotes || []).forEach((t) => kids.push(rtl(runs(t), { after: 60 })));
  kids.push(rtl(runs("בדיקה: קוד שונה מהמפתח שפותר את המשימה מקבל ניקוד מלא. טעות קטנה (למשל, פנייה לכיוון הלא נכון) פוגעת רק בשורת הניקוד שלה. חוסר ב-«turtle.» לפני הפקודה אינו מוריד נקודות."), { after: 60 }));

  qs.forEach((q, qi) => {
    kids.push(h(`שאלה ${qi + 1} · ${q.title} (${qpts(q)} נק׳)`, 26));
    const bullets = (r) => r.map(([t, p]) => `• ${t} (${p})`).join("\n");
    const rows = q.items.map((it, k) => it.kind === "mc"
      ? [HL[k], it.pts, "תשובה " + (it.ans + 1) + "\n" + it.options[it.ans] + (it.draw ? "\nציור: " + it.draw.model : ""),
        (it.draw ? `בחירה: ${it.pts - it.draw.pts} נק׳, ציור: ${it.draw.pts} נק׳\n${bullets(it.draw.rubric)}\n` : "") + it.why]
      : [HL[k], it.pts, it.model + (it.draw ? "\nציור: " + it.draw.model : ""), bullets(it.rubric) + "\n" + it.why]);
    kids.push(table([600, 800, 3900, 3700], ["סעיף", "נק׳", "תשובה / פתרון לדוגמה", q.items[0].kind === "mc" ? "הסבר" : "חלוקת ניקוד והסבר"], rows, { centerCols: [0, 1], codeCols: [2] }));
  });
  kids.push(h("ציורים לדוגמה: סעיפים עם רשת"));
  kids.push(rtl(runs("משבצות אפורות = מה שמצויר. ● = נקודת ההתחלה" + (META.noStartArrow ? " (מיקום לדוגמה)" : "") + ". החץ הגדול = היכן הצב עומד ולאן הוא פונה בסוף."), { after: 80 }));
  const drawn = [];
  qs.forEach((q, qi) => q.items.forEach((it, k) => { if (it.draw) drawn.push([`שאלה ${qi + 1}${HL[k]}  ·  משבצת = ${it.draw.cell} צעדים`, it.draw, walk(it.draw.code || it.code, it.draw)]); }));
  const half = (e) => new TableCell({ width: { size: 4700, type: WidthType.DXA }, borders: noB, margins: { bottom: 160 }, children: e
    ? [rtl(runs(e[0], { bold: true, size: 20 }), { after: 40, keepNext: true }), grid(e[1], { W: 380, key: e[2] }), new Paragraph({ children: [] })]
    : [new Paragraph({ children: [] })] });
  const drows = [];
  for (let i = 0; i < drawn.length; i += 2) drows.push(new TableRow({ cantSplit: true, children: [half(drawn[i]), half(drawn[i + 1])] }));
  kids.push(new Table({ width: { size: 9400, type: WidthType.DXA }, columnWidths: [4700, 4700], visuallyRightToLeft: true, rows: drows }));
  kids.push(h("פתרונות לדוגמה: סעיפי כתיבת קוד"));
  qs.forEach((q, qi) => q.items.forEach((it, k) => {
    if (it.kind === "code") {
      kids.push(rtl(runs(`שאלה ${qi + 1}${HL[k]}`, { bold: true }), { before: 100, after: 20, keepNext: true }));
      kids.push(...codeBlock(it.model));
    }
  }));
  return kids;
}

const common = { styles: { default: { document: { run: { font: FONT, size: 22 } } } } };
const page = { size: { width: 11906, height: 16838 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } };
const footer = (label) => new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: label + "  ·  עמוד ", font: FONT, size: 18, color: "777777", rightToLeft: true }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18, color: "777777" })] })] });

(async () => {
  const test = new Document({ ...common, sections: [{ properties: { page, bidi: true }, footers: { default: footer(META.footer || "מבחן Turtle בסיסי") }, children: buildTest() }] });
  const key = new Document({ ...common, sections: [{ properties: { page, bidi: true }, footers: { default: footer("מפתח תשובות – למורה") }, children: buildKey() }] });
  fs.writeFileSync(path.join(OUT, `u2-turtle-test-${FORM}-students-he.docx`), await Packer.toBuffer(test));
  fs.writeFileSync(path.join(OUT, `u2-turtle-test-${FORM}-key-he.docx`), await Packer.toBuffer(key));
  console.log("ok");
})();
