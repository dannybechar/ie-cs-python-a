# Unit 2 Addendum B - the same program in the exam notation (starter)
# In the national exam the window and the turtle each get a NAME, and every command is written after the turtle name:
#   wn = turtle.Screen()    the window
#   pen = turtle.Turtle()   the turtle
#   pen.forward(100)        a command of the turtle "pen"
#   wn.mainloop()           keeps the window open (like turtle.done())
# For now wn and pen are just labels; we learn variables properly in Unit 3.
# Run ONE part at a time: remove the # from one call at the bottom (close the window before the next run).
import turtle


# Part 1 - class style (what we know). Run it and look at the picture.
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


# Part 2 - translate Part 1 into the exam notation. The same picture is expected.
def part_2_exam_style():
    pass


# Part 3 - translate FROM the exam notation: rewrite in class style. Say first what it draws.
#   wn = turtle.Screen()
#   pen = turtle.Turtle()
#   pen.color("red")
#   pen.fd(80)
#   pen.rt(120)
#   pen.fd(80)
#   pen.rt(120)
#   pen.fd(80)
#   wn.mainloop()
def part_3_to_class_style():
    pass


# part_1_class_style()
# part_2_exam_style()
# part_3_to_class_style()
