# G7 Unit 2 Meeting 3 Lesson Strategy v2

## Grade 7 / Python A
### Unit 2 — Turtle & Graphics
### Meeting 3 — Geometry Challenge

**Status:** Approved strategy after critical review; ready for asset creation  
**Duration:** 90 minutes  
**Structure:** Lab + Lab  
**Current tool assumption:** Thonny  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 2

Unit 2 has 6 academic hours across 3 double meetings.

Meeting 1 established:

**Move → Turn → Predict → Build**

Meeting 2 extended control of Turtle state:

**movement → pen state → appearance → marker**

Meeting 3 does not add new Turtle API. It integrates the unit through:

**Read → Predict → Debug → Modify → Build → Explain**

The meeting ends with a short practical micro-assessment aligned to the official Unit 2 assessment direction: creating a basic geometric shape using a short sequential program.

---

## 2. Official Scope Used in This Meeting

This meeting consolidates only already-taught Unit 2 content:

- Turtle graphics environment
- visible Turtle / cursor
- movement and direction
- angle and distance
- pen state and simple Turtle attributes already introduced in Meeting 2
- short sequential code
- basic geometric construction
- brief documentation with comments
- practical assessment through a basic geometric shape

No new API is required.

### Sequential-code boundary

The official unit emphasizes short code of up to 8 simple sequential instructions. The protected assessment therefore uses exactly 8 movement/turn instructions to construct a rectangle.

---

## 3. Lesson Goal

By the end of the meeting, students should be able to reason about a short Turtle program before running it, detect a logic error from a mismatch between intended and actual geometry, modify an existing geometric program, and independently build a rectangle from a specification.

Core workflow:

**Read → Predict → Run → Check → Debug → Modify → Build**

Core conceptual relationship:

**instruction sequence → changing position/direction/state → geometry**

---

## 4. Student-Facing Learning Objectives

By the end of the lesson, students should be able to:

1. Predict the visible path of a short Turtle program before running it.
2. Track the Turtle's final facing direction.
3. Distinguish a logic error in geometry from a syntax error.
4. Identify which instruction first causes a path to differ from the intended shape.
5. Modify a square into a rectangle by changing distances while preserving 90° turns.
6. Use previously learned `penup()`, `pendown()`, and `stamp()` in an integrated path.
7. Build a rectangle from a specification using exactly 8 sequential movement/turn instructions.
8. Add one short comment explaining the purpose of the final program.
9. Compare predicted and actual output and debug if they differ.

---

## 5. Technical Baseline

Continue using module-level Turtle calls only.

Already-known calls available in this meeting:

```python
import turtle

turtle.Screen()
turtle.shape("turtle")

turtle.forward(...)
turtle.left(...)
turtle.right(...)
turtle.penup()
turtle.pendown()
turtle.pencolor(...)
turtle.pensize(...)
turtle.stamp()
turtle.hideturtle()
turtle.showturtle()

turtle.done()
```

### Deliberate exclusions

Do not introduce:

- `backward()`
- `goto()`
- coordinates
- heading/position getter calls
- fill operations
- speed control
- variables
- `input()`
- loops
- conditions
- function parameters
- return values
- events
- classes / OOP

Meeting 3 is an integration and assessment meeting, not an API-expansion meeting.

---

## 6. Core Mental Models and Misconceptions

### Geometry depends on state carried from the previous instruction

Each `forward()` begins from the position and direction left by the previous instruction.

### A correct-looking shape can still leave the Turtle facing the wrong direction

Returning to the starting point does not automatically restore the starting direction.

### A logic error can run successfully

A Turtle program may contain valid Python syntax and still draw the wrong geometry.

### Changing distance should not change angle

When converting a square to a rectangle, the 90° turns stay 90°. Only the relevant movement distances change.

### Opposite sides of a rectangle must match

For a 120 × 60 rectangle, the movement pattern is:

**120 → 60 → 120 → 60**

with a 90° turn after each side if the Turtle should finish facing the original direction.

---

# 7. First 45 Minutes — Read, Predict, Debug, Modify

## 0–7 min — Reactivate: Read the Starter

Students open:

[`GeometryChallenge_Starter.py`](GeometryChallenge_Starter.py)

Starter body:

```python
turtle.forward(80)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(60)
```

Do not run yet.

Students sketch:

- the visible path
- the Turtle's final facing direction

Then Run → Check.

Purpose: reactivate movement, direction, distance, and prediction without reteaching.

---

## 7–18 min — Trace the State, Not Just the Lines

Use the same short path.

Ask students to trace instruction by instruction:

1. Where is the Turtle now?
2. Which direction is it facing now?
3. Did this instruction move it, turn it, or both?

Key message:

> The next instruction starts from the state left by the previous one.

Finish with one oral question:

**If we add `turtle.forward(30)` now, in which direction will the new line go?**

---

## 18–30 min — Broken Rectangle: Predict → Find → Fix

### New Build

Students keep the setup lines and `turtle.done()` and replace the current movement body with:

```python
turtle.forward(80)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(80)
turtle.right(90)
```

Teacher tells students:

> This code is supposed to draw a square. One instruction is logically wrong.

Before running:

1. Sketch what the code will actually draw.
2. Circle the instruction where the route first stops matching a square.
3. Write the one-line fix.

Then Run → Check → Fix → Run again.

Correct fix:

```python
turtle.right(90)
```

instead of the third turn being `left(90)`.

### Why this task matters

The program is syntactically valid. The error is visible only by reasoning about the intended geometry and comparing it to the actual result.

---

## 30–40 min — Modify: Square → Rectangle

Students now have a correct 80 × 80 square program.

Specification:

> Change it into a rectangle 120 steps wide and 60 steps high.

Constraint:

> Change only the numbers in `forward(...)`. Do not change the turn instructions.

Before running, students write the four movement distances in order:

**120 → 60 → 120 → 60**

Then Run → Check.

Ask:

**Why did the 90° turns stay the same even though the shape changed?**

Target insight:

> Distance controls side length; angle controls direction change.

---

## 40–45 min — Assessment Briefing + Genuine Buffer

Do not add another concept.

Use this time for:

- troubleshooting
- making sure every student has a working Turtle file
- explaining the second-half workflow
- restoring a clean file state if needed

Reinforce:

**Predict first. Run second. Mismatch means debug, not guess.**

---

# 8. Second 45 Minutes — Integrated Challenge + Practical Micro-Assessment

## 45–55 min — Integrated Path Challenge

### New Build

Students replace the movement body with a path built from this specification:

1. leave a stamp at the start
2. draw forward 70
3. turn right 90°
4. lift the pen
5. move forward 40 without drawing
6. lower the pen
7. turn left 90°
8. draw forward 70

Expected body:

```python
turtle.stamp()
turtle.forward(70)
turtle.right(90)
turtle.penup()
turtle.forward(40)
turtle.pendown()
turtle.left(90)
turtle.forward(70)
```

Before Run, students sketch only what will remain visible:

- starting stamp
- first 70-step line
- invisible 40-step vertical move
- second 70-step line

This integrates Meeting 2 without introducing new syntax.

---

## 55–60 min — Check + Explain

Students run and compare.

Ask 2–3 students orally:

- Where did the Turtle move without leaving evidence as a line?
- Why are the two visible lines parallel?
- Which instruction restored drawing?

This is formative evidence only, not the protected assessment.

---

## 60–64 min — Reset for Assessment

Students keep only:

```python
import turtle

turtle.Screen()
turtle.shape("turtle")

# Write your assessment code here

turtle.done()
```

Save immediately as:

`G7_U2_M3_GeometryAssessment_<Name>.py`

### Tool Note – Thonny: Turtle Window

If a previous graphics window blocks the next run, close it. If the new Turtle window appears behind Thonny, switch windows and bring it forward.

---

## 64–82 min — Practical Micro-Assessment — Protected Time

### Task: Build a Rectangle from Specification

Starting direction: the default Turtle direction, facing right.

Build a rectangle that is:

- width: **120**
- height: **70**
- closed: the Turtle returns to the starting point
- final direction: the Turtle faces the same direction it faced at the start

Rules:

- use exactly **8 movement/turn instructions**
- use only `forward()`, `left()`, and/or `right()` in the 8 assessment instructions
- do not use loops
- do not use variables
- do not use coordinates or `goto()`
- add one short comment above the 8 instructions describing the program

Before first Run:

1. sketch the rectangle
2. write the movement distances in order
3. decide whether you will turn left or right
4. predict the final facing direction

Then Run → Check → Debug if needed.

### Valid reference pattern

One valid solution is:

```python
# Draw a 120 by 70 rectangle
turtle.forward(120)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
```

An equivalent all-left-turn solution is also valid.

### Assessment evidence

Teacher checks:

- prediction exists before first run
- rectangle dimensions follow the 120/70/120/70 pattern
- all turns are 90° and directionally consistent
- the rectangle closes
- the Turtle ends facing the starting direction
- exactly 8 movement/turn instructions are used
- no later-unit constructs are used
- one useful comment is present
- student can explain one correction if debugging was needed

The assessment is practical evidence, not a vocabulary quiz.

---

## 82–86 min — Save + Self-Check

Students verify:

- 4 sides
- opposite sides equal
- 4 right-angle turns
- closed rectangle
- final facing direction restored
- exactly 8 movement/turn instructions
- one comment

Save the assessment file.

---

## 86–90 min — Visual Exit Check / Buffer

Show this code:

```python
turtle.forward(60)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(40)
```

The path returns to the starting point, but there is no fourth turn.

Ask:

1. Is the shape closed?
2. Which direction is the Turtle facing at the end?

Use three visual answer choices for final direction.

Target insight:

> Position and direction are different parts of the Turtle's state.

---

# 9. Misconception Risks

## Misconception 1 — If the shape closes, the Turtle must face the original direction

Correction:

> Position can return to the start while direction is still different.

## Misconception 2 — A program that runs without an error must be correct

Correction:

> Logic errors can produce valid Python that draws the wrong result.

## Misconception 3 — To make a rectangle, the angles must change

Correction:

> A rectangle still uses 90° turns. The side lengths change.

## Misconception 4 — All four rectangle sides use the same distance

Correction:

> Opposite sides match: long, short, long, short.

## Misconception 5 — Debugging means changing lines until the picture looks right

Correction:

> First identify the earliest mismatch between the intended path and the predicted/actual path. Then change the instruction responsible for that mismatch.

---

# 10. Differentiation

## Support

Without changing the assessment target:

- allow a student to draw a small direction arrow after each turn on paper
- allow a four-box trace table: instruction / move or turn / current direction / visible result
- point to the rectangle specification, not to the answer code

Do not reduce the protected assessment to copy-and-run.

## Extension

Only after the assessment is complete:

- build the same rectangle using all left turns instead of all right turns
- change the dimensions while preserving the rectangle structure
- predict how the final direction changes if the last turn is removed

Do not introduce loops as enrichment.

---

# 11. Lesson Assets

1. [`m3-slides-he.pdf`](m3-slides-he.pdf) — Hebrew slides (NotebookLM, 18 slides)
2. [`GeometryChallenge_Starter.py`](GeometryChallenge_Starter.py)
3. [`m3-lab-brief-he.md`](m3-lab-brief-he.md) — Hebrew lab brief
4. [`GeometryAssessment_Reference.py`](GeometryAssessment_Reference.py)
5. [`m3-exit-check-he.png`](m3-exit-check-he.png)

---

# 12. Critical Review Decisions Incorporated in v2

The pre-build review made the following decisions:

1. **No new Turtle API.** Meeting 3 is consolidation and assessment; additional API would dilute the unit close.
2. **The practical assessment is a rectangle, not a decorative route.** This aligns directly with the official practical assessment direction of creating basic geometric shapes.
3. **The assessment uses exactly 8 movement/turn instructions.** This matches the unit's short sequential-code boundary and keeps the task independent but achievable.
4. **The rectangle task requires both closure and restored final direction.** This exposes the important position-vs-direction distinction rather than checking only appearance.
5. **Debugging occurs before the assessment.** Students encounter one deliberately valid-but-wrong program so the assessment does not become their first logic-error experience.
6. **A genuine 5-minute buffer remains before the second half and a 4-minute reset precedes the protected assessment.** These transitions are not filled with optional API content.
7. **The integrated path challenge uses Meeting 2 skills but is formative.** The protected assessment stays narrow enough to measure geometry rather than memory of many Turtle methods.
8. **Prediction remains mandatory before first Run.** Final output alone is insufficient evidence of reasoning.

---

# 13. Unit 2 Closure

After this meeting, Unit 2 is complete.

Students have experienced the progression:

**Move → Turn → Control State → Predict → Debug → Build Geometry**

The next official unit is Unit 3 — Variables, Input/Output & Arithmetic. Do not pre-teach it during Unit 2 closure.
