# Unit 5.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: the update brings the loop closer to its end
def fixed_warmup():
    number = 1
    while number <= 5:
        print(number)
        number = number + 1
    print("Finished")


# Task 1: ask again until the password is right
def password():
    word = input("Password: ")
    while word != "python":
        print("Try again")
        word = input("Password: ")
    print("Access granted")


# Task 2: add numbers until the user types 0 (the sentinel)
def sum_until_zero():
    total = 0
    number = int(input("Number, 0 to stop: "))
    while number != 0:
        total = total + number
        number = int(input("Number, 0 to stop: "))
    print("Total:", total)


# Task 3: how many trips before the battery drops below 20?
def rover_trips():
    battery = 100
    trips = 0
    while battery >= 20:
        battery = battery - 15
        trips = trips + 1
        print("Trip", trips, "battery", battery)
    print("Trips:", trips)


# Challenge: the sum of the digits of a number (print it; no return yet)
# n % 10 is the last digit, n // 10 removes it (from Unit 4)
def digit_sum():
    number = int(input("Number: "))
    total = 0
    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10
    print("Digit sum:", total)


# Classification drill (guided, not run in class): finite or endless?
# 1) i = 1; while i <= 5: print(i)            endless - no update
# 2) i = 10; while i > 0: i = i + 1           endless - the update goes the wrong way
# 3) i = 0; while i != 5: i += 2              endless - i jumps over 5 (0, 2, 4, 6 ...)
# 4) i = 0; while i < 5: i += 2               finite - 0, 2, 4: three rounds


# fixed_warmup()
# password()
# sum_until_zero()
# digit_sum()
rover_trips()
