# Exercise 10 - Welcome Sign
# Goal: make a sign - a thick dark-red frame on a light yellow background, with a word written inside it.
# What we practice:
#   - bgcolor() sets the background, pensize() + pencolor() set the frame
#   - write(text, align, font) puts TEXT on the screen, in the current pen color
#   - align="center" centers the text on the turtle's position - no need to guess the left edge
#   - font=("Arial", 32, "bold") is (font name, size, style)
import turtle

turtle.bgcolor("lightyellow")
turtle.pensize(8)
turtle.pencolor("darkred")
turtle.penup()
turtle.goto(-150, -50)
turtle.pendown()
turtle.forward(300)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.penup()
turtle.goto(0, -25)
turtle.write("Welcome!", align="center", font=("Arial", 32, "bold"))
turtle.hideturtle()
turtle.done()
