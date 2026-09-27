# Unit 7.1 — Algorithmic Problems

## Grade 7 / Python A · Lesson Strategy v1
### Topic: How Many Times? — the Counter Pattern (Mission 19)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit7_meeting1_counters_v2.pptx` (hand-count warm-up, counter structure and trace table, even-number prediction, two counters, the two-bug fix-it, passed grades, the y/n survey kept; the Python lists (`[4, 12, 18]`) replaced by `range` and `input`, because lists are not part of Python A; `count += 1` replaced by `count = count + 1`; a digit-counting task added that reuses Unit 6)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **7.1 (this)** | **counter: start at 0, add 1 when the event happens; two counters** | 0 / 90 |
| 7.2 | accumulator, average (accumulator ÷ counter), minimum and maximum | 0 / 90 |
| 7.3 | `random.randint`, games and simulations, Turtle random walk, unit checkpoint | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 7 (python-a.pdf p.15):

| Official goal / concept | Covered here |
|---|---|
| 1. Write a program based on counting patterns | ✅ Tasks 1–3 |
| 3. Identify a counting pattern from a problem description | ✅ warm-up, exit check |
| 4. A loop with a counting activity | ✅ all tasks |
| Concept: counter (מונה) | ✅ |

Official topic and minutes: "counter" — 90 practice.

### Deliberate exclusions
No lists, no `+=`, no `.count()` (the counter is written by hand, so students see the pattern).

---

## 3. Lesson Goal

**A counter answers "how many times?": it starts at 0 before the loop and grows by 1 only when the event happens.**

---

## 4. Core Mental Models

```python
count = 0                     # 1. start at 0, before the loop
for number in range(1, 21):
    if number % 3 == 0:       # 2. the event
        count = count + 1     # 3. add 1 to the value it already has
print("Count:", count)        # 4. print after the loop
```

- `count = 1` **replaces** the value; `count = count + 1` **adds** to it.
- Two questions → two counters, each with its own start and update.

---

# 5. First 30 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 19 |
| 1–5 | **Warm-up:** how many numbers from 1 to 20 divide by 3? Solve by hand, then say what a program does in each round |
| 5–7 | Answer: 6 (3, 6, 9, 12, 15, 18) — check each number, add 1 only when the condition holds |
| 7–13 | The counter pattern (above) |
| 13–18 | Trace table: `range(1, 7)`, `number % 3 == 0` → count 0, 0, 1, 1, 1, 2 |
| 18–21 | **Predict:** count the even numbers in `range(1, 8)` |
| 21–23 | Answer: 3 (2, 4, 6) |
| 23–29 | Two counters: even and odd in `range(1, 11)` → `5 5` |
| 29–30 | Lab missions |

---

# 6. Lab — 60 Minutes

Starter: [`Counters_Starter.py`](Counters_Starter.py). Reference: [`Counters_Reference.py`](Counters_Reference.py).

## 30–39 — Warm-up: two bugs

```python
# Warm-up: count the negative numbers. Find two bugs.
negative_count = 1
for i in range(4):
    number = int(input("Number: "))
    if number < 0:
        negative_count = 1
print("Negative:", negative_count)
```

Test −2, 4, −1, 7 → prints 1, should be 2. Bugs: start at 1 (should be 0); `= 1` replaces instead of adding.

## 39–53 — Task 1: `passed_count()`

Read 6 grades; count the grades of 60 and up. Test 70, 45, 90, 60, 30, 85 → `Passed: 4` (60 counts).

## 53–67 — Task 2: `survey()`

Read 8 answers `y`/`n`; count both. Check that the two counters add up to 8. Test y y n y n y y n → `Yes: 5`, `No: 3`.

## 67–81 — Task 3 (challenge): `count_digits()`

Read a text and count its digits: `for char in text` and `char.isnumeric()` from Unit 6. Test `rover-42` → `Digits: 2`.

## 81–84 — Document and save

Save As `G7_U7_M1_Counters_<Name>.py`.

## 84–90 — Exit check

1. Where does a counter start, and where? (0, before the loop)
2. When is it updated? (inside the `if`, when the event happens)
3. What is the difference between `count = 1` and `count = count + 1`? (replaces / adds 1)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The counter starts at 1 | Nothing has been counted yet: 0 |
| `count = 0` inside the loop | It resets every round — put it before |
| `count = 1` adds one | It replaces the value |
| Printing inside the loop | Print once, after the loop |
| 60 is not a pass | `>=` includes 60 |

---

# 8. Assessment Evidence (formative)

- Trace table and prediction
- Warm-up: both bugs named and fixed
- `survey()` checked: yes + no = 8
- Exit check
