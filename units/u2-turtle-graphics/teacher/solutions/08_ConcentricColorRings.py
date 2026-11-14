# Exercise 08 - Concentric Color Rings
# Goal: draw three circles with the same center - a big thin one, a medium one, a small thick one.
# What we practice:
#   - circle(radius) draws a circle that starts at the turtle and curves to the left
#   - the center of a circle is "radius" above the start point, so to share a center
#     the start y must be -radius: goto(0, -150), goto(0, -100), goto(0, -50)
#   - each ring has its own color and thickness: the smaller the ring, the thicker the pen
import turtle

turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.pencolor("purple")
turtle.pensize(2)
turtle.circle(150)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.pencolor("orange")
turtle.pensize(6)
turtle.circle(100)
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.pencolor("red")
turtle.pensize(12)
turtle.circle(50)
turtle.done()
