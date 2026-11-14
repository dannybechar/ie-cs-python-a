# Unit 7 — Algorithmic Problems

Python A, Grade 7 · 6 academic hours = 3 meetings = 270 minutes (45 theory / 225 practice). 3 lessons: the Hebrew lab brief is the lesson page, the Hebrew slide deck is a PDF beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

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
| 1 | **Unit 7.1 — Algorithmic Problems** · How Many Times? — the Counter Pattern<br>[md](lessons/L01-how-many-times.md) · [html](lessons/L01-how-many-times.html) · [slides PDF](lessons/L01-how-many-times/slides-he.pdf) | 0 / 90 | Approved by the teacher |
| 2 | **Unit 7.2 — Algorithmic Problems** · Sum, Average and Extremes — Accumulator, Minimum and Maximum<br>[md](lessons/L02-sum-average-and-extremes.md) · [html](lessons/L02-sum-average-and-extremes.html) · [slides PDF](lessons/L02-sum-average-and-extremes/slides-he.pdf) | 0 / 90 | Approved by the teacher |
| 3 | **Unit 7.3 — Algorithmic Problems** · Roll the Dice — Random Numbers, Simulations and the Unit Checkpoint<br>[md](lessons/L03-roll-the-dice.md) · [html](lessons/L03-roll-the-dice.html) · [slides PDF](lessons/L03-roll-the-dice/slides-he.pdf) | 45 / 45 | Approved by the teacher |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-how-many-times-notes.md`](teacher/L01-how-many-times-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L02-sum-average-and-extremes-notes.md`](teacher/L02-sum-average-and-extremes-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L03-roll-the-dice-notes.md`](teacher/L03-roll-the-dice-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/solutions/`](teacher/solutions) | 3 reference solutions (`*_Reference.py` and extras) |

## Status and open checks

- 3 of 3 lessons approved by the teacher (the addendum, where present, is outside the official meetings).
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs, checked in a browser for layout and printing on one sample deck only; not reviewed by the teacher.
- Ministry alignment: see [`docs/ministry-program/`](../../docs/ministry-program/README.md) and [`deck-sheet-backlog.md`](../../docs/ministry-program/deck-sheet-backlog.md) for open deck and sheet items.

## Detailed materials index

6 academic hours = 3 meetings = 270 minutes (45 theory / 225 practice).

## Meetings and materials

| Meeting | Type | File | What it is |
|---|---|---|---|
| **Unit** | Strategy | [`unit-strategy.md`](unit-strategy.md) | Official scope, topics, hours and the meeting breakdown |
| **7.1** How Many Times? | Lesson | [`teacher/L01-how-many-times-notes.md`](teacher/L01-how-many-times-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L01-how-many-times.md`](lessons/L01-how-many-times.md) | Hebrew lab brief |
|  | Exercise | [`Counters_Starter.py`](exercises/Counters_Starter.py) | Warm-up: a counter with two bugs |
|  | Exercise | [`Counters_Reference.py`](teacher/solutions/Counters_Reference.py) | Solutions, one function per task: warm-up, coin counter with `elif`, `+=` shorthand, `passed_count` (55), three-counter `survey`, `count_digits` |
|  | Lesson | [`lessons/L01-how-many-times/slides-he.pdf`](lessons/L01-how-many-times/slides-he.pdf) | Hebrew slide deck (17 slides, NotebookLM, patched) |
| **7.2** Sum, Average and Extremes | Lesson | [`teacher/L02-sum-average-and-extremes-notes.md`](teacher/L02-sum-average-and-extremes-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L02-sum-average-and-extremes.md`](lessons/L02-sum-average-and-extremes.md) | Hebrew lab brief |
|  | Exercise | [`Accumulators_Starter.py`](exercises/Accumulators_Starter.py) | Warm-up: `total = 0` inside the loop |
|  | Exercise | [`Accumulators_Reference.py`](teacher/solutions/Accumulators_Reference.py) | Solutions, one function per task: warm-up, guided `expenses`, `donations` (`while`), `+=` shorthand, `min_max`, `temperatures` |
|  | Lesson | [`lessons/L02-sum-average-and-extremes/slides-he.pdf`](lessons/L02-sum-average-and-extremes/slides-he.pdf) | Hebrew slide deck (19 slides, NotebookLM, patched) |
| **7.3** Roll the Dice | Lesson | [`teacher/L03-roll-the-dice-notes.md`](teacher/L03-roll-the-dice-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L03-roll-the-dice.md`](lessons/L03-roll-the-dice.md) | Hebrew lab brief |
|  | Exercise | [`Random_Starter.py`](exercises/Random_Starter.py) | Bonus: `randint` called twice |
|  | Exercise | [`Random_Reference.py`](teacher/solutions/Random_Reference.py) | Solutions and checkpoint A, one function per task: warm-up, double dice, `randint` / `randrange` / `random.random()`, `random_walk`, `dice_stats`, `guess_game` |
|  | Lesson | [`lessons/L03-roll-the-dice/slides-he.pdf`](lessons/L03-roll-the-dice/slides-he.pdf) | Hebrew slide deck (19 slides, NotebookLM, patched) |
| **All** | Extra | [`Extra_Practice_he.md`](exercises/Extra_Practice_he.md) | Take-home pack (18 exercises from the ministry material, no class minutes) |

Phase 5 (ministry alignment): the decks predate some changes. The lesson notes are the current plan; items without a slide are shown live (see the "Deck" paragraph in each note).
