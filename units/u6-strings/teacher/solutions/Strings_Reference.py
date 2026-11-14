# Unit 6.1 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: the last index is len(word) - 1 (or -1 from the end)
def fixed_warmup():
    word = "rover"
    print(word[len(word) - 1])
    print(word[-1])


# Task 1: the first letter of each name
def initials():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    print(first_name[0], last_name[0])


# Task 2: length, first letter and last letter of a word (two ways to the last)
def word_info():
    word = input("Word: ")
    print("Length:", len(word))
    print("First:", word[0])
    print("Last:", word[len(word) - 1])
    print("Last (short):", word[-1])


# Task 3 (challenge): every index, the same index from the end, and the letter
def index_map():
    word = input("Word: ")
    for i in range(len(word)):
        print(i, i - len(word), word[i])


# fixed_warmup()
# initials()
# word_info()
index_map()
