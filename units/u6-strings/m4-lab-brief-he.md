# יחידה 6.4 – מחרוזות

כיתה ז׳ · Python A · **כלים לטקסט: פעולות על מחרוזות ונקודת ביקורת**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> פעולות על מחרוזת עונות על שאלה או מחזירות עותק משונה. המחרוזת המקורית לא משתנה.

## דף עזר

| פעולה | דוגמה | תוצאה |
|---|---|---|
| `upper` | `"Hi".upper()` | `HI` |
| `lower` | `"Hi".lower()` | `hi` |
| `count` | `"banana".count("a")` | `3` |
| `find` | `"banana".find("na")` | `2` |
| `startswith` | `"report.pdf".startswith("rep")` | `True` |
| `endswith` | `"report.pdf".endswith(".pdf")` | `True` |
| `isalpha` | `"A12".isalpha()` | `False` |
| `isnumeric` | `"12345".isnumeric()` | `True` |
| `replace` | `"a-b".replace("-", "*")` | `a*b` |

```python
import turtle
turtle.write("Hello", align="center", font=("Arial", 24, "normal"))
```

<div dir="rtl">

- הפעולה `find` מחזירה את האינדקס של ההופעה הראשונה, או `-1` אם אין התאמה.
- הפעולות `upper`, `lower` ו-`replace` מחזירות מחרוזת חדשה.

</div>

## 1. חימום: למה Rejected?

פתחו את `Methods_Starter.py`, הריצו והקלידו `Yes`:

```python
# Warm-up: the user types Yes, but the program says Rejected. Why?
answer = input("Answer: ")
if answer == "yes":
    print("Accepted")
else:
    print("Rejected")
```

## 2. משימה 1: קובץ וטלפון

<div dir="rtl">

1. כתבו פונקציה בשם `file_check()` שמדפיסה `Python file` אם שם הקובץ מסתיים ב-`.py`, גם כשהוא כתוב `.PY`.
2. כתבו פונקציה בשם `hide_phone()` שמחליפה את המקפים בכוכביות: `050-123-4567` ← `050*123*4567`.

</div>

## 3. משימה 2: כרטיס שם ב-Turtle

כתבו פונקציה בשם `name_card()` שקולטת שם וכותבת במרכז המסך `Hello` והשם באותיות גדולות, בכחול, בלי צורת הצב.

## 4. נקודת ביקורת א׳ (לבד)

<div dir="rtl">

1. כתבו פונקציה בשם `text_report()` שקולטת משפט ומדפיסה: אורך, כמה פעמים מופיעה `a` (גדולה או קטנה), האינדקס של הרווח הראשון, האם המשפט מתחיל ב-`H`, והמשפט באותיות גדולות.
2. כתבו פונקציה בשם `code_check()`: קוד תלמיד תקין אם יש בו 6 ספרות בדיוק. היא מדפיסה `Valid` או `Invalid`.

</div>

בדקו את `text_report()` עם `Hello Mars and Saturn`, ואת `code_check()` עם `123456`, `12a456` ו-`12345`.

## 5. נקודת ביקורת ב׳ (על דף, בלי להריץ)

```python
text = "rover-42"
```

<div dir="rtl">

1. מה הערכים של `len(text)`, `text[0]` ו-`text[len(text) - 1]`?
2. מה נותנים `text[:5]`, `text[6:]` ו-`text[::2]`?
3. מה נותנים `text.find("-")`, `text.count("r")` ו-`"Rover" in text`?
4. מה נותן `"ab" + "c" * 3`? ומה ההבדל בין `"5" + "5"` לבין `5 + 5`?

</div>

## 6. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U6_M4_Methods_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מה מחזירה `find` כשאין התאמה?
2. מה ההבדל בין `isalpha` לבין `isnumeric`?
3. האם `replace` משנה את המחרוזת המקורית?

</div>
