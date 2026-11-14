# Unit 8.2 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
# turtle.done() (the exam word: mainloop) is the last line of a Turtle program.
import turtle


# Warm-up: the call belongs outside the function, not inside its body
def draw_square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


# Trace warm-up (ministry 4.3 Ex 1): write the output before running
def ex1():
    num = 34
    a = num + 10
    b = num / 10
    print(b * 10 + a)  # 78.0 - / gives a float


def ex5():
    a = 10
    b = 30
    c = 20
    print((a + b) // c)  # 2 - // drops the fraction


def ex6():
    a = 10
    b = 30
    print((b + a) / (b - a))  # 2.0 - / gives a float even when exact


def trace_task():
    ex1()
    ex5()
    ex6()


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


# Task 3: arithmetic on input, inside the function (ministry 4.3 Ex 4, 5)
def rectangle():
    a = int(input("Side a: "))
    b = int(input("Side b: "))
    print("Area:", a * b)


def pool():
    times = int(input("Visits: "))
    price = int(input("Price: "))
    print("Total:", times * price)


# Optional (take-home): a door at the bottom of the square
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


# trace_task()
# ask_age()
# rectangle()
# pool()
main()
turtle.done()
