# Unit 4.1 — Conditional Execution

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover's Sensors: Boolean Expressions (Mission 8)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `chapter4_session1_boolean_expressions_ready.pptx` (activities kept; lab time added; `not` added after the Phase 5 audit)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **4.1 (this)** | **comparisons → True/False → and/or/not → truth tables → order** | 45 / 45 |
| 4.2 | `if` and `if/else`, indentation, input filter | 45 / 45 |
| 4.3 | compound conditions in `if`, one-level nesting, rolling condition (`elif`), Turtle, checkpoint | 0 / 90 |

M1 builds the boolean language that M2 and M3 put inside `if`. **No `if` yet** — every result is printed as `True` or `False`.

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 4 (python-a.pdf p.10):

| Official goal / concept | Covered here |
|---|---|
| 2. Compound conditions with `and` / `or` | ✅ (inside `if` in M3) |
| Ministry classroom folder (meeting 8): the logical connective `not` | ✅ 5 min (beyond the PDF list; approved Phase 4, D4) |
| 3. Distinguish the order of boolean operations | ✅ arithmetic → comparison → `and` → `or` |
| 4. Build a truth table for a condition, and a condition from a truth table | ✅ lesson + Task 3 |
| Concepts: equality, greater, less, at least, at most, not equal | ✅ `== > < >= <= !=` |
| Concepts: truth table, and, or (and `not`) | ✅ |
| Teaching method: boolean expressions first, as the basis of conditions | ✅ |
| Teaching method: verbal algorithms and code; trace tables | ✅ sentence → expression; warm-up trace |

Official topic and minutes used: "boolean expressions" (45 theory + 45 practice). The topic's remaining 45 practice minutes are used in M3.

### Deliberate exclusions
No `if` (M2), no `elif` (taught in 4.3), no loops, no string methods. `%` and `//` may appear (taught in Unit 3).

### Terminology bridges (ministry wording)
Say the Hebrew terms next to the English words: **אופרטור יחס** (`== != > < >= <=`), **קשר לוגי** (`and or not`), **ביטוי בוליאני**. Gloss once: a function is called **פעולה** in the exam ("כתבו פעולה"). Unit 4 names four kinds of condition: simple, compound, nested, rolling (4.3).

---

## 3. Lesson Goal

**A comparison is a question the program asks. Its answer is always `True` or `False`.**

Core workflow: **Read → Predict → Run → Check → Fix**

---

## 4. Student-Facing Objectives

1. Use `== != > < >= <=` and predict the `True`/`False` result.
2. Explain the difference between `=` (put into) and `==` (is it equal?).
3. Store a comparison result in a variable (type `bool`).
4. Compare strings, knowing that capital letters matter and `5` is not `"5"`.
5. Fill the truth tables of `and` and `or`, and recognize a condition from its truth table.
6. Predict the order: arithmetic, then comparisons, then `not`, `and`, `or`.
7. Convert input before comparing it with a number.
8. Use `not` to flip a result, and rewrite `not (x > 5)` as `x <= 5`.

---

## 5. Core Mental Models

### A comparison gives a `bool`
`age >= 12` is not an instruction; it is a question with the answer `True` or `False`.

### `=` vs `==`
`=` puts a value into a box (Unit 3). `==` asks "are these equal?".

| Operator | Question | Example (age = 13) |
|---|---|---|
| `==` | equal? | `age == 15` → `False` |
| `!=` | not equal? | `age != 10` → `True` |
| `>` / `<` | greater / less? | `age > 13` → `False` |
| `>=` / `<=` | at least / at most? | `age >= 12` → `True` |

### `and` / `or`
`and` is `True` only when **both** sides are `True`. `or` is `True` when **at least one** side is `True`.

| `A` | `B` | `A and B` | `A or B` |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

### `not`
`not` flips the answer: `not True` is `False`, `not False` is `True`. `not (age >= 12)` means the same as `age < 12`. Use parentheses around the question: `not (x % 2 == 0)`.

| `A` | `not A` |
|---|---|
| True | False |
| False | True |

### Order
Arithmetic first, then comparisons, then `not`, then `and`, then `or`. Parentheses make the order visible.

---

# 6. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–5 | **Predict** (hook): `age = 13`, `print(age >= 12)`, `print(age == 15)`, `print(age != 10)` → `True`, `False`, `True`. What type is the result? (`bool`, from Unit 3) |
| 5–12 | The six comparison operators (table above). `=` vs `==`. `score = 82`, `passed = score >= 60` → `True`: a comparison result can be stored |
| 12–17 | **Students:** sentence → expression, in pairs: age at least 12 · price less than 50 · name not Dana · score exactly 100 → `age >= 12` · `price < 50` · `name != "Dana"` · `score == 100` |
| 17–20 | Strings: `"python" == "Python"` → `False` (capitals matter); `5 == "5"` → `False` (a number is not text) |
| 20–28 | `and` / `or` with a sensor story: the rover drives only if it **has fuel and** its battery is OK; it stops if there is **a rock or** a hole. **Students** fill the empty truth table, then check |
| 28–34 | Compound conditions: `age = 14`, `has_ticket = True`, `can_enter = age >= 12 and has_ticket` → `True`; `day = "Saturday"`, `day == "Friday" or day == "Saturday"` → `True` |
| 34–39 | Order: `price = 30`, `quantity = 2`, `has_coupon = False`, `price * quantity <= 70 or has_coupon` → `True`; `True or False and False` → `True` (`and` first); with parentheses `(True or False) and False` → `False` |
| 39–44 | **`not`** (new): the two-row table; **students predict** `x = 8`: `not (x > 5)` → `False`, `not (x % 2 == 0)` → `False`; `not (x > 5)` equals `x <= 5`; `not` binds before `and` (`not False and False` → `False`). Demo: `Booleans_Reference.py`, `not_demo()` |
| 44–45 | Transition to the lab; one function per task, one active call |

Time ledger (Phase 5): `not` +5 min, funded by strings −2, order −2, transition −1. The theory part still sums to 45.

### Tool Note – Thonny
`True` and `False` are shown in the Shell without quotes — they are `bool`, not text.

---

# 7. Second 45 Minutes — Lab

Starter: [`Booleans_Starter.py`](../exercises/Booleans_Starter.py). Reference: [`Booleans_Reference.py`](solutions/Booleans_Reference.py).

## 45–52 — Warm-up: trace (question only, then run) — 4 min + 3 min

```python
x = 8

a = x > 5
b = x < 10
c = a and b
d = x > 10 or x < 0

print(a, b, c, d)
```

Students fill a trace table (`a`, `b`, `c`, `d`) before running (4 min). Output: `True True True False`.

Then a 3-minute exam-style predict (ministry exam preparation, meeting 17 #3): `counter = 0`, `print(counter == 5)`, `counter = counter + 1`, `print("Hello!")` → `False`, `Hello!` (a comparison printed; `counter` changes by self-update from Unit 3).

## 52–62 — Task 1: sensor check

A function `sensor_check()` that reads a temperature and prints:

```text
Freezing: ...
Safe range: ...
```

`Freezing` = `temperature < 0`; `Safe range` = `temperature >= -20 and temperature <= 40`. Test with −5, 0, 25, 45:

| temperature | Freezing | Safe range |
|---|---|---|
| −5 | True | True |
| 0 | False | True |
| 25 | False | True |
| 45 | False | False |

## 62–72 — Task 2: fix the bug

```python
score = input("Score: ")
passed = score >= 60
print("Passed:", passed)
```

Error: `TypeError: '>=' not supported between instances of 'str' and 'int'`. The fix: `score = int(input("Score: "))`. Ask: **What was the type of `score` before the fix?** (`str`)

## 72–82 — Task 3: truth tables both ways

1. Build the truth table of `has_fuel and battery_ok` in code: four `print` lines, changing the two variables between them (see the reference).
2. The other direction — given this table, which condition is it?

| A | B | ? |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

Answer: `A or B`.

## 82–86 — Document and save

One comment above each function; one active call. Save As `G7_U4_M1_Booleans_<Name>.py`.

Take-home (0 class minutes): [`exercises/Extra_Practice.md`](../exercises/Extra_Practice.md), section 4.1.

## 86–90 — Exit check

1. What is the difference between `=` and `==`?
2. When is `A and B` `True`?
3. Write a condition for "x is between 1 and 10, including both": `x >= 1 and x <= 10`.

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| `=` and `==` are the same | `=` puts into a box; `==` asks a question |
| `True` is text | It is a `bool` — no quotes |
| `"python" == "Python"` | Capitals matter: `False` |
| `day == "Friday" or "Saturday"` checks both days | Each side of `or` needs its own comparison: `day == "Friday" or day == "Saturday"` |
| `and` means "one of them" | `and` needs both; `or` needs at least one |
| Comparing `input()` with a number works | `input()` gives text; convert with `int(...)` first |
| `not x > 5` needs no care | Write `not (x > 5)`; `not` flips the whole question in the parentheses |

---

# 9. Assessment Evidence (formative)

- Predictions before running (hook, warm-up trace)
- Sentence → expression in pairs
- Truth tables filled before checking; the condition identified from a table (official goal 4)
- `not` predictions (theory 39–44)
- `sensor_check()` tested with the four values
- The bug explained and fixed
- Exit check
