# Audit: Units 0 and 1 against the ministry Classroom program

Audited 2026-11-13. Repo: `units/u0-environment-setup`, `units/u1-introduction-python`. Ministry sources: `extracts/materials-m00-1-7969dd.md`, `materials-m00-2-3781f1.md`, `classwork-m00-3-e8380d.md` (folder meeting 0); `materials-m01-1-b6cfe9.md`, `classwork-m01-2-98da55.md` (folder meeting 1); `materials-m04-1-8172ae.md` slides 5-8 (only the `def`/call part of folder meeting 4); `materials-m19-2-5389b6.md` (formula sheet); `materials-misc-7fa1b5.md`. Hours authority: `docs/ministry-source/python-a.pdf` Chapter 1 (p.6).

## Verdict

1. Unit 0 is consistent with the PDF (goals 1-2) and fits its own 90 minutes; the ministry meeting 0 is about the Classroom workflow, not installation, so the two do not overlap much. No blocking item.
2. Unit 1 omits the ministry's first topic, the **algorithm** concept (PDF goal 7 "pseudo-verbal algorithm to running program" also asks for it), and the escape sequences `\n` / `\t` taught on slides 17-20 of the ministry deck.
3. The ministry marks only **task 4, the business card in a star frame, as mandatory** (`classwork-m01-2-98da55.md`); the repo has no equivalent and uses a different exit mission.
4. Terminology: the ministry calls a function **פעולה** (787 uses of "פעולה" against 7 of "פונקציה" across all extracts); the repo's Hebrew briefs say "פונקציה" only. The PDF itself says "פונקציה", so both words must be shown.
5. All time fixes below fit inside the existing 90 minutes by using the lab's own "cut first" list (Unit 1) or by replacing a teacher-walk-around step (Unit 0); nothing needs extra minutes. Units 0-1 are already taught, so they apply as notes to the deck/brief for the next cohort or as warm-ups in Unit 3.

Coverage note: the decks `m1-slides-he.pdf` in both units have **no text layer** (`pdftotext` returns only page breaks; 12 and 20 pages, matching the notes). The deck content was audited through `m1-lesson-notes.md` slide tables, not through the PDFs.

## Findings: Unit 0 (Environment Setup)

| id | severity | repo location | ministry source | what differs | proposed fix | est. min |
|---|---|---|---|---|---|---:|
| U0-01 | should | `m1-lesson-notes.md` 82-87 exit check; `m1-lab-brief-he.md` step 7 | `materials-m00-2-3781f1.md` slides 2-13 (Classroom workflow, "הגש", Snipping Tool, file upload); `classwork-m00-3-e8380d.md` (mood task, must press "הגש") | Ministry meeting 0 is a Classroom orientation with three hands-on submission tasks (0.3 mood, 0.4 screenshot, 0.5 upload a file). The repo has no submission step: evidence is "show the teacher". Whether the school uses Classroom is not stated anywhere in the repo. | Decide and record in `traceability.md`: if Classroom (or any LMS) is used, replace the 82-87 teacher walk-around with "take a screenshot of the check output and submit it" (the ministry 0.4 task). If not used, record "no Classroom" as an approved deviation. | 0 (replaces the 5-min walk-around) |
| U0-02 | nice | `m1-lesson-notes.md` 0-5 hook | `materials-m00-1-7969dd.md` slide 14 ("we will practice for the Ministry exam on computers") | The repo never tells the class that the year ends with the national exam (estimated May 2027, `course-map.md`). | One sentence at the end of the hook: "In May there is a national exam on a computer; this year trains for it." | 1 (inside the hook) |
| U0-03 | should | `m1-lesson-notes.md` section 6 (troubleshooting), 75-82 (home install) | `materials-m01-1-b6cfe9.md` slide 14: classes working from home, or schools without the software, may use a **web environment** | The repo's only fallback for blocked installs is a portable zip or IT. The ministry names a web environment as an accepted alternative. Which environment the exam uses is not stated in anything read; do not assume. | Add one troubleshooting row "no install possible at home: ask the teacher for the web option" and put "which environment does the exam use" on the teacher's question list for the ministry. | 2 |
| U0-04 | should | `exercises/EnvironmentCheck.py` (whole file); `m1-lesson-notes.md` 55-65 ("by the end of the year you will be able to write all of it") | `materials-m11-1-b5b1f5.md` slides 5-9 (template: `wn = turtle.Screen()`, `pen = turtle.Turtle()`, `wn.mainloop()`) | The check file uses `import sys`, `try/except ImportError`, `sys.exit()`, `sys.version_info`, `for`, `goto`, `write` and `t = turtle.Turtle()`. None of the try/except or sys part is ever taught in Python A, so the promise on the slide is false. It is also the **only** repo file that creates `t = turtle.Turtle()`, while Units 2-9 forbid that style (see U2-01). | Rewrite only the drawing part in the ministry template (`import turtle`, `wn = turtle.Screen()`, `pen = turtle.Turtle()`, `wn.mainloop()`), and change the promise to "most of this you will understand by the end of the year". Keep the OK-lines logic (it is the real test). Decide together with U2-01. | 0 (teacher prep) |
| U0-05 | nice | `m1-lesson-notes.md` section 5; `README.md` | n/a | Unit 0 is the only unit whose notes do not map slides to minutes: the deck has 12 slides, the notes have 11 time blocks and name no slide. Unit 1 and Unit 3 do list slides per block. | Add a slide column to the 0-90 timeline. | 0 |
| U0-06 | nice | `m1-lesson-notes.md` header; `m1-lab-brief-he.md` step 5 | n/a | Claims "Thonny 5.0.0 / Python 3.14, current in September 2026" and the expected output line `Python version: 3.14.x`. I could not verify these from the repo or the ministry material. | Re-check the version on one lab PC before the next cohort; make the expected line "3.x". | 0 |
| U0-07 | nice | `unit-strategy.md` | `materials-m00-1-7969dd.md` slides 3-11 (eight "get to know you" prompts), `classwork-m00-3-e8380d.md` question 2 ("what do you expect from the lessons") | Ministry opens with an ice-breaker and an expectations question; the repo opens with the demo. | Optional: use the expectations question as a one-line written answer in the exit check. | 2 |

## Findings: Unit 1 (Introduction to Python)

| id | severity | repo location | ministry source | what differs | proposed fix | est. min |
|---|---|---|---|---|---|---:|
| U1-01 | should | `m1-lesson-notes.md` sections 1-2 (scope and goal); `m1-lab-brief-he.md` title line says "מבוא לאלגוריתמיקה" | `materials-m01-1-b6cfe9.md` slides 2-11 (definition "an algorithm is a sequence of actions leading to the solution of a specific problem"; chocolate sandwich; drawing a square; drawing a rectangle, each written as steps with units); PDF Ch.1 goal 7 | The word "algorithm" is missing from every Unit 1 file except the brief title. The PDF goal "turn a pseudo-verbal algorithm into a running program" and the PDF teaching note ("emphasis on the simple algorithm, instruction after instruction") are not stated as objectives. The ministry opens with it. | Add the one-sentence definition on slide 2 (the countdown predict) and name the countdown as "an algorithm in steps". In the exit mission (slide 19) add "first write the 4 steps in words, then in code". The ministry square algorithm is exactly the Unit 2.1 human-turtle hook (`units/u2-turtle-graphics/teacher/L01-first-moves-notes.md` 0-7 min): label it "an algorithm for a square" there at no cost. | 1 in 1.1, 0 in 2.1 |
| U1-02 | should | `m1-lesson-notes.md` sections 5-6; whole of `units/u1*`; grep across `units/u[0-3]*` finds no `\n` or `\t` | `materials-m01-1-b6cfe9.md` slides 17-20 (`print("python\nlanguage")` "הורד שורה"; `print("so\tcool")` "טאב"); tasks 2 and 3 on the same deck | The repo never teaches the two escape sequences. Ministry teaches them in meeting 1 as commands with Hebrew names. The ministry's explanation "a tab is five spaces" is wrong (a tab goes to the next tab stop); do not copy that sentence. | Teach `\n` and `\t` as a 4-minute demo plus the 3-minute task "your name on two lines / first and last name separated by a tab". Minutes come from the lesson's own cut-first list: slide 18 steps 5-6 (5 min) move to homework. | 5 (net 0) |
| U1-03 | should | `m1-lesson-notes.md` section 6 slide 19; `m1-lab-brief-he.md` section 6; `solutions/FirstProgram_Reference.py` | `materials-m01-1-b6cfe9.md` slide 24 (task 4, 10 min); `classwork-m01-2-98da55.md` ("משימה 4 היא משימת חובה") | The ministry's only **mandatory** task is the business card: full name, class, school, hobby, each on its own line, inside a frame of stars, with spaces between the words. The repo's exit mission is `introduce_me()` and has no frame, no star border, no mandatory flag. | Keep `introduce_me()` as the in-class exit mission. Replace the optional `draw_rocket()` bonus with the business card as a take-home or fast-finisher task and mark it "חובה" in the brief. | 0 (homework) |
| U1-04 | should | `m1-lab-brief-he.md` (9 uses of "פונקציה"), `m1-lesson-notes.md` section 4, deck slides 8-17 | `materials-m04-1-8172ae.md` slides 5-8 ("פעולה בפייתון ... נקראת גם מתודה או פונקציה"; "הגדרת פעולה", "זימון פעולה") | Ministry word: **פעולה** (define = הגדרה, call = זימון, matches the repo). Repo word: **פונקציה**. PDF Ch.1 goal 6 uses "פונקציה", so the exam text can use either. | At first use write "פונקציה (פעולה)" on the definition slide and in the brief; keep the English `def`. Patch deck slide 10 or 12 (the definition vocabulary slide) at the next deck rebuild. | 1 |
| U1-05 | should | `m1-lesson-notes.md` slides 14-17 (inside/outside, dragon); Unit 8 note `units/u8-functions-parameters/teacher/L01-why-functions-notes.md` line 100 | `materials-m04-1-8172ae.md` slides 7-8 ("the call must be below the definition ... what happens if we call first?") | The ministry shows at the first function lesson that a call placed before the `def` fails. The repo's dragon story keeps definition before call and leaves the `NameError` for 8.1. | Add one predict question to slide 16 ("move the call above the `def`: what happens?") and show `NameError`. | 3 (from the slide-6 bonus, 2, plus 1 from the buffer) |
| U1-06 | nice | `m1-lesson-notes.md` section 5, slide 3 | `materials-m01-1-b6cfe9.md` slide 22 (block comment with triple quotes); `materials-m19-2-5389b6.md` (formula sheet writes strings with single quotes, `print ('your output!')`) | Repo teaches only `#` comments and only double-quoted strings. The ministry shows `'''` block comments (the slide text is partly garbled in the extract, so the exact form is unverified) and the exam sheet writes single quotes. | One sentence each on slide 3 and slide 6: "single or double quotes both work"; "triple quotes for a longer comment". | 1 |
| U1-07 | nice | `m1-lesson-notes.md` section 1, last paragraph | n/a (repo-internal) | The text says compound output is an "open gap in the course map", while `unit-strategy.md` marks it done in Unit 3.1 and `course-map.md` lists no open gaps. | Delete the stale paragraph or change it to "covered in 3.1". | 0 |
| U1-08 | nice | `unit-strategy.md`, `m1-lab-brief-he.md` title vs `README.md`, `course-map.md` | `materials-m01-1-b6cfe9.md` slide 1 title "מבוא לאלגוריתמיקה ולשפת פייתון" | Same unit has three names: "מבוא לאלגוריתמיקה" (brief), "My First Program" (README), "Introduction to Python" (course map). Brief title promises content the lesson did not teach until U1-01 is fixed. | Align after U1-01 (the ministry title fits once the algorithm sentence exists). | 0 |
| U1-09 | nice | all `m*-slides-he.pdf` in units 0-3 | n/a | Image-only decks, no searchable text; the repo cannot be grepped for terminology and the notes are the only text record. | Optionally keep a `m*-slides-he.txt` sidecar next to each deck (the scratchpad already holds OCR-style text files for Units 6, 8, 9). | 0 |
| U1-10 | nice | `solutions/`, `exercises/` | n/a | `exercises/` has one file (`Rocket_Starter.py`, a backup), `solutions/` has two (`Rocket_Reference.py`, `FirstProgram_Reference.py`); the exit mission has no starter. Described correctly in `README.md`; the pair is uneven by design. | None; mention "no starter for the exit mission" in README to avoid confusion. | 0 |

## Things the repo uses before the ministry introduces them (item 4)

- `def` and calls in meeting 1 (ministry: meeting 4, after variables and input). Required by the PDF (Ch.1 goal 6), so keep.
- Python error names `NameError`, `SyntaxError`, `IndentationError` in 1.1 (ministry meeting 1 does not name any error).
- Unit 0 `EnvironmentCheck.py`: `sys`, `try/except` (never in the ministry course).

## Time budget (item 5)

Unit 0 is outside the 60 h; its 90 min stay at 90. Unit 1 stays 90 min (45 theory / 45 practice, `course-map.md`). The additions above total 12 minutes of content, funded by: slide 18 steps 5-6 (5), slide 6 bonus (2), the 1-min definition inside slide 2's time, and homework. No proposal needs more than the lab's existing buffer.

## Page citations and consistency checks (item 6)

- `unit-strategy.md` cites `python-a.pdf` p.6 for Unit 1 and Chapter 1; verified: Chapter 1 and its hours table are on PDF page 6 (footer 6).
- Slide counts in `README.md` and `course-map.md` (Unit 0: 12, Unit 1: 20) match the PDFs (`pdfinfo`).
- Unit 1 notes: both 45-minute tables sum to 45 (checked line by line).
- No unit-level file in `units/u0*` or `units/u1*` links to `docs/ministry-program/`; the README rule says the program is the content authority. Add a "Ministry source" line to both `unit-strategy.md` files.

## Ministry exercises to adopt

| Ministry item | File and place | Adopt as | Mandatory? | Minutes |
|---|---|---|---|---:|
| Business card: name, class, school, hobby, star frame, spaces | `classwork-m01-2-98da55.md` task 4; `materials-m01-1-b6cfe9.md` slide 24 | Take-home / fast-finisher for 1.1 (see U1-03) | חובה (the only one marked) | 0 in class |
| Name on two lines with `\n` | slide 18, task 2 | 3-min task after the `\n` demo | no mark | 3 |
| First and last name separated by `\t` | slide 20, task 3 | same | no mark | 2 |
| Algorithm as written steps: chocolate sandwich, square, rectangle | slides 5-11 (shared board) | 5-min unplugged opener in 1.1, or reuse as the 2.1 human-turtle hook | no mark | 0-5 |
| Expectations question | `classwork-m00-3-e8380d.md` question 2 | Optional exit-check sentence in Unit 0 | no mark | 2 |

No exam-style (מפמ"ר) questions exist in the meeting 0 or 1 materials; none were found by searching the extracts for these two meetings.

## Ministry source defects found (do not copy)

- `materials-m01-1-b6cfe9.md` slides 15, 17, 19, 21, 22 carry the label "כניסקראץ'" ("in Scratch") on Python slides, and `materials-m00-1-7969dd.md` slides 4-11 say "כניסה והרשמה לסביבת סקראץ'": leftovers from the Scratch course.
- Slide 19 states a tab equals five spaces (incorrect).
- Slide 17 and 19 show `print("\n")` / `print("\t")` as a "command"; they are only escape sequences inside a string.
