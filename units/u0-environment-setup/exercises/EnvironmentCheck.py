# Environment check for the Grade 7 Python course.
# Open this file in Thonny and press Run.
# If every line says OK and a drawing appears, your computer is ready.

import sys

print("Python version:", sys.version.split()[0])

if sys.version_info >= (3, 8):
    print("OK   Python 3")
else:
    print("PROBLEM   Python is too old. Ask your teacher.")

import math
print("OK   math")

import random
print("OK   random")

try:
    import turtle
    print("OK   turtle")
except ImportError:
    print("PROBLEM   turtle is missing. Ask your teacher.")
    sys.exit()

print("Opening the drawing window...")

t = turtle.Turtle()
t.pensize(3)
t.color("blue")
for side in range(4):
    t.forward(120)
    t.left(90)

t.penup()
t.goto(0, -40)
t.write("Ready!", align="left", font=("Arial", 20, "bold"))
t.hideturtle()

print("All done. Close the drawing window to finish.")
turtle.done()
