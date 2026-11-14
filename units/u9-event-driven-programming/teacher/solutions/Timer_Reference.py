# Unit 9.5 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle

speed = 5
dx = 5
running = True


# Warm-up: ontimer gets the function's name and calls it later
def animate():
    turtle.forward(speed)
    turtle.ontimer(animate, 50)


def warmup():
    turtle.shape("turtle")
    animate()
    turtle.done()


# Task 1: bounce between -200 and 200 by flipping the sign of dx
def bounce():
    global dx
    turtle.setx(turtle.xcor() + dx)
    if turtle.xcor() > 200 or turtle.xcor() < -200:
        dx = -dx
    if running:
        turtle.ontimer(bounce, 30)


# Task 2: space stops the animation, s starts it again (only if stopped)
def stop():
    global running
    running = False


def start():
    global running
    if not running:
        running = True
        bounce()


def task_1_2():
    turtle.shape("turtle")
    turtle.penup()
    turtle.listen()
    turtle.onkey(stop, "space")
    turtle.onkey(start, "s")
    bounce()
    turtle.done()


# warmup()
task_1_2()
