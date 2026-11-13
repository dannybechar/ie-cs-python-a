# 19.1 _ פייתון א _ הכנה לבחינה המסכמת - מחרוזות והצב הגרפי.pptx

Source: `Materials/19.1 _ הכנה לבחינה המסכמת - מחרוזות והצב הגרפי/19.1 _ פייתון א _ הכנה לבחינה המסכמת - מחרוזות והצב הגרפי.pptx`

### Slide 1

- הכנה לבחינה המסכמת
- מחרוזות והצב הגרפי 

**Notes:**

- השיעור הנוכחי מתמקד בבחינות מפמ"ר.
- השיעור כולל תרגילים מבחינות. 
-  יש להקצות זמן להקניה ולהבנה בכל שלב.
- הקצו לתלמידים את הזמן הנדרש לפתרון.
- כל תרגיל כולל שקף הצעה לפתרון + קוד. 
- המלצה חמה: להציג תחילה את פתרונות התלמידים, ולאחר מכן להציג כסיכום את ההצעה לפתרון.
- משך זמן יחידה זו: שיעור (כולל זמן התרגול).
- בהצלחה!

### Slide 2

- רכיבי השיעור
- 19.1 | הכנה לבחינה (מצגת השיעור)
- 19.2 | דף נוסחאות
- 19.3 | הגשת משימות (להגשה)
- 19.4 | תרגול לפיצוח - דף עבודה (להגשה)
- 19.5 | מאסטר פייתון

**Notes:**

- ‹#›

### Slide 3

- מה נעשה בשיעור?
- נתרגל תרגילים מבחינות מפמ"ר בנושאים שלמדנו:
- מחרוזות.
- הצב הגרפי.

**Notes:**

- פתיח: שקף הצגת הנושאים הנלמדים ביחידה.
- בפתיחת השיעור, מומלץ לסקור בקצרה את הנושאים שנלמד.

### Slide 4

- מחרוזות

**Notes:**

- תרגילים מבחינות מפמ"ר בנושא מחרוזות.דגשים:
- יש להקצות מספיק זמן לפתרון התרגיל. יש לפתור את התרגיל בכתב, ללא הרצה בתוכנה. אפשרו לתלמידים להיעזר בדף העזר.
- יש להציג פתרונות של התלמידים, לעורר דיון ושיח ולהציג פתרון מלא על ידי המורה.

### Slide 5

- סיכום הפעולות שנלמדו
- הפעולה ()lower הופכת את כל האותיות במחרוזת לאותיות קטנות. ללא שינוי המחרוזת המקורית.
- text.lower()
- הפעולה len מחזירה את אורך המחרוזת.
- len(text)
- פעולה הבודקת אם המחרוזת מתחילה בתת-מחרוזת שהתקבלה בסוגריים, ומחזירה True/False.
- text.startswith(“xx”)
- הפעולה count מחזירה את מספר הפעמים שתת-המחרוזת מופיעה בתוך המחרוזת.
- text.count(“xx”)
- פעולה הבודקת אם המחרוזת מסתיימת בתת-מחרוזת שהתקבל בסוגריים, ומחזירה True/False.
- text.endswith(“xx”)
- ניתן לגשת לערך ספציפי בתוך המחרוזת  ע"י שימוש ב-[].
- []
- פעולה הבודקת אם המחרוזת מכילה ספרות בלבד, ומחזירה True/False.
- text.isdigit()
- חיתוך תת-מחרוזת מתוך המחרוזת המקורית.
- ללא שינוי המחרוזת המקורית.
- [ : : ]
- פעולה הבודקת אם המחרוזת מכילה אותיות בלבד, ומחזירה True/False.
- text.isalpha()
- הפעולה in בודקת אם תת-מחרוזת מופיעה בתוך המחרוזת המקורית, ומחזירה True/False.
- in
- הפעולה find מחזירה את המיקום של תת-מחרוזת בתוך המחרוזת המקורית. אם היא לא קיימת, יוחזר 1-.
- text.find(“xx”)
- החלפה של תת-מחרוזת מהמחרוזת המקורית בתת-מחרוזת אחרת שהתקבלה בסוגריים. ללא שינוי המחרוזת המקורית.
- text.replace(‘a’,’b’)
- הפעולה ()upper הופכת את כל האותיות במחרוזת לאותיות גדולות. ללא שינוי המחרוזת המקורית.
-   text.upper()

**Notes:**

- שקופית זו מכילה פעולות הקשורות למחרוזות, תוכלו לערוך חידון או סקירה קצרה על הפעולות.
- ‹#›

### Slide 6

- מחרוזות - תרגיל #1
- תרגיל #1 
- לפניכם מחרוזת. 
- עבור כל אחת מהפקודות בטבלה, רשמו מה הפלט המתקבל עבור המחרוזת.
- string = ‘Yes we can’
- פקודה
- פלט
- print(string[4])
- print(len(string))
- print(string[-3])
- print(string[ : : 2])
- print(string[4 : -4])
- print(string[ : ])

**Notes:**

- שימו לב כי הטבלה מתייחסת למחרוזת string, תלמידים לעיתים לא מקשרים כי אוס, הפעולות מתבצע על המחרוזת. הפנו את תשומת ליבם.בקשו מהתלמידים להציג נימוק, במקרה זה נימוק יכול להיות מספור תקין של תווי המחרוזת.בכל פעם שהתלמידים לא זוכרים מה הפקודה מבצעת הפנו אותם לדף העזר לרכישת מיומנות לומד עצמאי.
- מבחינה פדגוגית אפשרו למספר תלמידים לענות. תוכלו לשתף את מסך התלמידים או לבקש מהם להציג את דרך הפתרון.

### Slide 7

- מחרוזות - תרגיל #2
- קטע קוד
- פלט
- number = "12345" 
- print("4" in number)
- msg1 = "He" + "l"*2 +"o"
- msg2 = " world"
- print(msg1 + msg2) 
- print(len(msg1))
- title = "Python is fun!" 
- print(title[3]) 
- print(title[::2]) 
- print(title[-2]) 
- print(len(title)) 
- text = "Programming in python" print(text.find('r')) print(text.find('out'))
- תרגיל #2 
- לפניכם טבלה ובה ארבעה קטעי קוד.
- עבור כל קטע קוד בטבלה, רשמו מה הפלט המתקבל.

**Notes:**

- גם כאן שאלות דומות באופיין המרוכזות בטבלה. אפשרו לתלמידים זמן לפתור. 

### Slide 8

- מחרוזות - תרגיל #3
- תרגיל #3 
- "מחרוזת בדילוג 2" היא מחרוזת שנוצרת מתוך מחרוזת קיימת, תוך דילוג על שני תווים בכל פעם.
- לדוגמה: עבור המחרוזת הבאה: paryertgfhyjogqn,
- תיווצר ה"מחרוזת בדילוג 2": python.קטע הקוד שלפניכם קולט מהמשתמש מחרוזת st, 
- ומציג "מחרוזת בדילוג 2".
- השלימו את החלקים החסרים בקוד:
- (01) def create_skip2str ():
- (02) 	_________	= input("Please enter a string:")
- (03) 	skip2str = ""
- (04) 	for index in range( ____	, ____	, _____	):
- (05) 		skip2str = skip2str + _____
- (06) 	print((_____) 
- (07) create_skip2str ()

**Notes:**

- הציגו בפני התלמידים את השאלה המילולית. בקשו מאחד התלמידים להקריא את השאלה. השתמשו בכלים טכנולוגיים לסמן במרקר את החלקים החשובים.הרגילו את התלמידים לשאול את השאלות הבאות:מה שם הפעולה?מה מטרתה?מהו הקלט בגוף הלולאה?
- מהו הפלט בתום הלולאה?
- פתרו את הדוגמה, מספרו את התווים.
- לאחר מכן יש להשלים את החלקים החסרים, הנחו את התלמידים לקרוא את כל קטע הקוד. יש לחפש רמזים: שמות משתנים, מספר סבבים, חיתוך

### Slide 9

- תרגיל #4 
- "מחרוזת כוכבים" היא מחרוזת שנוצרת מתוך מחרוזת קיימת, כאשר כל תו במקום אי-זוגי במחרוזת המקורית מוחלף בסימן כוכב *. לדוגמה: עבור המחרוזת הבאה: Paybtchdoen, 
- תיווצר המחרוזת: P*y*t*h*o*n.
- קטע הקוד שלפניכם קולט מחרוזת st מהמשתמש, 
- ומציג "מחרוזת כוכבים". השלימו את הקוד:
- מחרוזות - תרגיל #4
- (01) def create_stars_str (): 
- (02) 	st =_______("Please enter a string:") 
- (03)	stars_str = ______
- (04) 	for index in range(________): 
- (05)		if ________ : 
- (06)			stars_str = stars_str + ______ 
- (07)		else: 
- (08)			stars_str = stars_str + ______
- (09)		print(_______) 
- (10) create_stars_str () 

**Notes:**

- פעלו לפני הנחיות השקפים הקודמים.

### Slide 10

- מחרוזות - תרגיל #5
- תרגיל #5 
- במזכירות התקבל מייל מסקרן המכיל מילת קסם סודית:
- "super_cali_fragi_listic_expi_ali_docious"
- בתוך המילה מסתתר מסר סודי לתלמידי עמ"ט.
- כדי לגלות מה המסר, יש לעקוב אחר קטע הקוד הבא:
- מה יודפס?
- (01) text = "super_cali_fragi_listic_expi_ali_docious"
- (02) ans = text[0:2]+text[4]+text[26]+text[12]+text[31]+text[-1]+text[24]
- (03) print(ans)

**Notes:**

- לפניכם חידה, כיצד נפתור אותה?החידה נראית ארוכה.
- נפתור כל רכיב בנפרד.ונחבר הכל ביחד.
- תוכלו לחלק את הכיתה (אפשר לתת לתלמידים שם של פרי, לבחור 5 פירות ולהכריז בסבב)כל קבוצה תפתור רכיב מהשאלה, תלמידי הקבוצה יכריזו על הפתרון לאחר שבדקו ביניהם שפתרו נכון.חברו את כל הפתרונות הכיתתיים יחד! מה קיבלתם?
- תוכלו לערוך תחרות מי אומר את המחרוזת הכי מהר כדי מעט לגוון את השיעור :)

### Slide 11

- מחרוזות - תרגיל #6
- תרגיל #6 
- נתונה פעולה what, המקבלת שתי מחרוזות: str1, str2.
- השלימו את ערכי המשתנים, לאחר ביצוע קטע הקוד הבא:
- (01) def what(str1, str2):
- (02) 		ch1 = str1[0]
- (04) 		ch2 = str2[-1]
- (05) 		word = ch1 + 'o'*2 + ch2
- (06) 		print(word)
- (07) what(‘Galit’,‘Liad’)
- ערך המשתנה
- שם המשתנה
- str1
- str2
- ch1
- ch2
- word

**Notes:**

- אפשרו לתלמידים לפתור ללא הרצה.

### Slide 12

- מחרוזות - פתרונות

**Notes:**

- ‹#›

### Slide 13

- מחרוזות - תרגיל #1 - פתרון 
- תרגיל #1 
- לפניכם מחרוזת. 
- עבור כל אחת מהפקודות בטבלה, רשמו מה הפלט המתקבל עבור המחרוזת.
- string = ‘Yes we can’
- פקודה
- פלט
- print(string[4])
- W
- print(len(string))
- 10
- print(string[-3])
- c
- print(string[ : : 2])
- Ysw a
- print(string[4 : -4])
- we
- print(string[ : ])
- Yes we can

**Notes:**

- לפניכם פתרון המשימה.

### Slide 14

- מחרוזות - תרגיל #3 - פתרון
- תרגיל #3 
- "מחרוזת בדילוג 2" היא מחרוזת שנוצרת מתוך מחרוזת קיימת, תוך דילוג על שני תווים בכל פעם.
- לדוגמה: עבור המחרוזת הבאה: paryertgfhyjogqn,
- תיווצר ה"מחרוזת בדילוג 2": python.קטע הקוד שלפניכם קולט מהמשתמש מחרוזת st, ומציג "מחרוזת בדילוג 2".
- השלימו את החלקים החסרים בקוד:
- (01) def create_skip2str ():
- (02)     string = input("Please enter a string:")
- (03)     skip2str = ""
- (04)     for index in range( 0, len(string), 3): 
- (05)        		skip2str = skip2str + string[index]
- (06)     print(skip2str)
- (07) create_skip2str()

**Notes:**

- לפניכם הפתרון.

### Slide 15

- מחרוזות - תרגיל #2 - פתרון
- קטע קוד
- פלט
- number = "12345" print("4" in number)
- True
- msg1 = "He" + "l"*2 +"o"
- msg2 = " world"
- print(msg1 + msg2) 
- print(len(msg1))
- Hello world
- title = "Python is fun!" 
- print(title[3]) 
- print(title[::2]) 
- print(title[-2]) 
- print(len(title)) 
- 5
- h
- Pto sfn
- n
- 14
- text = "Programming in python" print(text.find('r')) print(text.find('out'))
- 1
- -1
- תרגיל #2 
- לפניכם טבלה ובה ארבעה קטעי קוד.
- עבור כל קטע קוד בטבלה, רשמו מה הפלט המתקבל.

**Notes:**

- לפניכם הפתרון.

### Slide 16

- מחרוזות - תרגיל #4 - פתרון
- תרגיל #4 
- "מחרוזת כוכבים" היא מחרוזת שנוצרת מתוך מחרוזת קיימת, כאשר כל תו במקום אי-זוגי במחרוזת המקורית מוחלף בסימן כוכב *. לדוגמה: עבור המחרוזת הבאה: Paybtchdoen, 
- תיווצר המחרוזת: P*y*t*h*o*n.
- קטע הקוד שלפניכם קולט מחרוזת st מהמשתמש, 
- ומציג "מחרוזת כוכבים". השלימו את הקוד:
- (01) def create_stars_str (): 
- (02) 	st = input("Please enter a string:") 
- (03) 	stars_str = “ “
- (04) 	for index in range(len(st)): 
- (05) 		if index % 2 == 0: 
- (06) 			stars_str = stars_str + st[index] 
- (07) 		else: 
- (08) 			stars_str = stars_str + “*”
- (09) 	print(stars_str) 
- (10) create_stars_str () 

**Notes:**

- לפניכם הפתרון.

### Slide 17

- מחרוזות - תרגיל #5 - פתרון
- תרגיל #5 
- במזכירות התקבל מייל מסקרן המכיל מילת קסם סודית:
- "סופר-קלי-פרג'י-ליסטיק-אקספי-אלי-דושס".
- בתוך המילה מסתתר מסר סודי לתלמידי עמ"ט.
- כדי לגלות מה המסר, יש לעקוב אחר קטע הקוד הבא:
- מה יודפס?
- surprise
- (01) text = "super_cali_fragi_listic_expi_ali_docious"
- (02) ans = text[0:2]+text[4]+text[26]+text[12]+text[31]+text[-1]+text[24]
- (03) print(ans)

**Notes:**

- לפניכם הפתרון.

### Slide 18

- מחרוזות - תרגיל #6 - פתרון
- תרגיל #6 
- נתונה פעולה what, המקבלת שתי מחרוזות: str1, str2.
- השלימו את ערכי המשתנים, לאחר ביצוע קטע הקוד הבא:
- (01) def what(str1, str2):
- (02) 		ch1 = str1[0]
- (04) 		ch2 = str2[-1]
- (05) 		word = ch1 + 'o'*2 + ch2
- (06) 		print(word)
- (07) what(‘Galit’,‘Liad’)
- ערך המשתנה
- שם המשתנה
- Galit
- str1
- Liad
- str2
- G
- ch1
- d
- ch2
- Good
- word

**Notes:**

- לפניכם הפתרון.

### Slide 19

- הצב הגרפי

**Notes:**

- תרגילים מבחינות מפמ"ר בנושא הצב הגרפי.

### Slide 20

- קבלת ערכי מיקום הצב למשתנים
- x = player.pos()[0] 
- y = player.pos()[1]  
- קריאה למחלקה הגרפית
- import turtle   	
- שינוי מיקום של הצב
- player.setx(x)	player.sety(y)       	
-  מסך עבור צב
- wn = turtle.Screen() 
- עט מטה – הצב יצייר מסלול כשיבצע הוראות
- player.pendown()
-  יוצר צב ושמו player 
- player = turtle.Turtle()	
- עט מעלה – הצב לא יצייר מסלול כשיבצע הוראות
- player.penup()
-  התקדמות קדימה steps צעדים
- player.forward(steps)  
- שינוי עובי העט שאיתו מציירים
- player.pensize(num)
-  התקדמות אחורה steps צעדים
- player.backward(steps)
- שינוי צבע העט שאיתו מצייריםשינוי צבע הצב
- player.pencolor()	
- player. color()
- סיבוב ימין/שמאל num מעלות
- player.right(num) 	
- player.left(num)   
- שינוי צורת הצב
- player.shape("turtle") 
- קפיצה למיקום על המסך
- player.goto(x, y)       	
- סיכום הפעולות שנלמדו

**Notes:**

- תרגילים מבחינות מפמ"ר בנושא הצב הגרפי.

### Slide 21

- הצב הגרפי - תרגיל 4
- הצב הגרפי - תרגיל #1
- תרגיל #1 
- לפניכם משטח. אורכה ורוחבה של כל משבצת במשטח 40 צעדים. 
- הצב תופס משבצת שלמה. 
- על פי הקוד הבא, סרטטו על גבי המשטח מה יצייר הצב.
- import turtle 
- wn = turtle.Screen()
- player = turtle.Turtle() 
- player.shape("turtle") 
- player.goto(0,0) 
- player.left(180) 
- player.forward(80) 
- player.left(90) 
- player.forward(160) 
- player.left(90) 
- player.forward(80) 
- player.left(90) 
- player.forward(80) 
- player.left(90) 
- player.forward(80) 
- turtle.mainloop()  

### Slide 22

- הצב הגרפי - תרגיל #2
- תרגיל #2 
- עדי כתבה תסריט, שלפיו כל לחיצה על העכבר (הקלקה) תגרום לציור ריבוע על המסך, במיקום הלחיצה.
- הריבוע יצויר על המסך בצבעים אדום וכחול לסירוגין (הקלקה ראשונה — אדום, הקלקה שנייה — כחול, וכן הלאה).
- בכל הקלקה יצויר ריבוע שאורך צלעו יגדל ב-2.
- לפניכם קטע קוד שחסרות בו הוראות.
- השלימו את ההוראות החסרות.
- הערה: המשתנה size מייצג את אורך צלע הריבוע. 
- המשתנה click_num מייצג את מספר ההקלקות.
- import turtle 
- def do_it(x,y):
- global click_num 
- global size 
- player.penup() 
- player.goto(x,y) player.shapesize(size)
- if % 2 == 0: 
- player.color("____")
- else:
- player.color("____")
- player.stamp()
- click_num = ________ + _____
- size = ______  + _______
- tw = turtle.Screen()
- click_num = 0
- size = 2 tw.onclick(do_it)
- player = turtle.Turtle() player.shape("square") 
- turtle.mainloop()

### Slide 23

- הצב הגרפי - תרגיל #3
- תרגיל #3 
- לפניכם ארבעה קטעי קוד המשתמשים בספריית turtle.
- כל קטע קוד מצייר צורה שונה.
- התאימו לכל קטע קוד את הצורה שהוא מצייר. 
- הניחו שבתחילת כל קטע קוד מופיעות השורות הבאות, המשותפות לכל הקטעים:
- import turtle 
- wn = turtle.Screen() 
- player = turtle.Turtle() player.shape("turtle") 
- המשך בשקף הבא

### Slide 24

- הצב הגרפי - תרגיל #3
- for x in range(360):
- player.left(1) player.forward(1)
- turtle.mainloop()
- for index in range(3): 
-      player.forward(100)     player.left(360/3)
- turtle.mainloop()
- player.left(180) player.forward(80) player.left(90) player.forward(70)
- for index in range(4):	player.forward(80) 	player.left(90)
- turtle.mainloop()
- for index in range(4): 	player.left(90)	player.forward(50)	player.right(90)	player.forward(50)
- turtle.mainloop()
- 1
- 2
- 3
- 4
- א
- ב
- ג
- ד

### Slide 25

- ב
- א
- ד
- ג
- הצב הגרפי - תרגיל #4
- תרגיל #4 
- לפניכם קטע קוד המשתמש בספריית turtle.
- קטע הקוד הורץ. איזה מבין הפלטים שלפניכם יוצג על גבי מסך המחשב? 
- סמנו את התשובה הנכונה בעיגול.
- import turtle
- tw = turtle.Screen()
- player = turtle.Turtle()
- player.shape('square')
- size = 100
- player.pendown()
- for index in range(4):
-         for item in range(4):
-             player.forward(size)
-             player.left(90)
-             size = size - 20
- turtle.mainloop()

**Notes:**

- תרגיל מבחינה.
- יש להקצות מספיק זמן לפתרון התרגיל. יש לפתור את התרגיל בכתב, ללא הרצה בתוכנה. הפתרונות במצגת לעיתים מוצגים ללא מערכת הצירים.
- יש להציג פתרונות של התלמידים, לעורר דיון ושיח ולהציג פתרון מלא על ידי המורה.

### Slide 26

- הצב הגרפי - תרגיל #5
- תרגיל #5 
- לפניכם שלושה קטעי קוד המשתמשים בספריית turtle. כל קטע קוד מצייר צורה שונה. 
- יש להתאים בין קטע הקוד לצורה שהוא מצייר. 
- הניחו שבתחילת כל קטע קוד מופיעות השורות הבאות, המשותפות לכל הקטעים:
- import turtle 
- wn = turtle.Screen() 
- player = turtle.Turtle() player.shape("turtle") 
- המשך בשקף הבא

### Slide 27

- הצב הגרפי - תרגיל #5
- for index in range(3):
- player.forward(100)
- 	player.left(360 / 3)
- for index in range(3):
- player.forward(100)
- 	player.right(360 / 3) 
- turtle.mainloop()
- for index in range(5):
- player.forward(60)
-     player.left(360/5)
- turtle.mainloop()
- for item in range(180):
- player.forward(5) 
- player.left(2) 
- for item in range(180): 
- player.forward(5) 
- player.right(2) 
- turtle.mainloop() 
- 1
- 2
- 3
- א
- ב
- ג

### Slide 28

- הצב הגרפי - תרגיל #6
- תרגיל #6 
- גודל כל משבצת במשטח 20X20.  
- על פי הקוד הבא, סרטטו על גבי המשטח מה יצייר הצב.
- import turtle
- scrn = turtle.Screen()
- player = turtle.Turtle()
- player.penup()
- player.goto(0,100)
- player.pendown()
- player.goto(100,100)
- player.goto(0,0)
- player.goto(100,0) 

### Slide 29

- הצב הגרפי - תרגיל #7
- תרגיל #7 
- לפניכם קטע קוד המשתמש בספריית turtle.
- סרטטו על גבי התרשים שלפניכם את הצורה המתקבלת בתום הרצת התוכנית:
- באיזו נקודה נמצא player בתום הרצת התוכנית?________ 
- הערה: גודל כל משבצת 50X50
- 90°
- 0°
- 270°
- 180°
- import turtle
- wn = turtle.Screen()
- player = turtle.Turtle()
- player.penup()
- player.goto(0,0)
- player.pendown()
- for i in range(4):
- player.forward(50)
- player.left(90)
- player.forward(50)
- player.right(90)
- turtle.mainloop()

### Slide 30

- הצב הגרפי - תרגיל #8
- תרגיל #8 
- לפניכם תוכנית המציירת שני ריבועים, אחד בתוך השני, כמתואר בתרשים הבא.
- הערה: גודל כל משבצת 50X50. יש להשלים את הקטעים החסרים בתוכנית. 
- import turtle
- player = turtle.Turtle()
- player.penup()
- player.goto(-100,100)
- player.pendown()
- size = ____
- for i in range(___):
-     player.forward(size)
-     player.right(___)
- player.penup()
- player.goto(___,___)
- player.pendown()
- size = ___
- for i in range(___):
-     player.forward(size)
-     player.right(___)
- turtle.mainloop()

### Slide 31

- צב גרפי - פתרונות

**Notes:**

- ‹#›

### Slide 32

- הצב הגרפי - תרגיל 4
- הצב הגרפי - תרגיל #1 - פתרון
- תרגיל #1 
- לפניכם משטח. אורכה ורוחבה של כל משבצת במשטח 40 צעדים. 
- הצב תופס משבצת שלמה. 
- על פי הקוד הבא, סרטטו על גבי המשטח מה יצייר הצב.
- import turtle 
- wn = turtle.Screen()
- player = turtle.Turtle() 
- player.shape("turtle") 
- player.goto(0,0) 
- player.left(180) 
- player.forward(80) 
- player.left(90) 
- player.forward(160) 
- player.left(90) 
- player.forward(80) 
- player.left(90) 
- player.forward(80) 
- player.left(90) 
- player.forward(80) 
- turtle.mainloop()  

### Slide 33

- הצב הגרפי - תרגיל #2 - פתרון
- תרגיל #2 
- עדי כתבה תסריט, שלפיו כל לחיצה על העכבר (הקלקה) תגרום לציור ריבוע על המסך, במיקום הלחיצה.
- הריבוע יצויר על המסך בצבעים אדום וכחול לסירוגין (הקלקה ראשונה — אדום, הקלקה שנייה — כחול, וכן הלאה).
- בכל הקלקה יצויר ריבוע שאורך צלעו יגדל ב-2.
- לפניכם קטע קוד שחסרות בו הוראות.
- השלימו את ההוראות החסרות.
- הערה: המשתנה size מייצג את אורך צלע הריבוע. 
- המשתנה click_num מייצג את מספר ההקלקות.
- import turtle 
- def do_it(x,y):
- global click_num 
- global size 
- player.penup() 
- player.goto(x,y) player.shapesize(size)
- if % 2 == 0: 
- player.color("red")
- else:
- player.color("blue")
- player.stamp()
- click_num = click_num + 1
- size = size + 2
- tw = turtle.Screen()
- click_num = 0
- size = 2 tw.onclick(do_it)
- player = turtle.Turtle() player.shape("square") 
- turtle.mainloop()

### Slide 34

- הצב הגרפי - תרגיל #3 - פתרון
- for x in range(360):
- player.left(1) player.forward(1)
- turtle.mainloop()
- for index in range(3): 
-      player.forward(100)     player.left(360/3)
- turtle.mainloop()
- player.left(180) player.forward(80) player.left(90) player.forward(70)
- for index in range(4):	player.forward(80) 	player.left(90)
- turtle.mainloop()
- for index in range(4): 	player.left(90)	player.forward(50)	player.right(90)	player.forward(50)
- turtle.mainloop()
- 1
- 2
- 3
- 4
- א
- ב
- ג
- ד

### Slide 35

- ב
- א
- ד
- ג
- הצב הגרפי - תרגיל #4 - פתרון
- תרגיל #4 
- לפניכם קטע קוד המשתמש בספריית turtle.
- קטע הקוד הורץ. איזה מבין הפלטים שלפניכם יוצג על גבי מסך המחשב? 
- סמנו את התשובה הנכונה בעיגול.
- import turtle
- tw = turtle.Screen()
- player = turtle.Turtle()
- player.shape('square')
- size = 100
- player.pendown()
- for index in range(4):
-         for item in range(4):
-             player.forward(size)
-             player.left(90)
-             size = size - 20
- turtle.mainloop()

**Notes:**

- פתרון.

### Slide 36

- הצב הגרפי - תרגיל #5 - פתרון
- for index in range(3):
- player.forward(100)
- 	player.left(360 / 3)
- for index in range(3):
- player.forward(100)
- 	player.right(360 / 3)
- turtle.mainloop()
- for index in range(5):
- player.forward(60)
-     player.left(360/5)
- turtle.mainloop()
- for item in range(180):
- player.forward(5) 
- player.left(2) 
- for item in range(180): 
- player.forward(5) 
- player.right(2) 
- turtle.mainloop() 
- 1
- 2
- 3
- א
- ב
- ג

### Slide 37

- הצב הגרפי - תרגיל #6 - פתרון
- תרגיל #6 
- גודל כל משבצת במשטח 20X20.  
- על פי הקוד הבא, סרטטו על גבי המשטח מה יצייר הצב.
- import turtle
- scrn = turtle.Screen()
- player = turtle.Turtle()
- player.penup()
- player.goto(0,100)
- player.pendown()
- player.goto(100,100)
- player.goto(0,0)
- player.goto(100,0) 

### Slide 38

- הצב הגרפי - תרגיל #7 - פתרון
- תרגיל #7 
- לפניכם קטע קוד המשתמש בספריית turtle.
- סרטטו על גבי התרשים שלפניכם את הצורה המתקבלת בתום הרצת התוכנית:
- בתום הרצת התוכנית, player נמצא בנקודה (200,200). 
- הערה: גודל כל משבצת 50X50
- import turtle
- wn = turtle.Screen()
- player = turtle.Turtle()
- player.penup()
- player.goto(0,0)
- player.pendown()
- for i in range(4):
- player.forward(50)
- player.left(90)
- player.forward(50)
- player.right(90)
- turtle.mainloop()

### Slide 39

- הצב הגרפי - תרגיל #8 - פתרון
- תרגיל #8 
- לפניכם תוכנית המציירת שני ריבועים, אחד בתוך השני, כמתואר בתרשים הבא.
- הערה: גודל כל משבצת 50X50. יש להשלים את הקטעים החסרים בתוכנית. 
- import turtle
- player = turtle.Turtle()
- player.penup()
- player.goto(-100,100)
- player.pendown()
- size = 200
- for i in range(4):
-     player.forward(size)
-     player.right(90)
- player.penup()
- player.goto(-50,50)
- player.pendown()
- size = 100
- for i in range(4):
-     player.forward(size)
-     player.right(90)
- turtle.mainloop()

### Slide 40

- 19.4 | תרגול לפיצוח - דף עבודה
- היכנסו לרכיב 19.4 | תרגול לפיצוח - דף עבודה וענו על השאלות.
- שאלות חובה: 1-7
- שאלות בחירה: 8-10 
- בסיום, הגישו את דף העבודה. 

**Notes:**

- ‹#›

### Slide 41

- מאסטר פייתון
- היכנסו לרכיב 19.5 | מאסטר פייתון - תנאי פשוט וענו על השאלות. 

**Notes:**

- ‹#›

### Slide 42

-  נתרגל ונפתור תרגילים בעזרת תנאים והצב הגרפי.
- בשיעור הבא…
