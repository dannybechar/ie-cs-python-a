# יחידה 7.3 – בעיות אלגוריתמיות

כיתה ז׳ · Python A · **מטילים קובייה: מספרים אקראיים, סימולציה ונקודת ביקורת**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> הפעולה `random.randint(a, b)` מחזירה מספר שלם מ-a עד b — כולל שניהם. מגרילים פעם אחת, שומרים במשתנה, ואז משתמשים.

## דף עזר

| קריאה | ערכים אפשריים |
|---|---|
| `random.randint(1, 6)` | 1 עד 6 — קובייה |
| `random.randint(0, 1)` | 0 או 1 — מטבע |
| `random.randint(10, 20)` | 10 עד 20 |
| `random.randrange(1, 7)` | 1 עד 6 — הגבול העליון **לא** נכלל, כמו ב-`range` |
| `random.random()` | מספר עשרוני מ-0 ועד קטן מ-1 |

```python
import random

roll = random.randint(1, 6)
print("Roll:", roll)
if roll == 6:
    print("You win")
```

<div dir="rtl">

- ב-`randint`, בניגוד ל-`range`, הגבול העליון נכלל. ב-`randrange` הוא לא נכלל.
- כל קריאה ל-`randint` מגרילה מספר חדש.

</div>

## 1. משימה 1: הליכה אקראית ב-Turtle

כתבו פונקציה בשם `random_walk()`: 20 צעדים. בכל צעד הצב פונה `random.randint(0, 360)` ומתקדם `random.randint(10, 40)`.

ספרו כמה צעדים ארוכים מ-30, וצברו את המרחק הכולל. הדפיסו את שניהם.

## 2. נקודת ביקורת א׳ (לבד)

<div dir="rtl">

1. כתבו פונקציה בשם `dice_stats()` שמטילה קובייה 30 פעמים ומדפיסה: כמה פעמים יצא 6, את הסכום ואת הממוצע.
2. כתבו פונקציה בשם `guess_game()`: מספר סודי בין 1 ל-20. שואלים עד שמנחשים נכון, עם `Too low` או `Too high`, ובסוף מדפיסים כמה ניסיונות היו.

</div>

## 3. נקודת ביקורת ב׳ (על דף, בלי להריץ)

```python
count = 0
total = 0
for number in range(1, 6):
    total = total + number
    if number % 2 == 1:
        count = count + 1
print(count, total)
```

<div dir="rtl">

1. מה יודפס?
2. אילו ערכים יכולה להחזיר `random.randint(3, 7)`? ומה לגבי `random.randrange(3, 7)`?
3. שאלה ממבחן מפמ"ר: המטרה של כל קטע קוד היא לקלוט 10 ציונים ולמנות כמה מהם גבוהים מ-55 וקטנים מ-80. עבור 76 84 80 57 77 90 68 74 100 55 צריך להדפיס 5. האם כל קטע מבצע את הנדרש? אם לא, איך מתקנים?
4. למה מקסימום מתחיל בערך הראשון ולא ב-0?

</div>

```python
# קטע א
count = 0
for item in range(10):
    grade = int(input("Grade: "))
    if grade > 55 and grade < 80:
        count = count + 1
print(count)
```

```python
# קטע ג
count = 0
index = 0
while index < 10:
    grade = int(input("Grade: "))
    if grade > 55 and grade < 80:
        count = count + 1
print(count)
```

## 4. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U7_M3_Random_<Name>.py`

## בונוס: למה אין You win?

פתחו את `Random_Starter.py`. לפעמים מודפס `Roll: 6` ובכל זאת אין `You win`. למה?

---

**בדיקת יציאה:**

<div dir="rtl">

1. האם הגבול העליון נכלל ב-`randint`?
2. איזו תבנית סופרת כמה פעמים יצא 6?
3. למה הפלט של סימולציה משתנה בין הרצות?

</div>
