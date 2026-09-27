# יחידה 6.3 – מחרוזות

כיתה ז׳ · Python A · **חותכים את ההודעה: חיתוך מחרוזות**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> חיתוך לוקח את התווים מ-start ועד end — בלי end — בקפיצות של step.

## דף עזר

```python
word = "computer"
print(word[0:3])
print(word[:3])
print(word[3:])
print(word[::-1])
```

```text
com
com
puter
retupmoc
```

<div dir="rtl">

- המבנה: `text[start:end:step]`, בדיוק כמו `range(start, stop, step)`.
- בלי start מתחילים מההתחלה. בלי end ממשיכים עד הסוף.
- הצעד 2 לוקח כל תו שני. הצעד `-1` קורא מהסוף להתחלה.
- חיתוך יוצר מחרוזת חדשה, והמקור לא משתנה.

</div>

## 1. משימה 1: מתקנים את החיתוך

פתחו את `Slicing_Starter.py`:

```python
# Task 1: this should print the letters at indexes 1 to 4 (bcde). Fix the slice.
word = "abcdefgh"
print(word[1:4])
```

## 2. משימה 2: קצוות המילה

כתבו פונקציה בשם `ends()` שקולטת מילה ומדפיסה את שלושת התווים הראשונים ואת שלושת האחרונים.

בדקו עם `planet`: `pla` ואחר כך `net`.

## 3. משימה 3: ההודעה הסודית

כתבו פונקציה בשם `decode()`. ההודעה מסתתרת בכל תו שני, החל מאינדקס 1:

```python
secret = "xPxyxtxhxoxn"
```

## 4. משימה 4: פלינדרום

כתבו פונקציה בשם `palindrome()` שקולטת מילה ובודקת אם היא נקראת אותו דבר משני הכיוונים. היא מדפיסה `Palindrome` או `Not palindrome`.

בדקו עם `level` ועם `rover`.

## 5. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G7_U6_M3_Slicing_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. האם end נכלל בחיתוך?
2. מה לוקח `word[:3]`?
3. איך הופכים מחרוזת?

</div>
