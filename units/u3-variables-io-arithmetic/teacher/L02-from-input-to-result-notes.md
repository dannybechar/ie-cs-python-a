# Unit 3.2 — Variables, Input/Output & Arithmetic

## Grade 7 / Python A · Lesson Strategy v2
### Topic: From Input to Result

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (45 + 45)  
**Current tool assumption:** Thonny  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note - Thonny**.

---

## 1. Position in Unit 3

Unit 3 has 4 academic hours across 2 double meetings: 1 theory hour and 3 practical hours.

Meeting 1 used the single theory hour and introduced:

**value -> variable name -> input -> output**

Meeting 2 is therefore **Lab + Lab** and adds calculation:

**input -> convert -> calculate -> assign -> output**

This meeting closes Unit 3 and acts as the **Foundation checkpoint** before conditional execution.

---

## 2. Official Scope Used in This Meeting

This meeting draws from the Unit 3 requirements for:

- variables and assignment
- keyboard input and numeric conversion
- basic arithmetic operations
- mathematical operators, including the power operator `**` and basic precedence
- quotient operator (מנה שלמה, חלוקת שלמים) `//`
- remainder operator (שארית חלוקה, מודולו) `%`
- friendly output and intermediate output
- tracing a simple program (טבלת מעקב)
- swapping two values with a temporary variable, and updating a variable from itself (`score = score + 1`)
- choosing suitable numeric data types
- using variables with Turtle (covered in 3.1, Task 3)
- practical assessment using two input values and an arithmetic operation

### Source interpretation - `math`

The detailed Unit 3 page mentions performing basic calculations "using the `math` library," while the official annual overview explicitly names mathematical operators, `//`, `%`, and variables with Turtle, and does not identify any specific `math` functions to teach.

The ministry formula sheet does list `import math`, `math.sqrt`, `abs`, `max` and `min`. The teacher decided (Phase 5) that this meeting does **not** get a `math` lesson: the formula-sheet tour is deferred to exam preparation, and no minutes are added here. The core lesson teaches the explicitly named operators (`+ - * / ** // %`).

---

## 3. Lesson Goal

By the end of the meeting, students should be able to receive numeric input, perform a calculation using variables, trace the changing values, and display a clear result.

Core workflow:

**Read -> Predict -> Trace -> Run -> Check -> Modify -> Build**

Core conceptual relationship:

**input -> number -> calculation -> result -> output**

---

## 4. Student-Facing Learning Objectives

By the end of the lesson, students should be able to:

1. Use `+`, `-`, `*`, and `/` with numeric variables.
2. Predict the result of a simple arithmetic expression before running it.
3. Explain that `/` produces a division result that may be decimal.
4. Use `//` (מנה שלמה) to find the number of complete groups for positive integers.
5. Use `%` (שארית חלוקה, מודולו) to find the remainder after division.
6. Use `**` for powers and predict a short expression with `**`, `*` and parentheses.
7. Receive numeric values using `int(input(...))` or `float(input(...))` as appropriate.
8. Store a calculated result in a new variable.
9. Trace a short calculation program using a table (טבלת מעקב), including a swap through a temporary variable.
10. Update a variable from itself (`score = score + 1`): the right side is worked out first.
11. Produce friendly labeled output (פלט ידידותי).
12. Build a short two-input program that calculates and reports a result.

---

## 5. Technical Baseline

Use standard Python 3 expressions only:

```python
a = 12
b = 5

total = a + b
difference = a - b
product = a * b
quotient = a / b
power = a ** 2
```

Numeric input:

```python
a = int(input("First number: "))
b = int(input("Second number: "))
```

Whole groups and remainder:

```python
full_groups = a // b
left_over = a % b
```

### Beginner-safe boundary

All `//` and `%` examples use **positive integers** and a positive divisor. Do not teach negative floor-division behavior or division by zero in this meeting.

### Deliberate exclusions

Do not introduce:

- comparisons
- conditions
- loops
- advanced order-of-operations problems (only the one short precedence demo at 41-44)
- shorthand operators such as `+=` (the teacher adopted them only as a read-only note at the end of Unit 5.1)
- input validation
- exception handling
- formatted strings as required syntax
- new collections
- function parameters or return values

---

## 6. Core Mental Models and Misconceptions

### Calculation produces a value

```python
total = a + b
```

Read as:

> Calculate `a + b`, then assign the result to `total`.

### Input still needs conversion

```python
a = int(input("First number: "))
```

Mental model:

**input text -> convert -> assign**

### `/` vs `//`

For positive integers:

```python
17 / 5   # 3.4
17 // 5  # 3
```

Use the beginner wording:

> `/` gives the division result. `//` tells us how many complete groups fit.

### `%` is the remainder

```python
17 % 5  # 2
```

Use a physical grouping example: 17 items, 5 per pack -> 3 full packs and 2 left over.

### `**` is the power, and it goes before `*`

```python
2 ** 8      # 256
2 + 3 * 4   # 14
(2 + 3) * 4 # 20
```

Order: parentheses, then `**`, then `*  /  //  %`, then `+  -`.

### Swap needs a third box

```python
num1 = num2
num2 = num1
```

copies the same value twice. Keep one value safe in `temp` first.

### A variable can be updated from itself

```python
score = score + 1
```

Read as: take the **old** `score`, add 1, then store the answer back in `score`. The right side is worked out first.

---

# 7. First 45 Minutes - Lab + Guided Micro-Practice

## 0-5 min - Recap of 3.1 (two items the first lesson did not cover)

The 3.1 lesson was taught on 8 Nov before the ministry alignment, so this recap closes three gaps (full Hebrew script: [`L02-from-input-to-result-recap-he.md`](L02-from-input-to-result-recap-he.md); demo code: `solutions/Recap_Demo.py`). Live in Thonny, predict before every Run; the questions and answers are on add-on slides 1-2 (`../lessons/L02-from-input-to-result/addon-slides-he.pdf`, 8 slides in total), and the whole 15 Nov run of show with slide numbers is in [`L02-from-input-to-result-run-of-show-he.md`](L02-from-input-to-result-run-of-show-he.md).

| Min | Item | Show | Result |
|---|---|---|---|
| 0-1 | Predict | add-on slide 1: three snippets, students predict | |
| 1-2 | Multiple assignment | `a, b = 12, 5`, `print(a, b)` | `12 5` (one line, two assignments, in order) |
| 2-3 | Convert a stored variable; `str()` | `y = float(x)` (7 gives `7.0 <class 'float'>`), `str(5)` (`5 <class 'str'>`) | the original `x` does not change |
| 3-4 | "What is the purpose of the code?" | `number_float = float(number_int)` with input 34 | `34.0`: reads a whole number and prints it as a decimal number |
| 4-5 | Answers slide + one spoken aside | add-on slide 2; say aloud: `my-fuel` and `for` are not legal names (special character, reserved word), `Fuel` runs (convention) | |

Purpose: reactivate the variable model without reteaching Meeting 1, and give the students the tools used in this lesson (`a, b = ...`, `float(...)`, `str(...)`). Naming rules are a 30-second spoken aside, not a slide (they are in `L02-from-input-to-result-recap-he.md` if you want the full table).

---

## 5-13 min - Four Basic Arithmetic Operators

Show:

```python
a = 12
b = 5

print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
```

Students predict each result before Run.

Focus only on:

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division

Exponentiation (`**`) comes later in this half (41-44 min).

Explicitly notice that `12 / 5` produces `2.4`.

---

## 13-20 min - Store the Result

Move from calculation inside `print()` to a named result:

```python
price = 8
quantity = 3
total = price * quantity
print("Total:", total)
```

Trace together:

| After line | price | quantity | total | output |
|---|---:|---:|---:|---|
| `price = 8` | 8 | | | |
| `quantity = 3` | 8 | 3 | | |
| `total = price * quantity` | 8 | 3 | 24 | |
| `print(...)` | 8 | 3 | 24 | `Total: 24` |

Target insight:

> A calculation creates a value; a variable can store that result for later use.

---

## 20-29 min - Complete Groups with `//`

Physical/visual prompt:

> We have 17 stickers. Each pack holds 5. How many **full** packs can we make?

Then show:

```python
items = 17
per_pack = 5
full_packs = items // per_pack
print("Full packs:", full_packs)
```

Predict before Run.

Target answer: `3`.

Do not describe `//` as ordinary division with the decimal "cut off" in all cases. Keep the context to positive integers and complete groups.

---

## 29-36 min - What Is Left? `%`

Continue the same context:

```python
left_over = items % per_pack
print("Left over:", left_over)
```

Ask:

**What happened to the two stickers that did not fill another pack?**

Mental model:

**17 items = 3 full groups of 5 + 2 left over**

Connect:

- `17 // 5` -> 3 complete groups
- `17 % 5` -> 2 remaining items

---

## 36-41 min - Input -> Calculate -> Output

Turn fixed values into input:

```python
price = int(input("Price: "))
quantity = int(input("Quantity: "))
total = price * quantity
print("Total:", total)
```

Before Run, students identify the five stages:

1. input
2. conversion
3. assignment
4. calculation
5. output

Run with two different pairs of values.

---

## 41-44 min - The Power Operator `**` and Order of Operations

Show and predict, one line at a time:

```python
print(2 ** 8)
print(5 ** 2)
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 * 3 ** 2)
```

Verified output: `256`, `25`, `14`, `20`, `18`.

Say: `**` is the power: `5 ** 2` is 5 times 5. Order: parentheses first, then `**`, then `*  /  //  %`, then `+  -`. Parentheses change the order. Add the row to the helper table:

| Operator | Meaning | Example |
|---|---|---|
| `**` | power | `5 ** 2` ← `25` |

Target insight:

> `**` is done before `*`, and parentheses beat everything; with doubt, add parentheses.

Keep it to these five lines: this is not a precedence lesson.

---

## 44-45 min - Workflow + Transition

Show:

**Read -> Predict -> Trace -> Run -> Check -> Modify -> Build**

Keep one minute as genuine transition buffer.

---

# 8. Second 45 Minutes - Lab

Use one starter file that evolves through the lab.

## Starter filename

[`Arithmetic_Starter.py`](../exercises/Arithmetic_Starter.py)

Starter:

```python
a = 12
b = 5

total = a + b
difference = a - b
product = a * b
quotient = a / b

print("Add:", total)
print("Subtract:", difference)
print("Multiply:", product)
print("Divide:", quotient)
```

---

## 45-48 min - Open + Read + Predict

Students open the starter.

Do not run yet.

Predict all four output values.

---

## 48-51 min - Run -> Check

Run and compare.

Ask:

- Which operation produced a decimal value?
- Which variables store calculated results?

---

## 51-59 min - Change the Inputs, then Make It Interactive

Change only:

```python
a = 20
b = 4
```

Before Run, predict all four new outputs. Then choose another pair of positive integers and repeat.

Core habit:

**Change inputs -> predict results -> test**

Then replace the fixed values with:

```python
a = int(input("First number: "))
b = int(input("Second number: "))
```

Keep all calculation and output lines unchanged. Run with `12` and `5`, then with another pair.

Target insight:

> The algorithm stays the same while the input values change.

---

## 59-65 min - Quotient and Remainder Challenge

Add:

```python
full_groups = a // b
left_over = a % b

print("Full groups:", full_groups)
print("Left over:", left_over)
```

Use positive values with `b > 0`.

Before Run, complete this trace for `a = 17`, `b = 5`:

| expression | predicted value |
|---|---:|
| `a // b` | ___ |
| `a % b` | ___ |

Then Run -> Check.

---

## 65-69 min - Trace Challenge

Given:

```python
items = 23
per_pack = 6
full_packs = items // per_pack
left_over = items % per_pack
```

Students complete the four-variable trace before running.

Expected final values:

- `items` = 23
- `per_pack` = 6
- `full_packs` = 3
- `left_over` = 5

---

## 69-76 min - Swap with `temp` + Update from Itself

**Swap (5 min).** Predict first, then trace:

```python
num1 = 4
num2 = 9
num1 = num2
num2 = num1
print(num1, num2)
```

Many students predict `9 4`. Trace table:

| After line | num1 | num2 | output |
|---|---:|---:|---|
| `num1 = 4` | 4 | | |
| `num2 = 9` | 4 | 9 | |
| `num1 = num2` | 9 | 9 | |
| `num2 = num1` | 9 | 9 | |
| `print(num1, num2)` | 9 | 9 | `9 9` |

The first value was overwritten. Fix: keep it in a third box.

```python
num1 = 4
num2 = 9
temp = num1
num1 = num2
num2 = temp
print(num1, num2)
```

Output `9 4`. Students add the `temp` column and trace again.

**Self-update (2 min).** One line in the same trace style:

```python
score = 7
score = score + 1
print("Score:", score)
```

| After line | score | output |
|---|---:|---|
| `score = 7` | 7 | |
| `score = score + 1` | 8 | |
| `print(...)` | 8 | `Score: 8` |

Target insight: **the right side is worked out first, then stored in the name on the left.**

---

## 76-79 min - Reset + Genuine Buffer

Students clear the calculation block and keep a clean editor for the final build.

Use this time for:

- missing parentheses
- missing `int(...)`
- misspelled variable names
- accidental zero divisor

Do not introduce new syntax.

---

## 79-87 min - Packing Calculator - Protected Core Task

### New Build

Create a program that:

1. asks how many items there are and stores an `int` in `items`
2. asks how many items fit in each pack and stores a positive `int` in `per_pack`
3. calculates the number of full packs using `//`
4. calculates the number left over using `%`
5. stores both results in variables
6. prints two friendly output lines

Expected structure (one function and one call, the same style as 3.1):

```python
def packing():
    items = int(input("How many items? "))
    per_pack = int(input("How many items per pack? "))

    full_packs = items // per_pack
    left_over = items % per_pack

    print("Full packs:", full_packs)
    print("Left over:", left_over)


packing()
```

Starter: [`Packing_Starter.py`](../exercises/Packing_Starter.py) (the two inputs and the two prints; students write the two calculations).

Required test:

- `items = 17`
- `per_pack = 5`
- expected: 3 full packs, 2 left over

Students must predict the result before the first Run.

This task directly supplies the official practical evidence: **two input values + arithmetic calculation + clear output**.

---

## 87-90 min - Save + Visual Exit Check

Save as:

`G7_U3_M2_Packing_<Name>.py`

Exit code:

```python
items = 17
per_pack = 5
print(items // per_pack)
print(items % per_pack)
```

Ask:

**Which two lines will be printed?**

- A: `3` then `2`
- B: `3.4` then `0`
- C: `2` then `3`

Correct answer: **A**.

---

## Minute plan (sums to 90)

| Block | Minutes | Running total |
|---|---:|---:|
| Recap of 3.1 (multiple assignment, conversion, purpose) | 5 | 5 |
| Four basic operators | 8 | 13 |
| Store the result | 7 | 20 |
| Complete groups with `//` | 9 | 29 |
| What is left? `%` | 7 | 36 |
| Input -> calculate -> output | 5 | 41 |
| `**` and order of operations | 3 | 44 |
| Workflow + transition | 1 | 45 |
| Open, read, predict | 3 | 48 |
| Run -> check | 3 | 51 |
| Change the inputs, then make it interactive | 8 | 59 |
| Quotient and remainder challenge | 6 | 65 |
| Trace challenge | 4 | 69 |
| Swap with `temp` + update from itself | 7 | 76 |
| Reset + genuine buffer | 3 | 79 |
| Packing Calculator (protected) | 8 | 87 |
| Save + visual exit check | 3 | 90 |

Lab part 1: 0-45 (45). Lab part 2: 45-90 (45).

---

# 9. Misconception Risks

## Misconception 1 - `*` looks like the multiplication symbol students know

Correction:

> Python uses `*` for multiplication.

## Misconception 2 - `/` and `//` mean the same thing

Correction:

> In our positive-integer examples, `/` gives the division result; `//` gives the number of complete groups.

## Misconception 3 - `%` means percentage

Correction:

> In this Python context, `%` gives the remainder after division.

## Misconception 4 - Typed digits are automatically numeric

Correction:

> `input()` returns text. Convert with `int(...)` or `float(...)` before numeric calculation.

## Misconception 5 - The formula must change when the user enters different values

Correction:

> The same calculation can work with many input values because variables hold the changing data.

## Misconception 6 - `full_packs` must be calculated mentally rather than stored

Correction:

> Store useful intermediate results in named variables so the program is easier to read, trace, and reuse.

## Misconception 7 - `**` is the same as `*`

Correction:

> `5 * 2` is 10, `5 ** 2` is 25. `**` is the power and is done before `*`.

## Misconception 8 - `num1 = num2` then `num2 = num1` swaps them

Correction:

> After the first line both boxes hold the same value. Keep one value in `temp` first.

## Misconception 9 - `score = score + 1` is a false equation

Correction:

> `=` means "put into". The right side is worked out with the old value, then stored.

---

# 10. Assessment Evidence

Primary evidence:

- predicted output from the starter
- correct arithmetic results for `+`, `-`, `*`, `/`, and a predicted `**` / precedence line
- trace table for a calculated variable
- correct interpretation of `//` and `%`
- successful conversion of numeric input
- successful modification without changing formulas
- swap trace with `temp`, and the `score = score + 1` trace
- successful protected Packing Calculator
- friendly labeled output
- visual exit-check response

The **Packing Calculator** is the protected core task.

The trace challenge provides the official theoretical evidence; the Packing Calculator provides the official practical evidence.

---

# 11. Critical Review Applied Before Asset Creation

The draft strategy was reviewed for syllabus alignment, technical correctness, cognitive load, timing realism, and misconception risk.

### Decisions retained after review

1. **Meeting 2 is Lab + Lab.** The single Unit 3 theory hour was already used in Meeting 1.
2. **Teach one-operation expressions first.** Complex precedence problems are unnecessary at this stage; one short `**` and precedence demo (3 min, 41-44) is added because the ministry formula sheet lists `**`.
3. **Teach `//` and `%` through complete groups and leftovers.** This gives both operators a concrete model rather than presenting them as symbols to memorize.
4. **Restrict quotient/remainder examples to positive integers.** Negative floor semantics and division-by-zero handling are outside the Grade 7 scope here.
5. **Keep numeric conversion visible.** `int(input(...))` remains explicit so students do not lose the input-type model from Meeting 1.
6. **Use stored intermediate results.** This supports trace-table work and friendly, readable programs.
7. **No Turtle bridge in 3.2.** The official overview's "variables with Turtle" is covered by 3.1 Task 3 (`side` drives the square); the 3.2 bridge duplicated it and was deleted (Phase 5, U3-12), freeing 3 minutes.
8. **Do not add a separate `math`-module lesson.** The formula-sheet tour (`import math`, `math.sqrt`, `abs`, `max`, `min`) is deferred to exam preparation; the 3 minutes it would need do not fit this unit. `**` is taught as an operator (it is on the formula sheet).
9. **Protect 8 minutes for the final build and bank 3 minutes immediately before it.** If the lesson runs late, shorten earlier modification cycles rather than cutting the Packing Calculator.
10. **Use exactly two inputs in the protected task.** This matches the official practical-assessment direction directly.
11. **Swap and self-update added (Phase 5, U3-03), 7 minutes.** Funded by shortening open/read/predict (9 to 6) and merging "change the inputs" with "make it interactive" (12 to 8). The packing calculator is wrapped in `def packing():` (0 minutes) for consistency with 3.1.

---

# 12. Enrichment

Only after the Packing Calculator is complete.

Suitable extensions using the same concepts:

- change the context from packs to teams, trays, or pages
- add a third numeric input and another simple calculation
- use `float` input for a price calculation
- calculate and print an intermediate value for debugging
- use a variable to change the size of the Turtle square (as in 3.1 Task 3)

Do not introduce conditions, loops, collections, error handling, or advanced mathematical functions as enrichment.

---

# 13. Lesson Assets

- [`../lessons/L02-from-input-to-result/slides-he.pdf`](../lessons/L02-from-input-to-result/slides-he.pdf) — Hebrew slides (NotebookLM, 22 slides; skip slides 2-3 and 12-13, replaced by the recap and the `**` slides)
- [`../lessons/L02-from-input-to-result/addon-slides-he.pdf`](../lessons/L02-from-input-to-result/addon-slides-he.pdf) — 8 add-on slides (recap of 3.1, `**`, swap, self-update); built by `tools/lab-sheet-builder/build_u3_m2_addon.py`
- [`L02-from-input-to-result-recap-he.md`](L02-from-input-to-result-recap-he.md), [`L02-from-input-to-result-run-of-show-he.md`](L02-from-input-to-result-run-of-show-he.md) — recap script and minute-by-minute run of show
- [`Arithmetic_Starter.py`](../exercises/Arithmetic_Starter.py) and [`Arithmetic_Reference.py`](solutions/Arithmetic_Reference.py)
- [`../lessons/L02-from-input-to-result.md`](../lessons/L02-from-input-to-result.md) — Hebrew lab brief
- [`Packing_Starter.py`](../exercises/Packing_Starter.py) and [`Packing_Reference.py`](solutions/Packing_Reference.py)
- [`../lessons/L02-from-input-to-result/exit-check-he.png`](../lessons/L02-from-input-to-result/exit-check-he.png) — visual exit check A/B/C

---

# 14. Unit 3 Exit Criteria

At the end of Unit 3, a student should be able to:

**choose variables -> receive input -> convert type -> calculate -> trace -> display clear output**

Unit 3 is complete when students can independently solve the Packing Calculator and explain what `//` and `%` produce in that context.
