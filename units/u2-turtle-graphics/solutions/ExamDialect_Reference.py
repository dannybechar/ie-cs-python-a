# Unit 2 Addendum B - reference solutions: the exam notation (teacher).
# Run ONE part at a time: remove the # from one call at the bottom (each part opens its own window, close it before the next).
# Short names read in the exam: fd = forward, lt = left, rt = right, bk/back = backward, pu/up = penup, pd/down = pendown.
import turtle


# Part 1 - class style: a 100 x 60 rectangle, blue pen.
def part_1_class_style():
    turtle.Screen()
    turtle.shape("turtle")
    turtle.pensize(3)
    turtle.pencolor("blue")
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.done()


# Part 2 - the same rectangle in the exam notation.
def part_2_exam_style():
    wn = turtle.Screen()
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.pensize(3)
    pen.pencolor("blue")
    pen.forward(100)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    wn.mainloop()


# Part 3 - the exam-style code draws an equilateral triangle, side 80, red line and red turtle.
# Class style: every line becomes turtle.<command>(...); fd = forward, rt = right; wn.mainloop() becomes turtle.done().
def part_3_to_class_style():
    turtle.Screen()
    turtle.color("red")
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(80)
    turtle.done()


# part_1_class_style()
part_2_exam_style()
# part_3_to_class_style()
