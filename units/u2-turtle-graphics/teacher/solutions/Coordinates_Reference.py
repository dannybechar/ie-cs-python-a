# Unit 2 Addendum A - reference solutions: coordinates, goto, setx, sety (teacher).
# Same structure as the starter: one function per task. Run ONE task at a time: remove the # from one call at the bottom.
# Window coordinates: (0, 0) is the middle, x grows to the right, y grows upward. 1 unit = 1 step.
import turtle

turtle.Screen()
turtle.shape("turtle")


# Warm-up: the path is a rectangle 200 wide and 100 tall; the turtle stops at (0, 0), still facing right.
# goto draws a line when the pen is down (moving to a point draws a line).
def warm_up():
    turtle.goto(100, 50)
    turtle.goto(-100, 50)
    turtle.goto(-100, -50)
    turtle.goto(0, 0)


# Task A: pen up to jump, pen down to draw.
def task_a():
    turtle.penup()
    turtle.goto(-150, 80)
    turtle.pendown()
    turtle.goto(150, 80)


# Task B: setx changes only x, sety changes only y. Four corners of the square.
def task_b():
    turtle.setx(100)
    turtle.sety(100)
    turtle.setx(0)
    turtle.sety(0)


# Task C: square of side 80 in quadrant 2 (x < 0, y > 0): corner (-120, 40), then forward/left four times.
def task_c():
    turtle.penup()
    turtle.goto(-120, 40)
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)


# Task D: four squares of side 60 (each is 4 x forward/left), start points next to the crossing of the axes:
# quadrant 1 (10, 10), quadrant 2 (-70, 10), quadrant 3 (-70, -70), quadrant 4 (10, -70).
def task_d():
    turtle.penup()
    turtle.goto(10, 10)
    turtle.pendown()
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-70, 10)
    turtle.pendown()
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-70, -70)
    turtle.pendown()
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.penup()
    turtle.goto(10, -70)
    turtle.pendown()
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)


# warm_up()
# task_a()
# task_b()
# task_c()
task_d()

turtle.done()
