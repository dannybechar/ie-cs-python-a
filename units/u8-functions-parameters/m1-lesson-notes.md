# Unit 8.1 — Functions with Parameters

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Why Functions? — Define, Call and Split a Program (Mission 22)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit8_meeting1_why_functions_final.pptx` (the repeated-frame warm-up, definition vs call table, the A-B-C order prediction, no return value, the three-bug fix-it, `welcome()`, the menu with two functions kept; the "function calls function" slide from `unit8_meeting2` moved here; a define-before-call bug and a Turtle windmill added)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **8.1 (this)** | **why functions → define vs call → order of execution → functions that act (return: 8.3)** | 45 / 45 |
| 8.2 | functions without parameters: split a program, `main()`, input inside a function, Turtle | 0 / 90 |
| 8.3 | parameters and arguments, several parameters, parameter vs input, return-lite (a function hands back one value) | 45 / 45 |
| 8.4 | scope: local variables, `global`, Turtle with shared state, unit checkpoint | 0 / 90 |

Students have written one function per task since Unit 1. This unit names **why** and adds parameters and scope.

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 8 (python-a.pdf p.17):

| Official goal / concept | Covered here |
|---|---|
| 1. Write a function without parameters that returns no value, and call it | ✅ Tasks 1–3 |
| Concept: function | ✅ |
| Teaching: the motivation — modularity, reuse, fewer errors, encapsulation | ✅ slides 2–4 |

Official topics and minutes: "why functions?" — 45 theory; "function without parameters" — 45 of its 135 practice minutes.

### Deliberate exclusions
No parameters yet (8.3) and no `return` yet: in this meeting every function acts (prints or draws). `return` arrives in 8.3 as a deliberate, teacher-approved deviation (return-lite, 20 min, ruling D2) from python-a.pdf p.17; the assessed practical form (checkpoint A in 8.4) stays a function that returns no value.

**Terminology bridge (U8-06):** the course says "פונקציה" (as python-a.pdf and the exam do); Ministry of Education materials say **"פעולה"** (also "מתודה"). Say once: "פונקציה = פעולה". The same applies in 9.1 to "פעולת מאזין" (listener function).

---

## 3. Lesson Goal

**A function gives a name to a piece of code: we write it once and call it wherever we need it.**

---

## 4. Core Mental Models

| Part | Syntax | Role |
|---|---|---|
| definition | `def show_line():` | creates the action — nothing runs yet |
| body | indented lines | what will run |
| call | `show_line()` | runs the body now |

- **Order of execution:** Python reads the definition, but runs its body only at the call.
- **Define before you call:** a call above the `def` crashes with `NameError`.
- **Why functions:** reuse, one place to fix, shorter code, test each part alone, names that explain.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 22 |
| 1–5 | **Warm-up:** six `print` lines with a repeated frame — what repeats? Give the action a name |
| 5–7 | Answer: the star line repeats → one function `show_line()` |
| 7–14 | Why functions: reuse, one place to fix, test parts alone; `show_line()` called twice. **Bridge (1–2 min, inside the 7 min):** "פונקציה = פעולה בחומרי משרד החינוך" |
| 14–19 | Definition, body, call (table) |
| 19–23 | **Predict:** `def hello(): print("B")`, then `print("A")`, `hello()`, `print("C")` |
| 23–25 | Answer: A, B, C — the definition does not run by itself |
| 25–32 | A function that calls functions: `show_header()`, `show_menu()`, `main()` |
| 32–36 | Our functions so far **act** — print or draw; they do not hand a value back. Preview only: `input()` and `int()` already hand values back; our own functions will do it in 8.3 |
| 36–41 | **Students:** find three bugs (missing colon, body not indented, call without parentheses) |
| 41–44 | Answer |
| 44–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Functions_Starter.py`](exercises/Functions_Starter.py). Reference: [`Functions_Reference.py`](solutions/Functions_Reference.py).

## 45–50 — Warm-up: why does it crash?

```python
# Warm-up: why does this program crash?
show_title()


def show_title():
    print("=== GAME ===")
```

`NameError: name 'show_title' is not defined` — the call runs before the definition. Fix: define first, call after.

## 52–58 — Task 1: `welcome()`

Two lines, `Welcome` and `Let's code`; call it three times.

## 58–70 — Task 2: the menu

`show_title()` prints `=== GAME ===`; `show_options()` prints three options; `main()` calls both in order.

## 70–82 — Task 3: `windmill()` (Turtle)

`draw_square()` draws a square of side 80; `windmill()` calls it 4 times with `turtle.right(90)` between. How many sides are drawn? (16)

## 82–85 — Document and save

Save As `G7_U8_M1_Functions_<Name>.py`.

## 85–90 — Exit check

1. What is the difference between a definition and a call? (the definition creates the action; the call runs it)
2. Why is the body indented? (the indentation marks which lines belong to the function)
3. How do you call a function named `start`? (`start()`)

### Tool Note – Thonny
Close the Turtle window before the next run.

**Turtle note (U8-12):** `turtle.done()` is the end-of-program line; the exam material writes `mainloop()` for the same job ("`done()` = `mainloop()`"). In the reference file it now sits once at the end of the program, not inside a function.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `def` runs the code | Only the call runs it |
| A call without `()` runs the function | `show_title` only names it; `show_title()` calls it |
| The call can come before the `def` | Python must read the definition first |
| The call is indented under the `def` | Then it is part of the body (see 8.2 warm-up) |

---

# 8. Assessment Evidence (formative)

- Order-of-execution prediction
- The three bugs and the `NameError` explained
- Windmill side count
- Exit check
