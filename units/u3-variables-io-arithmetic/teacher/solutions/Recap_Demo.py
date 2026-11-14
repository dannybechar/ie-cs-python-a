# Unit 3.2 - Recap of 3.1 (teacher demo, 7 minutes)
# Run ONE block at a time: call a single function at the bottom, predict first, then run.
# Script in Hebrew: ../L02-from-input-to-result-recap-he.md


def block_1_one_value():
    score = 7
    score = 9
    print("Score:", score)          # Score: 9


def block_2_multiple_assignment():
    a, b = 12, 5                    # one line, two assignments, in order
    print(a, b)                     # 12 5


def block_3_convert_stored_variable():
    x = 7
    y = float(x)
    print(y, type(y))               # 7.0 <class 'float'>

    t = str(5)
    print(t, type(t))               # 5 <class 'str'>


def block_3b_what_is_the_purpose():
    # Type 34 when asked. Expected: 34.0
    # Purpose: reads a whole number and prints it as a decimal number.
    number_int = int(input())
    number_float = float(number_int)
    print(number_float)


def block_4_names():
    # Run each line on its own in the Shell or a new file:
    #   my-fuel = 5   -> SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
    #   for = 5       -> SyntaxError: invalid syntax   (for is a reserved word)
    Fuel = 5                        # legal: breaks the convention (lowercase), but it runs
    print(Fuel)                     # 5


block_1_one_value()
# block_2_multiple_assignment()
# block_3_convert_stored_variable()
# block_3b_what_is_the_purpose()
# block_4_names()
