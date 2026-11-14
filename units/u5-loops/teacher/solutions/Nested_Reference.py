# Unit 5.4 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Task 1a: 2 rows of 3 stars - print() ends a row after the inner loop
def stars_fixed():
    for row in range(2):
        for column in range(3):
            print("*", end="")
        print()


# Task 1b: a rectangle of 4 rows and 6 # signs, then a triangle
def patterns():
    for row in range(4):
        for column in range(6):
            print("#", end="")
        print()
    for row in range(1, 6):
        for column in range(row):
            print("*", end="")
        print()


# Optional (take-home): a flower of 8 squares - inner loop = square, outer loop = turn
def flower():
    turtle.shape("turtle")
    for square in range(8):
        for side in range(4):
            turtle.forward(70)
            turtle.right(90)
        turtle.right(45)
    turtle.done()


# Task 2: Super Python - ten scores, an elif chain inside a for loop
# 90 and up Super, 78-89 Good, 55-77 Pass, below 55 Fail
def super_python():
    super_count = 0
    super_total = 0
    fail_count = 0
    for student in range(10):
        score = int(input("Score: "))
        if score >= 90:
            print("Super")
            super_count = super_count + 1
            super_total = super_total + score
        elif score >= 78:
            print("Good")
        elif score >= 55:
            print("Pass")
        else:
            print("Fail")
            fail_count = fail_count + 1
    print("Super:", super_count)
    print("Fail:", fail_count)
    if super_count > 0:
        print("Average of the Super scores:", super_total / super_count)


# Checkpoint A1 (bounded loop): multiplication table 1 to 5
def times_grid():
    for row in range(1, 6):
        for column in range(1, 6):
            print(row * column, end=" ")
        print()


# Checkpoint A2 (conditional loop): count scores until -1
def count_scores():
    count = 0
    passed = 0
    score = int(input("Score, -1 to stop: "))
    while score != -1:
        count = count + 1
        if score >= 60:
            passed = passed + 1
        score = int(input("Score, -1 to stop: "))
    print("Scores:", count)
    print("Passed:", passed)


# stars_fixed()
# patterns()
# super_python()
# flower()
# times_grid()
count_scores()
