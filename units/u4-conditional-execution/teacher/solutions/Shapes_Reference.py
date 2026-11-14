# Unit 4.3 - reference for Shapes_Starter.py (Task 2): the starter, completed.
# Filter with and, then a rolling condition (if / elif / else) for the shape.
import turtle


def draw_shape():
    shape = input("square or triangle: ")
    size = int(input("Size: "))
    if size >= 20 and size <= 200:
        turtle.shape("turtle")
        if shape == "square":
            turtle.pencolor("blue")
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
        elif shape == "triangle":
            turtle.pencolor("green")
            turtle.forward(size)
            turtle.right(120)
            turtle.forward(size)
            turtle.right(120)
            turtle.forward(size)
            turtle.right(120)
        else:
            print("Unknown shape")
        turtle.done()
    else:
        print("Invalid size")


draw_shape()
