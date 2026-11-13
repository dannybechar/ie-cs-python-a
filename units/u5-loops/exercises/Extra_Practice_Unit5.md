# Unit 5 — Extra practice pack (take-home, zero class minutes)

For students who finish early and for homework after Unit 5. Statements are written for this course (no `return`, no lists, `input()` instead of parameters); the "Source" column points the teacher to the ministry file in `docs/ministry-program/extracts/`. No solutions here. Code that has to be traced goes on paper first, then is checked by running it.

Allowed tools: `for`, `range`, `while`, `if` / `elif`, `%`, `//`, `end=`, and `+=` as a shorthand you can read. A function is also called "פעולה" in the ministry texts.

## A. `for` loops (after 5.2)

| # | Statement | Source |
|---|---|---|
| A1 | Read a number `n`. Print `*` n times on one line, then print the numbers 1 to n separated by commas (no comma after the last is a bonus). | `materials-m12-1`, slides 13-20 |
| A2 | Read two whole numbers. Print every number from the first to the second (go down if the first is bigger). | `materials-m12-1`, slides 22-24 |
| A3 | Read `n`. Print the sum of the series 1 + 2 + ... + n. Then print the sum of the even numbers up to n. | `materials-m12-1`, slides 25-30 |
| A4 | Read 10 numbers and print their average. Write the loop with three different `range` forms that give the same count. | `materials-m12-1`, slides 31-34 |
| A5 | Print the even numbers from 0 to 100, then the odd numbers from 1 to 99, each on one line. | `materials-m12-1`, slides 28-30 |
| A6 | 7-boom up to 100: print `Boom` instead of a number that is a multiple of 7, ends with 7, or has 7 as its tens digit. | `materials-m12-1`, slides 38-39 (the ministry solution tests `number / 10 == 7`; that is wrong, use `//`) |
| A7 | Thirteen "what does it print?" snippets with `range`, `if` and `end=" "`. Solve on paper, then run. | `classwork-m12-7-6bdc55`, Q1 |
| A8 | A shirt fundraiser: read the size (S, M or L) of 5 students (S pays 20, M pays 30, L pays 40). Print how many of each size and the total paid. | `classwork-m12-4-4ec331`, Q1 (scaled down from 30 students) |
| A9 | Read the three grades of each of 5 students. The final grade is the average, plus 5 if the third grade is above 85, at most 100. Print each final grade and how many got 100. | `classwork-m12-4-4ec331`, Q2-Q3 (scaled down from 10 students) |
| A10 | Optional Turtle: the eight-square flower (`flower()` in `Nested_Reference.py`) with a different number of squares; the turn becomes `360 / squares`. | 5.4 brief, optional task |

## B. `while` loops (after 5.3)

| # | Statement | Source |
|---|---|---|
| B1 | Print the series 1, 4, 7, ... up to 30 with a `while` loop and again with a `for` loop; print a descending series the same two ways. | `materials-m13-1`, slides 10-13; `classwork-m13-2-8204a6` |
| B2 | Read numbers until the user types 0 or a negative number. Print the average of the positive numbers (guard against no numbers at all with an `if`). | `materials-m13-1`, slides 14-15 (the source solution is partial) |
| B3 | Read names until an empty line; print how many names were typed. | `materials-m13-1`, slides 16-17 |
| B4 | Ask for a three-digit number until the user gives one (`100` to `999`). Use `or` in the condition. | `materials-m13-1`, slides 21-22 |
| B5 | Ask for numbers until exactly three even numbers were typed; print them all at the end. (No lists: print each one as it arrives.) | `materials-m13-1`, slide 23 |
| B6 | Count the red beads: the user types a color, then yes or no for "continue?". Print the number of `red`. | `classwork-m12-4-4ec331`, Q4 (fill-in version: copy the skeleton with blanks) |
| B7 | Finite or endless? Ten snippets (five with a plain update, five with `i = i % 10`, `i = i / 10` or `!= 10` with a step). For a finite loop write the output. | `classwork-m13-4-acd0a1`, Q1-Q2 |
| B8 | Outputs of six `while` snippets with `+=` and `-=`, including `print(i, x)` after the loop (the values after the loop ends). | `classwork-m13-4-acd0a1`, Q3-Q4 |
| B9 | Read a positive number and print its digits one per line from the last to the first; then print the number reversed. | `classwork-m18-3-875584`, #3 (needs `% 10`, `// 10`; challenge) |
| B10 | Read a number and print whether it is a perfect number (equal to the sum of its divisors smaller than it). Challenge. | `materials-m18-1-88ee0a`, #11 |

## C. Exam-style paper sets (after Unit 5, again before the exam)

| Set | Items | Notes |
|---|---|---|
| 18.1 / 18.2 | #4, #5, #6, #7, #8, #9, #10 first; #1-#3 after Unit 4; #11-#12 optional | Item 8(c) must be `range(6, 1, -2)`; item 12 needs `range(1, 10)`. See section 9 of `m4-lesson-notes.md` |
| 18.3 | #1 after `elif`; #2(a) now; #3 optional | Skip #2(b): `for ... else` is not taught |

Source of every row: ministry Python A folder, read-only extracts. Solutions: ask the teacher; items that mirror class tasks have reference code in `solutions/`.
