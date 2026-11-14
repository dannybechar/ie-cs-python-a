# Unit 2 Addendum — Coordinates and the Exam Notation

## Grade 7 / Python A · Addendum session (Phase 5, written after Meetings 2.1–2.3 were taught)

**Duration:** 45 minutes, one session.
**When:** after 2.3 and the Unit 2 tests, or as the opening of the first later meeting that uses the turtle. It is **not** part of the three taught minute plans (45 + 45 each, still 90 and unchanged) and **not** part of the official 270 minutes of Unit 2: it is an addendum for classes that were already taught (audit `audit-u2.md`, findings U2-01 to U2-05, U2-08, U2-09; teacher rulings D3 and D5). For classes that have not yet taken Unit 2, the same content can go to the extras session; do not squeeze it into 2.1–2.3.
**Student material:** [`L04-coordinates-and-exam-notation.md`](../lessons/L04-coordinates-and-exam-notation.md). **Code:** [`exercises/Coordinates_Starter.py`](../exercises/Coordinates_Starter.py) / [`solutions/Coordinates_Reference.py`](solutions/Coordinates_Reference.py), [`exercises/ExamDialect_Starter.py`](../exercises/ExamDialect_Starter.py) / [`solutions/ExamDialect_Reference.py`](solutions/ExamDialect_Reference.py), extra 11 (`11_QuadrantSquares.py`).

## Minute plan (sums to 45)

| Time | Min | Block | Kind | Audit id |
|---|---:|---|---|---|
| 0–5 | 5 | Paper warm-up: mark points on the axes, name the quadrant; the four defaults (shape arrow/turtle, black, position (0, 0), facing right) | unplugged | U2-02, U2-09 |
| 5–15 | 10 | Coordinates block: `goto`, `setx`, `sety`, `position()`, `penup`/`pendown` to jump; Coordinates tasks A–C | demo → task | U2-02 |
| 15–18 | 3 | Short names (`fd lt rt bk pu pd`, read-only table) and `backward(n)` | demo | U2-03 |
| 18–21 | 3 | `color("red")` sets line and turtle together; `pencolor` = the line only; one hex code | demo | U2-04 |
| 21–26 | 5 | `begin_fill` / `fillcolor` / `end_fill` with the open-shape question; `turtlesize` | demo → task | U2-05 |
| 26–31 | 5 | Optional: types of angles (acute, right, obtuse) — cut first if time is short | task | U2-08 |
| 31–41 | 10 | Translation drill: the same program in class style and exam notation; read-only questions | drill | U2-01 |
| 41–45 | 4 | Exit check (two lines each: a coordinate question and an exam-notation question) and buffer | check | — |
| | **45** | | | |

Rhythm follows the course rule: no teacher talk longer than 10 minutes without a student action. The longest talk here is the 3-minute demos. If the session is cut to 35 minutes, drop the angle block (5) and the fill demo (5); keep coordinates and the translation drill, which close blocking findings.

---

## 0–5 min — Paper warm-up (no computer)

On the board draw the axes. Say: **"The window is a grid. The turtle always knows where it stands: two numbers, (x, y). The turtle starts at (0, 0), in the middle, facing right."**

Students mark on paper (students use squared paper): (2, 4), (−3, 5), (4, −2), (0, 0). Then name the quadrant of each (1: x > 0, y > 0; 2: x < 0, y > 0; 3: both negative; 4: x > 0, y < 0). Points on the axes belong to no quadrant.

In the grid 1 unit on paper stands for 50 steps on the screen if the class wants to link to the lab sheets; otherwise 1 unit = 1 step (the code uses steps).

Defaults, 30 seconds: **shape classic (arrow) · color black · position (0, 0) · facing right (east).** (`turtle.shape("turtle")` was our choice in 2.1.)

## 5–15 min — Coordinates block

**Demo (4 min, live in Thonny).** Starter `Coordinates_Starter.py`, function `warm_up`. Before running ask: "Where will the turtle be after each line?" Students write the four points. Run it: it draws a rectangle, and the turtle ends at (0, 0) facing right (`goto` moves, it does **not** turn).

Key sentences:

- `turtle.goto(x, y)` moves the turtle to the point; **if the pen is down, moving draws a line**. (Same as `forward`: moving with the pen down draws.)
- To jump without a line: `penup()`, `goto(...)`, `pendown()` — the same pen idea as in 2.2.
- `turtle.setx(x)` changes only the x coordinate, `turtle.sety(y)` only y. The other coordinate stays.
- `turtle.position()` retrieves the position; `print(turtle.position())` shows it, like `pensize()` in 2.2 (retrieve vs update). Long names `setposition`/`setpos` and the short `pos` exist; read-only.

**Tasks (6 min, one function each, as in 2.2):** A (jump then draw a line), B (square with `setx`/`sety` only), C (square in quadrant 2). Task D (four squares in four quadrants) is the extension; extra 11 is the home version.

Common errors: `goto(100 50)` or `goto(100; 50)` (comma, like in `print`); `penup(x, y)` (it takes no arguments; the ministry deck contains this typo, do not copy it); forgetting `pendown()` after the jump; thinking `goto` turns the turtle.

Do not introduce `setheading`, `xcor`/`ycor`, `distance` (later or enrichment). Do not teach `goto` with variables (Unit 3).

## 15–18 min — Short names and `backward`

Show the read-only table on the handout:

| Long | Short |
|---|---|
| `forward` | `fd` |
| `backward` | `back`, `bk` |
| `left` | `lt` |
| `right` | `rt` |
| `penup` | `pu`, `up` |
| `pendown` | `pd`, `down` |

"We write the long names, because they explain themselves. The exam may print the short ones, so you must be able to read them." `turtle.backward(50)` moves backward **without turning** and draws if the pen is down. Demo 2 min: the square with one side drawn by `backward`. Stress: the short names are the same commands, only shorter.

## 18–21 min — `color()` next to `pencolor()`

- `turtle.pencolor("red")` — only the line.
- `turtle.color("red")` — the line **and** the turtle (and its stamps). This is the everyday command in the exam material.
- With a single argument `color` sets both. The two-argument form `color("red", "yellow")` (line, fill) is read-only here.
- A hex color code in quotes works too: `"#1AA260"`. Mention once.

Link to the 2.2 note ("stamps are black"): with `color("red")` the stamps are red. Quick demo: `color("red")`, `shape("turtle")`, `stamp()`. Unit 9 already uses `color`: this closes that inconsistency.

## 21–26 min — Fill and `turtlesize`

Demo, closed triangle: `fillcolor("yellow")`, `begin_fill()`, three sides, `end_fill()`. Then the question: **"What happens if the shape is not closed?"** Run it with a missing last side: Python closes the shape by a straight line for the fill only. Students predict first.

`turtlesize(2)` makes the turtle bigger (this is `turtlesize(stretch)`, one number). Extras 03 and 07 already use fill; this block gives them their missing explanation.

## 26–31 min — Types of angles (optional, cut first)

Ministry task adapted without input and without `if`: draw three angles from the same corner, **each in its own function**: right angle (turn 90), acute angle (drawn angle 35°, so the turtle turns 145), obtuse angle (drawn angle 135°, so the turtle turns 45). It tests the central idea of 2.1: **the turtle turns the outside angle**; the angle drawn inside the corner is 180 minus the turn. Each function is run on its own from a fresh start (turtle at (0, 0), facing right): forward(80), left(turn), forward(80). Students predict which one looks sharp, which one wide, before running.

## 31–41 min — The exam notation: translation drill

**Say (2 min):** "In class we write `turtle.forward(100)`. In the national exam the window and the turtle get names, and commands are written after the turtle's name. It is the same turtle, the same commands; only the notation changes." Show side by side (handout page 2):

| Class notation | Exam notation |
|---|---|
| `import turtle` | `import turtle` |
| `turtle.Screen()` | `wn = turtle.Screen()` |
| (the turtle already exists) | `pen = turtle.Turtle()` |
| `turtle.forward(100)` | `pen.forward(100)` |
| `turtle.pencolor("red")` | `pen.pencolor("red")` |
| `turtle.done()` | `wn.mainloop()` |

Say: `wn` and `pen` are **names** for the window and the turtle (like a name on a drawer); the names can be anything (`player`, `t`). Real work with names is Unit 3: today it is only notation. The exam also uses the short names (`pen.fd(100)`).

**Student action (8 min), `ExamDialect_Starter.py`:** Part 1 run in class style; Part 2 translate it into the exam notation; Part 3 read exam-style code (equilateral triangle, `rt(120)`) and rewrite it in class style, saying first what it draws. Then three read-only questions on the board (no computer), for example:

1. `pen.fd(50)`, `pen.lt(90)`, `pen.fd(50)`: what is drawn, where is the turtle facing? (L shape, facing up.)
2. After `pen.pu()`, `pen.goto(-50, 0)`, `pen.pd()`, `pen.fd(100)`: what is drawn? (A horizontal line from (−50, 0) to (50, 0).)
3. `pen.bk(30)` at the start: where is the turtle? ((−30, 0), facing right.)

**Terminology bridge:** the exam says "פעולה" for what we call a function (a "פעולה" is a function in the ministry wording: `pen.forward(100)` is "a turtle action"). Mention in one sentence; do not drill.

Mixed notation is allowed only in the drill: do not mix styles inside one program (`pen.forward` and `turtle.forward` together in one file confuses the reader). Using `turtle.Screen()` unassigned plus `pen = turtle.Turtle()` works, but avoid it.

**Reuse:** this notation is used again in the Unit 6 and Unit 9 checkpoints (a short exam-style translation block). The teaching style in all other units stays module-level (approved deviation, see `unit-strategy.md`).

## 41–45 min — Exit check

Two items, answered on paper: (1) "The turtle is at (0, 0) facing right. Write the line that moves it to the middle of quadrant 3 without drawing." (`penup()` then `goto(-50, -50)` and `pendown()`; check that the pen is lifted.) (2) "Write `turtle.left(90)` in exam notation." (`pen.left(90)` or `pen.lt(90)`). Collect the two answers.

---

## For the teacher: where the exercises stand

| File | Content | Needs |
|---|---|---|
| `Coordinates_Starter.py` / `Coordinates_Reference.py` | warm-up and tasks A–D | this addendum (5–15 min) |
| `ExamDialect_Starter.py` / `ExamDialect_Reference.py` | translation parts 1–3 | this addendum (31–41 min) |
| `11_QuadrantSquares.py` / solution | four squares in four quadrants | coordinates block; home or extras session |
| Extras 01, 03–10 | `goto` is used in 01, 03, 04, 05, 06, 07, 08, 09, 10 | **the coordinates block**; assign the extras only after it (see README) |

Ministry source defects not copied: `penup(x, y)` / `pendown(x, y)` (slide 11 of meeting 14; both take no arguments), `hideTurtle`/`shoTurtle` (slide 36; correct names are `hideturtle`/`showturtle`).
