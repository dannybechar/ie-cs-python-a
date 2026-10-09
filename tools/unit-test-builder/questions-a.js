// Unit 2 test data. «...» marks inline code. `fixed` = options already in display order, ans = index of the correct one.
// diff: A easy, B medium, C hard. meeting: 1/2/3.
const L = ["א", "ב", "ג", "ד"];
const q = [];
const add = (o) => q.push(o);

// ---------- Meeting 2.1 ----------
add({ m: 1, d: "A", topic: "ספריית Turtle", t: "מה עושה השורה «import turtle»?",
  correct: "מביאה לתוכנית את ספריית ה-Turtle, ארגז כלים של פקודות ציור",
  wrong: ["פותחת את חלון הציור", "מציירת קו על המסך", "משאירה את החלון פתוח עד שסוגרים אותו"],
  why: "import = להביא את הספרייה. פתיחת החלון היא Screen(), והשארתו פתוח היא done()." });

add({ m: 1, d: "A", topic: "מצב התחלתי של הצב", t: "איפה הצב נמצא, ולאן הוא פונה, כשהתוכנית מתחילה?",
  correct: "באמצע החלון, פונה ימינה",
  wrong: ["באמצע החלון, פונה למעלה", "בפינה השמאלית-תחתונה, פונה ימינה", "בפינה השמאלית-עליונה, פונה למטה"],
  why: "הצב מתחיל באמצע החלון ופונה ימינה." });

add({ m: 1, d: "A", topic: "תיעוד קוד", t: "השורה הראשונה בקובץ היא «# A triangle with equal sides». מה התפקיד של שורה כזו?",
  correct: "להסביר לבני אדם מה התוכנית מציירת. Python מדלגת עליה",
  wrong: ["להגיד לצב לצייר משולש", "לגרום לתוכנית לרוץ מהר יותר", "לתקן שגיאות בקוד"],
  why: "הערה (#) נכתבת בשביל מי שקורא את הקוד, גם אנחנו בעוד חודש. Python מתעלמת ממנה." });

add({ m: 1, d: "A", topic: "שגיאות נפוצות", t: "איזו מהשורות הבאות תרוץ בלי הודעת שגיאה?",
  codeOpts: true,
  correct: "turtle.forward(100)",
  wrong: ["turtle.Forward(100)", "turtle.forward(\"100\")", "turtle.forward 100"],
  why: "Forward באות גדולה נותן AttributeError. מספר במרכאות הוא טקסט. בלי סוגריים זו שגיאת תחביר." });

add({ m: 1, d: "B", topic: "מעקב כיוון", t: "לאן הצב פונה (על המסך) בסוף התוכנית?",
  code: "turtle.forward(100)\nturtle.right(90)\nturtle.forward(50)\nturtle.right(90)",
  fixed: ["למעלה", "למטה", "שמאלה", "ימינה"], ans: 2,
  why: "התחלה: ימינה. אחרי right(90) למטה. אחרי right(90) נוסף: שמאלה." });

add({ m: 1, d: "B", topic: "ימין ושמאל של הצב", t: "הצב פונה למטה אחרי «right(90)». לאן ילך הקו השני, אחרי «left(90)»?",
  code: "turtle.right(90)\nturtle.forward(50)\nturtle.left(90)\nturtle.forward(50)",
  fixed: ["שמאלה", "ימינה", "למטה", "למעלה"], ans: 1,
  why: "שמאל וימין הם של הצב, לא של המסך. כשהצב פונה למטה, ה«שמאל» שלו הוא ימין המסך." });

add({ m: 1, d: "B", topic: "משולש שווה צלעות", t: "במעבדה ציירנו משולש עם שלוש צלעות שוות. בכמה מעלות הצב מסתובב בכל פינה?",
  fixed: ["60", "90", "120", "180"], ans: 2,
  why: "כדי לסיים פונה לאותו כיוון, כל הסיבובים יחד הם 360. 360 ÷ 3 = 120. (60 היא הזווית בתוך המשולש, לא הסיבוב.)" });

add({ m: 1, d: "C", topic: "מדרגות (משימה 1)", t: "במעבדה ציירנו מדרגות שעולות ימינה: שתי מדרגות, כל אחת 40 על 40, ב-8 פקודות בדיוק, והצב מסיים פונה ימינה. באיזה סדר הסיבובים (בכל פעם 90 מעלות)?",
  code: "turtle.forward(40)\nturtle.???(90)   # turn 1\nturtle.forward(40)\nturtle.???(90)   # turn 2\nturtle.forward(40)\nturtle.???(90)   # turn 3\nturtle.forward(40)\nturtle.???(90)   # turn 4",
  codeOpts: true,
  correct: "left, right, left, right",
  wrong: ["left, left, left, left", "right, left, right, left", "left, right, right, left"],
  why: "מדרגות מתחלפות: שמאלה (למעלה), ימינה (חזרה לימין), וכך שוב. סדר ימין-שמאל היה יורד למטה. ארבעה left הם ריבוע." });

// ---------- Meeting 2.2 ----------
add({ m: 2, d: "A", topic: "מצב העט", t: "מה קורה כשהצב מבצע את הפקודה «turtle.penup()»?",
  correct: "הצב ממשיך לזוז, אבל לא משאיר קו",
  wrong: ["הצב עוצר ולא זז עד ל-pendown()", "כל הציור נמחק", "הצב נעלם מהמסך"],
  why: "עט למעלה משנה מה מצויר, לא לאן הצב הולך." });

add({ m: 2, d: "A", topic: "צבע העט", t: "איזו שורה מגדירה נכון את צבע העט לאדום?",
  codeOpts: true,
  correct: "turtle.pencolor(\"red\")",
  wrong: ["turtle.pencolor(red)", "turtle.pencolor \"red\"", "turtle.pencolor(\"reed\")"],
  why: "שם צבע הוא טקסט ולכן במרכאות. בלי מרכאות: NameError. שגיאת כתיב: bad color string." });

add({ m: 2, d: "B", topic: "הגדרות נשארות", t: "איך ייראה הקו השני?",
  code: "turtle.pensize(5)\nturtle.pencolor(\"blue\")\nturtle.forward(50)\nturtle.left(90)\nturtle.forward(50)",
  correct: "כחול ועבה, כמו הראשון",
  wrong: ["שחור ודק, כי חוזרים להגדרות ההתחלה", "כחול ודק", "שחור ועבה"],
  why: "עובי וצבע נשארים עד שמשנים אותם, בדיוק כמו מיקום וכיוון." });

add({ m: 2, d: "B", topic: "חותמות (stamp)", t: "מה נשאר על המסך בסוף הריצה?",
  code: "turtle.shape(\"circle\")\nturtle.stamp()\nturtle.forward(50)\nturtle.stamp()\nturtle.hideturtle()",
  correct: "שני עיגולים וקו באורך 50 ביניהם",
  wrong: ["שני עיגולים בלי קו ביניהם", "רק הקו", "כלום, כי הצב מוסתר"],
  why: "העט למטה ולכן יש קו. stamp משאיר עותק של הצורה, והסתרת הצב מסתירה רק את הסמן." });

add({ m: 2, d: "B", topic: "כביש מקווקו (משימה A)", t: "כביש מקווקו: שלושה קווים, כל אחד באורך 30, ורווח של 15 בין קו לקו (בלי רווח אחרי הקו האחרון). כמה צעדים הצב עובר בסך הכול, מתחילת הקו הראשון ועד סוף הקו השלישי?",
  fixed: ["90", "105", "120", "135"], ans: 2,
  why: "30 + 15 + 30 + 15 + 30 = 120. גם הצעדים עם עט למעלה נספרים." });

add({ m: 2, d: "B", topic: "שכחנו pendown()", t: "שכחנו לכתוב pendown(). מה נראה על המסך?",
  code: "turtle.forward(30)\nturtle.penup()\nturtle.forward(15)\nturtle.forward(30)",
  correct: "קו אחד באורך 30 בלבד. אחרי זה הצב זז 45 צעדים בלי לצייר",
  wrong: ["שני קווים באורך 30 עם רווח ביניהם", "קו אחד ארוך באורך 75", "לא נראה כלום"],
  why: "העט נשאר למעלה עד שמורידים אותו, וזו הטעות הנפוצה ביותר ביחידה." });

add({ m: 2, d: "C", topic: "שינוי צבע בזמן עט למעלה", t: "איך ייראה הציור? (הצב פונה ימינה בתחילת הריצה)",
  code: "turtle.pencolor(\"green\")\nturtle.forward(40)\nturtle.penup()\nturtle.forward(30)\nturtle.pencolor(\"orange\")\nturtle.pendown()\nturtle.forward(40)\nturtle.pencolor(\"purple\")\nturtle.forward(40)",
  correct: "ירוק 40, רווח 30, כתום 40, סגול 40",
  wrong: ["ירוק 40, רווח 30, ירוק 40, כתום 40", "ירוק 40, קו כתום 30, כתום 40, סגול 40", "ירוק 40, רווח 30, כתום 80"],
  why: "הצבע החדש תופס לקו הבא שמציירים, גם אם הוחלף כשהעט למעלה. בזמן הרווח העט למעלה, אין קו." });

add({ m: 2, d: "B", topic: "אחזור (משימה D)", t: "מה יודפס בחלון ה-Shell, לפי הסדר?",
  code: "turtle.pensize(3)\nprint(turtle.pensize())\nturtle.pencolor(\"red\")\nprint(turtle.pencolor())\nturtle.pensize(7)\nprint(turtle.pensize())",
  codeOpts: true,
  correct: "3, red, 7",
  wrong: ["1, black, 7", "3, red, 3", "3, black, 7"],
  why: "עם ערך בסוגריים משנים (עדכון). עם סוגריים ריקים שואלים מה הערך עכשיו (אחזור), ו-print מציג אותו." });

add({ m: 2, d: "B", topic: "עדכון מול אחזור", t: "איזו פקודה רק שואלת מה הערך הנוכחי (אחזור) ולא משנה כלום?",
  codeOpts: true,
  correct: "turtle.pensize()",
  wrong: ["turtle.pensize(8)", "turtle.pencolor(\"blue\")", "turtle.shape(\"arrow\")"],
  why: "סוגריים ריקים = אחזור. ערך בסוגריים = עדכון." });

add({ m: 2, d: "B", topic: "פונקציה לכל משימה", t: "במעבדה כל משימה נכתבה כפונקציה נפרדת, ובכל הרצה היה פעיל זימון אחד בלבד (שאר הזימונים בהערה). למה?",
  correct: "כדי שכל הרצה תתחיל מאפס, וההגדרות של משימה אחת (צבע, עובי, עט למעלה) לא יעברו למשימה הבאה",
  wrong: ["כי Python מאפשרת להריץ רק פונקציה אחת בקובץ", "כי פקודות turtle עובדות רק בתוך פונקציה", "כדי שהצב יצייר מהר יותר"],
  why: "זה כלל העבודה של השיעור, וכך גם הבנו למה Task D הדפיס black ולא כתום של Task B." });

// ---------- Meeting 2.3 ----------
add({ m: 3, d: "A", topic: "שגיאה לוגית", t: "תוכנית «ריבוע שבור» רצה בלי שום הודעת שגיאה, אבל הציור יוצא לא ריבוע. איזו שגיאה זו?",
  correct: "שגיאה לוגית: הקוד תקין, אבל ההוראות לא מתאימות למה שרצינו לצייר",
  wrong: ["שגיאת תחביר (SyntaxError)", "שגיאת שם (NameError)", "שגיאת import"],
  why: "תוכנית יכולה לרוץ בהצלחה ועדיין לצייר לא נכון." });

const broken = "turtle.forward(80)\nturtle.right(90)\nturtle.forward(80)\nturtle.right(90)\nturtle.forward(80)\nturtle.left(90)\nturtle.forward(80)\nturtle.right(90)";

add({ m: 3, d: "B", topic: "תיקון באג", t: "הקוד אמור לצייר ריבוע 80 על 80 אבל מצייר צורה אחרת. איזה תיקון הופך אותו לריבוע?",
  code: broken,
  correct: "לשנות את ה-«left(90)» לשורה «right(90)»",
  wrong: ["לשנות את ה-forward(80) האחרון ל-forward(100)", "למחוק את ה-right(90) האחרון", "להוסיף «turtle.left(90)» בסוף התוכנית"],
  why: "הסיבוב השלישי הוא הסיבוב היחיד שלא כמו האחרים. מתקנים את ההוראה שגרמה לבעיה ולא מנחשים." });

add({ m: 3, d: "C", topic: "מעקב עם סיבובים מעורבים", t: "בקוד הבא, לאן הולך הקו הרביעי והאחרון על המסך?",
  code: "turtle.forward(60)\nturtle.left(90)\nturtle.forward(40)\nturtle.right(90)\nturtle.forward(30)\nturtle.right(90)\nturtle.forward(20)",
  fixed: ["ימינה", "למעלה", "שמאלה", "למטה"], ans: 3,
  why: "הקו הראשון ימינה, left(90) למעלה, right(90) שוב ימינה, ואז right(90) מכיוון ימינה פונה למטה. הקו האחרון הולך למטה." });

add({ m: 3, d: "B", topic: "ריבוע למלבן", t: "משנים ריבוע 80 על 80 למלבן 120 על 60. מה משנים בקוד?",
  correct: "רק את המספרים בתוך forward(...): 120, 60, 120, 60. הסיבובים נשארים 90",
  wrong: ["את כל הזוויות, ל-120 ול-60", "מוסיפים עוד שתי פקודות סיבוב", "את כל ארבעת ה-forward ל-120"],
  why: "מרחק קובע אורך צלע, זווית קובעת שינוי כיוון. מלבן הוא עדיין ארבע פינות של 90°, והצלעות הנגדיות שוות." });

add({ m: 3, d: "C", topic: "מלבן 120 × 70 (המבחן המעשי)", t: "איזו תוכנית מציירת מלבן 120 על 70, סוגרת אותו, והצב מסתיים פונה ימינה כמו בהתחלה? הקיצורים: «F» = forward, «L» = left, «R» = right.",
  codeOpts: true,
  correct: "F120 R90 F70 R90 F120 R90 F70 R90",
  wrong: ["F120 R90 F70 R90 F120 R90 F70", "F120 R90 F70 R90 F70 R90 F120 R90", "F120 L90 F70 R90 F120 L90 F70 R90"],
  why: "צלעות נגדיות שוות (120, 70, 120, 70), ארבעה סיבובים בכיוון אחד. בלי הסיבוב הרביעי הצורה סגורה אבל הצב פונה למעלה." });

add({ m: 3, d: "C", topic: "מיקום מול כיוון (בדיקת יציאה)", t: "האם הצורה סגורה (הצב חזר לנקודת ההתחלה), ולאן הצב פונה בסוף?",
  code: "turtle.forward(50)\nturtle.left(90)\nturtle.forward(30)\nturtle.left(90)\nturtle.forward(50)\nturtle.left(90)\nturtle.forward(30)",
  correct: "סגורה, והצב פונה למטה",
  wrong: ["סגורה, והצב פונה ימינה", "לא סגורה, והצב פונה למטה", "לא סגורה, והצב פונה ימינה"],
  why: "הצב חוזר להתחלה אחרי ארבע צלעות, אבל עשה רק שלושה סיבובים של 90 שמאלה: 270°. הוא פונה למטה. מיקום וכיוון הם שני דברים נפרדים." });

add({ m: 3, d: "C", topic: "מסלול משולב (חותמת + עט)", t: "מה נראה על המסך בסוף?",
  code: "turtle.stamp()\nturtle.forward(50)\nturtle.left(90)\nturtle.penup()\nturtle.forward(30)\nturtle.pendown()\nturtle.right(90)\nturtle.forward(50)",
  correct: "חותמת בהתחלה, ושני קווים אופקיים מקבילים באורך 50 שאינם מחוברים. השני גבוה ב-30 וממשיך ימינה",
  wrong: ["חותמת וקו אחד באורך 100", "חותמת וקו בצורת האות L", "שני קווים אופקיים שמחוברים בקו אנכי באורך 30"],
  why: "ה-30 האנכיים נעשו כשהעט למעלה, ולכן אין קו אנכי. אחרי right(90) הצב שוב פונה ימינה." });

// ---------- answer positions ----------
// target letter index for the non-fixed questions, by question number (1-based); fixed ones keep their ans.
const keyPlan = {1:0, 2:3, 3:1, 4:0, 8:3, 9:0, 10:1, 11:3, 12:0, 14:1, 15:2, 16:3, 17:1, 18:0, 19:3, 20:1, 22:0, 23:2, 24:1, 25:2};
q.forEach((o, i) => {
  const n = i + 1;
  if (o.fixed) { o.options = o.fixed; o.answer = o.ans; }
  else {
    const pos = keyPlan[n];
    if (pos === undefined) throw new Error("no key plan for Q" + n);
    const opts = o.wrong.slice(); opts.splice(pos, 0, o.correct);
    o.options = opts; o.answer = pos;
  }
});
module.exports = { q, L };
