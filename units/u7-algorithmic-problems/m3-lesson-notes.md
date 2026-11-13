# Unit 7.3 — Algorithmic Problems

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Roll the Dice — Random Numbers, Simulations and the Unit Checkpoint (Mission 21)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab with the unit checkpoint  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit7_meeting3_random_numbers_v2.pptx` (the "can we know the output?" warm-up, the `randint` table, choosing a range, dice, the guessing game with a `while` and an attempts counter, the 100-roll simulation and its prediction kept; the lab became a Turtle random walk and the unit checkpoint; Phase 5: the one-die demo became the ministry two-dice "double" example, `randrange` and `random.random()` added to the table, checkpoint B rebuilt on the ministry past-exam question 16.3 Q3)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | counter: start at 0, add 1 when the event happens; two counters | 0 / 90 |
| 7.2 | accumulator, average (accumulator ÷ counter), minimum and maximum | 0 / 90 |
| **7.3 (this)** | **`random.randint`, games and simulations, Turtle random walk, unit checkpoint** | 45 / 45 |

This meeting closes Unit 7 and holds its **checkpoint** (practical + theoretical), as the official assessment asks.

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.15) | Covered here |
|---|---|
| 2. Write a program that draws a random number and uses it | ✅ slides 7–9, Task 1, checkpoint A |
| Formula-sheet calls: `randint`, `randrange(start, end)`, `random.random()` | ✅ table, "students choose", checkpoint B item 2 (U7-05) |
| Concept: random number (מספר אקראי) | ✅ |
| Teaching: explain what a random value is and how to use it | ✅ slides 2–6 |
| Program overview: algorithmic problems with Turtle | ✅ Task 1 (random walk) |
| Assessment (theory): trace a program and print its output; find the defect in code | ✅ checkpoint B (items 1 and 3) |
| Assessment (practical): a program with a counter, an accumulator and a random number | ✅ checkpoint A |

With this meeting Unit 7 uses exactly its 270 official minutes (45 theory / 225 practice).

### Deliberate exclusions
No `choice` or `seed` (not on the formula sheet); no `goto` (the random walk turns and moves forward; the optional alternative with `goto` and random coordinates is in the take-home pack). `randrange` and `random.random()` are taught as recognition of the exam formula sheet; the practical tasks use `randint`.

---

## 3. Lesson Goal

**`random.randint(a, b)` returns a whole number from a to b — both included. Draw once, save the value in a variable, then use it.**

---

## 4. Core Mental Models

- **Unlike `range`, `randint` includes the upper bound:** `randint(1, 6)` can return 6. **`randrange(start, end)` behaves like `range`:** `randrange(1, 7)` returns 1 to 6, 7 is excluded.
- **`random.random()`** returns a decimal number from 0 up to, but not including, 1.
- **Draw once, then check:** `roll = random.randint(1, 6)` and then `if roll == 6` — calling `randint` again draws a new number.
- **A simulation repeats a random event** and uses the unit's patterns (counter, accumulator) on the results; the exact output changes between runs, but its range does not.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 21 |
| 1–5 | **Warm-up:** `random.randint(1, 6)` — can we know what will be printed? What can we know? |
| 5–7 | Answer: not the exact number; always a whole number from 1 to 6, 6 included |
| 7–17 | `import random`; the table: `randint(1, 6)` dice, `randint(0, 1)` coin (short), `randint(10, 20)`; then **`randrange(1, 7)`** (7 excluded, like `range`) and **`random.random()`** (0 up to, not including, 1); the upper bound of `randint` is included |
| 17–21 | **Students:** choose a call for a digit 0–9, a number 5–15, an even number from 2, 4, 6; which values can `randrange(3, 7)` return? |
| 21–23 | Answer: `randint(0, 9)`, `randint(5, 15)`, `randint(1, 3) * 2`; `randrange(3, 7)` → 3, 4, 5, 6 |
| 23–29 | **Double dice (ministry example):** draw `dice1` and `dice2` once each, save them, `if dice1 == dice2:` print "double"; then 10 rolls and a counter of doubles (inline, no `return`) |
| 29–36 | Guessing game: `while guess != secret`, hints, an attempts counter (5.3 + 7.1). Variant: only 3 attempts with `for i in range(3)` |
| 36–41 | Simulation: 100 rolls, count the sixes |
| 41–44 | **Predict:** what can we say about the simulation's output? Answer: a whole number from 0 to 100; it changes between runs |
| 44–45 | Lab missions |

### Minute plan (sums to 90)

| Block | Minutes | Running total |
|---|---:|---:|
| Title + warm-up + answer | 7 | 7 |
| `randint` table + `randrange` + `random.random()` | 10 | 17 |
| Students choose a call + answer | 6 | 23 |
| Double dice (two dice, 10 rolls, counter) | 6 | 29 |
| Guessing game | 7 | 36 |
| Simulation | 5 | 41 |
| Prediction + answer | 3 | 44 |
| Lab missions | 1 | 45 |
| Task 1: `random_walk()` | 12 | 57 |
| Checkpoint A (practical) | 16 | 73 |
| Checkpoint B (theory) | 8 | 81 |
| Checkpoint B answers | 3 | 84 |
| Document and save | 2 | 86 |
| Exit check | 4 | 90 |

Knowledge + guided practice 0–45 (45), lab 45–90 (45): the 45 / 45 split is unchanged. Net change against the old plan: +4 added (`randrange` and `random.random()`), offset by a shorter coin row (−2) and a shorter simulation and prediction (−3: simulation 6 → 5, prediction 5 → 3, with +1 for the two-dice example taking the slot of the one-die demo).

**Deck:** [`m3-slides-he.pdf`](m3-slides-he.pdf) predates these changes. The `randrange` / `random.random()` rows, the two-dice example, the 3-attempts variant and the new checkpoint B (fragments A and C) have no slides: show them live, and add the answer lines to the answer slide by hand, until the deck is rebuilt.

---

# 6. Second 45 Minutes — Lab with the Checkpoint

Starter: [`Random_Starter.py`](exercises/Random_Starter.py). Reference: [`Random_Reference.py`](solutions/Random_Reference.py).

The starter's warm-up (it draws twice, so `Roll: 6` can appear without `You win`) is for students who finish early or for homework; the lab time goes to the random walk and the checkpoint.

## 45–57 — Task 1: `random_walk()` (Turtle)

20 steps: turn `random.randint(0, 360)`, move `random.randint(10, 40)`. Count the steps longer than 30 and add up the distance; print both. Every run draws a different path.

## 57–73 — Checkpoint A (practical, alone)

- **A1 — `dice_stats()`:** roll a die 30 times; print how many sixes, the total and the average.
- **A2 — `guess_game()`:** a secret number 1–20; ask until correct, with Too low / Too high, and print the number of attempts.

## 73–81 — Checkpoint B (theory, on paper, no running)

Item 3 comes from the ministry past-exam question 16.3 Q3 (ממבחן מפמ"ר): the goal is to read 10 grades and count those **above 55 and below 80**; for the sequence 76 84 80 57 77 90 68 74 100 55 the output should be 5. For each fragment: does it do what is required? If not, how do you fix it?

```python
count = 0
total = 0
for number in range(1, 6):
    total = total + number
    if number % 2 == 1:
        count = count + 1
print(count, total)
```

1. What is printed?
2. Which values can `random.randint(3, 7)` return? And `random.randrange(3, 7)`?
3. Fragments A and C (below).
4. Why does a maximum start with the first value and not with 0?

```python
# Fragment A
count = 0
for item in range(10):
    grade = int(input("Grade: "))
    if grade > 55 and grade < 80:
        count = count + 1
print(count)
```

```python
# Fragment C
count = 0
index = 0
while index < 10:
    grade = int(input("Grade: "))
    if grade > 55 and grade < 80:
        count = count + 1
print(count)
```

## 81–84 — Checkpoint B answers

1. `3 15`. 2. `randint(3, 7)`: 3, 4, 5, 6, 7; `randrange(3, 7)`: 3, 4, 5, 6. 3. **A** does what is required (`and`: both conditions; 55 and 80 are not counted; the sample gives 5). **C** does not: `index` never changes, so the loop never ends; fix with `index = index + 1` inside the loop. 4. With negative values 0 would win although it is not in the data.

Fragments B (`or` is always true: counts every grade) and D (`print(count + 1)` instead of updating `count`, which stays 0) are in the take-home pack. The old "counter, accumulator or minimum?" item moved out: it is practised in the 7.1 and 7.2 warm-ups and exit checks.

## 84–86 — Document and save

Save As `G7_U7_M3_Random_<Name>.py`.

## 86–90 — Exit check

1. Is the upper bound included in `randint`? (yes)
2. Which pattern counts how many times a 6 came up? (a counter)
3. Why does a simulation's output change between runs? (every `randint` call can return another value)

### Tool Note – Thonny
Close the Turtle window before the next run.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `randint(1, 6)` stops before 6 | Both bounds are included — unlike `range` |
| `randrange(1, 7)` can return 7 | It behaves like `range`: the end is excluded |
| `random.random()` can return 1 | 0 is possible, 1 is not |
| `grade > 55 or grade < 80` counts the grades between | `or` is true for every number: use `and` |
| A `while` counts by itself | Nothing changes `index` unless we update it inside the loop |
| Calling `randint` again gives the same number | Every call draws again — save the value |
| A random program cannot be checked | Check the range and the patterns, not the exact number |
| The simulation always prints about 16 | Likely near it, but any number from 0 to 100 is possible |

---

# 8. Assessment Evidence

- `randint` range choices (formative)
- **Checkpoint A** (practical): `dice_stats()` and `guess_game()`
- **Checkpoint B** (theoretical): trace with a counter and an accumulator, `randint` / `randrange` range, judging and fixing code fragments (ministry 16.3 Q3), the maximum start
- Exit check
