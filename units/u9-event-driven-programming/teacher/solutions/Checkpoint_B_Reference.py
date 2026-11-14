# Unit 9.6 - Checkpoint B, question 3: reference answer for the teacher.
# Exam style (object style), after the ministry exercise "Adi's squares" (m19 slide 22).
# Every click draws a square at the click: red and blue alternately,
# and each square's side is 2 longer than the one before.
# The blanks in the student sheet are: click_num | "red" | "blue" | click_num + 1 | size + 2
# GUI program: run it, then click the window several times.
import turtle


def do_it(x, y):
    global click_num
    global size
    player.penup()
    player.goto(x, y)
    player.shapesize(size)
    if click_num % 2 == 0:
        player.color("red")
    else:
        player.color("blue")
    player.stamp()
    click_num = click_num + 1
    size = size + 2


tw = turtle.Screen()
click_num = 0
size = 2
player = turtle.Turtle()
player.shape("square")
tw.onclick(do_it)
turtle.mainloop()
