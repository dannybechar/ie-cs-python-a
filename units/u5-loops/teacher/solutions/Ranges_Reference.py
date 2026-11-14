# Unit 5.2 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Task 1: sequences with a step
def sequences():
    for number in range(2, 12, 2):
        print(number)
    for number in range(20, 0, -5):
        print(number)


# Guided block A: end=" " keeps the next print on the same line
# (end is an attribute of print; the default is a new line)
def numbers_in_a_line():
    for number in range(1, 8):
        print(number, end=" ")
    print()
    for number in range(2, 11, 2):
        print(number, end=",")
    print()


# Guided block B: for + if with %, or range with a step - same output?
def multiples_of_3():
    for number in range(17):
        if number % 3 == 0:
            print(number, end=" ")
    print()
    for number in range(0, 17, 3):
        print(number, end=" ")
    print()


# Guided block B, variant: 7-boom from 1 to 50
# (number // 10 == 7 is "the tens digit is 7"; number / 10 would be wrong)
def seven_boom():
    for number in range(1, 51):
        if number % 7 == 0 or number % 10 == 7 or number // 10 == 7:
            print("Boom", end=" ")
        else:
            print(number, end=" ")
    print()


# Task 2: any regular polygon - the turns add up to 360
def polygon():
    sides = int(input("Sides: "))
    angle = 360 / sides
    turtle.shape("turtle")
    for side in range(sides):
        turtle.forward(80)
        turtle.right(angle)
    turtle.done()


# Task 3: square spiral - the loop variable is the distance
def spiral():
    turtle.shape("turtle")
    for distance in range(20, 200, 20):
        turtle.forward(distance)
        turtle.right(90)
    turtle.done()


# Task 4: countdown from the user's number
def countdown():
    start = int(input("Start: "))
    for seconds in range(start, 0, -1):
        print(seconds)
    print("Launch!")


# Task 4, one-line version: the same count, with commas
def countdown_line():
    start = int(input("Start: "))
    for seconds in range(start, 0, -1):
        print(seconds, end=",")
    print("Launch!")


# Challenge: a five-pointed star
def star():
    turtle.shape("turtle")
    for point in range(5):
        turtle.forward(150)
        turtle.right(144)
    turtle.done()


# sequences()
# numbers_in_a_line()
# multiples_of_3()
# seven_boom()
# polygon()
# spiral()
# countdown()
# countdown_line()
star()
