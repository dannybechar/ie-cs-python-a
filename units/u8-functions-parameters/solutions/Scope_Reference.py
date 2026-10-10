# Unit 8.4 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle

score = 0
steps = 40
squares_drawn = 0


# Warm-up: global lets the function change the outside variable
def add_point():
    global score
    score = score + 1


def two_points():
    add_point()
    add_point()
    print(score)


# Task 1: a growing spiral - steps is kept between calls
def grow_step():
    global steps
    turtle.forward(steps)
    turtle.right(90)
    steps = steps + 15


def spiral():
    for i in range(6):
        grow_step()
    turtle.done()


# Checkpoint A1: a parameter for the size, a global counter for the drawings
def draw_square(size):
    global squares_drawn
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    squares_drawn = squares_drawn + 1


# Checkpoint A2: a function with two parameters that prints a line
def show_line(symbol, amount):
    print(symbol * amount)


def checkpoint():
    show_line("=", 20)
    draw_square(40)
    draw_square(70)
    draw_square(100)
    print("Squares:", squares_drawn)
    show_line("=", 20)
    turtle.done()


# two_points()
# spiral()
checkpoint()
