# Unit 4.3 — Conditional Execution

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover at the Junction — Compound Conditions, Nesting and Turtle (Mission 10)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (27 min guided practice, then 63 min lab with the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `chapter4_session3_compound_conditions_turtle_ready_v2.pptx` (eligibility trace, payment `or`, nested ticket check, "compound can replace nesting", Turtle choice kept; `elif`, `t = turtle.Turtle()` and `setheading` removed)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 4.1 | comparisons → True/False → and/or → truth tables → order | 45 / 45 |
| 4.2 | `if` → false skips → indentation → `if/else` → input filter → errors | 45 / 45 |
| **4.3 (this)** | **`and`/`or` in `if` → one-level nesting → Turtle → checkpoint** | 0 / 90 |

This meeting closes Unit 4 and holds its **checkpoint** (practical + tracing), as the official assessment asks.

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 4 (python-a.pdf p.10):

| Official goal / concept | Covered here |
|---|---|
| 2. Compound conditions (one-level nesting, `and` / `or`) | ✅ warm-up, payment, Task 1, checkpoint |
| Concepts: compound condition, branches, simple input filter | ✅ size filter (Task 2), age filter (checkpoint A) |
| Teaching method: geometric shapes combining conditional execution (Turtle) | ✅ Task 2 |
| Teaching method: trace tables | ✅ nested trace, checkpoint B |
| Assessment: practical — a program with a simple and a compound condition | ✅ checkpoint A |
| Assessment: theoretical — algorithm analysis | ✅ checkpoint B (trace table) |

Official minutes used: the remaining practice of both topics (45 boolean + 45 conditional). With this meeting Unit 4 uses exactly its 270 official minutes.

### Deliberate exclusions
No `elif` (not in the official concept list), no nesting deeper than one level, no `not`, no loops (so the Turtle shapes repeat their lines, as in Unit 2), no `t = turtle.Turtle()`, no `setheading`.

---

## 3. Lesson Goal

**Two questions, one decision: join them with `and` / `or`, or ask the second inside the first.**

Core workflow: **Read → Predict → Run → Check → Fix**

---

## 4. Student-Facing Objectives

1. Use `and` / `or` in an `if` condition.
2. Remember that each side of `or` needs its own comparison.
3. Trace a nested `if`: the inner question is asked only when the outer answer is `True`.
4. Rewrite a nested `if` as one compound condition when both paths lead to the same actions.
5. Let a condition choose what the turtle draws.
6. Pass the checkpoint: write a program with a simple and a compound condition, and trace a nested program.

---

## 5. Core Mental Models

### Two gates or one gate
A nested `if` is two gates in a row: the second is checked only after passing the first. A compound `and` condition is one gate that checks both at once.

```python
# Nested
if age >= 12:
    if has_ticket == "yes":
        print("Enter")

# Compound
if age >= 12 and has_ticket == "yes":
    print("Enter")
```

The two give the same result here. Nesting is needed when each failure gets its own message (`Ticket required` vs `Age requirement not met`).

### Each side of `or` is a full question
`payment == "cash" or payment == "card"` — never `payment == "cash" or "card"` (from 4.1).

---

# 6. First 27 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 10, the rover at the junction |
| 1–7 | **Warm-up (predict):** `if age >= 12 and has_ticket:` → `Approved` / `Not approved` for (14, True), (10, True), (14, False) |
| 7–9 | Answer: only the first is approved; in the others one side of `and` is `False` |
| 9–14 | `or` for several valid options: `payment == "cash" or payment == "card"` → cash, card accepted; coupon not. Warning: each side needs its own comparison |
| 14–19 | **Predict:** nested ticket check for (13, yes), (13, no), (10, yes) |
| 19–21 | Answer: `You may enter` · `Ticket required` · `Age requirement not met`. The inner `if` runs only when `age >= 12` |
| 21–25 | Nested vs compound (code above): same result when there is one shared action |
| 25–27 | Lab missions; one function per task, one active call |

---

# 7. Lab — 63 Minutes

Starter: [`Shapes_Starter.py`](Shapes_Starter.py). Reference: [`Conditions_Reference.py`](Conditions_Reference.py).

## 27–37 — Task 1: may the rover move?

a. Function `rover_move()`: reads `battery` (int) and `obstacle` (`yes`/`no`). Prints `Move forward` only if the battery is at least 20 **and** there is no obstacle; otherwise `Stop`.
b. Function `rover_move_nested()`: the same decision with a nested `if`.

| battery | obstacle | Output (both versions) |
|---|---|---|
| 50 | no | `Move forward` |
| 50 | yes | `Stop` |
| 10 | no | `Stop` |
| 20 | no | `Move forward` |

Ask: **Which version is shorter? Why do both print the same?**

## 37–52 — Task 2: the rover draws by choice (Turtle)

`Shapes_Starter.py` already has the square and triangle lines from Unit 2 — and draws **both**. Students add the conditions and fix the indentation:

1. Draw only if `size` is from 20 to 200 (`and`); otherwise print `Invalid size` (input filter).
2. Inside: `square` → blue square (`right(90)` ×4); anything else → green triangle (`right(120)` ×3).

Tests: `square` 100 → blue square below-right of the start; `triangle` 100 → green triangle pointing down, corners (0, 0), (100, 0), (50, −86.6); `square` 10 → `Invalid size`, no drawing. The turtle ends at the start, facing right.

### Tool Note – Thonny
Answer the `input` questions in the Shell first; the Turtle window opens after them. Close the Turtle window before the next run.

## 52–67 — Checkpoint A (practical, alone)

Function `ticket_price()`: reads an age.
- Less than 0 or more than 120 → `Invalid age`.
- Otherwise: under 12 **or** 65 and up → `Price: 20`; else `Price: 40`.

Tests: −1 → `Invalid age` · 5 → `Price: 20` · 12 → `Price: 40` · 64 → `Price: 40` · 65 → `Price: 20` · 130 → `Invalid age`.
The program contains a simple filter, a compound condition and one-level nesting — the official practical assessment.

## 67–80 — Checkpoint B (tracing, on paper, no running)

```python
fuel = 80
weather = "clear"

if fuel >= 50:
    if weather == "clear" or weather == "cloudy":
        print("Launch")
    else:
        print("Wait for weather")
else:
    print("Refuel")
print("Check done")
```

| fuel | weather | `fuel >= 50` | Output |
|---|---|---|---|
| 80 | clear | True | `Launch`, `Check done` |
| 80 | storm | True | `Wait for weather`, `Check done` |
| 30 | clear | False | `Refuel`, `Check done` |
| 50 | cloudy | True | `Launch`, `Check done` |

10 minutes to fill the table, 3 minutes to check it together.

## 80–84 — Document and save

One comment above each function; one active call. Save As `G7_U4_M3_Conditions_<Name>.py`.

## 84–90 — Exit check

1. When do we use `and`, and when `or`? (`and` — every requirement must hold; `or` — one of several options is enough)
2. In a nested `if`, which condition is checked first? (the outer one; the inner only if the outer is `True`)
3. Write one compound condition for the nested ticket check. (`age >= 12 and has_ticket == "yes"`)

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| `payment == "cash" or "card"` | Each side of `or` needs its own comparison |
| The inner `if` always runs | Only when the outer condition is `True` |
| `and` and `or` are interchangeable | `and` needs all; `or` needs one |
| Nesting and `and` are always the same | Same only when the failures share one action |
| The body of the inner `if` needs the same indentation as the outer | Each level adds 4 spaces |
| Invalid size still draws | The drawing lines must be inside the `if` |

---

# 9. Assessment Evidence

- Warm-up and nested-trace predictions (formative)
- Task 1 both versions agree on the four tests
- Task 2 draws only for valid sizes and the chosen shape
- **Checkpoint A** (practical): `ticket_price()` passes the six tests
- **Checkpoint B** (theoretical): trace table correct
- Exit check
