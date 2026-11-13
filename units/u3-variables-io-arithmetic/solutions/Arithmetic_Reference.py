# Unit 3 Meeting 2 - reference solutions for the teacher.
# Pairs with Arithmetic_Starter.py (the starter is the first step of the lab).
# The packing calculator is in Packing_Reference.py.
# Run ONE function at a time: remove the # from one call at the bottom.


# Lab steps 3-5: the starter made interactive, plus // and %
def arithmetic():
    a = int(input("First number: "))
    b = int(input("Second number: "))

    total = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    full_groups = a // b
    left_over = a % b

    print("Add:", total)
    print("Subtract:", difference)
    print("Multiply:", product)
    print("Divide:", quotient)
    print("Full groups:", full_groups)
    print("Left over:", left_over)


# The power operator and the order of operations
def power_and_order():
    print(2 ** 8)
    print(5 ** 2)
    print(2 + 3 * 4)
    print((2 + 3) * 4)
    print(2 * 3 ** 2)


# Swap two values with a temporary variable
def swap():
    num1 = 4
    num2 = 9
    temp = num1
    num1 = num2
    num2 = temp
    print(num1, num2)


# Update a variable from itself: the right side is worked out first
def self_update():
    score = 7
    score = score + 1
    print("Score:", score)


arithmetic()
# power_and_order()
# swap()
# self_update()
