# Exercise 05 - House With Red Roof
# Goal: draw a house in ONE continuous path: blue walls and floor, and a red triangle roof.
# What we practice:
#   - the roof is two sides of 71 steps; turning left(45), left(90), left(45) makes the pointed top
#   - changing pencolor() in the middle of a drawing (blue -> red -> blue)
#   - planning the path: floor, right wall, roof, left wall - and we end where we started
import turtle

turtle.penup()
turtle.goto(-50, -100)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("blue")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.pencolor("red")
turtle.left(45)
turtle.forward(71)
turtle.left(90)
turtle.forward(71)
turtle.pencolor("blue")
turtle.left(45)
turtle.forward(100)
turtle.hideturtle()
turtle.done()
