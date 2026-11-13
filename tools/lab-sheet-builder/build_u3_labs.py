"""Builds the Unit 3 printable lab sheets (Hebrew, RTL, black and white) and the teacher key.

Usage: python build_u3_labs.py <output folder>
Writes m1-lab-sheet-he.pdf, m2-lab-sheet-he.pdf and u3-lab-sheets-key-he.pdf using headless Edge.
Each student sheet must stay within 2 pages (one sheet, both sides); the script checks it.

WORKSHEET STANDARD (teacher's rules, apply to every worksheet):
- Two question types only: RUN = run this code, write what was printed, explain why;
  CODE = write the code that does this or that.
- Layout of every question: a pair of equal-height boxes. The CODE is always in the LEFT box
  (given code, or an empty box where the student writes code). The RIGHT box holds the answer
  prompts (what was printed, explain why) with blank space. No ruled lines.
Edit this file with the Edit/Write tools, not with shell heredocs (Hebrew gets mangled).
"""
import os
import subprocess
import sys
import tempfile

import fitz  # PyMuPDF, used only to count pages

EDGE = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

CSS = """
@page { size: A4; margin: 10mm 13mm; }
* { box-sizing: border-box; }
body { direction: rtl; font-family: Arial, 'Segoe UI', sans-serif; font-size: 10.2pt; line-height: 1.33; color: #000; }
h1 { font-size: 16pt; margin: 0; }
.sub { font-size: 10.3pt; margin: 1pt 0 2pt; }
.top { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2pt solid #000; padding-bottom: 2pt; margin-bottom: 4pt; }
.who { font-size: 10pt; white-space: nowrap; }
.box { border: 1.2pt solid #000; padding: 2pt 7pt; margin: 3pt 0; }
.box ul { margin: 1pt 0; padding-right: 14pt; }
.part { font-size: 12pt; font-weight: bold; background: #e6e6e6; border: 1pt solid #000; padding: 0 7pt; margin: 6pt 0 0; }
.sec { margin: 5pt 0 0; break-inside: avoid; }
.sh { font-size: 11pt; font-weight: bold; border-bottom: 1pt solid #000; padding-bottom: 1pt; margin-bottom: 2pt; display: flex; justify-content: space-between; break-after: avoid; }
.sh span { font-weight: normal; font-size: 9.5pt; }
code, pre { font-family: Consolas, 'Courier New', monospace; font-size: 9.5pt; direction: ltr; unicode-bidi: isolate; }
.qrow { display: flex; direction: ltr; gap: 9pt; align-items: stretch; margin: 3pt 0; break-inside: avoid; }
.qrow > div { flex: 1; border: 1pt solid #000; padding: 3pt 7pt; }
.cbox { direction: ltr; text-align: left; font-family: Consolas, 'Courier New', monospace; font-size: 9.5pt; line-height: 1.28; white-space: pre; }
.cbox .lab { font-family: Arial, 'Segoe UI', sans-serif; font-size: 8.5pt; direction: rtl; text-align: left; white-space: normal; }
.abox { direction: rtl; text-align: right; }
.abox pre { margin: 1pt 0; font-size: 9.5pt; line-height: 1.28; direction: ltr; text-align: left; }
.al { font-weight: bold; }
table { border-collapse: collapse; width: 100%; margin: 3pt 0; }
th, td { border: 1pt solid #000; padding: 2pt 5pt; text-align: center; }
th { background: #e6e6e6; }
td.t { text-align: right; }
.bl { display: inline-block; border-bottom: 1pt solid #000; min-width: 38pt; height: 11pt; vertical-align: bottom; }
.bl.w { min-width: 90pt; }
.hint { font-size: 9.5pt; }
.ch { border: 1.2pt dashed #000; padding: 2pt 7pt; margin-top: 6pt; break-inside: avoid; }
.k { font-size: 9.6pt; }
.k h2 { font-size: 12pt; margin: 7pt 0 2pt; border-bottom: 1pt solid #000; }
"""

BL = '<span class="bl"></span>'
BLW = '<span class="bl w"></span>'


def page(title, body):
    return f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>'


def head(title, sub):
    return (
        f'<div class="top"><div><h1>{title}</h1><div class="sub">{sub}</div></div>'
        f'<div class="who">שם: {BLW} &nbsp; כיתה: {BL}</div></div>'
    )


def part(title):
    return f'<div class="part">{title}</div>'


def sec(n, title, minutes, inner):
    return f'<div class="sec"><div class="sh">{n}. {title}<span>{minutes} דקות</span></div>{inner}</div>'


def ans(label, h):
    """A prompt in the right-hand box followed by blank writing space of h points."""
    return f'<div class="al">{label}</div><div style="height:{h}pt"></div>'


def code(text):
    """Left box with given code."""
    return f'<div class="cbox">{text}</div>'


def empty(h, label="כתבו כאן את הקוד"):
    """Left box where the student writes code (min height h points)."""
    return f'<div class="cbox" style="min-height:{h}pt"><div class="lab">{label}</div></div>'


def qrow(left, right):
    """Standard pair: code on the left, answer box on the right, equal height."""
    return f'<div class="qrow">{left}<div class="abox">{right}</div></div>'


# ---------------------------------------------------------------- Lab 3.1
M1 = head("מעבדה 3.1 · הזיכרון של הרובר", "משתנים, טיפוסים וקלט · פייתון א׳ · זמן: 45 דקות")
M1 += """
<div class="box"><b>במעבדה יש שני סוגי משימות:</b><ul>
<li><b>הרצה והסבר:</b> מקלידים את הקוד (או פותחים את הקובץ), מריצים, כותבים מה הודפס, ו<b>מסבירים למה</b> זה מה שהודפס.</li>
<li><b>כתיבת קוד:</b> כותבים קוד שעושה את מה שמבקשים. כל משימה בפונקציה משלה (<code>def</code>), ובסוף הקובץ רק זימון אחד פעיל (השאר עם <code>#</code>).</li>
</ul>
<div class="hint">בכל משימה: משמאל הקוד, ומימין התיבה לתשובות. הקלט מחכה בחלון Shell: לוחצים שם, מקלידים ולוחצים Enter. כותבים בעיפרון.</div></div>
"""
M1 += part("חלק א׳ · הרצה והסבר")
M1 += sec(1, "יומן הרובר", 4, "פתחו את <code>Variables_Starter.py</code> והריצו." + qrow(
    code('''planet = "Mars"
distance = 225
speed = 3.5
landed = False

print("Planet:", planet)
print("Distance:", distance)
print("Speed:", speed)
print("Landed:", landed)

landed = True
print("Landed:", landed)'''),
    ans("מה הודפס? (כל השורות)", 70) + ans("הסבירו: למה <code>Landed</code> הודפס פעמיים, ובכל פעם עם ערך אחר? מה קרה לערך <code>False</code>?", 36)))
M1 += sec(2, "מרכאות וטיפוסים", 6, "הקלידו והריצו כל קוד בנפרד." + qrow(
    code('''fuel = 80
print(fuel)
print("fuel")'''),
    ans("מה הודפס?", 26) + ans("הסבירו: שתי הפקודות <code>print</code> כמעט זהות. למה התוצאות שונות?", 26))
    + qrow(
    code('''print(type(7))
print(type("7"))
print(type(7.0))
print(type(True))
print(type("True"))'''),
    ans("מה הודפס, שורה אחר שורה?", 62) + ans("הסבירו: <code>7</code> ו-<code>&quot;7&quot;</code> נראים כמעט אותו דבר. למה הטיפוס שלהם שונה? ולמה הטיפוס של <code>&quot;True&quot;</code> הוא לא <code>bool</code>?", 34)))
M1 += sec(3, "קלט הוא תמיד טקסט", 5, "הקלידו והריצו, והקלידו כשמבקשים: <code>12</code>" + qrow(
    code('''age = input("Age: ")
print(type(age))'''),
    ans("מה הודפס?", 20) + ans("הסבירו: הקלדתם מספר. למה הטיפוס הוא לא <code>int</code>?", 30))
    + "עכשיו שנו את השורה הראשונה כך, והריצו פעמיים: עם הקלט <code>12</code>, ואחר כך עם <code>abc</code>."
    + qrow(
    code('''age = int(input("Age: "))
print(type(age))'''),
    ans("מה הודפס בכל הרצה?", 30) + ans("הסבירו: למה בהרצה עם <code>abc</code> קרה מה שקרה?", 28)))
M1 += sec(4, "משתנה שמניע את הצב", 5, "הקלידו והריצו פעמיים: עם הקלט <code>50</code>, ואחר כך עם <code>120</code>." + qrow(
    code('''import turtle
side = int(input("Side length: "))
turtle.forward(side)
turtle.right(90)
turtle.forward(side)
turtle.done()'''),
    ans("מה ציירתם בכל הרצה?", 30) + ans("הסבירו: מה השתנה בציור בין ההרצות ומה נשאר זהה? כמה שורות בקוד שיניתם, ולמה?", 36)))
M1 += part("חלק ב׳ · כתיבת קוד")
M1 += sec(5, "כרטיס משימה", 6, """
כתבו פונקציה <code>mission_card()</code> ששואלת מה שמכם ומה שם הרובר שלכם, ומדפיסה כרטיס. רמז: בשורה האחרונה יש כמה ערכים ב-<code>print</code> אחד, מופרדים בפסיקים.""" + qrow(
    empty(96),
    '<div class="al">הפלט הנדרש, עם הקלט שלכם במקום Dana ו-Curiosity, הוא:</div><pre>Commander: Dana\nRover: Curiosity\nMission card: Dana and Curiosity</pre>'
    + ans("מה הודפס בהרצה שלכם?", 34)))
M1 += sec(6, "בלש הטיפוסים", 8, """
כתבו פונקציה <code>types_detective()</code> ששואלת: גיל, גובה במטרים, עיר ומספר אחים ואחיות. שמרו כל תשובה <b>בטיפוס המתאים</b> (<code>int</code> / <code>float</code> / <code>str</code>) ו<b>הדפיסו כל ערך עם הטיפוס שלו</b>, למשל: <code>print("Age:", age, type(age))</code>""" + qrow(
    empty(112),
    ans("מה הודפס בהרצה שלכם? (ארבע שורות)", 52) + ans("הסבירו: איזה טיפוס בחרתם לגובה, ולמה?", 36))
    + '<div class="hint">מעל כל פונקציה כתבו הערה (<code>#</code>) שמסבירה מה היא עושה. שמרו: <code>File &gt; Save As</code> ← <code>U3_M1_Variables_&lt;Name&gt;.py</code></div>')

# ---------------------------------------------------------------- Lab 3.2
M2 = head("מעבדה 3.2 · מחשבון הרובר", "מהקלט לתוצאה: חישובים עם משתנים · פייתון א׳ · זמן: 45 דקות")
M2 += """
<table style="margin-top:2pt"><tr><th>פעולה</th><th><code>+</code> חיבור</th><th><code>-</code> חיסור</th><th><code>*</code> כפל</th><th><code>/</code> חילוק</th><th><code>//</code> קבוצות שלמות</th><th><code>%</code> שארית</th></tr>
<tr><td class="t">דוגמה</td><td><code>12 + 5</code> ← 17</td><td><code>12 - 5</code> ← 7</td><td><code>12 * 5</code> ← 60</td><td><code>12 / 5</code> ← 2.4</td><td><code>17 // 5</code> ← 3</td><td><code>17 % 5</code> ← 2</td></tr></table>
<div class="box"><b>שני סוגי משימות:</b> <b>הרצה והסבר</b> (מריצים, כותבים מה הודפס ומסבירים למה) ו<b>כתיבת קוד</b> (כותבים קוד שעושה את מה שמבקשים). בכל משימה: משמאל הקוד, ומימין התיבה לתשובות. היום ב-<code>//</code> וב-<code>%</code> משתמשים רק במספרים שלמים חיוביים, ומחלקים במספר גדול מ-0.</div>
"""
M2 += part("חלק א׳ · הרצה והסבר")
M2 += sec(1, "ארבע פעולות", 4, "פתחו את <code>Arithmetic_Starter.py</code> והריצו." + qrow(
    code('''a = 12
b = 5

total = a + b
difference = a - b
product = a * b
quotient = a / b

print("Add:", total)
print("Subtract:", difference)
print("Multiply:", product)
print("Divide:", quotient)'''),
    ans("מה הודפס?", 44) + ans("הסבירו: איזו פעולה נתנה מספר עשרוני, ולמה, אף ש-<code>a</code> ו-<code>b</code> שלמים?", 34)))
M2 += sec(2, "החלפה ועדכון", 7, "הקלידו והריצו." + qrow(
    code('''a = 4
b = 9
a = b
b = a
print(a, b)'''),
    ans("מה הודפס?", 20) + ans("הסבירו: רצינו להחליף בין <code>a</code> ל-<code>b</code>. למה שניהם 9?", 28))
    + "כתבו מחדש כך ש-<code>a</code> ו-<code>b</code> באמת יוחלפו (יודפס <code>9 4</code>). השתמשו במשתנה שלישי בשם <code>temp</code>." + qrow(
    empty(44, "כתבו כאן את הקוד"),
    ans("מה הודפס עכשיו?", 20))
    + "הקלידו והריצו." + qrow(
    code('''score = 10
score = score + 1
print(score)'''),
    ans("מה הודפס?", 20) + ans("הסבירו: איזה צד של סימן ה-<code>=</code> מחושב קודם?", 30)))
M2 += sec(3, "קבוצות שלמות ושארית", 4, "החזירו <code>a = 17</code> ו-<code>b = 5</code>. הוסיפו לתוכנית והריצו." + qrow(
    code('''full_groups = a // b
left_over = a % b
print("Full groups:", full_groups)
print("Left over:", left_over)'''),
    ans("מה הודפס בשתי השורות?", 24) + ans("הסבירו: איך שתי התוצאות ביחד מרכיבות את המספר 17?", 26)))
M2 += sec(4, "משתנה לא מתעדכן לבד", 4, "הקלידו והריצו." + qrow(
    code('''price = 8
quantity = 3
total = price * quantity
quantity = 5
print("Total:", total)'''),
    ans("מה הודפס?", 18) + ans("הסבירו: שינינו את <code>quantity</code> ל-5. למה <code>total</code> לא השתנה?", 28)))
M2 += sec(5, "קלט בלי המרה", 5, "הקלידו והריצו עם הקלט <code>12</code> ואחר כך <code>5</code>." + qrow(
    code('''a = input("First number: ")
b = input("Second number: ")
print(a + b)'''),
    ans("מה הודפס?", 18) + ans("הסבירו: למה זה לא 17?", 26))
    + "כתבו את שתי השורות הראשונות מתוקנות, כך שיודפס 17, והריצו שוב." + qrow(
    empty(46, "כתבו כאן את השורות המתוקנות"),
    ans("מה הודפס עכשיו?", 24)))
M2 += part("חלק ב׳ · כתיבת קוד")
M2 += sec(6, "מחשבון אריזות (עובדים לבד)", 14, """
כתבו תוכנית חדשה שקולטת כמה פריטים יש (<code>items</code>) וכמה פריטים נכנסים בכל חבילה (<code>per_pack</code>), מחשבת כמה חבילות מלאות יש ומה נשאר, ומדפיסה שתי שורות ברורות. דוגמה לפלט מופיעה בתיבה שמימין.""" + qrow(
    empty(128),
    '<div class="al">דוגמה לפלט (הצורה, לא התוצאה שלכם):</div><pre>Full packs: 3\nLeft over: 2</pre>'
    + ans("הרצה עם <code>items = 17</code> ו-<code>per_pack = 5</code>: מה הודפס?", 24)
    + ans("הרצה עם <code>items = 3</code> ו-<code>per_pack = 5</code>: מה הודפס?", 24)
    + ans("הסבירו: בהרצה השנייה יש פחות פריטים מאשר בחבילה אחת. למה הודפסו המספרים האלה?", 34))
    + '<div class="hint">שמרו: <code>File &gt; Save As</code> ← <code>U3_M2_Packing_&lt;Name&gt;.py</code></div>')
M2 += """
<div class="ch"><b>★ למי שסיים (כתיבת קוד):</b> 1. חבילה עולה 12 ש״ח. הוסיפו לתוכנית שורה שמדפיסה כמה עולות החבילות המלאות בלבד.
2. כתבו תוכנית חדשה שקולטת מחיר של פריט וכמה פריטים קנו, ומדפיסה את הסכום הכולל.
3. כתבו שורת קוד אחת שמדפיסה את 2 בחזקת 10 (בעזרת <code>**</code>), ושורה שמדפיסה את <code dir="ltr" style="unicode-bidi:isolate">2 + 3 * 4</code>. מה הודפס בכל שורה, ואיזו פעולה חושבה קודם בשורה השנייה?</div>
"""

# ---------------------------------------------------------------- Key
KEY = """
<div class="top"><div><h1>מפתח למורה · מעבדות 3.1 ו-3.2</h1><div class="sub">תוצאות צפויות, הסברים מצופים ותזמון. לא להפיץ לתלמידים.</div></div></div>
<div class="k">
<h2>מעבדה 3.1 · הזיכרון של הרובר</h2>
<table><tr><th>משימה</th><th>דקות</th><th>מה אמור להיות מודפס · ההסבר המצופה</th></tr>
<tr><td>1. יומן הרובר<br>(הרצה)</td><td>4</td><td class="t">חמש שורות: <code>Planet: Mars</code>, <code>Distance: 225</code>, <code>Speed: 3.5</code>, <code>Landed: False</code>, <code>Landed: True</code>. הסבר: בקופסה <code>landed</code> יש ערך אחד בכל רגע; ההשמה <code>landed = True</code> החליפה את <code>False</code>, והוא נעלם. ההדפסה השנייה קוראת את הערך החדש.</td></tr>
<tr><td>2. מרכאות וטיפוסים<br>(הרצה)</td><td>6</td><td class="t">קוד ראשון: <code>80</code> ואחריו <code>fuel</code>. הסבר: בלי מרכאות פייתון מדפיסה את הערך שבתוך המשתנה; עם מרכאות זה טקסט, והיא מדפיסה את האותיות עצמן. קוד שני: <code>&lt;class 'int'&gt;</code>, <code>&lt;class 'str'&gt;</code>, <code>&lt;class 'float'&gt;</code>, <code>&lt;class 'bool'&gt;</code>, <code>&lt;class 'str'&gt;</code>. הסבר: מה שבתוך מרכאות הוא טקסט (<code>str</code>), גם אם נראה כמו מספר או כמו <code>True</code>; מספר בלי מרכאות הוא <code>int</code>, ועם נקודה עשרונית <code>float</code>; רק <code>True</code> בלי מרכאות הוא <code>bool</code>.</td></tr>
<tr><td>3. קלט<br>(הרצה)</td><td>5</td><td class="t">בלי המרה: <code>&lt;class 'str'&gt;</code>. עם <code>int(...)</code> והקלט 12: <code>&lt;class 'int'&gt;</code>. עם <code>abc</code>: <code>ValueError: invalid literal for int() with base 10: 'abc'</code>. הסבר: <code>input</code> תמיד מחזירה טקסט, גם כשמקלידים מספר; <code>int()</code> ממירה טקסט שנראה כמו מספר שלם, ולא יכולה להמיר <code>abc</code>.</td></tr>
<tr><td>4. צב<br>(הרצה)</td><td>5</td><td class="t">הקלט 50: צורת L קטנה (קו ימינה ואז קו למטה, שניהם באורך 50). הקלט 120: אותה צורה בגודל גדול יותר. הסבר: אורך שני הקווים נקבע מהמשתנה <code>side</code>, והזווית (90) קבועה בקוד, ולכן הצורה נשארת והגודל משתנה. <b>0 שורות</b> בקוד השתנו, כי רק הקלט שונה. (הכנה לריבוע בהדגמה: ארבע צלעות באותו <code>side</code>.)</td></tr>
<tr><td>5. כרטיס משימה<br>(קוד)</td><td>6</td><td class="t"><code>def mission_card():</code> ובתוכה <code>name = input(...)</code>, <code>rover = input(...)</code>, <code>print("Commander:", name)</code>, <code>print("Rover:", rover)</code>, <code>print("Mission card:", name, "and", rover)</code>. טעות נפוצה: מרכאות סביב <code>name</code> (מדפיס את המילה name).</td></tr>
<tr><td>6. בלש הטיפוסים<br>(קוד)</td><td>8</td><td class="t">גיל ואחים: <code>int(input(...))</code>; גובה: <code>float(input(...))</code>; עיר: <code>input(...)</code>; ארבע הדפסות בצורה <code>print("Age:", age, type(age))</code>. הסבר: גובה הוא <code>float</code> כי הוא יכול להיות עם שבר (1.65); מספר אחים תמיד שלם. טעות נפוצה: <code>int</code> על גובה עשרוני (<code>ValueError</code>).</td></tr></table>
<div>סה״כ בערך 35 דקות של משימות ומרווח של כ-10 דקות להקלדה ולהסברים. אם הכיתה מתעכבת: לדלג על משימה 4 (ולעשות אותה בהדגמה), ולא לוותר על משימות 5 ו-6. הפתרון המלא של <code>turtle_square()</code> (ארבע צלעות) נמצא ב-<code>solutions/Variables_Reference.py</code>.</div>

<h2>מעבדה 3.2 · מחשבון הרובר</h2>
<table><tr><th>משימה</th><th>דקות</th><th>מה אמור להיות מודפס · ההסבר המצופה</th></tr>
<tr><td>1. ארבע פעולות<br>(הרצה)</td><td>4</td><td class="t"><code>Add: 17</code>, <code>Subtract: 7</code>, <code>Multiply: 60</code>, <code>Divide: 2.4</code>. הסבר: החילוק <code>/</code> נותן מספר עשרוני כי 12 לא מתחלק ב-5 בשלמות (2.4); שאר הפעולות על שלמים נותנות שלמים.</td></tr>
<tr><td>2. החלפה ועדכון<br>(הרצה + קוד)</td><td>7</td><td class="t">הרצה ראשונה: <code>9 9</code>. הסבר: אחרי <code>a = b</code> שני המשתנים שווים 9, והערך הישן של <code>a</code> (4) כבר נמחק, ולכן <code>b = a</code> מעתיקה 9. תיקון: <code>temp = a</code>, <code>a = b</code>, <code>b = temp</code>; יודפס <code>9 4</code>. הרצה שנייה: <code>11</code>. הסבר: מחשבים קודם את צד ימין (10 + 1 = 11) ורק אז שומרים ב-<code>score</code>, והערך הישן נעלם. ★ 3: <code>print(2 ** 10)</code> ← 1024, <code>print(2 + 3 * 4)</code> ← 14, כי הכפל מחושב לפני החיבור.</td></tr>
<tr><td>3. // ו-%<br>(הרצה)</td><td>4</td><td class="t"><code>Full groups: 3</code>, <code>Left over: 2</code>. הסבר: 17 = 3 קבוצות של 5 (15) ועוד 2 שנשארו; <code>//</code> נותן את מספר הקבוצות השלמות ו-<code>%</code> את מה שנשאר. ב-Python <code>%</code> הוא שארית, לא אחוזים.</td></tr>
<tr><td>4. לא מתעדכן<br>(הרצה)</td><td>4</td><td class="t"><code>Total: 24</code>. הסבר: <code>total</code> חושב בשורה 3 מהערכים שהיו אז (8 · 3). שינוי <code>quantity</code> אחר כך לא מחשב מחדש; צריך לכתוב שוב את שורת החישוב.</td></tr>
<tr><td>5. קלט בלי המרה<br>(הרצה)</td><td>5</td><td class="t"><code>125</code>. הסבר: <code>input</code> מחזירה טקסט, ו-<code>+</code> על שני טקסטים מחבר אותם זה לזה ולא מחשב. תיקון: <code>a = int(input("First number: "))</code> ו-<code>b = int(input("Second number: "))</code>; אז יודפס 17.</td></tr>
<tr><td>6. מחשבון אריזות<br>(קוד)</td><td>14</td><td class="t"><code>items = int(input(...))</code>, <code>per_pack = int(input(...))</code>, <code>full_packs = items // per_pack</code>, <code>left_over = items % per_pack</code>, ושתי הדפסות. הרצה 17 ו-5: <code>3, 2</code>. הרצה 3 ו-5: <code>0, 3</code>. הסבר: אין אפילו חבילה מלאה אחת, ולכן 0 חבילות מלאות וכל 3 הפריטים נשארו. טעות נפוצה: <code>/</code> במקום <code>//</code>.</td></tr>
<tr><td>★ 1, 2</td><td></td><td class="t">1: <code>print("Cost:", full_packs * 12)</code> (ל-17 ו-5: 36). 2: <code>price = int(input(...))</code>, <code>quantity = int(input(...))</code>, <code>print("Total:", price * quantity)</code>.</td></tr></table>
<div>סה״כ בערך 38 דקות של משימות ומרווח של כ-7 דקות. אם הכיתה מתעכבת: לדלג על משימה 4 ולהסביר אותה בכיתה, ולשמור על משימת הליבה. קבצי ההתחלה <code>Variables_Starter.py</code> ו-<code>Arithmetic_Starter.py</code> נמצאים ב-<code>exercises/</code>, ופתרונות מלאים ב-<code>solutions/</code>. בשמות הקבצים הוחלף <code>G7</code> ב-<code>U3</code> כי המעבדה לכיתות ז׳ וח׳.</div>
</div>
"""

DOCS = {
    "m1-lab-sheet-he.pdf": ("מעבדה 3.1", M1, True),
    "m2-lab-sheet-he.pdf": ("מעבדה 3.2", M2, True),
    "u3-lab-sheets-key-he.pdf": ("מפתח מעבדות יחידה 3", KEY, False),
}


def main(out):
    out = os.path.abspath(out)
    os.makedirs(out, exist_ok=True)
    tmp = tempfile.mkdtemp()
    for name, (title, body, strict) in DOCS.items():
        hp = os.path.join(tmp, name + ".html")
        open(hp, "w", encoding="utf-8").write(page(title, body))
        pdf = os.path.join(out, name)
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", "file:///" + hp.replace("\\", "/")],
                       check=True, capture_output=True, timeout=120)
        n = fitz.open(pdf).page_count
        print(name, n, "pages")
        if strict and n > 2:
            print("  TOO LONG: must fit one sheet, both sides")
            sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1])
