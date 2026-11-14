# Unit 6 — Strings

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
| 1 | **Unit 6.1 — Strings** · The Rover's Message — Strings, `len` and Indexes<br>[md](lessons/L01-the-rovers-message.md) · [html](lessons/L01-the-rovers-message.html) · [slides PDF](lessons/L01-the-rovers-message/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 2 | **Unit 6.2 — Strings** · Building Messages — `+`, `*`, `in` and a Loop over Characters<br>[md](lessons/L02-building-messages.md) · [html](lessons/L02-building-messages.html) · [slides PDF](lessons/L02-building-messages/slides-he.pdf) | 0 / 90 | Approved by the teacher |
| 3 | **Unit 6.3 — Strings** · Cutting the Message — Slicing<br>[md](lessons/L03-cutting-the-message.md) · [html](lessons/L03-cutting-the-message.html) · [slides PDF](lessons/L03-cutting-the-message/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 4 | **Unit 6.4 — Strings** · Text Tools — String Operations, Turtle `write` and the Unit Checkpoint<br>[md](lessons/L04-text-tools.md) · [html](lessons/L04-text-tools.html) · [slides PDF](lessons/L04-text-tools/slides-he.pdf) | 0 / 90 | Approved by the teacher |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-the-rovers-message-notes.md`](teacher/L01-the-rovers-message-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L02-building-messages-notes.md`](teacher/L02-building-messages-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L03-cutting-the-message-notes.md`](teacher/L03-cutting-the-message-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L04-text-tools-notes.md`](teacher/L04-text-tools-notes.md) | Lesson notes: minute-by-minute plan |
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
| **6.1** The Rover's Message | Lesson | [`teacher/L01-the-rovers-message-notes.md`](teacher/L01-the-rovers-message-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L01-the-rovers-message.md`](lessons/L01-the-rovers-message.md) | Hebrew lab brief |
|  | Exercise | [`Strings_Starter.py`](exercises/Strings_Starter.py) | Warm-up: `word[len(word)]` crashes |
|  | Exercise | [`Strings_Reference.py`](teacher/solutions/Strings_Reference.py) | Solutions, one function per task (negative indexes) |
|  | Lesson | [`lessons/L01-the-rovers-message/slides-he.pdf`](lessons/L01-the-rovers-message/slides-he.pdf) | Hebrew slide deck (20 slides, NotebookLM, patched) |
| **6.2** Building Messages | Lesson | [`teacher/L02-building-messages-notes.md`](teacher/L02-building-messages-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L02-building-messages.md`](lessons/L02-building-messages.md) | Hebrew lab brief |
|  | Exercise | [`Operators_Starter.py`](exercises/Operators_Starter.py) | Warm-up: `"2" + "3"` prints 23 |
|  | Exercise | [`Operators_Reference.py`](teacher/solutions/Operators_Reference.py) | Solutions, one function per task (build-a-string, `check_mail()`) |
|  | Lesson | [`lessons/L02-building-messages/slides-he.pdf`](lessons/L02-building-messages/slides-he.pdf) | Hebrew slide deck (18 slides, NotebookLM, patched) |
| **6.3** Cutting the Message | Lesson | [`teacher/L03-cutting-the-message-notes.md`](teacher/L03-cutting-the-message-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L03-cutting-the-message.md`](lessons/L03-cutting-the-message.md) | Hebrew lab brief |
|  | Exercise | [`Slicing_Starter.py`](exercises/Slicing_Starter.py) | Task 1: `word[1:4]` misses index 4 |
|  | Exercise | [`Slicing_Reference.py`](teacher/solutions/Slicing_Reference.py) | Solutions, one function per task (negative bounds) |
|  | Lesson | [`lessons/L03-cutting-the-message/slides-he.pdf`](lessons/L03-cutting-the-message/slides-he.pdf) | Hebrew slide deck (20 slides, NotebookLM, patched) |
| **6.4** Text Tools | Lesson | [`teacher/L04-text-tools-notes.md`](teacher/L04-text-tools-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L04-text-tools.md`](lessons/L04-text-tools.md) | Hebrew lab brief |
|  | Exercise | [`Methods_Starter.py`](exercises/Methods_Starter.py) | Warm-up: `Yes` is rejected (capitals) |
|  | Exercise | [`Methods_Reference.py`](teacher/solutions/Methods_Reference.py) | Solutions and checkpoint A, one function per task (`index`, exam-dialect Turtle) |
|  | Lesson | [`lessons/L04-text-tools/slides-he.pdf`](lessons/L04-text-tools/slides-he.pdf) | Hebrew slide deck (20 slides, NotebookLM, patched) |
|  | Extra practice | [`Strings_Extra_Practice.md`](exercises/Strings_Extra_Practice.md) | Take-home pack: ministry exam-prep strings homework (meeting 19.4) and worksheet 15.2 items, zero class minutes |
