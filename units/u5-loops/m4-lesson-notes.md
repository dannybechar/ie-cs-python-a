# Unit 5.4 — Repetition and Loops

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Loops Inside Loops — Nesting, Rolling Execution and the Unit Checkpoint (Mission 14)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (27 min guided practice, then 63 min lab with the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit5_meeting4_nested_loops.pptx` (while warm-up, row/column trace, X/End prediction, star rectangle and triangle, rotated-squares flower, loop-choice table, multiplication table, `print()` indentation bug kept; the 3×3 grid with `backward` dropped as too advanced; `t = turtle.Turtle()` replaced by the Unit 2 style; the flower made an optional take-home; a rolling-condition task, equivalent-loops items and exam-style checkpoint items added from the ministry program)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | why repeat → `for` + `range(n)` → loop variable → trace → running total | 45 / 45 |
| 5.2 | `range(start, stop, step)` → countdown → Turtle polygons, spiral, star | 0 / 90 |
| 5.3 | `while` → condition + update → endless loop → input until valid → sentinel → for vs while | 45 / 45 |
| **5.4 (this)** | **loops inside loops → star patterns → rolling condition (`elif`) inside a loop → checkpoint** | 0 / 90 |

This meeting closes Unit 5 and holds its **checkpoint** (practical + theoretical), as the official assessment asks.

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.11–12) | Covered here |
|---|---|
| 9. Trace code with rolling repeated execution (ביצוע חוזר מתגלגל) | ✅ Task 2 Super Python (a `for` loop with a rolling `elif` condition), checkpoint B |
| Teaching: draw geometric shapes with control structures | ✅ covered in 5.2 (polygon, spiral, star); the nested-loop flower is an optional take-home |
| Teaching: practice all of repetition in depth | ✅ |
| Assessment (theory): trace; identify the loop type; count the rounds | ✅ checkpoint B (adds exam-style items: equivalent loops, fill the blank, purpose of a loop, finite or endless) |
| Assessment (practical): a bounded-loop program and a conditional-loop program | ✅ checkpoint A1 (`for`), A2 (`while`) |

With this meeting Unit 5 uses exactly its 360 official minutes (90 theory / 270 practice).

### Source interpretation
**"Rolling" (מתגלגל)** — in the ministry folder the word always means the rolling condition, the `elif` chain (Unit 4.3; python-a.pdf p.4 lists both "rolling conditional statement" and "rolling repeated execution"). Folder meeting 12.3 puts it inside a `for` loop ("Super Python": ten scores, ranges, counts per type). So here goal 9 is covered by **Task 2**: a loop whose body is a rolling `elif` chain. The earlier reading ("each round continues from the previous value", `value = value * 2`) is kept only as a tracing exercise and is now called **"the value carries over from round to round"**, not "rolling". Open point for the supervisor: which reading the exam intends; the folder supports the `elif` reading.
**Nested loops** are not named in the official concept list; they are kept as a short demo and the star patterns (official teaching: shapes with control structures). `print(..., end="")` was introduced in 5.2; here it builds rows. The ministry calls `end` an attribute (תכונה) of `print`.

### Deliberate exclusions
No `break`, no nesting deeper than two loops, no `backward` / `goto`. `+=` and `elif` may be used (taught in 5.1 and 4.3); `+=` stays recognition, long form first. The Turtle flower is not done in class (optional take-home, `flower()` in the reference).

---

## 3. Lesson Goal

**For every round of the outer loop, the inner loop runs all its rounds.**

---

## 4. Core Mental Models

- **Rows and columns:** the outer loop picks a row; the inner loop walks all the columns of that row.
- **Counting:** 3 outer rounds × 4 inner rounds = 12 inner-body runs.
- **`end=""`** keeps printing on the same line; an empty `print()` after the inner loop ends the row.
- **Rolling condition:** the `elif` chain checks the ranges in order; the first one that is `True` wins, the rest are skipped. Inside a `for`, the chain runs once per round.
- **The value carries over:** each round starts from the value the previous round left (tracing only).

---

# 5. First 27 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 14 |
| 1–4 | **Warm-up:** `count = 4`, `while count > 0: print(count); count = count - 2` |
| 4–6 | Answer: 4, 2 — then `count` is 0, the condition is `False` |
| 6–11 | Loop in a loop: `row` / `column` with `range(2)` each → `0 0`, `0 1`, `1 0`, `1 1` (trace table) |
| 11–14 | **Predict:** how many `X` and how many `End`? (`range(2)` × `range(3)`) |
| 14–16 | Answer: `X` 6 times, `End` 2 times |
| 16–19 | Star rectangle: 3 rows × 5 stars with `end=""` (from 5.2) and `print()` |
| 19–23 | **Students trace** how the value carries over: `value = 1`, 5 rounds of `value = value * 2` → 2, 4, 8, 16, 32 — each round uses the previous value |
| 23–26 | A rolling condition in a loop: `for` over three scores with `if score >= 90: print("Super")`, `elif score >= 78: print("Good")`, `else: print("Pass")` — only one branch per round (revision of 4.3; prepares Task 2) |
| 26–27 | Lab missions |

---

# 6. Lab — 63 Minutes

Starter: [`Nested_Starter.py`](exercises/Nested_Starter.py). Reference: [`Nested_Reference.py`](solutions/Nested_Reference.py).

## 27–33 — Task 1: star patterns

The starter should print 2 rows of 3 stars but prints six single stars: `print()` is inside the inner loop. Fix → `***` / `***`. Then `patterns()`: a 4 × 6 rectangle of `#`; the triangle of 1 to 5 stars (`for column in range(row)`) is for whoever finishes early.

## 33–45 — Task 2: Super Python (a `for` loop with a rolling condition)

`super_python()`: read the scores of 10 students (`for student in range(10)`). For each score print its level with an `elif` chain: 90 and up `Super`, 78–89 `Good`, 55–77 `Pass`, below 55 `Fail`. At the end print how many `Super` and how many `Fail` there were. Challenge: the average of the `Super` scores (guard against zero Supers). Test: 95, 80, 60, 40, 91, 78, 55, 54, 100, 20 → `Super: 3`, `Fail: 3`, average 95.33…. Adapted from the ministry's guided task 12.3. Optional take-home: the Turtle `flower()` (eight squares of side 70, turning 45; `forward` runs 8 × 4 = 32 times).

## 45–68 — Checkpoint A (practical, alone)

- **A1 — bounded loop:** `times_grid()` prints the 1–5 multiplication table (rows `1 2 3 4 5` … `5 10 15 20 25`).
- **A2 — conditional loop:** `count_scores()` reads scores until `-1` and prints how many scores and how many passed (60+). Test 70, 45, 90, −1 → `Scores: 3`, `Passed: 2`.

## 68–82 — Checkpoint B (theory, on paper, no running)

Exam-style items (the ministry's exam preparation uses the same types: trace, equivalent loops, fill the blank, purpose, finite or endless).

1. What does this print, and how many stars?

```python
for row in range(3):
    for column in range(2):
        print("*", end="")
    print("|")
```

2. How many rounds does `for n in range(10, 0, -3):` run, with which values?
3. **Equivalent loops:** which `while` loop prints the same as each `for` loop?
   - `for` A: `for item in range(2, 10, 2): print(item)`
   - `for` B: `for item in range(1, 4): print(item)`
   - `while` 1: `i = 1`, `while i <= 4: print(i); i += 1`
   - `while` 2: `i = 2`, `while i < 10: print(i); i += 2`
   - `while` 3: `i = 1`, `while i < 4: print(i); i += 1`
4. **Purpose:** what does this print, and what is the purpose of the code?
   `total = 0` · `for number in range(1, 10):` · `if number % 2 == 1:` · `total += number` · `print(total)` (the last line is outside the loop)
5. **Fill the blanks:** `for item in range(6, ___, ___): print(item, end=" ")` must print `6 4 2`.
6. **Carried value:** `x = 3`, then 3 rounds of `x = x + x` — the value after each round?
7. **Finite or endless?** `i = 1`, `while i != 6: print(i); i += 2` — and say why.

Suggested pace: 1 (2 min) · 2 (1) · 3 (3) · 4 (2) · 5 (2) · 6 (2) · 7 (2).

## 82–85 — Checkpoint B answers

1. `**|` three times; 6 stars. 2. 4 rounds: 10, 7, 4, 1. 3. A with `while` 2 (2 4 6 8); B with `while` 3 (1 2 3); `while` 1 prints 1 2 3 4, so it matches neither. 4. 25 — the sum of the odd numbers from 1 to 9. 5. `range(6, 1, -2)` (stop 0 also works; stop 2 would lose the 2). 6. 6, 12, 24. 7. Endless: 1, 3, 5, 7 … the value 6 is never reached, so the condition stays `True`.

## 85–87 — Document and save

Save As `G7_U5_M4_Nested_<Name>.py`.

## 87–90 — Exit check

1. How do you count the inner-body runs of two loops? (outer rounds × inner rounds)
2. When do you choose `while`? (when the end depends on a condition, not a known count)
3. What makes sure a loop ends? (something in the body moves the condition toward `False`)

### Tool Note – Thonny
Close the Turtle window before the next run.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `print()` inside the inner loop | It ends the row — put it after the inner loop, in the outer body |
| The inner loop runs once in total | It runs fully for every outer round |
| 3 × 4 loops print 7 times | Multiply: 12 |
| In the triangle every row has the same length | `range(row)` grows with the row |
| Rolling condition = checks every branch | The first `True` branch wins, the later `elif` branches are skipped |
| The value is reset every round | Each round continues from the previous value (when the variable is set before the loop) |
| `while i != 6` with step 2 stops at 6 | It jumps over 6 and never ends — prefer `<` or `<=` |

---

# 8. Assessment Evidence

- Warm-up and nested predictions (formative)
- **Checkpoint A** (practical): `times_grid()` and `count_scores()`
- Super Python (goal 9: a loop with a rolling condition)
- **Checkpoint B** (theoretical): trace, round counting, equivalent loops, purpose, fill the blank, finite or endless
- Exit check

---

# 9. Homework and Exam Preparation (ministry meeting 18)

The ministry has a 90-minute exam-preparation meeting on conditions and loops (exercise set 18.1, submission sheet 18.2, second worksheet 18.3). The repo has no free meeting for it and no spare minutes, so it is covered in two ways, both at **zero class minutes**:

1. **Checkpoint B above** is already written in the same item types (the Unit 4.3 checkpoint B holds the conditions side).
2. **Homework after 5.4, on paper, no running** (the ministry says to solve these on paper). Repeat the same set a few weeks before the exam. Source files: `docs/ministry-program/extracts/materials-m18-1-88ee0a.md`, `classwork-m18-2-41ab22.md`, `classwork-m18-3-875584.md`.

| Ministry item | Skill | Status after Unit 5 |
|---|---|---|
| 18.1 #4, #5, #7 | output of a `for` with `if` and `%`, `range` with a step | assign (5.2 guided block B) |
| 18.1 #6 | `+=` accumulator; state the purpose | assign (5.1 `+=`, 5.4 CP-B item 4) |
| 18.1 #8 | fill the blanks of `range` and of a `while` update | assign; **correct (ג) is `range(6, 1, -2)`** — the ministry solution slide prints `6 5 4 3 2` |
| 18.1 #9 | match equivalent loops | assign (5.4 CP-B item 3) |
| 18.1 #10 | `while` output with `+=`, `-=`, final values | assign (5.3) |
| 18.1 #1, #2, #3 | conditions: order two numbers, find input, `%` and `//` in conditions | after Unit 4 (4.3 side; `%` and `//` conditions are Unit 4). Parts of #1 (swap by arithmetic) are optional |
| 18.1 #11 (perfect number), #12 (ID digit positions) | divisor loop; digit loop with a flag | optional challenge. #12 needs `range(1, 10)` to print `1 3 4` (the ministry slide with `range(0, 10)` is wrong) |
| 18.3 #1 | six even/odd solutions | after 4.3 (`elif`) |
| 18.3 #2a | `range(-5, 0, 1)` output | assign |
| 18.3 #2b | `for ... else` | **do not assign** — not taught in the course or in the folder extracts read; confirm it is in scope first |
| 18.3 #3 | reverse a number with `% 10` and `// 10` | optional challenge (after 5.3 `digit_sum()`) |

More take-home practice with source references (no class minutes): [`exercises/Extra_Practice_Unit5.md`](exercises/Extra_Practice_Unit5.md).
