"""Builds the Unit 3.2 add-on slides (16:9 PDF, Hebrew, RTL): the 3.1 recap plus the new `**`, swap and
self-update blocks that are not in the NotebookLM deck m2-slides-he.pdf.

Usage: python build_u3_m2_addon.py <output folder>      (writes m2-addon-slides-he.pdf)
Question slides never show their answer; the answer is the next slide. Code is always left-to-right.
Edit with the Edit/Write tools, not shell heredocs (Hebrew gets mangled).
"""
import os
import subprocess
import sys
import tempfile

import fitz  # PyMuPDF, page count check only

EDGE = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
FOOTER = "יחידה 3.2 – משתנים, קלט/פלט וחישובים"

CSS = """
@page { size: 1280px 720px; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { direction: rtl; font-family: 'Segoe UI', Arial, sans-serif; color: #111; }
.s { width: 1280px; height: 720px; padding: 46px 70px 62px; position: relative; page-break-after: always; overflow: hidden; background: #fff; }
.s:last-child { page-break-after: auto; }
.tag { position: absolute; top: 22px; left: 28px; font-size: 20px; color: #444; direction: rtl; }
h1 { font-size: 54px; margin: 8px 0 10px; border-bottom: 5px solid #111; padding-bottom: 8px; }
h2 { font-size: 46px; margin: 0 0 14px; }
.q { display: block; width: max-content; background: #111; color: #fff; font-size: 26px; padding: 3px 18px; border-radius: 6px; margin: 0 0 10px; }
.a { display: block; width: max-content; border: 4px solid #111; font-size: 26px; padding: 0 16px; border-radius: 6px; margin: 0 0 10px; }
p, li { font-size: 40px; line-height: 1.4; margin: 6px 0; }
ul { margin: 6px 0; padding-right: 36px; }
code, pre { font-family: Consolas, 'Courier New', monospace; direction: ltr; unicode-bidi: isolate; }
pre { font-size: 50px; line-height: 1.32; margin: 12px 0; padding: 16px 28px; border: 4px solid #111; border-radius: 10px; text-align: left; display: inline-block; min-width: 520px; }
pre.out { background: #eee; border-style: dashed; }
td code { white-space: nowrap; }
code { font-size: 0.92em; background: #eee; padding: 0 8px; border-radius: 5px; }
table { border-collapse: collapse; margin: 10px 0; }
th, td { border: 3px solid #111; padding: 6px 24px; font-size: 38px; text-align: center; }
th { background: #ddd; }
td.l { text-align: right; }
.row { display: flex; gap: 40px; align-items: flex-start; }
.ft { position: absolute; bottom: 16px; left: 0; right: 0; text-align: center; font-size: 20px; color: #444; }
.big { font-size: 52px; font-weight: bold; }
"""


def slide(inner, tag=""):
    if tag:
        word, rng = tag.split(" ", 1)
        t = f'<div class="tag">{word} <bdi dir="ltr">{rng}</bdi></div>'
    else:
        t = ""
    return f'<div class="s">{t}{inner}<div class="ft">{FOOTER}</div></div>'


S = []

# ------------------------------------------------------------------ recap (minutes 0-7)
S.append(slide('<h1>חזרה מ-3.1</h1><p class="big">שלושה דברים קטנים לפני שמתחילים לחשב</p>'
               '<ul><li>השמה מרובה</li><li>המרה של משתנה ששמור, ו-<code>str()</code></li><li>שמות: חוק ומוסכמה</li></ul>'
               '<p>כל שקופית שאלה: קודם מנחשים, ורק אז מריצים ב-Thonny.</p>', "דקה 0"))
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>מה יודפס, ולמה?</h2>'
               '<pre>score = 7\nscore = 9\nprint("Score:", score)</pre>', "דקה 0–1"))
S.append(slide('<div class="a">תשובה</div><h2>בקופסה יש ערך אחד בכל רגע</h2>'
               '<pre class="out">Score: 9</pre><p>ההשמה השנייה החליפה את 7. הערך הישן נעלם.</p>', "דקה 0–1"))
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>שורה אחת, שתי השמות. מה יודפס?</h2>'
               '<pre>a, b = 12, 5\nprint(a, b)</pre>', "דקה 1–3"))
S.append(slide('<div class="a">תשובה</div><h2>השמה מרובה</h2><pre class="out">12 5</pre>'
               '<p>הערך הראשון ל-<code>a</code>, השני ל-<code>b</code>. שקול לשתי שורות נפרדות.</p>'
               '<table><tr><th>שורה</th><th><code>a</code></th><th><code>b</code></th></tr>'
               '<tr><td class="l"><code>a, b = 12, 5</code></td><td>12</td><td>5</td></tr></table>', "דקה 1–3"))
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>מה יודפס בכל אחד?</h2>'
               '<pre>x = 7\ny = float(x)\nprint(y, type(y))\n\nt = str(5)\nprint(t, type(t))</pre>', "דקה 3–5"))
S.append(slide('<div class="a">תשובה</div><h2>אפשר להמיר גם משתנה ששמור</h2>'
               '<pre class="out">7.0 &lt;class \'float\'&gt;\n5 &lt;class \'str\'&gt;</pre>'
               '<ul><li><code>float(x)</code>: עותק עשרוני, <code>x</code> נשאר 7</li>'
               '<li><code>str(5)</code>: נראה כמו 5, אבל זה טקסט</li></ul>', "דקה 3–5"))
S.append(slide('<div class="q">מה מטרת הקוד?</div><h2>מקלידים 34. מה יודפס, ומה הקוד עושה?</h2>'
               '<pre>number_int = int(input())\nnumber_float = float(number_int)\nprint(number_float)</pre>', "דקה 3–5"))
S.append(slide('<div class="a">תשובה</div><pre class="out">34.0</pre>'
               '<p class="big">הקוד קולט מספר שלם ומדפיס אותו כמספר עשרוני.</p>', "דקה 3–5"))
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>איזה שם פייתון תקבל?</h2>'
               '<pre>my-fuel = 5\nfor = 5\nFuel = 5</pre>', "דקה 5–7"))
S.append(slide('<div class="a">תשובה</div><h2>חוק בל יעבור או מוסכמה</h2>'
               '<table><tr><th>שם</th><th>תוצאה</th><th>למה</th></tr>'
               '<tr><td><code>my-fuel</code></td><td>שגיאה</td><td class="l">מקף הוא תו מיוחד (נקרא כחיסור)</td></tr>'
               '<tr><td><code>for</code></td><td>שגיאה</td><td class="l">מילה שמורה של פייתון</td></tr>'
               '<tr><td><code>Fuel</code></td><td>רץ</td><td class="l">מוסכמה: מקובל באותיות קטנות, אבל לא חוק</td></tr></table>', "דקה 5–7"))

# ------------------------------------------------------------------ lesson half: ** (minutes 41-44)
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>מה יודפס בכל חלק?</h2>'
               '<pre>print(2 ** 8, 5 ** 2)\nprint(2 + 3 * 4)\nprint((2 + 3) * 4)\nprint(2 + 3 ** 2)</pre>', "דקה 41–44"))
S.append(slide('<div class="a">תשובה</div><h2><code>**</code> היא חזקה, ויש סדר חישוב</h2>'
               '<div class="row"><pre class="out">256 25\n14\n20\n11</pre>'
               '<ol style="font-size:42px;line-height:1.5"><li>סוגריים</li><li><code>**</code> חזקה</li>'
               '<li><code>*</code> <code>/</code> <code>//</code> <code>%</code></li><li><code>+</code> <code>-</code></li></ol></div>', "דקה 41–44"))

# ------------------------------------------------------------------ lab half: swap and self-update (minutes 69-76)
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>רצינו להחליף בין <code>a</code> ל-<code>b</code>. מה יודפס?</h2>'
               '<pre>a = 4\nb = 9\na = b\nb = a\nprint(a, b)</pre>', "דקה 69–76"))
S.append(slide('<div class="a">תשובה</div><h2>הערך הישן של <code>a</code> נמחק</h2><pre class="out">9 9</pre>'
               '<table><tr><th>שורה</th><th><code>a</code></th><th><code>b</code></th></tr>'
               '<tr><td class="l"><code>a = 4</code></td><td>4</td><td>-</td></tr>'
               '<tr><td class="l"><code>b = 9</code></td><td>4</td><td>9</td></tr>'
               '<tr><td class="l"><code>a = b</code></td><td>9</td><td>9</td></tr>'
               '<tr><td class="l"><code>b = a</code></td><td>9</td><td>9</td></tr></table>', "דקה 69–76"))
S.append(slide('<div class="a">התיקון: משתנה שלישי</div><h2>שומרים את <code>a</code> לפני שדורסים אותו</h2>'
               '<div class="row"><pre>a = 4\nb = 9\ntemp = a\na = b\nb = temp\nprint(a, b)</pre><pre class="out">9 4</pre></div>', "דקה 69–76"))
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>מה יודפס? איזה צד של <code>=</code> מחושב קודם?</h2>'
               '<pre>score = 10\nscore = score + 1\nprint(score)</pre>', "דקה 69–76"))
S.append(slide('<div class="a">תשובה</div><pre class="out">11</pre>'
               '<p class="big">קודם מחשבים את צד ימין (10 + 1), ורק אז שומרים ב-<code>score</code>.</p>'
               '<p>ככה מעדכנים משתנה מעצמו.</p>', "דקה 69–76"))


def main(out):
    out = os.path.abspath(out)
    os.makedirs(out, exist_ok=True)
    html = ('<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>%s</body></html>'
            % ("תוספות לשיעור 3.2", CSS, "".join(S)))
    tmp = os.path.join(tempfile.mkdtemp(), "addon.html")
    open(tmp, "w", encoding="utf-8").write(html)
    pdf = os.path.join(out, "m2-addon-slides-he.pdf")
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}",
                    "file:///" + tmp.replace("\\", "/")], check=True, capture_output=True, timeout=120)
    n = fitz.open(pdf).page_count
    print("m2-addon-slides-he.pdf", n, "pages (expected %d)" % len(S))
    if n != len(S):
        print("  a slide overflowed or split: fix the layout")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1])
