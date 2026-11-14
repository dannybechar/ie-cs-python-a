# Exercise 06 - Three Color Ribbons
# Goal: draw three thick horizontal ribbons, one above the other, each in a different color.
# What we practice:
#   - one thick line (pensize(40)) looks like a ribbon - no rectangle code needed
#   - for every ribbon: lift the pen, goto() the start, put the pen down, choose a color, draw
#   - the y values 60, 0, -60 place the ribbons evenly on the screen
import turtle

turtle.pensize(40)
turtle.penup()
turtle.goto(-100, 60)
turtle.pendown()
turtle.pencolor("crimson")
turtle.forward(200)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.pencolor("gold")
turtle.forward(200)
turtle.penup()
turtle.goto(-100, -60)
turtle.pendown()
turtle.pencolor("seagreen")
turtle.forward(200)
turtle.hideturtle()
turtle.done()
