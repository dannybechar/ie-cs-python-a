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


# fixed_warmup()
# password()
# sum_until_zero()
rover_trips()
