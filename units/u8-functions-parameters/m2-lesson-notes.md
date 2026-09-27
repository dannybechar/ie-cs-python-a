# Unit 8.2 — Functions with Parameters

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Building Blocks — Functions without Parameters, `main()` and Turtle (Mission 23)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit8_meeting2_functions_without_parameters_final.pptx` (the B-A-B call-order warm-up, splitting a program with `main()`, input inside a function, `ask_age()`, `draw_square()` called in a loop, the side-count prediction, the house with a roof, the door challenge kept; `t = turtle.Turtle()` style avoided; a "call inside its own body" bug added)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | why functions → define vs call → order of execution → no return value | 45 / 45 |
| **8.2 (this)** | **functions without parameters: split a program, `main()`, input inside a function, Turtle** | 0 / 90 |
| 8.3 | parameters and arguments, several parameters, parameter vs input, Turtle sizes | 45 / 45 |
| 8.4 | scope: local variables, `global`, Turtle with shared state, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.17) | Covered here |
|---|---|
| 1. Write a function without parameters that returns no value, and call it | ✅ Tasks 1–3 |
| Teaching: tell a function without parameters from one that reads values inside it | ✅ slide 5, Task 1 |
| Teaching: functions with Turtle | ✅ slides 6–8, Tasks 2–3 |

Official topic and minutes: "function without parameters" — 90 of its 135 practice minutes (with 8.1, all 135).

### Deliberate exclusions
No parameters yet: every size is fixed inside the function — that limit is the reason for 8.3. No `goto`.

---

## 3. Lesson Goal

**Split a program into small named functions; `main()` calls them in order.**

---

## 4. Core Mental Models

- **`main()`** holds the order of the program; each other function does one job.
- **A function without parameters can still read input** inside its body.
- **A drawing function is a stamp:** call it again and again, turn between calls.
- **The call goes outside the definition** (not indented under it).

---

# 5. First 30 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 23 |
| 1–4 | **Warm-up:** `first()` prints A, `second()` prints B; calls `second()`, `first()`, `second()` |
| 4–6 | Answer: B, A, B — the calls decide the order, not the definitions |
| 6–12 | Split a program: `show_header()`, `show_menu()`, `main()` |
| 12–17 | Input inside a function: `ask_name()` |
| 17–23 | A Turtle function: `draw_square()`, called 6 times with `turtle.right(60)` |
| 23–26 | **Predict:** `for i in range(5): draw_square()` — how many sides? |
| 26–28 | Answer: 5 × 4 = 20 |
| 28–30 | Lab missions |

---

# 6. Lab — 60 Minutes

Starter: [`Modules_Starter.py`](Modules_Starter.py). Reference: [`Modules_Reference.py`](Modules_Reference.py).

## 30–37 — Warm-up: nothing is drawn

```python
# Warm-up: the program runs with no error, but nothing is drawn. Why?
import turtle


def draw_square():
    for i in range(4):
        turtle.forward(80)
        turtle.right(90)
    draw_square()


turtle.done()
```

The call is indented, so it is inside the body — and the body never runs. Fix: unindent the call (put it before `turtle.done()`).

## 37–47 — Task 1: `ask_age()`

Read an age; print `Adult` for 18 and up, else `Minor`. Test 17 and 18.

## 47–65 — Task 2: a house

`draw_square()` (side 100), `draw_roof()` (3 × `forward(100)`, `left(120)`), and `main()` that calls them. The roof sits on the top side of the square.

## 65–80 — Task 3 (challenge): `draw_door()`

Add a door at the bottom of the square: `penup()`, `forward(40)`, `right(90)`, `forward(60)`, `pendown()`, then a 20 × 40 rectangle. `main()` calls it last.

## 80–83 — Document and save

Save As `G7_U8_M2_Modules_<Name>.py`.

## 83–90 — Exit check

1. Can a function without parameters read input? (yes — inside its body)
2. What is `main()` for? (it sets the order of the program)
3. Why write separate drawing functions? (reuse them and fix each part in one place)

### Tool Note – Thonny
Close the Turtle window before the next run.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Functions run in the order they are defined | They run in the order they are called |
| The call belongs under the `def` | Then it is part of the body and never runs |
| A function without parameters cannot use input | It can read input inside itself |
| `main` is a special Python word | It is a name we choose for the order function |

---

# 8. Assessment Evidence (formative)

- Call-order and side-count predictions
- Warm-up explained (the indented call)
- The house drawn with `main()`
- Exit check
