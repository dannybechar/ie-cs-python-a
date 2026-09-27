# יחידה 9.1 – תכנות מונחה אירועים

כיתה ז׳ · Python A · **הרובר מחכה לפקודות: אירוע, מאזין ותגובה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> בתוכנית מונחית אירועים המשתמש קובע מה יקרה עכשיו: אירוע קורה, מאזין מזהה אותו, ופונקציית תגובה רצה.

## דף עזר

```python
import turtle


def say_hello(x, y):
    print("Hello")


turtle.shape("turtle")
turtle.onclick(say_hello)
turtle.done()
```

| מושג | בקוד |
|---|---|
| אירוע | לחיצה על הצב |
| מאזין | `turtle.onclick(say_hello)` |
| פונקציית תגובה | `say_hello(x, y)` |
| לולאת האירועים | `turtle.done()` |

<div dir="rtl">

- מוסרים למאזין את **שם** הפונקציה, בלי סוגריים.
- לחיצה שולחת את המקום שלה, ולכן לפונקציה יש שני פרמטרים: `x` ו-`y`.

</div>

## 1. חימום: נופל לפני שלוחצים

פתחו את `Events_Starter.py`:

```python
# Warm-up: the program crashes before anyone clicks. Why?
import turtle


def say_hello(x, y):
    print("Hello")


turtle.shape("turtle")
turtle.onclick(say_hello())
turtle.done()
```

## 2. משימה 1: איפה לחצו?

כתבו פונקציה בשם `report_click(x, y)` שמדפיסה `Clicked` ואת שתי הקואורדינטות.

## 3. משימה 2: לחיצה מזיזה

כתבו פונקציה בשם `turn_and_move(x, y)`: בכל לחיצה על הצב הוא פונה 90 ומתקדם 50. אחרי כמה לחיצות הוא חוזר למקום?

## 4. משימה 3 (אתגר): סופרים לחיצות

כתבו פונקציה בשם `count_click(x, y)` שמעדכנת מונה `global` ומדפיסה `Clicks: 1`, `Clicks: 2` וכן הלאה.

## 5. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U9_M1_Events_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מהו אירוע?
2. מה התפקיד של המאזין?
3. למה מוסרים את שם הפונקציה בלי סוגריים?

</div>
