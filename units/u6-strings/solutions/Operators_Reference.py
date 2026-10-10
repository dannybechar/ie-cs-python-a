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


# Task 1b: a word inside a frame of stars
def banner():
    word = input("Word: ")
    line = "*" * (len(word) + 4)
    print(line)
    print("* " + word + " *")
    print(line)


# Task 2: count one letter with a loop and a counter
def count_letter():
    word = input("Word: ")
    letter = input("Letter: ")
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print(letter, "appears", count, "times")


# Task 3: check a password with in
def password_check():
    password = input("Password: ")
    if "!" in password:
        print("Contains !")
    if "7" in password:
        print("Contains 7")
    if "!" in password and "7" in password:
        print("Strong password")


# fixed_warmup()
# greeting()
# banner()
# count_letter()
password_check()
