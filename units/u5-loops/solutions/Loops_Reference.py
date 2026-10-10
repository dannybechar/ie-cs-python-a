# Unit 5.1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: the fixed indentation - print is inside the loop
def fixed_warmup():
    for i in range(4):
        value = i * 2
        print(value)


# Task 1: one line, six times, with the round number from 1
def fun_lines():
    for i in range(6):
        print(i + 1, "Python is fun")


# Task 2: the sum 1 + 2 + ... + n, shown after every round
def sum_to_n():
    n = int(input("n: "))
    total = 0
    for number in range(1, n + 1):
        total = total + number
        print("number =", number, "total =", total)
    print("Final total:", total)


# Task 3 (challenge): the multiplication table of one number
def times_table():
    number = int(input("Number: "))
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


# fixed_warmup()
# fun_lines()
# sum_to_n()
times_table()
