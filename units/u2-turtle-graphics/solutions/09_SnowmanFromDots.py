# Exercise 09 - Snowman From Dots
# Goal: build a snowman using only dots - no lines at all - on a blue background.
# What we practice:
#   - dot(size, color) draws a filled circle of the given diameter at the turtle's position
#   - penup() once at the start - the turtle never draws a line, it only jumps with goto()
#   - big dots first (body, middle, head), small dots last (eyes, nose) so they stay on top
import turtle

turtle.bgcolor("steelblue")
turtle.penup()
turtle.goto(0, -90)
turtle.dot(120, "white")
turtle.goto(0, -20)
turtle.dot(90, "white")
turtle.goto(0, 50)
turtle.dot(60, "white")
turtle.goto(-10, 58)
turtle.dot(8, "black")
turtle.goto(10, 58)
turtle.dot(8, "black")
turtle.goto(0, 46)
turtle.dot(12, "orange")
turtle.hideturtle()
turtle.done()
