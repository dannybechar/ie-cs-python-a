# תרגיל מודרך — לולאות שקולות (Unit 13.3, guided practice: equivalent loops)

Source: Materials/13.3 סרטון תרגול מודרך _ לולאות שקולות___/13.3 תרגול מודרך _ לולאות שקולות.pptx
Method: vision transcription

Note: 4 slides, all pictures; no text in slide XML or notes.

### Slide 1
Title slide. Ministry logos. Text: "תרגיל מודרך" / "לולאות שקולות" / "מעקב אחר לולאות for ו- while".

### Slide 2
Title: "לולאות שקולות"
Text: "לולאות שקולות הן לולאות שמדפיסות את אותו הפלט בדיוק אך נכתבות באופן שונה.

בשקופית הבאה מופיעים שני טורים עם לולאות, עליכם להתאים לכל לולאה מטור א את הלולאה השקולה מטור ב"

### Slide 3
Table: columns "טור א" (numbered rows 1-4 on the far side) and "טור ב" (lettered rows A-D). The image appears cut off after row 4/D (nothing further is visible).

| # | טור א | אות | טור ב |
|---|---|---|---|
| 1 | see code below | A | see code below |
| 2 | | B | |
| 3 | | C | |
| 4 | | D | |

Row 1, טור א:
```python
i = 1
while i <= 10:
    if i % 3 == 0:
        print(i)
    i = i + 1
```
Row A, טור ב:
```python
for i in range(-4, 5, 2):
    print(i + 5)
```
Row 2, טור א:
```python
for i in range(16, 3, -4):
    print(i)
```
Row B, טור ב:
```python
i = 1
while i <= 3:
    print(i * 3)
    i = i + 1
```
Row 3, טור א:
```python
i = 1
while i < 10:
    print(i)
    i = i + 2
```
Row C, טור ב:
```python
i = 8
while i > 0:
    print(i * 2)
    i = i - 2
```
Row 4, טור א:
```python
for i in range(-5, 6):
    print(i + 6)
```
Row D, טור ב:
```python
for i in range(1, 12):
    print(i)
```

### Slide 4
Title: "צפו בסרטון הדרכה המדגים מעקב אחר לולאות"
Image: video thumbnail (play button) of the title slide "תרגיל מודרך לולאות שקולות / מעקב אחר לולאות for ו-while".
