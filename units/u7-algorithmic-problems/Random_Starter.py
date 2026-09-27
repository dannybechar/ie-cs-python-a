# Warm-up: the program should say You win when the roll is 6.
# Sometimes it prints Roll: 6 and still no You win. Why?
import random

roll = random.randint(1, 6)
print("Roll:", roll)
if random.randint(1, 6) == 6:
    print("You win")
