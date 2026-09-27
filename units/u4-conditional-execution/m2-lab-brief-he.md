# יחידה 4.2 – ביצוע מותנה

כיתה ז׳ · Python A · **הרובר מחליט: if ו-if/else**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> התשובה לשאלה (`True` או `False`) קובעת אילו שורות ירוצו.

## דף עזר

```python
number = int(input("Number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
print("Done")
```

<div dir="rtl">

- אחרי התנאי — נקודתיים `:`
- גוף ה-`if` וגוף ה-`else` — מוזחים (4 רווחים).
- בכל הרצה רץ **מסלול אחד בדיוק**: `if` או `else`.
- השורה `print("Done")` לא מוזחת, ולכן היא רצה תמיד.

</div>

> [!TIP]
> שגיאה? קוראים את ההודעה, מתקנים דבר אחד, ומריצים שוב.

## 1. חימום: טבלת מעקב

פתחו את `Decisions_Starter.py`. אל תריצו עדיין!

```python
# Rover delivery: which branch runs?
amount = 49

if amount >= 50:
    print("Free delivery")
else:
    print("Delivery fee")

print("Order saved")
```

השלימו את הטבלה. אחר כך שנו את `amount` והריצו כל מקרה.

<div dir="rtl">

| `amount` | `amount >= 50` | הפלט |
|---|---|---|
| 49 | &nbsp; | &nbsp; |
| 50 | &nbsp; | &nbsp; |
| 80 | &nbsp; | &nbsp; |

</div>

## 2. משימה 1: עובר או לא

כתבו פונקציה בשם `grade_check()` שקולטת ציון ומדפיסה `Passed` אם הציון 60 ומעלה, ואחרת `Try again`.

בדקו את הגבול: 59, 60 ו-61. חזו לפני כל הרצה.

## 3. משימה 2: מצאו את הבאגים

פתחו את `ScoreBug_Starter.py`:

```python
# Fix ONE bug per run, then run again.
score = int(input("Score: "))
if score = 100
print("Perfect")
else:
print("Not perfect")
```

<div dir="rtl">

1. מריצים וקוראים את הודעת השגיאה.
2. מתקנים באג **אחד** בלבד, ומריצים שוב.
3. חוזרים על זה עד שהתוכנית עובדת. כמה הודעות שגיאה שונות קיבלתם?
4. מעתיקים את הקוד המתוקן לפונקציה בשם `perfect_check()` בקובץ שלכם. בודקים עם 100 ועם 99.

</div>

## 4. משימה 3: מסננת קלט

כתבו פונקציה בשם `battery_filter()` שקולטת את רמת הסוללה ומדפיסה `Valid battery` אם היא בין 0 ל-100, כולל. אחרת היא מדפיסה `Invalid battery`.

בדקו עם מינוס 5, עם 0, עם 57, עם 100 ועם 101.

## 5. משימה 4 (אתגר): הנחה

כתבו פונקציה בשם `discount()` שקולטת מחיר (`float`). מ-100 ומעלה המחיר הסופי נמוך ב-10% (`price * 0.9`). אחרת המחיר לא משתנה. התוכנית מדפיסה:

```text
Final price: ...
```

בדקו עם 100, עם 99.5 ועם 250.

## 6. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U4_M2_Decisions_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מתי גוף ה-`if` רץ?
2. מה מסמנת ההזחה?
3. כמה מסלולים של `if/else` רצים בהרצה אחת?

</div>
