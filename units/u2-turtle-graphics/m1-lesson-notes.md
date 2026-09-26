# G7 Unit 2 Meeting 1 Lesson Strategy v2

## Grade 7 / Python A
### Unit 2 — Turtle & Graphics
### Meeting 1 — First Moves

**Status:** Revised after external review (v2)  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45 — this meeting carries all of Unit 2's official theory time  
**Current tool assumption:** Thonny  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 2

Unit 2 has 6 academic hours (1 theory, 5 practice) across 3 double meetings:

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **M1 (this)** | **Move → Turn → Predict → Build** | 45 / 45 |
| M2 | movement → pen state → appearance → marker | 0 / 90 |
| M3 (built) | Read → Predict → Debug → Modify → Build → Explain; rectangle micro-assessment | 0 / 90 |

M3 assumes students already know: `import turtle`, `turtle.Screen()`, `turtle.shape("turtle")`, `forward`, `left`, `right`, `penup`, `pendown`, `pencolor`, `pensize`, `stamp`, `hideturtle`, `showturtle`, `turtle.done()`. M1 teaches the first half of that list; M2 teaches the rest.

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 2 (python-a.pdf p.7):

| Official goal | Covered here |
|---|---|
| 1. Import the Turtle graphics library | ✅ `import turtle` |
| 2. Know the purpose of documenting code; document code | ✅ a top comment, and one comment per part |
| 3. Define the basic graphic elements: window (Screen) and turtle (cursor) | ✅ |
| 4. Call movement functions with a parameter: direction, angle, number of sides | ✅ `forward`, `left`, `right`; square (4 sides) vs triangle (3 sides) |
| 5–6. Change shape attributes; use hiding, stamping | ➡️ Meeting 2 |
| 7. Write a code segment of up to 8 simple sequential instructions | ✅ every task stays within 8 movement/turn instructions |

Official topics and minutes used: "the turtle library" (45 theory + 45 practice) and the start of "movement, position and direction".

Prior knowledge from Units 0–1: Thonny, open/run/save, `print("...")`, comments with `#`, reading error messages, define → call → execute for a function with no parameters.

### Deliberate exclusions

Do not introduce: `backward()`, `goto()`, coordinates, `heading()`/`position()`, `circle()`, fill, `speed()`, variables, `input()`, loops, conditions, parameters of our own functions, return values, events, classes.

> Loops are the obvious temptation here ("the square repeats 4 times!"). Say: **"You spotted a pattern. In Unit 5 we'll teach Python to repeat. Today we write every step."**

---

## 3. Lesson Goal

Students write, predict and correct short Turtle programs, knowing that each instruction starts from where the previous one left the turtle: its **position and direction**.

Core workflow:

**Read → Predict (sketch) → Run → Check → Fix**

---

## 4. Student-Facing Objectives

Students should be able to:

1. Explain what `import turtle`, `turtle.Screen()` and `turtle.done()` do.
2. Use `forward(distance)` to move the turtle and draw.
3. Use `left(angle)` and `right(angle)` to turn in place, relative to the direction the turtle is facing.
4. Predict and sketch the path and the final direction of a short program before running it.
5. Build a square and a triangle, and explain why the triangle turns 120° and not 60°.
6. Keep a program within 8 movement/turn instructions.
7. Add a comment that explains what the program draws.

---

## 5. Core Mental Models

### The turtle has a state: where it is and which way it faces
It starts in the middle of the window, facing right. Each instruction starts from the state the previous one left.

### `forward` moves; `left`/`right` only turn
A turn does not move the turtle or draw anything.

### Left and right are the turtle's left and right, not the screen's
When the turtle faces down, `left(90)` makes it face **right** on the screen.

### Numbers without quotes
`print("Hello")` needed quotes because it was text. `forward(100)` is a number, so no quotes: `forward("100")` is an error.

### The angle is how much the turtle turns, not the angle inside the shape
For a triangle with equal sides, each corner inside is 60°, but the turtle must turn 120°.

---

# 6. First 45 Minutes — Knowledge + Guided Practice

## 0–7 min — Hook: The Human Turtle (unplugged)

One volunteer is the "turtle" and stands facing the class's right-hand wall. The class gives commands, one at a time:

- "forward 3 steps"
- "turn right 90"
- "forward 2 steps"

The turtle obeys literally. Then ask the class to give commands that bring the turtle back to where it started, **facing the same way**.

Key message:

> **The turtle only knows two things: where it is and which way it faces. Every command changes one of them.**

---

## 7–14 min — The Parts of a Turtle Program

Show on the projector:

```python
# My first Turtle drawing
import turtle

turtle.Screen()
turtle.shape("turtle")

turtle.forward(100)

turtle.done()
```

Explain each line in one sentence:

| Line | Meaning |
|---|---|
| `import turtle` | Bring in the Turtle library, a toolbox of drawing commands |
| `turtle.Screen()` | Open the drawing window (the work surface) |
| `turtle.shape("turtle")` | Show the cursor as a turtle, so we can see which way it faces |
| `turtle.forward(100)` | Move forward 100 steps and draw a line |
| `turtle.done()` | Keep the window open until we close it |

Run it. Point out: the turtle starts in the middle, facing right.

Connect to Unit 1: **the comment on the first line** says what the program draws; Python skips it.

Ask (30 seconds, take two answers): **אם אני פותח את הקובץ שלכם בעוד חודש — למה השורה שמתחילה ב-`#` יכולה לעזור לי?** This covers the official goal "know the **purpose** of documentation", not only writing comments.

---

## 14–22 min — Turning: Left and Right Are the Turtle's

Add turns:

```python
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
```

Students sketch the path **and** draw an arrow for the final direction before running.

Expected: a line to the right, then a line down; the turtle ends facing **left**.

Then the key prediction:

```python
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
```

Ask: **After going down, `left(90)` — which way will the next line go on the screen?**

Many students say "left". Expected: **right**, because the turtle was facing down, and its own left is the screen's right.

Tip: let students turn their own body in their chair, or rotate their notebook, to check.

Angles to name: 90 = a quarter turn, 180 = turn around, 360 = a full turn back to the same direction.

---

## 22–32 min — Guided Build: A Square

Together, build a 100 × 100 square. Before writing code, the class decides:

1. How many sides? (4)
2. How long is each? (100)
3. How much to turn at each corner? (90)
4. After the last side, should we turn again? (Yes, if we want to face the starting direction.)

```python
# A 100 by 100 square
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
```

Count: 8 instructions. This is the **8-instruction limit** used in this unit.

Ask: **Would the square look different with `left(90)` everywhere?** (Same size, drawn upward instead of downward.)

---

## 32–36 min — Common Errors (4 minutes, max)

Students already read `NameError` and `SyntaxError` in Unit 1, so keep this short. One Turtle-specific error:

```python
turtle.Forward(100)
```

Ask: **מה אתם חושבים שקרה?** Then run: `AttributeError: module 'turtle' has no attribute 'Forward'`. Fix: lowercase `forward`.

Flash one more, quickly: `turtle.forward("100")` → a `TypeError`. Don't read its message aloud (`can't multiply sequence by non-int of type 'float'` is confusing at this level). Say only: **"a number was written as text: remove the quotes."**

(Both messages checked in Python 3.14.)

---

## 36–45 min — Transition to Lab + Buffer

Explain the lab: one starter file, the must-do tasks in order (staircase, triangle), the letter if there is time; predict before every run.

Protected buffer for questions, opening files and the Turtle window.

---

# 7. Second 45 Minutes — Lab

Starter file: `TurtleFirstMoves_Starter.py` (setup lines + a 3-instruction path).

**Priority order.** Turtle adds friction (closing the window between runs), and the triangle needs real discussion time, so the lab has one flexible block:

| Must complete | If time |
|---|---|
| 1. Starter prediction · 2. Staircase · 3. Triangle · 5. Save | 4. Letter |

The letter stays in the brief; it is the block to cut when the class is slow.

### Tool Note – Thonny: the Turtle window

- The drawing opens in a separate window. It can open **behind** Thonny: check the taskbar.
- **Close the drawing window before running again.**
- If you close the window while the turtle is still drawing, Thonny may show `Terminator` in the Shell. Just run again.
- Never save a file as `turtle.py` (Unit 0 rule).

---

## 45–50 min — Read → Predict → Run

Students open the starter, sketch the path and final direction, then run.

```python
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
```

Expected: right 100, then up 50; the turtle faces up.

---

## 50–60 min — Task 1: The Staircase

Specification: two stairs going up to the right, each 40 wide and 40 high. Use **exactly 8** movement/turn instructions. The turtle should end facing right.

Students replace the movement lines, predict, run, check.

Reference:

```python
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
```

Insight: stairs alternate **left** and **right**; a square always turns the same way.

---

## 60–72 min — Task 2: The Triangle Puzzle (must do)

Specification: a triangle with three equal sides of 100, closed, the turtle ending in the starting direction.

1. Most students try `left(60)` first. Let them. They get an open shape (half a hexagon).
2. Ask: **כדי שהצב יסיים כשהוא שוב מסתכל ימינה, כמה מעלות הוא צריך להסתובב בסך הכול?** (A full turn: 360.)
3. 360 ÷ 3 corners = **120**.

Reference:

```python
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
```

Check with the square: 360 ÷ 4 = 90. ✔

Target insight:

> **The turtle turns the outside angle. In our square and triangle, to finish facing the same direction again, all the turns together must add up to 360°.**

Keep the rule this narrow. Don't generalize it to "every closed shape"; that is not true for every closed Turtle path.

---

## 72–82 min — Task 3: A Letter (if time — the flexible block)

Only after the triangle works. If the class is behind, skip this and use the time for the triangle and saving.

Draw one capital letter, 100 tall, using at most 8 movement/turn instructions. Choose one: **L, U, C, T**.

Hints (in the lab brief):

- **L:** turn to face down first.
- **C:** start by turning around (`left(180)`), so the top bar goes to the left.
- **T:** draw the top bar, turn around, go back half way, then turn down.

References (all verified):

```python
# L
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(60)
```

```python
# T
turtle.forward(60)
turtle.left(180)
turtle.forward(30)
turtle.left(90)
turtle.forward(100)
```

U and C are in `TurtleFirstMoves_Reference.py`.

---

## 82–85 min — Document and Save

- Add a top comment that says what the file draws, e.g. `# A triangle with equal sides`.
- Save As: `G7_U2_M1_FirstMoves_<Name>.py`

---

## 85–90 min — Exit Check

Show:

```python
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
```

1. Sketch what is drawn. (A line to the right, then a line up: two sides of a square.)
2. Which way is the turtle facing at the end? **up / left / down / right** (Answer: **left**.)

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| `left` means the left side of the screen | It is the turtle's own left. Turn your body to check |
| A turn also moves the turtle | Only `forward` moves; turns happen in place |
| The triangle's turn is 60° | The turtle turns the outside angle: in a triangle with equal sides, 360 ÷ 3 = 120 |
| Back at the start = facing the start direction | Position and direction are separate. Add the last turn |
| Numbers need quotes, like text | Numbers are written without quotes |
| "I'll just use a loop" | Loops come in Unit 5. Today every step is written |

---

# 9. Assessment Evidence (formative)

- Sketches made **before** running (path + direction arrow)
- Staircase with exactly 8 instructions, ending facing right
- Triangle with 120° turns, and an oral explanation of why not 60°
- One correct letter (if time)
- Top comment and correct Save As
- Exit check answer

---

# 10. Differentiation

**Support:** a paper "direction arrow" after each line of code; a strip of paper to rotate like the turtle; start with L before T.

**Extension (no new commands):** draw a letter with a diagonal line, like **Z** (the turns are 135°), or build the staircase so it goes **down**.
