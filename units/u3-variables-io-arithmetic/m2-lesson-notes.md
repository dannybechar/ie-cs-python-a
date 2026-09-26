# G7 Unit 3 Meeting 2 Lesson Strategy v2

## Grade 7 / Python A
### Unit 3 - Variables, Input/Output & Arithmetic
### Meeting 2 - From Input to Result

**Status:** Approved strategy after critical review; ready for asset creation  
**Duration:** 90 minutes  
**Structure:** Lab + Lab  
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
- mathematical operators
- quotient operator `//`
- remainder operator `%`
- friendly output and intermediate output
- tracing a simple program
- choosing suitable numeric data types
- using variables with Turtle
- practical assessment using two input values and an arithmetic operation

### Source interpretation - `math`

The detailed Unit 3 page mentions performing basic calculations "using the `math` library," while the official annual overview explicitly names mathematical operators, `//`, `%`, and variables with Turtle, and does not identify any specific `math` functions to teach.

For this 4-hour beginner unit, the core lesson therefore teaches the explicitly named operators and does **not** add a separate `math.sqrt`, `math.pow`, or similar API. If later Ministry implementation materials specify required `math` functions, they can be inserted without changing the unit architecture.

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
4. Use `//` to find the number of complete groups for positive integers.
5. Use `%` to find the remainder after division.
6. Receive numeric values using `int(input(...))` or `float(input(...))` as appropriate.
7. Store a calculated result in a new variable.
8. Trace a short calculation program using a table.
9. Produce friendly labeled output.
10. Use a variable as a Turtle movement parameter.
11. Build a short two-input program that calculates and reports a result.

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
- exponentiation as required syntax
- advanced order-of-operations problems
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

### Variable values can drive Turtle

```python
side = 80
turtle.forward(side)
```

The movement distance comes from the current value of `side`.

---

# 7. First 45 Minutes - Lab + Guided Micro-Practice

## 0-5 min - Reactivate the Variable Model

Show:

```python
score = 7
score = 9
print("Score:", score)
```

Students predict before Run.

Ask:

**Which value is used by `print()` and why?**

Purpose: reactivate reassignment without reteaching Meeting 1.

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

Do not add exponentiation.

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

## 41-44 min - Bridge Back to Turtle

Show only as a short connection to Unit 2:

```python
import turtle

side = 80

turtle.forward(side)
turtle.right(90)
turtle.forward(side)
turtle.right(90)
turtle.forward(side)
turtle.right(90)
turtle.forward(side)
turtle.right(90)

turtle.done()
```

Ask before Run:

**If `side` changes from 80 to 120, what changes and what stays the same?**

Target insight:

> The variable controls the movement distance; the square structure stays the same.

Do not re-teach Turtle.

---

## 44-45 min - Workflow + Transition

Show:

**Read -> Predict -> Trace -> Run -> Check -> Modify -> Build**

Keep one minute as genuine transition buffer.

---

# 8. Second 45 Minutes - Lab

Use one starter file that evolves through the lab.

## Starter filename

`G7_U3_M2_Arithmetic_Starter.py`

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

## 45-50 min - Open + Read + Predict

Students open the starter.

Do not run yet.

Predict all four output values.

---

## 50-54 min - Run -> Check

Run and compare.

Ask:

- Which operation produced a decimal value?
- Which variables store calculated results?

---

## 54-60 min - Change the Inputs, Not the Formulas

Change only:

```python
a = 20
b = 4
```

Before Run, predict all four new outputs.

Then choose another pair of positive integers and repeat.

Core habit:

**Change inputs -> predict results -> test**

---

## 60-66 min - Make the Program Interactive

Replace the fixed values with:

```python
a = int(input("First number: "))
b = int(input("Second number: "))
```

Keep all calculation and output lines unchanged.

Run with `12` and `5`, then with another pair.

Target insight:

> The algorithm stays the same while the input values change.

---

## 66-72 min - Quotient and Remainder Challenge

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

## 72-76 min - Trace Challenge

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

Expected structure:

```python
items = int(input("How many items? "))
per_pack = int(input("How many items per pack? "))

full_packs = items // per_pack
left_over = items % per_pack

print("Full packs:", full_packs)
print("Left over:", left_over)
```

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

---

# 10. Assessment Evidence

Primary evidence:

- predicted output from the starter
- correct arithmetic results for `+`, `-`, `*`, `/`
- trace table for a calculated variable
- correct interpretation of `//` and `%`
- successful conversion of numeric input
- successful modification without changing formulas
- correct use of a variable as a Turtle movement parameter
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
2. **Teach one-operation expressions first.** Complex precedence problems are unnecessary at this stage.
3. **Teach `//` and `%` through complete groups and leftovers.** This gives both operators a concrete model rather than presenting them as symbols to memorize.
4. **Restrict quotient/remainder examples to positive integers.** Negative floor semantics and division-by-zero handling are outside the Grade 7 scope here.
5. **Keep numeric conversion visible.** `int(input(...))` remains explicit so students do not lose the input-type model from Meeting 1.
6. **Use stored intermediate results.** This supports trace-table work and friendly, readable programs.
7. **Include a very short Turtle bridge.** The official overview mentions variables used with Turtle; this is covered without reopening Unit 2 or adding new Turtle API.
8. **Do not add a separate `math`-module API.** The source names no required functions, while the overview explicitly specifies arithmetic operators, `//`, and `%`. This avoids API scope creep while preserving the stated arithmetic outcomes.
9. **Protect 8 minutes for the final build and bank 3 minutes immediately before it.** If the lesson runs late, shorten earlier modification cycles rather than cutting the Packing Calculator.
10. **Use exactly two inputs in the protected task.** This matches the official practical-assessment direction directly.

---

# 12. Enrichment

Only after the Packing Calculator is complete.

Suitable extensions using the same concepts:

- change the context from packs to teams, trays, or pages
- add a third numeric input and another simple calculation
- use `float` input for a price calculation
- calculate and print an intermediate value for debugging
- use a variable to change the size of the Turtle square

Do not introduce conditions, loops, collections, error handling, or advanced mathematical functions as enrichment.

---

# 13. Required Lesson Assets

- teacher deck in Hebrew
- `G7_U3_M2_Arithmetic_Starter.py`
- student lab brief in Hebrew
- PDF version of the lab brief
- `G7_U3_M2_Packing_Reference_v1.py`
- visual exit-check image A/B/C

---

# 14. Unit 3 Exit Criteria

At the end of Unit 3, a student should be able to:

**choose variables -> receive input -> convert type -> calculate -> trace -> display clear output**

Unit 3 is complete when students can independently solve the Packing Calculator and explain what `//` and `%` produce in that context.
