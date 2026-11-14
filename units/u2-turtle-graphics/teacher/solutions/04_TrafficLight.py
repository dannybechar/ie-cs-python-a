# Exercise 04 - Traffic Light
# Goal: draw a traffic light - a thick black body with a red, yellow and green light.
# What we practice:
#   - a VERY thick line is a rectangle: pensize(80) + forward(200) draws a black bar 80 wide
#   - left(90) turns the turtle so the bar goes UP instead of right
#   - dot(size, color) stamps a filled circle - after penup() we can place dots anywhere with goto()
import turtle

turtle.pensize(80)
turtle.pencolor("black")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.left(90)
turtle.forward(200)
turtle.penup()
turtle.goto(0, 80)
turtle.dot(45, "red")
turtle.goto(0, 0)
turtle.dot(45, "yellow")
turtle.goto(0, -80)
turtle.dot(45, "green")
turtle.hideturtle()
turtle.done()
