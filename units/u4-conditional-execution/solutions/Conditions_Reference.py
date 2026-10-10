# Unit 4.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Task 1a: compound condition - move only with enough battery AND no obstacle
def rover_move():
    battery = int(input("Battery: "))
    obstacle = input("Obstacle? yes/no: ")
    if battery >= 20 and obstacle == "no":
        print("Move forward")
    else:
        print("Stop")


# Task 1b: the same decision with a nested if
def rover_move_nested():
    battery = int(input("Battery: "))
    obstacle = input("Obstacle? yes/no: ")
    if battery >= 20:
        if obstacle == "no":
            print("Move forward")
        else:
            print("Stop")
    else:
        print("Stop")


# Task 2: input filter + nested choice + Turtle
def draw_shape():
    shape = input("square or triangle: ")
    size = int(input("Size: "))
    if size >= 20 and size <= 200:
        turtle.shape("turtle")
        if shape == "square":
            turtle.pencolor("blue")
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
        else:
            turtle.pencolor("green")
            turtle.forward(size)
            turtle.right(120)
            turtle.forward(size)
            turtle.right(120)
            turtle.forward(size)
            turtle.right(120)
        turtle.done()
    else:
        print("Invalid size")


# Checkpoint A: ticket price - filter, then a compound condition inside
def ticket_price():
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age")
    else:
        if age < 12 or age >= 65:
            print("Price: 20")
        else:
            print("Price: 40")


# rover_move()
# rover_move_nested()
# draw_shape()
ticket_price()
