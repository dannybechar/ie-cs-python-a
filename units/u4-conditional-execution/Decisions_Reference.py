# Unit 4 Meeting 2 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Task 1: pass or try again - 60 is a passing score
def grade_check():
    score = int(input("Score: "))
    if score >= 60:
        print("Passed")
    else:
        print("Try again")


# Task 2: the fixed bug program - ==, colon, indentation
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


# Task 4 (challenge): 10% discount from 100 and up
def discount():
    price = float(input("Price: "))
    if price >= 100:
        final_price = price * 0.9
    else:
        final_price = price
    print("Final price:", final_price)


# grade_check()
# perfect_check()
# battery_filter()
discount()
