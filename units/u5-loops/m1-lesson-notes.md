# Unit 5.1 — Repetition / Loops

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover Repeats — Why Loops, `for` and `range` (Mission 11)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit5_meeting1_for_basics.pptx` (Hello ×5 warm-up, `range` boundary task, loop-variable trace, counter and running total, indentation bug kept; `+=` replaced by `x = x + 1`)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **5.1 (this)** | **why repeat → `for` + `range(n)` → loop variable → trace → running total** | 45 / 45 |
| 5.2 | `range(start, stop, step)`, countdown, Turtle polygons and spirals | 0 / 90 |
| 5.3 | `while`: condition, update, endless loop, input until valid, sentinel, for vs while | 45 / 45 |
| 5.4 | loops inside loops, rolling execution, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 5 (python-a.pdf p.11–12):

| Official goal / concept | Covered here |
|---|---|
| 1. Identify problems that need repetition | ✅ warm-up (Hello ×5 → ×100) |
| 5. Write code with bounded repetition | ✅ Tasks 1–3 |
| Concepts: bounded repetition, range, loop variable | ✅ |
| Teaching: neutral pseudo-code "repeat n times" | ✅ slide 3 |
| Teaching: emphasize the loop variable, `for item in range(n)` | ✅ |
| Assessment: trace; count how many times a loop runs | ✅ predictions, trace tables |

Official topics and minutes used: "why repetition" (45 theory) + 45 practice of "bounded and conditional repetition".

### Deliberate exclusions
`range` with a step (5.2), `while` (5.3), nested loops (5.4). No `+=` — the course keeps `total = total + number`.

---

## 3. Lesson Goal

**Describe the action once, and say how many times to repeat it.**

---

## 4. Student-Facing Objectives

1. Recognize repetition in a task and write "repeat n times" as pseudo-code.
2. Write `for i in range(n):` with a colon and an indented body.
3. Predict the values of `range(n)` and `range(start, stop)` — stop is not included.
4. Use the loop variable inside the body.
5. Trace a loop in a table, one row per round.
6. Keep a running total: start before the loop, update inside it.

---

## 5. Core Mental Models

- **The body repeats, the rest runs once.** Indented lines are inside the loop.
- **`range(5)` = 0, 1, 2, 3, 4** — five values, starting at 0, stopping before 5.
- **`range(1, 6)` = 1 … 5** — to include 5, stop at 6.
- **Running total:** `total = 0` before the loop; `total = total + number` inside it; print the final total after it.

---

# 6. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 11 |
| 1–6 | **Warm-up:** print `Hello` five times — two ways. Which is easier to change to 100? |
| 6–10 | Answer: five `print` lines vs `for i in range(5): print("Hello")`. Pseudo-code: "חזור 5 פעמים: הדפס Hello" |
| 10–16 | Structure: `for i in range(4): print("Round", i)` then `print("Finished")` → `Round 0` … `Round 3`, `Finished` |
| 16–19 | **Predict:** `for i in range(3): print(i)` then `print("Go")` |
| 19–22 | Answer: `0 1 2 Go`; `range(5)` stops before 5 |
| 22–26 | **Students:** change `range(5)` so it prints 1 to 5 |
| 26–28 | Answer: `range(1, 6)` |
| 28–35 | Loop variable: `square = number * number` for `range(4)` → 0 0 · 1 1 · 2 4 · 3 9, with a trace table |
| 35–40 | **Students trace** a running total: `total = 0`, `for number in range(1, 5): total = total + number` |
| 40–43 | Answer: total 1, 3, 6, 10; `Final total: 10` |
| 43–45 | Lab missions |

---

# 7. Second 45 Minutes — Lab

Starter: [`Loops_Starter.py`](Loops_Starter.py). Reference: [`Loops_Reference.py`](Loops_Reference.py).

## 45–52 — Warm-up: why only one number?

```python
# Warm-up: why does this print only one number?
for i in range(4):
    value = i * 2
print(value)
```

Predict, then run → `6`. The `print` is outside the loop, so it runs once, after the last round. Fix: indent it → `0 2 4 6`.

## 52–60 — Task 1: `fun_lines()`

Print `Python is fun` six times with the round number from 1: `1 Python is fun` … `6 Python is fun` (`print(i + 1, "Python is fun")`).

## 60–72 — Task 2: `sum_to_n()`

Read `n`; add 1 + 2 + … + n, printing `number = … total = …` each round and `Final total: …` at the end. Tests: 5 → 15, 10 → 55.

## 72–82 — Task 3 (challenge): `times_table()`

Read a number and print its table from 1 to 10: `7 x 1 = 7` … `7 x 10 = 70`.

## 82–85 — Document and save

Save As `G7_U5_M1_Loops_<Name>.py`.

## 85–90 — Exit check

1. Which values does `range(3)` give? (0, 1, 2)
2. What does the indentation mark? (the lines that repeat — the loop body)
3. Where do we set `total = 0`? (before the loop)

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| `range(5)` includes 5 | Stops before 5: 0–4 |
| `range(5)` starts at 1 | Starts at 0 |
| `total = 0` inside the loop | It resets every round — set it before |
| An unindented line repeats | Only the indented body repeats |
| The loop variable must be `i` | Any name: `number`, `side`, `row` |

---

# 9. Assessment Evidence (formative)

- Predictions (warm-up, `range` values, running-total trace)
- Warm-up bug explained and fixed
- `sum_to_n()` tested with 5 and 10
- Exit check
