# Plan to the mafmar exam — Python A, Monday 15 March 2027

Source of scope: [`ministry-source/focus-python-a-tashpaz-he.pdf`](ministry-source/focus-python-a-tashpaz-he.pdf) (the תשפ"ז focus document). Course status: [`../class-progress.md`](../class-progress.md), [`../course-map.md`](../course-map.md).
Status: **approved by the teacher on 18 Nov 2026**. Applies to Grade 7 and Grade 8 (same point in the course).

## 1. What is on the exam (from the focus document)

| Focus ch. | On the exam | Excluded (red) | Repo meetings |
|---|---|---|---|
| 1 | print (simple, compound); documentation, naming, file names; function structure and call; function with no parameters and no return value | — | 1.1, 8.2 (trimmed) |
| 2 | Turtle library, window coordinates, **basic** Turtle commands | — | 2.1–2.3 (taught) |
| 3 | variables, `input`, types and assignment, arithmetic, `%` and `//` | variables with Turtle | 3.1, 3.2 |
| 4 | Boolean conditions, `if`, `if/else`, `and`/`or`, `elif` | `not` (struck out), conditions with Turtle | 4.1–4.3 |
| 5 | `for` with a fixed count | `while`, nested loops, loops with Turtle | 5.1, 5.2 |
| 6 | — | Strings: whole chapter | — |
| 7 | counter, accumulator | random number, algorithms with Turtle | 7.1, 7.2 |
| 8 | function with no return value (as in ch. 1) | `global`, parameters, Turtle functions: whole chapter | 8.2 only |
| 9 | — | Event-driven: whole chapter | — |

**Consequence:** of the 31 meetings, only about 12 carry exam material. Units 6, 9 and most of 8, plus 5.3, 5.4 and 7.3, are not examined on 15 Mar.

## 2. Calendar

Sundays from 22 Nov to 14 Mar, skipping 6 Dec (Hanukkah, as in `course-map.md`): **16 meetings**. The 14 Mar meeting is the day before the exam.
3.2 was **not** taught on 15 Nov (teacher's correction, 18 Nov): it moves to 22 Nov with the Q1 quiz, and the flex slot absorbs the shift. Still to confirm: no other Sunday closures (end-of-semester events, trips); exam length and room are not yet known.

## 3. The plan

Phases: **A** teach exam material (P1–P10) · **B** full-scope tests and gap closing (P11–P12) · **C** exam rehearsal and final preparation (P13–P16).

| # | Sunday | Content | Assessment / practice |
|---:|---|---|---|
| P1 | 22 Nov | **Q1 quiz first**, then 3.2 Input/Output & Arithmetic (not taught on 15 Nov) | **Quiz Q1** (10 min, variables; already built) |
| P2 | 29 Nov | 4.1 Boolean expressions, truth tables, `and`/`or` | Trace-table warm-up (5 min) |
| P3 | 13 Dec | 4.2 `if`, `if/else` | Exit ticket |
| P4 | 20 Dec | 4.3 compound conditions, nesting, `elif`; Turtle part cut (not examined) | Trace-table warm-up |
| P5 | 27 Dec | 5.1 `for` and `range`, loop variable | **Quiz Q2** (15 min, Unit 4) |
| P6 | 3 Jan | 5.2 `range` with a step; loop with a running total; Turtle only as an optional extra | Trace-table warm-up |
| P7 | 10 Jan | Mixed lab: ch. 3, 4, 5 together (45 min) | **Test T1** (45 min, Units 3–5) |
| P8 | 17 Jan | T1 feedback (15 min) + 7.1 counter | Exit ticket |
| P9 | 24 Jan | 7.2 accumulator, average, minimum and maximum | Trace-table warm-up |
| P10 | 31 Jan | Functions in exam scope: structure, call, no parameters, no return, naming and documentation (8.2 trimmed) | **Quiz Q3** (15 min, Unit 7) |
| P11 | 7 Feb | Mixed lab across all examined chapters | **Test T2** (60 min, all examined chapters, mafmar format) |
| P12 | 14 Feb | T2 feedback and gap closing by weak topic; Turtle basics refresher (the former flex slot, now used) | Short retake quizzes by topic |
| P13 | 21 Feb | — | **Rehearsal R1**: past mafmar exam under exam conditions (full session) |
| P14 | 28 Feb | Item-by-item review of R1; targeted practice; exam technique (reading the task, trace tables, time split) | **Quiz Q4** (10 min) on the weakest chapter |
| P15 | 7 Mar | — | **Rehearsal R2**: second past exam or built mock, under exam conditions |
| P16 | 14 Mar | Review of R2, aids sheet, logistics; quick-fire questions per chapter, Q&A. **No new material** | None (confidence, not stress) |

Totals: 9 meetings of new material (3.2, 4.1–4.3, 5.1, 5.2, 7.1, 7.2, functions), 2 tests (T1, T2), 4 quizzes (Q1–Q4), 2 full rehearsals, 3 review and gap-closing meetings.

## 4. Rules of the plan

- **Exam-first order:** nothing out of scope is taught before 15 Mar. Meetings 5.3, 5.4, 6.1–6.4, 7.3, 8.1, 8.3, 8.4 and 9.1–9.6 (16 meetings) move to **after the exam**, from 21 Mar. The school year then has about 11–14 Sundays for them, so merging will be needed. That is a later decision.
- **Trim, don't extend:** 5.1–5.2 and 8.2 are compressed to exam scope. Official unit minutes (Unit 5: 360, Unit 8: 360) are not met before the exam; the remainder is taught afterwards.
- **If a Sunday is lost:** there is no flex slot left (it was used when 3.2 moved to 22 Nov). Drop Q4 and shorten the T1 feedback; if a second is lost, make R2 a half-exam and fold exam technique into P16.
- **Past exams:** use only items inside the focus. The index of past exams is in [`ministry-source/exam-index-python-a-he.pdf`](ministry-source/exam-index-python-a-he.pdf) (links only, so the teacher must download them). Older exams can include `while`, strings or functions with parameters; mark or replace those items before use. Check the aids sheet (דף עזר) of the relevant year.
- **Pass line before rehearsal:** T2 average and a per-chapter table decide what P12 covers.

## 5. Open questions

1. Exam length and the exact format (parts, points) are not in the repo: confirm from the Ministry's circular or the exam index.
2. Are Turtle loops within "basic Turtle commands" in chapter 2? The focus excludes Turtle in chapters 3, 4, 5 and 7 but chapter 2 allows basic commands. I plan to keep Turtle to the Unit 2 commands only.
3. Is the `% `-and-`//` content in 3.1 and 3.2 enough, or does it need a practice sheet?
4. Is 6 Dec really free, and is there any known closure (semester end, trips, exams in other subjects)?

## 6. Material to build (not done yet)

| Item | For meeting | Status |
|---|---|---|
| Trimmed decks and briefs for 4.1–4.3, 5.1–5.2, 7.1–7.2, functions (no Turtle, no `not`) | P2–P10 | Not built; existing decks are pre-alignment |
| Quizzes Q2, Q3, Q4 (Q1 exists) | P5, P10, P14 | Not built |
| Tests T1 and T2 with keys | P7, P11 | Not built |
| Mixed labs and gap-closing stations | P7, P11, P12 | Not built |
| Mock exam in mafmar format (if the past exams are unsuitable) and keys | P13, P15 | Not built |
| Update `course-map.md` and `class-progress.md` to this order | — | Done 18 Nov, revised the same day for 3.2 on 22 Nov |
