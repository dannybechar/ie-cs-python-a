# Unit 3 Meeting 1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Task 1: mission card - text input, friendly output, several values in one print
def mission_card():
    name = input("What is your name? ")
    rover = input("What is your rover's name? ")
    print("Commander:", name)
    print("Rover:", rover)
    print("Mission card:", name, "and", rover)


# Task 2: types detective - choose the right type for each input
def types_detective():
    age = int(input("Age: "))
    height = float(input("Height in meters: "))
    city = input("City: ")
    siblings = int(input("Number of siblings: "))
    print("Age:", age, type(age))
    print("Height:", height, type(height))
    print("City:", city, type(city))
    print("Siblings:", siblings, type(siblings))


# Task 3: a variable drives the turtle
def turtle_square():
    side = int(input("Side length: "))
    turtle.shape("turtle")
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.done()


# mission_card()
# types_detective()
turtle_square()
