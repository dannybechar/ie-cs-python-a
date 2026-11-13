# מצגת elif (Unit 9.4 — elif presentation)

Source: Materials/9.4 מצגת elif/מצגת elif.pptx
Method: vision transcription

Note: all slides are NotebookLM-style images; no text in slide XML or notes (notes empty). 17 slides; slide 17 is blank (no content).

### Slide 1
Small header: "שם השיעור: תנאים מרובים בפייתון."
Title: "החיים הם לא רק 'כן' או 'לא'"
Subtitle: "הרחבת ארגז הכלים של המתכנת עם `elif`"
Image (right): a game menu with a cartoon character and four buttons: Attack, Defend, Use Potion, Flee. Caption: "מודל `elif`: אפשרויות מרובות לטיפול במצבים שונים."
Image (left): a road fork with two direction signposts (arrows left and right).

### Slide 2
Title: "העולם של if ו-else"
Subtitle: "איפה היינו עד עכשיו? (חזרה מהירה)"
Text: "עד היום, הקוד שלנו ידע לקבל החלטות של 'שחור או לבן':"
Two boxes (table-like):
| אם התנאי מתקיים (True) | אחרת (else) |
|---|---|
| ← בצע פעולה א' | ← בצע פעולה ב' |

Diagram: a decision diamond "יורד גשם?" with "כן" (green) leading to an umbrella in rain and "לא" (red) leading to a sun.
Bottom text: "אבל מה קורה כשיש לנו **יותר משתי אפשרויות**? 🤔"

### Slide 3
Title: "מה ללבוש כשיש יותר משתי אפשרויות?"
Text: "נניח שאנחנו רוצים לכתוב תוכנה שממליצה מה ללבוש לפי הטמפרטורה:"
- קר מאוד (מתחת ל-10 מעלות) -> מעיל.
- נעים (בין 10 ל-25 מעלות) -> קפוצ'ון.
- חם (מעל 25 מעלות) -> חולצה קצרה.

Image: a boy at an open wardrobe with a question mark, and a thermometer labelled >25°, 10-25°, <10°.
Code window (messy nested if/else; comments in the image are "# accent_blue" etc., rendering artifacts; the first comment line reads "# This code is intentionally messy to look at"):
```python
if temperature < 25:
    if temperature < 10:
        print("מעיל")
    else:
        print("קפוצ'ון")
else:
    print("חולצה קצרה")
```
Red handwritten note: "אפשרי, אבל מסורבל וקשה וקשה לקריאה!"

### Slide 4
Title: "הפתרון: הכירו את הכלי החדש `elif` (קיצור של Else If)"
Text: "**המהות:** `elif` מאפשר לנו לשאול שאלה נוספת *רק אם* התשובה לשאלה הקודמת הייתה 'לא'. זהו 'הגשר' בין ה-`if` הראשון ל-`else` האחרון. אפשר להשתמש בכמה `elif` שרוצים!"
Diagram: a staircase of three steps: "if" -> arrow "האם קר? (לא)" -> "elif" -> arrow "האם נעים? (לא)" -> "else" with text "אז בטח חם."

### Slide 5
Title: "התחביר: איך בונים שרשרת תנאים?"
Code window:
```python
grade = 85

if grade >= 90:
    print("מצוין!")
elif grade >= 80:
    print("טוב מאוד!")
elif grade >= 70:
    print("טוב")
else:
    print("צריך להשתפר")
```
Callouts: arrow at the first `if grade >= 90:` line: "נקודתיים בסוף כל תנאי"; bracket on the body lines: "הזחה (Indentation) אחידה".
Bottom text: "**דגש חשוב:** ההזחה (Indentation) חייבת להיות אחידה, והנקודתיים (:) בסוף כל שורת תנאי."

### Slide 6
Title: "הדוגמה הקלאסית: צבע הסוללה"
Subtitle: "תרחיש מחיי היומיום 1"
Text: "איך הטלפון הנייד שלנו יודע באיזה צבע להציג את אייקון הסוללה? התשובה היא שרשרת של בדיקות, בדיוק כמו if-elif-else."
Three cards (battery icons):
- 90% battery (green card):
```python
if battery > 20:
    color = "white"
```
- 15% battery (yellow card):
```python
elif battery > 10:
    color = "yellow"
```
- 5% battery (red card):
```python
else:
    color = "red"
```
Question box (light bulb): "שאלה לכיתה: אם הסוללה שלי 75%, האם המחשב יבדוק גם את תנאי ה-elif?"

### Slide 7
Same three battery cards and question box as slide 6 (cropped), plus answer box:
"התשובה היא **לא**! אם הסוללה היא 75%, הקוד יזהה שהתנאי הראשון נכון, יבצע את הפקודה שלו, וידלג על כל שאר ה-'elif' וה-'else'."

### Slide 8
Title: "חוק הזהב: הראשון שצודק, מנצח!"
Text: "שרשרת `if-elif-else` עוצרת ברגע שהיא מוצאת את התנאי הראשון שהוא True. כל שאר הבדיקות בשרשרת לא יתבצעו כלל."
Image: a race track with three lanes labelled if, elif, else; the "if" runner crosses the finish line first; a red stop sign "עצור" stands in front of the elif and else runners.

### Slide 9
Title: "שתי אסטרטגיות, שתי משימות שונות"
Text: "מתי משתמשים בשרשרת `elif`, ומתי ברצף של `if`-ים נפרדים?"
Image: road fork. Left winding road sign: "רק תשובה אחת אפשרית (if-elif-else)". Right multi-lane highway sign: "מספר תשובות אפשריות (`if, if, if...`)".

### Slide 10
Title: "אסטרטגיה 1: שרשרת 'או-או' (הזוכה לוקח הכל)"
Text:
**מתי משתמשים?** כשרק מצב **אחד** יכול להיות נכון בו-זמנית. ברגע שהמחשב מוצא תנאי `True` אחד, הוא מדלג על כל השאר.

**דוגמאות:**
- ציון במבחן (אי אפשר לקבל גם 'טוב' וגם 'מצוין').
- מצב דמות במשחק (חיה / פצועה / מתה).
- ימות השבוע.

**יתרון:** יעיל ומהיר.
Image: a podium with a trophy (places 1, 2, 3).

### Slide 11
Title: "אסטרטגיה 2: רשימת 'גם-וגם' (בדיקה של **הכל**)"
Text: "**מתי משתמשים?** כשאנחנו רוצים לבדוק מספר תנאים, וייתכן שיותר מאחד מהם יהיה נכון. כל `if` נבדק בנפרד, ללא קשר לאחרים."
"**דוגמה מרכזית:**"
```python
if wants_olives:
    add_olives()
if wants_mushrooms:
    add_mushrooms()
if wants_extra_cheese:
    add_extra_cheese()
```
Text: "כאן אני יכול לרצות גם זיתים וגם פטריות! אם הייתי משתמש ב-`elif`, הייתי מקבל רק תוספת אחת."
Image: a tablet showing a pizza toppings form "בחר תוספות:" with checkboxes: זיתים (checked), פטריות (checked), גבינה נוספת (checked), בצל (unchecked).

### Slide 12
Title: "ראש בראש: שרשרת בלעדית מול רשימה מצטברת"
Left panel "כל אחד ייבדק":
```python
if wants_olives:
    add_olives()
if wants_mushrooms:
    add_mushrooms()
```
Caption: "מתאים למצבים של 'גם-וגם'. בודק כל אפשרות בנפרד."
Right panel "רק אחד יתבצע":
```python
if grade >= 90:
    print("מצוין!")
elif grade >= 80:
    print("טוב מאוד!")
```
Caption: "מתאים למצבים של 'או-או'. עוצר אחרי התשובה הנכונה הראשונה."
Center: a balance scale (three separate ifs on the left pan; if/elif/else stack on the right pan).

### Slide 13
Title: "מבחן למתקדמים: חשיבות הסדר בשרשרת `elif`"
Text: "**תרחיש:** קביעת דרגה (Rank) במשחק לפי נקודות ניסיון (XP)."
```python
if xp > 1000:
    print("אגדה")
elif xp > 500:
    print("מאסטר")
elif xp > 100:
    print("פרו")
else:
    print("מתחיל")
```
Right image: a downward blue arrow with rank badges from top to bottom: אגדה (diamond), מאסטר (gold), פרו (silver), מתחיל (bronze).
"**שאלה לדיון:** למה חייבים לבדוק מהתנאי הגבוה (הכי קשה להשגה) לנמוך? מה היה קורה אם היינו הופכים את הסדר?"
(Slide also contains a tiny blank cream image, a decoration with no content.)

### Slide 14
Title: "מלכודת נפוצה: מה קורה אם הסדר הפוך?"
Code in a red-bordered warning box (comment: "# קוד שגוי!"):
```python
# קוד שגוי!
xp = 1200
if xp > 100:
    print("פרו")
elif xp > 500:
    print("מאסטר")
elif xp > 1000:
    print("אגדה")
```
Arrow from the `print("פרו")` line to a yellow callout: "הבדיקה תעצור כאן!"
Right text: "**הסבר הבעיה:** שחקן עם 1200 נקודות יקבל את דרגת ה-**'פרו'** במקום 'אגדה'. למה? כי התנאי הראשון (`xp > 100`) הוא True, והשרשרת נעצרת מיד."

### Slide 15
Title: "ארגז הכלים שלכם: סיכום וטיפים"
Heading: "רשימת צ'ק-ליסט (איך ניגשים לפתור תרגיל?)"
- ✅ האם יש יותר מ-2 אפשרויות? -> שקלו להשתמש ב-elif.
- ✅ האם האפשרויות סותרות זו את זו (רק אחת יכולה להיות נכונה)? -> השתמשו בשרשרת if-elif-else.
- ✅ האם ניתן לבחור כמה דברים ביחד? -> השתמשו ברצף של if-ים נפרדים.
- ✅ **בשרשרת `elif`, זכרו:** הסדר קובע! התחילו מהתנאי הכי ספציפי או 'קיצוני'.
- ✅ **אל תשכחו את `else`:** זו רשת הביטחון שלכם למקרה שאף תנאי לא התקיים.
Image: an open toolbox with if / elif / else buttons, a ladder, a fork arrow, a podium, and a checklist.

### Slide 16
Title: "עכשיו תורכם לבנות!"
Text: "יש לכם עכשיו את הכלים להתמודד עם קבלת החלטות מורכבות בקוד שלכם. אתם יכולים ליצור לוגיקה חכמה ומדויקת יותר במשחקים, באפליקציות ובכל פרויקט שתדמיינו."
Bold question: "מה הדבר המורכב הבא שתלמדו את המחשב שלכם להחליט?"
Image: hands on a laptop keyboard with faint app wireframes in the background.

### Slide 17
Blank slide (no image, no text, cream background).
