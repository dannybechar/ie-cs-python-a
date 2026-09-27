# יחידה 4.3 – ביצוע מותנה

כיתה ז׳ · Python A · **הרובר בצומת: תנאים מורכבים, קינון ו-Turtle**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> שתי שאלות, החלטה אחת: מחברים אותן עם `and` או `or`, או שואלים את השנייה בתוך הראשונה.

## דף עזר

```python
# Nested
if age >= 12:
    if has_ticket == "yes":
        print("Enter")

# Compound
if age >= 12 and has_ticket == "yes":
    print("Enter")
```

<div dir="rtl">

- ה-`if` הפנימי נבדק רק כשהתנאי החיצוני `True`.
- כל רמת קינון מוסיפה 4 רווחים.
- כל צד של `or` צריך השוואה משלו.

</div>

## 1. משימה 1: האם הרובר זז?

<div dir="rtl">

1. כתבו פונקציה בשם `rover_move()` שקולטת `battery` (מספר) ו-`obstacle` (`yes` או `no`). היא מדפיסה `Move forward` רק אם הסוללה לפחות 20 **וגם** אין מכשול. אחרת היא מדפיסה `Stop`.
2. כתבו פונקציה בשם `rover_move_nested()` שמחליטה אותו דבר עם `if` מקונן.

</div>

<div dir="rtl">

| `battery` | `obstacle` | הפלט |
|---|---|---|
| 50 | no | &nbsp; |
| 50 | yes | &nbsp; |
| 10 | no | &nbsp; |
| 20 | no | &nbsp; |

</div>

איזו גרסה קצרה יותר? למה שתיהן מדפיסות אותו דבר?

## 2. משימה 2: הרובר מצייר לפי בחירה

פתחו את `Shapes_Starter.py`. התוכנית מציירת גם ריבוע וגם משולש. הוסיפו תנאים והזחה:

<div dir="rtl">

1. מציירים רק אם `size` בין 20 ל-200, כולל. אחרת מדפיסים `Invalid size`.
2. בפנים: `square` ← ריבוע כחול. כל תשובה אחרת ← משולש ירוק.

</div>

בדקו עם `square` ו-100, עם `triangle` ו-100, ועם `square` ו-10.

## 3. נקודת ביקורת א׳ (לבד)

כתבו פונקציה בשם `ticket_price()` שקולטת גיל:

<div dir="rtl">

- גיל קטן מ-0 או גדול מ-120 ← `Invalid age`
- אחרת: מתחת ל-12 **או** 65 ומעלה ← `Price: 20`, ואחרת ← `Price: 40`

</div>

בדקו עם מינוס 1, עם 5, עם 12, עם 64, עם 65 ועם 130.

## 4. נקודת ביקורת ב׳: טבלת מעקב (בלי להריץ)

```python
fuel = 80
weather = "clear"

if fuel >= 50:
    if weather == "clear" or weather == "cloudy":
        print("Launch")
    else:
        print("Wait for weather")
else:
    print("Refuel")
print("Check done")
```

<div dir="rtl">

| `fuel` | `weather` | `fuel >= 50` | הפלט |
|---|---|---|---|
| 80 | clear | &nbsp; | &nbsp; |
| 80 | storm | &nbsp; | &nbsp; |
| 30 | clear | &nbsp; | &nbsp; |
| 50 | cloudy | &nbsp; | &nbsp; |

</div>

## 5. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U4_M3_Conditions_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מתי משתמשים ב-`and`, ומתי ב-`or`?
2. ב-`if` מקונן, איזה תנאי נבדק קודם?
3. כתבו תנאי מורכב אחד לבדיקת הכרטיס המקוננת.

</div>
