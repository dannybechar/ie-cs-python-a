# G7 Unit 1 Lesson Strategy v5

## Grade 7 / Python A
### Unit 1 — Introduction to Python
### Meeting 1 — My First Program (Missions 1+2)

**Status:** Rewritten to match the class slide deck [`m1-slides-he.pdf`](m1-slides-he.pdf) (20 slides)  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice (slides 1–13), then 45 min Lab (slides 14–20)  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny (installed in [Unit 0](../u0-environment-setup))  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Scope

From the Ministry program, Chapter 1 (python-a.pdf p.6), with installing and touring the environment already done in Unit 0:

- sequential instructions: the program starts at the first line and runs in order
- `print()` output
- comments with `#`, including "turning off" a line
- reading error messages: `NameError`, `SyntaxError`, `IndentationError`
- a function with no parameters and no return value: define → call → execute
- indentation marks the lines that belong to the function
- predict output before running

Do not introduce variables, `input()`, arithmetic, conditions, loops, parameters, `return`, or formal scope.

**Not covered here (open gap in the course map):** compound output — several values in one `print`. Add it here or in Unit 3 Meeting 1.

---

## 2. Lesson Goal

**Read → Predict → Run → Check → Modify → Comment → Save** (קוראים ← חוזים ← מריצים ← בודקים ← משנים ← מתעדים ← שומרים)

Two missions:
- **Mission 1 — launch control training:** programs run top to bottom; `print`; comments; reading errors.
- **Mission 2 — building our own commands:** functions, define → call → execute, indentation.

---

## 3. Student-Facing Objectives

Students should be able to:

1. Explain that a program starts at the first line and runs in order.
2. Use `print` to show output, and predict the exact output of short programs.
3. Write a comment with `#`, and use `#` to turn a line off without deleting it.
4. Read an error message, find the line, and fix it (the four errors on slide 7).
5. Define a function with `def` and indentation, and explain why a definition alone prints nothing.
6. Call a function, and trace the order in which lines run when calls and definitions are mixed.
7. Save a file under a new name.

---

## 4. Core Model

### Sequential execution
Python starts at the first line of the file and goes down, line by line, to the end.

### Output
`print("Hello!")` shows `Hello!` — the text only. The quotes say "this is text"; they are not printed.

### Comments
A line that starts with `#` is an explanation for people; Python skips it. `#` at the start of a line "turns it off" without deleting it.

### Functions: define → call → execute
- **Define (הגדרה):** write the recipe. A definition alone prints nothing — "like a recipe: we haven't cooked anything yet".
- **Call (זימון):** write the name with brackets: `cheer()`.
- **Execute (ביצוע):** the lines inside the function run — each time it is called.

Beginner-safe indentation wording:

> **השורות ששייכות לפונקציה זזות פנימה ומיושרות באותה צורה.**

When Python reaches `def`, it only remembers the function and skips its body. The body runs only when the function is called.

---

# 5. First 45 Minutes — Knowledge + Guided Practice (slides 1–13)

| Clock | Slide | Activity | Min |
|---|---|---|---:|
| 0–1 | 1 | Title: "משימות 1+2" | 1 |
| 1–5 | 2 | **Predict:** the countdown `3, 2, 1, Liftoff!`. Students write the output in their notebooks before anything runs | 4 |
| 5–10 | 3 | Answer + where the program starts; anatomy of `print("Hello!")`: command name (lowercase!), brackets, string in quotes, output without the quotes | 5 |
| 10–17 | 4 | **Students:** type the countdown in a new file, run (F5), start it from 5, change `Liftoff!` to their own message, predict what happens if the message moves to the first line, then Save As `rocket.py` | 7 |
| 17–20 | 5 | **Predict:** the secret robot — which lines will print? (two lines start with `#`) | 3 |
| 20–22 | 6 | Answer: only `Hello, human!` and `I come in peace.` Comments are skipped; `#` turns a line off. Bonus box: "break it on purpose" — **only if time** | 2 |
| 22–25 | 7 | The four errors we met (table below) | 3 |
| 25–28 | 8 | Why functions? The same two cheer lines written three times — "and what if we want 100 times?" | 3 |
| 28–30 | 9 | **Predict:** `def cheer():` with two prints and no call — what prints? | 2 |
| 30–33 | 10 | Answer: **nothing!** Anatomy: `def`, the name, `()`, the colon, indentation | 3 |
| 33–35 | 11 | **Predict:** the same definition plus `cheer()` twice | 2 |
| 35–37 | 12 | Answer: four lines, the pair twice. Space dictionary: define / call / execute | 2 |
| 37–45 | 13 | **Students:** type only the definition and run (nothing); leave the indentation with Backspace, add `cheer()`, run; predict three calls, run | 8 |

### The four errors (slide 7)

| What we wrote | What Python says | Fix |
|---|---|---|
| `print(cat)` | `NameError: name 'cat' is not defined` | Put quotes around the text |
| `print("Hello)` | `SyntaxError: unterminated string literal` | Close the quotes |
| `print("Hello"` | `SyntaxError: '(' was never closed` | Close the bracket |
| `Print("Hello")` | `NameError: name 'Print' is not defined` | Lowercase `print` |

All four messages checked in Python 3.14. Python 3.14 adds `Did you mean: 'print'?` to the last one — worth pointing out.

### Tool Note – Thonny
- F5 runs the file; output appears in the Shell.
- After `def ...:` and Enter, Thonny indents automatically; press **Backspace** to leave the function (slide 13, step 3).

---

# 6. Second 45 Minutes — Lab (slides 14–20)

| Clock | Slide | Activity | Min |
|---|---|---|---:|
| 45–50 | 14 | **Inside or outside?** Type `hello()` with `print("Hello!")`; add `print("Bye!")` inside with the same indentation and a call `hello()` at the end, run; then un-indent the Bye line — **predict first**, then run | 5 |
| 50–52 | 15 | Answer: the red example (no indentation) gives `IndentationError`; the green example prints `Bye!` then `Hello!` — Bye is no longer part of the function, so it runs immediately, before the call | 2 |
| 52–55 | 16 | **Predict:** the dragon story — the order of the 5 output lines | 3 |
| 55–57 | 17 | Answer, with the route arrows. "When Python sees `def`, it only remembers the function and skips its body" | 2 |
| 57–77 | 18 | **Launch challenge**, 6 steps (below) | 20 |
| 77–84 | 19 | **Exit mission:** a program that introduces you (below) | 7 |
| 84–85 | 20 | Summary: "I know…" and the work cycle | 1 |
| 85–90 | — | Buffer: late saves, questions | 5 |

### Slide 15 examples (verified)

```python
def hello():
print("Hello!")
```

```text
IndentationError: expected an indented block after function definition on line 1
```

```python
def hello():
    print("Hello!")
print("Bye!")
hello()
```

```text
Bye!
Hello!
```

### Slide 16–17: the dragon story (verified)

```python
print("Once upon a time...")

def dragon():
    print("ROAR!")
    print("The dragon wakes up")

print("A knight enters the cave")
dragon()
print("The end")
```

```text
Once upon a time...
A knight enters the cave
ROAR!
The dragon wakes up
The end
```

### Slide 18: launch challenge — 6 steps

1. Open `rocket.py` from the start of the lesson (`File › Open`) and Save As `G7_U1_Rocket_<Name>.py`.
   If a student's `rocket.py` is missing, they open [`Rocket_Starter.py`](Rocket_Starter.py) instead.
2. Add `def launch():` above the countdown and indent all the countdown lines, including Liftoff. Run: **nothing is printed** — we only defined it.
3. Add the call `launch()` at the end, with no indentation. Run.
4. Add a second `launch()`. Predict how many times the countdown prints; run and check.
5. Add `print("Ignition!")` inside the function, before the first number. Run.
6. Un-indent the Liftoff line and predict when it appears now; run. (It prints **first, once** — before both countdowns, because it is no longer part of the function.) Restore the indentation, turn off one call with `#`, add a comment at the top that explains the program, and save.

Finished program: [`Rocket_Reference.py`](Rocket_Reference.py).

Bonus: define `draw_rocket()` with drawing lines inside (ASCII art with `print`), and call it after `launch()`.

### Slide 19: exit mission (7 minutes, alone)

A new file with a function `introduce_me()` that prints the student's name and something they like, with a `print` before the call and after it. Predict the output order, then run.
Save As `G7_U1_FirstProgram_<Name>.py`.

Model (on the slide) and reference: [`FirstProgram_Reference.py`](FirstProgram_Reference.py):

```text
Start
Ready
My name is Dana
I like basketball
End
```

Ask 2–3 students orally: **Why didn't the lines inside `introduce_me()` run when Python reached the definition?**

---

# 7. Timing Priorities

The lab has no spare block except the 5-minute buffer. If the class runs late:

| Must complete | Cut first |
|---|---|
| Slides 13, 14–15, 18 steps 1–4, 19 | Slide 6 bonus ("break it on purpose"), slide 18 steps 5–6, the `draw_rocket()` bonus |

The exit mission (slide 19) is the assessment evidence — protect it.

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| The quotes are printed too | `print` shows only the text inside the quotes |
| Comments appear in the output | Lines starting with `#` are for people; Python skips them |
| Order doesn't matter | Predict, reorder, run again — the output order follows the code order |
| The function runs when it is defined | A definition is a recipe; the body runs only when called |
| A function runs once no matter how many calls | Each call runs the whole body again |
| Indentation is decorative | It decides which lines belong to the function (slide 15) |
| `Print` and `print` are the same | Python is case-sensitive: `NameError` |
| Thonny is Python | Thonny is the tool; Python is the language (Unit 0) |

---

# 9. Assessment Evidence

- Written predictions before running (slides 2, 5, 9, 11, 14, 16)
- `rocket.py` saved and changed (slide 4)
- `G7_U1_Rocket_<Name>.py` with `def launch():` and a call (slide 18)
- `G7_U1_FirstProgram_<Name>.py` with `introduce_me()`, a correct output prediction, and an oral explanation of definition vs call (slide 19)

Do not use a vocabulary quiz as the main assessment.
