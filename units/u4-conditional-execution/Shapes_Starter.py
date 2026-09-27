# Task 2: the rover draws the shape the user chooses
import turtle


def draw_shape():
    shape = input("square or triangle: ")
    size = int(input("Size: "))
    # TODO 1: only draw if size is from 20 to 200, otherwise print "Invalid size"
    # TODO 2: "square" -> the blue square, anything else -> the green triangle
    turtle.shape("turtle")

    turtle.pencolor("blue")
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

    turtle.pencolor("green")
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)

    turtle.done()


draw_shape()
