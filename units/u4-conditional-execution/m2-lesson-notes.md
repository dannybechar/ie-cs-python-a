# Unit 4.2 — Conditional Execution

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover Decides: `if` and `if/else` (Mission 9)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `chapter4_session2_if_else_ready_v2.pptx` (warm-up, examples, error lab and delivery trace kept; lab time added; digits, `not` and max of two added after the Phase 5 audit; the discount challenge moved to the take-home pack)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 4.1 | comparisons → True/False → and/or → truth tables → order | 45 / 45 |
| **4.2 (this)** | **`if` → false skips → indentation → `if/else` → input filter → errors → digits with `//` and `%` → max of two** | 45 / 45 |
| 4.3 | compound conditions in `if`, one-level nesting, rolling condition (`elif`), Turtle, checkpoint | 0 / 90 |

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
| Ministry classroom folder (meetings 7-8): a condition on a digit of a number (`// 10`, `% 10`), the larger of two numbers, odd with `not` | ✅ digits 3 min (theory) + Task 5 (challenge); max of two = Task 4; `not` inside the even/odd demo |

Official topic and minutes used: "conditional statements" (45 theory + 45 practice). The topic's remaining 45 practice minutes are used in M3.

### Deliberate exclusions
No `elif` (rolling condition: 4.3), no nesting (M3), no loops, no re-asking for input. `not` appears only as the second way to write "odd" (taught in 4.1).

### Terminology bridges (ministry wording)
Before the tasks: a function is called **פעולה** in the exam; a comparison sign is an **אופרטור יחס**; `and`/`or`/`not` are **קשרים לוגיים**. This lesson's condition type is the **תנאי פשוט** (simple condition) with its two roads.

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
5. Check even/odd with `% 2 == 0`, and write "odd" also as `not (number % 2 == 0)`.
6. Write a simple input filter that prints valid / invalid.
7. Read and fix the three common errors: `=` instead of `==`, a missing colon, missing indentation.
8. Split a two-digit number with `// 10` (tens) and `% 10` (ones), and use the digits in a decision.
9. Find the larger of two numbers with `if/else`.

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
| 1–6 | **Warm-up (predict):** `is_teen = age >= 12 and age <= 18` for age 11, 12, 18, 19 → `False`, `True`, `True`, `False`. Boundaries are included because of `>=` / `<=` |
| 6–11 | `if` structure: condition, colon, indented body; `print("Program finished")` is outside and always runs |
| 11–15 | **Predict:** `temperature = 18`, `if temperature > 25:` → only `Current temperature: 18`. A false condition skips the body |
| 15–20 | **Students trace:** `score >= 80` → `Excellent`, then `Done`, for 90 and for 70. Mark each line "runs / skipped" |
| 20–24 | `if/else`: one road out of two. Age check: `You may enter` / `You are too young`, then `Check completed` always |
| 24–29 | **Predict:** even/odd with `number % 2 == 0` for 7 and 12 → `Odd`, `Even`. Odd another way: `not (number % 2 == 0)` is `True` for 7 (1 min, `not` from 4.1) |
| 29–32 | **Digits (new):** for `number = 47`: `number // 10` → `4` (tens), `number % 10` → `7` (ones); students predict 83 and 50. Same `//` and `%` as Unit 3, now feeding a decision (`Decisions_Reference.py`, `two_digits()`) |
| 32–36 | Simple input filter: age 0–120 → `Valid age` / `Invalid age` for 25, −3, 130. It classifies; it does not ask again |
| 36–39 | Three common errors and their messages (table above). "Read the error, fix one thing, run again" |
| 39–44 | **Predict:** indentation decides — two programs that differ only in the indentation of `print("Well done")`, `score = 70` → A: `Done` · B: `Well done`, `Done` |
| 44–45 | Transition to the lab; one function per task, one active call |

All outputs and error messages checked in Python 3.14.

Time ledger (Phase 5): digits +3 min, funded by warm-up −1, transition −1, errors −1. The theory part still sums to 45.

### Tool Note – Thonny
After `if ...:` and Enter, Thonny indents the next line automatically (4 spaces). To leave the `if` body, press Backspace once. Thonny shows the error in the Shell and highlights the line.

---

# 7. Second 45 Minutes — Lab

Starters: [`Decisions_Starter.py`](exercises/Decisions_Starter.py), [`ScoreBug_Starter.py`](exercises/ScoreBug_Starter.py). References: [`Decisions_Reference.py`](solutions/Decisions_Reference.py) (one function per task), [`ScoreBug_Reference.py`](solutions/ScoreBug_Reference.py) (the fixed bug program).

Times below are the Phase 5 plan: 5 + 8 + 8 + 8 + 5 + 5 + 2 + 4 = 45.

## 45–50 — Warm-up: delivery trace (question only, then run)

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

## 50–58 — Task 1: pass or try again

Function `grade_check()`: reads a score and prints `Passed` (60 and up) or `Try again`. Test the boundary: 59 → `Try again`, 60 → `Passed`, 61 → `Passed`.

## 58–66 — Task 2: fix the bugs

Open `ScoreBug_Starter.py`:

```python
# Fix ONE bug per run, then run again.
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

Then copy the fixed lines into a function `perfect_check()` in the main file. Test with 100 and 99. (Teacher: the fixed program alone is `ScoreBug_Reference.py`.)

## 66–74 — Task 3: input filter

Function `battery_filter()`: reads a battery level and prints `Valid battery` if it is from 0 to 100 (inclusive), otherwise `Invalid battery`. Test: −5 → invalid, 0 → valid, 57 → valid, 100 → valid, 101 → invalid.

## 74–79 — Task 4: the larger of two numbers

Function `max_of_two()`: reads two integers and prints `Largest: ...`. Tests: (3, 8) → `8`, (9, 2) → `9`, (5, 5) → `5`. Ask: **What is printed when they are equal? Does it matter?** (Source: ministry 7.0 "המספר המקסימלי".)

## 79–84 — Task 5 (challenge): digits

Function `digits_check()`: reads a two-digit number (10 to 99). Even number → print `Sum: ...` (tens + ones); odd number → print `Product: ...` (tens × ones). Tests: 24 → `Sum: 6`, 35 → `Product: 15`, 10 → `Sum: 1`, 99 → `Product: 81`. (Source: ministry 7.0 #3 "even: sum of digits, else product".)

Students who do not reach Task 5 are not behind — Tasks 1–4 are the core. The discount task (final price assigned in both branches, printed once) moved to the take-home pack.

## 84–86 — Document and save

One comment above each function; one active call. Save As `G7_U4_M2_Decisions_<Name>.py`.

Take-home (0 class minutes): [`exercises/Extra_Practice.md`](exercises/Extra_Practice.md), section 4.2.

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
| `number // 10` is the ones digit | `// 10` is the tens (what is left after dropping the last digit); `% 10` is the ones |

---

# 9. Assessment Evidence (formative)

- Predictions before running (warm-up, temperature, indentation)
- "Runs / skipped" marks on the traced lines
- Delivery trace table (official teaching method)
- `grade_check()` tested at 59 / 60 / 61
- The four error messages read and fixed one at a time
- `battery_filter()` tested with the five values
- `max_of_two()` tested with three pairs; `digits_check()` (challenge)
- Exit check
