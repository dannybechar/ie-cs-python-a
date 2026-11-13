# Unit 4.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
# Shapes_Reference.py is the completed Shapes_Starter.py (Task 2) on its own.
import turtle


# Task 1: compound condition - move only with enough battery AND no obstacle
def rover_move():
    battery = int(input("Battery: "))
    obstacle = input("Obstacle? yes/no: ")
    if battery >= 20 and obstacle == "no":
        print("Move forward")
    else:
        print("Stop")


# Guided demo: the same decision with a nested if (shown by the teacher)
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


# Guided demo: rolling condition - the first True condition wins
def battery_color():
    battery = int(input("Battery: "))
    if battery >= 70:
        print("Green")
    elif battery >= 30:
        print("Yellow")
    else:
        print("Red")


# Task 2: input filter + rolling choice + Turtle
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
        elif shape == "triangle":
            turtle.pencolor("green")
            turtle.forward(size)
            turtle.right(120)
            turtle.forward(size)
            turtle.right(120)
            turtle.forward(size)
            turtle.right(120)
        else:
            print("Unknown shape")
        turtle.done()
    else:
        print("Invalid size")


# Checkpoint A: ticket price - filter, then a compound condition (elif version)
def ticket_price():
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age")
    elif age < 12 or age >= 65:
        print("Price: 20")
    else:
        print("Price: 40")


# Checkpoint A: the same program with one-level nesting (also accepted)
def ticket_price_nested():
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age")
    else:
        if age < 12 or age >= 65:
            print("Price: 20")
        else:
            print("Price: 40")


# Checkpoint B (part 1): the gift chain, for the teacher to check the trace table
def gift_chain():
    amount = int(input("Amount: "))
    if amount < 80:
        print("No gift")
    elif amount < 800:
        if amount <= 500:
            print("Yoga ball")
        elif amount < 650:
            print("Tennis balls")
        else:
            print("Football")
    else:
        print("Running shoes")


# Checkpoint B (part 2): evaluate with a = 10, b = 15, c = 0
def evaluate_expressions():
    a = 10
    b = 15
    c = 0
    print(a % 5 == 0 and b // 5 > c)
    print(a % 2 == c % 2 and b % 3 > a % 3)


# Stretch / take-home: the largest of three numbers, with elif
def max_of_three():
    a = int(input("First: "))
    b = int(input("Second: "))
    c = int(input("Third: "))
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)


# rover_move()
# rover_move_nested()
# battery_color()
# draw_shape()
# ticket_price_nested()
# gift_chain()
# evaluate_expressions()
# max_of_three()
ticket_price()
