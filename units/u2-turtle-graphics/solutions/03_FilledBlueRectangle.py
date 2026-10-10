# Exercise 03 - Filled Blue Rectangle
# Goal: draw a rectangle with a dark blue border that is filled with light blue, in the lower-right of the screen.
# What we practice:
#   - fillcolor() chooses the inside color, pencolor() chooses the border color
#   - begin_fill() ... end_fill() - everything drawn between them gets filled
#   - the turtle only fills a shape that we finished drawing
import turtle

turtle.penup()
turtle.goto(60, -150)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("navy")
turtle.fillcolor("lightblue")
turtle.begin_fill()
turtle.forward(180)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(180)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
