# Warm-up: the program runs with no error, but nothing is drawn. Why?
import turtle


def draw_square():
    for i in range(4):
        turtle.forward(80)
        turtle.right(90)
    draw_square()


turtle.done()
