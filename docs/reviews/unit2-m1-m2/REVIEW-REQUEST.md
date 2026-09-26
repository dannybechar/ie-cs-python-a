# Review request: Grade 7 Python — Unit 2, Meetings 1 and 2

Please review the attached draft lessons as an experienced middle-school computer science teacher and curriculum reviewer.

## Context

- **Course:** Israeli Ministry of Education "Python A" (חשיבה אלגוריתמית באמצעות שפת Python — חלק א), Grade 7 (ages 12–13).
- **Language:** students are Hebrew speakers. Student-facing materials are in Hebrew; code, commands and error messages stay in English.
- **Tool:** Thonny (includes Python 3.14).
- **Lesson format:** one 90-minute double meeting per week. The default is 45 minutes of knowledge delivery + 45 minutes of lab; "Lab + Lab" meetings are all practice.
- **Deadline pressure:** the Ministry exam is in May, and the year is already tight, so each meeting must fit its 90 minutes realistically.

### What students already know (Units 0–1)
Installing and using Thonny; open/run/save; `print("...")`; comments with `#`; reading error messages (NameError, SyntaxError); defining and calling a function with no parameters and no return value; indentation.

### Official Unit 2 requirements (Ministry program, Chapter 2)
- **Hours:** 6 academic hours of 45 minutes (1 theory + 5 practice) = 3 meetings.
- **Topic hours:**
  - the turtle library: 1 theory + 1 practice
  - work surface and pen: 1 practice
  - movement, position and direction: 2 practice
  - changing shape attributes: 1 practice
- **Performance goals:**
  1. import the Turtle library;
  2. know the purpose of documentation and document code;
  3. define the window (Screen) and the turtle (cursor);
  4. call movement functions with a parameter (direction, angle, number of sides);
  5. change attributes: cursor type, pen thickness, pen color;
  6. use shape attributes: hiding, stamping;
  7. write a code segment of up to 8 simple sequential instructions.
- **Concepts:** work surface (Screen), turtle; retrieve/update operations.
- **Official assessment:** practical — creating basic geometric shapes.

### Meeting 3 already exists (not attached) and depends on these two meetings
M3 is Lab + Lab: predict, debug and modify a square/rectangle, an integrated path with stamp and pen up/down, and a rectangle micro-assessment using exactly 8 `forward`/`left`/`right` instructions. It assumes students know: `import turtle`, `turtle.Screen()`, `turtle.shape("turtle")`, `forward`, `left`, `right`, `penup`, `pendown`, `pencolor`, `pensize`, `stamp`, `hideturtle`, `showturtle`, `turtle.done()`. It forbids: `backward`, `goto`, coordinates, heading/position getters, fill, `speed`, variables, `input`, loops, conditions, function parameters, return values, events, classes.

## Files

| File | What it is |
|---|---|
| `m1-lesson-notes.md` | Teacher plan, Meeting 1 "First Moves" (45 knowledge + 45 lab) |
| `m1-lab-brief-he.md` | Student lab brief, Meeting 1 (Hebrew) |
| `TurtleFirstMoves_Starter.py` / `_Reference.py` | Meeting 1 starter and teacher solutions |
| `m2-lesson-notes.md` | Teacher plan, Meeting 2 "Pen, Appearance and Stamps" (Lab + Lab) |
| `m2-lab-brief-he.md` | Student lab brief, Meeting 2 (Hebrew) |
| `TurtlePenStamp_Starter.py` / `_Reference.py` | Meeting 2 starter and teacher solutions |

All code has been run in Python 3.14: every drawing, final position/direction, Shell output and quoted error message in the notes was checked.

## What to review

1. **Timing:** is each minute block realistic for 12–13 year olds in their 3rd–4th programming lesson? Where will it run over, and what should be cut first?
2. **Alignment:** does every official goal and topic above get covered across M1 + M2 (+ M3)? Anything missing, or anything taught that is out of scope?
3. **Continuity:** will a student who finishes M1 and M2 be ready for M3 as described? Any command M3 needs that is not taught?
4. **Pedagogy:** are the hook, the prediction tasks, the triangle puzzle (60° vs 120°) and the update/retrieve task well sequenced and age-appropriate? Are the misconceptions the right ones?
5. **Correctness:** any wrong claim about Turtle behavior, Python errors or geometry?
6. **Hebrew:** in the two lab briefs, is the language natural, clear and age-appropriate for Israeli 7th graders? Point out awkward or incorrect phrasing and suggest wording.
7. **Differentiation:** are the support and extension ideas useful without adding new commands?

## How to answer

Give a numbered list of findings. For each: **file and section**, **severity** (must fix / should fix / nice to have), **the problem**, and **a concrete suggested fix**. Start with the must-fix items. Keep praise short; the goal is to find problems.
