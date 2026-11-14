# Unit 3 — Variables, Input/Output & Arithmetic

Python A, Grade 7 · 4 academic hours = 2 meetings = 180 minutes (45 theory / 135 practice). 2 lessons: the Hebrew lab brief is the lesson page, the Hebrew slide deck is a PDF beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

[Back to the ordered table of contents](../../CONTENTS.md) · [Repository home](../../README.md)

## Start here

| I want to… | Open |
|---|---|
| Read the unit's official scope, topics and hours | [`unit-strategy.md`](unit-strategy.md) |
| Read the background paper | *not yet added* (see below) |
| See the lesson sequence, minutes and status | [`unit-plan.md`](unit-plan.md) |
| Open a lesson (Hebrew lab brief + slide deck) | [Lessons in teaching order](#lessons-in-teaching-order) |
| Get the student starter code | [`exercises/`](exercises) |
| Plan a lesson, see solutions, answer keys, run of show (**teacher-only, do not distribute**) | [`teacher/`](teacher) |
| See external reviews | [`docs/reviews/`](../../docs/reviews/README.md) (no per-unit `feedback/` folder) |

## Background paper: go straight to a statement

The unit's background paper (`background-paper.md`) is **not yet added**; it is to be supplied by the owner and copied in unchanged. Until then the official scope per topic is in [`unit-strategy.md`](unit-strategy.md) and the ministry traceability is in [`docs/ministry-program/`](../../docs/ministry-program/README.md). There are no anchors to link, so the statement table is omitted.

## Lessons in teaching order

| # | Lesson (Hebrew lab brief as `.md`; HTML deck; slide PDF) | Level (theory / practice min) | Review status |
|---|---|---|---|
| 1 | **Unit 3.1 — Variables, Input/Output & Arithmetic** · The Rover's Memory<br>[md](lessons/L01-the-rovers-memory.md) · [html](lessons/L01-the-rovers-memory.html) · [slides PDF](lessons/L01-the-rovers-memory/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 2 | **Unit 3.2 — Variables, Input/Output & Arithmetic** · From Input to Result<br>[md](lessons/L02-from-input-to-result.md) · [html](lessons/L02-from-input-to-result.html) · [slides PDF](lessons/L02-from-input-to-result/slides-he.pdf) | 0 / 90 | Approved by the teacher |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-the-rovers-memory-notes.md`](teacher/L01-the-rovers-memory-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L02-from-input-to-result-notes.md`](teacher/L02-from-input-to-result-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L02-from-input-to-result-recap-he.md`](teacher/L02-from-input-to-result-recap-he.md) | Hebrew recap script |
| [`teacher/L02-from-input-to-result-run-of-show-he.md`](teacher/L02-from-input-to-result-run-of-show-he.md) | Run of show with slide numbers |
| [`teacher/u3-lab-sheets-key-he.pdf`](teacher/u3-lab-sheets-key-he.pdf) | Answer key |
| [`teacher/solutions/`](teacher/solutions) | 4 reference solutions (`*_Reference.py` and extras) |

## Status and open checks

- 2 of 2 lessons approved by the teacher (the addendum, where present, is outside the official meetings).
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs, checked in a browser for layout and printing on one sample deck only; not reviewed by the teacher.
- Ministry alignment: see [`docs/ministry-program/`](../../docs/ministry-program/README.md) and [`deck-sheet-backlog.md`](../../docs/ministry-program/deck-sheet-backlog.md) for open deck and sheet items.

## Detailed materials index

4 academic hours = 2 meetings = 180 minutes (45 theory / 135 practice).

## Meetings and materials

| Meeting | Type | File | What it is |
|---|---|---|---|
| **Unit** | Strategy | [`unit-strategy.md`](unit-strategy.md) | Official scope, topics, hours and the meeting breakdown |
| **3.1** The Rover's Memory | Lesson | [`teacher/L01-the-rovers-memory-notes.md`](teacher/L01-the-rovers-memory-notes.md) | Lesson plan: variables as boxes, reassignment and trace tables, four types, friendly output, input and conversion |
|  | Exercise | [`lessons/L01-the-rovers-memory.md`](lessons/L01-the-rovers-memory.md) | Hebrew lab brief: rover log, mission card, types detective, turtle square |
|  | Exercise | [`lessons/L01-the-rovers-memory/lab-sheet-he.pdf`](lessons/L01-the-rovers-memory/lab-sheet-he.pdf) | Printable student lab sheet, one sheet both sides, large print, 3 tasks (about 20 minutes: what students can finish): `//` and `%`, swap, packing calculator, plus a star task. Two question types only: run the code, write the output and explain why; write code that does X |
|  | Exercise | [`Variables_Starter.py`](exercises/Variables_Starter.py) | Rover log for the trace-table warm-up. This is the only starter of 3.1: tasks 1-3 are written from scratch |
|  | Exercise | [`Variables_Reference.py`](teacher/solutions/Variables_Reference.py) | Solutions, one function per item: the rover log, the warm-up extras (multiple assignment, conversion) and tasks 1-3 |
|  | Lesson | [`lessons/L01-the-rovers-memory/slides-he.pdf`](lessons/L01-the-rovers-memory/slides-he.pdf) | Hebrew slides (22 slides, made in NotebookLM from 15; 7 question/answer slides added, footers added) |
| **3.2** From Input to Result | Lesson | [`teacher/L02-from-input-to-result-notes.md`](teacher/L02-from-input-to-result-notes.md) | Lesson plan |
|  | Lesson | [`lessons/L02-from-input-to-result/slides-he.pdf`](lessons/L02-from-input-to-result/slides-he.pdf) | Hebrew slides (22 slides, made in NotebookLM; slides 5, 10, 13, 15, 16 corrected, exit answer 22 added). Since the ministry alignment: skip slides 2-3 and 12-13, use the add-on deck |
|  | Lesson | [`lessons/L02-from-input-to-result/addon-slides-he.pdf`](lessons/L02-from-input-to-result/addon-slides-he.pdf) | 8 add-on slides for 15 Nov (the most that fit): 3.1 recap, `**`, swap, self-update (white background, question slide then answer slide) |
|  | Lesson | [`teacher/L02-from-input-to-result-recap-he.md`](teacher/L02-from-input-to-result-recap-he.md), [`teacher/L02-from-input-to-result-run-of-show-he.md`](teacher/L02-from-input-to-result-run-of-show-he.md) | Hebrew recap script (5 min) and the minute-by-minute run of show with slide numbers |
|  | Exercise | [`lessons/L02-from-input-to-result.md`](lessons/L02-from-input-to-result.md) | Hebrew lab brief |
|  | Exercise | [`lessons/L02-from-input-to-result/lab-sheet-he.pdf`](lessons/L02-from-input-to-result/lab-sheet-he.pdf) | Printable student lab sheet, one sheet both sides, 45 minutes (about 35 minutes of tasks plus buffer). Two question types only: run the code, write the output and explain why; write code that does X, plus fast-finisher challenges |
|  | Exercise | [`u3-lab-sheets-key-he.pdf`](teacher/u3-lab-sheets-key-he.pdf) | One-page teacher key for both lab sheets: answers, timing, common mistakes. Built by [`tools/lab-sheet-builder/`](../../tools/lab-sheet-builder/README.md) |
|  | Exercise | [`lessons/L02-from-input-to-result/exit-check-he.png`](lessons/L02-from-input-to-result/exit-check-he.png) | Exit check |
|  | Exercise | [`Arithmetic_Starter.py`](exercises/Arithmetic_Starter.py) | Starter file (four operators) |
|  | Exercise | [`Arithmetic_Reference.py`](teacher/solutions/Arithmetic_Reference.py) | Reference for the Arithmetic lab: the interactive program with `//` and `%`, `**` and precedence, swap with `temp`, `score = score + 1` |
|  | Exercise | [`Packing_Starter.py`](exercises/Packing_Starter.py) | Packing calculator skeleton inside `def packing():` (two inputs, two prints, calculations left as TODO) |
|  | Exercise | [`Packing_Reference.py`](teacher/solutions/Packing_Reference.py) | Packing calculator solution, inside `def packing():` |

### Starter and reference pairs

| Starter (`exercises/`) | Reference (`solutions/`) |
|---|---|
| `Variables_Starter.py` (rover log) | `Variables_Reference.py` (`rover_log()` is the same code; also the extras and tasks 1-3) |
| `Arithmetic_Starter.py` | `Arithmetic_Reference.py` |
| `Packing_Starter.py` | `Packing_Reference.py` |
