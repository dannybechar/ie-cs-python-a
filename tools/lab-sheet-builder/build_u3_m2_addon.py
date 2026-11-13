"""Builds the Unit 3.2 add-on slides (16:9 PDF, Hebrew, RTL): 8 slides, the most the teacher can show.
They cover only what the NotebookLM deck m2-slides-he.pdf lacks: the 3.1 recap, `**`, swap, self-update.

Usage: python build_u3_m2_addon.py <output folder>      (writes m2-addon-slides-he.pdf)
Question slides never show their answer; the answer is the next slide (or the live run in Thonny).
Code is always left-to-right. Edit with the Edit/Write tools, not shell heredocs (Hebrew gets mangled).
"""
import os
import subprocess
import sys
import tempfile

import fitz  # PyMuPDF, page count check only

EDGE = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
FOOTER = "יחידה 3.2 – משתנים, קלט/פלט וחישובים"
MAX_SLIDES = 8

CSS = """
@page { size: 1280px 720px; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { direction: rtl; font-family: 'Segoe UI', Arial, sans-serif; color: #111; }
.s { width: 1280px; height: 720px; padding: 46px 70px 62px; position: relative; page-break-after: always; overflow: hidden; background: #fff; }
.s:last-child { page-break-after: auto; }
.tag { position: absolute; top: 22px; left: 28px; font-size: 20px; color: #444; direction: rtl; }
h2 { font-size: 46px; margin: 0 0 14px; }
.q { display: block; width: max-content; background: #111; color: #fff; font-size: 26px; padding: 3px 18px; border-radius: 6px; margin: 0 0 10px; }
.a { display: block; width: max-content; border: 4px solid #111; font-size: 26px; padding: 0 16px; border-radius: 6px; margin: 0 0 10px; }
p, li { font-size: 40px; line-height: 1.4; margin: 6px 0; }
ul { margin: 6px 0; padding-right: 36px; }
code, pre { font-family: Consolas, 'Courier New', monospace; direction: ltr; unicode-bidi: isolate; }
pre { font-size: 50px; line-height: 1.32; margin: 12px 0; padding: 16px 28px; border: 4px solid #111; border-radius: 10px; text-align: left; display: inline-block; min-width: 520px; }
pre.sm { font-size: 38px; line-height: 1.3; margin: 6px 0; padding: 10px 22px; min-width: 0; }
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

# 1-2  recap of 3.1 (minutes 0-5): three snippets, run live in Thonny after the students predict
S.append(slide('<div class="q">ניחוש לפני הרצה · חזרה מ-3.1</div><h2>מה יודפס בכל אחד? ומה מטרת הקוד השלישי?</h2>'
               '<div class="row"><pre class="sm">a, b = 12, 5\nprint(a, b)</pre>'
               '<pre class="sm">x = 7\ny = float(x)\nprint(y, type(y))\nt = str(5)\nprint(t, type(t))</pre></div>'
               '<pre class="sm">number_int = int(input())       # type 34\nnumber_float = float(number_int)\nprint(number_float)</pre>', "דקה 0–5"))
S.append(slide('<div class="a">תשובות</div>'
               '<table><tr><th>קוד</th><th>מודפס</th><th>מה למדנו</th></tr>'
               '<tr><td><code>a, b = 12, 5</code></td><td><code>12 5</code></td><td class="l">שורה אחת, שתי השמות, לפי הסדר</td></tr>'
               '<tr><td><code>float(x)</code></td><td><code>7.0</code></td><td class="l">עותק עשרוני; <code>x</code> נשאר 7</td></tr>'
               '<tr><td><code>str(5)</code></td><td><code>5</code> (טקסט)</td><td class="l">נראה כמו מספר, אבל <code>str</code></td></tr>'
               '<tr><td>הקוד השלישי</td><td><code>34.0</code></td><td class="l">קולט מספר שלם ומדפיס אותו כמספר עשרוני</td></tr></table>', "דקה 0–5"))

# 3-4  ** and order of operations (minutes 41-44)
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>מה יודפס בכל שורה?</h2>'
               '<pre>print(2 ** 8, 5 ** 2)\nprint(2 + 3 * 4)\nprint((2 + 3) * 4)\nprint(2 + 3 ** 2)</pre>', "דקה 41–44"))
S.append(slide('<div class="a">תשובה</div><h2><code>**</code> היא חזקה, ויש סדר חישוב</h2>'
               '<div class="row"><pre class="out">256 25\n14\n20\n11</pre>'
               '<ol style="font-size:42px;line-height:1.5"><li>סוגריים</li><li><code>**</code> חזקה</li>'
               '<li><code>*</code> <code>/</code> <code>//</code> <code>%</code></li><li><code>+</code> <code>-</code></li></ol></div>', "דקה 41–44"))

# 5-6  swap (minutes 69-76)
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>רצינו להחליף בין <code>a</code> ל-<code>b</code>. מה יודפס?</h2>'
               '<pre>a = 4\nb = 9\na = b\nb = a\nprint(a, b)</pre>', "דקה 69–76"))
S.append(slide('<div class="a">תשובה: <code>9 9</code>. הערך הישן של <code>a</code> נמחק</div>'
               '<div class="row"><table><tr><th>שורה</th><th><code>a</code></th><th><code>b</code></th></tr>'
               '<tr><td class="l"><code>a = 4</code></td><td>4</td><td>-</td></tr>'
               '<tr><td class="l"><code>b = 9</code></td><td>4</td><td>9</td></tr>'
               '<tr><td class="l"><code>a = b</code></td><td>9</td><td>9</td></tr>'
               '<tr><td class="l"><code>b = a</code></td><td>9</td><td>9</td></tr></table>'
               '<div><p style="margin:0 0 4px">התיקון: משתנה שלישי</p>'
               '<pre class="sm">temp = a\na = b\nb = temp</pre><pre class="sm out">9 4</pre></div></div>', "דקה 69–76"))

# 7  self-update question (the answer is run live: 11)   8  the four things to remember
S.append(slide('<div class="q">ניחוש לפני הרצה</div><h2>מה יודפס? איזה צד של <code>=</code> מחושב קודם?</h2>'
               '<pre>score = 10\nscore = score + 1\nprint(score)</pre>', "דקה 69–76"))
S.append(slide('<h2>ארבעה דברים לזכור</h2>'
               '<ul><li><code>a, b = 12, 5</code>: שתי השמות בשורה אחת</li>'
               '<li><code>float(x)</code>, <code>str(x)</code>: עותק מומר, המקור לא משתנה</li>'
               '<li><code>**</code> חזקה; קודם סוגריים, אחר כך <code>**</code>, אחר כך <code>*</code> ו-<code>+</code></li>'
               '<li>החלפה: צריך <code>temp</code>. עדכון: <code>score = score + 1</code>, צד ימין מחושב קודם (תשובה: 11)</li></ul>', "דקה 76"))

assert len(S) <= MAX_SLIDES, "too many slides: %d" % len(S)


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
