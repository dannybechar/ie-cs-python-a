# Unit 6.2 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: convert to int, then + adds numbers
def fixed_warmup():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("Sum:", a + b)


# Task 1a: a greeting built with +
def greeting():
    first = input("First name: ")
    last = input("Last name: ")
    message = "Hello " + first + " " + last
    print(message)


# Task 1b: build a new string without the spaces
# result starts as "" like a counter starts at 0
def remove_spaces():
    text = input("Sentence: ")
    result = ""
    for char in text:
        if char != " ":
            result = result + char  # the short form: result += char
    print(result)


# Task 2: count one letter with a loop and a counter
def count_letter():
    word = input("Word: ")
    letter = input("Letter: ")
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print(letter, "appears", count, "times")


# Task 3: build a string, even indexes become stars
def stars():
    text = input("Word: ")
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result = result + "*"
        else:
            result = result + text[i]
    print(result)


# Task 4: a valid mail has no space and has an @
def check_mail():
    mail = input("Mail: ")
    if " " not in mail and "@" in mail:
        print("Valid")
    else:
        print("Invalid")


# Task 5: check a password with in
def password_check():
    password = input("Password: ")
    if "!" in password:
        print("Contains !")
    if "7" in password:
        print("Contains 7")
    if "!" in password and "7" in password:
        print("Strong password")


# Optional: a word inside a frame of stars
def banner():
    word = input("Word: ")
    line = "*" * (len(word) + 4)
    print(line)
    print("* " + word + " *")
    print(line)


# Optional: every third letter (range with a step)
def every_third():
    text = input("Text: ")
    result = ""
    for i in range(0, len(text), 3):
        result = result + text[i]
    print(result)


# fixed_warmup()
# greeting()
# remove_spaces()
# count_letter()
# stars()
# check_mail()
# banner()
# every_third()
password_check()
