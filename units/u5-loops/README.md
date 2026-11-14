# Unit 5 — Repetition and Loops

Python A, Grade 7 · 8 academic hours = 4 meetings = 360 minutes (90 theory / 270 practice). 4 lessons: the Hebrew lab brief is the lesson page, the Hebrew slide deck is a PDF beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

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
| 1 | **Unit 5.1 — Repetition and Loops** · The Rover Repeats — Why Loops, `for` and `range`<br>[md](lessons/L01-the-rover-repeats.md) · [html](lessons/L01-the-rover-repeats.html) · [slides PDF](lessons/L01-the-rover-repeats/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 2 | **Unit 5.2 — Repetition and Loops** · The Rover Draws in Steps — `range(start, stop, step)` and Turtle<br>[md](lessons/L02-the-rover-draws-in-steps.md) · [html](lessons/L02-the-rover-draws-in-steps.html) · [slides PDF](lessons/L02-the-rover-draws-in-steps/slides-he.pdf) | 0 / 90 | Approved by the teacher |
| 3 | **Unit 5.3 — Repetition and Loops** · Until the Job Is Done — the `while` Loop<br>[md](lessons/L03-until-the-job-is-done.md) · [html](lessons/L03-until-the-job-is-done.html) · [slides PDF](lessons/L03-until-the-job-is-done/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 4 | **Unit 5.4 — Repetition and Loops** · Loops Inside Loops — Nesting, Rolling Execution and the Unit Checkpoint<br>[md](lessons/L04-loops-inside-loops.md) · [html](lessons/L04-loops-inside-loops.html) · [slides PDF](lessons/L04-loops-inside-loops/slides-he.pdf) | 0 / 90 | Approved by the teacher |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-the-rover-repeats-notes.md`](teacher/L01-the-rover-repeats-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L02-the-rover-draws-in-steps-notes.md`](teacher/L02-the-rover-draws-in-steps-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L03-until-the-job-is-done-notes.md`](teacher/L03-until-the-job-is-done-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L04-loops-inside-loops-notes.md`](teacher/L04-loops-inside-loops-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/solutions/`](teacher/solutions) | 4 reference solutions (`*_Reference.py` and extras) |

## Status and open checks

- 4 of 4 lessons approved by the teacher (the addendum, where present, is outside the official meetings).
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs, checked in a browser for layout and printing on one sample deck only; not reviewed by the teacher.
- Ministry alignment: see [`docs/ministry-program/`](../../docs/ministry-program/README.md) and [`deck-sheet-backlog.md`](../../docs/ministry-program/deck-sheet-backlog.md) for open deck and sheet items.

## Detailed materials index

8 academic hours = 4 meetings = 360 minutes (90 theory / 270 practice).

## Meetings and materials

| Meeting | Type | File | What it is |
|---|---|---|---|
| **Unit** | Strategy | [`unit-strategy.md`](unit-strategy.md) | Official scope, topics, hours and the meeting breakdown |
| **5.1** The Rover Repeats | Lesson | [`teacher/L01-the-rover-repeats-notes.md`](teacher/L01-the-rover-repeats-notes.md) | Lesson plan (includes `+=` as recognition) |
|  | Exercise | [`lessons/L01-the-rover-repeats.md`](lessons/L01-the-rover-repeats.md) | Hebrew lab brief |
|  | Exercise | [`Loops_Starter.py`](exercises/Loops_Starter.py) | Warm-up: `print` outside the loop |
|  | Exercise | [`Loops_Reference.py`](teacher/solutions/Loops_Reference.py) | Solutions, one function per task, plus the `+=` form |
|  | Lesson | [`lessons/L01-the-rover-repeats/slides-he.pdf`](lessons/L01-the-rover-repeats/slides-he.pdf) | Hebrew slide deck (20 slides, NotebookLM, patched) |
| **5.2** The Rover Draws in Steps | Lesson | [`teacher/L02-the-rover-draws-in-steps-notes.md`](teacher/L02-the-rover-draws-in-steps-notes.md) | Lesson plan (includes the `end` block and `for` + `if %`) |
|  | Exercise | [`lessons/L02-the-rover-draws-in-steps.md`](lessons/L02-the-rover-draws-in-steps.md) | Hebrew lab brief |
|  | Exercise | [`Ranges_Starter.py`](exercises/Ranges_Starter.py) | Task 1: a `range` boundary bug |
|  | Exercise | [`Ranges_Reference.py`](teacher/solutions/Ranges_Reference.py) | Solutions, one function per task, plus `end`, multiples, 7-boom, one-line countdown |
|  | Lesson | [`lessons/L02-the-rover-draws-in-steps/slides-he.pdf`](lessons/L02-the-rover-draws-in-steps/slides-he.pdf) | Hebrew slide deck (17 slides, NotebookLM, patched) |
| **5.3** Until the Job Is Done | Lesson | [`teacher/L03-until-the-job-is-done-notes.md`](teacher/L03-until-the-job-is-done-notes.md) | Lesson plan (includes the finite/endless drill and `digit_sum()`) |
|  | Exercise | [`lessons/L03-until-the-job-is-done.md`](lessons/L03-until-the-job-is-done.md) | Hebrew lab brief |
|  | Exercise | [`While_Starter.py`](exercises/While_Starter.py) | Warm-up: a loop with no update |
|  | Exercise | [`While_Reference.py`](teacher/solutions/While_Reference.py) | Solutions, one function per task, plus `digit_sum()` |
|  | Lesson | [`lessons/L03-until-the-job-is-done/slides-he.pdf`](lessons/L03-until-the-job-is-done/slides-he.pdf) | Hebrew slide deck (20 slides, NotebookLM, patched) |
| **5.4** Loops Inside Loops | Lesson | [`teacher/L04-loops-inside-loops-notes.md`](teacher/L04-loops-inside-loops-notes.md) | Lesson plan, including the checkpoint and the exam-prep homework list |
|  | Exercise | [`lessons/L04-loops-inside-loops.md`](lessons/L04-loops-inside-loops.md) | Hebrew lab brief |
|  | Exercise | [`Nested_Starter.py`](exercises/Nested_Starter.py) | Task 1: `print()` in the wrong loop |
|  | Exercise | [`Nested_Reference.py`](teacher/solutions/Nested_Reference.py) | Solutions, one function per task, plus `super_python()`; the flower is optional |
|  | Lesson | [`lessons/L04-loops-inside-loops/slides-he.pdf`](lessons/L04-loops-inside-loops/slides-he.pdf) | Hebrew slide deck (18 slides, NotebookLM, patched) |
| **Unit** | Exercise | [`Extra_Practice_Unit5.md`](exercises/Extra_Practice_Unit5.md) | Take-home extra practice pack (zero class minutes): ministry-based exercises with source references, no solutions |
