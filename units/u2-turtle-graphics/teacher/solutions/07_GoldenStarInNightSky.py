# Exercise 07 - Golden Star In The Night Sky
# Goal: paint the background dark blue and draw a big golden star in it.
# What we practice:
#   - bgcolor() colors the whole screen, not just the line
#   - a 5-point star: forward(160) and right(144), five times - 144 degrees is the "star" turn
#   - begin_fill() / end_fill() fills even a shape whose lines cross each other
import turtle

turtle.bgcolor("midnightblue")
turtle.pencolor("gold")
turtle.fillcolor("gold")
turtle.penup()
turtle.goto(-80, 50)
turtle.pendown()
turtle.begin_fill()
turtle.forward(160)
turtle.right(144)
turtle.forward(160)
turtle.right(144)
turtle.forward(160)
turtle.right(144)
turtle.forward(160)
turtle.right(144)
turtle.forward(160)
turtle.right(144)
turtle.end_fill()
turtle.done()
