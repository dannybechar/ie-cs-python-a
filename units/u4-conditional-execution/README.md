# Unit 4 — Conditional Execution

Python A, Grade 7 · 6 academic hours = 3 meetings = 270 minutes (90 theory / 180 practice). 3 lessons: the Hebrew lab brief is the lesson page, the Hebrew slide deck is a PDF beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

[Back to the ordered table of contents](../../CONTENTS.md) · [Repository home](../../README.md)

## Start here

| I want to… | Open |
|---|---|
| Read the unit's official scope, topics and hours | [`unit-strategy.md`](unit-strategy.md) |
| Read the background paper | *not yet added* (see below) |
| See the lesson sequence, minutes and status | [`unit-plan.md`](unit-plan.md) |
| Open a lesson (Hebrew lab brief + slide deck) | [Lessons in teaching order](#lessons-in-teaching-order) |
| Get the student starter code and the extra-practice pack | [`exercises/`](exercises) |
| Plan a lesson, see solutions, answer keys, run of show (**teacher-only, do not distribute**) | [`teacher/`](teacher) |
| See external reviews | [`docs/reviews/`](../../docs/reviews/README.md) (no per-unit `feedback/` folder) |

## Background paper: go straight to a statement

The unit's background paper (`background-paper.md`) is **not yet added**; it is to be supplied by the owner and copied in unchanged. Until then the official scope per topic is in [`unit-strategy.md`](unit-strategy.md) and the ministry traceability is in [`docs/ministry-program/`](../../docs/ministry-program/README.md). There are no anchors to link, so the statement table is omitted.

## Lessons in teaching order

| # | Lesson (Hebrew lab brief as `.md`; HTML deck; slide PDF) | Level (theory / practice min) | Review status |
|---|---|---|---|
| 1 | **Unit 4.1 — Conditional Execution** · The Rover's Sensors: Boolean Expressions<br>[md](lessons/L01-the-rovers-sensors.md) · [html](lessons/L01-the-rovers-sensors.html) · [slides PDF](lessons/L01-the-rovers-sensors/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 2 | **Unit 4.2 — Conditional Execution** · The Rover Decides: `if` and `if/else`<br>[md](lessons/L02-the-rover-decides.md) · [html](lessons/L02-the-rover-decides.html) · [slides PDF](lessons/L02-the-rover-decides/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 3 | **Unit 4.3 — Conditional Execution** · The Rover at the Junction — Compound Conditions, Nesting, the Rolling Condition and Turtle<br>[md](lessons/L03-the-rover-at-the-junction.md) · [html](lessons/L03-the-rover-at-the-junction.html) · [slides PDF](lessons/L03-the-rover-at-the-junction/slides-he.pdf) | 0 / 90 | Approved by the teacher |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-the-rovers-sensors-notes.md`](teacher/L01-the-rovers-sensors-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L02-the-rover-decides-notes.md`](teacher/L02-the-rover-decides-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L03-the-rover-at-the-junction-notes.md`](teacher/L03-the-rover-at-the-junction-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/solutions/`](teacher/solutions) | 5 reference solutions (`*_Reference.py` and extras) |

## Status and open checks

- 3 of 3 lessons approved by the teacher (the addendum, where present, is outside the official meetings).
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs, checked in a browser for layout and printing on one sample deck only; not reviewed by the teacher.
- Ministry alignment: see [`docs/ministry-program/`](../../docs/ministry-program/README.md) and [`deck-sheet-backlog.md`](../../docs/ministry-program/deck-sheet-backlog.md) for open deck and sheet items.

## Detailed materials index

6 academic hours = 3 meetings = 270 minutes (90 theory / 180 practice).

## Meetings and materials

| Meeting | Type | File | What it is |
|---|---|---|---|
| **Unit** | Extra practice | [`exercises/Extra_Practice.md`](exercises/Extra_Practice.md) | Take-home pack, 0 class minutes, with ministry source references |
| **Unit** | Strategy | [`unit-strategy.md`](unit-strategy.md) | Official scope, topics, hours and the meeting breakdown |
| **4.1** The Rover's Sensors (boolean expressions, `and` / `or` / `not`) | Lesson | [`teacher/L01-the-rovers-sensors-notes.md`](teacher/L01-the-rovers-sensors-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L01-the-rovers-sensors.md`](lessons/L01-the-rovers-sensors.md) | Hebrew lab brief |
|  | Exercise | [`Booleans_Starter.py`](exercises/Booleans_Starter.py) | Trace warm-up |
|  | Exercise | [`Booleans_Reference.py`](teacher/solutions/Booleans_Reference.py) | Solutions, one function per task (and the `not` demo) |
|  | Lesson | [`lessons/L01-the-rovers-sensors/slides-he.pdf`](lessons/L01-the-rovers-sensors/slides-he.pdf) | Hebrew slide deck (23 slides, NotebookLM, patched) |
| **4.2** The Rover Decides (if and if/else, digits with `//` and `%`, max of two) | Lesson | [`teacher/L02-the-rover-decides-notes.md`](teacher/L02-the-rover-decides-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L02-the-rover-decides.md`](lessons/L02-the-rover-decides.md) | Hebrew lab brief |
|  | Exercise | [`Decisions_Starter.py`](exercises/Decisions_Starter.py) | Delivery trace warm-up |
|  | Exercise | [`ScoreBug_Starter.py`](exercises/ScoreBug_Starter.py) | Program with three kinds of bugs to fix one at a time |
|  | Exercise | [`Decisions_Reference.py`](teacher/solutions/Decisions_Reference.py) | Solutions, one function per task |
|  | Exercise | [`ScoreBug_Reference.py`](teacher/solutions/ScoreBug_Reference.py) | The fixed ScoreBug program (pairs with `ScoreBug_Starter.py`) |
|  | Lesson | [`lessons/L02-the-rover-decides/slides-he.pdf`](lessons/L02-the-rover-decides/slides-he.pdf) | Hebrew slide deck (25 slides, NotebookLM, patched) |
| **4.3** The Rover at the Junction (compound, nested and rolling `elif` conditions, Turtle) | Lesson | [`teacher/L03-the-rover-at-the-junction-notes.md`](teacher/L03-the-rover-at-the-junction-notes.md) | Lesson plan, including the checkpoint |
|  | Exercise | [`lessons/L03-the-rover-at-the-junction.md`](lessons/L03-the-rover-at-the-junction.md) | Hebrew lab brief |
|  | Exercise | [`Shapes_Starter.py`](exercises/Shapes_Starter.py) | Draws both shapes; students add the conditions |
|  | Exercise | [`Shapes_Reference.py`](teacher/solutions/Shapes_Reference.py) | The completed `Shapes_Starter.py` (pairs with it) |
|  | Exercise | [`Conditions_Reference.py`](teacher/solutions/Conditions_Reference.py) | Solutions to all 4.3 tasks, one function per task |
|  | Lesson | [`lessons/L03-the-rover-at-the-junction/slides-he.pdf`](lessons/L03-the-rover-at-the-junction/slides-he.pdf) | Hebrew slide deck (16 slides, NotebookLM, patched) |
