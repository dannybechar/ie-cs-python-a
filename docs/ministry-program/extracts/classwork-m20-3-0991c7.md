# [Template] 20.3 _ פייתון א _ תרגול לפיצוח #2 - דף עבודה _ אירועי עכבר - פרויקט הצייר.docx

Source: `Classwork/20.3 _ תרגול לפיצוח #2 - דף עבודה _ אירועי עכבר - פרויקט הצייר/[Template] 20.3 _ פייתון א _ תרגול לפיצוח #2 - דף עבודה _ אירועי עכבר - פרויקט הצייר.docx`

שיעור 20 | תרגול לפיצוח #2 

אירועי עכבר - פרויקט הצייר

משימה 1: 

כיתבו פעולה המזיזה את הצב למיקום הקלקת העכבר.

משימה 2: 

כיתבו פעולה המסמנת את מיקום הלחיצה – חתימה.

משימה 3:

כיתבו פעולה המזיזה את הצב למיקום הלחיצה ומשנה את צבע העט לפי רבעון מיקום הלחיצה. כאשר הצב יזוז למיקום החדש,  צבע הקו יתאים לצבע הרבעון שלו.

משימה 4:

כתבו תכנית המציירת עיגולים בצבעים כחול-אדום-ירוק  לסרוגין

משימה 5:

כתבו תכנית המשנה רנדומלית את גודל הצב כאשר מקליקים עליו

משימה 6:

כתבו תכנית המשנה את גודל הצב לפי החוקיות הבאה:הגדלת ה-size של הצב כאשר מקליקים עליו.הקטנת ה-size של הצב כאשר מקליקים בחלון מחוץ לגבולות הצב.

פתרון משימה 1:

import turtlewn = turtle.Screen()def clickMe(x,y):    player.penup()    player.goto(x,y)wn.onclick(clickMe)player = turtle.Turtle()turtle.mainloop()פעולת הלחיצה – הרמת עט ותזוזה למיקום הלחיצהיצירת צב בשם player ורישום למאזין לחיצה על המסך

import turtlewn = turtle.Screen()def clickMe(x,y):    player.penup()    player.goto(x,y)wn.onclick(clickMe)player = turtle.Turtle()turtle.mainloop()

פעולת הלחיצה – הרמת עט ותזוזה למיקום הלחיצה

יצירת צב בשם player ורישום למאזין לחיצה על המסך

פתרון משימה 2:

import turtlewn = turtle.Screen()def clickMe(x,y):    player.penup()    player.goto(x,y)	player.stamp()wn.onclick(clickMe)player = turtle.Turtle()turtle.mainloop()פעולת הלחיצה – הרמת עט, תזוזה למיקום הלחיצה וחתימהיצירת צב בשם player ורישום למאזין לחיצה על המסך

import turtlewn = turtle.Screen()def clickMe(x,y):    player.penup()    player.goto(x,y)

	player.stamp()wn.onclick(clickMe)player = turtle.Turtle()turtle.mainloop()

פעולת הלחיצה – הרמת עט, תזוזה למיקום הלחיצה וחתימה

יצירת צב בשם player ורישום למאזין לחיצה על המסך

פתרון משימה 3:

wn = turtle.Screen()def clickMe(x,y):    if x>=0 and y>=0:        player.pencolor('red')    elif x>=0 and y<0:        player.pencolor('blue')    elif x<0 and y>=0:        player.pencolor('green')    else:        player.pencolor('yellow')    player.goto(x,y)wn.onclick(clickMe)player = turtle.Turtle()turtle.mainloop()שינוי צבע הצב על פי מיקום הלחיצה

wn = turtle.Screen()def clickMe(x,y):    if x>=0 and y>=0:        player.pencolor('red')    elif x>=0 and y<0:        player.pencolor('blue')    elif x<0 and y>=0:        player.pencolor('green')    else:        player.pencolor('yellow')    player.goto(x,y)wn.onclick(clickMe)player = turtle.Turtle()turtle.mainloop()

שינוי צבע הצב על פי מיקום הלחיצה

פתרון משימה 4:

משתנה global – משתנה אשר מוכר בכל התוכנית כל בתוך פונקציות. ניתן לשינוי רק אם הכרזנו עליו כ global

wn = turtle.Screen()counter = 0 # ספירת מספר הלחיצותdef clickMe(x,y):    global counter    color = 'green'    if counter % 3 == 1:        color = 'blue'    elif counter % 3 == 2:        color = 'red'    player.penup()    player.goto(x,y)    player.color(color)    player.stamp()    counter +=1player = turtle.Turtle()player.shape("circle")player.shapesize(2)wn.onclick(clickMe)turtle.mainloop()שינוי צורה וגודל הצב.רישום למאזין לחיצה

wn = turtle.Screen()counter = 0 # ספירת מספר הלחיצותdef clickMe(x,y):    global counter    color = 'green'    if counter % 3 == 1:        color = 'blue'    elif counter % 3 == 2:        color = 'red'    player.penup()    player.goto(x,y)    player.color(color)    player.stamp()    counter +=1player = turtle.Turtle()player.shape("circle")player.shapesize(2)wn.onclick(clickMe)turtle.mainloop()

שינוי צורה וגודל הצב.

רישום למאזין לחיצה

פתרון משימה 5:

במשימה זו נתבקשנו לשנות את גודל הצב בלחיצה עליו. לכן, רשמנו את הצב למאזין לחיצה. בתרגילים הקודמים רשמנו את המסך.

בנוסף, בכדי להשתמש במספרים אקראיים (רנדומלים), יש לייבא את ספרית random

import randomwn = turtle.Screen()def clickMe(x,y):    num = random.randint(1,6)    player.turtlesize(num)player = turtle.Turtle()player.shape("circle")player.shapesize(2)player.onclick(clickMe)turtle.mainloop()

import randomwn = turtle.Screen()def clickMe(x,y):    num = random.randint(1,6)    player.turtlesize(num)player = turtle.Turtle()player.shape("circle")player.shapesize(2)player.onclick(clickMe)turtle.mainloop()

פתרון משימה 6:

לחיצה על הצב מפעילה גם את פעולת לחיצה על המסך. לכן, נפריד את הלחיצות לכםתורים שונים.

כפתור שמאל של העכבר – לחיצה על הצב.

כפתור ימין של העכבר – לחיצה על המסך.

wn = turtle.Screen()size = 2def clickTurtle(x,y):    global size    size +=1    player.turtlesize(size)def clickScreen(x,y):    global size    size -=1    player.turtlesize(size)player = turtle.Turtle()player.shape("circle")player.shapesize(2)player.onclick(clickTurtle,btn=1)wn.onclick(clickScreen,btn=3)

wn = turtle.Screen()size = 2def clickTurtle(x,y):    global size    size +=1    player.turtlesize(size)def clickScreen(x,y):    global size    size -=1    player.turtlesize(size)player = turtle.Turtle()player.shape("circle")player.shapesize(2)

player.onclick(clickTurtle,btn=1)wn.onclick(clickScreen,btn=3)
