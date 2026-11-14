# Unit 8.2 — Functions with Parameters

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Building Blocks — Functions without Parameters, `main()` and Turtle (Mission 23)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit8_meeting2_functions_without_parameters_final.pptx` (the B-A-B call-order warm-up, splitting a program with `main()`, input inside a function, `ask_age()`, `draw_square()` called in a loop, the side-count prediction, the house with a roof, the door challenge moved to take-home (Phase 5: ministry 4.3 arithmetic-in-a-function tasks take its minutes); `t = turtle.Turtle()` style avoided; a "call inside its own body" bug added)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | why functions → define vs call → order of execution → functions that act (return: 8.3) | 45 / 45 |
| **8.2 (this)** | **functions without parameters: split a program, `main()`, input inside a function, Turtle** | 0 / 90 |
| 8.3 | parameters and arguments, several parameters, parameter vs input, return-lite (a function hands back one value) | 45 / 45 |
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
No parameters yet: every size is fixed inside the function — that limit is the reason for 8.3. No `goto`. Functions here print or draw; they hand nothing back (`return` is 8.3).

**Ministry link (U8-04):** the 6-minute trace warm-up and Task 3 come from ministry worksheet 4.3 (Ex 1, 4, 5, `classwork-m04-3`): arithmetic inside a function, input inside, result printed. In 8.3 `pool()` becomes `pool(times, price)`.

**Terminology (U8-06, U8-08):** "פונקציה" = "פעולה" (ministry word). `main()` is a name we choose; ministry solutions simply call the function at module level right after the definition — show that style once, it is equally correct.

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
| 6–12 | Split a program: `show_header()`, `show_menu()`, `main()` (and the same program with plain module-level calls, ministry style) |
| 12–17 | Input inside a function: `ask_name()` |
| 17–23 | A Turtle function: `draw_square()`, called 6 times with `turtle.right(60)` |
| 23–26 | **Predict:** `for i in range(5): draw_square()` — how many sides? |
| 26–28 | Answer: 5 × 4 = 20 |
| 28–30 | Lab missions |

---

# 6. Lab — 60 Minutes

Starter: [`Modules_Starter.py`](../exercises/Modules_Starter.py). Reference: [`Modules_Reference.py`](solutions/Modules_Reference.py).

## 30–33 — Warm-up: nothing is drawn (3 min)

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

## 33–39 — Trace warm-up: what does the function print? (6 min, ministry 4.3 Ex 1)

Three functions, each with fixed numbers and one `print`; students write the output before running:

```python
def ex1():
    num = 34
    a = num + 10
    b = num / 10
    print(b * 10 + a)      # 78.0  (/ gives a float)


def ex5():
    a = 10
    b = 30
    c = 20
    print((a + b) // c)    # 2     (// drops the fraction)


def ex6():
    a = 10
    b = 30
    print((b + a) / (b - a))   # 2.0 (/ gives a float even when exact)
```

Common trap: `78.0` not `78`, and `2.0` not `2`. Items ב, ג, ד of the ministry sheet are take-home.

## 39–47 — Task 1: `ask_age()` (8 min)

Read an age; print `Adult` for 18 and up, else `Minor`. Test 17 and 18.

## 47–65 — Task 2: a house

`draw_square()` (side 100), `draw_roof()` (3 × `forward(100)`, `left(120)`), and `main()` that calls them. The roof sits on the top side of the square.

## 65–80 — Task 3: `rectangle()` and `pool()` (15 min, ministry 4.3 Ex 4, 5)

Both functions read input **inside** and print the result:

- `rectangle()` reads `a` and `b` (side lengths) and prints the area.
- `pool()` reads `times` (visits) and `price` (entry price) and prints the total.

Test with two inputs each. Keep the `pool()` code: in 8.3 it becomes `pool(times, price)`.

**Enrichment / take-home (רשות):** `draw_door()` — a door at the bottom of the square: `penup()`, `forward(40)`, `right(90)`, `forward(60)`, `pendown()`, then a 20 × 40 rectangle; `main()` calls it last. Also ministry 4.3 Ex 6 `super()` with a 10% discount.

## 80–83 — Document and save

Save As `G7_U8_M2_Modules_<Name>.py`.

## 83–90 — Exit check

1. Can a function without parameters read input? (yes — inside its body)
2. What is `main()` for? (it sets the order of the program)
3. Why write separate drawing functions? (reuse them and fix each part in one place)
4. Ministry 4.3 Ex 3 style, on a short `school_info()` that prints a fixed `school_name` (code is on the brief): what is the function's name? (`school_info`, not `school_name` and not `def`); which line becomes `school_name = input("Enter school name: ")`? (the assignment line)

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
- Trace warm-up (`78.0`, `2`, `2.0`) and `rectangle()` / `pool()` working
- Exit check
