# Unit 8 — Extra practice pack (take-home, 0 class minutes)

Optional ("רשות") practice for Unit 8, one block per meeting. Nothing here is graded and nothing is needed for the checkpoint. Statements are written for this course (no solutions); the source column points to the ministry material the idea comes from, for the teacher. Solutions: the teacher writes them from the sources or asks for them; the reference files hold only the in-class tasks.

Terminology: "פעולה" = "פונקציה". Where a task says "returns", it uses return-lite from 8.3 (one simple value).

## After 8.1 and 8.2 (functions that act, input inside)

| # | Exercise | Source (extract file) |
|---|---|---|
| 1 | "Magic carpet": write three print-shapes (for example a line, a triangle, a square of stars) as three functions, and call them in different orders to build different patterns. | `materials-m04-1-8172ae.md` slide 17 |
| 2 | `draw_door()`: add a door to the 8.2 house (starter steps in the 8.2 lab brief). | repo 8.2 (moved from the in-class challenge) |
| 3 | The ministry trace sheet: write the output of the three remaining functions (items ב, ג, ד) before running them. | `classwork-m04-3-ab81e5.md` Ex 1 |
| 4 | Pizza order: a function reads the number of pizzas and the price of one pizza and prints the total. Run it with two different inputs. | `classwork-m04-3-ab81e5.md` Ex 2 (word-bank version) |
| 5 | `super()`: read the number of bottles and the price of one bottle, print the total with a 10% discount. | `classwork-m04-3-ab81e5.md` Ex 6 |
| 6 | Triangle perimeter and a small calculator: functions that read inputs and print a result (optional ministry tasks; the cake-sale task is marked "not required" there). | `classwork-m04-2-e18765.md` |

## After 8.3 (parameters and return-lite)

| # | Exercise | Source |
|---|---|---|
| 7 | `draw_rectangle(width, height)`: call it as `(140, 70)` and `(70, 140)` and describe the difference. | repo 8.3 (moved from the in-class Task 3) |
| 8 | "Greeting" and "my name": `greet(name)` and `show_name(first, last)`. Call `show_name` with the names in the wrong order and explain what is printed. | `classwork-m10-2-2fab02.md` ("ברכת שלום", "השם שלי") |
| 9 | "Sign of a number" first as a function that prints, then as a function that returns the text; compare the call lines. | `classwork-m10-2-2fab02.md` ("סימן מספר", "סימן מספר 2") |
| 10 | `subtract(num1, num2)` that returns the difference. Predict `print(subtract(7, 4))`, `print(subtract(4, 7))`, `print(subtract(1, 5))`, `print(subtract(5, 1))`; does the order matter? Then read two numbers with `input` outside the function, send them in and print the result. | `materials-m10-1-480a45.md` slides 21-22 (optional task "פעולת חיסור") |
| 11 | `modulo(num1, num2)`, `power(num1, num2)`: two functions that return a value; predict the output of three calls each. | `materials-m10-1-480a45.md` slides 25-28 |
| 12 | `average(a, b)` that returns the average of two numbers, and `repeat(word, times)` that returns the word repeated `times` times (print outside). | `classwork-m10-4-dc62f7.md` Q3, Q8 |
| 13 | `even(number)` that returns `True` or `False`, and a function `guess_game` style task that compares a guess to a secret number and returns a message. Uses `%` and `elif`. | `classwork-m10-4-dc62f7.md` Q1, Q11 |
| 14 | Digit functions: `last_digit(number)` returns the last digit (`%`), `drop_last_digit(number)` returns the number without it (`//`). Optional: `reverse` of a 3-digit number. This is the digit-extraction practice deferred from Unit 3 (hosted by Unit 4, extended here). | `materials-m10-1-480a45.md` slide 32 (optional) |
| 15 | A bus or flower-shop price function with a compound condition (age and time), returning the price. | `classwork-m10-4-dc62f7.md` Q5, Q10 |

## After 8.4 (scope, global, spiral)

| # | Exercise | Source |
|---|---|---|
| 16 | The `score` riddle, with the `global` line deleted and then restored: predict both outputs, then run. | `materials-m16-1-42299c.md` slides 33-35 |
| 17 | `roll_dice()` that returns `True` or `False` (a "six" or not) and a global counter that counts the sixes in ten rolls. Needs `random` (Unit 7) and return. | `materials-m16-1-42299c.md` slide 37 |
| 18 | `gcd(a, b)`: a function with two parameters that returns the greatest common divisor. For strong students only. | `classwork-m16-6-1c1b6a.md` task 9 |
| 19 | Convert a Unit 5 loop task of your choice (a sum, a counter, a table) into a function with parameters: first printing, then returning. | repo Unit 5; `materials-m12-1-028c50.md` slide 25 |
| 20 | Optional online practice (links, content not machine-checked): H5P 10.5 "ספרייה דיגיטלית", 10.6 "חדר כושר לתכנות"; "Master Python" 4.4 and 10.3. | `links.md`, `materials-m10-1-480a45.md` slide 1 notes |

The ministry source defects listed in `docs/ministry-program/audit-summary.md` ("do NOT copy") apply to every item above; the statements here were written fresh.
