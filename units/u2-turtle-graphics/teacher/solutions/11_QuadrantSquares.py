# Exercise 11 - Squares in the Four Quadrants (solution) - needs the coordinates block (Addendum A)
# Goal: on the axes, draw four squares of side 50, one in each quadrant, each in a different color.
# What we practice:
#   - the plane has four quadrants: (1) x>0,y>0  (2) x<0,y>0  (3) x<0,y<0  (4) x>0,y<0
#   - penup() + goto(x, y) + pendown() = move to a start point without drawing
# Your task:
#   Quadrant 1 red, start (20, 20) ; quadrant 2 green, start (-70, 20) ; quadrant 3 blue, start (-70, -70) ; quadrant 4 orange, start (20, -70).
#   Before running, mark the four start points on paper. Each square: forward(50), left(90), four times.
# Challenge (optional): a house with a red triangular roof, a door and two windows, the walls in quadrant 1.
import turtle

turtle.Screen()
turtle.shape("turtle")

turtle.pencolor("red")
turtle.penup()
turtle.goto(20, 20)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

turtle.pencolor("green")
turtle.penup()
turtle.goto(-70, 20)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

turtle.pencolor("blue")
turtle.penup()
turtle.goto(-70, -70)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

turtle.pencolor("orange")
turtle.penup()
turtle.goto(20, -70)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

turtle.hideturtle()
turtle.done()
