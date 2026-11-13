# Phase 3 audit: consolidated review (for the Phase 4 gate)

Date: 2026-11-13. Detail per unit: `audit-u0-u1.md`, `audit-u2.md` … `audit-u9.md` (u5 also holds meeting 18, u6 meeting 19, u3 meeting 17). About **136 findings: 11 blocking, 76 should, 49 nice.** Nothing in `units/` has been edited. Limits: the Unit 0–9 deck PDFs are image-only, so decks were checked through the lesson notes plus ~60 sampled slides, not by text; some folder items (H5P, Master Python, a few table images) could not be read.

## What was verified by hand (not only by the audit agents)
- `python-a.pdf` p.4 lists **"משפט ביצוע מותנה מתגלגל"** (Chapter 4) and **"ביצוע חוזר מתגלגל"** (Chapter 5). So the repo statements "elif is not in the official concept list" (Unit 4 strategy, three lesson notes) and "Open coverage gaps: none" are wrong.
- `python-a.pdf` p.17 (Chapter 8): "פונקציה שאינה מחזירה ערך"; practical assessment = write a function that does not return a value. The folder (meeting 10) teaches `return`. **The two authorities conflict.**

## Decisions needed (they decide how much of Phase 5 is done)

| # | Decision | Evidence | Recommendation |
|---|---|---|---|
| D1 | `elif` / rolling condition | In the PDF and the folder and the exam formula sheet; no repo `.py` has it; 4.3 of 17.1 and 18.1 exam items need it | Adopt: ~10 min in 4.3, fix false statements in `unit-strategy.md`, lesson notes, `course-map.md` |
| D2 | `return` | PDF excludes it (p.17); folder teaches it; clarifications PDF p.3 puts it in Python B | Your call. Option: "return-lite" ~20 min inside 8.3 at zero net time, or record an approved deviation (no return) |
| D3 | Turtle notation | Repo uses module-level `turtle.forward`, `turtle.done()`; folder, formula sheet and exam question use `wn = turtle.Screen()`, `pen = turtle.Turtle()`, `wn.mainloop()` | One-off ~10 min translation drill (Unit 2, repeated in 6/9 checkpoints) plus an approved-deviation record |
| D4 | `+=` and `not` | Repo bans `+=` (Units 5, 7) and `not`; folder teaches both, exam items use them; Unit 9 code already uses `not` | Teach as shorthand (5 min and 5 min); remove the bans |
| D5 | Coordinates, `goto`, `setx/sety` | In PDF overview and folder meeting 14; Unit 2 excludes them yet the 10 extra exercises and Unit 9 use them | Add 8–10 min coordinates block to Unit 2 (taught units: addendum) |
| D6 | Modulo, digit extraction, swap, `x = x + 1`, negative indexes, string-building loops | Missing/only once in the repo, all exam staples | Add inside existing minutes (3.2, 6.1–6.3); take-home packs for the rest |
| D7 | Exam prep meetings 17–19 | No slot (meeting 31 falls on 30 May) | Convert checkpoints B to exam-style items, assign folder 17–19 worksheets as homework, give students the official formula sheet (19.2) |
| D8 | Terminology "פעולה"/"פרמטר"/`main()` vs repo "פונקציה"/"ארגומנט" | Folder and exam wording differ | One bridge line per unit |
| D9 | "מתגלגל" meaning | Repo: carry over between rounds; folder: the `elif` chain | Align with folder once D1 is adopted; ask the supervisor if unsure |
| D10 | Unit order | Repo follows the PDF (turtle first, functions in Unit 8); folder is variables → functions A → conditions → functions B → turtle | Keep the repo order (units 0–2 already taught; audit of Unit 8 shows Units 1–7 only use parameterless functions); record as approved deviation |
| D11 | Unit 9 timer/animation (9.5) | PDF requires it; absent from folder meeting 20; clarifications puts timers under Python C | Keep; compress first if May schedule is cut |

## Blocking findings (11)
U2-01 turtle notation · U2-02 coordinates/`goto` · U3-01 modulo/digit extraction · U4-01 `elif` · U5-01 `+=` · U6-01 negative indexes · U6-02 string-building loop · U6-03 exam turtle dialect · U7-01 `+=` · U7-02 `elif` in counters · U8-01 `return`.

## Ministry source defects (do NOT copy)
`char == ' . '` in 19.4 Q5; `work =+1` and `range(9)` in 16.3 Q4/Q5; `Y`/`y` mismatch on 16.1 slide 24; 18.1 ex #8ג `range(6,1,-1)` prints 6 5 4 3 2 (not 6 4 2); 18.1 ex #12 wrong `for` solution; 12.1 "7-boom" `number / 10 == 7` should be `// 10`; typos `penup(x,y)`, `mod`, `pint`.

## Repo-internal fixes (no ministry decision needed)
- Unit 4: `Shapes_Starter.py` pairs with `Conditions_Reference.py`; ScoreBug solution sits inside `Decisions_Reference.py` (uneven pairs).
- `EnvironmentCheck.py` (Unit 0) uses constructs not yet taught.
- `survey()` counts any non-`y` as `n`; Unit 9 exit-criteria sentence missing a number; Unit 9 "Python C enrichment" calls timers enrichment while 9.5 teaches them as core.
- `traceability.md` rows to correct: row 15, 20.5 ≡ 19.2 (formula sheet), meeting-number collisions.
- Add the three uncited PDFs (clarifications, exam index, lab specs) to the course-map sources.

## Time budget
Every audit proposes additions funded inside the same meeting or as homework; no meeting is added. Largest additions: Unit 5 ≈ 44 min, Unit 4 ≈ 29 min, Unit 3 ≈ 27 min (17 in-class), Unit 2 ≈ 37 min. Per-unit official minutes (course-map.md) must still match after Phase 5.
