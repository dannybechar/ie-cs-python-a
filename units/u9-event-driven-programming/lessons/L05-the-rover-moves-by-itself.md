# יחידה 9.5 – תכנות מונחה אירועים

כיתה ז׳ · Python A · **הרובר זז לבד: אנימציה עם טיימר**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> אנימציה היא הרבה שינויים קטנים: פונקציית צעד זזה מעט, ומבקשת מהטיימר לזמן אותה שוב בעוד כמה אלפיות שנייה.

## דף עזר

```python
def animate():
    turtle.forward(5)
    turtle.ontimer(animate, 50)


animate()
turtle.done()
```

<div dir="rtl">

- הזימון הראשון `animate()` מתחיל את השרשרת.
- המרחק בכל צעד קובע כמה רחוק. הזמן של הטיימר קובע כמה פעמים.
- קפיצה מהקצה: `dx = -dx` הופך את הכיוון.
- עצירה: כש-`running` הוא `False`, הצעד לא מתזמן את הצעד הבא.

</div>

## 1. חימום: RecursionError

פתחו את `Timer_Starter.py`:

```python
# Warm-up: the rover should move 5 steps every 50 milliseconds.
# The program crashes with RecursionError. Why?
import turtle


def animate():
    turtle.forward(5)
    turtle.ontimer(animate(), 50)


turtle.shape("turtle")
animate()
turtle.done()
```

## 2. משימה 1: קופץ מהקצוות

כתבו פונקציה בשם `bounce()`: הצב זז עם `dx`, והופך כיוון ב-`-200` וב-200.

## 3. משימה 2: עצירה והפעלה

רווח מפעיל את `stop()`. המקש `s` מפעיל את `start()`, שמתחילה שרשרת חדשה רק אם האנימציה עצורה.

## 4. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U9_M5_Timer_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מה עושה `turtle.ontimer`?
2. מה ההבדל בין המרחק בכל צעד לבין הזמן של הטיימר?
3. איך עוצרים שרשרת של זימוני טיימר?

</div>
