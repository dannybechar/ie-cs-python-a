# Unit 9.6 - the game skeleton. Build it step by step (see the brief).
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


def move_left():
    turtle.setx(turtle.xcor() - 20)
    check_hit()


def move_right():
    turtle.setx(turtle.xcor() + 20)
    check_hit()


# Step 1: write move_up() and move_down(), and connect them to the arrows
# Step 2: write place_target(x, y) for a click on the screen
# Step 3: write tick() - a 30-second timer that ends with Game over
# Step 4: the rover must not move after the game is over


turtle.shape("turtle")
turtle.penup()
draw_target()
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.done()
