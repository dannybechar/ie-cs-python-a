# Unit 7.1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: start at 0, and add 1 to the value it already has
def fixed_warmup():
    negative_count = 0
    for i in range(4):
        number = int(input("Number: "))
        if number < 0:
            negative_count = negative_count + 1
    print("Negative:", negative_count)


# Task 1: how many of 6 grades passed (60 and up)?
def passed_count():
    passed = 0
    for i in range(6):
        grade = int(input("Grade: "))
        if grade >= 60:
            passed = passed + 1
    print("Passed:", passed)


# Task 2: a survey of 8 answers - two counters
def survey():
    yes_count = 0
    no_count = 0
    for i in range(8):
        answer = input("y/n: ")
        if answer == "y":
            yes_count = yes_count + 1
        else:
            no_count = no_count + 1
    print("Yes:", yes_count)
    print("No:", no_count)


# Task 3 (challenge): count the digits in a text (Unit 6 + a counter)
def count_digits():
    text = input("Text: ")
    digits = 0
    for char in text:
        if char.isnumeric():
            digits = digits + 1
    print("Digits:", digits)


# fixed_warmup()
# passed_count()
# survey()
count_digits()
