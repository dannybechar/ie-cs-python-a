# Unit 5.2 — Repetition and Loops

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover Draws in Steps — `range(start, stop, step)` and Turtle (Mission 12)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (26 min guided practice, then 64 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit5_meeting2_range_and_turtle.pptx` (range table, countdown, sequence tasks, `range(2, 10, 2)` bug, polygon angle 360 / n, distance-from-range, countdown from input kept; `t = turtle.Turtle()` replaced by the Unit 2 style)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | why repeat → `for` + `range(n)` → loop variable → trace → running total | 45 / 45 |
| **5.2 (this)** | **`range(start, stop, step)` → countdown → Turtle polygons, spiral, star** | 0 / 90 |
| 5.3 | `while`: condition, update, endless loop, input until valid, sentinel, for vs while | 45 / 45 |
| 5.4 | loops inside loops, rolling execution, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.11–12) | Covered here |
|---|---|
| 5. Write code with bounded repetition | ✅ all tasks |
| Concepts: range, jump size (step), loop variable | ✅ |
| Teaching: `for item in range(start, stop, step)` | ✅ |
| Teaching: draw basic geometric shapes with loops (Turtle) | ✅ polygon, spiral, star |
| Assessment: count how many times a loop runs | ✅ range-value predictions |
| Exam notation: `print(..., end=" ")` / `end=","` — one line of output (ministry deck 12.1, every exam item) | ✅ guided block A |
| A bounded loop with a condition inside: `for` + `if` with `%`, compared with a `range` step (ministry deck 12.1, exam items) | ✅ guided block B |

90 practice minutes of "bounded and conditional repetition".

### Deliberate exclusions
`while` (5.3), nested loops (5.4), `elif` inside loops (5.4, Super Python). Turtle stays in the Unit 2 style: `turtle.forward`, `turtle.right` — no `t = turtle.Turtle()`, no `goto`, no `setheading`.

---

## 3. Lesson Goal

**`range` can start anywhere, jump by any step, and even count down — and the loop variable can drive the drawing.**

---

## 4. Core Mental Models

| Range | Values |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 6)` | 2, 3, 4, 5 |
| `range(1, 10, 3)` | 1, 4, 7 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

- **stop is never included.** To count down, the step is negative.
- **One line of output:** `print(number, end=" ")` keeps the next print on the same line; `end=","` puts a comma after each value. The ministry calls `end` an **attribute (תכונה)** of `print`, not a command; the 5.4 brief also calls it a parameter. A plain `print()` after the loop ends the line.
- **`for` + `if` or a step?** `for number in range(17): if number % 3 == 0: print(number)` and `for number in range(0, 17, 3): print(number)` print the same numbers — two ways to get the multiples.
- **Regular polygon:** n sides, turn `360 / n` each time — the turns add up to one full circle.

---

# 5. First 26 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 12 |
| 1–5 | **Warm-up:** `for i in range(4): print(i + 10)` → predict |
| 5–7 | Answer: 10, 11, 12, 13 (i is 0–3) |
| 7–12 | `range(start, stop, step)`: `range(2, 11, 2)` → 2 4 6 8 10 + the table above |
| 12–16 | **Students:** values of `range(3, 8)`, `range(0, 10, 2)`, `range(10, 3, -2)` |
| 16–18 | Answer: 3 4 5 6 7 · 0 2 4 6 8 · 10 8 6 4 |
| 18–21 | Countdown: `for seconds in range(5, 0, -1)` then `Launch!` |
| 21–25 | Turtle square with `for side in range(4)`; polygon angle `360 / sides` |
| 25–26 | Lab missions |

---

# 6. Lab — 64 Minutes

Starter: [`Ranges_Starter.py`](../exercises/Ranges_Starter.py). Reference: [`Ranges_Reference.py`](solutions/Ranges_Reference.py).

## 26–31 — Guided block A: one line of output (`end`)

Teacher-led, students type along (`numbers_in_a_line()` in the reference). `for number in range(1, 8): print(number, end=" ")` → `1 2 3 4 5 6 7` on one line; then `range(2, 11, 2)` with `end=","`. Ask: what does `print()` do after the loop? (ends the line). Say "תכונה" (attribute) next to "פרמטר". Source: ministry deck 12.1, slides 15–20.

## 31–39 — Guided block B: `for` + `if` with `%`, or a step?

Students predict, then run: "print the multiples of 3 up to 16" two ways — `for number in range(17): if number % 3 == 0: print(number, end=" ")` and `for number in range(0, 17, 3): print(number, end=" ")`. Same output? (yes: `0 3 6 9 12 15`). Then a one-line **7-boom** from 1 to 50: print `Boom` when the number is a multiple of 7, ends with 7, or has 7 as its tens digit — `number % 7 == 0 or number % 10 == 7 or number // 10 == 7` (`seven_boom()`). Warn: `number / 10 == 7` is only true for 70 — use `//`. `%` and `//` come from Unit 3–4. Source: ministry deck 12.1, slides 38–42.

## 39–49 — Task 1: `sequences()`

The starter prints 2, 4, 6, 8 — 10 is missing (`range(2, 10, 2)`). Fix: `range(2, 12, 2)`. Then add a second loop that prints 20, 15, 10, 5 (`range(20, 0, -5)`). Fast finishers: print both lines on one line with `end=" "`.

## 49–61 — Task 2: `polygon()` (Turtle)

Read `sides`; draw a regular polygon with side 80 and turn `360 / sides`. Tests: 3 (triangle), 4 (square), 6 (hexagon). In every test the turtle ends back at the start, facing right.

## 61–73 — Task 3: `spiral()` (Turtle)

`for distance in range(20, 200, 20): turtle.forward(distance); turtle.right(90)` — nine lines, each 20 longer than the one before: a square spiral. The loop variable is the distance. The turtle ends at (100, 80) — outside the spiral, facing down.

## 73–79 — Task 4: `countdown()`

Read a start number, count down to 1, then `Launch!`. Test 7 → 7 … 1, `Launch!`. Then the one-line version with `end=","` → `7,6,5,4,3,2,1,Launch!` (`countdown_line()`).

## 79–83 — Challenge: `star()` (Turtle)

Five lines of 150 with `right(144)` → a five-pointed star, back at the start. Ask: why 144 and not 72? (The turtle turns twice around: 5 × 144 = 720.)

### Tool Note – Thonny
Close the Turtle window before the next run. Answer the `input` question in the Shell before the Turtle window opens.

## 83–85 — Document and save

Save As `G7_U5_M2_Ranges_<Name>.py`.

## 85–90 — Exit check

1. What is the stop in `range(2, 9, 2)`, and is it printed? (9, never)
2. Which step counts down? (a negative one, e.g. `-1`)
3. How much does the turtle turn in a regular hexagon? (60)
4. What does `print(i, end=",")` do differently from `print(i)`? (no new line; a comma after each value)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `range(2, 10, 2)` reaches 10 | stop is excluded — use 12 (or 11) |
| `range(5, 0)` counts down | without a negative step it gives nothing |
| The polygon angle is the inside angle | the turtle turns the outside angle, `360 / n` |
| `range(20, 200, 20)` includes 200 | stops at 180 |
| `end=" "` is a separate command | It belongs inside `print(...)`; `print()` alone ends the line |
| `number / 10 == 7` finds the 70s | Only 70 — use `number // 10 == 7` |

---

# 8. Assessment Evidence (formative)

- Range predictions (official: count how many times a loop runs)
- `polygon()` tested with 3, 4 and 6
- Spiral explained: the loop variable is the distance
- Guided blocks: `for`+`if %` and a `range` step give the same output (official: bounded loop, count rounds)
- Exit check
