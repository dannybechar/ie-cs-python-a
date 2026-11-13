# Unit 7.1 — Algorithmic Problems

## Grade 7 / Python A · Lesson Strategy v1
### Topic: How Many Times? — the Counter Pattern (Mission 19)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit7_meeting1_counters_v2.pptx` (hand-count warm-up, counter structure and trace table, even-number prediction, two counters, the two-bug fix-it, passed grades, the y/n survey kept; the Python lists (`[4, 12, 18]`) replaced by `range` and `input`, because lists are not part of Python A; `count += 1` kept as a recognition-only shorthand after the long form (Phase 5: teacher ruling, `+=` adopted); a three-way coin counter with `elif` and an invalid-input branch added; the pass mark moved from 60 to 55 to match the ministry items; a digit-counting task added that reuses Unit 6)  
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

Also covered (Phase 5, ministry audit `audit-u7.md`): `elif` for three or more classes (U7-02, teacher ruling D1, first taught in 4.3); `+=` as a shorthand of `x = x + 1` (U7-01, ruling D4, first shown in 5.1 and now reused); an explicit invalid-input branch in the survey (U7-04); the "success circle" planning questions (U7-12); the ministry word **קידום** (counter update) next to "עדכון" (U7-14).

### Deliberate exclusions
No lists and no `.count()` (the counter is written by hand, so students see the pattern). `+=` and `elif` are allowed from this unit on: the **long form stays the main form for writing** (it shows what happens), `+=` is read, recognized and may be used by students who ask for it.

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
- Two questions → two counters, each with its own start and update. Three classes → three counters and `if` / `elif` / `else`.
- Shorthand: `count += 1` is the same as `count = count + 1` (קידום המונה). We write the long form; we can read both.

---

# 5. First 30 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 19 |
| 1–5 | **Warm-up:** how many numbers from 1 to 20 divide by 3? Solve by hand, then say what a program does in each round |
| 5–7 | Answer: 6 (3, 6, 9, 12, 15, 18) — check each number, add 1 only when the condition holds |
| 7–14 | The counter pattern (above), with the **success circle**: what to count, what to keep, what to reset, what to compare, what to read, what to print (one slide, planning checklist) |
| 14–17 | **Shorthand:** `count += 1` means `count = count + 1` (ministry: "כתיבה מקוצרת", **קידום** of the counter). Recognize it, keep writing the long form |
| 17–22 | Trace table: `range(1, 7)`, `number % 3 == 0` → count 0, 0, 1, 1, 1, 2. **Predict** with the same table: the even numbers in `range(1, 8)` → 3 |
| 22–29 | **Three-way counter (coins 1, 5, 10):** three counters, `if` / `elif` / `elif` / `else: print("value not accepted")`. Input 1 5 10 5 2 1 → `2 2 1` and one "value not accepted". Why `elif`: one coin belongs to exactly one class (rolling condition, from 4.3) |
| 29–30 | Lab missions |

### Minute plan (sums to 90)

| Block | Minutes | Running total |
|---|---:|---:|
| Title + warm-up + answer | 7 | 7 |
| Counter pattern + success circle | 7 | 14 |
| `+=` shorthand | 3 | 17 |
| Trace table + prediction (evens in `range(1, 8)`) | 5 | 22 |
| Three-way counter, coins, `elif` | 7 | 29 |
| Lab missions | 1 | 30 |
| Warm-up: two bugs | 9 | 39 |
| Task 1: `passed_count()` (pass mark 55) | 14 | 53 |
| Task 2: `survey()` with an invalid branch | 17 | 70 |
| Task 3 (challenge): `count_digits()` | 11 | 81 |
| Document and save | 3 | 84 |
| Exit check | 6 | 90 |

Guided practice 0–30 (30), lab 30–90 (60). Net change against the old plan: +12 added (`+=` 3, `elif` three-way 5, survey branch 3, checklist 1), offset by merging the even-number prediction into the trace table (−3), replacing the even/odd two-counter demo by the coin counter (−6) and shortening the challenge slot (−3). The "two counters" idea (even and odd) is now covered by the coin demo, which has three.

**Deck:** [`m1-slides-he.pdf`](m1-slides-he.pdf) predates these changes. The success-circle checklist, the `+=` shorthand, the coin counter with `elif`, the pass mark 55 and the three-way survey have no slides: show them live (board or editor) until the deck is rebuilt.

---

---

# 6. Lab — 60 Minutes

Starter: [`Counters_Starter.py`](exercises/Counters_Starter.py). Reference: [`Counters_Reference.py`](solutions/Counters_Reference.py).

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

Read 6 grades; count the grades of 55 and up (the ministry pass mark). Test 70, 45, 90, 55, 30, 85 → `Passed: 4` (55 counts).

## 53–70 — Task 2: `survey()`

Read 8 answers. `y` and `n` are counted; **any other answer is "not valid"**: print `not valid` and count it in a third counter (the round is still used). Use `if` / `elif` / `else`. Check that **the three counters add up to 8**. Tests: y y n y n y y n → `Yes: 5`, `No: 3`, `Not valid: 0`; and y y n x n y Y n → `Yes: 3`, `No: 3`, `Not valid: 2` (`x` and `Y` are not valid; the old version counted them as `n` and the sum check always passed).

## 70–81 — Task 3 (challenge): `count_digits()`

Read a text and count its digits: `for char in text` and `char.isnumeric()` from Unit 6. Test `rover-42` → `Digits: 2`. A challenge: students who finish early continue, the others move on to the save at 81 with a note of where they stopped.

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
| 55 is not a pass | `>=` includes 55 |
| An unexpected answer is `n` | `else` catches everything: use `elif answer == "n"` and keep `else` for "not valid" |
| `if` `if` `if` for three classes | It works, but `elif` says "exactly one class" and stops checking |

---

# 8. Assessment Evidence (formative)

- Trace table and prediction
- Warm-up: both bugs named and fixed
- `survey()` checked: yes + no + not valid = 8, with an invalid answer in the test
- Coin counter with `elif`
- Exit check
