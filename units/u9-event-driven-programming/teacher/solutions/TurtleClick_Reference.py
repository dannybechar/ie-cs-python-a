# Unit 9.2 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle

current = "blue"
big = False
moves = 0
click_count = 0
size = 1
player = None


# Warm-up: a click handler receives x and y, even if it does not use them
def change_color(x, y):
    turtle.color("red")


def warmup():
    turtle.shape("turtle")
    turtle.onclick(change_color)
    turtle.done()


# Task 1: every click switches the color - the state is kept between clicks
def toggle_color(x, y):
    global current
    if current == "blue":
        current = "orange"
    else:
        current = "blue"
    turtle.color(current)


def task_1():
    turtle.shape("turtle")
    turtle.color(current)
    turtle.onclick(toggle_color)
    turtle.done()


# Task 2: every click switches the size
def toggle_size(x, y):
    global big
    big = not big
    if big:
        turtle.shapesize(3)
    else:
        turtle.shapesize(1)


def task_2():
    turtle.shape("turtle")
    turtle.onclick(toggle_size)
    turtle.done()


# Worked lines for 9.2 (38-44): % for even/odd clicks, and += as recognition
def even_odd(x, y):
    global click_count, size
    if click_count % 2 == 0:
        print("Even click")
    else:
        print("Odd click")
    click_count = click_count + 1
    size += 2                      # recognition only: the same as size = size + 2
    print("size is", size)


def demo_parity():
    turtle.shape("turtle")
    turtle.onclick(even_odd)
    turtle.done()


# Task 3 (challenge, 8 min): the toggle_color program in the exam (object) style.
# Module style -> object style: turtle.onclick -> player.onclick,
# turtle.color -> player.color, turtle.done() -> wn.mainloop()
def toggle_color_obj(x, y):
    global current
    if current == "blue":
        current = "orange"
    else:
        current = "blue"
    player.color(current)


def task_3():
    global player
    wn = turtle.Screen()
    player = turtle.Turtle()
    player.shape("turtle")
    player.color(current)
    player.onclick(toggle_color_obj)
    wn.mainloop()


# Take-home: move 40 per click; after 5 clicks print Arrived
def step_forward(x, y):
    global moves
    if moves < 5:
        turtle.forward(40)
        moves = moves + 1
        if moves == 5:
            print("Arrived")


def task_3_home():
    turtle.shape("turtle")
    turtle.onclick(step_forward)
    turtle.done()


# warmup()
# task_1()
# task_2()
# demo_parity()
# task_3_home()
task_3()
