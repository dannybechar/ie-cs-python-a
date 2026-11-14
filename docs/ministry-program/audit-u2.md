# Audit: Unit 2 (Turtle and Graphics) against the ministry Classroom program

Audited 2026-11-13. Repo: `units/u2-turtle-graphics` (`unit-strategy.md`, `README.md`, `m1-3-lesson-notes.md`, `m1-3-lab-brief-he.md`, `exercises/`, `solutions/`, three decks, tests not audited). Ministry sources: folder meeting 11 (`extracts/materials-m11-1-b5b1f5.md`, `classwork-m11-2-e06b98.md`), folder meeting 14 (`materials-m14-1-c60ce9.md`, `classwork-m14-2-a38593.md`, `materials-m14-5-63a137.md`), the formula sheet (`materials-m19-2-5389b6.md`, "מודל Turtle") and `materials-misc-7fa1b5.md` (teacher notes for meetings 11 and 14). Hours authority: `docs/ministry-source/python-a.pdf` Chapter 2 (p.7) and its overview (p.3).

## Verdict

1. **Blocking (decision needed):** the repo teaches the turtle only as module-level calls (`turtle.forward`, `turtle.Screen()` unassigned, `turtle.done()`), in every unit from 2 to 9. Every ministry deck and the exam formula sheet write `wn = turtle.Screen()`, `pen = turtle.Turtle()` / `player = turtle.Turtle()`, `pen.forward(...)` and `wn.mainloop()`. The ministry says the `mainloop` line "appears in the curriculum and in the national exams". This deviation is not recorded in `traceability.md`.
2. **Blocking:** coordinates, `goto`, `setx`/`sety`, `position()` are excluded from all three Unit 2 meetings, yet the PDF overview lists "understanding the cursor position in the window" for Unit 2, the ministry teaches it (meeting 14), and the ten extra exercises cannot be done without `goto`. Unit 9 then says `goto` and coordinates "appear for the first time in 9.3". `unit-strategy.md` marks the topic "movement, position and direction" as done.
3. Smaller gaps: `backward`/`back`, abbreviations (`fd lt rt bk pu pd`), `color()` next to `pencolor()`, `fillcolor`/`begin_fill`/`end_fill`, `turtlesize`, and the ministry default-state list.
4. The hours are fine: 270 minutes stay 270; the ministry's own estimates (145 + 180 min) are not the authority. The fixes below total about 30 minutes of content and mostly have to be retrofitted, because all three meetings and the written test are already taught.
5. The ministry's "types of angles" task is a ready-made test of the repo's strongest idea (turn the outside angle) and is worth adopting; the ministry sources contain a few typos to avoid (see end).

Coverage note: the three decks have no text layer (`pdftotext` returns page breaks only; page counts 23, 15, 18 match `README.md`). Audited through the notes. Not read in full: `materials-m14-1-c60ce9.md` slides 26-39 (loops, spirals, balloon).

## Findings

| id | severity | repo location | ministry source | what differs | proposed fix | est. min |
|---|---|---|---|---|---|---:|
| U2-01 | blocking (decision) | all `units/u2*` code and notes (`m1-lesson-notes.md` section 6 table, `m3-lesson-notes.md` section 5 "module-level Turtle calls only"); same rule in `u4`, `u5`, `u6`, `u9` notes; `traceability.md` section 4 (no approved deviation) | `materials-m11-1-b5b1f5.md` slides 5-9 (template with 5 commented parts: import, window `wn`, turtle `pen`, commands, `wn.mainloop()`), slide 5 teacher note; `materials-m19-2-5389b6.md` "מודל Turtle" (`wn = turtle.Screen()`, `player = turtle.Turtle()`, `turtle.mainloop()`, `wn.exitonclick()`) | Repo: `turtle.Screen()` (result unused), `turtle.shape(...)`, `turtle.done()`. Ministry: the window and the turtle are **variables** and commands are methods of the turtle variable; the window is kept open with `wn.mainloop()`. A student who passes the repo course will not have seen `pen.forward(100)`, `wn`, `player`, or `mainloop` before the exam. `turtle.done()` appears nowhere in the ministry material (`grep` finds no `done()`). | Keep module style for lessons already taught, but (a) add a one-time "same program in the exam's notation" page and a 10-minute translation drill (both styles side by side, then read-only questions in `pen.` style); (b) record "module-level style in lessons" as an approved deviation with that mitigation; (c) rewrite the Unit 0 check file in the ministry template (U0-04). Alternative if the teacher prefers: switch the notation from Unit 3 onward (large rewrite of Units 4-9 code, not recommended). Slot for (a): the "Reactivate/trace" blocks of 2.3 (0-18 min) are protected; the cheapest slot is the first 10 minutes of the first Turtle-using later meeting (4.3) or the exam-prep recap. | 10 (one-off) |
| U2-02 | blocking | `unit-strategy.md` topic table row "הוראות תנועה, מיקום ושינוי כיוון ... ✅"; `m1-lesson-notes.md` line 48, `m2-lesson-notes.md` line 44, `m3-lesson-notes.md` section 5 (exclusions); `README.md` extras (use `goto`); `units/u9-event-driven-programming/unit-strategy.md` line 44 and `m3-lesson-notes.md` line 39 ("`goto` and coordinates appear here for the first time") | `materials-m14-1-c60ce9.md` slides 5-12 (default state, axes and quadrants, `position/pos`, `setposition/setpos`, `setx`, `sety`, `goto`, why moving draws a line, `penup/pendown` to move without drawing); `classwork-m14-2-a38593.md` tasks 1-3 (mark points on the axes, read points, square on the axes), tasks 4-6 (square in quadrant 1, 2, four quadrants), 8 (house); PDF Ch.2 overview (p.3) "הבנה והתמצאות מיקום סמן בחלון" and teaching note 3 ("change parameters: angle, **change of position**, number of steps") | The PDF and the ministry both teach the coordinate plane as part of the turtle. The repo reads "position" only as the turtle's state and excludes coordinates, then (a) the ten extra exercises (`exercises/01...10`, solutions) require `goto` and screen coordinates with only a comment line of explanation, (b) Unit 9 claims coordinates appear first in 9.3, and (c) `course-map.md` says "no open coverage gaps". | Add a 8-10 minute "where is the turtle? coordinates, `goto`, `penup`/`pendown` to jump" block. Slot: it needs a home that is not the protected 2.3 assessment; use the opening of the first extra-exercise session, or move 2.2 Task D (`pensize()` retrieval, 10 min) into 2.3's read step and use those 10 minutes. Paper warm-up first (ministry 14.2 tasks 1-3: mark (2,4), (-3,5), (4,-2), (0,0), then name the quadrant). Correct the Unit 9 claim and the course-map gap table. | 10 |
| U2-03 | should | `m1-lesson-notes.md` line 48, `m2-lesson-notes.md` line 44 (`backward()` excluded), `u5/m4-lesson-notes.md` line 46 | `materials-m11-1-b5b1f5.md` slides 10, 16, 33 (`forward/fd`, `left/lt`, `backward/back/bk`, `right/rt`); `materials-m19-2-5389b6.md` (`fd`, `back`, `lt`, `rt`, `pd`, `down`, `pu`, `up`) | The repo teaches only the long names and never `backward`. The ministry teaches long and short names side by side, and the exam sheet lists the short names, so a student can meet `pen.fd(100)` or `pu()` on the exam. | Add a one-slide "short names" table (read-only) and `backward(n)` as a 2-minute demo in 2.1 or 2.2 (Demo 1 pen state). | 3 |
| U2-04 | should | `m2-lesson-notes.md` section 5 and 6 (`pencolor` only; "colored stamps need `fillcolor`/`color`, kept out of Unit 2"); `u9` code uses `turtle.color(...)` | `materials-m11-1-b5b1f5.md` slides 21-27 (`pen.color("green")`, `pen.color("#1AA260")` hex codes; the ministry solutions use `color` throughout); `materials-m19-2-5389b6.md` (`pencolor` = pen colour, `color` = turtle colour) | The repo uses `pencolor` in Unit 2 and `color` in Unit 9: inconsistent inside the course. The ministry's everyday command is `color`, which also colours stamps and the turtle, so the "black stamps" workaround in 2.2 disappears. Hex colour codes are not mentioned in the repo. | Teach `color("red")` as the short form that sets pen and turtle together; keep `pencolor` for "only the line". Mention `"#1AA260"` once. | 3 |
| U2-05 | should | `m2-lesson-notes.md` section 2 (`fillcolor`/`begin_fill` excluded), extras 03 and 07 | `materials-m14-1-c60ce9.md` slides 15-17 (`fillcolor`, `begin_fill()`, `end_fill()`, example, "what happens if we fill an open line?") and tasks #2, #3 | Fill is taught in the ministry course; the repo uses it in two extra exercises with a one-line header only. | Teach as a 5-minute demo with the open-shape question, in the extras session; add `turtlesize(size)` from the formula sheet in the same demo (it is the only sheet command about turtle size and the PDF Ch.2 teaching note lists "size"). | 5 |
| U2-06 | should | `exercises/01-10`, `solutions/01-10`, `README.md` ("no functions, loops or variables"); `units/u6-strings/teacher/L04-text-tools-notes.md` (first `turtle.write`) | `materials-m19-2-5389b6.md`, `materials-m20-1-a1ab64.md` (`circle`, `dot`, `stamp` appear only in later meetings 19-20); `materials-m14-1-c60ce9.md` slide 34 (`bgcolor`, `screensize`, `turtlesize`) | The extras use `goto`, `begin_fill`, `dot`, `circle`, `bgcolor`, `write` that no Unit 2 lesson teaches, and Unit 6 says `turtle.write` is new in 6.4. `circle` and `dot` are taught by the ministry only at meetings 19-20, so the extras run ahead of the ministry order too. | Add a "new commands" table to the extras README (command, one-line meaning, ministry meeting where it is taught), and reword Unit 6.4's "first use" if the extras are assigned before. | 0 |
| U2-07 | should | `m1-lesson-notes.md` section 4 objectives; `m2-lesson-notes.md` "retrieve/update" | `materials-m11-1-b5b1f5.md` slides 5-9 (library, window, turtle as three separate ideas: "ספרייה", "חלונית ציור", "צב גרפי"); PDF Ch.2 concept "פעולות אחזור/עדכון" | Terms: ministry says "חלונית ציור" and "הצב הגרפי"; the repo says "חלון הציור" and "הסמן" (the PDF says "חלון וסמן"). Fine either way; the repo's "עדכון/אחזור" wording matches the PDF. The ministry also calls movement commands "פעולות תנועה יחסיות", styling "פעולות עיצוב", position "פעולות מיקום", pen "פעולות עט". | Use the ministry's four group names in the command table of the lab briefs (no new content). | 0 |
| U2-08 | nice | `m3-lesson-notes.md` section 2 | `materials-m11-1-b5b1f5.md` slides 14-15 (task 2, angle types: acute = `left(145)`, obtuse = `left(45)`; teacher note "the angle changes from the current angle"); task 1 right angle | The ministry's angle task is the same insight as the repo's "the turtle turns the outside angle" (acute drawn angle = turn of 145, obtuse = turn of 45). The repo has no angle-naming task. | Adopt as an optional extension in 2.3 (no input, no `if`: just draw the three angles one after another, each in its own function). | 5 (from the optional letter block) |
| U2-09 | nice | `m1-lesson-notes.md` 7-14 min | `materials-m14-1-c60ce9.md` slide 5 (default state: shape classic, colour black, position (0,0), facing right) | Repo says "starts in the middle, facing right" only. | Add the four defaults to the 2.1 slide that shows the first run. | 1 |
| U2-10 | nice | `README.md` table | n/a (repo-internal) | The written-test row lists only Form A files; Form B (`u2-turtle-test-b-*`) is described in the text below but not in the table. There are two file families: `u2-test-*` (multiple choice) and `u2-turtle-test-*` (written). Starter/solution pairs: `GeometryChallenge_Starter.py` vs `GeometryAssessment_Reference.py` (different stems); ten extras have matching names. | Rename or note the pairing; add Form B to the table. | 0 |
| U2-11 | nice | `unit-strategy.md`, `m1-lesson-notes.md` section 2 | n/a | Every file cites PDF p.7. Verified: Chapter 2 and its hours table are on PDF page 7 (footer 7). The overview with hours is on pp.3-5. | None. | 0 |

## Constructs: repo against ministry (item 1)

| Construct | Ministry | Repo |
|---|---|---|
| `import turtle`; window; turtle; keep window open | meeting 11 (template with `wn`, `pen`, `wn.mainloop()`) | 2.1 (module style, `turtle.done()`) |
| `forward/fd`, `left/lt` | 11 | 2.1 (long names only) |
| `right/rt`, `backward/back/bk` | 11 (slide 16) | `right` in 2.1; `backward` never |
| `pensize`, `shape`, `color` | 11 (slides 19-21) | 2.2 (`pencolor`, not `color`) |
| `penup/pendown` (`up/down`, `pu/pd`) | 14 | 2.2 (earlier than the ministry) |
| `stamp`, `hideturtle`, `showturtle` | `stamp` 19-20; `hideturtle` 14 slide 36 | 2.2 (earlier) |
| axes, quadrants, `position`, `setposition`, `setx`, `sety`, `goto` | 14 | not in lessons (extras only); Unit 9.3 |
| `fillcolor`, `begin_fill`, `end_fill` | 14 | extras only |
| `circle`, `dot`, `bgcolor`, `write`, `speed` | `bgcolor` 14 slide 34; `circle` 19; `dot`, `speed`, `write` 20 | extras (`circle`, `dot`, `bgcolor`, `write`) |
| loops, input, `if` inside turtle tasks | ministry turtle comes after conditions and input (teacher doc: "prior knowledge: output, input, functions, variables, operators, modulo, conditions") | repo teaches turtle first, no loops/input/`if` (PDF unit order), so tasks like the ministry's angle chooser (input + `elif`) cannot be used in Unit 2 |

## Things the repo uses before the ministry introduces them (item 4)

- `stamp()` (ministry: meetings 19-20), `penup/pendown` and `hideturtle` (ministry: meeting 14), functions around turtle tasks from 2.2 (ministry teaches functions at meeting 4, so the ministry also wraps tasks in `def`; this is aligned).
- `pensize()` / `pencolor()` getters printed with `print` in 2.2 Task D; the ministry shows getters only as `position()` and on the sheet (`heading()`, `pos()`, `xcor()`).

## Time budget (item 5)

`course-map.md`: Unit 2 = 270 min (45 theory / 225 practice); the PDF gives the same. Proposed additions: U2-01 10, U2-02 10, U2-03 3, U2-04 3, U2-05 5, U2-08 5, U2-09 1 = 37 minutes. Funding: 2.2 Task D merge (10), the optional letter block in 2.1 (10, already "cut first"), the extras session (outside the budget), and the exam-prep recap. Only U2-02 needs a real slot; if no slot is found, teach it with a worksheet in the extras session and record it as an approved deviation rather than overrun 2.3.

## Meeting 11 / 14 exercises against the repo

| Ministry task | Repo equivalent | Verdict |
|---|---|---|
| 11 #1 right angle, function `right_angle()` | 2.1 L-shaped letters, 2.1 first moves | covered |
| 11 #2 types of angles (input + `elif`) | none | adopt without input/`if` (U2-08) |
| 11 #3 square with all four commands incl. `backward` | 2.1 square (no `backward`) | add `backward` variant |
| 11 #4 coloured square, input for pen size and side | 2.2 Task B colour square; 3.1 Task 3 `turtle_square()` (side by input) | covered across Units 2-3; add pen-size input as an extension in 3.1 |
| 11 #5 coloured equilateral triangle | 2.1 triangle, 2.2 colours | covered |
| 11 #6 coloured pentagon (turn 72), #7 pentagram (turn 144) | extra 07 star (turn 144), Unit 5.2 polygons | pentagon: 10 instructions, over the 8-instruction limit; leave to Unit 5 |
| 14 #1-#3 mark points / read points / square on axes (GeoGebra) | none | adopt on paper (U2-02) |
| 14 #4-#6 square in quadrant 1, 2, four squares in four quadrants | extra 01 (rectangle upper-left with `goto`) | extend extras |
| 14 #7 polygon generator (input + `elif`) | none | Unit 8/9 material, not Unit 2 |
| 14 #8 house with red triangular roof, challenge: windows, door | extra 05 `HouseWithRedRoof` | covered; add the challenge as a stretch |

## Ministry exercises to adopt

| Ministry item | File | Adopt as | Mandatory? | Min |
|---|---|---|---|---:|
| 11 #2 types of angles (drawn without input) | `materials-m11-1-b5b1f5.md` slides 14-15; `classwork-m11-2-e06b98.md` task 2 | 2.3 optional extension (U2-08) | no marks in the sheet (the sheet has no mandatory/optional labels for meeting 11) | 5 |
| 11 #3 square with `backward` | slide 17-18 | 2.1/2.2 variant of the square | no mark | 3 |
| 14 #1-#3 axes on paper | `classwork-m14-2-a38593.md` tasks 1-3 | coordinates warm-up (U2-02) | no mark | 5 |
| 14 #4-#6 squares in quadrants | tasks 4-6 | extras 11-13 (new) | no mark | 0 in class |
| 14 #8 house with windows and door | task 8 | extra 05 stretch | challenge ("אתגר") | 0 in class |
| Exam-style questions | none about the turtle in meetings 11 and 14; the formula sheet is the only exam artefact (`materials-m19-2-5389b6.md`) | build 3 read-only questions in `pen.`/`wn.` notation for U2-01 | n/a | 10 |

H5P and "Master Python" items for meetings 11 and 14 (11.3 "Ninja Turtles", 14.3 "Summer camp") exist only as links (`links.md`) and could not be read.

## Ministry source defects found (do not copy)

- `materials-m14-1-c60ce9.md` slide 11 writes `penup(x, y)` and `pendown(x, y)`; both take no arguments.
- Slide 36 writes `hideTurtle` and `shoTurtle` (wrong case and spelling); the working names are `hideturtle`/`showturtle`.
- Slide 33 imports `random` and `time` for the balloon task before those libraries are taught.
