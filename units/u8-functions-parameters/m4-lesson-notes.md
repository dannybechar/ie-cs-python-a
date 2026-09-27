# Unit 8.4 — Functions with Parameters

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Who Knows This Variable? — Scope, `global` and the Unit Checkpoint (Mission 25)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab with the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit8_meeting4_scope_and_global_final.pptx` (the `make_number()` NameError warm-up, same name inside and outside, reading an outside variable, `global score`, the local vs global table, the `demo()` prediction, the growing Turtle spiral, `draw_square(size)` with a global counter kept; `+=` replaced; the missing-`global` bug and a paper checkpoint added)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | why functions → define vs call → order of execution → no return value | 45 / 45 |
| 8.2 | functions without parameters: split a program, `main()`, input inside a function, Turtle | 0 / 90 |
| 8.3 | parameters and arguments, several parameters, parameter vs input, Turtle sizes | 45 / 45 |
| **8.4 (this)** | **scope: local variables, `global`, Turtle with shared state, unit checkpoint** | 0 / 90 |

This meeting closes Unit 8 and holds its **checkpoint** (practical + theoretical), as the official assessment asks.

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.17) | Covered here |
|---|---|
| 3. Tell the scope of a variable outside and inside a function | ✅ slides 2–9, warm-up |
| Concept: scope — local variable, a variable with `global` | ✅ |
| Teaching: examples of local and `global` variables | ✅ |
| Teaching: functions with/without parameters with Turtle, using a `global` variable | ✅ Task 1, checkpoint A |
| Assessment (theory): a problem solved by calling/writing functions | ✅ checkpoint B |
| Assessment (practical): a function with parameter(s) that returns no value | ✅ checkpoint A |

Official topic and minutes: "function with parameters" — the last 90 of its 135 practice minutes. With this meeting Unit 8 uses exactly its 360 official minutes (90 theory / 270 practice).

### Deliberate exclusions
No `return`, no `nonlocal`. `global` is used only for shared state such as a counter or a growing step.

---

## 3. Lesson Goal

**A variable created inside a function lives only there. To change an outside variable inside a function, declare it `global`.**

---

## 4. Core Mental Models

| | Local variable | `global` variable |
|---|---|---|
| Created | inside a function | outside all functions |
| Known | only in that function | everywhere in the program |
| Changed inside a function | a normal assignment | needs `global name` first |

- **Reading** an outside variable works without `global`; **changing** it needs `global`.
- **Same name inside and outside:** the assignment inside makes a new local variable; the outside one does not change.
- Prefer **parameters** for values a function needs; keep `global` for shared state (a counter, a step that grows).

---

# 5. First 30 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 25 |
| 1–4 | **Warm-up:** `make_number()` sets `x = 10` and prints it; then `print(x)` outside |
| 4–6 | Answer: 10, then `NameError` — `x` is local |
| 6–11 | Same name: `value = 100` outside, `value = 20` inside → `Inside: 20`, `Outside: 100` |
| 11–15 | Reading an outside variable: `school = "Galil"` |
| 15–21 | `global score`: `add_point()` twice → 2 |
| 21–24 | Local vs `global` (table) |
| 24–27 | **Predict:** `value = 7`; `demo()` sets `value = 3` and prints it; then `print(value)` |
| 27–29 | Answer: 3, then 7 |
| 29–30 | Lab missions |

---

# 6. Lab — 60 Minutes

Starter: [`Scope_Starter.py`](Scope_Starter.py). Reference: [`Scope_Reference.py`](Scope_Reference.py).

## 30–35 — Warm-up: why does it crash?

```python
# Warm-up: add_point() should add 1 to score. Why does it crash?
score = 0


def add_point():
    score = score + 1


add_point()
print(score)
```

`UnboundLocalError`: the assignment makes `score` local, and the local one has no value yet. Fix: `global score` as the first line of the body.

## 37–49 — Task 1: a growing spiral (Turtle)

`steps = 40` outside; `grow_step()` declares `global steps`, moves `steps`, turns 90 and adds 15. Call it 6 times in a loop: each side is 15 longer.

## 49–69 — Checkpoint A (practical, alone)

- **A1 — `draw_square(size)`:** draws a square of the given size and adds 1 to a `global` counter `squares_drawn`.
- **A2 — `show_line(symbol, amount)`:** prints `symbol * amount`.
- **`checkpoint()`:** a line of 20 `=`, squares of 40, 70 and 100, `Squares: 3`, and another line.

## 69–79 — Checkpoint B (theory, on paper, no running)

```python
count = 0


def tick(step):
    global count
    count = count + step


tick(2)
tick(5)
print(count)
```

1. What is printed? 2. Which is the parameter, and which are the arguments? 3. What happens if the line `global count` is removed? 4. `def show(a, b): print(a - b)` — what do `show(10, 4)` and `show(4, 10)` print?

## 79–82 — Checkpoint B answers

1. `7`. 2. Parameter `step`; arguments 2 and 5. 3. `UnboundLocalError` — `count` becomes local. 4. `6` and `-6`.

## 82–85 — Document and save

Save As `G7_U8_M4_Scope_<Name>.py`.

## 85–90 — Exit check

1. Where is a local variable known? (only inside its function)
2. When do we need `global`? (to change an outside variable inside a function)
3. `calls = 0`; a function adds 1 with `global calls`; it is called 3 times — what is printed? (3)

### Tool Note – Thonny
The Variables view (View › Variables) shows the global variables after each run.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A variable made in a function is known everywhere | Only inside that function |
| The inner `value = 3` changes the outer `value` | It makes a new local variable |
| `global` is needed to read an outside variable | Only to change it |
| Use `global` for everything | Prefer parameters; keep `global` for shared state |

---

# 8. Assessment Evidence

- Scope predictions (formative)
- **Checkpoint A** (practical): `draw_square(size)` with a global counter, `show_line(symbol, amount)`
- **Checkpoint B** (theoretical): trace with `global`, parameter vs argument, argument order
- Exit check
