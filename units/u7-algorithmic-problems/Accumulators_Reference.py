# Unit 7.2 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: the accumulator starts once, before the loop
def fixed_warmup():
    total = 0
    for value in range(1, 6):
        total = total + value
    print("Total:", total)


# Task 1: total and average of 5 expenses
def expenses():
    total = 0
    count = 0
    for i in range(5):
        expense = int(input("Expense: "))
        total = total + expense
        count = count + 1
    print("Total:", total)
    print("Average:", total / count)


# Task 2: the lowest and the highest of 6 grades
def min_max():
    grade = int(input("Grade: "))
    minimum = grade
    maximum = grade
    for i in range(5):
        grade = int(input("Grade: "))
        if grade < minimum:
            minimum = grade
        if grade > maximum:
            maximum = grade
    print("Lowest:", minimum)
    print("Highest:", maximum)


# Task 3: 5 temperatures - average, coldest, hottest, and how many above 25
def temperatures():
    value = int(input("Temperature: "))
    total = value
    minimum = value
    maximum = value
    hot = 0
    if value > 25:
        hot = hot + 1
    for i in range(4):
        value = int(input("Temperature: "))
        total = total + value
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
        if value > 25:
            hot = hot + 1
    print("Average:", total / 5)
    print("Coldest:", minimum)
    print("Hottest:", maximum)
    print("Above 25:", hot)


# fixed_warmup()
# expenses()
# min_max()
temperatures()
