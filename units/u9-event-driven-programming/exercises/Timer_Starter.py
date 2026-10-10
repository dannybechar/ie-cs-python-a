# Warm-up: the rover should move 5 steps every 50 milliseconds.
# The program crashes with RecursionError. Why?
import turtle


def animate():
    turtle.forward(5)
    turtle.ontimer(animate(), 50)


turtle.shape("turtle")
animate()
turtle.done()
