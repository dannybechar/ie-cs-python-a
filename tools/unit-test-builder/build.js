const fs = require("fs");
const path = require("path");
const D = require("docx");
const { q, L } = require(process.env.QFILE || "./questions-a.js");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, AlignmentType, Footer, PageNumber } = D;

const OUT = process.argv[2];
const VER = process.env.VER || "";   // e.g. "B"
const VLABEL = VER === "B" ? " · גרסה ב׳" : "";
const TAG = VER === "B" ? "b" : "a";
const FONT = "Arial", CODE = "Consolas";
const NAMES = { 1: "יחידה 2.1 – צעדים ראשונים", 2: "יחידה 2.2 – עט, מראה וחותמות", 3: "יחידה 2.3 – אתגר הגאומטריה" };

// split text on «code» markers into RTL Hebrew runs and LTR code runs
function runs(text, o = {}) {
  const parts = text.split(/(«[^»]*»)/).filter(Boolean);
  return parts.map((p) => p.startsWith("«")
    ? new TextRun({ text: "‎" + p.slice(1, -1) + "‎", font: CODE, size: (o.size || 22) - 2, rightToLeft: false, bold: false })
    : new TextRun({ text: p, font: FONT, size: o.size || 22, bold: o.bold, rightToLeft: true, color: o.color }));
}
const rtl = (children, o = {}) => new Paragraph({ bidirectional: true, alignment: o.align || AlignmentType.START, spacing: { before: o.before ?? 0, after: o.after ?? 60, line: o.line }, keepNext: o.keepNext, keepLines: true, indent: o.indent, border: o.border, shading: o.shading, children });

function codeBlock(code) {
  const lines = code.split("\n");
  return lines.map((ln, i) => new Paragraph({
    bidirectional: false, alignment: AlignmentType.LEFT, keepNext: true, keepLines: true,
    spacing: { before: 0, after: 0 }, indent: { left: 300, right: 2400 },
    shading: { type: ShadingType.CLEAR, fill: "F2F2F2", color: "auto" },
    border: {
      left: { style: BorderStyle.SINGLE, size: 6, color: "999999", space: 4 },
      top: i === 0 ? { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 2 } : undefined,
      bottom: i === lines.length - 1 ? { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 2 } : undefined,
    },
    children: [new TextRun({ text: ln || " ", font: CODE, size: 20 })],
  }));
}

function optionPara(letter, text, isCode, last, first) {
  if (isCode) return new Paragraph({ bidirectional: false, alignment: AlignmentType.LEFT, keepLines: true, keepNext: !last, spacing: { before: first ? 80 : 0, after: last ? 200 : 40 }, indent: { left: 700 },
    children: [new TextRun({ text: letter + "‎.  ", font: FONT, size: 22, bold: true }), new TextRun({ text: "‎" + text, font: CODE, size: 20 })] });
  return rtl([new TextRun({ text: letter + ".  ", font: FONT, size: 22, bold: true, rightToLeft: true }), ...runs(text)], { indent: { start: 360 }, before: first ? 80 : 0, after: last ? 200 : 40, keepNext: !last });
}

function buildTest() {
  const kids = [];
  kids.push(rtl([new TextRun({ text: "מבחן – יחידה 2: Turtle וגרפיקה" + VLABEL, font: FONT, size: 36, bold: true, rightToLeft: true })], { align: AlignmentType.CENTER, after: 60 }));
  kids.push(rtl([new TextRun({ text: "פייתון א׳ · כיתות ז׳–ח׳", font: FONT, size: 24, rightToLeft: true, color: "555555" })], { align: AlignmentType.CENTER, after: 200 }));
  kids.push(rtl(runs("שם: ______________________     כיתה: ________     תאריך: ____________"), { after: 160 }));
  kids.push(rtl(runs("הוראות", { bold: true }), { after: 40, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "999999", space: 2 } } }));
  const ins = [
    "משך המבחן: 45 דקות. 25 שאלות, בכל שאלה תשובה נכונה אחת. כל שאלה שווה 4 נקודות (סה״כ 100).",
    "סמנו בעיגול את האות של התשובה הנכונה ביותר. אם טעיתם, מחקו את הסימון ברור וסמנו מחדש.",
    "אין להשתמש במחשב, במחברת או בשיעורי בית. שרבוט וציור על הדף מותרים ואף מומלצים (למשל, לצייר חץ כיוון).",
    "כל התוכניות בשאלות רצות מנקודת ההתחלה הרגילה: הצב באמצע החלון ופונה ימינה. «import turtle» בתחילת הקוד ו-«turtle.done()» בסופו מושמטים.",
    "אל תתעכבו על שאלה אחת. סמנו אותה, עברו הלאה וחזרו אליה בסוף.",
  ];
  ins.forEach((t, i) => kids.push(rtl([new TextRun({ text: (i + 1) + ".  ", font: FONT, size: 21, rightToLeft: true }), ...runs(t, { size: 21 })], { indent: { start: 360, hanging: 360 }, after: 40 })));
  kids.push(rtl([], { after: 120 }));

  let lastM = 0;
  q.forEach((o, i) => {
    if (o.m !== lastM) {
      lastM = o.m;
      kids.push(rtl([new TextRun({ text: "חלק " + ["א", "ב", "ג"][o.m - 1] + "  ·  " + NAMES[o.m], font: FONT, size: 24, bold: true, rightToLeft: true, color: "1F4E79" })], { before: 200, after: 120, keepNext: true, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "1F4E79", space: 2 } } }));
    }
    kids.push(rtl([new TextRun({ text: (i + 1) + ".  ", font: FONT, size: 22, bold: true, rightToLeft: true }), ...runs(o.t)], { keepNext: true, before: 120, after: 80, indent: { start: 360, hanging: 360 } }));
    if (o.code) kids.push(...codeBlock(o.code));
    o.options.forEach((t, k) => kids.push(optionPara(L[k], t, !!o.codeOpts, k === 3, k === 0)));
  });
  kids.push(rtl([new TextRun({ text: "בהצלחה!", font: FONT, size: 24, bold: true, rightToLeft: true })], { align: AlignmentType.CENTER, before: 240 }));
  return kids;
}

// ---------------- teacher key ----------------
const cellB = { style: BorderStyle.SINGLE, size: 4, color: "BBBBBB" };
const borders = { top: cellB, bottom: cellB, left: cellB, right: cellB };
function cell(text, w, o = {}) {
  return new TableCell({ width: { size: w, type: WidthType.DXA }, borders, margins: { top: 50, bottom: 50, left: 80, right: 80 },
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined,
    children: [new Paragraph({ bidirectional: true, alignment: o.center ? AlignmentType.CENTER : AlignmentType.START, spacing: { after: 0 }, children: runs(String(text), { size: o.size || 19, bold: o.bold }) })] });
}
function table(widths, header, rows, o = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths, visuallyRightToLeft: true,
    rows: [new TableRow({ tableHeader: true, children: header.map((h, i) => cell(h, widths[i], { bold: true, fill: "DCE6F1", center: true })) }),
      ...rows.map((r) => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, widths[i], { center: o.centerCols?.includes(i), bold: o.boldCols?.includes(i) })) }))] });
}

function buildKey() {
  const kids = [];
  const h = (t, s = 28) => rtl([new TextRun({ text: t, font: FONT, size: s, bold: true, rightToLeft: true, color: "1F4E79" })], { before: 200, after: 100, keepNext: true });
  kids.push(rtl([new TextRun({ text: "מפתח תשובות ומפרט – מבחן יחידה 2" + VLABEL, font: FONT, size: 34, bold: true, rightToLeft: true })], { align: AlignmentType.CENTER, after: 40 }));
  kids.push(rtl([new TextRun({ text: "לשימוש המורה בלבד", font: FONT, size: 22, rightToLeft: true, color: "C00000" })], { align: AlignmentType.CENTER, after: 160 }));

  const dc = { A: 0, B: 0, C: 0 }, mc = { 1: 0, 2: 0, 3: 0 };
  q.forEach((o) => { dc[o.d]++; mc[o.m]++; });
  kids.push(h("מפרט המבחן"));
  kids.push(table([2500, 1900, 1200, 4100],
    ["נושא", "שאלות", "ציון לשאלה", "מקור"],
    [[NAMES[1], mc[1] + " (שאלות 1–8)", "4", VER ? "הדרכה + מעבדה: מדרגות, משולש, ריבוע" : "הדרכה + מעבדה: מדרגות, משולש"],
     [NAMES[2], mc[2] + " (שאלות 9–18)", "4", "מעבדה: Task A–D, פונקציה לכל משימה"],
     [NAMES[3], mc[3] + " (שאלות 19–25)", "4", "באג בריבוע, ריבוע למלבן, מבחן המלבן, בדיקות יציאה"]],
    { centerCols: [1, 2] }));
  kids.push(rtl([], { after: 100 }));

  kids.push(h("רמות קושי והתפלגות ציונים צפויה"));
  const tm = dc.A * 0.7 + dc.B * 1.5 + dc.C * 2.5;
  kids.push(table([1900, 1100, 1700, 4800],
    ["רמה", "שאלות", "הצלחה צפויה", "מה זה כולל"],
    [["קלה (א)", dc.A, "בערך 90%", "אוצר מילים ופקודה אחת: import, מצב התחלתי, הערה, penup, pencolor, שגיאה לוגית"],
     ["בינונית (ב)", dc.B, "בערך 72%", "מעקב בן 2–5 שורות, משולש 120°, הגדרות שנשארות, חותמות, אחזור, פונקציה לכל משימה"],
     ["קשה (ג)", dc.C, "בערך 45%", "מעקב בן 7–8 שורות או שני רעיונות יחד: מדרגות, שינוי צבע בעט למעלה, מיקום מול כיוון, מסלול משולב"]],
    { centerCols: [1, 2] }));
  const mean = (dc.A * 0.9 + dc.B * 0.72 + dc.C * 0.45) / 25;
  kids.push(rtl(runs(`ממוצע צפוי: כ-${Math.round(mean * 100)} מתוך 100. זמן פתרון מוערך לתלמיד טוב: כ-${Math.round(tm)} דקות, ועוד כ-5 דקות לבדיקה, כלומר בתוך 45 הדקות.`), { before: 80, after: 60 }));
  kids.push(rtl(runs("ציון מעל 90 דורש לכל היותר 2 טעויות מתוך 25 (92 ומעלה). כדי לעשות זאת תלמיד צריך לעבור בדיוק גם על שש השאלות הקשות, ולכן רק תלמידים שהשתתפו במעבדה וגם הקפידו על מעקב שלב אחר שלב צפויים להצליח."), { after: 60 }));
  kids.push(rtl(runs("שימו לב: זו הערכה שמבוססת על מבנה המבחן ולא על נתונים. הציון של כיתה אמיתית תלוי בכיתה. אם אחרי המבחן יותר מ-2 תלמידים מעל 90, החליפו 2–3 שאלות מרמה ב׳ בשאלות מעקב ארוכות. אם אף אחד לא מעל 90, בדקו אילו שאלות קשות נכשלו אצל כולם, כי ייתכן שמדובר בנושא שלא תורגל מספיק."), { after: 60 }));

  kids.push(h("מפתח תשובות"));
  const sym = { A: "קלה", B: "בינונית", C: "קשה" };
  const key = q.map((o, i) => [i + 1, L[o.answer], sym[o.d], o.topic, o.why]);
  kids.push(table([600, 800, 1000, 2200, 4900], ["#", "תשובה", "רמה", "נושא", "הסבר קצר"], key, { centerCols: [0, 1, 2], boldCols: [1] }));
  kids.push(rtl([], { after: 80 }));
  kids.push(rtl(runs("רצף התשובות: " + q.map((o) => L[o.answer]).join("   ")), { after: 60 }));

  if (!VER) {
kids.push(h("הערה על חומר הלימוד"));
  kids.push(rtl(runs("בהערות השיעור של 2.2 (האתגר לתלמידים מהירים ב-Task A) כתוב שמחיקת ה-«pendown()» השני משאירה קו אחד בלבד. בקוד ההפניה יש שני «pendown()», ומחיקת השני משאירה שני קווים. רק מחיקת הראשון משאירה קו אחד. לכן לא שאלתי על התרחיש הזה, ושאלה 14 (שכחנו pendown) משתמשת בקוד שאין בו ספק. כדאי לבדוק מה נאמר בכיתה ולתקן את ההערות."), { after: 60 }));
  }
  return kids;
}

const common = {
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
};
const page = { size: { width: 11906, height: 16838 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } };
const footer = (label) => new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: label + "  ·  עמוד ", font: FONT, size: 18, color: "777777", rightToLeft: true }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18, color: "777777" })] })] });

(async () => {
  const test = new Document({ ...common, sections: [{ properties: { page, bidi: true }, footers: { default: footer("מבחן יחידה 2" + VLABEL) }, children: buildTest() }] });
  const key = new Document({ ...common, sections: [{ properties: { page, bidi: true }, footers: { default: footer("מפתח תשובות – למורה" + VLABEL) }, children: buildKey() }] });
  fs.writeFileSync(path.join(OUT, "u2-test-" + TAG + "-students-he.docx"), await Packer.toBuffer(test));
  fs.writeFileSync(path.join(OUT, "u2-test-" + TAG + "-key-he.docx"), await Packer.toBuffer(key));
  console.log("ok");
})();
