# Unit 2 Meeting 2 - reference solutions for the teacher.
# Same structure the students use: one function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom, run, and compare.
import turtle

turtle.Screen()
turtle.shape("turtle")


# Task A: a dashed road with 3 dashes
def dashed_road():
    turtle.forward(30)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.forward(30)


# Task B: a square with a thick pen and a different color on each side
def color_square():
    turtle.pensize(5)
    turtle.pencolor("red")
    turtle.forward(100)
    turtle.left(90)
    turtle.pencolor("blue")
    turtle.forward(100)
    turtle.left(90)
    turtle.pencolor("green")
    turtle.forward(100)
    turtle.left(90)
    turtle.pencolor("orange")
    turtle.forward(100)
    turtle.left(90)
    turtle.hideturtle()


# Task C: stepping stones - three stamps with no lines between them
def stepping_stones():
    turtle.shape("circle")
    turtle.penup()
    turtle.stamp()
    turtle.forward(50)
    turtle.stamp()
    turtle.forward(50)
    turtle.stamp()
    turtle.hideturtle()


# Task D: update a value, then read it back in the Shell
def read_the_pen():
    print(turtle.pensize())
    turtle.pensize(8)
    print(turtle.pensize())
    print(turtle.pencolor())


# dashed_road()
# color_square()
# stepping_stones()
read_the_pen()

turtle.done()
