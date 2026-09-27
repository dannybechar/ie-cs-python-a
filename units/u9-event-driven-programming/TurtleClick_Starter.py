# Warm-up: click the rover. It should turn red. Why is there an error?
import turtle


def change_color():
    turtle.color("red")


turtle.shape("turtle")
turtle.onclick(change_color)
turtle.done()
