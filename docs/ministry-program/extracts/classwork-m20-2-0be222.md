# 20.2 _ פייתון א _ תרגול לפיצוח #1 - דף עבודה _ תרגול כיוונים וצורות - מציירים מספרים.docx

Source: `Classwork/20.2 _ תרגול לפיצוח #1 - דף עבודה _ תרגול כיוונים וצורות - מציירים מספ/20.2 _ פייתון א _ תרגול לפיצוח #1 - דף עבודה _ תרגול כיוונים וצורות - מציירים מספרים.docx`

שיעור 20 | תרגול לפיצוח #1 

תרגול כיוונים וצורות - מציירים מספרים

במשימה זו עליכם ליצור ספרות על המסך באמצעות הצב.

- השלימו את הפקודות החסרות במקום שמצוייר קו.

- לאחר השלמת הפקודות זמנו את הפעולות וצרו את המספרים 123, 689. שימו לב שעליכם לאתחל את כיוון  הצב לפני שאתם מציירים סיפרה חדשה.  הקפידו לשמור על מרחקים בין הספרות היעזרו בפעולות ()goto (), seth.

- כתבו פעולה המגרילה סיפרה ומציירת אותה. אל תשכחו לבצע import random

- שפרו את הקוד, שנו את עובי העט וצבעו.

- זמנו את הספרות, 2 ו-3 בלחיצה על המסך.

import turtle

# פעולה  שמציירת את הספרה 1

def draw_one():

    turtle.penup()

    turtle.goto(0, 0)

    turtle.pendown()

    turtle.left(90)

    turtle.forward(100)

# פעולה  שמציירת את הספרה 2

def draw_two():

    turtle.penup()

    turtle.goto(0, 100)

    turtle.pendown()

    turtle.right(90)

    turtle.circle(50, 180)

    turtle.right(90)

    turtle.forward(100)

    turtle.left(90)

    turtle.forward(100)

# פעולה  שמציירת את הספרה 3

def draw_three():

    turtle.penup()

    turtle.goto(0, 100)

    turtle.pendown()

    turtle.circle(50, -180)

    turtle.left(      ) 

    turtle.circle(50, -180)

# פעולה  שמציירת את הספרה 4

def draw_four():

    turtle.penup()

    turtle.goto(0, 0)

    turtle.pendown()

    turtle.          (100)

    turtle.backward(50)

    turtle.left(90)

    turtle.forward(100)

    turtle.right(90)

    turtle.forward(50)

# פעולה  שמציירת את הספרה 5

def draw_five():

    turtle.penup()

    turtle.goto(100, 100)

    turtle.pendown()

    turtle.backward(100)

    turtle.right(90)

    turtle.forward(50)

    turtle.left(      ) 

    turtle.forward(50)

    turtle.right(90)

    turtle.forward(50)

# פעולה  שמציירת את הספרה 6

def draw_six():

    turtle.penup()

    turtle.goto(0, 100)

    turtle.pendown()

    turtle.circle(50, 180)

    turtle.right(180)

    turtle.circle(50, -360)

# פעולה  שמציירת את הספרה 7

def draw_seven():

    turtle.penup()

    turtle.goto(0, 100)

    turtle.pendown()

    turtle.forward(100)

    turtle.right(135)

    turtle.forward(140)

# פעולה  שמציירת את הספרה 8

def draw_eight():

    turtle.penup()

    turtle.goto(0, 50)

    turtle.          () 

    turtle.circle(50)

    turtle.left(90)

    turtle.penup()

    turtle.goto(0, 150)

    turtle.pendown()

    turtle.circle(50)

# פעולה  שמציירת את הספרה 9

def draw_nine():

    turtle.penup()

    turtle.goto(0, 0)

    turtle.pendown()

    turtle.circle(50, -360)

    turtle.right(180)

    turtle.penup()

    turtle.goto(0, 50)

    turtle.pendown()

    turtle.circle(50, -180)
