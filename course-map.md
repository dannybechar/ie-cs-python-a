# Grade 7 course map — Python A

Official numbering and hours from [`docs/ministry-source/python-a.pdf`](docs/ministry-source/python-a.pdf) (hours table, pp. 3–5).
Full framing strategy: [`docs/annual-strategy.md`](docs/annual-strategy.md).

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
| 4 | [Conditional Execution](units/u4-conditional-execution) | 6 (2 / 4) | 270 (90 / 180) | 3 | 270 (90 / 180) | 0 | 🔶 3/3 (awaiting approval) |
| 5 | [Repetition / Loops](units/u5-loops) | 8 (2 / 6) | 360 (90 / 270) | 4 | 0 | 360 | ❌ 0/4 |
| 6 | [Strings](units/u6-strings) | 8 (2 / 6) | 360 (90 / 270) | 4 | 0 | 360 | ❌ 0/4 |
| 7 | [Algorithmic Problems](units/u7-algorithmic-problems) | 6 (1 / 5) | 270 (45 / 225) | 3 | 0 | 270 | ❌ 0/3 |
| 8 | [Functions with Parameters](units/u8-functions-parameters) | 8 (2 / 6) | 360 (90 / 270) | 4 | 0 | 360 | ❌ 0/4 |
| 9 | [Event-Driven Programming](units/u9-event-driven-programming) | 12 (4 / 8) | 540 (180 / 360) | 6 | 0 | 540 | ❌ 0/6 |
|  | **TOTAL (units 1–9)** | **60 (16 / 44)** | **2,700 (720 / 1,980)** | **30** | **810 (225 / 585)** | **1,890** | **9/30 meetings built** |

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
| 6 | Writing strings using Turtle | Add to U6 m3 or m4 |
| 7 | Algorithmic problems using Turtle | Add to U7 m2 or m3 |
| 7 | Min/max pattern is taught but not in the official list | Keep only if it fits in the 270 minutes |
| 8 | Functions without parameters: 3 official practice hours, only reviewed in the plan | Include them in the m3/m4 labs |

## Schedule

All 31 meetings in teaching order. Fill in **Target week** once the school calendar is known, and **Taught on** after each lesson.

| # | Meeting | Content | Built | Target week (starts Sunday) | Taught on |
|---:|---|---|---|---|---|
| 1 | 0.1 Environment Setup | Install, check, save | ✅ | Oct 4, 2026 | |
| 2 | 1.1 Introduction to Python | First program: print, comments, first function | ✅ | Oct 11, 2026 | |
| 3 | 2.1 Turtle & Graphics | Turtle library, work surface, movement | ✅ | Oct 18, 2026 | |
| 4 | 2.2 Turtle & Graphics | Pen and shape attributes | ✅ | Oct 25, 2026 | |
| 5 | 2.3 Turtle & Graphics | Geometry challenge | ✅ | Nov 1, 2026 | |
| 6 | 3.1 Variables, Input/Output & Arithmetic | Variables, types, input, friendly output | ✅ | Nov 8, 2026 | |
| 7 | 3.2 Variables, Input/Output & Arithmetic | Input → calculation → output | ✅ | Nov 15, 2026 | |
| 8 | 4.1 Conditional Execution | Boolean expressions, truth tables, and/or | 🔶 | Nov 22, 2026 | |
| 9 | 4.2 Conditional Execution | if and if/else, input filter | 🔶 | Nov 29, 2026 | |
| 10 | 4.3 Conditional Execution | Compound conditions, nesting, Turtle, checkpoint | 🔶 | Dec 13, 2026 | |
| 11 | 5.1 Repetition / Loops | Why loops; for and range | ⏳ | Dec 20, 2026 | |
| 12 | 5.2 Repetition / Loops | while, stop condition | ⏳ | Dec 27, 2026 | |
| 13 | 5.3 Repetition / Loops | Loops with Turtle | ⏳ | Jan 3, 2027 | |
| 14 | 5.4 Repetition / Loops | Tracing and loop challenge | ⏳ | Jan 10, 2027 | |
| 15 | 6.1 Strings | str, indexing, len, + * in | ⏳ | Jan 17, 2027 | |
| 16 | 6.2 Strings | Slicing and string methods | ⏳ | Jan 24, 2027 | |
| 17 | 6.3 Strings | String manipulation problems | ⏳ | Jan 31, 2027 | |
| 18 | 6.4 Strings | Text-processing challenge | ⏳ | Feb 7, 2027 | |
| 19 | 7.1 Algorithmic Problems | Counter, accumulator, random | ⏳ | Feb 14, 2027 | |
| 20 | 7.2 Algorithmic Problems | Combined pattern problems | ⏳ | Feb 21, 2027 | |
| 21 | 7.3 Algorithmic Problems | Algorithmic challenge | ⏳ | Feb 28, 2027 | |
| 22 | 8.1 Functions with Parameters | Why functions; parameters | ⏳ | Mar 7, 2027 | |
| 23 | 8.2 Functions with Parameters | Scope, local vs global | ⏳ | Mar 14, 2027 | |
| 24 | 8.3 Functions with Parameters | Parameterized Turtle functions | ⏳ | Mar 21, 2027 | |
| 25 | 8.4 Functions with Parameters | Integrated modular task | ⏳ | Mar 28, 2027 | |
| 26 | 9.1 Event-Driven Programming | Why event-driven; first interactive program | ⏳ | Apr 4, 2027 | |
| 27 | 9.2 Event-Driven Programming | Mouse events (onclick) | ⏳ | May 2, 2027 ⚠️ May | |
| 28 | 9.3 Event-Driven Programming | Keyboard events (onkey, listen) | ⏳ | May 9, 2027 ⚠️ May | |
| 29 | 9.4 Event-Driven Programming | Animation with a timer | ⏳ | May 16, 2027 ⚠️ May | |
| 30 | 9.5 Event-Driven Programming | Build an interactive game | ⏳ | May 23, 2027 ⚠️ May | |
| 31 | 9.6 Event-Driven Programming | Final project and assessment | ⏳ | May 30, 2027 ⚠️ May | |

## Meeting log

One row per built meeting. Minutes come from the **Duration** and **Structure** lines of its lesson notes.

| Unit | Meeting | Minutes | Theory / Practice | Structure | Source | Notes |
|---|---|---:|---:|---|---|---|
| 0 | 0.1 Environment Setup | 90 | 0 / 90 | Lab + Lab | [`m1-lesson-notes.md`](units/u0-environment-setup/m1-lesson-notes.md) | Outside the 60 h budget |
| 1 | 1.1 Introduction to Python | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u1-introduction-python/m1-lesson-notes.md) | Slides: NotebookLM deck `m1-slides-he.pdf` (20 slides, 85 min + 5 buffer); notes, brief and code rewritten to match |
| 2 | 2.1 Turtle & Graphics | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u2-turtle-graphics/m1-lesson-notes.md) | Reviewed by ChatGPT (round 1 fixes applied); slides: `m1-slides-he.pdf` (23 slides, 90 min) |
| 2 | 2.2 Turtle & Graphics | 90 | 0 / 90 | Lab + Lab | [`m2-lesson-notes.md`](units/u2-turtle-graphics/m2-lesson-notes.md) | Reviewed by ChatGPT (round 1 fixes applied); slides: `m2-slides-he.pdf` (15 slides, 90 min) |
| 2 | 2.3 Turtle & Graphics | 90 | 0 / 90 | Lab + Lab | [`m3-lesson-notes.md`](units/u2-turtle-graphics/m3-lesson-notes.md) | Slides: `m3-slides-he.pdf` (18 slides, 90 min); lab brief converted to Markdown |
| 3 | 3.1 Variables, Input/Output & Arithmetic | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u3-variables-io-arithmetic/m1-lesson-notes.md) | New; closes the Turtle-variables and compound-output gaps; slides: `m1-slides-he.pdf` (22 slides) |
| 3 | 3.2 Variables, Input/Output & Arithmetic | 90 | 0 / 90 | Lab + Lab | [`m2-lesson-notes.md`](units/u3-variables-io-arithmetic/m2-lesson-notes.md) | Slides: `m2-slides-he.pdf` (22 slides, 90 min); lab brief converted to Markdown |
| 4 | 4.1 Conditional Execution | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u4-conditional-execution/m1-lesson-notes.md) | Inspired by the teacher's raw deck; slides: `m1-slides-he.pdf` (23 slides, 90 min; NotebookLM, patched) |
| 4 | 4.2 Conditional Execution | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u4-conditional-execution/m2-lesson-notes.md) | Inspired by the teacher's raw deck; slides pending (NotebookLM folder ready) |
| 4 | 4.3 Conditional Execution | 90 | 0 / 90 | Lab + Lab | [`m3-lesson-notes.md`](units/u4-conditional-execution/m3-lesson-notes.md) | Unit checkpoint (practical + tracing); slides pending (NotebookLM folder ready) |

## Keeping this up to date

When a meeting is added or its timing changes:
1. Add or update its row in the **Meeting log**, and mark it 🔶 in the **Schedule** (✅ only after the teacher approves it).
2. Update that unit's **Planned minutes**, **Remaining** and **Built** in the time budget, and the totals.
3. A unit's planned minutes must not exceed its official minutes. If they would, cut the lesson or
   note the overrun in the unit row with the reason.
4. Update the status of the topics it covers in the unit's `unit-strategy.md` ("Official topics and hours"),
   and remove any gap it closes from **Open coverage gaps**.

After each lesson is taught:
1. Fill in **Taught on** in the **Schedule**.
2. Recheck **Deadline and pace**: meetings left in the schedule must not exceed meetings left before the exam.

Each unit folder's `unit-strategy.md` has the full official scope,
per-meeting breakdown, exit criteria, depth boundary and enrichment notes
for that unit.
