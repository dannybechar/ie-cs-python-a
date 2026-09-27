# Unit 8.3 — Functions with Parameters

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Send a Value — Parameters and Arguments (Mission 24)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit8_meeting3_functions_with_parameters_final.pptx` (the fixed-greeting warm-up, parameter vs argument, the calls trace table, `print_stars(amount)`, two parameters and their order, parameter vs input table, `repeat_message`, `draw_square(size)`, `draw_rectangle(width, height)` kept; a missing-argument bug and a two-parameter prediction added)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | why functions → define vs call → order of execution → no return value | 45 / 45 |
| 8.2 | functions without parameters: split a program, `main()`, input inside a function, Turtle | 0 / 90 |
| **8.3 (this)** | **parameters and arguments, several parameters, parameter vs input, Turtle sizes** | 45 / 45 |
| 8.4 | scope: local variables, `global`, Turtle with shared state, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.17) | Covered here |
|---|---|
| 2. Write a function with parameters that returns no value, and call it | ✅ Tasks 1–3 |
| Concept: parameters | ✅ |
| Teaching: a function that receives parameters vs one that reads input inside | ✅ slide 10 |
| Teaching: functions with parameters with Turtle | ✅ Tasks 2–3 |

Official topic and minutes: "function with parameters" — 45 theory + 45 of its 135 practice minutes.

### Deliberate exclusions
No `return`, no default or keyword arguments.

---

## 3. Lesson Goal

**A parameter is a variable in the definition; the argument is the value the call sends to it.**

---

## 4. Core Mental Models

```python
def greet(name):        # name is the parameter
    print("Hello", name)


greet("Dana")           # "Dana" is the argument
greet("Noam")
```

- **Same body, different values:** each call fills the parameter again.
- **Order matters:** `show_rectangle(8, 3)` sends 8 to the first parameter and 3 to the second.
- **Parameter or input?** A parameter gets its value from the call; `input` gets it from the user while the function runs.
- A call must send **one argument per parameter**, or Python stops with `TypeError`.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 24 |
| 1–5 | **Warm-up:** `greet()` always prints `Hello Dana` — how do we greet Noam without a second function? |
| 5–7 | Answer: `def greet(name):` |
| 7–15 | Parameter and argument: `greet("Dana")`, `greet("Noam")` |
| 15–20 | Trace table: call · value of `name` · output |
| 20–26 | A number parameter: `print_stars(amount)` with `"*" * amount` (from 6.2) |
| 26–30 | **Predict:** `show(word, times)` prints `word * times`; `show("ab", 3)`, `show("-", 5)` |
| 30–32 | Answer: `ababab`, `-----` |
| 32–38 | The order of arguments: `show_rectangle(8, 3)` vs `show_rectangle(3, 8)` |
| 38–44 | Parameter or input? (table) |
| 44–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Parameters_Starter.py`](Parameters_Starter.py). Reference: [`Parameters_Reference.py`](Parameters_Reference.py).

## 45–50 — Warm-up: why does it crash?

```python
# Warm-up: why does this program crash?
def welcome(city):
    print("Welcome to", city)


welcome()
```

`TypeError: welcome() missing 1 required positional argument: 'city'`. Fix: `welcome("Haifa")`.

## 52–62 — Task 1: `repeat_message(message, times)`

Print the message `times` times with a loop. Call `repeat_message("Go", 4)`.

## 62–72 — Task 2: `draw_square(size)` (Turtle)

One function, three sizes: `draw_square(50)`, `draw_square(100)`, `draw_square(150)` — three squares from the same corner.

## 72–82 — Task 3: `draw_rectangle(width, height)` (Turtle)

Two rounds of width, turn, height, turn. Call `draw_rectangle(140, 70)` and `draw_rectangle(70, 140)`: the order of the arguments changes the drawing.

## 82–85 — Document and save

Save As `G7_U8_M3_Parameters_<Name>.py`.

## 85–90 — Exit check

1. Where is the parameter written? (in the definition, inside the parentheses)
2. What is an argument? (the value sent in the call)
3. Why does the order of the arguments matter? (the first value goes to the first parameter, and so on)

### Tool Note – Thonny
Close the Turtle window before the next run.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Parameter and argument are the same | Parameter in the definition; argument in the call |
| The argument must have the same name as the parameter | Any value or variable can be sent |
| A call can leave out an argument | One argument per parameter, or `TypeError` |
| `draw_rectangle(70, 140)` equals `(140, 70)` | The order decides which is width |

---

# 8. Assessment Evidence (formative)

- Two-parameter prediction
- The `TypeError` explained
- Two rectangles compared
- Exit check
