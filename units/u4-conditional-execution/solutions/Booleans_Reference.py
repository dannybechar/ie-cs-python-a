# Unit 4 Meeting 1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Task 1: sensor check - every line prints True or False
def sensor_check():
    temperature = int(input("Temperature: "))
    print("Freezing:", temperature < 0)
    print("Safe range:", temperature >= -20 and temperature <= 40)


# Task 2: fixed bug - input gives text, so convert before comparing
def fixed_score():
    score = int(input("Score: "))
    passed = score >= 60
    print("Passed:", passed)


# Task 3: build the truth table of "has_fuel and battery_ok"
def truth_table():
    has_fuel = True
    battery_ok = True
    print(has_fuel, battery_ok, has_fuel and battery_ok)
    battery_ok = False
    print(has_fuel, battery_ok, has_fuel and battery_ok)
    has_fuel = False
    battery_ok = True
    print(has_fuel, battery_ok, has_fuel and battery_ok)
    battery_ok = False
    print(has_fuel, battery_ok, has_fuel and battery_ok)


# sensor_check()
# fixed_score()
truth_table()
