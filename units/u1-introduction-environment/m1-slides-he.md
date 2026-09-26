---
marp: true
theme: g7-rtl
paginate: true
footer: G7 · Unit 1
---

<!-- _class: lead -->
<!-- _paginate: false -->

# יחידה 1 · התוכנית הראשונה שלי

## סדר · פלט · תיעוד · פונקציה ראשונה

כיתה ז׳ · Python A · Predict before run

---

# לפני שמריצים — מה יודפס?

קודם קוראים. אחר כך חוזים. רק אז מריצים.

```python
print("Good morning")
print("Welcome to Python")
print("Ready!")
```

כתבו או אמרו את שלוש שורות הפלט בסדר המדויק.

---

# הסדר משנה

שפת Python מבצעת הוראה אחרי הוראה.

<div dir="rtl">

| תוכנית 1 | תוכנית 2 |
|---|---|
| `print("A")`<br>`print("B")`<br>`print("C")` | `print("C")`<br>`print("A")`<br>`print("B")` |

</div>

האם שתי התוכניות נותנות אותו פלט?

---

# הוראת print() מציגה פלט

```python
print("Hello")
```

<div dir="rtl">

| | |
|---|---|
| **קוד** | הוראה ש-Python מבצע |
| **פלט** | מה שמופיע על המסך |

</div>

---

# הערה (comment) מיועדת לאדם שקורא את הקוד

```python
# This program prints a greeting
print("Hello")
```

איזו שורה תופיע בפלט?

התו `#` מתחיל הערה. Python לא מבצע אותה כהוראה.

---

# הגדרנו פונקציה. האם היא כבר רצה?

```python
def say_hello():
    print("Hello")
    print("Welcome")
```

מה יודפס אם נריץ עכשיו?

---

# Define → Call → Execute

שלושה שלבים בלבד בשלב הזה.

<div dir="rtl">

| שלב | מה קורה |
|---|---|
| **Define** | מגדירים מה הפונקציה יודעת לעשות. |
| **Call** | מבקשים מ-Python לבצע אותה. |
| **Execute** | ההוראות שבתוך הפונקציה מתבצעות. |

</div>

```python
say_hello()
```

---

# הזחה: מי שייך לפונקציה?

```python
def introduce_me():
    print("My name is Dana")
    print("I like basketball")

introduce_me()
```

כל השורות ששייכות לפונקציה מוזחות פנימה ומיושרות באותה צורה.

---

# עקבו אחרי הקוד: מה יהיה סדר הפלט?

```python
print("Start")

def say_hello():
    print("Hello")
    print("Welcome")

print("Ready")
say_hello()
print("End")
```

אל תריצו עדיין.

---

# דרך העבודה שלנו

**Open → Read → Predict → Run → Check → Modify → Comment → Save**

לא רק “להריץ”. קודם קוראים וחוזים, אחר כך בודקים.

---

# Tool Note – Thonny

רק החלק הזה תלוי בכלי שבו נבחר.

<div dir="rtl">

| פעולה | בתפריט | מה זה עושה |
|---|---|---|
| **Open** | `File → Open` | פתיחת קובץ קיים |
| **Run** | `Run → Run current script` | הרצת הקובץ הנוכחי |
| **Save As** | `File → Save As` | שמירה בשם חדש |

</div>

אחרי `:` ולחיצה על Enter, Thonny בדרך כלל מזיח את השורה הבאה אוטומטית.

---

# המעבדה: קובץ אחד שמתפתח

<div dir="rtl">

1. פתחו את הקובץ
2. קראו → חזו → הריצו → בדקו
3. שנו את התוכנית
4. שנו את סדר הפלט
5. הוסיפו הערות
6. השלימו את הפונקציה
7. חזו את הפלט הסופי
8. שמרו בשם חדש

</div>

---

# Final Predict Challenge

כתבו את הפלט המדויק לפני Run.

```python
# My first Python program

print("Start")

def introduce_me():
    print("My name is ...")
    print("I like ...")

print("Ready")
introduce_me()
print("End")
```

---

# מסיימים נכון

<div dir="rtl">

| | |
|---|---|
| **Save As** | `G7_U1_FirstProgram_<Name>.py` |
| **אני מסוגל/ת** | לקרוא קוד, לחזות מה יקרה, להריץ, לבדוק, לשנות, לתעד ולשמור. |

</div>

המטרה היום הייתה להתחיל לעבוד עם קוד Python בצורה נכונה.

**Open → Read → Predict → Run → Check → Modify → Comment → Save**
