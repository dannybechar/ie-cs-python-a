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
| `find` מצב התחלה | `"banana".find("a", 2)` | `3` |
| `index` | `"banana".index("na")` | `2` |
| `startswith` | `"report.pdf".startswith("rep")` | `True` |
| `startswith` מצב התחלה | `"playlist".startswith("list", 4)` | `True` |
| `endswith` | `"report.pdf".endswith(".pdf")` | `True` |
| `isalpha` (לא בדף העזר של הבחינה) | `"A12".isalpha()` | `False` |
| `isdigit` (לא בדף העזר של הבחינה) | `"12345".isdigit()` | `True` |
| `replace` | `"a-b".replace("-", "*")` | `a*b` |
| `replace` עם מספר פעמים | `"a-b-c".replace("-", "*", 1)` | `a*b-c` |

```python
import turtle
turtle.write("Hello", align="center", font=("Arial", 24, "normal"))

# הצורה שבה הבחינה כותבת את אותו דבר
wn = turtle.Screen()
pen = turtle.Turtle()
pen.write("Hello", align="center", font=("Arial", 24, "normal"))
wn.mainloop()
```

<div dir="rtl">

- הפעולה `find` מחזירה את האינדקס של ההופעה הראשונה, או `-1` אם אין התאמה. הפעולה `index` עושה אותו דבר, אבל כשאין התאמה היא נופלת בשגיאה.
- מספר שני ב-`find`, ב-`count` וב-`startswith` אומר מאיפה להתחיל. מספר שלישי ב-`replace` אומר כמה החלפות לעשות.
- `isnumeric` הוא השם בחוברת התוכנית, ו-`isdigit` הוא השם בתרגילי הבחינה. על ספרות התוצאה זהה. יש גם `islower` ו-`isupper`.
- הפעולות `upper`, `lower` ו-`replace` מחזירות מחרוזת חדשה.
- בנקודת ביקורת ב׳ משתמשים רק בדף העזר המודפס של הבחינה.
- מילון: פונקציה שכתבתם נקראת בבחינה **פעולה**. בדף העזר של הבחינה יש יותר ממה שלמדנו (רשימות, תור): מתעלמים מהם.

</div>

## 1. חימום: למה Rejected?

פתחו את `Methods_Starter.py`, הריצו והקלידו `Yes`:

```python
# Warm-up: the user types Yes,
# but the program says Rejected. Why?
answer = input("Answer: ")
if answer == "yes":
    print("Accepted")
else:
    print("Rejected")
```

## 2. משימה 1: קובץ וטלפון

<div dir="rtl">

1. כתבו פונקציה בשם `file_check()` שמדפיסה `Python file` אם שם הקובץ מסתיים ב-`.py`, גם כשהוא כתוב `.PY`.
2. כתבו פונקציה בשם `hide_phone()` שמחליפה את המקפים בכוכביות: `050-123-4567` ← `050*123*4567`. חיזוי: מה נותן `phone.replace("-", "*", 1)`?

</div>

## 3. משימה 2: כרטיס שם ב-Turtle

כתבו פונקציה בשם `name_card()` שקולטת שם וכותבת במרכז המסך `Hello` והשם באותיות גדולות, בכחול, בלי צורת הצב.

## 4. משימה 3: אותו כרטיס בניב הבחינה

תרגמו את `name_card()` לצורה שבה הבחינה כותבת: `wn = turtle.Screen()`, `pen = turtle.Turtle()`, `pen.write(...)`, `wn.mainloop()`. השתמשו בטבלת התרגום מיחידה 2.

## 5. נקודת ביקורת א׳ (לבד)

<div dir="rtl">

1. כתבו פונקציה בשם `text_report()` שקולטת משפט ומדפיסה: אורך, כמה פעמים מופיעה `a` (גדולה או קטנה), האינדקס של הרווח הראשון, האם המשפט מתחיל ב-`H`, התו האחרון (`text[-1]`), והמשפט באותיות גדולות.
2. כתבו פונקציה בשם `code_check()`: קוד תלמיד תקין אם יש בו 6 ספרות בדיוק (`isdigit()`). היא מדפיסה `Valid` או `Invalid`.

</div>

בדקו את `text_report()` עם `Hello Mars and Saturn`, ואת `code_check()` עם `123456`, `12a456` ו-`12345`.

## 6. נקודת ביקורת ב׳ (על דף, בלי להריץ, עם דף העזר של הבחינה)

```python
text = "rover-42"
```

<div dir="rtl">

1. השלימו את הטבלה:

</div>

| פקודה | פלט |
|---|---|
| `len(text)` | |
| `text[-1]` | |
| `text[:5]` | |
| `text[2:-2]` | |
| `text[::2]` | |
| `text.find("-")` | |

<div dir="rtl">

2. מה נותנים `text.count("r")`, `"Rover" in text` ו-`"-" not in text`?
3. מה נותן `"ab" + "c" * 3`? ומה ההבדל בין `str(5) + "5"` לבין `5 + 5`?

</div>

## 7. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U6_M4_Methods_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מה מחזירה `find` כשאין התאמה? ומה עושה `index`?
2. מה ההבדל בין `isalpha` לבין `isdigit`?
3. האם `replace` משנה את המחרוזת המקורית?

</div>
