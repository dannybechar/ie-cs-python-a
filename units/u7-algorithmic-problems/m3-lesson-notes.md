# Unit 7.3 — Algorithmic Problems

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Roll the Dice — Random Numbers, Simulations and the Unit Checkpoint (Mission 21)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab with the unit checkpoint  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit7_meeting3_random_numbers_v2.pptx` (the "can we know the output?" warm-up, the `randint` table, choosing a range, dice, the guessing game with a `while` and an attempts counter, the 100-roll simulation and its prediction kept; `+=` replaced; the lab became a Turtle random walk and the unit checkpoint)  
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
| Concept: random number (מספר אקראי) | ✅ |
| Teaching: explain what a random value is and how to use it | ✅ slides 2–6 |
| Program overview: algorithmic problems with Turtle | ✅ Task 1 (random walk) |
| Assessment (theory): trace a program and print its output | ✅ checkpoint B |
| Assessment (practical): a program with a counter, an accumulator and a random number | ✅ checkpoint A |

With this meeting Unit 7 uses exactly its 270 official minutes (45 theory / 225 practice).

### Deliberate exclusions
No `random.random()`, `choice` or `seed`; no `goto` (the random walk turns and moves forward).

---

## 3. Lesson Goal

**`random.randint(a, b)` returns a whole number from a to b — both included. Draw once, save the value in a variable, then use it.**

---

## 4. Core Mental Models

- **Unlike `range`, `randint` includes the upper bound:** `randint(1, 6)` can return 6.
- **Draw once, then check:** `roll = random.randint(1, 6)` and then `if roll == 6` — calling `randint` again draws a new number.
- **A simulation repeats a random event** and uses the unit's patterns (counter, accumulator) on the results; the exact output changes between runs, but its range does not.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 21 |
| 1–5 | **Warm-up:** `random.randint(1, 6)` — can we know what will be printed? What can we know? |
| 5–7 | Answer: not the exact number; always a whole number from 1 to 6, 6 included |
| 7–15 | `import random`; the `randint` table: dice, coin, a range; the upper bound is included (unlike `range`) |
| 15–19 | **Students:** choose a call for a digit 0–9, a number 5–15, an even number from 2, 4, 6 |
| 19–21 | Answer: `randint(0, 9)`, `randint(5, 15)`, `randint(1, 3) * 2` |
| 21–26 | Dice: draw once, save, then check `roll == 6` |
| 26–33 | Guessing game: `while guess != secret`, hints, an attempts counter (5.3 + 7.1) |
| 33–39 | Simulation: 100 rolls, count the sixes |
| 39–42 | **Predict:** what can we say about the simulation's output? |
| 42–44 | Answer: a whole number from 0 to 100; it changes between runs |
| 44–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab with the Checkpoint

Starter: [`Random_Starter.py`](Random_Starter.py). Reference: [`Random_Reference.py`](Random_Reference.py).

The starter's warm-up (it draws twice, so `Roll: 6` can appear without `You win`) is for students who finish early or for homework; the lab time goes to the random walk and the checkpoint.

## 45–57 — Task 1: `random_walk()` (Turtle)

20 steps: turn `random.randint(0, 360)`, move `random.randint(10, 40)`. Count the steps longer than 30 and add up the distance; print both. Every run draws a different path.

## 57–73 — Checkpoint A (practical, alone)

- **A1 — `dice_stats()`:** roll a die 30 times; print how many sixes, the total and the average.
- **A2 — `guess_game()`:** a secret number 1–20; ask until correct, with Too low / Too high, and print the number of attempts.

## 73–81 — Checkpoint B (theory, on paper, no running)

```python
count = 0
total = 0
for number in range(1, 6):
    total = total + number
    if number % 2 == 1:
        count = count + 1
print(count, total)
```

1. What is printed? 2. Which values can `random.randint(3, 7)` return? 3. Counter, accumulator or minimum: how many passed · the sum of the expenses · the coldest day. 4. Why does a maximum start with the first value and not with 0?

## 81–84 — Checkpoint B answers

1. `3 15`. 2. 3, 4, 5, 6, 7. 3. counter · accumulator · minimum. 4. With negative values 0 would win although it is not in the data.

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
| Calling `randint` again gives the same number | Every call draws again — save the value |
| A random program cannot be checked | Check the range and the patterns, not the exact number |
| The simulation always prints about 16 | Likely near it, but any number from 0 to 100 is possible |

---

# 8. Assessment Evidence

- `randint` range choices (formative)
- **Checkpoint A** (practical): `dice_stats()` and `guess_game()`
- **Checkpoint B** (theoretical): trace with a counter and an accumulator, `randint` range, pattern identification
- Exit check
