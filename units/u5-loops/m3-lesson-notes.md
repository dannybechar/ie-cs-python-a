# Unit 5.3 — Repetition and Loops

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Until the Job Is Done — the `while` Loop (Mission 13)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit5_meeting3_while.pptx` (while structure and trace, prediction, missing update, input until valid, sentinel, password, sum until 0, for vs while table, correctness kept; `+=` replaced by `x = x + 1`)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | why repeat → `for` + `range(n)` → loop variable → trace → running total | 45 / 45 |
| 5.2 | `range(start, stop, step)` → countdown → Turtle polygons, spiral, star | 0 / 90 |
| **5.3 (this)** | **`while` → condition + update → endless loop → input until valid → sentinel → for vs while** | 45 / 45 |
| 5.4 | loops inside loops, rolling execution, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.11–12) | Covered here |
|---|---|
| 2. Tell a known-length loop from a conditional loop | ✅ for vs while table, exit check |
| 3. Explain the need for a loop's stop condition | ✅ endless loop, warm-up |
| 4. Explain the correctness of a loop algorithm | ✅ correctness slide |
| 6. Write code with conditional repetition | ✅ Tasks 1–3 |
| 7. Explain the differences between bounded and conditional loops | ✅ |
| 8. A conditional loop whose stop depends on a variable | ✅ Task 3 (`battery`) |
| Teaching: a loop may never end; correctness = the goal holds at the end, and the loop ends | ✅ |

45 theory minutes of "bounded and conditional repetition" + 45 practice minutes.

### Deliberate exclusions
`break`, `while True`, `+=`, nested loops (5.4).

---

## 3. Lesson Goal

**`while` repeats as long as its condition is `True` — something inside the loop must bring it closer to `False`.**

---

## 4. Core Mental Models

Every `while` loop has three parts:

```python
count = 1              # 1. start value (before the loop)
while count <= 5:      # 2. condition (checked before every round)
    print(count)
    count = count + 1  # 3. update (moves toward the end)
print("Finished")
```

- The last check, which gives `False`, is part of the trace too.
- No update → the condition stays `True` → the program never stops.
- **Input until valid / sentinel:** read once before the loop, and again at the end of the body.
- **Choosing:** the number of rounds is known before starting → `for`; the end depends on a condition → `while`.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 13 |
| 1–5 | **Warm-up:** write a `for` that prints 3, 6, 9, 12 |
| 5–7 | Answer: `range(3, 15, 3)` |
| 7–13 | Pseudo-code "כל עוד … בצע" and the `while` structure (above) |
| 13–18 | Trace table for `count <= 3`: checks 1–3 `True`, check 4 `False` — no round |
| 18–22 | **Predict:** `x = 2`, `while x < 10: print(x); x = x + 3` → output and final `x` |
| 22–24 | Answer: 2, 5, 8; `x` is 11 |
| 24–29 | Endless loop: the update is missing → `1 1 1 …`. How to stop it (Tool Note) |
| 29–34 | Input until valid: age 0–120, asks again (Unit 4.2 only classified) |
| 34–40 | Sentinel: numbers until 0, sum; 0 is not added |
| 40–44 | for or while? four situations; correctness: the condition, the update, the goal at the end |
| 44–45 | Lab missions |

### Tool Note – Thonny
An endless loop keeps printing. Press the red **Stop** button (or Ctrl+F2) to stop the program.

---

# 6. Second 45 Minutes — Lab

Starter: [`While_Starter.py`](While_Starter.py). Reference: [`While_Reference.py`](While_Reference.py).

## 45–52 — Warm-up: the loop that never stops

```python
# Warm-up: this loop never stops. Do not run it yet!
number = 1
while number <= 5:
    print(number)
print("Finished")
```

Predict, run, stop it with Stop, then add `number = number + 1` inside the body → 1 … 5, `Finished`.

## 52–62 — Task 1: `password()`

Ask `Password: ` again and again until the user types `python`; wrong tries print `Try again`; then `Access granted`. Test: `hello`, `Python`, `python` → two `Try again`, then `Access granted` (capitals matter — from 4.1).

## 62–72 — Task 2: `sum_until_zero()`

Read numbers until 0 and print `Total: …`. Test 5, 8, −3, 0 → `Total: 10`. Test 0 alone → `Total: 0` (the loop never runs — a valid case to test).

## 72–80 — Task 3: `rover_trips()`

The battery starts at 100; every trip uses 15; the rover travels while the battery is at least 20. Print each trip and the total:

| Trip | Battery after |
|---|---|
| 1 | 85 |
| 2 | 70 |
| 3 | 55 |
| 4 | 40 |
| 5 | 25 |
| 6 | 10 |

`Trips: 6` — the stop depends on the variable `battery` (official goal 8). Ask: why can't a `for` easily do this?

## 80–83 — Document and save

Save As `G7_U5_M3_While_<Name>.py`.

## 83–90 — Exit check

1. When does a `while` loop run a round? (when its condition is `True`)
2. Why must the body change something? (otherwise the condition never becomes `False` — the loop never ends)
3. For each: print 10 times · read numbers until 0 → `for` · `while`

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The condition is checked in the middle of a round | Only before each round |
| The update can come before the loop | It must be inside, or the condition never changes |
| The sentinel 0 is added to the total | Read the next value at the end of the body; 0 ends the loop before being added |
| `while` is the same as `if` | `if` checks once; `while` checks again after every round |
| A loop that runs 0 times is a bug | It can be correct (e.g. first number is 0) |

---

# 8. Assessment Evidence (formative)

- Trace tables including the final `False` check (official: trace)
- Endless loop explained and fixed (official goal 3)
- `sum_until_zero()` tested with an empty input (correctness)
- for / while choices with reasons (official goals 2, 7)
- Exit check
