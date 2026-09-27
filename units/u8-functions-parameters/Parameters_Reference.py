# Unit 8.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Warm-up: the call must send a value (an argument) to the parameter
def welcome(city):
    print("Welcome to", city)


# Task 1: two parameters - what to print and how many times
def repeat_message(message, times):
    for i in range(times):
        print(message)


# Task 2: one drawing function, any size
def draw_square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)


def three_squares():
    draw_square(50)
    draw_square(100)
    draw_square(150)
    turtle.done()


# Task 3: a rectangle - the order of the arguments matters
def draw_rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


def two_rectangles():
    draw_rectangle(140, 70)
    draw_rectangle(70, 140)
    turtle.done()


# welcome("Haifa")
# repeat_message("Go", 4)
# three_squares()
two_rectangles()
