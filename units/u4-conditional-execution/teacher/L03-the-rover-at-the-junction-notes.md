# Unit 4.3 — Conditional Execution

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover at the Junction — Compound Conditions, Nesting, the Rolling Condition and Turtle (Mission 10)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (37 min guided practice, then 53 min lab with the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `chapter4_session3_compound_conditions_turtle_ready_v2.pptx` (eligibility trace, payment `or`, nested ticket check, "compound can replace nesting", Turtle choice kept; `elif` restored after the Phase 5 audit; `t = turtle.Turtle()` and `setheading` stay out: module-level Turtle is the approved teaching style, the exam dialect is practised in Units 2, 6 and 9)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 4.1 | comparisons → True/False → and/or → truth tables → order | 45 / 45 |
| 4.2 | `if` → false skips → indentation → `if/else` → input filter → errors | 45 / 45 |
| **4.3 (this)** | **`and`/`or` in `if` → one-level nesting → rolling condition (`elif`) → Turtle → checkpoint** | 0 / 90 |

This meeting closes Unit 4 and holds its **checkpoint** (practical + tracing), as the official assessment asks.

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 4 (python-a.pdf p.10):

| Official goal / concept | Covered here |
|---|---|
| 2. Compound conditions (one-level nesting, `and` / `or`) | ✅ warm-up, payment, Task 1, checkpoint |
| Overview p.4: rolling conditional statement (משפט ביצוע מותנה מתגלגל, `elif`) | ✅ 10-minute block, Task 2, checkpoint A and B |
| Overview p.4: conditions with Turtle (הוראת תנאים באמצעות Turtle) | ✅ Task 2 |
| Concepts: compound condition, branches, simple input filter | ✅ size filter (Task 2), age filter (checkpoint A) |
| Exam preparation (ministry meeting 17): nested `if` inside an `elif` chain; evaluate `%` / `//` expressions | ✅ checkpoint B (gift chain, two expressions) |
| Teaching method: geometric shapes combining conditional execution (Turtle) | ✅ Task 2 |
| Teaching method: trace tables | ✅ nested trace, checkpoint B |
| Assessment: practical — a program with a simple and a compound condition | ✅ checkpoint A |
| Assessment: theoretical — algorithm analysis | ✅ checkpoint B (trace table) |

Official minutes used: the remaining practice of both topics (45 boolean + 45 conditional). With this meeting Unit 4 uses exactly its 270 official minutes.

### Deliberate exclusions
No nesting deeper than one level in the core (the three-level admission task is optional take-home), no loops (so the Turtle shapes repeat their lines, as in Unit 2), no `t = turtle.Turtle()`, no `setheading`. `elif` is now taught (rolling condition); `not` is available from 4.1.

### Terminology bridges (ministry wording)
Name the four kinds of condition, in Hebrew and English, on the board: **תנאי פשוט** (simple), **תנאי מורכב** (compound: `and` / `or`), **תנאי מקונן** (nested), **תנאי מתגלגל** (rolling: `if` / `elif` / `else`). "מתגלגל" here means a chain where the first true condition wins; it is a different thing from the repeated-execution "מתגלגל" met later in Unit 5. In the exam a function is a **פעולה**.

---

## 3. Lesson Goal

**Two questions, one decision: join them with `and` / `or`, or ask the second inside the first.**

Core workflow: **Read → Predict → Run → Check → Fix**

---

## 4. Student-Facing Objectives

1. Use `and` / `or` in an `if` condition.
2. Remember that each side of `or` needs its own comparison.
3. Trace a nested `if`: the inner question is asked only when the outer answer is `True`.
4. Rewrite a nested `if` as one compound condition when both paths lead to the same actions.
5. Let a condition choose what the turtle draws.
6. Write a rolling condition (`if` / `elif` / `else`), and explain that the first true condition wins and the order matters.
7. State the rule: an `else` belongs to the nearest `if` at the same indentation.
8. Pass the checkpoint: write a program with a simple and a compound condition, and trace a nested program inside an `elif` chain.

---

## 5. Core Mental Models

### Two gates or one gate
A nested `if` is two gates in a row: the second is checked only after passing the first. A compound `and` condition is one gate that checks both at once.

```python
# Nested
if age >= 12:
    if has_ticket == "yes":
        print("Enter")

# Compound
if age >= 12 and has_ticket == "yes":
    print("Enter")
```

The two give the same result here. Nesting is needed when each failure gets its own message (`Ticket required` vs `Age requirement not met`).

### Each side of `or` is a full question
`payment == "cash" or payment == "card"` — never `payment == "cash" or "card"` (from 4.1).

### The rolling condition: first true wins
A chain of questions. Python asks them from the top; the first `True` runs its body, and **the rest are skipped**. `else` is the last road, when nothing was `True`.

```python
if battery >= 70:
    print("Green")
elif battery >= 30:
    print("Yellow")
else:
    print("Red")
```

Order matters: with `battery >= 30` first, a battery of 90 prints `Yellow`. Separate `if`s are not a chain: three `if`s for 90 print two lines; the `elif` chain prints one.

### An `else` belongs to the nearest `if`
An `else` pairs with the nearest `if` above it **at the same indentation**. Indentation, not the line order, decides which `if` an `else` closes.

---

# 6. First 37 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 10, the rover at the junction |
| 1–7 | **Warm-up (predict):** `if age >= 12 and has_ticket:` → `Approved` / `Not approved` for (14, True), (10, True), (14, False) |
| 7–9 | Answer: only the first is approved; in the others one side of `and` is `False` |
| 9–14 | `or` for several valid options: `payment == "cash" or payment == "card"` → cash, card accepted; coupon not. Warning: each side needs its own comparison |
| 14–19 | **Predict:** nested ticket check for (13, yes), (13, no), (10, yes) |
| 19–23 | Answer: `You may enter` · `Ticket required` · `Age requirement not met`. The inner `if` runs only when `age >= 12`. **The association rule:** point at each `else` and its `if` at the same indentation (ministry 9.1 wording) |
| 23–26 | Nested vs compound (code above): same result when there is one shared action. Demo: the rover decision both ways (`rover_move_nested()` in the reference); **ask:** which is shorter? why do both print the same? |
| 26–29 | **Rolling condition (new):** the battery colour chain (code above); **students predict** 90, 50, 10 → `Green`, `Yellow`, `Red` |
| 29–31 | **First true wins:** 90 matches two questions, but only `Green` prints. **Predict the trap:** the same chain with `battery >= 30` first → 90 prints `Yellow` (the order matters) |
| 31–34 | **Chain or separate `if`s?** Three separate `if`s for 90 print two lines; the `elif` chain prints one. Rule of thumb: separate `if`s answer separate questions; `elif` is one question with many answers |
| 34–36 | Name the four kinds of condition (simple, compound, nested, rolling) on the board. Where would `elif` shorten the ticket check? (checkpoint A) |
| 36–37 | Lab missions; one function per task, one active call |

Time ledger (Phase 5): `elif` block +10 and association rule +2, minus 2 (nested-vs-compound 4→3, transition 2→1): guided 27 → 37. Funded by the lab: Task 1 10→7 (nested version folded into the guided demo), Task 2 15→13, checkpoint B 13→12, document 4→2, exit check 6→4 (−10). The meeting still sums to 90 (37 guided + 53 lab).

---

# 7. Lab — 53 Minutes

Starter: [`Shapes_Starter.py`](../exercises/Shapes_Starter.py). References: [`Conditions_Reference.py`](solutions/Conditions_Reference.py) (one function per task) and [`Shapes_Reference.py`](solutions/Shapes_Reference.py) (the completed starter).

## 37–44 — Task 1: may the rover move?

Function `rover_move()`: reads `battery` (int) and `obstacle` (`yes`/`no`). Prints `Move forward` only if the battery is at least 20 **and** there is no obstacle; otherwise `Stop`. (The nested version was shown in the guided part; students who finish early write it as `rover_move_nested()`.)

| battery | obstacle | Output |
|---|---|---|
| 50 | no | `Move forward` |
| 50 | yes | `Stop` |
| 10 | no | `Stop` |
| 20 | no | `Move forward` |

## 44–57 — Task 2: the rover draws by choice (Turtle)

`Shapes_Starter.py` already has the square and triangle lines from Unit 2 — and draws **both**. Students add the conditions and fix the indentation:

1. Draw only if `size` is from 20 to 200 (`and`); otherwise print `Invalid size` (input filter).
2. Inside, a rolling condition: `square` → blue square (`right(90)` ×4); `triangle` → green triangle (`right(120)` ×3); anything else → print `Unknown shape`.

Tests: `square` 100 → blue square below-right of the start; `triangle` 100 → green triangle pointing down, corners (0, 0), (100, 0), (50, −86.6); `circle` 100 → `Unknown shape`, no drawing; `square` 10 → `Invalid size`, no drawing. The turtle ends at the start, facing right.

### Tool Note – Thonny
Answer the `input` questions in the Shell first; the Turtle window opens after them. Close the Turtle window before the next run. For `Unknown shape` an empty Turtle window may open; just close it.

## 57–72 — Checkpoint A (practical, alone)

Function `ticket_price()`: reads an age.
- Less than 0 or more than 120 → `Invalid age`.
- Otherwise: under 12 **or** 65 and up → `Price: 20`; else `Price: 40`.

Tests: −1 → `Invalid age` · 5 → `Price: 20` · 12 → `Price: 40` · 64 → `Price: 40` · 65 → `Price: 20` · 130 → `Invalid age`.
The program contains a simple filter and a compound condition — the official practical assessment. Both forms are accepted: one-level nesting (`ticket_price_nested()`) or the rolling condition (`if` / `elif` / `else`, `ticket_price()` in the reference).

## 72–84 — Checkpoint B (tracing, on paper, no running)

Exam-style, adapted from the ministry exam preparation (meeting 17, exercises #4 and #5). The older fuel/weather trace moved to the take-home pack.

### B1 (72–80) — a nested `if` inside an `elif` chain

```python
if amount < 80:
    print("No gift")
elif amount < 800:
    if amount <= 500:
        print("Yoga ball")
    elif amount < 650:
        print("Tennis balls")
    else:
        print("Football")
else:
    print("Running shoes")
```

| amount | Output |
|---|---|
| 25 | `No gift` |
| 200 | `Yoga ball` |
| 550 | `Tennis balls` |
| 750 | `Football` |

6 minutes to fill the table, 2 minutes to check it together (999 → `Running shoes` on the board). The source exercise has a redundant `amount >= 80 and` in the inner condition; it is dropped here.

### B2 (80–84) — evaluate with `a = 10`, `b = 15`, `c = 0`

| Expression | Value |
|---|---|
| `a % 5 == 0 and b // 5 > c` | `True` |
| `a % 2 == c % 2 and b % 3 > a % 3` | `False` |

3 minutes to fill, 1 minute to check. The other three expressions of the source exercise go to the take-home pack.

## 84–86 — Document and save

One comment above each function; one active call. Save As `G7_U4_M3_Conditions_<Name>.py`.

Take-home (0 class minutes): [`exercises/Extra_Practice.md`](../exercises/Extra_Practice.md), section 4.3.

## 86–90 — Exit check

1. When do we use `and`, and when `or`? (`and` — every requirement must hold; `or` — one of several options is enough)
2. In a nested `if`, which condition is checked first? (the outer one; the inner only if the outer is `True`)
3. Write one compound condition for the nested ticket check. (`age >= 12 and has_ticket == "yes"`)
4. When does an `elif` run? (only if every question above it was `False`, and its own question is `True`)

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| `payment == "cash" or "card"` | Each side of `or` needs its own comparison |
| The inner `if` always runs | Only when the outer condition is `True` |
| `and` and `or` are interchangeable | `and` needs all; `or` needs one |
| Nesting and `and` are always the same | Same only when the failures share one action |
| The body of the inner `if` needs the same indentation as the outer | Each level adds 4 spaces |
| Invalid size still draws | The drawing lines must be inside the `if` |
| Separate `if`s and an `elif` chain are the same | Separate `if`s can all run; in a chain only the first `True` runs |
| The order of the `elif`s does not matter | The first true wins: put the narrow/high case first (`>= 70` before `>= 30`) |
| An `else` pairs with the `if` just before it in the text | It pairs with the nearest `if` at the same indentation |

---

# 9. Assessment Evidence

- Warm-up and nested-trace predictions (formative)
- Task 1 both versions agree on the four tests
- Task 2 draws only for valid sizes and the chosen shape; `Unknown shape` for anything else
- **Checkpoint A** (practical): `ticket_price()` passes the six tests
- **Checkpoint B** (theoretical): gift-chain trace table and the two expressions correct
- Exit check
