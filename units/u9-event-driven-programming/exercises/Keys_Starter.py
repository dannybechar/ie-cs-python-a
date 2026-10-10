# Warm-up: press the Up arrow. Why does nothing happen?
import turtle


def up():
    turtle.sety(turtle.ycor() + 20)


turtle.shape("turtle")
turtle.onkey(up, "Up")
turtle.done()
