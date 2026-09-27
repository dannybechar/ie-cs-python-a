# Unit 6.1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: the last index is len(word) - 1
def fixed_warmup():
    word = "rover"
    print(word[len(word) - 1])


# Task 1: the first letter of each name
def initials():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    print(first_name[0], last_name[0])


# Task 2: length, first letter and last letter of a word
def word_info():
    word = input("Word: ")
    print("Length:", len(word))
    print("First:", word[0])
    print("Last:", word[len(word) - 1])


# Task 3 (challenge): every index with its letter
def index_map():
    word = input("Word: ")
    for i in range(len(word)):
        print(i, word[i])


# fixed_warmup()
# initials()
# word_info()
index_map()
