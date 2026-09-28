# Unit 2.2 — Turtle & Graphics

## Grade 7 / Python A · Lesson Strategy v2
### Topic: Pen, Appearance and Stamps

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab: three short demos (4–5 min each), each followed immediately by a task  
**Minutes (theory / practice):** 0 / 90  
**Current tool assumption:** Thonny  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 2

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 2.1 | Move → Turn → Predict → Build | 45 / 45 |
| **2.2 (this)** | **movement → pen state → appearance → marker** | 0 / 90 |
| 2.3 (built) | Read → Predict → Debug → Modify → Build → Explain; rectangle micro-assessment | 0 / 90 |

M2 adds the rest of the commands M3 expects: `penup`, `pendown`, `pencolor`, `pensize`, `stamp`, `hideturtle`, `showturtle`, plus `shape` with other shapes. M3's integrated path (stamp → line → pen up → move → pen down → line) must feel familiar after today.

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 2 (python-a.pdf p.7):

| Official goal / concept | Covered here |
|---|---|
| 2. Document code | ✅ one comment above each task's function |
| 5. Change graphic attributes: cursor type, pen thickness, pen color | ✅ `shape`, `pensize`, `pencolor` |
| 6. Use shape attributes: hiding, leaving a stamp | ✅ `hideturtle`, `showturtle`, `stamp` |
| 7. Up to 8 simple sequential instructions | ✅ the exit check and task C; tasks A–B are practice and a little longer |
| Concept: work surface and pen | ✅ pen up / pen down |
| Concept: retrieve / update operations (פעולות אחזור/עדכון) | ✅ `turtle.pensize(8)` updates; `turtle.pensize()` retrieves, shown with `print` |

Official topics and minutes used: "work surface and pen" (45 practice) and "changing shape attributes" (45 practice).

### Deliberate exclusions

Same as M1: no `backward()`, `goto()`, coordinates, `heading()`/`position()`, `circle()`, `fillcolor`/`begin_fill`, `speed()`, variables, `input()`, loops, conditions, our own function parameters, return values, events, classes.

> Stamps are drawn with the turtle's **fill** color, which stays black. Colored stamps need `fillcolor`/`color`, which we keep out of Unit 2.

---

## 3. Lesson Goal

Students control **what** the turtle leaves behind, not only **where** it goes: pen up/down, pen color and size, turtle shape and visibility, and stamps. They learn that these settings **stay on until changed**, just like position and direction.

Core workflow:

**Read → Predict (sketch, with colors) → Run → Check → Fix → Document**

### One function per task (the Unit 1 pattern)

Every task is written as its own function with no parameters, and **only one call is active at a time**; the other calls stay as comments:

```python
def dashed_road():
    ...

def color_square():
    ...

# dashed_road()
color_square()
```

Why:

- **Each run starts fresh.** The turtle's settings from one task (pen size 5, orange, pen up) cannot leak into the next, so every prediction is deterministic.
- **All the day's work stays in one file,** with one comment above each function.
- **It reinforces Unit 1:** define → call → execute, indentation, and "turning off" a line with `#`.

Student rule: **בכל פעם מפעילים רק משימה אחת. שאר הזימונים נשארים כהערות.**

---

## 4. Student-Facing Objectives

Students should be able to:

1. Use `penup()` and `pendown()` to move with or without drawing.
2. Change the pen with `pencolor("...")` and `pensize(...)`.
3. Change how the turtle looks with `shape("...")`, `hideturtle()` and `showturtle()`.
4. Leave a mark with `stamp()`.
5. Explain that a setting stays on until it is changed.
6. Tell the difference between **updating** a setting (`turtle.pensize(8)`) and **retrieving** it (`print(turtle.pensize())`).
7. Organize each task as its own function and run one at a time.
8. Document each part of a program with a comment.

---

## 5. Core Mental Models

### The turtle carries a pen, and the pen has a state
Pen up or down, its color and its size are all part of the turtle's state. Each stays as it is until an instruction changes it.

### A moving turtle with the pen up leaves no line, but it still moves
Pen up changes what is drawn, not where the turtle goes.

### Changing the color while the pen is up still counts
The next line drawn after `pendown()` uses the latest color.

### Colors and shapes are text, so they need quotes
`pencolor("red")` — with quotes. `pencolor(red)` gives `NameError: name 'red' is not defined`, exactly like `print(cat)` in Unit 1. A misspelled color gives `TurtleGraphicsError: bad color string`.

### Update vs. retrieve
Use the Ministry's words, **עדכון / אחזור**, not "מחזירה" (return values are not taught in Python A):

> **כשיש ערך בסוגריים — משנים. כשהסוגריים ריקים — שואלים מה הערך עכשיו.**

---

# 6. Lesson Flow (Lab + Lab)

Starter file: `TurtlePenStamp_Starter.py`. It already contains the warm-up as a function, `warm_up()`, and a call to it.

### Tool Note – Thonny

- Close the drawing window before running again.
- `print(...)` output appears in Thonny's **Shell**, not in the drawing window.
- After typing `def ...:` and pressing Enter, Thonny indents the next line automatically. Press Backspace to leave the function.

---

## 0–8 min — Warm-up: Predict

Students open the starter and **don't run it yet**:

```python
def warm_up():
    turtle.forward(60)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(60)
```

Ask: **What will we see?** Let them guess what `penup` means from its name. Then run.

Expected: two lines of 60 with a gap of 40 between them. The turtle moved 160 in total.

Point at the bottom of the file: **"Each task gets its own function. We run one task at a time."**

---

## 8–12 min — Demo 1: Pen State

Say one sentence each:

- `penup()` lifts the pen: the turtle moves without drawing.
- `pendown()` puts it back: drawing starts again.
- **The pen stays up until you put it down.** Forgetting `pendown()` is the most common bug today.

---

## 12–25 min — Task A: Dashed Road

Specification: a straight dashed road with **3 dashes**, each 30 long, with gaps of 15.

Students write a new function `dashed_road()` above the calls, turn `warm_up()` into a comment, and call `dashed_road()`. Before running, they draw the road on paper with the numbers.

Reference (9 instructions):

```python
# Task A: dashed road
def dashed_road():
    turtle.forward(30)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.forward(30)


# warm_up()
dashed_road()
```

Debug prompt for early finishers: **delete the second `pendown()` — predict first, then run. How many dashes now?** (Only one dash; the pen never comes back down.)

---

## 25–30 min — Demo 2: Appearance

Show, one line at a time:

```python
turtle.pensize(5)
turtle.pencolor("red")
turtle.shape("arrow")
turtle.hideturtle()
```

Then ask: **איך לדעתכם נחזיר אותו?** Let a student suggest `turtle.showturtle()`. **Everyone types `hideturtle()` and `showturtle()` once** in their current task and runs it.

- Shapes available: `"arrow"`, `"turtle"`, `"circle"`, `"square"`, `"triangle"`, `"classic"`.
- Colors are English names in quotes: `"red"`, `"blue"`, `"green"`, `"orange"`, `"purple"`, `"black"`.
- Show the two errors: `pencolor(red)` → `NameError` (like `print(cat)`); `pencolor("bluee")` → `bad color string`.

---

## 30–45 min — Task B: Color Square

Specification: a 100 × 100 square with a thick pen (size 5), each side a different color, ending in the starting direction. Hide the turtle at the end so only the drawing shows.

Reference:

```python
# Task B: color square
def color_square():
    turtle.pensize(5)
    turtle.pencolor("red")
    turtle.forward(100)
    turtle.left(90)
    turtle.pencolor("blue")
    turtle.forward(100)
    turtle.left(90)
    turtle.pencolor("green")
    turtle.forward(100)
    turtle.left(90)
    turtle.pencolor("orange")
    turtle.forward(100)
    turtle.left(90)
    turtle.hideturtle()
```

Ask: **Where must each `pencolor` go: before or after its `forward`?** (Before, because the color is used for the next line drawn.)

---

## 45–50 min — Demo 3: Stamps

`stamp()` prints a copy of the turtle's shape where it stands. It stays on the screen even after the turtle moves on or hides.

Show: `turtle.shape("circle")`, `turtle.stamp()`, move, `turtle.stamp()`.

---

## 50–65 min — Task C: Stepping Stones (אבני קפיצה)

Specification: three round stones in a row, 50 apart, with **no line** between them. At the end, only the stones are visible. Use at most 8 instructions.

Reference (8 instructions):

```python
# Task C: stepping stones
def stepping_stones():
    turtle.shape("circle")
    turtle.penup()
    turtle.stamp()
    turtle.forward(50)
    turtle.stamp()
    turtle.forward(50)
    turtle.stamp()
    turtle.hideturtle()
```

Ask: **Why is there no line between the stones?** (The pen is up.) **Why are there three circles if the turtle is hidden?** (Stamps stay.)

Extension (no new commands): turn 90° between stones to make an L-shaped path of 5 stones.

---

## 65–75 min — Task D: Update vs. Retrieve

Students write a new function and make it the **only active call**, so the turtle starts with its default settings:

```python
# Task D: update or retrieve?
def read_the_pen():
    print(turtle.pensize())
    turtle.pensize(8)
    print(turtle.pensize())
    print(turtle.pencolor())


# warm_up()
# dashed_road()
# color_square()
# stepping_stones()
read_the_pen()
```

Before running, students write what the Shell will show. Output (checked in Python 3.14, fresh run):

```text
1
8
black
```

Explain:

> **כשיש ערך בסוגריים — משנים (עדכון). כשהסוגריים ריקים — שואלים מה הערך עכשיו (אחזור).**

Ask: **Why is the color `black`, when Task B used orange?** (Only `read_the_pen()` runs. Each run starts fresh with the default settings.)

---

## 75–82 min — Document and Save

Students check that every function has a one-line comment above it, and that only one call is active.

Save As: `G7_U2_M2_PenAndStamp_<Name>.py`

---

## 82–90 min — Exit Check

Show:

```python
turtle.pencolor("red")
turtle.forward(50)
turtle.penup()
turtle.pencolor("blue")
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
```

1. How many lines are visible? (**2**)
2. What color is each? (**first red, second blue**, because the color changed while the pen was up)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `penup` stops the turtle | It still moves, it just doesn't draw |
| A setting applies to one line only | It stays on until changed: pen, color, size |
| Changing color with the pen up does nothing | The new color is used for the next line drawn |
| A hidden turtle erases its stamps and lines | Hiding only hides the cursor |
| `pencolor(red)` is fine without quotes | Names like `red` without quotes are treated as variables: `NameError` |
| `pencolor` after `forward` colors that line | The color is used for the **next** line |
| Settings from the previous task are still on | Each run starts fresh; only the active call runs |

---

# 8. Assessment Evidence (formative)

- Predictions before running, with colors marked
- Task A: 3 dashes, pen restored each time
- Task B: correct colors in order, thick pen, turtle hidden, facing the start direction
- Task C: 3 stones, no lines, within 8 instructions
- Task D: correct Shell prediction and the update/retrieve sentence
- One function per task, one comment per function, one active call; correct Save As
- Exit check answers

---

# 9. Differentiation

**Support:** a checklist card of the pen state ("up/down · color · size") that students update after each line; start Task B with only two colors; if writing a new function is hard, the student copies the `warm_up()` function and edits it.

**Extension (no new commands):** a "space mission map" using stamps (`shape("triangle")` as the rocket, `shape("circle")` as planets) and a dashed route between them, as one more function.

---

# 10. Link to Meeting 3

M3 opens with an integrated path: stamp → line → turn → pen up → move → pen down → turn → line. After today, every command in it is familiar, including `showturtle()`, which everyone typed in Demo 2. M3 adds no new commands.
