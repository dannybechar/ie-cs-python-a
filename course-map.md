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
1. Add or update its row in the **Meeting log**.
2. Update that unit's **Planned minutes**, **Remaining** and **Built** in the time budget, and the totals.
3. A unit's planned minutes must not exceed its official minutes. If they would, cut the lesson or
   note the overrun in the unit row with the reason.

Each unit folder's `unit-strategy.md` has the full official scope,
per-meeting breakdown, exit criteria, depth boundary and enrichment notes
for that unit.
