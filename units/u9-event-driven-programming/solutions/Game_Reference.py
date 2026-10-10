# Unit 9.6 - reference solution for the teacher: the full game.
import turtle
import random

score = 0
time_left = 30
running = True
target_x = 150
target_y = 100


def draw_target():
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.clear()
    turtle.goto(target_x, target_y)
    turtle.dot(20, "red")
    turtle.goto(x, y)


def check_hit():
    global score, target_x, target_y
    if turtle.distance(target_x, target_y) < 20:
        score = score + 1
        print("Score:", score)
        target_x = random.randint(-200, 200)
        target_y = random.randint(-200, 200)
        draw_target()


# Keyboard events: move only while the game is running
def move_left():
    if running:
        turtle.setx(turtle.xcor() - 20)
        check_hit()


def move_right():
    if running:
        turtle.setx(turtle.xcor() + 20)
        check_hit()


def move_up():
    if running:
        turtle.sety(turtle.ycor() + 20)
        check_hit()


def move_down():
    if running:
        turtle.sety(turtle.ycor() - 20)
        check_hit()


# Mouse event: a click on the screen moves the target
def place_target(x, y):
    global target_x, target_y
    target_x = x
    target_y = y
    draw_target()


# Timer event: one second less, then schedule the next tick
def tick():
    global time_left, running
    if time_left > 0:
        time_left = time_left - 1
        print("Time:", time_left)
        turtle.ontimer(tick, 1000)
    else:
        running = False
        print("Game over. Score:", score)


turtle.shape("turtle")
turtle.penup()
draw_target()
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onscreenclick(place_target)
tick()
turtle.done()
