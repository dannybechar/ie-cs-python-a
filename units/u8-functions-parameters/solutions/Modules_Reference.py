# Unit 8.2 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Warm-up: the call belongs outside the function, not inside its body
def draw_square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


# Task 1: a function with no parameters can still read input
def ask_age():
    age = int(input("Age: "))
    if age >= 18:
        print("Adult")
    else:
        print("Minor")


# Task 2: a house from two drawing functions, in the order main() sets
def draw_roof():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)


# Task 3 (challenge): a door at the bottom of the square
def draw_door():
    turtle.penup()
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(60)
    turtle.pendown()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)


def main():
    draw_square()
    draw_roof()
    draw_door()
    turtle.done()


# ask_age()
main()
