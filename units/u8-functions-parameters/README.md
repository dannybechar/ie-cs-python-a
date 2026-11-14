# Unit 8 — Functions with Parameters

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
| 1 | **Unit 8.1 — Functions with Parameters** · Why Functions? — Define, Call and Split a Program<br>[md](lessons/L01-why-functions.md) · [html](lessons/L01-why-functions.html) · [slides PDF](lessons/L01-why-functions/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 2 | **Unit 8.2 — Functions with Parameters** · Building Blocks — Functions without Parameters, `main()` and Turtle<br>[md](lessons/L02-building-blocks.md) · [html](lessons/L02-building-blocks.html) · [slides PDF](lessons/L02-building-blocks/slides-he.pdf) | 0 / 90 | Approved by the teacher |
| 3 | **Unit 8.3 — Functions with Parameters** · Send a Value — Parameters and Arguments<br>[md](lessons/L03-send-a-value.md) · [html](lessons/L03-send-a-value.html) · [slides PDF](lessons/L03-send-a-value/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 4 | **Unit 8.4 — Functions with Parameters** · Who Knows This Variable? — Scope, `global` and the Unit Checkpoint<br>[md](lessons/L04-who-knows-this-variable.md) · [html](lessons/L04-who-knows-this-variable.html) · [slides PDF](lessons/L04-who-knows-this-variable/slides-he.pdf) | 0 / 90 | Approved by the teacher |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-why-functions-notes.md`](teacher/L01-why-functions-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L02-building-blocks-notes.md`](teacher/L02-building-blocks-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L03-send-a-value-notes.md`](teacher/L03-send-a-value-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L04-who-knows-this-variable-notes.md`](teacher/L04-who-knows-this-variable-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/solutions/`](teacher/solutions) | 4 reference solutions (`*_Reference.py` and extras) |

## Status and open checks

- 4 of 4 lessons approved by the teacher (the addendum, where present, is outside the official meetings).
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs, checked in a browser for layout and printing on one sample deck only; not reviewed by the teacher.
- Ministry alignment: see [`docs/ministry-program/`](../../docs/ministry-program/README.md) and [`deck-sheet-backlog.md`](../../docs/ministry-program/deck-sheet-backlog.md) for open deck and sheet items.

## Detailed materials index

8 academic hours = 4 meetings = 360 minutes (90 theory / 270 practice).

Phase 5 alignment with the ministry program (see [`audit-u8.md`](../../docs/ministry-program/audit-u8.md)): 8.3 now teaches return-lite (20 min, approved deviation from python-a.pdf p.17, checkpoint A stays return-free); 8.2 uses the ministry 4.3 arithmetic-in-a-function tasks; 8.4 uses the 16.1 `score` riddle and a return trace in checkpoint B. The decks and printed sheets still show the pre-Phase-5 content (see the coordinator's deck list); the lab briefs and lesson notes are current.

## Meetings and materials

| Meeting | Type | File | What it is |
|---|---|---|---|
| **Unit** | Strategy | [`unit-strategy.md`](unit-strategy.md) | Official scope, topics, hours and the meeting breakdown |
| **8.1** Why Functions? | Lesson | [`teacher/L01-why-functions-notes.md`](teacher/L01-why-functions-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L01-why-functions.md`](lessons/L01-why-functions.md) | Hebrew lab brief |
|  | Exercise | [`Functions_Starter.py`](exercises/Functions_Starter.py) | Warm-up: a call before the definition |
|  | Exercise | [`Functions_Reference.py`](teacher/solutions/Functions_Reference.py) | Solutions, one function per task |
|  | Lesson | [`lessons/L01-why-functions/slides-he.pdf`](lessons/L01-why-functions/slides-he.pdf) | Hebrew slide deck (20 slides, NotebookLM, patched) |
| **8.2** Building Blocks | Lesson | [`teacher/L02-building-blocks-notes.md`](teacher/L02-building-blocks-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L02-building-blocks.md`](lessons/L02-building-blocks.md) | Hebrew lab brief |
|  | Exercise | [`Modules_Starter.py`](exercises/Modules_Starter.py) | Warm-up: the call indented inside the function |
|  | Exercise | [`Modules_Reference.py`](teacher/solutions/Modules_Reference.py) | Solutions, one function per task |
|  | Lesson | [`lessons/L02-building-blocks/slides-he.pdf`](lessons/L02-building-blocks/slides-he.pdf) | Hebrew slide deck (17 slides, NotebookLM, patched) |
| **8.3** Send a Value | Lesson | [`teacher/L03-send-a-value-notes.md`](teacher/L03-send-a-value-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L03-send-a-value.md`](lessons/L03-send-a-value.md) | Hebrew lab brief |
|  | Exercise | [`Parameters_Starter.py`](exercises/Parameters_Starter.py) | Warm-up: a call with no argument |
|  | Exercise | [`Parameters_Reference.py`](teacher/solutions/Parameters_Reference.py) | Solutions, one function per task |
|  | Lesson | [`lessons/L03-send-a-value/slides-he.pdf`](lessons/L03-send-a-value/slides-he.pdf) | Hebrew slide deck (19 slides, NotebookLM, patched) |
| **8.4** Who Knows This Variable? | Lesson | [`teacher/L04-who-knows-this-variable-notes.md`](teacher/L04-who-knows-this-variable-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L04-who-knows-this-variable.md`](lessons/L04-who-knows-this-variable.md) | Hebrew lab brief |
|  | Exercise | [`Scope_Starter.py`](exercises/Scope_Starter.py) | Warm-up: changing an outside variable without `global` |
|  | Exercise | [`Scope_Reference.py`](teacher/solutions/Scope_Reference.py) | Solutions and checkpoint A, one function per task |
|  | Lesson | [`lessons/L04-who-knows-this-variable/slides-he.pdf`](lessons/L04-who-knows-this-variable/slides-he.pdf) | Hebrew slide deck (18 slides, NotebookLM, patched) |
|  | Exercise | [`Extra_Practice_U8.md`](exercises/Extra_Practice_U8.md) | Take-home extra practice pack for the whole unit (0 class minutes) |
