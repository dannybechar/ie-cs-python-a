# Unit 2 Addendum A - where is the turtle? coordinates, goto, setx, sety (starter)
# Needs the addendum lesson (addendum-lesson-notes.md): the window has an x axis and a y axis, the turtle starts at (0, 0).
# One function per task, as in Unit 2.2. Run ONE task at a time: remove the # from one call at the bottom.
# Rule: no loops, no variables, no input.
import turtle

turtle.Screen()
turtle.shape("turtle")


# Warm-up (read, predict, run): where does the turtle stop? Write each point on paper first.
def warm_up():
    turtle.goto(100, 50)
    turtle.goto(-100, 50)
    turtle.goto(-100, -50)
    turtle.goto(0, 0)


# Task A: jump without drawing.
# Move the turtle to (-150, 80) WITHOUT a line, then draw a line to (150, 80).
def task_a():
    pass


# Task B: setx and sety change ONE coordinate.
# Start at (0, 0). Use only setx and sety (no goto) to draw a 100 x 100 square: corners (100, 0), (100, 100), (0, 100), (0, 0).
def task_b():
    pass


# Task C: a square in quadrant 2 (upper left): side 80, one corner at (-120, 40). Jump there first, no line on the way.
def task_c():
    pass


# Task D: four squares of side 60, one in EACH quadrant, next to the crossing of the axes.
# Hint: draw the first square, then penup, goto the next start point, pendown.
def task_d():
    pass


# warm_up()
# task_a()
# task_b()
# task_c()
# task_d()

turtle.done()
