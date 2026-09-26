# Unit 2 Meeting 1 - reference solutions for the teacher.
# Each task is a function (define -> call, from Unit 1).
# Remove the # from ONE call at the bottom, run, and compare.
import turtle

turtle.Screen()
turtle.shape("turtle")


# Guided build: a 100 by 100 square, ending in the starting direction
def square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)


# Task 1: two stairs going up to the right, 40 by 40 each
def staircase():
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)


# Task 2: the letter L (100 tall, 60 wide)
def letter_l():
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)


# Task 2: the letter U (100 tall, 60 wide)
def letter_u():
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(100)


# Task 2: the letter C (60 wide, 100 tall)
def letter_c():
    turtle.left(180)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)


# Task 2: the letter T (60 wide, 100 tall)
def letter_t():
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(100)


# Task 3: a triangle with three equal sides - the turn is 120, not 60
def triangle():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)


# square()
# staircase()
# letter_l()
# letter_u()
# letter_c()
# letter_t()
triangle()

turtle.done()
