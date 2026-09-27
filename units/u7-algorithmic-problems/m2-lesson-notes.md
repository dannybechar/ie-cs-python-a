# Unit 7.2 — Algorithmic Problems

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Sum, Average and Extremes — Accumulator, Minimum and Maximum (Mission 20)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (35 min guided practice, then 55 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit7_meeting2_accumulators_min_max_v4.pptx` (counter-or-accumulator warm-up, accumulator trace table, expenses, average = accumulator ÷ counter, the average prediction, maximum with the first value, why not start at 0, lowest and highest grade, the temperatures summary kept; lists replaced by `range` and `input`; `+=` replaced by `total = total + value`)  
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

### Deliberate exclusions
No lists, no `+=`, no `min()` / `max()` (the pattern is written by hand).

---

## 3. Lesson Goal

**An accumulator adds the value itself; a counter adds 1. A minimum or maximum starts from the first real value and changes only when a smaller or bigger one arrives.**

---

## 4. Core Mental Models

| Variable | Role | Start | Update |
|---|---|---|---|
| `count` | counter | 0 | `count = count + 1` |
| `total` | accumulator | 0 | `total = total + value` |
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
| 13–18 | Average: 4 grades with a counter and an accumulator; 80, 70, 90, 100 → 85.0 |
| 18–21 | **Predict:** inputs 6, 10, 8 → total, count, average |
| 21–23 | Answer: 24, 3, 8.0 |
| 23–29 | Maximum: read the first number before the loop, then 4 more |
| 29–32 | **Students:** why not `maximum = 0`? Find an input where it fails |
| 32–34 | Answer: −5, −2, −9, −7, −3 → 0 is printed, but 0 is not in the data |
| 34–35 | Lab missions |

---

# 6. Lab — 55 Minutes

Starter: [`Accumulators_Starter.py`](Accumulators_Starter.py). Reference: [`Accumulators_Reference.py`](Accumulators_Reference.py).

## 35–42 — Warm-up: why 5?

```python
# Warm-up: the total should be 15. Why is it 5?
for value in range(1, 6):
    total = 0
    total = total + value
print("Total:", total)
```

`total = 0` is inside the loop, so it resets every round. Move it before the loop → 15.

## 42–54 — Task 1: `expenses()`

Read 5 expenses; print the total and the average. Test 20, 35, 15, 50, 30 → `Total: 150`, `Average: 30.0`.

## 54–66 — Task 2: `min_max()`

Read 6 grades (the first before the loop); print the lowest and the highest. Test 70, 45, 90, 60, 30, 85 → 30, 90.

## 66–82 — Task 3: `temperatures()`

Read 5 temperatures; print the average, the coldest, the hottest, and how many are above 25 (a counter too). Test 22, 28, 31, 19, 25 → 25.0, 19, 31, 2.

## 82–85 — Document and save

Save As `G7_U7_M2_Accumulators_<Name>.py`.

## 85–90 — Exit check

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

---

# 8. Assessment Evidence (formative)

- Counter-or-accumulator warm-up
- Average prediction
- The `maximum = 0` counter-example
- `temperatures()` tested
- Exit check
