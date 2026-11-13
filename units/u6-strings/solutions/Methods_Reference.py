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


# Task 1c: find vs index, and the optional parameters
def index_and_options():
    text = "banana"
    print(text.find("z"))  # -1
    # print(text.index("z"))  # ValueError: substring not found (on purpose)
    print(text.find("a", 2))  # 3: start looking at index 2
    print("playlist".startswith("list", 4))  # True
    print("a-b-c".replace("-", "*", 1))  # a*b-c


# Task 2: write a greeting on the Turtle screen (course style, GUI)
def name_card():
    name = input("Name: ")
    turtle.hideturtle()
    turtle.pencolor("blue")
    turtle.write("Hello " + name.upper(), align="center", font=("Arial", 24, "normal"))
    turtle.done()


# Task 3: the same card in the exam dialect (GUI)
def name_card_exam():
    name = input("Name: ")
    wn = turtle.Screen()
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pencolor("blue")
    pen.write("Hello " + name.upper(), align="center", font=("Arial", 24, "normal"))
    wn.mainloop()


# Checkpoint A1: a short report on a sentence
def text_report():
    text = input("Sentence: ")
    print("Length:", len(text))
    print("a count:", text.lower().count("a"))
    print("First space:", text.find(" "))
    print("Starts with H:", text.startswith("H"))
    print("Last:", text[-1])
    print("Upper:", text.upper())


# Checkpoint A2: a student code is 6 digits
def code_check():
    code = input("Code: ")
    if code.isdigit() and len(code) == 6:  # isnumeric works the same on digits
        print("Valid")
    else:
        print("Invalid")


# fixed_warmup()
# file_check()
# hide_phone()
# index_and_options()
# name_card()
# name_card_exam()
# text_report()
code_check()
