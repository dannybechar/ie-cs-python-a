# יחידה 9.3 – תכנות מונחה אירועים

כיתה ז׳ · Python A · **לוחצים על המפה: לחיצה על המסך וקואורדינטות**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> הפעולה `turtle.onscreenclick` מגיבה ללחיצה בכל מקום בחלון, ושולחת את הנקודה שנלחצה.

## דף עזר

```python
def move_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


turtle.onscreenclick(move_to)
```

| המקום בחלון | x | y |
|---|---|---|
| ימין למעלה | חיובי | חיובי |
| שמאל למעלה | שלילי | חיובי |
| שמאל למטה | שלילי | שלילי |
| ימין למטה | חיובי | שלילי |

<div dir="rtl">

- הנקודה (0, 0) נמצאת באמצע החלון.
- בבחינה כותבים `wn.onclick(...)` במקום `turtle.onscreenclick(...)` — אותו דבר.
- לחיצה על הצב נחשבת גם ללחיצה על המסך. מפרידים בין כפתורי העכבר: `btn=1` שמאל, `btn=3` ימין.
- הפקודה `goto` מציירת קו — אלא אם העט מורם.

</div>

## 1. חימום: קו במקום קפיצה

פתחו את `ScreenClick_Starter.py`:

```python
# Warm-up: the rover should jump to the click without drawing a line. Fix it.
import turtle


def move_to(x, y):
    turtle.goto(x, y)


turtle.shape("turtle")
turtle.onscreenclick(move_to)
turtle.done()
```

## 2. משימה 1: חותמות צבעוניות

כתבו פונקציה בשם `mark(x, y)`: חותמת בכל לחיצה, בצבע לפי רבע החלון: ימין למעלה אדום, ימין למטה כחול, שמאל למעלה ירוק, שמאל למטה צהוב. השתמשו ב-`and` וב-`elif`.

## 3. משימה 2: רק חמש

כתבו פונקציה בשם `mark_five(x, y)`: רק 5 חותמות. אחר כך כל לחיצה מדפיסה `Finished`.

בדקו גם לחיצות על הצירים ובקצוות החלון.

## 4. משימה 3 (אתגר): גדל וקטן

כתבו שתי פונקציות עם המשתנה `size`: `grow(x, y)` — לחיצה **על הצב** מגדילה אותו ב-1; `shrink(x, y)` — לחיצה **במקום אחר** מקטינה אותו ב-1 (לא מתחת ל-1). חברו אותן עם `turtle.onclick(grow, btn=1)` ועם `turtle.onscreenclick(shrink, btn=3)`.

בית: `connect(x, y)` — `goto` עם עט למטה, ואז `dot(10, "orange")`. כאן הקו מהחימום הוא המטרה!

## 5. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U9_M3_ScreenClick_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מה ההבדל בין `turtle.onclick` לבין `turtle.onscreenclick`? איך זה נכתב בבחינה?
2. מה מקבלים `x` ו-`y`?
3. איך סופרים לחיצות?

</div>
