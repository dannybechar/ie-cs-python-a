# Unit 6.3 - reference solutions for the teacher.
# One function per task (define -> call, from Unit 1).
# Run ONE task at a time: remove the # from one call at the bottom.


# Task 1: end is not included, so stop at 5 to include index 4
def fixed_slice():
    word = "abcdefgh"
    print(word[1:5])


# Task 2: the first three and the last three letters
def ends():
    word = input("Word: ")
    print(word[:3])
    print(word[len(word) - 3:])


# Task 3: the secret message hides in every second letter
def decode():
    secret = "xPxyxtxhxoxn"
    print(secret[1::2])


# Task 4: a palindrome reads the same in both directions
def palindrome():
    word = input("Word: ")
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")


# fixed_slice()
# ends()
# decode()
palindrome()
