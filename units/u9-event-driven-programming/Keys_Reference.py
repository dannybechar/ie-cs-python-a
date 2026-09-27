# Unit 9.4 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle

pen_on = True


# Task 1: four directions - a key event sends no x and y
def up():
    turtle.sety(turtle.ycor() + 20)


def down():
    turtle.sety(turtle.ycor() - 20)


# Task 2: stay inside -200 ... 200 on the x axis
def left():
    new_x = turtle.xcor() - 20
    if new_x >= -200:
        turtle.setx(new_x)


def right():
    new_x = turtle.xcor() + 20
    if new_x <= 200:
        turtle.setx(new_x)


# Task 2: space switches between drawing and moving without drawing
def toggle_pen():
    global pen_on
    pen_on = not pen_on
    if pen_on:
        turtle.pendown()
    else:
        turtle.penup()


def task_1_2():
    turtle.shape("turtle")
    turtle.listen()
    turtle.onkey(up, "Up")
    turtle.onkey(down, "Down")
    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")
    turtle.onkey(toggle_pen, "space")
    turtle.done()


# Task 3 (challenge): reach the target at (160, 100)
def check_goal():
    if turtle.distance(160, 100) < 20:
        print("Win")


def up_and_check():
    up()
    check_goal()


def right_and_check():
    right()
    check_goal()


def task_3():
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(160, 100)
    turtle.dot(20, "red")
    turtle.goto(0, 0)
    turtle.listen()
    turtle.onkey(up_and_check, "Up")
    turtle.onkey(right_and_check, "Right")
    turtle.done()


# task_1_2()
task_3()
