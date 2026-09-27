# יחידה 9.2 – תכנות מונחה אירועים

כיתה ז׳ · Python A · **לוחצים על הרובר: onclick, קואורדינטות ומצב**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> הפעולה `turtle.onclick` מגיבה רק ללחיצה על הצב. משתנה שצריך להישמר בין לחיצות נמצא מחוץ לפונקציה, ומשנים אותו עם `global`.

## דף עזר

```python
current = "blue"


def toggle_color(x, y):
    global current
    if current == "blue":
        current = "orange"
    else:
        current = "blue"
    turtle.color(current)
```

<div dir="rtl">

- לפונקציית תגובה ללחיצה יש תמיד `(x, y)`, גם אם היא לא משתמשת בהם.
- הפקודה `big = not big` הופכת את הערך הבוליאני.
- בדיקה: שני פרמטרים · שם הפונקציה בלי סוגריים · `turtle.done()` בסוף.

</div>

## 1. חימום: שגיאה בלחיצה

פתחו את `TurtleClick_Starter.py`, הריצו ולחצו על הצב:

```python
# Warm-up: click the rover. It should turn red. Why is there an error?
import turtle


def change_color():
    turtle.color("red")


turtle.shape("turtle")
turtle.onclick(change_color)
turtle.done()
```

## 2. משימה 1: צבע מתחלף

כתבו פונקציה בשם `toggle_color(x, y)`: כחול ← כתום ← כחול, בכל לחיצה.

## 3. משימה 2: גודל מתחלף

כתבו פונקציה בשם `toggle_size(x, y)` עם המשתנה `big`: גודל 3 או גודל 1 (`turtle.shapesize`).

## 4. משימה 3 (אתגר): חמישה צעדים

כתבו פונקציה בשם `step_forward(x, y)`: כל לחיצה מקדמת את הצב 40. אחרי 5 לחיצות הוא מדפיס `Arrived` ולא זז יותר.

## 5. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U9_M2_TurtleClick_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. על מה מגיבה `turtle.onclick`?
2. למה הפונקציה מקבלת `x` ו-`y`?
3. מתי צריך `global`?

</div>
