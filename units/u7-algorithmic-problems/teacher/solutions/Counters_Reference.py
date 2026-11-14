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


# Task 1: how many of 6 grades passed (55 and up)?
def passed_count():
    passed = 0
    for i in range(6):
        grade = int(input("Grade: "))
        if grade >= 55:
            passed = passed + 1
    print("Passed:", passed)


# Task 2: a survey of 8 answers - three counters (yes, no, not valid)
def survey():
    yes_count = 0
    no_count = 0
    invalid_count = 0
    for i in range(8):
        answer = input("y/n: ")
        if answer == "y":
            yes_count = yes_count + 1
        elif answer == "n":
            no_count = no_count + 1
        else:
            print("not valid")
            invalid_count = invalid_count + 1
    print("Yes:", yes_count)
    print("No:", no_count)
    print("Not valid:", invalid_count)
    print("Check, should be 8:", yes_count + no_count + invalid_count)


# Guided demo: three-way counter with elif (coins 1, 5, 10)
def coins():
    ones = 0
    fives = 0
    tens = 0
    for i in range(6):
        coin = int(input("Coin: "))
        if coin == 1:
            ones = ones + 1
        elif coin == 5:
            fives = fives + 1
        elif coin == 10:
            tens = tens + 1
        else:
            print("value not accepted")
    print(ones, fives, tens)


# Shorthand: += is the same as x = x + 1 (recognition only)
def shorthand():
    count = 0
    for number in range(1, 21):
        if number % 3 == 0:
            count += 1
    print("Count:", count)


# Task 3 (challenge): count the digits in a text (Unit 6 + a counter)
def count_digits():
    text = input("Text: ")
    digits = 0
    for char in text:
        if char.isnumeric():
            digits = digits + 1
    print("Digits:", digits)


# fixed_warmup()
# coins()
# shorthand()
# passed_count()
# survey()
count_digits()
