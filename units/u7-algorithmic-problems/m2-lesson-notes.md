# Unit 7.2 — Algorithmic Problems

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Sum, Average and Extremes — Accumulator, Minimum and Maximum (Mission 20)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (35 min guided practice, then 55 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit7_meeting2_accumulators_min_max_v4.pptx` (counter-or-accumulator warm-up, accumulator trace table, expenses (now the guided example), average = accumulator ÷ counter, the average prediction, maximum with the first value, why not start at 0, lowest and highest grade, the temperatures summary kept; lists replaced by `range` and `input`; `total += value` shown as a recognition-only shorthand after the long form; the lab's Task 1 became the ministry donations task with a `while` loop that stops on a sentinel)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | counter: start at 0, add 1 when the event happens; two counters | 0 / 90 |
| **7.2 (this)** | **accumulator, average (accumulator ÷ counter), minimum and maximum** | 0 / 90 |
| 7.3 | `random.randint`, games and simulations, Turtle random walk, unit checkpoint | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.15) | Covered here |
|---|---|
| 1. Write a program based on accumulating and counting patterns | ✅ Tasks 1, 3 |
| 3. Identify an accumulating, counting, minimum or maximum pattern | ✅ warm-up, exit check |
| 5. A loop that finds a minimum or maximum | ✅ slides 8–10, Tasks 2–3 |
| Concepts: accumulator (צובר), minimum, maximum | ✅ |
| Teaching: combine counter, accumulator, minimum and maximum by condition | ✅ Task 3 |

Official topic and minutes: "accumulator" — 45 practice; minimum and maximum — 45 practice (see the unit plan: the hours table has no separate line for them).

Also covered (Phase 5, `audit-u7.md`): a counter and an accumulator inside a `while` loop that stops on a sentinel value (U7-03, ministry donations task); `+=` as a shorthand (U7-01, teacher ruling D4); the ministry shortcuts `max(a, b, c)` / `min(...)` and `text.count(ch)` as a closing note (U7-11); the success-circle planning questions on the min/max slide (U7-12).

### Deliberate exclusions
No lists. `min()` / `max()` are not used for the stream of inputs: the pattern is written by hand (PDF goal 5), and the shortcut is only named at the end. `+=` is allowed (read it, use it if you like); the long form stays the main form for writing.

---

## 3. Lesson Goal

**An accumulator adds the value itself; a counter adds 1. A minimum or maximum starts from the first real value and changes only when a smaller or bigger one arrives.**

---

## 4. Core Mental Models

| Variable | Role | Start | Update |
|---|---|---|---|
| `count` | counter | 0 | `count = count + 1` |
| `total` | accumulator | 0 | `total = total + value` (shorthand: `total += value`) |
| `minimum` | minimum | the first value | if `value < minimum` |
| `maximum` | maximum | the first value | if `value > maximum` |

- **Average** = `total / count` (a `float`, from Unit 3).
- **Why not `maximum = 0`?** If every value is negative, 0 "wins" although it is not in the data.

---

# 5. First 35 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 20 |
| 1–5 | **Warm-up:** `a = a + 1` and `b = b + value` over `range(1, 4)` — which is a counter, which an accumulator? |
| 5–7 | Answer: `a` counter → 3; `b` accumulator → 6 |
| 7–13 | Accumulator trace table: `range(1, 5)` → total 1, 3, 6, 10 |
| 13–15 | **Shorthand:** `total += value` means `total = total + value`; `count += 1` from 7.1. Recognize it, keep writing the long form |
| 15–20 | Average: 4 grades with a counter and an accumulator (the guided version of `expenses()` with a fixed number of rounds); 80, 70, 90, 100 → 85.0 |
| 20–22 | **Predict** (inputs 6, 10, 8 → total, count, average) and answer: 24, 3, 8.0 |
| 22–29 | Maximum: read the first number before the loop, then 4 more; the six success-circle questions as a checklist for planning |
| 29–32 | **Students:** why not `maximum = 0`? Find an input where it fails |
| 32–34 | Answer: −5, −2, −9, −7, −3 → 0 is printed, but 0 is not in the data |
| 34–35 | Lab missions |

### Minute plan (sums to 90)

| Block | Minutes | Running total |
|---|---:|---:|
| Title + warm-up + answer | 7 | 7 |
| Accumulator trace table | 6 | 13 |
| `+=` shorthand | 2 | 15 |
| Average, guided | 5 | 20 |
| Prediction + answer | 2 | 22 |
| Maximum + success circle | 7 | 29 |
| `maximum = 0` counter-example + answer | 5 | 34 |
| Lab missions | 1 | 35 |
| Warm-up: why 5? | 6 | 41 |
| Task 1: `donations()` (`while`, sentinel) | 15 | 56 |
| Task 2: `min_max()` | 12 | 68 |
| Task 3: `temperatures()` | 16 | 84 |
| Shortcut note: `max`, `min`, `text.count` | 2 | 86 |
| Document and save | 1 | 87 |
| Exit check | 3 | 90 |

Guided practice 0–35 (35), lab 35–90 (55). Net change against the old plan: +7 added (donations `while` 3, `+=` 2, shortcut note 2), offset by shortening the average prediction (−3) and the save and exit slots (−4, save 3 → 1, exit 5 → 3); the success circle (1) and the warm-up (−1) balance each other. Official minutes unchanged: accumulator 45 and min/max 45.

**Deck:** [`m2-slides-he.pdf`](m2-slides-he.pdf) predates these changes. The `+=` shorthand, the donations task (with `while`) and the shortcut note have no slides: show them live until the deck is rebuilt. The `expenses()` slide stays as the guided example.

---

# 6. Lab — 55 Minutes

Starter: [`Accumulators_Starter.py`](exercises/Accumulators_Starter.py). Reference: [`Accumulators_Reference.py`](solutions/Accumulators_Reference.py).

## 35–41 — Warm-up: why 5?

```python
# Warm-up: the total should be 15. Why is it 5?
for value in range(1, 6):
    total = 0
    total = total + value
print("Total:", total)
```

`total = 0` is inside the loop, so it resets every round. Move it before the loop → 15.

## 41–56 — Task 1: `donations()` (a `while` loop with a sentinel)

Read donations until the donation is 0 or negative (the stop signal, not a donation). Print how many donors and the total. Pattern: read the first value before the loop, `while donation > 0`, update the counter and the accumulator, read the next value at the end of the loop. Test 50, 20, 100, 0 → `Donors: 3`, `Total: 170`; test 0 at once → `Donors: 0`, `Total: 0`.

The fixed-count version (`expenses()`: 5 expenses, total and average; test 20, 35, 15, 50, 30 → `Total: 150`, `Average: 30.0`) is the guided example and stays in the reference file. Optional for fast finishers: the average donation (careful: no donors means no division). The card game and storage-space tasks are in the take-home pack.

## 56–68 — Task 2: `min_max()`

Read 6 grades (the first before the loop); print the lowest and the highest. Test 70, 45, 90, 60, 30, 85 → 30, 90.

## 68–84 — Task 3: `temperatures()`

Read 5 temperatures; print the average, the coldest, the hottest, and how many are above 25 (a counter too). Test 22, 28, 31, 19, 25 → 25.0, 19, 31, 2.

## 84–86 — Shortcut note (2 minutes, talk only)

`max(a, b, c)` and `min(a, b, c)` exist and are on the exam formula sheet; they compare values you already have. A stream of inputs still needs the loop pattern. And `text.count(ch)` (Unit 6) is exactly the `count_letter` loop we wrote by hand.

## 86–87 — Document and save

Save As `G7_U7_M2_Accumulators_<Name>.py`.

## 87–90 — Exit check

1. Which variable answers "how many?" (a counter)
2. How does a maximum start? (with the first value)
3. Which two variables make an average? (an accumulator and a counter)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The accumulator adds 1 | It adds the value |
| `total = 0` inside the loop | It resets every round |
| `maximum = 0` always works | Not with negative numbers — start with the first value |
| The first value is read twice | Read it once before the loop, then loop one time fewer |
| `if` / `elif` for minimum and maximum | Two separate `if`s: one value can update both at the start |
| The stop value is counted as a donation | Read it, test it in the `while` condition, and only then count it |
| Forgetting the last `input` inside the `while` | The loop never ends: read the next value at the end of every round |

---

# 8. Assessment Evidence (formative)

- Counter-or-accumulator warm-up
- Average prediction
- The `maximum = 0` counter-example
- `donations()` tested, including a first value of 0
- `temperatures()` tested
- Exit check
