# 14.1_ פייתון א _ צב גרפי חלק ב'.pptx

Source: `Materials/14.1 _ למידה תכל'ס - הצב הגרפי חלק ב/14.1_ פייתון א _ צב גרפי חלק ב'.pptx`

### Slide 1

- הצב הגרפי
- חלק ב'

**Notes:**

- השיעור הנוכחי מתמקד בנושא הצב הגרפי.
- נתחיל את השיעור בהסבר רעיוני להבנה בסיסית, ולאחר מכן הקניה - עד 10 דקות, כולל דוגמאות ושיח.
- לאחר מכן, תרגול. התרגול יתמקד בהכרת מבנה הצב, הפעלת פקודות בסיסיות וציור בסיסי. התרגול ישלב את כל החומר הנלמד עד לנקודת זמן הנוכחית. 
- הקצו לתלמידים את הזמן הנדרש לפתרון.
- לכל תרגיל יש שקף הצעה לפתרון + קוד. 
- המלצה חמה: להציג תחילה את פתרונות התלמידים, ולאחר מכן להציג כסיכום את ההצעה לפתרון.
- משך זמן יחידה זו: 180  דקות, כולל זמן התרגול.
- בהצלחה!

### Slide 2

- רכיבי השיעור - Classroom
- 14.1 | למידה תכלס (מצגת השיעור)
- 14.2 | הגשת משימות (להגשה)
- 14.3 | תרגול לפיצוח | מחנה קיץ
- 14.4 | מאסטר פייתון
- 14.5 | סיכום בקטנה

### Slide 3

- מה נלמד בשיעור?
- מהי מערכת צירים?
-  	נכיר את ראשית הצירים.
- נלמד ונכיר פעולות ופקודות מיקום.
- נתרגל ונצייר באמצעות הצב הגרפי.

**Notes:**

- פתיח: שקף הצגת הנושאים הנלמדים ביחידה.
-  בפתיחת השיעור, מומלץ לסקור בקצרה את הנושאים שנלמד.

### Slide 4

- כל תוכנית צב גרפי תיפתח ברצף שורות קוד של המבנה הבסיסי: 
- הצב הגרפי - תזכורת

**Notes:**

- מבנה תבניתי בסיסי של תוכניות הצב הגרפי.
- שורת קוד מספר 11 אינה הכרחית בהצגה גרפית בפייתון ווב, אולם פעולה זו מופיעה בתוכנית הלימודים ובבחינות המפמ"ר, לכן יש להציגה ולהסביר את משמעותה. כדאי מאוד להריץ הדגמה של מבנה הקוד, ללא השורה ועם השורה, בתוכנה לא-וובית.
- # ייבוא ספריית הצב הגרפי
- import turtle
- # הגדרת חלונית ציור
- wn = turtle.Screen()
- # הגדרת צב גרפי
- pen = turtle.Turtle()
- # רצף שורות קוד
- # השארת מופע חלונית הציור על המסך
- wn.mainloop()

### Slide 5

- הצב הגרפי - תזכורת
- הגדרת ברירת המחדל של הצב הגרפי:
- צורת הצב הגרפי: classic.
- צבע הצב הגרפי: שחור.
- מיקום הצב הגרפי: מרכז חלונית הציור - בנקודה (0,0).
- כיוון הצב: הצב פונה לצד ימין.

### Slide 6

- הצב הגרפי - מערכת הצירים
- מיקום הצב הגרפי בחלונית הציור:
- המסך שלנו מבוסס על מערכת הצירים, כאשר ראשית הצירים היא הנקודה (0,0) - שהיא גם מרכז חלונית הציור.
- המסך מחולק ל-4 חלקים בשם רביע
- 2
- 1
- 3
- 4

**Notes:**

- למורה: יש להדגים פקודות תנועה, ולבדוק את מיקום הצב באמצעות הפקודה position, המופיעה בשקף הבא. 

### Slide 7

- שם משתנה
- .
- שם הפעולה
- pen
- .
- position(  )
- pen
- .
- pos(  )
- הצב הגרפי - פעולות מיקום
- בדיקת מיקום הצב הגרפי:

**Notes:**

- למורה: יש להדגים במסך הקוד תזוזה על המסך והדפסת מיקום הנקודות השונות. שתי הפקודות מבצעות את אותה פעולה. אפשר לקיים דיון על קיצור שמות הפעולות בגרסאות השונות של פייתון.
- print(pen.position())

### Slide 8

- הצב הגרפי - פעולות מיקום
- שם משתנה
- .
- שם הפעולה
- pen
- .
- setposition(x, y )
- pen
- .
- setpos( x, y )
- שינוי מיקום סמן הצב הגרפי: 
- דוגמה:
- מיקמנו את הצב הגרפי בנקודה (10,20):
- x = 10, y = 20
- pen.setposition(10, 20)

**Notes:**

- למורה: יש להדגים במסך הקוד תזוזה על המסך והדפסת מיקום הנקודות השונות. שתי הפקודות מבצעות את אותה פעולה. אפשר לקיים דיון על קיצור שמות הפעולות בגרסאות השונות של פייתון. 
- pen.setposition(10, 20)

### Slide 9

- הצב הגרפי - פעולות מיקום
- שם משתנה
- .
- שם הפעולה
- pen
- .
- setx( x )
- pen
- .
- sety( y )
- הגדרת מיקום נקודות x ו-y של סמן הצב הגרפי:
- דוגמה:

**Notes:**

- למורה: יש להדגים במסך הקוד תזוזה על המסך והדפסת מיקום הנקודות השונות.
- pen.setx(7)
- pen.sety(100)

### Slide 10

- מיקמנו נקודות x ו-y, וראינו שהצב צייר על המסך בלי שסימנו לו לצייר - 
- באמצעות פקודות forward / backward. 
- מה הסיבה, לדעתכם?

**Notes:**

- למורה: יש לעודד שיח ודיון ולהדגים במסך הקוד. מוטיבציה להרמה והורדת עט.

### Slide 11

- הצב הגרפי - פעולות עט
- שם משתנה
- .
- שם הפעולה
- pen
- .
- penup(x, y)
- pen
- .
- up(x, y)
- הרמת עט
- כשהעט מורם - לא מציירים קו בתנועה. 
- שם משתנה
- .
- שם הפעולה
- pen
- .
- pendown(x, y)
- pen
- .
- down(x, y)
- הורדת עט
- במצב זה מציירים קו בתנועה. 

**Notes:**

- למורה: יש להדגים במסך הקוד תזוזה על המסך והדפסת מיקום הנקודות השונות.

### Slide 12

- הצב הגרפי - פעולות מיקום
- שם משתנה
- .
- שם הפעולה
- pen
- .
- goto(x , y)
- הגדרת מיקום הצב הגרפי בפקודה נוספת:
- בעזרת פקודה זו ניתן להזיז את הצב הגרפי ממיקומו הנוכחי לנקודה מסויימת במערכת הצירים.
- דוגמה:

**Notes:**

- למורה: יש להדגים במסך הקוד תזוזה על המסך והדפסת מיקום הנקודות השונות.
- pen.goto(20, 40)

### Slide 13

- בואו נתרגל #1
- משימה: ריבוע ברביע 1 
- כתבו פעולה המציירת ריבוע בעל צלעות בצבע ירוק, ברביע הראשון של המסך.
- היכנסו לרכיב 14.2 | הגשת משימות והגישו את הפתרון במקום המיועד. 
- משך המשימה: 10 דקות

**Notes:**

- למורה: ממליצה להציג פתרונות של התלמידים. כדאי להציג פתרונות שונים.
- הצעה לפתרון בשקף הבא.

### Slide 14

- הצעה לפתרון #1

**Notes:**

- למורה: המלצה חמה להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם. אפשר לדון בחזרתיות של הפעולות שנכתבו בקוד ,ולציין שנמצא לכך פתרון יעיל יותר בקוד בהמשך (לולאה).
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—----------------------#
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- pen.penup()
- pen.goto(100, 100)
- pen.pendown()
- pen.pencolor("green")
- def square():
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
- square()
- wn.mainloop()

### Slide 15

- הצב הגרפי - פעולות עיצוב
- שם משתנה
- .
- שם הפעולה
- תיאור הפעולה
- pen
- .
- fillcolor( “שם הצבע” )
- הגדרת צבע המילוי
- pen
- .
- begin_fill( )
- תחילת צביעה
- pen
- .
- end_fill( )
- סיום צביעה
- צביעת שטח צורה בצבע:
- על מנת לצבוע שטח צורה סגורה בצבע, נכתוב את שורות הקוד הבאות:
- בין פעולת תחילת הצביעה לפעולת סיום הצביעה, נכתוב את קוד ציור הצורה.
- דוגמה בשקף הבא

**Notes:**

- למורה: יש להדגים את הפקודות במסך הקוד. התרגילים הבאים ישלבו בהדרגה את כל הפקודות הנלמדות.

### Slide 16

- הצב הגרפי - פעולות עיצוב
- צביעת שטח צורה סגורה בצבע - דוגמה:
- קוד ציור הצורה נכתב בין פעולת תחילת הצביעה לפעולת סיום הצביעה. 

**Notes:**

- למורה: יש להדגים את הפקודות במסך הקוד. התרגילים הבאים ישלבו בהדרגה את כל הפקודות הנלמדות.
- pen.filling("green")
- pen.begin_fill()
- square()  # ציור צורה
- pen.end_fill()

### Slide 17

- מה לדעתכם יקרה אם ננסה לצבוע קו 
- (או כל צורה פתוחה אחרת)?

**Notes:**

- למורה: יש לעודד שיח ודיון ולהדגים במסך הקוד. מוטיבציה להרמה והורדת עט.

### Slide 18

- בואו נתרגל #2
- משימה: ריבוע ברביע 2 
- כתבו תוכנית המציירת ריבוע צהוב, בעל צלעות בצבע ירוק, ברביע השני של המסך.
- היכנסו לרכיב 14.2 | הגשת משימות והגישו את הפתרון במקום המיועד. 
- משך המשימה: 20 דקות

**Notes:**

- למורה: ממליצה להציג פתרונות של התלמידים. כדאי להציג פתרונות שונים.
- הצעה לפתרון בשקף הבא.

### Slide 19

- הצעה לפתרון #2

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם. אפשר לדון בחזרתיות של הפעולות שנכתבו בקוד, ולציין שנמצא לכך פתרון יעיל יותר בקוד בהמשך (לולאה).מצ"ב הצעה לפתרון הקוד:
- #-------------------------code—-----------------------#
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- pen.penup()
- pen.goto(-200, 100)
- pen.pendown()
- pen.pencolor("green")
- def square():
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
- pen.fillcolor("yellow")
- pen.begin_fill()
- square()  # ציור צורה
- pen.end_fill()
- wn.mainloop()

### Slide 20

- הצעה לפתרון #2
- שימו לב, ניתן לכתוב את הפעולה לציור ריבוע בעזרת לולאה.
- ציור ריבוע: מציירים קו ומסתובבים 90.
- מבצעים את הקוד 4 פעמים.

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם. אפשר לדון בחזרתיות של הפעולות שנכתבו בקוד, ולציין שנמצא לכך פתרון יעיל יותר בקוד בהמשך (לולאה).מצ"ב הצעה לפתרון הקוד:
- #-------------------------code—-----------------------#
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- pen.penup()
- pen.goto(-200, 100)
- pen.pendown()
- pen.pencolor("green")
- def square():
-   for i in range(4):
-      pen.forward(100)
-      pen.left(90)
- pen.fillcolor("yellow")
- pen.begin_fill()
- square()  # ציור צורה
- pen.end_fill()
- wn.mainloop()

### Slide 21

- בואו נתרגל #3
- משימה: ריבועים ברביעים
- כתבו תוכנית המציירת ארבעה ריבועים בצבעים שונים בארבעת הרביעים.
- היכנסו לרכיב 14.2 | הגשת משימות והגישו את הפתרון במקום המיועד. 
- משך המשימה: 20 דקות

**Notes:**

- למורה: ממליצה להציג פתרונות של התלמידים.
- יש להקצות זמן לכתיבת התוכנית.
- הצעה לפתרון בשקף הבא.

### Slide 22

- הצעה לפתרון #3

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם. בשקף זה יש לציין את פעולת ציור ריבוע, שתזומן בהמשך התוכנית. המשך הקוד בשקף הבא.
- מצ"ב הצעה לפתרון הקוד:
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- def square():
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
- pen.penup()
- pen.goto(100, 100)
- pen.pendown()
- pen.fillcolor("purple")
- pen.begin_fill()
- square()
- pen.end_fill()
- #
- pen.penup()
- pen.goto(-200, 100)
- pen.pendown()
- pen.ht()
- pen.fillcolor("yellow")
- pen.begin_fill()
- square()
- pen.end_fill()
- #
- pen.penup()
- pen.goto(-200, -100)
- pen.pendown()
- pen.fillcolor("blue")
- pen.begin_fill()
- square()
- pen.end_fill()
- #
- pen.penup()
- pen.goto(100, -100)
- pen.pendown()
- pen.fillcolor("green")
- pen.begin_fill()
- square()
- pen.end_fill()
- wn.mainloop()

### Slide 23

- מדוע מרימים את הצב כשזזים לרביע אחר? 
- מה הופיע על המסך כשלא עשיתם זאת?

**Notes:**

- למורה: יש לנהל שיח ודיון ולהדגים במסך הקוד. מוטיבציה להרמה והורדת עט.

### Slide 24

- בואו נתרגל #3
- משימה: מחולל מצולעים צבעוניים
- כתבו תוכנית המקבלת כקלט שם של מצולע מבין המצולעים הבאים: משולש, ריבוע, מחומש.
- יש להשתמש בכתיבת פעולה בהתאם לקלט כל צורה, ובקריאה לפעולות בעזרת שימוש בתנאי מתגלגל.
- היכנסו לרכיב 14.2 | הגשת משימות והגישו את הפתרון במקום המיועד. 
- משך המשימה: 10 דקות

**Notes:**

- למורה: ממליצה להציג פתרונות של התלמידים.
- יש להקצות זמן לכתיבת התוכנית.
- הצעה לפתרון בשקף הבא.

### Slide 25

- הצעה לפתרון #3
- המשך בשקף הבא
- ריבוע
- מלבן
- משולש

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם.
- מצ"ב הצעה לפתרון הקוד:
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- pen.penup()
- pen.goto(-200, 100)
- pen.pendown()
- #pen.pencolor("green")
- pen.ht()
- def square():
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
- def draw_rectangle():
-    height = 5
-    width = 2
-    pen.forward(width * 30)
-    pen.right(90)
-    pen.forward(height * 30)
-    pen.right(90)
-    pen.forward(width * 30)
-    pen.right(90)
-    pen.forward(height * 30)
- def triangle():
-    pen.forward(120)
-    pen.left(120)
-    pen.forward(120)
-    pen.left(120)
-    pen.forward(120)
- def main():
-    shape = input("בחר צורה מבין הצורות: משולש / ריבוע / מלבן:")
-    if shape == "ריבוע":
-        square()
-    elif shape == "מלבן" :
-        draw_rectangle()
-    elif shape == "משולש":
-        triangle()
-    else:
-        print("באפשרותינו לצייר משולש/ריבוע/מלבן בלבד .")
- main()
- wn.mainloop()

### Slide 26

- הצעה לפתרון #3 - המשך

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם.
- מצ"ב הצעה לפתרון הקוד:
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- pen.penup()
- pen.goto(-200, 100)
- pen.pendown()
- #pen.pencolor("green")
- pen.ht()
- def square():
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
-    pen.forward(100)
-    pen.left(90)
- def draw_rectangle():
-    height = 5
-    width = 2
-    pen.forward(width * 30)
-    pen.right(90)
-    pen.forward(height * 30)
-    pen.right(90)
-    pen.forward(width * 30)
-    pen.right(90)
-    pen.forward(height * 30)
- def triangle():
-    pen.forward(120)
-    pen.left(120)
-    pen.forward(120)
-    pen.left(120)
-    pen.forward(120)
- def main():
-    shape = input("בחר צורה מבין הצורות: משולש / ריבוע / מלבן:")
-    if shape == "ריבוע":
-        square()
-    elif shape == "מלבן" :
-        draw_rectangle()
-    elif shape == "משולש":
-        triangle()
-    else:
-        print("באפשרותינו לצייר משולש/ריבוע/מלבן בלבד .")
- main()
- wn.mainloop()

### Slide 27

- הצעה לפתרון #3
- ריבוע
- מלבן
- משולש
- שימו לב, ניתן לכתוב את הפעולות של הצורות בעזרת לולאה.

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם.
- מצ"ב הצעה לפתרון הקוד:
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- pen.penup()
- pen.goto(-200, 100)
- pen.pendown()
- #pen.pencolor("green")
- pen.ht()
- def square():
-   for i in range(4):
-      pen.forward(100)
-      pen.left(90)
- def draw_rectangle():
-   height = 5
-   width = 2
-   for i in range (2):
-      pen.forward(width * 30)
-      pen.right(90)
-      pen.forward(height * 30)
-      pen.right(90)
- def triangle():
-   for i in range (3):
-      pen.forward(120)
-      pen.left(120)
- def main():
-    shape = input("בחר צורה מבין הצורות: משולש / ריבוע / מלבן:")
-    if shape == "ריבוע":
-        square()
-    elif shape == "מלבן" :
-        draw_rectangle()
-    elif shape == "משולש":
-        triangle()
-    else:
-        print("באפשרותינו לצייר משולש/ריבוע/מלבן בלבד .")
- main()
- wn.mainloop()

### Slide 28

- בואו נתרגל #4
- משימה: ציור בית
- כתבו תוכנית המציירת בית בעל גג משולש אדום, שמבנהו ריבוע בצבע אחר לבחירתכם.
- אתגר: הוסיפו חלונות ודלת.
- היכנסו לרכיב 14.2 | הגשת משימות והגישו את הפתרון במקום המיועד. 
- משך המשימה: 20 דקות

**Notes:**

- למורה: ממליצה להציג פתרונות של התלמידים. תרגיל המיישם פעולות ושימוש בצב גרפי. כדאי לאפשר לתלמידים להביע יצירתיות חופשית, בלי להציג להם דוגמה מקדימה, אלא אם כן התלמידים מבקשים זאת.
- יש להקצות זמן לכתיבת התוכנית.
- הצעה לפתרון בשקף הבא.

### Slide 29

- הצעה לפתרון #4
- המשך בשקף הבא

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם.
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—--------------------------#
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- def house():
-    pen.pencolor("light gray")
-    pen.fillcolor("light gray")
-    pen.begin_fill()
-    pen.forward(150)
-    pen.rt(90)
-    pen.forward(150)
-    pen.rt(90)
-    pen.forward(150)
-    pen.rt(90)
-    pen.forward(150)
-    pen.rt(90)
-    pen.end_fill()
- def window():
-    pen.pencolor("black")
-    pen.fillcolor("blue")
-    pen.begin_fill()
-    pen.penup()
-    pen.forward(40)
-    pen.rt(90)
-    pen.forward(40)
-    pen.rt(90)
-    pen.forward(40)
-    pen.rt(90)
-    pen.forward(40)
-    pen.rt(90)
-    pen.end_fill()
- def door():
-    pen.pencolor("brown")
-    pen.fillcolor("brown")
-    pen.begin_fill()
-    pen.forward(50)
-    pen.rt(90)
-    pen.forward(70)
-    pen.rt(90)
-    pen.forward(50)
-    pen.rt(90)
-    pen.forward(70)
-    pen.end_fill()
- def roof():
-    pen.pendown()
-    pen.pencolor("red")
-    pen.fillcolor("red")
-    pen.begin_fill()
-    pen.goto(75, 40)
-    pen.goto(150, 0)
-    pen.goto(0, 0)
-    pen.end_fill()
- house()
- pen.goto(20, -20)
- window()
- pen.goto(90, -20)
- window()
- pen.goto(50, -80)
- door()
- pen.penup()
- pen.goto(0, 0)
- roof()
- wn.mainloop()

### Slide 30

- הצעה לפתרון #4 - המשך

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם.
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—--------------------------#
- import turtle
- wn = turtle.Screen()
- pen = turtle.Turtle()
- def house():
-    pen.pencolor("light gray")
-    pen.fillcolor("light gray")
-    pen.begin_fill()
-    pen.forward(150)
-    pen.rt(90)
-    pen.forward(150)
-    pen.rt(90)
-    pen.forward(150)
-    pen.rt(90)
-    pen.forward(150)
-    pen.rt(90)
-    pen.end_fill()
- def window():
-    pen.pencolor("black")
-    pen.fillcolor("blue")
-    pen.begin_fill()
-    pen.penup()
-    pen.forward(40)
-    pen.rt(90)
-    pen.forward(40)
-    pen.rt(90)
-    pen.forward(40)
-    pen.rt(90)
-    pen.forward(40)
-    pen.rt(90)
-    pen.end_fill()
- def door():
-    pen.pencolor("brown")
-    pen.fillcolor("brown")
-    pen.begin_fill()
-    pen.forward(50)
-    pen.rt(90)
-    pen.forward(70)
-    pen.rt(90)
-    pen.forward(50)
-    pen.rt(90)
-    pen.forward(70)
-    pen.end_fill()
- def roof():
-    pen.pendown()
-    pen.pencolor("red")
-    pen.fillcolor("red")
-    pen.begin_fill()
-    pen.goto(75, 40)
-    pen.goto(150, 0)
-    pen.goto(0, 0)
-    pen.end_fill()
- house()
- pen.goto(20, -20)
- window()
- pen.goto(90, -20)
- window()
- pen.goto(50, -80)
- door()
- pen.penup()
- pen.goto(0, 0)
- roof()
- wn.mainloop()

### Slide 31

- משך המשימה: 20 דקות
- היכנסו לרכיב 14.2 | הגשת משימות והגישו את הפתרון במקום המיועד. 
- בואו נתרגל #5
- משימה: יוצרים צורות עם לולאות
- ניעזר בלולאת for ליצירת ריבוע. 
- נעדכן את הנתונים בלולאה וניצור ציור מרשים.
- עדכנו נתונים שונים וראו מה קורה.
- import turtle
- pen = turtle.Turtle()
- pen.pensize(3)
- pen.color("blue")
- pen.shape("arrow")
- pen.pu()
- for i in range(4):
- 	pen.pd()
- 	pen.fd(100)
- 	pen.left(90)
- import turtle
- pen = turtle.Turtle()
- pen.pensize(3)
- pen.color("blue")
- pen.shape("arrow")
- pen.pu()
- for i in range(30):
- 	pen.pd()
- 	pen.fd(40)
- 	pen.left(100)

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם.
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—--------------------------#

### Slide 32

- בואו נתרגל #6
- משימה: ספירלות
- הפעולה draw שלפניכם מקבלת את מספר הצלעות n ומציירת על המסך איורים עם הצורה הנוצרת.
- צרו איורים משלכם, צבעו אותם בצבעים שונים והציגו בכיתה.
- הפעולה draw
- חישוב מתמטי של זווית הסיבוב
- זימון הפעולה בלולאה
- קלט מהמשתמש
- היכנסו לרכיב 14.2 | הגשת משימות והגישו את הפתרון במקום המיועד. 
- משך המשימה: 20 דקות

**Notes:**

- למורה: הציגו לתלמידים את הקוד והריצו יחד, אפשרו להם להקליד את מספר הצלעות ואת מספר סבבי הלולאה. הציגו את היצירות בכיתה. בקשו מהתלמידים לשנות צבע ליצירת גיוון ומוטיבציה להריץ את הקוד החדש.
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—--------------------------#
- import turtle
- pen = turtle.Turtle()
- pen.pensize(3)
- pen.color("blue")
- pen.shape("arrow")
- pen.pu()
- def draw(n):
-         for i in range(n):
-                 pen.pd()
-                 pen.fd(100)
-                 pen.rt(360/n)
- num = int(input("Enter number of shape sides: "))
- times = int(input("Enter number of spins: "))
- for i in range(times):
-         draw(num)
-         pen.left(50)

### Slide 33

- בואו נתרגל #7
- משימה: הבלון המעופף
- במשימה זו ניצור צב שצורתו אליפסה ונקרא לו balloon.
- הצב ידלג באופן אקראי על המסך כ 10 פעמים.
- כדי לבצע את המשימה עלינו להכיר את הספריות הבאות:
- import turtle
- import random
- import time
- היכנסו לרכיב 14.2 | הגשת משימות והגישו את הפתרון במקום המיועד. 
- משך המשימה: 20 דקות

**Notes:**

- למורה:עקבו אחר הקוד, אנו ממליצים להריץ ולהציג את הקוד בפני התלמידים בסביבת העבודה, שלב אחר שלב. ולאחר מכן להציג את הסיכום בשקפים מהמצגת.
- עודדו את התלמידים לבחור צבעים או צורות שונות לצב.
- הקדישו זמן להצגת עבודות התלמידים. 
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—--------------------------#
- import turtle
- import random
- import time

### Slide 34

- צב ולולאות - הבלון
- import turtle
- import random
- import time
- wn = turtle.Screen() 		 #ניצור חלון
- wn.bgcolor("lightblue")	    	#רקע המסך
- wn.screensize(300,300)	#גודל המסך
- balloon = turtle.Turtle()           	#ניצור צב  
- balloon.shape("circle")            	 #צורת הצב
- balloon.turtlesize(3,2)             	#רוחב וגובה של צב
- balloon.color("red")               	#צבע של צב
- balloon.pu()                        		#עט מעלה, אל תצייר
- for i in range(10):                 		  #לולאה 
-     x = random.randint(-250,250)    	#בחר מספר אקראי בטווח
-     y = random.randint(-250,250)    	#בחר מספר אקראי בטווח
-     balloon.goto(x,y)               		 #קפוץ אל נקודות
-     time.sleep(1)                   		  #מצב שינה, מחכים שנייה
-  עדכנו את מספר הסבבים של הלולאה.
- שנו את צבע הבלון וגודלו.

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם.
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—--------------------------#
- import turtle
- import random
- import time
- wn = turtle.Screen() 		    #ניצור חלון
- wn.bgcolor("lightblue")	            #רקע המסך
- wn.screensize(300,300)	            #גודל המסך
- balloon = turtle.Turtle()           #ניצור צב  
- balloon.shape("circle")             #צורת הצב
- balloon.turtlesize(3,2)             #רוחב וגובה של צב
- balloon.color("red")                #צבע של צב
- balloon.pu()                        #עט מעלה, אל תצייר
- for i in range(10):                 #לולאה 
-     x = random.randint(-250,250)    #בחר מספר אקראי בטווח
-     y = random.randint(-250,250)    #בחר מספר אקראי בטווח
-     balloon.goto(x,y)               #קפוץ אל נקודות
-     time.sleep(1)                   #מצב שינה, מחכים שינייה

### Slide 35

- צב ולולאות - אירועי עכבר מקלדת
- בהמשך למשימת הבלון, בפייתון ניתן לבצע פעולות בלחיצת עכבר.
- לשם כך נלמד על אירוע לחיצת העכבר onClick ונוסיף את הפקודות הבאות:

**Notes:**

- למורה:בשקף זה היכרות ראשונית בלבד עם אירועי עכבר מקלדת, על המורה להדגים את הקוד ועדיין לא לאפשר לתלמידים לבצע לבד. ניתן לאפשר לתלמידים לבצע חקר, יחידה זו משמשת כמבוא ויצירת סקרנות להמשך.בהמשך יורחב הפרק והתלמידים ילמדו באופן מסודר על אירועי עכבר מקלדת.
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—--------------------------#
- import turtle
- import random
- import time
- wn = turtle.Screen() 		    #ניצור חלון
- wn.bgcolor("lightblue")	            #רקע המסך
- wn.screensize(300,300)	            #גודל המסך
- balloon = turtle.Turtle()           #ניצור צב  
- balloon.shape("circle")             #צורת הצב
- balloon.turtlesize(3,2)             #רוחב וגובה של צב
- balloon.color("red")                #צבע של צב
- balloon.pu()                        #עט מעלה, אל תצייר
- def hide(x,y):
-     balloon.ht()
-     time.sleep(1)
-     x = random.randint(-250,250)    #בחר מספר אקראי בטווח
-     y = random.randint(-250,250)    #בחר מספר אקראי בטווח
-     balloon.goto(x,y)               #קפוץ אל נקודות
-     time.sleep(1) 
-     balloon.st()
- balloon.onclick(hide)
- wn.mainloop()

### Slide 36

- צב ולולאות - אירועי עכבר מקלדת
- הפעולה hide מקבלת באופן אוטומטי את מיקום הלחיצה (x,y).
- נחביא את הבלון באמצעות ההוראה hideTurtle  או בקיצור ht.
- נחכה, ונציג את הבלון באמצעות הפעולה shoTurtle או בקיצור st.
- בלחיצה על הבלון, נזמן את הפעולה hide.
- הריצו להנאתכם!

**Notes:**

- למורה: המלצה חמה - להציג פתרונות של התלמידים לפני הצגת הפתרון המסכם.
- מצ"ב הצעה לפתרון הקוד:
- #---------------------------code—--------------------------#
- import turtle
- import random
- import time
- wn = turtle.Screen() 		    #ניצור חלון
- wn.bgcolor("lightblue")	            #רקע המסך
- wn.screensize(300,300)	            #גודל המסך
- balloon = turtle.Turtle()           #ניצור צב  
- balloon.shape("circle")             #צורת הצב
- balloon.turtlesize(3,2)             #רוחב וגובה של צב
- balloon.color("red")                #צבע של צב
- balloon.pu()                        #עט מעלה, אל תצייר
- def hide(x,y):
-     balloon.ht()
-     time.sleep(1)
-     x = random.randint(-250,250)    #בחר מספר אקראי בטווח
-     y = random.randint(-250,250)    #בחר מספר אקראי בטווח
-     balloon.goto(x,y)               #קפוץ אל נקודות
-     time.sleep(1) 
-     balloon.st()
- balloon.onclick(hide)
- wn.mainloop()

### Slide 37

- היכנסו לרכיב 14.3 | תרגול לפיצוח - מחנה קיץ וענו על השאלות. 
- 14.3 | תרגול לפיצוח - מחנה קיץ 

**Notes:**

- ‹#›

### Slide 38

- 14.4 | מאסטר פייתון
- היכנסו לרכיב 14.4 | מאסטר פייתון וענו על השאלות. 

**Notes:**

- ‹#›

### Slide 39

- למדנו מהי מערכת צירים.
- למדנו מהי נקודת ראשית הצירים.
- למדנו למקם את ערכי נקודות הצב הגרפי בחלונית הציור.
- תרגלנו וציירנו.
- בואו נסכם
