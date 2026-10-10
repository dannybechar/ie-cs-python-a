# Unit 7.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import random
import turtle


# Warm-up: draw once, save it, then check the saved value
def fixed_warmup():
    roll = random.randint(1, 6)
    print("Roll:", roll)
    if roll == 6:
        print("You win")


# Task 1: a random walk with Turtle - a counter and an accumulator
def random_walk():
    long_steps = 0
    distance = 0
    for i in range(20):
        turtle.right(random.randint(0, 360))
        step = random.randint(10, 40)
        turtle.forward(step)
        distance = distance + step
        if step > 30:
            long_steps = long_steps + 1
    print("Long steps:", long_steps)
    print("Distance:", distance)
    turtle.done()


# Checkpoint A1: 30 dice rolls - how many sixes, the total and the average
def dice_stats():
    sixes = 0
    total = 0
    for i in range(30):
        roll = random.randint(1, 6)
        total = total + roll
        if roll == 6:
            sixes = sixes + 1
    print("Sixes:", sixes)
    print("Total:", total)
    print("Average:", total / 30)


# Checkpoint A2: guess the secret number, count the attempts
def guess_game():
    secret = random.randint(1, 20)
    attempts = 1
    guess = int(input("Guess 1-20: "))
    while guess != secret:
        if guess < secret:
            print("Too low")
        else:
            print("Too high")
        guess = int(input("Guess 1-20: "))
        attempts = attempts + 1
    print("Correct in", attempts, "attempts")


# fixed_warmup()
# random_walk()
# dice_stats()
guess_game()
