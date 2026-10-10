# Unit 6.4 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.
import turtle


# Warm-up: lower() makes Yes, YES and yes the same
def fixed_warmup():
    answer = input("Answer: ").lower()
    if answer == "yes":
        print("Accepted")
    else:
        print("Rejected")


# Task 1a: is it a Python file? (.py or .PY)
def file_check():
    filename = input("File name: ")
    if filename.lower().endswith(".py"):
        print("Python file")
    else:
        print("Not a Python file")


# Task 1b: hide the dashes in a phone number
def hide_phone():
    phone = input("Phone: ")
    print(phone.replace("-", "*"))


# Task 2: write a greeting on the Turtle screen
def name_card():
    name = input("Name: ")
    turtle.hideturtle()
    turtle.pencolor("blue")
    turtle.write("Hello " + name.upper(), align="center", font=("Arial", 24, "normal"))
    turtle.done()


# Checkpoint A1: a short report on a sentence
def text_report():
    text = input("Sentence: ")
    print("Length:", len(text))
    print("a count:", text.lower().count("a"))
    print("First space:", text.find(" "))
    print("Starts with H:", text.startswith("H"))
    print("Upper:", text.upper())


# Checkpoint A2: a student code is 6 digits
def code_check():
    code = input("Code: ")
    if code.isnumeric() and len(code) == 6:
        print("Valid")
    else:
        print("Invalid")


# fixed_warmup()
# file_check()
# hide_phone()
# name_card()
# text_report()
code_check()
