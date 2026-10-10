# Unit 9.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle

stamps = 0


# Warm-up: lift the pen before moving, put it down after
def move_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def warmup():
    turtle.shape("turtle")
    turtle.onscreenclick(move_to)
    turtle.done()


# Task 1: a stamp where the user clicks - blue above the middle, red below
def mark(x, y):
    turtle.penup()
    if y > 0:
        turtle.color("blue")
    else:
        turtle.color("red")
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


# Task 3 (challenge): connect the dots - here the line is the goal
def connect(x, y):
    turtle.goto(x, y)
    turtle.dot(10, "orange")


def task_3():
    turtle.shape("turtle")
    turtle.onscreenclick(connect)
    turtle.done()


# warmup()
# task_1()
# task_2()
task_3()
