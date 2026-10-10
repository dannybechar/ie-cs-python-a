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


# Challenge: a five-pointed star
def star():
    turtle.shape("turtle")
    for point in range(5):
        turtle.forward(150)
        turtle.right(144)
    turtle.done()


# sequences()
# polygon()
# spiral()
# countdown()
star()
