# Unit 9 — Event-Driven Programming

Python A, Grade 7 · 12 academic hours = 6 meetings = 540 minutes (180 theory / 360 practice). 6 lessons: the Hebrew lab brief is the lesson page, the Hebrew slide deck is a PDF beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

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
| 1 | **Unit 9.1 — Event-Driven Programming** · The Rover Waits for Orders — Event, Listener, Response<br>[md](lessons/L01-the-rover-waits-for-orders.md) · [html](lessons/L01-the-rover-waits-for-orders.html) · [slides PDF](lessons/L01-the-rover-waits-for-orders/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 2 | **Unit 9.2 — Event-Driven Programming** · Click the Rover — `onclick`, x and y, State between Clicks<br>[md](lessons/L02-click-the-rover.md) · [html](lessons/L02-click-the-rover.html) · [slides PDF](lessons/L02-click-the-rover/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 3 | **Unit 9.3 — Event-Driven Programming** · Click the Map — Screen Clicks and Coordinates<br>[md](lessons/L03-click-the-map.md) · [html](lessons/L03-click-the-map.html) · [slides PDF](lessons/L03-click-the-map/slides-he.pdf) | 0 / 90 | Approved by the teacher |
| 4 | **Unit 9.4 — Event-Driven Programming** · Drive with the Arrows — Keyboard Events<br>[md](lessons/L04-drive-with-the-arrows.md) · [html](lessons/L04-drive-with-the-arrows.html) · [slides PDF](lessons/L04-drive-with-the-arrows/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 5 | **Unit 9.5 — Event-Driven Programming** · The Rover Moves by Itself — Animation with a Timer<br>[md](lessons/L05-the-rover-moves-by-itself.md) · [html](lessons/L05-the-rover-moves-by-itself.html) · [slides PDF](lessons/L05-the-rover-moves-by-itself/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 6 | **Unit 9.6 — Event-Driven Programming** · Mission Game — Keys, a Click and a Timer, and the Final Checkpoint<br>[md](lessons/L06-mission-game.md) · [html](lessons/L06-mission-game.html) · [slides PDF](lessons/L06-mission-game/slides-he.pdf) | 0 / 90 | Approved by the teacher |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-the-rover-waits-for-orders-notes.md`](teacher/L01-the-rover-waits-for-orders-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L02-click-the-rover-notes.md`](teacher/L02-click-the-rover-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L03-click-the-map-notes.md`](teacher/L03-click-the-map-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L04-drive-with-the-arrows-notes.md`](teacher/L04-drive-with-the-arrows-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L05-the-rover-moves-by-itself-notes.md`](teacher/L05-the-rover-moves-by-itself-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/L06-mission-game-notes.md`](teacher/L06-mission-game-notes.md) | Lesson notes: minute-by-minute plan |
| [`teacher/solutions/`](teacher/solutions) | 7 reference solutions (`*_Reference.py` and extras) |

## Status and open checks

- 6 of 6 lessons approved by the teacher (the addendum, where present, is outside the official meetings).
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs, checked in a browser for layout and printing on one sample deck only; not reviewed by the teacher.
- Ministry alignment: see [`docs/ministry-program/`](../../docs/ministry-program/README.md) and [`deck-sheet-backlog.md`](../../docs/ministry-program/deck-sheet-backlog.md) for open deck and sheet items.

## Detailed materials index

12 academic hours = 6 meetings = 540 minutes (180 theory / 360 practice).

## Meetings and materials

| Meeting | Type | File | What it is |
|---|---|---|---|
| **Unit** | Strategy | [`unit-strategy.md`](unit-strategy.md) | Official scope, topics, hours and the meeting breakdown |
| **9.1** The Rover Waits for Orders | Lesson | [`teacher/L01-the-rover-waits-for-orders-notes.md`](teacher/L01-the-rover-waits-for-orders-notes.md) | Lesson plan (`done()` = `mainloop()`, ministry wording) |
|  | Exercise | [`lessons/L01-the-rover-waits-for-orders.md`](lessons/L01-the-rover-waits-for-orders.md) | Hebrew lab brief |
|  | Exercise | [`Events_Starter.py`](exercises/Events_Starter.py) | Warm-up: `onclick(say_hello())` |
|  | Exercise | [`Events_Reference.py`](teacher/solutions/Events_Reference.py) | Solutions, one function per task |
|  | Lesson | [`lessons/L01-the-rover-waits-for-orders/slides-he.pdf`](lessons/L01-the-rover-waits-for-orders/slides-he.pdf) | Hebrew slide deck (18 slides, NotebookLM, patched) |
| **9.2** Click the Rover | Lesson | [`teacher/L02-click-the-rover-notes.md`](teacher/L02-click-the-rover-notes.md) | Lesson plan (`%`, `+=` recognition, translation to the exam's object style) |
|  | Exercise | [`lessons/L02-click-the-rover.md`](lessons/L02-click-the-rover.md) | Hebrew lab brief |
|  | Exercise | [`TurtleClick_Starter.py`](exercises/TurtleClick_Starter.py) | Warm-up: a click response without `(x, y)` |
|  | Exercise | [`TurtleClick_Reference.py`](teacher/solutions/TurtleClick_Reference.py) | Solutions, one function per task |
|  | Lesson | [`lessons/L02-click-the-rover/slides-he.pdf`](lessons/L02-click-the-rover/slides-he.pdf) | Hebrew slide deck (18 slides, NotebookLM, patched) |
| **9.3** Click the Map | Lesson | [`teacher/L03-click-the-map-notes.md`](teacher/L03-click-the-map-notes.md) | Lesson plan (four-quarter colours, `btn=`, `wn.onclick` bridge) |
|  | Exercise | [`lessons/L03-click-the-map.md`](lessons/L03-click-the-map.md) | Hebrew lab brief |
|  | Exercise | [`ScreenClick_Starter.py`](exercises/ScreenClick_Starter.py) | Warm-up: `goto` draws a line |
|  | Exercise | [`ScreenClick_Reference.py`](teacher/solutions/ScreenClick_Reference.py) | Solutions, one function per task |
|  | Lesson | [`lessons/L03-click-the-map/slides-he.pdf`](lessons/L03-click-the-map/slides-he.pdf) | Hebrew slide deck (17 slides, NotebookLM, patched) |
| **9.4** Drive with the Arrows | Lesson | [`teacher/L04-drive-with-the-arrows-notes.md`](teacher/L04-drive-with-the-arrows-notes.md) | Lesson plan (`onkeypress`, ministry blanks as exit check) |
|  | Exercise | [`lessons/L04-drive-with-the-arrows.md`](lessons/L04-drive-with-the-arrows.md) | Hebrew lab brief |
|  | Exercise | [`Keys_Starter.py`](exercises/Keys_Starter.py) | Warm-up: `turtle.listen()` missing |
|  | Exercise | [`Keys_Reference.py`](teacher/solutions/Keys_Reference.py) | Solutions, one function per task |
|  | Lesson | [`lessons/L04-drive-with-the-arrows/slides-he.pdf`](lessons/L04-drive-with-the-arrows/slides-he.pdf) | Hebrew slide deck (19 slides, NotebookLM, patched) |
| **9.5** The Rover Moves by Itself | Lesson | [`teacher/L05-the-rover-moves-by-itself-notes.md`](teacher/L05-the-rover-moves-by-itself-notes.md) | Lesson plan |
|  | Exercise | [`lessons/L05-the-rover-moves-by-itself.md`](lessons/L05-the-rover-moves-by-itself.md) | Hebrew lab brief |
|  | Exercise | [`Timer_Starter.py`](exercises/Timer_Starter.py) | Warm-up: `ontimer(animate(), 50)` |
|  | Exercise | [`Timer_Reference.py`](teacher/solutions/Timer_Reference.py) | Solutions, one function per task |
|  | Lesson | [`lessons/L05-the-rover-moves-by-itself/slides-he.pdf`](lessons/L05-the-rover-moves-by-itself/slides-he.pdf) | Hebrew slide deck (18 slides, NotebookLM, patched) |
| **9.6** Mission Game | Lesson | [`teacher/L06-mission-game-notes.md`](teacher/L06-mission-game-notes.md) | Lesson plan (Checkpoint B includes an exam-style question) |
|  | Exercise | [`lessons/L06-mission-game.md`](lessons/L06-mission-game.md) | Hebrew lab brief |
|  | Exercise | [`Game_Starter.py`](exercises/Game_Starter.py) | The game skeleton (Left and Right work) |
|  | Exercise | [`Game_Reference.py`](teacher/solutions/Game_Reference.py) | The full game |
|  | Exercise | [`Checkpoint_B_Reference.py`](teacher/solutions/Checkpoint_B_Reference.py) | Checkpoint B question 3: Adi's squares, answers |
|  | Lesson | [`lessons/L06-mission-game/slides-he.pdf`](lessons/L06-mission-game/slides-he.pdf) | Hebrew slide deck (15 slides, NotebookLM, patched) |

## Take-home pack

| File | What it is |
|---|---|
| [`ExtraPractice_Unit9.md`](exercises/ExtraPractice_Unit9.md) | Extra practice, zero class minutes: exercises with ministry source references, no solutions |
