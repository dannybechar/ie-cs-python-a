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

כתבו פונקציה בשם `mark(x, y)`: חותמת בכל לחיצה — כחולה מעל האמצע (`y > 0`), אדומה מתחתיו.

## 3. משימה 2: רק חמש

כתבו פונקציה בשם `mark_five(x, y)`: רק 5 חותמות. אחר כך כל לחיצה מדפיסה `Finished`.

בדקו גם לחיצות על הצירים ובקצוות החלון.

## 4. משימה 3 (אתגר): מחברים נקודות

כתבו פונקציה בשם `connect(x, y)`: `goto` עם עט למטה, ואז `dot(10, "orange")`. כאן הקו מהחימום הוא המטרה!

## 5. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U9_M3_ScreenClick_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מה ההבדל בין `turtle.onclick` לבין `turtle.onscreenclick`?
2. מה מקבלים `x` ו-`y`?
3. איך סופרים לחיצות?

</div>
