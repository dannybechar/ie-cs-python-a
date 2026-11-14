# Unit 8.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
# turtle.done() (the exam word: mainloop) is the last line of a Turtle program.
import turtle


# Warm-up: the call must send a value (an argument) to the parameter
def welcome(city):
    print("Welcome to", city)


# From input to parameters (ministry 4.3 Ex 5): the numbers come from the call
def pool(times, price):
    print("Total:", times * price)


# Order of arguments (ministry "my name"): the first value goes to the first parameter
def show_name(first, last):
    print(first, last)


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


# Task 3 (return-lite): these functions return a value; the print is outside
def add(x, y):
    return x + y


def sub(a, b):
    return a - b


def absolute_value(number):
    if number < 0:
        return -number
    return number


def sign_text(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


def return_task():
    print(absolute_value(-7))
    print(absolute_value(4))
    print(sign_text(5))
    print(sign_text(-3))
    print(sign_text(0))
    total = add(5, 7)
    print(total)
    print(add(add(5, 6), add(1, 2)))
    print(sub(10, 4))
    print(sub(4, 10))


# Optional (take-home): a rectangle - the order of the arguments matters
def draw_rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


def two_rectangles():
    draw_rectangle(140, 70)
    draw_rectangle(70, 140)


# welcome("Haifa")
# pool(3, 25)
# show_name("Dana", "Levi")
# repeat_message("Go", 4)
# three_squares()
# two_rectangles()
return_task()
# turtle.done()   (last line of the Turtle tasks)
