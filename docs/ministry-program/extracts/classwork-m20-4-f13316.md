# [Template] 20.4 _ פייתון א _ תרגול לפיצוח #3 - דף עבודה _ אירועי מקלדת - משחק פינג פונג.docx

Source: `Classwork/20.4 _ תרגול לפיצוח #3 - דף עבודה _ אירועי מקלדת - משחק פינג פונג/[Template] 20.4 _ פייתון א _ תרגול לפיצוח #3 - דף עבודה _ אירועי מקלדת - משחק פינג פונג.docx`

שיעור 20 | תרגול לפיצוח #3

אירועי מקלדת - משחק פינג פונג

האזנה למקלדת

כדי שהצב שלנו יגיב לאירועי מקלדת נוסיף לחלון הצב את הפקודה()listen, אשר תאזין לאירועי מקלדת.

screen .listen()

()listen הינה פקודת ההאזנה למסך, שמטרתה לאפשר  קליטה של אירועי מקלדת (הקשות מקלדת). את הפקודה נוסיף מיד לאחר יצירת החלון של הצב.

אירוע מקלדת מתרחש כאשר לוחצים על מקש כלשהו בזמן ריצת התכנית, בעקבותיו יתרחשו סדרת הוראות. 

משימה 1 - הזזת הצב על המסך

לפניכם קטע תוכנית:

import turtlescreen = turtle.Screen()screen .setup(500, 500)wn.listen()pen = turtle.Turtle()pen .penup()pen .setposition(-230, 230)pen .pensize(4)pen .color("red")pen .pencolor("red")pen .shape("arrow")turtle.mainloop()

עתה ניצור ארבע פונקציות, אשר יגרמו לתזוזת הצב על פי החיצים שנקיש במקלדת:

הפעולה ()KL גורמת לצב לנוע את שמאלה 5 צעדים:

def kL():    pen.setheading(180)    pen.forward(20)

נזמן את הפעולה הפעולה בתוכנית הראשית אופן הבא:

screen.onkey(kL, "Left")

בצעו את המשימות שלפניכם:

א. 

כתבו שלוש פונקציות לתזוזת הצב:

ימינה  (0)  - "Right"

למעלה (90) – "Up"

למטה (270) – "Down"  

ב. זמנו אותן מהתוכנית הראשית.

ג. בדקו אם הצב הולך לפי כיוון החיצים.

ד. הוסיפו פקודות ()pendown ,stamp או את הצבעים של הצב בהתאם לתזוזה. 

הגישו את עבודתכם. 

משימה 2 - יצירת משחק פינג פונגספריית turtle מאפשרת יצירת גרפיקה על המסך באמצעות צב הנע ומצייר בקווים. אחד המאפיינים השימושיים בספרייה זו הוא האפשרות לשלוט בצב באמצעות מקשי המקלדת, כמו מקשי החיצים.

כדי לבצע זאת נשתמש בפעולה ()onkey ולאחריו הפעולה ()listen, בהתאם לתבנית הבאה:

import turtle

screen = turtle.Screen()

def go_up():

        #write your code here

screen.onkeypress(go_up , "Up")

screen.listen()

הפעולה ()screen.onkey מקשרת את לחיצות מקשים הספציפיות לפעולות המתאימות. 

הפעולה ()screen.listen אומרת למסך הצב שיתחיל להאזין לאירועי מקלדת.

לפניכם קטע תוכנית חלקי המדגים תנועה עם החיצים, screen הינו אובייקט המסך:

#our code

# חיבור המקשים לפעולות התזוזה 

screen.onkeypress(move_up, "Up") # מקשר את מקש החץ העליון לפעולת move_up screen.onkeypress(move_down, "Down") # מקשר את מקש החץ התחתון לפעולת move_down screen.onkeypress(move_left, "Left") #  מקשר את מקש החץ השמאלי לפעולתmove_left screen.onkeypress(move_right, "Right") # מקשר את מקש החץ הימני לפעולת move_right

screen.listen() # מאפשר למקש להאזין לאירועים

בשיעור זה ניצור משחק pong, לפניכם הדרכה ליצירת המשחק. בסיום ההדרכה הריצו את הקוד ולאחר מכן תוכלו לשפר את המשחק.

במשחק שלנו ניצור שני מחבטים אותם נזיז בעזרת המקשים, ביניהם ינוע כדור מקפץ על המסך כפי שמופיע בתמונה.

## תכנון המשחק והאילוצים שלו:

- הגדרת המסך:

- ניצור חלון המשחק עם רקע שחור וגודל של 800x600 פיקסלים.

- יצירת המחבטים והכדור:

- כל מחבט נוצר כעצם turtle עם צורת ריבוע, צבע לבן וגדלים מתאימים.

- הכדור נוצר גם הוא כעצם turtle עם תכונות דומות ונקודת התחלה במרכז המסך.

- יצירת לוח התוצאות:

- עצם turtle נוסף המשמש לכתיבת התוצאות של השחקנים על המסך.

- פעולות להזזת המחבטים:

- פעולות paddle_a_up, paddle_a_down, paddle_b_up, paddle_b_down להזזת המחבטים למעלה ולמטה בהתאמה.

- הגדרת המקשים:

- שימוש בפעולות()screen.listen ו- ()screen.onkeypress כדי לקשר את המקשים לפעולות הזזת המחבטים.

- הלולאה הראשית של המשחק:

- הלולאה מעדכנת את מיקום הכדור ובודקת אם הוא פוגע בגבולות המסך או במחבטים.

- התנגשות עם גבולות המסך מעלה או מורידה את הניקוד ומעדכנת את לוח התוצאות.

- התנגשות עם המחבטים משנה את כיוון הכדור.

הגדרת המסך:

- שימוש ב ()turtle.Screen  ליצירת חלון עם כותרת, צבע רקע וגודל מותאם.

יצירת הצב:

- שימוש ב  ()turtle.Turtle ליצירת צב עם צורה, צבע ומהירות מותאמים.

פעולות להזזת הצב:

- move_up : מקבלת את המיקום הנוכחי של הצב בציר ה-y ומעדכנת את המיקום על ידי הוספת 20 יחידות למעלה.

- move_down : מקבלת את המיקום הנוכחי של הצב בציר ה-y ומעדכנת את המיקום על ידי חיסור 20 יחידות למטה.

- move_left : מקבלת את המיקום הנוכחי של הצב בציר ה-x ומעדכנת את המיקום על ידי חיסור 20 יחידות שמאלה.

- move_right : מקבלת את המיקום הנוכחי של הצב בציר ה-x ומעדכנת את המיקום על ידי הוספת 20 יחידות ימינה.

חיבור המקשים לפעולות התזוזה:

- screen.listen : מאפשר למסך להאזין לאירועי מקשים.

- screen.onkey : מקשר מקשי חיצים לפעולות התזוזה המתאימות.

לולאת התכנית הראשית:

- screen.mainloop : לולאה המאפשרת לתוכנית להמשיך לרוץ ולהאזין לאירועי מקשים כל הזמן.

הקוד:

import turtle

# הגדרת המסך

screen = turtle.Screen()

screen.title("Pong Game")

screen.bgcolor("black")

screen.setup(width=800, height=600)

screen.tracer(0)

# מחבט A

paddle_a = turtle.Turtle()

paddle_a.speed(0)

paddle_a.shape("square")

paddle_a.color("white")

paddle_a.shapesize(stretch_wid=6, stretch_len=1)

paddle_a.penup()

paddle_a.goto(-350, 0)

# מחבט B

paddle_b = turtle.Turtle()

paddle_b.speed(0)

paddle_b.shape("square")

paddle_b.color("white")

paddle_b.shapesize(stretch_wid=6, stretch_len=1)

paddle_b.penup()

paddle_b.goto(350, 0)

# כדור

ball = turtle.Turtle()

ball.speed(0)

ball.shape("square")

ball.color("white")

ball.penup()

ball.goto(0, 0)

ball.dx = 0.15

ball.dy = -0.15

# ניקוד

score_a = 0

score_b = 0

# לוח תוצאות

pen = turtle.Turtle()

pen.speed(0)

pen.color("white")

pen.penup()

pen.hideturtle()

pen.goto(0, 260)

pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# פעולות להזזת המחבטים

def paddle_a_up():

    y = paddle_a.ycor()

    if y < 250:

        y += 20

    paddle_a.sety(y)

def paddle_a_down():

    y = paddle_a.ycor()

    if y > -240:

        y -= 20

    paddle_a.sety(y)

def paddle_b_up():

    y = paddle_b.ycor()

    if y < 250:

        y += 20

    paddle_b.sety(y)

def paddle_b_down():

    y = paddle_b.ycor()

    if y > -240:

        y -= 20

    paddle_b.sety(y)

# מקשים להזזת המחבטים, עליכם להשלים את החסר

screen.________________(paddle_a_up, "w")

screen.onkeypress(________________, "s")

screen.onkeypress(paddle_b_up, "Up")

____________.onkeypress(paddle_b_down, ______________)

screen.listen()

# הלולאה הראשית של המשחק

while True:

    screen.update()

    # הזזת הכדור

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    # בדיקת גבולות המסך הכדור

    if ball.ycor() > 290:

        ball.sety(290)

        ball.dy *= -1

    if ball.ycor() < -290:

        ball.sety(-290)

        ball.dy *= -1

    if ball.xcor() > 390:

        ball.goto(0, 0)

        ball.dx *= -1

        score_a += 1

        pen.clear()

        msg = ("Courier", 24, "normal")

                 pen.write(f"Player A: {score_a}  Player B: {score_b}", align = "center", font = msg)

    if ball.xcor() < -390:

        ball.goto(0, 0)

        ball.dx *= -1

        score_b += 1

        pen.clear()

        msg = ("Courier", 24, "normal")

        pen.write(f"Player A: {score_a}  Player B: {score_b}", align = "center", font = msg)

    # בדיקת התנגשות עם המחבטים

    if (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):

        ball.setx(340)

        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):

        ball.setx(-340)

        ball.dx *= -1

בצעו את המשימות הבאות:

א. השלימו את שורות הקוד שלפניכם:

screen.________________(paddle_a_up, "w")

screen.onkeypress(________________, "s")

screen.onkeypress(paddle_b_up, "Up")

____________.onkeypress(paddle_b_down, ______________)

screen.listen()

תרמילון:

paddle_a_down | "Down" | onkeypress | screen |

ב. סמנו נכון / לא נכון

- מטרת הוראה  ball.dx *= -1 היא החלפת כיוון             

- ball.xcor() > 390 מאפשרים לנוע בגבולות שנקבעו על המסך              

- score_b += 1 מונה את כמות התזוזות             

- הפעולה ()ball.setx משמשת לקבוע את נקודת ה X בה ימוקם הכדור             

ג. עדכנו את צבעי הרקע, המחבטים והכדור.

ד. עדכנו את גבולות המסך ודאגו לתקן את הקוד כך שהכדור לא יצא מהגבולות שהוגדרו.

ה. שנו את מהירות התזוזה של הכדור.

תוכלו לשתף את המשחק בתחרויות ופסטיבלים.
