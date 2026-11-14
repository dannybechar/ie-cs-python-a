# Unit 3 Meeting 1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Warm-up: the rover log (same code as Variables_Starter.py)
def rover_log():
    planet = "Mars"
    distance = 225
    speed = 3.5
    landed = False
    print("Planet:", planet)
    print("Distance:", distance)
    print("Speed:", speed)
    print("Landed:", landed)
    landed = True
    print("Landed:", landed)


# Warm-up extras: multiple assignment, converting a stored variable
def warmup_extras():
    fuel, speed = 80, 3.5
    print(fuel, speed)
    x = 7
    y = float(x)
    print(y, type(y))
    text = str(5)
    print(text, type(text))
    number_int = int(input("Number: "))
    number_float = float(number_int)
    print(number_float)


# Task 1: mission card - text input, friendly output, several values in one print
def mission_card():
    name = input("What is your name? ")
    rover = input("What is your rover's name? ")
    print("Commander:", name)
    print("Rover:", rover)
    print("Mission card:", name, "and", rover)


# Task 2: types detective - choose the right type for each input
# (the siblings question is the extra for fast finishers / the lab sheet)
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


# rover_log()
# warmup_extras()
# mission_card()
# types_detective()
turtle_square()
