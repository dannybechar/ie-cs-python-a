# Unit 3.1 — Variables, Input/Output & Arithmetic

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover's Memory (Mission 5)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45 — this meeting carries all of Unit 3's official theory time  
**Current tool:** Thonny  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 3

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **3.1 (this)** | **value → variable → type → input → output** | 45 / 45 |
| 3.2 (built) | input → convert → calculate → assign → output | 0 / 90 |

M2 opens by "reactivating the variable model without reteaching Meeting 1". It assumes students already know:
assignment and reassignment (`score = 7`, then `score = 9`), friendly output (`print("Score:", score)`), that `input()` returns text and must be converted with `int(...)` or `float(...)`, and trace tables. M1 teaches exactly these, **without arithmetic** — calculations start in M2.

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 3 (python-a.pdf p.8):

| Official goal / concept | Covered here |
|---|---|
| 1. A basic program with at least one variable (without calculations) | ✅ the rover log, the mission card |
| 2. Receive input into a variable and display its value (without further operations) | ✅ `input` → variable → `print` |
| 3. Choose the variable type that fits the algorithm, initialize and assign a value | ✅ int / float / str / bool, the types detective |
| 4. Basic calculations on input values | ➡️ Meeting 2 |
| Concepts: data, variable | ✅ |
| Concepts: input from the keyboard, a sequence of inputs, correctness of input | ✅ several inputs in a row; `ValueError` when the input doesn't fit the type |
| Concepts: output, friendly output, intermediate output | ✅ `print("Label:", value)`; printing a value midway to check it |
| Concepts: simple types — integer, decimal, string, boolean | ✅ |
| Teaching method: tracing with trace tables | ✅ slide warm-up, lab warm-up, exit check |
| Program overview: variables using Turtle | ✅ Task 3 (closes a course-map gap) |

Official topics and minutes used: "variables and data types" (45 theory + 45 practice); input/output is practiced here and again in M2.

Also closes the Unit 1 gap **compound output** (several values in one `print`): `print("Mission card:", name, "and", rover)`.

### Deliberate exclusions

No arithmetic (M2), no conditions, no loops, no string operations (Unit 6), no f-strings or `+` joining of text and numbers, no input validation beyond *seeing* a `ValueError`.

---

## 3. Lesson Goal

**A variable is a named box that holds one value. The value has a type. `=` puts a value into the box.**

Core workflow: **Read → Predict (trace table) → Run → Check → Fix**

---

## 4. Student-Facing Objectives

Students should be able to:

1. Explain the difference between a value (data) and a variable.
2. Assign a value with `=`, and predict the result of reassignment.
3. Name variables by the rules (English letters, digits, `_`; not starting with a digit; no spaces; case matters).
4. Recognize the four types: `int`, `float`, `str`, `bool`, and check a type with `type(...)`.
5. Write friendly output with several values in one `print`.
6. Receive input into a variable, and explain that `input()` always gives text.
7. Convert input with `int(input(...))` or `float(input(...))`, choosing the type that fits.
8. Fill in a trace table before running.

---

## 5. Core Mental Models

### A variable is a labeled box
The box has a name (`fuel`) and holds one value (`80`). Putting in a new value replaces the old one.

### `=` means "put into", not "equals"
`fuel = 50` reads: "put 50 into the box called fuel". The right side is worked out, then stored in the name on the left.

### A name vs. text
`print(fuel)` prints the value in the box; `print("fuel")` prints the word *fuel*. Quotes make text.

### Every value has a type

| Type | Example | In words |
|---|---|---|
| `int` | `12`, `-3` | whole number (שלם) |
| `float` | `3.5`, `7.0` | decimal number (עשרוני) |
| `str` | `"Dana"`, `"7"` | text (מחרוזת) — anything in quotes |
| `bool` | `True`, `False` | true / false (בוליאני) |

`"7"` is a `str`, not an `int`; `"True"` is a `str`, not a `bool`.

### `input()` always gives text
Even when the user types `12`, `input()` gives the text `"12"`. To get a number: `int(input(...))` or `float(input(...))`.

---

## 5a. The class deck

[`m1-slides-he.pdf`](m1-slides-he.pdf) — 22 slides. Every prediction question is on its own slide, followed by its answer:

| Slides | Section | Timing below |
|---|---|---|
| 1–3 | Title · predict `fuel` / `"fuel"` · answer | 0–5 |
| 4–6 | Data and variables · legal names? · naming rules | 5–12 |
| 7–8 | Trace table (empty) · answer 80 → 50 | 12–17 |
| 9–11 | Four types · card sort · answer | 17–25 |
| 12 | Friendly output | 25–32 |
| 13–15 | Input · "type 12 — what prints?" · answer + `int` / `float` | 32–40 |
| 16 | `ValueError` | 40–45 |
| 17–18 | Rover log (empty table) · answer with types | 45–52 |
| 19 | Tasks 1 and 2 (mission card, types detective) | 52–72 |
| 20 | Task 3 + document and save | 72–86 |
| 21–22 | Exit check · answer | 86–90 |

The deck has no separate "lab missions" overview slide: explain the lab from slide 17 (one function per task, one active call).

---

# 6. First 45 Minutes — Knowledge + Guided Practice

## 0–5 min — Hook: predict

```python
fuel = 80
print(fuel)
print("fuel")
```

Students write the output before running. Expected:

```text
80
fuel
```

Key message: **`fuel` without quotes is a box; `"fuel"` with quotes is text.**

---

## 5–12 min — Data and Variables

- **Data (נתון):** a value — `80`, `"Mars"`.
- **Variable (משתנה):** a named box that holds a value.
- `=` puts a value into the box.

Naming rules, with a quick "legal or not?" round (students answer, then run):

| Name | Legal? | Why |
|---|---|---|
| `fuel` | ✅ | |
| `rover_name` | ✅ | `_` instead of a space |
| `2fuel` | ❌ | `SyntaxError: invalid decimal literal` — can't start with a digit |
| `my fuel` | ❌ | `SyntaxError: invalid syntax` — no spaces |
| `Fuel` vs `fuel` | two different names | case matters |

---

## 12–17 min — Reassignment + the Trace Table (student action)

```python
fuel = 80
fuel = 50
print(fuel)
```

Students fill the trace table **before** running:

| Line | `fuel` | Output |
|---|---|---|
| `fuel = 80` | 80 | |
| `fuel = 50` | 50 | |
| `print(fuel)` | 50 | `50` |

Key message: **a box holds one value; the new value replaces the old one.**

---

## 17–25 min — Four Types (student action: card sort)

Show the four types table. Then pairs sort seven cards into int / float / str / bool:

`7` · `7.0` · `"7"` · `True` · `"True"` · `-3` · `0.5`

Check with `type(...)`:

```python
print(type(7))
print(type("7"))
```

Verified answers: `7` int · `7.0` float · `"7"` str · `True` bool · `"True"` str · `-3` int · `0.5` float.

---

## 25–32 min — Friendly Output

```python
name = "Dana"
age = 12
print("Name:", name, "Age:", age)
```

Output: `Name: Dana Age: 12`

- A comma in `print` separates values and adds a space between them.
- **Friendly output:** a label tells the reader what the value is.
- **Intermediate output:** printing a value in the middle of a program to check it is right.

---

## 32–40 min — Input

```python
name = input("What is your name? ")
print("Hello,", name)
```

Then the key experiment:

```python
age = input("Age: ")
print(type(age))
```

Type `12` → `<class 'str'>`. **Even a number arrives as text.** Convert:

```python
age = int(input("Age: "))
print(type(age))
```

→ `<class 'int'>`. For a decimal (height 1.52): `float(input(...))`.

---

## 40–45 min — Input that doesn't fit + Transition

Run `age = int(input("Age: "))` and type `abc`:

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

Say only: **"The input doesn't fit the type we asked for."** (Typing `12.5` gives the same error: `int` wants a whole number — that's what `float` is for.) This is the official concept "correctness of input".

Explain the lab: one file, one function per task (like Unit 2 Meeting 2), predict before every run.

### Tool Note – Thonny
- `input` waits in the **Shell**: click there and type, then press Enter.
- After `def ...:` and Enter, the next line is indented automatically.

---

# 7. Second 45 Minutes — Lab

Starter file: [`Variables_Starter.py`](Variables_Starter.py). Reference: [`Variables_Reference.py`](Variables_Reference.py).

## 45–52 min — Warm-up: the rover log (trace table)

```python
planet = "Mars"
distance = 225
speed = 3.5
landed = False

print("Planet:", planet)
print("Distance:", distance)
print("Speed:", speed)
print("Landed:", landed)

landed = True
print("Landed:", landed)
```

Before running: fill a trace table (planet, distance, speed, landed, output) and write each variable's type. Then run and check.

Output (verified):

```text
Planet: Mars
Distance: 225
Speed: 3.5
Landed: False
Landed: True
```

Types: `planet` str · `distance` int · `speed` float · `landed` bool.

## 52–62 min — Task 1: Mission card

A function `mission_card()` that asks for the student's name and their rover's name, and prints:

```text
Commander: Dana
Rover: Curiosity
Mission card: Dana and Curiosity
```

The last line uses several values in one `print`.

## 62–72 min — Task 2: Types detective

A function `types_detective()` that asks four questions and stores each in the right type, then prints each value and its type:

| Question | Type | Code |
|---|---|---|
| Age | `int` | `int(input(...))` |
| Height in meters | `float` | `float(input(...))` |
| City | `str` | `input(...)` |
| Number of siblings | `int` | `int(input(...))` |

Ask: **Why is height a `float` and age an `int`?**

## 72–82 min — Task 3: A variable drives the turtle

A function `turtle_square()`: `side = int(input("Side length: "))`, then the Unit 2 square with `turtle.forward(side)` four times.

Predict: **To make the square bigger, how many lines do you change?** (None — just type a different number.)

**If time is short, this is the task to shorten** — show it as a demo instead.

## 82–86 min — Document and save

One comment above each function; only one call active. Save As `G7_U3_M1_Variables_<Name>.py`.

## 86–90 min — Exit check (trace)

```python
x = 5
y = "5"
x = 8
print("x:", x)
print("y:", y)
```

1. What is printed? (`x: 8`, `y: 5`)
2. What is the type of `x`, and of `y`? (`int`, `str`)

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| `=` means "equals" as in math | It means "put into": the value on the right goes into the box on the left |
| A variable keeps all its values | It holds one value; reassignment replaces it |
| `print(fuel)` and `print("fuel")` are the same | Quotes make text; no quotes means "the value in the box" |
| `"7"` is a number | Anything in quotes is a `str` |
| `input()` gives a number when you type a number | `input()` always gives text; convert with `int`/`float` |
| `int` works for 12.5 | `int` is for whole numbers; use `float` |

---

# 9. Assessment Evidence (formative)

- Trace tables filled **before** running (12–17, 45–52, exit check)
- Card sort into the four types
- `mission_card()` with friendly output and several values in one `print`
- `types_detective()` with the right conversion for each input
- `turtle_square()` driven by one variable (or its prediction, if shown as a demo)
- Exit check: output and types

The official theoretical assessment ("trace a simple program") is practiced in the trace tables; the official practical assessment (two values + an arithmetic operation) comes in Meeting 2.

---

# 10. Differentiation

**Support:** a printed trace-table template; type cards with pictures (box of whole numbers / decimal ruler / text bubble / on-off switch).

**Extension (no new syntax):** add a `bool` question to the mission card, e.g. `ready = True`, and print it; or ask for the turtle's pen size as a second variable.
