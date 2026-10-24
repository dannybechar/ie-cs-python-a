// Builds the written turtle-basics test (student sheet + teacher key) from questions-turtle-a.js
const fs = require("fs");
const path = require("path");
const D = require("docx");
const { qs, MIN } = require("./questions-turtle-a.js");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, AlignmentType, Footer, PageNumber } = D;

const OUT = process.argv[2];
const FONT = "Arial", CODE = "Consolas", BLUE = "1F4E79";
const HL = ["א", "ב", "ג", "ד", "ה"];

// same text helpers as build.js: «code» markers split into RTL Hebrew runs and LTR code runs
function runs(text, o = {}) {
  return text.split(/(«[^»]*»)/).filter(Boolean).map((p) => p.startsWith("«")
    ? new TextRun({ text: "‎" + p.slice(1, -1) + "‎", font: CODE, size: (o.size || 22) - 2, rightToLeft: false })
    : new TextRun({ text: p, font: FONT, size: o.size || 22, bold: o.bold, rightToLeft: true, color: o.color }));
}
const rtl = (children, o = {}) => new Paragraph({ bidirectional: true, alignment: o.align || AlignmentType.START, spacing: { before: o.before ?? 0, after: o.after ?? 60 }, keepNext: o.keepNext, keepLines: true, indent: o.indent, border: o.border, children });
const bold = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || 22, bold: true, rightToLeft: true, color: o.color });

function codeBlock(code) {
  const lines = code.split("\n");
  return lines.map((ln, i) => new Paragraph({
    bidirectional: false, alignment: AlignmentType.LEFT, keepNext: true, keepLines: true, spacing: { before: 0, after: 0 }, indent: { left: 300, right: 2400 },
    shading: { type: ShadingType.CLEAR, fill: "F2F2F2", color: "auto" },
    border: { left: { style: BorderStyle.SINGLE, size: 6, color: "999999", space: 4 },
      top: i === 0 ? { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 2 } : undefined,
      bottom: i === lines.length - 1 ? { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 2 } : undefined },
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
const lineB = { style: BorderStyle.DOTTED, size: 6, color: "888888" };
const boxB = { style: BorderStyle.SINGLE, size: 6, color: "999999" };
function answerArea(it) {
  const W = 8800, code = it.kind === "code";
  const rows = code ? 1 : it.lines;
  const rowH = code ? it.lines * 400 : 480;
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], alignment: AlignmentType.LEFT, indent: { size: 300, type: WidthType.DXA },
    rows: Array.from({ length: rows }, (_, ri) => new TableRow({ cantSplit: true, height: { value: rowH, rule: "atLeast" }, children: [new TableCell({ width: { size: W, type: WidthType.DXA },
      borders: code ? { top: boxB, bottom: boxB, left: boxB, right: boxB } : { top: none, left: none, right: none, bottom: lineB },
      children: [new Paragraph({ spacing: { after: 0 }, keepNext: ri < rows - 1, children: [] })] })] })) });
}

// drawing grid: 8 columns x 5 rows, start dot at column 2, row 2
const gb = { style: BorderStyle.SINGLE, size: 4, color: "AAAAAA" };
function grid() {
  const W = 560, cols = 8, rows = 5;
  return new Table({ width: { size: W * cols, type: WidthType.DXA }, columnWidths: Array(cols).fill(W), alignment: AlignmentType.LEFT, indent: { size: 300, type: WidthType.DXA },
    rows: Array.from({ length: rows }, (_, r) => new TableRow({ cantSplit: true, height: { value: W, rule: "exact" }, children: Array.from({ length: cols }, (_, c) => new TableCell({
      width: { size: W, type: WidthType.DXA }, borders: { top: gb, bottom: gb, left: gb, right: gb }, verticalAlign: "center",
      children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, keepNext: r < rows - 1, children: [new TextRun({ text: r === 1 && c === 1 ? "●" : "", font: FONT, size: 28 })] })] })) })) });
}

const qpts = (q) => q.items.reduce((a, i) => a + i.pts, 0);
const total = qs.reduce((s, q) => s + qpts(q), 0);

function buildTest() {
  const kids = [];
  kids.push(rtl([bold("מבחן – פקודות Turtle בסיסיות", { size: 36 })], { align: AlignmentType.CENTER, after: 60 }));
  kids.push(rtl([new TextRun({ text: "פייתון א׳ · כיתות ז׳–ח׳", font: FONT, size: 24, rightToLeft: true, color: "555555" })], { align: AlignmentType.CENTER, after: 200 }));
  kids.push(rtl(runs("שם: ______________________     כיתה: ________     תאריך: ____________"), { after: 160 }));
  kids.push(rtl([bold("הוראות – קראו לפני שמתחילים")], { after: 60, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "999999", space: 2 } } }));
  const ins = [
    "משך המבחן: 60 דקות. יש 6 שאלות, ובכל שאלה כמה סעיפים. סך הכול 100 נקודות. מספר הנקודות כתוב ליד כל סעיף.",
    "כל סעיף עומד בפני עצמו: הוא מביא איתו את הקוד ואת נקודת ההתחלה שלו. אם לא הצלחתם סעיף, עברו לבא אחריו. אפשר לקבל נקודות בכל סעיף גם אם טעיתם בקודם.",
    "אלא אם כתוב אחרת, בכל הקודים הצב מתחיל באמצע החלון, פונה ימינה, והעט למטה (הוא מצייר).",
    "הפקודות במבחן: «turtle.forward(100)», «turtle.left(90)», «turtle.right(90)», «turtle.penup()», «turtle.pendown()». המספר בסוגריים הוא מרחק (ב-forward) או זווית (ב-left וב-right). כותבים כל פקודה בשורה נפרדת, ומספרים בלי מרכאות. אין צורך לכתוב «import turtle» ולא «turtle.done()».",
    "רמזים שיעזרו לכם: ימין ושמאל הם של הצב, לא של המסך (כשהצב פונה למטה, «left(90)» מפנה אותו ימינה על המסך). פנייה מסובבת את הצב במקום, בלי לזוז ובלי לצייר. ריבוע הוא 4 צלעות שוות ו-4 פניות של 90 מעלות. «penup()» מרימה את העט, כך שהצב זז בלי לצייר, ו-«pendown()» מורידה אותו שוב.",
    "מותר ומומלץ לשרבט על הדף: למשל, לצייר חץ שמראה לאן הצב פונה אחרי כל פקודה.",
    "בשאלות בחירה מרובה: סמנו בעיגול מספר אחד. בשאלות כתיבה: אפשר לקבל נקודות גם על קוד חלקי, ולכן כתבו מה שהצלחתם. כל קוד שונה מהמצופה שפותר את המשימה מתקבל.",
  ];
  ins.forEach((t, i) => kids.push(rtl([new TextRun({ text: (i + 1) + ".  ", font: FONT, size: 21, rightToLeft: true }), ...runs(t, { size: 21 })], { indent: { start: 360, hanging: 360 }, after: 50 })));

  qs.forEach((q, qi) => {
    kids.push(rtl([bold(`שאלה ${qi + 1}  ·  ${q.title}  (${qpts(q)} נקודות)`, { size: 24, color: BLUE })], { before: 280, after: 120, keepNext: true, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: BLUE, space: 2 } } }));
    q.items.forEach((it, k) => {
      kids.push(rtl([bold(HL[k] + ".  "), ...runs(it.t), bold(`   (${it.pts} נק׳)`, { size: 20, color: "555555" })], { keepNext: true, before: 100, after: 80, indent: { start: 360, hanging: 360 } }));
      if (it.code) kids.push(...codeBlock(it.code));
      if (it.kind === "mc") it.options.forEach((t, j) => kids.push(optionPara(j + 1, t, !!it.codeOpts, j === 3)));
      else if (it.kind === "grid") { kids.push(gap(100, true)); kids.push(grid()); kids.push(gap(100)); }
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
    rows: [new TableRow({ tableHeader: true, children: header.map((hd, i) => cell(hd, widths[i], { bold: true, fill: "DCE6F1", center: true })) }),
      ...rows.map((r) => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, widths[i], { center: o.centerCols?.includes(i), bold: o.boldCols?.includes(i), code: o.codeCols?.includes(i) })) }))] });
}
const h = (t, s = 28) => rtl([bold(t, { size: s, color: BLUE })], { before: 200, after: 100, keepNext: true });

function buildKey() {
  const kids = [];
  kids.push(rtl([bold("מפתח תשובות ומפרט – מבחן Turtle בסיסי", { size: 34 })], { align: AlignmentType.CENTER, after: 40 }));
  kids.push(rtl([new TextRun({ text: "לשימוש המורה בלבד", font: FONT, size: 22, rightToLeft: true, color: "C00000" })], { align: AlignmentType.CENTER, after: 160 }));

  kids.push(h("מפרט המבחן"));
  const types = ["בחירה מרובה", "בחירה מרובה", "ניתוח קוד", "ניתוח קוד", "כתיבת קוד", "כתיבת קוד"];
  kids.push(table([600, 2400, 1700, 1200, 1500, 1600], ["#", "נושא", "סוג", "סעיפים", "נקודות", "זמן מוערך (דקות)"],
    qs.map((q, i) => [i + 1, q.title, types[i], q.items.length, qpts(q), MIN[i]]).concat([["", "סך הכול", "", qs.reduce((a, q) => a + q.items.length, 0), total, MIN.reduce((a, b) => a + b, 0)]]),
    { centerCols: [0, 3, 4, 5] }));
  kids.push(rtl(runs("כל סעיף עומד בפני עצמו (מקבל קוד ונקודת התחלה משלו), כדי שתלמיד שטעה בסעיף אחד עדיין יוכל לצבור נקודות בשאר השאלה. בסעיפי הכתיבה והניתוח הפתוחים מחלקים ניקוד חלקי לפי הטבלאות."), { before: 100, after: 60 }));
  kids.push(rtl(runs("הזמן המוערך הוא לתלמיד ממוצע. ההערכה מבוססת על מבנה המבחן ולא על נתונים, ולכן כדאי לבדוק אותה אחרי המבחן הראשון."), { after: 60 }));
  kids.push(rtl(runs("בדיקה: קוד שונה מהמפתח שפותר את המשימה מקבל ניקוד מלא. טעות קטנה (למשל, פנייה לכיוון הלא נכון) פוגעת רק בשורת הניקוד שלה. חוסר ב-«turtle.» לפני הפקודה אינו מוריד נקודות."), { after: 60 }));

  qs.forEach((q, qi) => {
    kids.push(h(`שאלה ${qi + 1} · ${q.title} (${qpts(q)} נק׳)`, 26));
    const rows = q.items.map((it, k) => it.kind === "mc"
      ? [HL[k], it.pts, "תשובה " + (it.ans + 1) + "\n" + it.options[it.ans], it.why]
      : [HL[k], it.pts, it.model, it.rubric.map(([t, p]) => `• ${t} (${p})`).join("\n") + "\n" + it.why]);
    kids.push(table([600, 800, 3900, 3700], ["סעיף", "נק׳", "תשובה / פתרון לדוגמה", q.items[0].kind === "mc" ? "הסבר" : "חלוקת ניקוד והסבר"], rows, { centerCols: [0, 1], codeCols: [2] }));
  });
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
  const test = new Document({ ...common, sections: [{ properties: { page, bidi: true }, footers: { default: footer("מבחן Turtle בסיסי") }, children: buildTest() }] });
  const key = new Document({ ...common, sections: [{ properties: { page, bidi: true }, footers: { default: footer("מפתח תשובות – למורה") }, children: buildKey() }] });
  fs.writeFileSync(path.join(OUT, "u2-turtle-test-a-students-he.docx"), await Packer.toBuffer(test));
  fs.writeFileSync(path.join(OUT, "u2-turtle-test-a-key-he.docx"), await Packer.toBuffer(key));
  console.log("ok");
})();
