# Unit 5.4 — Repetition / Loops

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Loops Inside Loops — Nesting, Rolling Execution and the Unit Checkpoint (Mission 14)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (27 min guided practice, then 63 min lab with the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit5_meeting4_nested_loops.pptx` (while warm-up, row/column trace, X/End prediction, star rectangle and triangle, rotated-squares flower, loop-choice table, multiplication table, `print()` indentation bug kept; the 3×3 grid with `backward` dropped as too advanced; `t = turtle.Turtle()` replaced by the Unit 2 style; a rolling-execution trace added from the official program)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | why repeat → `for` + `range(n)` → loop variable → trace → running total | 45 / 45 |
| 5.2 | `range(start, stop, step)` → countdown → Turtle polygons, spiral, star | 0 / 90 |
| 5.3 | `while` → condition + update → endless loop → input until valid → sentinel → for vs while | 45 / 45 |
| **5.4 (this)** | **loops inside loops → star patterns → rolling execution → Turtle flower → checkpoint** | 0 / 90 |

This meeting closes Unit 5 and holds its **checkpoint** (practical + theoretical), as the official assessment asks.

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.11–12) | Covered here |
|---|---|
| 9. Trace code with rolling repeated execution (ביצוע חוזר מתגלגל) | ✅ slides 8–9, checkpoint B4 |
| Teaching: draw geometric shapes with control structures | ✅ Task 2 (flower) |
| Teaching: practice all of repetition in depth | ✅ |
| Assessment (theory): trace; identify the loop type; count the rounds | ✅ checkpoint B |
| Assessment (practical): a bounded-loop program and a conditional-loop program | ✅ checkpoint A1 (`for`), A2 (`while`) |

With this meeting Unit 5 uses exactly its 360 official minutes (90 theory / 270 practice).

### Source interpretation
**Rolling repeated execution** is taught as a loop where each round uses the result of the round before (`value = value * 2`). Students trace it; they are not asked to invent one.
**Nested loops** are not named in the official concept list, but the official teaching methods ask for shapes and in-depth practice; the rotated-squares flower needs them. `print(..., end="")` is shown only as a tool for star patterns.

### Deliberate exclusions
No `break`, no `+=`, no nesting deeper than two loops, no `backward` / `goto`.

---

## 3. Lesson Goal

**For every round of the outer loop, the inner loop runs all its rounds.**

---

## 4. Core Mental Models

- **Rows and columns:** the outer loop picks a row; the inner loop walks all the columns of that row.
- **Counting:** 3 outer rounds × 4 inner rounds = 12 inner-body runs.
- **`end=""`** keeps printing on the same line; an empty `print()` after the inner loop ends the row.
- **Rolling:** each round starts from the value the previous round left.

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
| 16–20 | Star rectangle: 3 rows × 5 stars with `end=""` and `print()` |
| 20–24 | **Students trace** rolling execution: `value = 1`, 5 rounds of `value = value * 2` |
| 24–26 | Answer: 2, 4, 8, 16, 32 — each round uses the previous value |
| 26–27 | Lab missions |

---

# 6. Lab — 63 Minutes

Starter: [`Nested_Starter.py`](Nested_Starter.py). Reference: [`Nested_Reference.py`](Nested_Reference.py).

## 27–37 — Task 1: star patterns

The starter should print 2 rows of 3 stars but prints six single stars: `print()` is inside the inner loop. Fix → `***` / `***`. Then `patterns()`: a 4 × 6 rectangle of `#`, and a triangle of 1 to 5 stars (`for column in range(row)`).

## 37–49 — Task 2: `flower()` (Turtle)

Eight squares of side 70, turning 45 after each square: the inner loop draws a square, the outer loop turns and repeats. Ask: how many times does `forward` run? (8 × 4 = 32). The turtle ends at the start, facing right.

## 49–72 — Checkpoint A (practical, alone)

- **A1 — bounded loop:** `times_grid()` prints the 1–5 multiplication table (rows `1 2 3 4 5` … `5 10 15 20 25`).
- **A2 — conditional loop:** `count_scores()` reads scores until `-1` and prints how many scores and how many passed (60+). Test 70, 45, 90, −1 → `Scores: 3`, `Passed: 2`.

## 72–82 — Checkpoint B (theory, on paper, no running)

1. What does this print, and how many stars?

```python
for row in range(3):
    for column in range(2):
        print("*", end="")
    print("|")
```

2. How many rounds does `for n in range(10, 0, -3):` run, with which values?
3. `for`, `while` or a loop in a loop? · read an age until it is valid · draw a 12-sided polygon · print 5 rows of 5 stars
4. Rolling: `x = 3`, then 3 rounds of `x = x + x` — the value after each round?

## 82–85 — Checkpoint B answers

1. `**|` three times; 6 stars. 2. 4 rounds: 10, 7, 4, 1. 3. `while` · `for` · a loop in a loop. 4. 6, 12, 24.

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
| Rolling = starting over each round | Each round continues from the previous value |

---

# 8. Assessment Evidence

- Warm-up and nested predictions (formative)
- **Checkpoint A** (practical): `times_grid()` and `count_scores()`
- **Checkpoint B** (theoretical): trace, round counting, loop type, rolling execution
- Exit check
