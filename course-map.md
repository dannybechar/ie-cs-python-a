# Grade 7 course map — Python A

Official numbering and hours from [`docs/ministry-source/python-a.pdf`](docs/ministry-source/python-a.pdf) (hours table, pp. 3–5).
Full framing strategy: [`docs/annual-strategy.md`](docs/annual-strategy.md).
Content authority: the ministry Classroom program, indexed in [`docs/ministry-program/`](docs/ministry-program/README.md); this file's hours still come from the PDF above.

## Time budget

1 academic hour = 45 minutes, so the course is 60 hours = **2,700 minutes** = 30 double meetings of 90 minutes.
Minutes are written as **total (theory / practice)**. "Planned" counts only meetings that are built in the repo.

Status: ✅ built and approved by the teacher · 🔶 built, awaiting teacher approval · ⚠️ partly built · ❌ / ⏳ not built yet.

| # | Unit | Official hours (T/P) | Official minutes (T/P) | Meetings | Planned minutes (T/P) | Remaining | Built |
|---|---|---:|---:|---:|---:|---:|---|
| 0 | [Environment Setup](units/u0-environment-setup) — *school addition* | — | — | 1 | 90 (0 / 90) | *+90 outside the budget* | ✅ 1/1 |
| 1 | [Introduction to Python](units/u1-introduction-python) | 2 (1 / 1) | 90 (45 / 45) | 1 | 90 (45 / 45) | 0 | ✅ 1/1 |
| 2 | [Turtle & Graphics](units/u2-turtle-graphics) | 6 (1 / 5) | 270 (45 / 225) | 3 | 270 (45 / 225) | 0 | ✅ 3/3 |
| 3 | [Variables, Input/Output & Arithmetic](units/u3-variables-io-arithmetic) | 4 (1 / 3) | 180 (45 / 135) | 2 | 180 (45 / 135) | 0 | ✅ 2/2 |
| 4 | [Conditional Execution](units/u4-conditional-execution) | 6 (2 / 4) | 270 (90 / 180) | 3 | 270 (90 / 180) | 0 | ✅ 3/3 |
| 5 | [Repetition and Loops](units/u5-loops) | 8 (2 / 6) | 360 (90 / 270) | 4 | 360 (90 / 270) | 0 | ✅ 4/4 |
| 6 | [Strings](units/u6-strings) | 8 (2 / 6) | 360 (90 / 270) | 4 | 360 (90 / 270) | 0 | ✅ 4/4 |
| 7 | [Algorithmic Problems](units/u7-algorithmic-problems) | 6 (1 / 5) | 270 (45 / 225) | 3 | 270 (45 / 225) | 0 | ✅ 3/3 |
| 8 | [Functions with Parameters](units/u8-functions-parameters) | 8 (2 / 6) | 360 (90 / 270) | 4 | 360 (90 / 270) | 0 | ✅ 4/4 |
| 9 | [Event-Driven Programming](units/u9-event-driven-programming) | 12 (4 / 8) | 540 (180 / 360) | 6 | 540 (180 / 360) | 0 | ✅ 6/6 |
|  | **TOTAL (units 1–9)** | **60 (16 / 44)** | **2,700 (720 / 1,980)** | **30** | **2,700 (720 / 1,980)** | **0** | **30/30 meetings built** |

Unit 0 is a school addition outside the official 60 hours: one lab meeting
to install and check the environment before Unit 1 (it covers Chapter 1
goals 1–2, "install" and "run the working environment"). With it, the
year is 31 meetings.

**Theory vs. practice:** every built unit matches its official theory / practice split.

## Deadline and pace

- **Deadline:** the Ministry's Python A exam (בחינת מפמ"ר) is estimated for **May 2027**, with the exact date to be sent during the year
  ([`ministry-circular-tashpaz-he.pdf`](docs/ministry-source/ministry-circular-tashpaz-he.pdf), p.2).
  All 9 units must be taught before it, not by the end of June.
- **Meetings needed:** 31 = 30 official + Unit 0.
- **Meetings available:** one double meeting a week, on **Sundays**, starting **Sunday, Oct 4, 2026** (after the Sukkot break).
  Skipping the Hanukkah Sunday (Dec 6) and the Passover break (Sundays Apr 11, 18 and 25, 2027), there are
  **26 meetings by the end of April** and 31 only by **Sunday, May 30, 2027**.
  Sunday-specific checks, to confirm against the school's official calendar:
  - **Oct 4** is the day after Simchat Torah (Isru Chag). If school is closed, every meeting moves one week later and meeting 31 falls on June 6.
  - **Apr 11** may still be a school day before the Passover break. If so, one meeting is gained.
  - The other holidays before the exam fall on weekdays, not Sundays: election day (Oct 27), Purim (Mar 23),
    Holocaust Remembrance Day (May 4), Memorial/Independence Day (May 11–12) and Lag BaOmer (May 25).
- **Gap:** 31 meetings are needed, so **meetings 27–31 (Unit 9 m2–m6) fall in May**, the exam month. If the exam is early
  in May, up to 5 meetings of Unit 9 would come after it. Decide before winter which meetings to merge, or find extra time.
- **Check after every lesson:** meetings left in the schedule below ≤ meetings left before the exam.

## Open coverage gaps

Official topics that no planned meeting fully covers yet. Details are in each unit's `unit-strategy.md`, under "Official topics and hours".

| Unit | Gap | Fix to plan |
|---|---|---|
| — | None: every official topic is covered by a built meeting (rolling condition `elif` was added to 4.3 on 2026-11-13; the earlier claim that it was not official was wrong, see python-a.pdf p.4) | — |

Ministry alignment (2026-11-13): the ministry Classroom program is the content authority, see [`docs/ministry-program/`](docs/ministry-program/README.md). All units' notes, briefs and code were aligned (`audit-summary.md`, `traceability.md` section 4); official minutes per unit and 90 minutes per meeting are unchanged. **Debt:** the slide decks and printed lab sheets still show the pre-alignment content: [`deck-sheet-backlog.md`](docs/ministry-program/deck-sheet-backlog.md). Units 0-2 changes live in addendum files because those classes are already taught (Unit 2 addendum = 45 min outside the official minutes).

## Schedule

All 31 meetings in teaching order. Fill in **Target week** once the school calendar is known, and **Taught on** after each lesson. What each class has actually completed is tracked in [`class-progress.md`](class-progress.md).

| # | Meeting | Content | Built | Target week (starts Sunday) | Taught on |
|---:|---|---|---|---|---|
| 1 | 0.1 Environment Setup | Install, check, save | ✅ | Oct 4, 2026 | |
| 2 | 1.1 Introduction to Python | First program: print, comments, first function | ✅ | Oct 11, 2026 | |
| 3 | 2.1 Turtle & Graphics | Turtle library, work surface, movement | ✅ | Oct 18, 2026 | |
| 4 | 2.2 Turtle & Graphics | Pen and shape attributes | ✅ | Oct 25, 2026 | |
| 5 | 2.3 Turtle & Graphics | Geometry challenge | ✅ | Nov 1, 2026 | |
| 6 | 3.1 Variables, Input/Output & Arithmetic | Variables, types, input, friendly output | ✅ | Nov 8, 2026 | Nov 8, 2026 |
| 7 | 3.2 Variables, Input/Output & Arithmetic | Input → calculation → output | ✅ | Nov 15, 2026 | |
| 8 | 4.1 Conditional Execution | Boolean expressions, truth tables, and/or | ✅ | Nov 22, 2026 | |
| 9 | 4.2 Conditional Execution | if and if/else, input filter | ✅ | Nov 29, 2026 | |
| 10 | 4.3 Conditional Execution | Compound conditions, nesting, Turtle, checkpoint | ✅ | Dec 13, 2026 | |
| 11 | 5.1 Repetition and Loops | Why loops; for and range, loop variable, running total | ✅ | Dec 20, 2026 | |
| 12 | 5.2 Repetition and Loops | range with a step; Turtle polygons, spiral, star | ✅ | Dec 27, 2026 | |
| 13 | 5.3 Repetition and Loops | while, update, sentinel, for vs while | ✅ | Jan 3, 2027 | |
| 14 | 5.4 Repetition and Loops | Nested loops, rolling execution, checkpoint | ✅ | Jan 10, 2027 | |
| 15 | 6.1 Strings | str, empty string, len, indexes | ✅ | Jan 17, 2027 | |
| 16 | 6.2 Strings | + and *, strings vs numbers, in, loop over characters | ✅ | Jan 24, 2027 | |
| 17 | 6.3 Strings | Slicing: start, end, step, reverse | ✅ | Jan 31, 2027 | |
| 18 | 6.4 Strings | String operations, Turtle write, unit checkpoint | ✅ | Feb 7, 2027 | |
| 19 | 7.1 Algorithmic Problems | Counter pattern, two counters | ✅ | Feb 14, 2027 | |
| 20 | 7.2 Algorithmic Problems | Accumulator, average, minimum and maximum | ✅ | Feb 21, 2027 | |
| 21 | 7.3 Algorithmic Problems | Random numbers, simulation, Turtle random walk, checkpoint | ✅ | Feb 28, 2027 | |
| 22 | 8.1 Functions with Parameters | Why functions; definition vs call; main() | ✅ | Mar 7, 2027 | |
| 23 | 8.2 Functions with Parameters | Functions without parameters; input inside; Turtle house | ✅ | Mar 14, 2027 | |
| 24 | 8.3 Functions with Parameters | Parameters and arguments; Turtle sizes | ✅ | Mar 21, 2027 | |
| 25 | 8.4 Functions with Parameters | Scope, global, Turtle spiral, checkpoint | ✅ | Mar 28, 2027 | |
| 26 | 9.1 Event-Driven Programming | Why event-driven; event, listener, response; first click | ✅ | Apr 4, 2027 | |
| 27 | 9.2 Event-Driven Programming | Clicking the rover: onclick, (x, y), state | ✅ | May 2, 2027 ⚠️ May | |
| 28 | 9.3 Event-Driven Programming | Clicking the screen: onscreenclick, goto, stamps | ✅ | May 9, 2027 ⚠️ May | |
| 29 | 9.4 Event-Driven Programming | Keyboard: listen, onkey, borders | ✅ | May 16, 2027 ⚠️ May | |
| 30 | 9.5 Event-Driven Programming | Animation with a timer: ontimer, bounce, stop/start | ✅ | May 23, 2027 ⚠️ May | |
| 31 | 9.6 Event-Driven Programming | Final game project and checkpoint | ✅ | May 30, 2027 ⚠️ May | |

## Meeting log

One row per built meeting. Minutes come from the **Duration** and **Structure** lines of its lesson notes.

| Unit | Meeting | Minutes | Theory / Practice | Structure | Source | Notes |
|---|---|---:|---:|---|---|---|
| 0 | 0.1 Environment Setup | 90 | 0 / 90 | Lab + Lab | [`L01-install-check-save-notes.md`](units/u0-environment-setup/teacher/L01-install-check-save-notes.md) | Outside the 60 h budget |
| 1 | 1.1 Introduction to Python | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-my-first-program-notes.md`](units/u1-introduction-python/teacher/L01-my-first-program-notes.md) | Slides: NotebookLM deck `m1-slides-he.pdf` (20 slides, 85 min + 5 buffer); notes, brief and code rewritten to match |
| 2 | 2.1 Turtle & Graphics | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-first-moves-notes.md`](units/u2-turtle-graphics/teacher/L01-first-moves-notes.md) | Reviewed by ChatGPT (round 1 fixes applied); slides: `m1-slides-he.pdf` (23 slides, 90 min) |
| 2 | 2.2 Turtle & Graphics | 90 | 0 / 90 | Lab + Lab | [`L02-pen-appearance-and-stamps-notes.md`](units/u2-turtle-graphics/teacher/L02-pen-appearance-and-stamps-notes.md) | Reviewed by ChatGPT (round 1 fixes applied); slides: `m2-slides-he.pdf` (15 slides, 90 min) |
| 2 | 2.3 Turtle & Graphics | 90 | 0 / 90 | Lab + Lab | [`L03-geometry-challenge-notes.md`](units/u2-turtle-graphics/teacher/L03-geometry-challenge-notes.md) | Slides: `m3-slides-he.pdf` (18 slides, 90 min); lab brief converted to Markdown |
| 3 | 3.1 Variables, Input/Output & Arithmetic | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-the-rovers-memory-notes.md`](units/u3-variables-io-arithmetic/teacher/L01-the-rovers-memory-notes.md) | New; closes the Turtle-variables and compound-output gaps; slides: `m1-slides-he.pdf` (22 slides) |
| 3 | 3.2 Variables, Input/Output & Arithmetic | 90 | 0 / 90 | Lab + Lab | [`L02-from-input-to-result-notes.md`](units/u3-variables-io-arithmetic/teacher/L02-from-input-to-result-notes.md) | Slides: `m2-slides-he.pdf` (22 slides, 90 min; skip 2-3 and 12-13) + `m2-addon-slides-he.pdf` (8 slides); 5-min recap of 3.1; lab sheet 3 tasks (~20 min); run of show in `m2-run-of-show-he.md` |
| 4 | 4.1 Conditional Execution | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-the-rovers-sensors-notes.md`](units/u4-conditional-execution/teacher/L01-the-rovers-sensors-notes.md) | Inspired by the teacher's raw deck; slides: `m1-slides-he.pdf` (23 slides, 90 min; NotebookLM, patched) |
| 4 | 4.2 Conditional Execution | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L02-the-rover-decides-notes.md`](units/u4-conditional-execution/teacher/L02-the-rover-decides-notes.md) | Inspired by the teacher's raw deck; slides: `m2-slides-he.pdf` (25 slides, 90 min; NotebookLM, patched) |
| 4 | 4.3 Conditional Execution | 90 | 0 / 90 | Lab + Lab | [`L03-the-rover-at-the-junction-notes.md`](units/u4-conditional-execution/teacher/L03-the-rover-at-the-junction-notes.md) | Unit checkpoint (practical + tracing); slides: `m3-slides-he.pdf` (16 slides, 90 min; NotebookLM, patched) |
| 5 | 5.1 Repetition and Loops | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-the-rover-repeats-notes.md`](units/u5-loops/teacher/L01-the-rover-repeats-notes.md) | From the teacher's raw deck; slides: `m1-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 5 | 5.2 Repetition and Loops | 90 | 0 / 90 | Lab + Lab | [`L02-the-rover-draws-in-steps-notes.md`](units/u5-loops/teacher/L02-the-rover-draws-in-steps-notes.md) | From the teacher's raw deck; slides: `m2-slides-he.pdf` (17 slides, 90 min; NotebookLM, patched) |
| 5 | 5.3 Repetition and Loops | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L03-until-the-job-is-done-notes.md`](units/u5-loops/teacher/L03-until-the-job-is-done-notes.md) | From the teacher's raw deck; slides: `m3-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 5 | 5.4 Repetition and Loops | 90 | 0 / 90 | Lab + Lab | [`L04-loops-inside-loops-notes.md`](units/u5-loops/teacher/L04-loops-inside-loops-notes.md) | Unit checkpoint (practical + theory); slides: `m4-slides-he.pdf` (18 slides, 90 min; NotebookLM, patched) |
| 6 | 6.1 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-the-rovers-message-notes.md`](units/u6-strings/teacher/L01-the-rovers-message-notes.md) | From the teacher's raw deck; slides: `m1-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 6 | 6.2 Strings | 90 | 0 / 90 | Lab + Lab | [`L02-building-messages-notes.md`](units/u6-strings/teacher/L02-building-messages-notes.md) | From the teacher's raw deck; slides: `m2-slides-he.pdf` (18 slides, 90 min; NotebookLM, patched) |
| 6 | 6.3 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L03-cutting-the-message-notes.md`](units/u6-strings/teacher/L03-cutting-the-message-notes.md) | From the teacher's raw deck; slides: `m3-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 6 | 6.4 Strings | 90 | 0 / 90 | Lab + Lab | [`L04-text-tools-notes.md`](units/u6-strings/teacher/L04-text-tools-notes.md) | Unit checkpoint (practical + theory), Turtle `write`; slides: `m4-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 7 | 7.1 Algorithmic Problems | 90 | 0 / 90 | Lab + Lab | [`L01-how-many-times-notes.md`](units/u7-algorithmic-problems/teacher/L01-how-many-times-notes.md) | From the teacher's raw deck (lists replaced); slides: `m1-slides-he.pdf` (17 slides, 90 min; NotebookLM, patched) |
| 7 | 7.2 Algorithmic Problems | 90 | 0 / 90 | Lab + Lab | [`L02-sum-average-and-extremes-notes.md`](units/u7-algorithmic-problems/teacher/L02-sum-average-and-extremes-notes.md) | From the teacher's raw deck (lists replaced); slides: `m2-slides-he.pdf` (19 slides, 90 min; NotebookLM, patched) |
| 7 | 7.3 Algorithmic Problems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L03-roll-the-dice-notes.md`](units/u7-algorithmic-problems/teacher/L03-roll-the-dice-notes.md) | Unit checkpoint; Turtle random walk; slides: `m3-slides-he.pdf` (19 slides, 90 min; NotebookLM, patched) |
| 8 | 8.1 Functions with Parameters | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-why-functions-notes.md`](units/u8-functions-parameters/teacher/L01-why-functions-notes.md) | From the teacher's raw deck; slides: `m1-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 8 | 8.2 Functions with Parameters | 90 | 0 / 90 | Lab + Lab | [`L02-building-blocks-notes.md`](units/u8-functions-parameters/teacher/L02-building-blocks-notes.md) | From the teacher's raw deck; slides: `m2-slides-he.pdf` (17 slides, 90 min; NotebookLM, patched) |
| 8 | 8.3 Functions with Parameters | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L03-send-a-value-notes.md`](units/u8-functions-parameters/teacher/L03-send-a-value-notes.md) | From the teacher's raw deck; slides: `m3-slides-he.pdf` (19 slides, 90 min; NotebookLM, patched) |
| 8 | 8.4 Functions with Parameters | 90 | 0 / 90 | Lab + Lab | [`L04-who-knows-this-variable-notes.md`](units/u8-functions-parameters/teacher/L04-who-knows-this-variable-notes.md) | Unit checkpoint; slides: `m4-slides-he.pdf` (18 slides, 90 min; NotebookLM, patched) |
| 9 | 9.1 Event-Driven Programming | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-the-rover-waits-for-orders-notes.md`](units/u9-event-driven-programming/teacher/L01-the-rover-waits-for-orders-notes.md) | From the teacher's raw deck; slides: `m1-slides-he.pdf` (18 slides, 90 min; NotebookLM, patched) |
| 9 | 9.2 Event-Driven Programming | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L02-click-the-rover-notes.md`](units/u9-event-driven-programming/teacher/L02-click-the-rover-notes.md) | From the teacher's raw deck; slides: `m2-slides-he.pdf` (18 slides, 90 min; NotebookLM, patched) |
| 9 | 9.3 Event-Driven Programming | 90 | 0 / 90 | Lab + Lab | [`L03-click-the-map-notes.md`](units/u9-event-driven-programming/teacher/L03-click-the-map-notes.md) | From the teacher's raw deck; slides: `m3-slides-he.pdf` (17 slides, 90 min; NotebookLM, patched) |
| 9 | 9.4 Event-Driven Programming | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L04-drive-with-the-arrows-notes.md`](units/u9-event-driven-programming/teacher/L04-drive-with-the-arrows-notes.md) | From the teacher's raw deck; slides: `m4-slides-he.pdf` (19 slides, 90 min; NotebookLM, patched) |
| 9 | 9.5 Event-Driven Programming | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L05-the-rover-moves-by-itself-notes.md`](units/u9-event-driven-programming/teacher/L05-the-rover-moves-by-itself-notes.md) | From the teacher's raw deck; slides: `m5-slides-he.pdf` (18 slides, 90 min; NotebookLM, patched) |
| 9 | 9.6 Event-Driven Programming | 90 | 0 / 90 | Lab + Lab | [`L06-mission-game-notes.md`](units/u9-event-driven-programming/teacher/L06-mission-game-notes.md) | Final checkpoint (the game); slides: `m6-slides-he.pdf` (15 slides, 90 min; NotebookLM, patched) |

## Unit tests

Unit tests are assessment time on top of the lesson minutes and are not counted in the time budget above. Each takes one 45-minute lesson slot, so schedule it deliberately (see **Deadline and pace**).

| Unit | Test | Forms | Files |
|---|---|---|---|
| 2 | Turtle & Graphics, 45 min, 25 multiple-choice questions | A and B | [`units/u2-turtle-graphics`](units/u2-turtle-graphics/README.md#unit-2-test) |
| 2 | Turtle basics (5 commands), 60 min, written: 2 MC + 2 analysis + 2 code | A | [`units/u2-turtle-graphics`](units/u2-turtle-graphics/README.md#unit-2-written-test) |

## Keeping this up to date

When a meeting is added or its timing changes:
1. Add or update its row in the **Meeting log**, and mark it 🔶 in the **Schedule** (✅ only after the teacher approves it).
2. Update that unit's **Planned minutes**, **Remaining** and **Built** in the time budget, and the totals.
3. A unit's planned minutes must not exceed its official minutes. If they would, cut the lesson or
   note the overrun in the unit row with the reason.
4. Update the status of the topics it covers in the unit's `unit-strategy.md` ("Official topics and hours"),
   and remove any gap it closes from **Open coverage gaps**.
5. Layout: the student lesson page is `units/<unit>/lessons/L<NN>-<slug>.md` (Hebrew lab brief) with its generated `.html` deck
   (`python tools/lesson-decks/build_decks.py`); the teacher plan is `teacher/L<NN>-<slug>-notes.md`; the NotebookLM PDF is
   `lessons/L<NN>-<slug>/slides-he.pdf`. Inserting a lesson means renumbering with `git mv`.
6. Update the unit's entry page `README.md`, its `unit-plan.md` and the root `CONTENTS.md`, then run the checks in `units/README.md`.

After each lesson is taught:
1. Fill in **Taught on** in the **Schedule**.
2. Recheck **Deadline and pace**: meetings left in the schedule must not exceed meetings left before the exam.

Each unit folder's `unit-strategy.md` has the full official scope,
per-meeting breakdown, exit criteria, depth boundary and enrichment notes
for that unit.
