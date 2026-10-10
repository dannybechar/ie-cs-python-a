# Unit 8.1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Warm-up: define first, then call
def show_title():
    print("=== GAME ===")


# Task 1: one function, called three times
def welcome():
    print("Welcome")
    print("Let's code")


# Task 2: a menu built from two functions, and main() that sets the order
def show_options():
    print("1. Play")
    print("2. Help")
    print("3. Exit")


def main():
    show_title()
    show_options()


# Task 3: a windmill - the same square four times
def draw_square():
    for i in range(4):
        turtle.forward(80)
        turtle.right(90)


def windmill():
    for i in range(4):
        draw_square()
        turtle.right(90)
    turtle.done()


# show_title()
# welcome()
# welcome()
# welcome()
# main()
windmill()
