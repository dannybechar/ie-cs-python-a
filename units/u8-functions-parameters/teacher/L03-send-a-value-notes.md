# Unit 8.3 — Functions with Parameters

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Send a Value — Parameters and Arguments (Mission 24)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit8_meeting3_functions_with_parameters_final.pptx` (the fixed-greeting warm-up, parameter vs argument, the calls trace table, `print_stars(amount)`, two parameters and their order, parameter vs input table, `repeat_message`, `draw_square(size)`, `draw_rectangle(width, height)` kept as a take-home; a missing-argument bug and a two-parameter prediction added; Phase 5 adds return-lite and ministry `pool(times, price)`, `absolute_value`, `sign_text`)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | why functions → define vs call → order of execution → functions that act (return: 8.3) | 45 / 45 |
| 8.2 | functions without parameters: split a program, `main()`, input inside a function, Turtle | 0 / 90 |
| **8.3 (this)** | **parameters and arguments, several parameters, parameter vs input, return-lite (a function hands back one value)** | 45 / 45 |
| 8.4 | scope: local variables, `global`, Turtle with shared state, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.17) | Covered here |
|---|---|
| 2. Write a function with parameters that returns no value, and call it | ✅ Tasks 1–3 |
| Concept: parameters | ✅ |
| Teaching: a function that receives parameters vs one that reads input inside | ✅ slide 10 |
| Teaching: functions with parameters with Turtle | ✅ Task 2 (`draw_rectangle` is optional take-home) |
| **Return-lite (approved deviation D2 from p.17, ministry meeting 10, 20 min)** | ✅ knowledge 34–44, Task 3 |

Official topic and minutes: "function with parameters" — 45 theory + 45 of its 135 practice minutes.

### Deliberate exclusions
No default or keyword arguments. `return` is taught here **lightly** (return-lite): functions that hand back **one simple value** (a number or a string), used in `print(...)` or stored in a variable. Not taught: returning several values, `return` inside loops as a search pattern, `None` and printing a function that has no `return`. This is a teacher-approved deviation (ruling D2, `traceability.md` section 4) from python-a.pdf p.17, which describes functions that return no value; the assessed practical form (checkpoint A, 8.4) stays return-free.

**Terminology (U8-06, U8-07):** "פעולה" is the ministry word for "פונקציה". We keep the two words parameter / argument apart because it is clearer; say once: "במבחן ובחומרי משרד החינוך קוראים לשניהם 'פרמטר' או 'ערך'". The ministry also says 'הפעולה מקבלת פרמטר' for the value that the call sends.

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
- **`print` shows, `return` hands back.** `print("x")` writes on the screen and the program cannot use it; `return x` gives the value back to the line that called, so it can be printed, stored (`total = add(5, 7)`) or used inside another call (`add(add(5, 6), add(1, 2))`). We already use functions that hand values back: `input()`, `int()`, `randint(...)`.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 24 |
| 1–5 | **Warm-up:** `greet()` always prints `Hello Dana` — how do we greet Noam without a second function? |
| 5–7 | Answer: `def greet(name):` |
| 7–15 | Parameter and argument: `greet("Dana")`, `greet("Noam")`. **Bridge (1 min, inside the 8):** "במבחן קוראים לשניהם 'פרמטר' או 'ערך'"; the function = "פעולה" |
| 15–18 | Trace table: call · value of `name` · output (3 min) |
| 18–22 | A number parameter: `print_stars(amount)` with `"*" * amount` (from 6.2) (4 min) |
| 22–26 | **Predict + answer:** `show(word, times)` prints `word * times`; `show("ab", 3)`, `show("-", 5)` → `ababab`, `-----` (4 min) |
| 26–30 | The order of arguments, ministry "השם שלי": `show_name(first, last)` called with the names swapped; `show_rectangle(8, 3)` vs `(3, 8)` (4 min) |
| 30–34 | Parameter or input? Two rows: input **inside** the function (`name = input(...)` in the body) vs read **outside** and pass in (`name = input(...)` then `greet(name)`, the ministry module-level style) (4 min) |
| 34–38 | **Return-lite:** `def add(x, y): return x + y`; `num = add(5, 7)`; `print(num)`; `print(add(5, 6))`. The one rule: print shows, return hands back (link to `input()`, `int()`, `randint`) (4 min) |
| 38–42 | **Predict:** `print(add(add(5, 6), add(1, 2)))` → 14 (work inside out: 11, 3, then 14); then `sub(10, 4)` and `sub(4, 10)` with `return a - b` → 6, -6, so order matters here too (4 min) |
| 42–44 | `sign_text(number)` with `if / elif / else` returning a string; call it from `print` (2 min) |
| 44–45 | Lab missions |

Minute check: 1 + 4 + 2 + 8 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 2 + 1 = 45 (the 10 minutes freed by trimming the old trace, `print_stars`, predict, order and parameter-or-input slots fund the 10-minute return-lite block 34–44).

---

# 6. Second 45 Minutes — Lab

Starter: [`Parameters_Starter.py`](../exercises/Parameters_Starter.py). Reference: [`Parameters_Reference.py`](solutions/Parameters_Reference.py).

## 45–50 — Warm-up: why does it crash? (5 min)

```python
# Warm-up: why does this program crash?
def welcome(city):
    print("Welcome to", city)


welcome()
```

`TypeError: welcome() missing 1 required positional argument: 'city'`. Fix: `welcome("Haifa")`.

## 50–54 — From input to parameters: `pool(times, price)` (4 min, ministry 4.3 Ex 5)

Take the 8.2 `pool()` that read `times` and `price` inside. Rewrite it as `pool(times, price)`: the numbers come from the call, e.g. `pool(3, 25)`. Contrast: which version can be called twice with different numbers without typing? (the parameter version)

## 54–62 — Task 1: `repeat_message(message, times)` (8 min)

Print the message `times` times with a loop. Call `repeat_message("Go", 4)`.

## 62–72 — Task 2: `draw_square(size)` (Turtle, 10 min)

One function, three sizes: `draw_square(50)`, `draw_square(100)`, `draw_square(150)` — three squares from the same corner.

## 72–82 — Task 3: functions that return a value (10 min)

Replaces `draw_rectangle` (argument order is already covered at 26–30).

- `absolute_value(number)` returns the number without its minus sign. Call: `print(absolute_value(-7))` → 7, `print(absolute_value(4))` → 4.
- `sign_text(number)` returns the string `"positive"`, `"negative"` or `"zero"`. Call it **outside**, in `print(...)`, for 5, -3 and 0.
- Core: both functions return and do **not** print; the printing is in the call line.

**Enrichment / take-home (רשות):** `draw_rectangle(width, height)` — two rounds of width, turn, height, turn; compare `draw_rectangle(140, 70)` with `draw_rectangle(70, 140)`. Also the ministry `subtract` and `average` (see the extra-practice pack, `exercises/Extra_Practice_U8.md`).

## 82–85 — Document and save

Save As `G7_U8_M3_Parameters_<Name>.py`.

## 85–90 — Exit check

1. Where is the parameter written? (in the definition, inside the parentheses)
2. What is an argument? (the value sent in the call)
3. Why does the order of the arguments matter? (the first value goes to the first parameter, and so on)
4. What is the difference between `print` and `return` inside a function? (print shows on the screen; return hands the value back to the call so it can be stored or printed)

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
| `return` prints the value | `return` only hands it back; without `print(...)` around the call nothing appears |
| A function that prints is the same as one that returns | `print` cannot be stored or used in another calculation; `total = add(5, 7)` needs `return` |

---

# 8. Assessment Evidence (formative)

- Two-parameter prediction
- The `TypeError` explained
- `pool(times, price)` converted from input to parameters
- `absolute_value` and `sign_text` called with `print(...)` outside
- Nested-call prediction (14) and print-versus-return exit question
