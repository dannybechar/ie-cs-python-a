# Exercise 02 - Four Color Frame
# Goal: draw one rectangle whose four sides each have a DIFFERENT color AND a DIFFERENT thickness.
# What we practice:
#   - the pen keeps its color and size until we change them, so we change them before each side
#   - the order of the lines matters: set the pen first, then draw the side with it
#   - the sides get thicker one after another: 2, 6, 10, 14
import turtle

turtle.pensize(2)
turtle.pencolor("red")
turtle.forward(180)
turtle.left(90)
turtle.pensize(6)
turtle.pencolor("blue")
turtle.forward(100)
turtle.left(90)
turtle.pensize(10)
turtle.pencolor("green")
turtle.forward(180)
turtle.left(90)
turtle.pensize(14)
turtle.pencolor("orange")
turtle.forward(100)
turtle.left(90)
turtle.hideturtle()
turtle.done()
