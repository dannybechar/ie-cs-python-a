# Grade 7 course map — Python A

Official numbering and hours from [`docs/ministry-source/python-a.pdf`](docs/ministry-source/python-a.pdf) (hours table, pp. 3–5).
Full framing strategy: [`docs/annual-strategy.md`](docs/annual-strategy.md).

## Time budget

1 academic hour = 45 minutes, so the course is 60 hours = **2,700 minutes** = 30 double meetings of 90 minutes.
Minutes are written as **total (theory / practice)**. "Planned" counts only meetings that are built in the repo.

| # | Unit | Official hours (T/P) | Official minutes (T/P) | Meetings | Planned minutes (T/P) | Remaining | Built |
|---|---|---:|---:|---:|---:|---:|---|
| 0 | [Environment Setup](units/u0-environment-setup) — *school addition* | — | — | 1 | 90 (0 / 90) | *+90 outside the budget* | ✅ 1/1 |
| 1 | [Introduction to Python](units/u1-introduction-python) | 2 (1 / 1) | 90 (45 / 45) | 1 | 90 (45 / 45) | 0 | ✅ 1/1 |
| 2 | [Turtle & Graphics](units/u2-turtle-graphics) | 6 (1 / 5) | 270 (45 / 225) | 3 | 90 (0 / 90) | 180 | ⚠️ 1/3 (m3 only) |
| 3 | [Variables, Input/Output & Arithmetic](units/u3-variables-io-arithmetic) | 4 (1 / 3) | 180 (45 / 135) | 2 | 90 (0 / 90) | 90 | ⚠️ 1/2 (m2 only) |
| 4 | [Conditional Execution](units/u4-conditional-execution) | 6 (2 / 4) | 270 (90 / 180) | 3 | 0 | 270 | ❌ 0/3 |
| 5 | [Repetition / Loops](units/u5-loops) | 8 (2 / 6) | 360 (90 / 270) | 4 | 0 | 360 | ❌ 0/4 |
| 6 | [Strings](units/u6-strings) | 8 (2 / 6) | 360 (90 / 270) | 4 | 0 | 360 | ❌ 0/4 |
| 7 | [Algorithmic Problems](units/u7-algorithmic-problems) | 6 (1 / 5) | 270 (45 / 225) | 3 | 0 | 270 | ❌ 0/3 |
| 8 | [Functions with Parameters](units/u8-functions-parameters) | 8 (2 / 6) | 360 (90 / 270) | 4 | 0 | 360 | ❌ 0/4 |
| 9 | [Event-Driven Programming](units/u9-event-driven-programming) | 12 (4 / 8) | 540 (180 / 360) | 6 | 0 | 540 | ❌ 0/6 |
|  | **TOTAL (units 1–9)** | **60 (16 / 44)** | **2,700 (720 / 1,980)** | **30** | **270 (45 / 225)** | **2,430** | **3/30 meetings built** |

Unit 0 is a school addition outside the official 60 hours: one lab meeting
to install and check the environment before Unit 1 (it covers Chapter 1
goals 1–2, "install" and "run the working environment"). With it, the
year is 31 meetings.

**Theory vs. practice:** Units 2 and 3 are behind on theory so far (0 of 45 minutes each), because only
their Lab + Lab meetings are built. Their first meetings, still to be written, should carry the
45 theory minutes.

## Deadline and pace

- **Deadline:** the Ministry's Python A exam (בחינת מפמ"ר) is estimated for **May 2027**, with the exact date to be sent during the year
  ([`ministry-circular-tashpaz-he.pdf`](docs/ministry-source/ministry-circular-tashpaz-he.pdf), p.2).
  All 9 units must be taught before it, not by the end of June.
- **Meetings needed:** 31 = 30 official + Unit 0.
- **Meetings available:** *to fill in from the school calendar*: first lesson date, meetings per week, and holidays/trips before the exam.
  Rough estimate: at **one double meeting a week**, from early October 2026 to the end of April 2027 there are about 30 weeks,
  minus about 3–4 weeks of Hanukkah and Passover breaks, so **about 26–27 meetings, plus 1–3 in May**. That is probably
  **fewer than 31**. If the class meets once a week, plan now which meetings to merge or shorten.
- **Check after every lesson:** meetings left in the schedule below ≤ meetings left before the exam.

## Open coverage gaps

Official topics that no planned meeting fully covers yet. Details are in each unit's `unit-strategy.md`, under "Official topics and hours".

| Unit | Gap | Fix to plan |
|---|---|---|
| 1 | Compound output (several values in one `print`) | Add to U1 m1 or U3 m1 |
| 1 | The NotebookLM deck for class runs about 100–115 min, not 90 | Correction plan in Downloads (`notebooklm-unit1-deck-fixes.md`) |
| 3 | Teaching variables using Turtle | Add to U3 m1 |
| 6 | Writing strings using Turtle | Add to U6 m3 or m4 |
| 7 | Algorithmic problems using Turtle | Add to U7 m2 or m3 |
| 7 | Min/max pattern is taught but not in the official list | Keep only if it fits in the 270 minutes |
| 8 | Functions without parameters: 3 official practice hours, only reviewed in the plan | Include them in the m3/m4 labs |

## Schedule

All 31 meetings in teaching order. Fill in **Target week** once the school calendar is known, and **Taught on** after each lesson.

| # | Meeting | Content | Built | Target week | Taught on |
|---:|---|---|---|---|---|
| 1 | U0 m1 | Install, check, save | ✅ | | |
| 2 | U1 m1 | First program: print, comments, first function | ✅ | | |
| 3 | U2 m1 | Turtle library, work surface, movement | ⏳ | | |
| 4 | U2 m2 | Pen and shape attributes | ⏳ | | |
| 5 | U2 m3 | Geometry challenge | ✅ | | |
| 6 | U3 m1 | Variables, types, input, friendly output | ⏳ | | |
| 7 | U3 m2 | Input → calculation → output | ✅ | | |
| 8 | U4 m1 | Boolean expressions, simple conditional | ⏳ | | |
| 9 | U4 m2 | else, and/or, nesting | ⏳ | | |
| 10 | U4 m3 | Integrated decisions (Turtle) | ⏳ | | |
| 11 | U5 m1 | Why loops; for and range | ⏳ | | |
| 12 | U5 m2 | while, stop condition | ⏳ | | |
| 13 | U5 m3 | Loops with Turtle | ⏳ | | |
| 14 | U5 m4 | Tracing and loop challenge | ⏳ | | |
| 15 | U6 m1 | str, indexing, len, + * in | ⏳ | | |
| 16 | U6 m2 | Slicing and string methods | ⏳ | | |
| 17 | U6 m3 | String manipulation problems | ⏳ | | |
| 18 | U6 m4 | Text-processing challenge | ⏳ | | |
| 19 | U7 m1 | Counter, accumulator, random | ⏳ | | |
| 20 | U7 m2 | Combined pattern problems | ⏳ | | |
| 21 | U7 m3 | Algorithmic challenge | ⏳ | | |
| 22 | U8 m1 | Why functions; parameters | ⏳ | | |
| 23 | U8 m2 | Scope, local vs global | ⏳ | | |
| 24 | U8 m3 | Parameterized Turtle functions | ⏳ | | |
| 25 | U8 m4 | Integrated modular task | ⏳ | | |
| 26 | U9 m1 | Why event-driven; first interactive program | ⏳ | | |
| 27 | U9 m2 | Mouse events (onclick) | ⏳ | | |
| 28 | U9 m3 | Keyboard events (onkey, listen) | ⏳ | | |
| 29 | U9 m4 | Animation with a timer | ⏳ | | |
| 30 | U9 m5 | Build an interactive game | ⏳ | | |
| 31 | U9 m6 | Final project and assessment | ⏳ | | |

## Meeting log

One row per built meeting. Minutes come from the **Duration** and **Structure** lines of its lesson notes.

| Unit | Meeting | Minutes | Theory / Practice | Structure | Source | Notes |
|---|---|---:|---:|---|---|---|
| 0 | m1 Install, check, save | 90 | 0 / 90 | Lab + Lab | [`m1-lesson-notes.md`](units/u0-environment-setup/m1-lesson-notes.md) | Outside the 60 h budget |
| 1 | m1 First program | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u1-introduction-python/m1-lesson-notes.md) | The NotebookLM deck planned for class runs about 100–115 min as is; the correction plan cuts it to 90 |
| 2 | m3 Geometry challenge | 90 | 0 / 90 | Lab + Lab | [`m3-lesson-notes.md`](units/u2-turtle-graphics/m3-lesson-notes.md) | |
| 3 | m2 Input to result | 90 | 0 / 90 | Lab + Lab | [`m2-lesson-notes.md`](units/u3-variables-io-arithmetic/m2-lesson-notes.md) | |

## Keeping this up to date

When a meeting is added or its timing changes:
1. Add or update its row in the **Meeting log**, and mark it ✅ in the **Schedule**.
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
