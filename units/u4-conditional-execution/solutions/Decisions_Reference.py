# Unit 4 Meeting 2 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
# ScoreBug_Reference.py is the fixed ScoreBug_Starter.py on its own.


# Guided demo: even or odd; "odd" also written with not
def even_odd():
    number = int(input("Number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
    print(not (number % 2 == 0))


# Guided demo: the two digits of a two-digit number
def two_digits():
    number = int(input("Two-digit number: "))
    print("Tens:", number // 10)
    print("Ones:", number % 10)


# Task 1: pass or try again - 60 is a passing score
def grade_check():
    score = int(input("Score: "))
    if score >= 60:
        print("Passed")
    else:
        print("Try again")


# Task 2: the fixed bug program (same code as ScoreBug_Reference.py)
def perfect_check():
    score = int(input("Score: "))
    if score == 100:
        print("Perfect")
    else:
        print("Not perfect")


# Task 3: input filter - a battery level must be 0 to 100
def battery_filter():
    battery = int(input("Battery: "))
    if battery >= 0 and battery <= 100:
        print("Valid battery")
    else:
        print("Invalid battery")


# Task 4: the larger of two numbers
def max_of_two():
    first = int(input("First: "))
    second = int(input("Second: "))
    if first >= second:
        print("Largest:", first)
    else:
        print("Largest:", second)


# Task 5 (challenge): two-digit number - even: sum of the digits, else product
def digits_check():
    number = int(input("Two-digit number: "))
    tens = number // 10
    ones = number % 10
    if number % 2 == 0:
        print("Sum:", tens + ones)
    else:
        print("Product:", tens * ones)


# Take-home (extra practice): 10% discount from 100 and up
def discount():
    price = float(input("Price: "))
    if price >= 100:
        final_price = price * 0.9
    else:
        final_price = price
    print("Final price:", final_price)


# even_odd()
# two_digits()
# grade_check()
# perfect_check()
# battery_filter()
# max_of_two()
# discount()
digits_check()
