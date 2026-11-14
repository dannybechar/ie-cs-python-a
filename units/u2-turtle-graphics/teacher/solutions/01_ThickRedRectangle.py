# Exercise 01 - Thick Red Rectangle
# Goal: draw a 160 x 80 rectangle with a thick red pen, in the upper-left part of the screen.
# What we practice:
#   - pensize() and pencolor() change how the line looks
#   - penup() + goto() + pendown() move the turtle WITHOUT drawing, so we choose where the drawing starts
#   - a rectangle = forward(long), left(90), forward(short), left(90), and again
import turtle

turtle.Screen()
turtle.shape("turtle")
turtle.pensize(8)
turtle.pencolor("red")
turtle.penup()
turtle.goto(-200, 120)
turtle.pendown()
turtle.forward(160)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(160)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.hideturtle()
turtle.done()
