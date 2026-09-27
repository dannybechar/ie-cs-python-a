# יחידה 8.4 – פונקציות עם פרמטרים

כיתה ז׳ · Python A · **מי מכיר את המשתנה? טווח הכרה, global ונקודת ביקורת**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> משתנה שנוצר בתוך פונקציה קיים רק בה. כדי לשנות משתנה חיצוני בתוך פונקציה, מצהירים עליו `global`.

## דף עזר

```python
score = 0


def add_point():
    global score
    score = score + 1


add_point()
add_point()
print(score)
```

| | משתנה מקומי | משתנה `global` |
|---|---|---|
| איפה נוצר | בתוך פונקציה | מחוץ לכל הפונקציות |
| איפה מוכר | רק בפונקציה שלו | בכל התוכנית |
| שינוי בתוך פונקציה | השמה רגילה | צריך קודם `global` |

<div dir="rtl">

- לקרוא משתנה חיצוני אפשר בלי `global`. לשנות אותו — רק עם `global`.
- ערכים שהפונקציה צריכה — שולחים בפרמטרים. את `global` שומרים למצב משותף, כמו מונה.

</div>

## 1. חימום: למה התוכנית נופלת?

פתחו את `Scope_Starter.py`:

```python
# Warm-up: add_point() should add 1 to score. Why does it crash?
score = 0


def add_point():
    score = score + 1


add_point()
print(score)
```

## 2. משימה 1: ספירלה שגדלה

המשתנה `steps = 40` נמצא מחוץ לפונקציות. כתבו פונקציה בשם `grow_step()` שמצהירה `global steps`, מתקדמת `steps`, פונה 90 ומוסיפה 15 ל-`steps`. זמנו אותה 6 פעמים בלולאה.

## 3. נקודת ביקורת א׳ (לבד)

<div dir="rtl">

1. כתבו פונקציה בשם `draw_square(size)` שמציירת ריבוע בגודל `size` ומוסיפה 1 למונה `global` בשם `squares_drawn`.
2. כתבו פונקציה בשם `show_line(symbol, amount)` שמדפיסה `symbol * amount`.
3. כתבו פונקציה בשם `checkpoint()`: קו של 20 סימני `=`, ריבועים בגדלים 40, 70 ו-100, ההדפסה `Squares: 3`, ועוד קו.

</div>

## 4. נקודת ביקורת ב׳ (על דף, בלי להריץ)

```python
count = 0


def tick(step):
    global count
    count = count + step


tick(2)
tick(5)
print(count)
```

<div dir="rtl">

1. מה יודפס?
2. מהו הפרמטר, ומהם הארגומנטים?
3. מה יקרה אם נמחק את השורה `global count`?
4. הפונקציה `show(a, b)` מדפיסה `a - b`. מה ידפיסו `show(10, 4)` ו-`show(4, 10)`?

</div>

## 5. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U8_M4_Scope_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. איפה מוכר משתנה מקומי?
2. מתי צריך `global`?
3. המשתנה `calls = 0`, ופונקציה מוסיפה לו 1 עם `global calls`. מזמנים אותה 3 פעמים — מה יודפס?

</div>
