# Environment check for the Grade 7 Python course.
# Open this file in Thonny and press Run.
# If every line says OK and a drawing appears, your computer is ready.
#
# You do not need to understand all of this yet. Most of it you will
# understand by the end of the year. Lines marked "later" use things
# that are taught in later units (or that you will meet on your own).

import sys   # later: a module that knows about Python itself (only used for the version)

print("Python version:", sys.version.split()[0])

# "if" is taught in Unit 4. It checks that Python is version 3.8 or newer.
if sys.version_info >= (3, 8):
    print("OK   Python 3")
else:
    print("PROBLEM   Python is too old. Ask your teacher.")

# If one of the next three lines shows a red error, that module is missing: ask your teacher.
import math
print("OK   math")

import random
print("OK   random")

import turtle
print("OK   turtle")

print("Opening the drawing window...")

# The drawing part uses the same template as the Ministry exam.
wn = turtle.Screen()
pen = turtle.Turtle()

pen.pensize(3)
pen.color("blue")

# A square: forward and left, four times (loops come in Unit 5).
pen.forward(120)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(120)
pen.left(90)

pen.penup()
pen.goto(0, -40)    # goto is taught in Unit 2
# later: write() puts text in the drawing window
pen.write("Ready!", align="left", font=("Arial", 20, "bold"))
pen.hideturtle()

print("All done. Close the drawing window to finish.")
wn.mainloop()
