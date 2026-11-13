# Unit 9.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle

stamps = 0
size = 2


# Warm-up: lift the pen before moving, put it down after
def move_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def warmup():
    turtle.shape("turtle")
    turtle.onscreenclick(move_to)
    turtle.done()


# Task 1: a stamp where the user clicks - a colour for each quarter of the window
# (the ministry's 20.3 task 3: x and y signs with and / elif)
def mark(x, y):
    turtle.penup()
    if x >= 0 and y >= 0:
        turtle.color("red")
    elif x >= 0 and y < 0:
        turtle.color("blue")
    elif x < 0 and y >= 0:
        turtle.color("green")
    else:
        turtle.color("yellow")
    turtle.goto(x, y)
    turtle.stamp()


def task_1():
    turtle.shape("turtle")
    turtle.onscreenclick(mark)
    turtle.done()


# Task 2: only 5 stamps, then Finished
def mark_five(x, y):
    global stamps
    if stamps < 5:
        turtle.penup()
        turtle.goto(x, y)
        turtle.stamp()
        stamps = stamps + 1
    else:
        print("Finished")


def task_2():
    turtle.shape("circle")
    turtle.onscreenclick(mark_five)
    turtle.done()


# Task 3 (challenge): a click on the rover grows it, a click elsewhere shrinks it.
# A click on the rover is also a click on the screen, so the two listeners
# are split between mouse buttons: btn=1 is the left button, btn=3 the right one
# (on a Mac the right button is btn=2). Size never goes below 1.
def grow(x, y):
    global size
    size = size + 1
    turtle.shapesize(size)


def shrink(x, y):
    global size
    if size > 1:
        size = size - 1
        turtle.shapesize(size)


def task_3():
    turtle.shape("turtle")
    turtle.shapesize(size)
    turtle.onclick(grow, btn=1)
    turtle.onscreenclick(shrink, btn=3)
    turtle.done()


# Take-home: connect the dots - here the line is the goal
def connect(x, y):
    turtle.goto(x, y)
    turtle.dot(10, "orange")


def task_3_home():
    turtle.shape("turtle")
    turtle.onscreenclick(connect)
    turtle.done()


# warmup()
# task_1()
# task_2()
# task_3_home()
task_3()
