# Warm-up: the rover should jump to the click without drawing a line. Fix it.
import turtle


def move_to(x, y):
    turtle.goto(x, y)


turtle.shape("turtle")
turtle.onscreenclick(move_to)
turtle.done()
