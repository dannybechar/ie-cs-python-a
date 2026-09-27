# יחידה 3.2 – משתנים, קלט/פלט וחישובים

כיתה ז׳ · Python A · **מהקלט לתוצאה: חישובים עם משתנים**

**קוראים ← חוזים ← עוקבים ← מריצים ← בודקים ← משנים ← בונים**

## דף עזר

<div dir="rtl">

| פעולה | משמעות | דוגמה |
|---|---|---|
| `+` | חיבור | `12 + 5` ← `17` |
| `-` | חיסור | `12 - 5` ← `7` |
| `*` | כפל | `12 * 5` ← `60` |
| `/` | חילוק | `12 / 5` ← `2.4` |
| `//` | כמה קבוצות שלמות | `17 // 5` ← `3` |
| `%` | שארית | `17 % 5` ← `2` |

</div>

> [!IMPORTANT]
> היום, בכל הדוגמאות של `//` ו-`%`, משתמשים במספרים שלמים חיוביים, ומחלקים במספר גדול מ-0.

## 1. פותחים וקוראים

פתחו את `Arithmetic_Starter.py`. אל תריצו עדיין!

```python
a = 12
b = 5

total = a + b
difference = a - b
product = a * b
quotient = a / b

print("Add:", total)
print("Subtract:", difference)
print("Multiply:", product)
print("Divide:", quotient)
```

התחזית שלי: `Add:` ___ · `Subtract:` ___ · `Multiply:` ___ · `Divide:` ___

## 2. מריצים ובודקים

הריצו והשוו לתחזית. איזו פעולה נתנה מספר עשרוני?

## 3. משנים רק את הקלטים

שנו רק את `a` ואת `b`, ל-20 ול-4. אל תשנו את החישובים. חזו את ארבע התוצאות, ורק אז הריצו.

`Add:` ___ · `Subtract:` ___ · `Multiply:` ___ · `Divide:` ___

## 4. תוכנית שמקבלת קלט

החליפו את שתי ההשמות הקבועות בקלט של מספרים:

```python
a = int(input("First number: "))
b = int(input("Second number: "))
```

השאירו את כל השאר בלי שינוי. הריצו פעם עם 12 ו-5, ופעם עם זוג מספרים אחר.

## 5. קבוצות שלמות ושארית

הוסיפו לתוכנית:

```python
full_groups = a // b
left_over = a % b

print("Full groups:", full_groups)
print("Left over:", left_over)
```

עבור `a = 17` ו-`b = 5`, חזו לפני ההרצה: `a // b` = ___ · `a % b` = ___

## 6. אתגר מעקב

עקבו אחרי התוכנית בלי להריץ, ומלאו את הטבלה:

```python
items = 23
per_pack = 6
full_packs = items // per_pack
left_over = items % per_pack
```

<div dir="rtl">

| אחרי השורה | `items` | `per_pack` | `full_packs` | `left_over` |
|---|---|---|---|---|
| `items = 23` | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| `per_pack = 6` | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| `full_packs = ...` | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| `left_over = ...` | &nbsp; | &nbsp; | &nbsp; | &nbsp; |

</div>

## 7. משימת ליבה: מחשבון אריזות

> [!WARNING]
> זמן מוגן. עובדים לבד.

בנו תוכנית חדשה שקולטת כמה פריטים יש (`items`) וכמה פריטים נכנסים לכל חבילה (`per_pack`), מחשבת כמה חבילות מלאות יש ומה נשאר, ומדפיסה שתי שורות ברורות.

```python
items = int(input("How many items? "))
per_pack = int(input("How many items per pack? "))

full_packs = ____________________
left_over = ____________________

print("Full packs:", full_packs)
print("Left over:", left_over)
```

לפני ההרצה הראשונה, חזו: 17 פריטים, 5 בכל חבילה ← ___ חבילות מלאות, ___ פריטים נשארו.

## 8. שומרים

שומרים: `File › Save As` ← `G7_U3_M2_Packing_<Name>.py`

---

**בדיקת יציאה:** בלי להריץ — מה יודפס?

```python
items = 17
per_pack = 5
print(items // per_pack)
print(items % per_pack)
```

<div dir="rtl">

- **A:** `3` ואז `2`
- **B:** `3.4` ואז `0`
- **C:** `2` ואז `3`

</div>

**אני יכול/ה:** לקלוט מספרים ← לחשב ← לעקוב אחרי משתנים ← להציג פלט ברור.
