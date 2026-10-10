# Unit 9.1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle

clicks = 0


# Warm-up: give onclick the function's name - no parentheses
def say_hello(x, y):
    print("Hello")


def warmup():
    turtle.shape("turtle")
    turtle.onclick(say_hello)
    turtle.done()


# Task 1: print where the click happened
def report_click(x, y):
    print("Clicked", x, y)


def task_1():
    turtle.shape("turtle")
    turtle.onclick(report_click)
    turtle.done()


# Task 2: every click on the rover turns it and moves it
def turn_and_move(x, y):
    turtle.right(90)
    turtle.forward(50)


def task_2():
    turtle.shape("turtle")
    turtle.onclick(turn_and_move)
    turtle.done()


# Task 3 (challenge): count the clicks - the counter lives between events
def count_click(x, y):
    global clicks
    clicks = clicks + 1
    print("Clicks:", clicks)


def task_3():
    turtle.shape("turtle")
    turtle.onclick(count_click)
    turtle.done()


# warmup()
# task_1()
# task_2()
task_3()
