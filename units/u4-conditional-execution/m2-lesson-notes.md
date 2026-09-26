# G7 Unit 4 Meeting 2 Lesson Strategy v1

## Grade 7 / Python A
### Unit 4 — Conditional Execution
### Meeting 2 — The Rover Decides: `if` and `if/else` (Mission 9)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `chapter4_session2_if_else_ready_v2.pptx` (warm-up, examples, error lab, delivery trace and discount challenge kept; lab time added)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| M1 | comparisons → True/False → and/or → truth tables → order | 45 / 45 |
| **M2 (this)** | **`if` → false skips → indentation → `if/else` → input filter → errors** | 45 / 45 |
| M3 | compound conditions in `if`, one-level nesting, Turtle, checkpoint | 0 / 90 |

M1 built the questions (`True`/`False`). M2 lets the answer **choose what runs**. `and` appears only inside the range check of the input filter, exactly as in M1 (`x >= 1 and x <= 10`); compound conditions are the focus of M3.

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 4 (python-a.pdf p.10):

| Official goal / concept | Covered here |
|---|---|
| 1. Program with a simple condition (`if…else`) | ✅ |
| Concepts: simple condition, branches | ✅ `if` body, `else` body, exactly one branch runs |
| Concepts: input validity, simple input filter | ✅ age 0–120 demo, battery 0–100 task (classify only, no re-asking) |
| Teaching method: verbal algorithms and code; trace tables | ✅ sentence → condition; delivery trace table |
| Assessment: tracing which branch was chosen | ✅ warm-up, exit check |

Official topic and minutes used: "conditional statements" (45 theory + 45 practice). The topic's remaining 45 practice minutes are used in M3.

### Deliberate exclusions
No `elif` (not in the official concept list — optional extension in M3 at most), no nesting (M3), no `not`, no loops, no re-asking for input.

---

## 3. Lesson Goal

**The answer to a question decides which lines run.**

Core workflow: **Read → Predict → Run → Check → Fix**

---

## 4. Student-Facing Objectives

1. Write an `if` with a condition, a colon and an indented body.
2. Explain that a `False` condition skips the body, and that unindented lines always run.
3. Use `if/else` and explain that exactly one branch runs.
4. Test the boundary (`>=` includes the boundary value).
5. Check even/odd with `% 2 == 0`.
6. Write a simple input filter that prints valid / invalid.
7. Read and fix the three common errors: `=` instead of `==`, a missing colon, missing indentation.

---

## 5. Core Mental Models

### The fork in the road
The condition is the question from M1. `True` → the rover takes the `if` road. `False` → it takes the `else` road (or skips, if there is no `else`). Then both roads meet again.

### Indentation is the fence
The indented lines under `if:` are **inside** the fence. The first unindented line is outside and always runs.

```python
age = int(input("Age: "))
if age >= 12:
    print("You may enter")
print("Program finished")
```

### Exactly one branch
In `if/else`, every run executes the `if` body **or** the `else` body — never both, never neither.

### Three common errors (Python 3.14 messages)

| Mistake | Message |
|---|---|
| `if score = 100:` | `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` |
| `if score == 100` (no colon) | `SyntaxError: expected ':'` |
| body not indented | `IndentationError: expected an indented block after 'if' statement on line 3` |

Students do not learn `:=`; tell them to read the "Maybe you meant `==`" part.

---

# 6. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 9, the rover decides |
| 1–7 | **Warm-up (predict):** `is_teen = age >= 12 and age <= 18` for age 11, 12, 18, 19 → `False`, `True`, `True`, `False`. Boundaries are included because of `>=` / `<=` |
| 7–12 | `if` structure: condition, colon, indented body; `print("Program finished")` is outside and always runs |
| 12–16 | **Predict:** `temperature = 18`, `if temperature > 25:` → only `Current temperature: 18`. A false condition skips the body |
| 16–21 | **Students trace:** `score >= 80` → `Excellent`, then `Done`, for 90 and for 70. Mark each line "runs / skipped" |
| 21–25 | `if/else`: one road out of two. Age check: `You may enter` / `You are too young`, then `Check completed` always |
| 25–30 | **Predict:** even/odd with `number % 2 == 0` for 7 and 12 → `Odd`, `Even` |
| 30–34 | Simple input filter: age 0–120 → `Valid age` / `Invalid age` for 25, −3, 130. It classifies; it does not ask again |
| 34–38 | Three common errors and their messages (table above). "Read the error, fix one thing, run again" |
| 38–43 | **Predict:** indentation decides — two programs that differ only in the indentation of `print("Well done")`, `score = 70` → A: `Done` · B: `Well done`, `Done` |
| 43–45 | Transition to the lab; one function per task, one active call |

All outputs and error messages checked in Python 3.14.

### Tool Note – Thonny
After `if ...:` and Enter, Thonny indents the next line automatically (4 spaces). To leave the `if` body, press Backspace once. Thonny shows the error in the Shell and highlights the line.

---

# 7. Second 45 Minutes — Lab

Starters: [`Decisions_Starter.py`](Decisions_Starter.py), [`ScoreBug_Starter.py`](ScoreBug_Starter.py). Reference: [`Decisions_Reference.py`](Decisions_Reference.py).

## 45–52 — Warm-up: delivery trace (question only, then run)

```python
# Rover delivery: which branch runs?
amount = 49

if amount >= 50:
    print("Free delivery")
else:
    print("Delivery fee")

print("Order saved")
```

Students fill the trace table for 49, 50 and 80, then change `amount` and run each one:

| amount | `amount >= 50` | Output |
|---|---|---|
| 49 | False | `Delivery fee`, `Order saved` |
| 50 | True | `Free delivery`, `Order saved` |
| 80 | True | `Free delivery`, `Order saved` |

50 is included because of `>=`.

## 52–60 — Task 1: pass or try again

Function `grade_check()`: reads a score and prints `Passed` (60 and up) or `Try again`. Test the boundary: 59 → `Try again`, 60 → `Passed`, 61 → `Passed`.

## 60–70 — Task 2: fix the bugs

Open `ScoreBug_Starter.py`:

```python
# This program has bugs. Run it, read the error, fix ONE bug, run again.
score = int(input("Score: "))
if score = 100
print("Perfect")
else:
print("Not perfect")
```

Fix one bug per run. The messages appear in this order:

1. `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` → `==`
2. `SyntaxError: expected ':'` → add `:`
3. `IndentationError: expected an indented block after 'if' statement on line 3` → indent `print("Perfect")`
4. `IndentationError: expected an indented block after 'else' statement on line 5` → indent `print("Not perfect")`

Then copy the fixed lines into a function `perfect_check()` in the main file. Test with 100 and 99.

## 70–78 — Task 3: input filter

Function `battery_filter()`: reads a battery level and prints `Valid battery` if it is from 0 to 100 (inclusive), otherwise `Invalid battery`. Test: −5 → invalid, 0 → valid, 57 → valid, 100 → valid, 101 → invalid.

## 78–83 — Task 4 (challenge): discount

Function `discount()`: reads a price (`float`). From 100 and up, the final price is 10% lower (`price * 0.9`); otherwise it stays the same. Print `Final price: ...`. Tests: 100 → `90.0`, 99.5 → `99.5`, 250 → `225.0`.
Key point: `final_price` gets a value in **both** branches, and is printed once, after the `if/else`.

Students who do not reach Task 4 are not behind — Tasks 1–3 are the core.

## 83–86 — Document and save

One comment above each function; one active call. Save As `G7_U4_M2_Decisions_<Name>.py`.

## 86–90 — Exit check

1. When does the `if` body run? (when the condition is `True`)
2. What does indentation mark? (which lines are inside the `if` / `else`)
3. How many branches of an `if/else` run in one run? (exactly one)

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| `if score = 100:` | `=` puts in; a condition asks with `==` |
| The line after the `if` body is part of it | Only indented lines are inside; the first unindented line always runs |
| Both `if` and `else` can run | Exactly one branch runs |
| `else` needs a condition | `else:` has no condition — it is "everything else" |
| `> 60` for "60 and up" | "and up" includes 60: `>= 60`. Always test the boundary |
| The input filter asks again | Here it only classifies the input (loops come in Unit 5) |
| Fixing all errors at once | Python reports the first error only: fix one, run again |

---

# 9. Assessment Evidence (formative)

- Predictions before running (warm-up, temperature, indentation)
- "Runs / skipped" marks on the traced lines
- Delivery trace table (official teaching method)
- `grade_check()` tested at 59 / 60 / 61
- The four error messages read and fixed one at a time
- `battery_filter()` tested with the five values
- Exit check
