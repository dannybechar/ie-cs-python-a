# Audit: Unit 5 (repetition and loops) and ministry exam-prep meeting 18

Audited 2026-11-13, read-only. Repo: `units/u5-loops/` (4 meetings, 360 min). Ministry: folder meetings 12 (for), 13 (while), 18 (exam prep, conditions and loops). Hours authority: `docs/ministry-source/python-a.pdf` p.4, p.11-12.

**Verdict (5 lines)**
1. Unit 5 matches the PDF: 8 h = 360 min (1 T + 6 P in "bounded and conditional" plus 1 T "why repetition"), goals 1-9 on p.11, minutes sum to 90 in every meeting; the lesson notes, briefs, starters and references agree with each other (4 starters, 4 references, 1:1).
2. BLOCKING for exam readiness: the repo bans `+=` / `-=` ("the course keeps `x = x + 1`") while the ministry teaches `+=` in every loop deck (12.1 #7, #10; 13.1) and the exam items use it (13.4 Q4, 18.1 #6, #10); the exam formula sheet lists `+= -= *= /= **= //= %=`.
3. SHOULD: `print(..., end="")` appears only in 5.4 (ministry: first `for` meeting, used in all exam items); no `if`/`%` inside a `for` before 5.4 (7-boom, 18.1 #4-#7); no finite/infinite classification and no for/while equivalence tasks (13.3, 13.4, 18.1 #9); no digit loops (digit sum 13.5, 18.1 #11-#12, 18.3 #3); the repo's "rolling repeated execution" (value carried between rounds) is an inference, while the folder uses "מתגלגל" for the `elif` chain.
4. Meeting 18: there is no repo exam-prep slot and no spare minutes (2,700 min fully allocated, meeting 31 lands on May 30). Cover it by turning the 4.3 and 5.4 checkpoints B into 18.1-style written items and assigning 18.1/18.2 as homework; five items are not answerable from the repo today (list below). Three ministry solutions contain errors (verified by running them): do not copy them.
5. Time: ministry estimates about 5 h of class time for the `for` meeting alone (12.1 speaker notes: 4 teaching sessions of 15-20 min, 2.5-3 h of exercises, about 1.5 h interactive) and 2-3 double lessons for `while`; the repo has 360 min for everything. About 44 min of additions are proposed with named cuts; nested loops (5.4) are repo-only and are the main source of room.

Method note: decks `m1-4-slides-he.pdf` are image-only (NotebookLM). I read lesson notes and briefs in full and sampled decks as contact sheets (5.2 slides 20-25, 5.4 slides 7-12); they match the notes. Image-only ministry decks were read from `extracts/ocr-m12-3.md`, `ocr-m12-5.md`, `ocr-m13-3.md`, `ocr-m13-5.md` (all present). Caveats: `ocr-m13-3.md` slide 3 is cut off after row 4 (the source image is cropped); 13.5 is only "part A" (no part B in the import); 13.1 speaker notes mention bonus exercises 8-10 that are not in the extracted deck: not invented here.

## Findings: Unit 5

| id | sev | repo location | ministry source | what differs | proposed fix | min |
|---|---|---|---|---|---|---:|
| U5-01 | blocking | `unit-strategy.md` "Scope decisions" (`+=`/`-=` not used); `m1`/`m3`/`m4-lesson-notes.md` "No `+=`"; also `u7` 7.2 and 5.1-5.4 "Source of inspiration" lines ("`+=` replaced by `x = x + 1`") | `materials-m12-1-028c50.md` slides 25 (`total += i`), 32-34 (`total += num`); `materials-m13-1-bcc65c.md` slides 7 and 9 (`i += 1`, `n += 2`); `classwork-m13-4-acd0a1.md` Q3-Q4 (`i += 1`, `x -= 1`); `materials-m18-1-88ee0a.md` ex #6, #10 (slides 20, 24); `materials-m19-2-5389b6.md` (formula sheet augmented operators) | The ministry teaches and tests `+=`/`-=`; exam questions will contain it. The repo bans it in Units 5 and 7. PDF p.3 lists no such operator, so this is a content-authority deviation not yet approved | Keep `x = x + 1` as the main form but teach `+=` / `-=` as "same thing, shorter" in 5.1 (3 min, at the running total, trace both lines) and use it in 5.3 (2 min). Students must read it, not necessarily write it. Update the "No `+=`" lines in 5.1, 5.3, 5.4 and `u7` notes. Cross-unit: flag for the U6/U7 audits | 5 |
| U5-02 | should | `unit-strategy.md` "Nested loops and `print(..., end="")` appear in 5.4 only"; `m4-lesson-notes.md`; `Ranges_Reference.py` `sequences()` prints one number per line | `materials-m12-1` slides 15-20 (the `end` attribute taught in the first `for` meeting; "stars in one line", "numbers with commas"), slides 28, 30, 37 (`end=","`); `classwork-m12-7-6bdc55.md` Q1 (`end = " "` in items 1 and 3 of 13); `materials-m18-1` ex #8, #10, #12 | Ministry teaches `end` at the start of loops and every exam item uses it; repo shows it in the last meeting only, for star patterns. Ministry calls it "תכונה" (attribute), not a command (12.1 slide 16 notes); the 5.4 brief says "הפרמטר" | Move a 5-min `end=" "` / `end=","` demo into 5.2 (print a range on one line, 12.1 slides 15-20) and keep the star pattern in 5.4. Fund by shortening the 5.2 star challenge (8 -> 4) and 5.2 spiral (13 -> 12). Use "תכונה" next to "פרמטר" | 5 |
| U5-03 | should | 5.1-5.3 (no `if` inside a `for`); first `if` in a loop is `count_scores()` (while) in 5.4 Checkpoint A2 | `materials-m12-1` slides 38-42 (7-boom; "same or different?" `for`+`if %` vs `range` with step); `classwork-m12-7` Q1 #6, #9, Q2; `ocr-m12-3.md` slides 2-4 (if/elif ranges inside a `for`); `materials-m18-1` ex #4, #5, #7, #10(ב) | The ministry combines `for` with `if` and `%` from the first meeting and the exam repeats it (filter by remainder, count matches). Repo students meet `for` + `if` only at the checkpoint | Add a 8-min guided item to 5.2: slides 40-42 ("print the multiples of 3 up to 16: `for`+`if %` vs `range(0, 17, 3)`: same output?") then a one-line 7-boom variant. Use `number // 10 == 7` (the ministry solution is wrong, see Defects). Fund: 5.2 polygon task 16 -> 12 and star challenge (above) | 8 |
| U5-04 | should | none; no `% 10` / `// 10` loop in Units 3-5 | `ocr-m13-5.md` slides 1-3 (sum of digits with `while`, part A, "return"); `materials-m18-1` ex #11-#12; `classwork-m18-3-875584.md` #3 (reverse number); `classwork-m07-3` Ex 4 | Digit-peeling loops (`while n > 0: d = n % 10; n = n // 10`) are the ministry's standard `while` example and appear in the exam-prep items. Repo has no preparation (and U3 has only packs/remainder, see U4-04) | After U4-04 is in place: add `digit_sum()` as the 5.3 challenge (8 min) replacing nothing mandatory: shorten the 5.3 password task 10 -> 8 and rover_trips 8 -> 6; `return`-free (print the result; the ministry task says "return" but returns come in Unit 8) | 8 |
| U5-05 | should | 5.3 (endless-loop warm-up only); 5.4 CP-B Q3 (loop-type choice) | `classwork-m13-4-acd0a1.md` Q1-Q4 (finite or endless? with `i = i % 10`, `num != 10` step 3, etc.); `ocr-m13-3.md` slide 3 ("לולאות שקולות": match for/while loops with the same output); `materials-m18-1` ex #9 (match 8 loops), slide 34 answer D-A-B-C; `materials-m13-1` slides 8-9, 30-34 | Ministry trains "is this loop finite? what does it print? which two loops print the same?" in 12.6, 13.3, 13.4, 18.1. Repo has neither a classification drill nor an equivalence drill (PDF p.11 goals 3 and 7 and assessment items 2-3 point to it) | Add 6 min to 5.3 guided: 3 snippets (13.1 slides 27-34) classify and fix; and 5.4 CP-B: replace Q3 by two 18.1 #9 pairs (4 min, written). Fund by cutting the 5.4 flower (see U5-07) | 6 |
| U5-06 | should | none: the repo's rolling definition `m4-lesson-notes.md` "Source interpretation", `m4-lab-brief-he.md`, `unit-strategy.md`; deck 5.4 slide 8 | `materials-m09-1-ba5939.md` slide 25 ("תנאי מתגלגל" = `elif` chain); `materials-m08-6`, `materials-m09-7`; `ocr-m12-3.md` title "לולאת for ותנאי מורכב ומתגלגל"; PDF p.4 and p.11 goal 9 ("ביצוע חוזר מתגלגל") | In the folder "מתגלגל" always means the `elif` chain (and 12.3 puts it inside a `for`). No folder text defines a "rolling loop". The repo reads goal 9 as "each round continues from the previous value" and labels it an interpretation (honest, but unsupported). The word now means two things in the course once `elif` is added | Keep the accumulation trace (cheap), but rename it "הערך מתגלגל מסבב לסבב" or keep it as "tracing", and after U4-01 add the 12.3 "Super Python" task (`for` over 10 scores, `elif` ranges, counts per type, average of one type; `ocr-m12-3.md` slides 2-4) as the main goal-9 evidence. Ask the supervisor/teacher which reading is intended before the exam | 0 |
| U5-07 | nice | 5.4 (nested loops, star patterns, `flower()`, 63 min lab) | PDF p.11-12 does not name nested loops; no nested loop in folder m12, m13, m18; `classwork-m16-3-61a733.md` only asks a true/false "no nested loops in the code" | Nested loops are repo-only (➕). They fit PDF teaching method 6 (shapes with control structures) and meeting 16 uses the term, but they cost 10 (star patterns) + 12 (flower) + 3 trace minutes that the ministry spends on `for`+`if`, counters and `while` tracing | Keep a short nesting demo (6-8 min); reduce the `flower()` to a short demo or drop it (shapes with loops stay covered by 5.2 polygon/spiral/star); frees up to about 20 min for U5-03, U5-05, U5-06 | -20 |
| U5-08 | nice | 5.1-5.3 and 5.4 loop variable names (`i`, `number`, `row`, `side`, `seconds`) | PDF p.11 teaching method 3 (`for item in range(...)`); `classwork-m12-7`, `materials-m18-1` use `item`; 13.0 speaker note: the name can be `item, index, char, word, ans` | Exam items write `item`; repo mostly uses `i` / meaning names and says "any name" in 5.1 | Add `for item in range(...)` once in 5.1 exit check or 5.2 warm-up; no extra minutes | 0 |
| U5-09 | nice | Hebrew lab briefs ("כתבו פונקציה") | ministry tasks: "כתבו פעולה"; 12.1 #5-#9 need parameters and `return` | Same terminology issue as U4-08. In addition 12.1 tasks #5-#9 (parameters, `return`) cannot be adopted verbatim before Unit 8; adapt them with `input()` | One gloss line; adapt tasks (see adopt list) | 0 |
| U5-10 | nice | 5.1-5.2 loops print each value on its own line; no tracing-table format for output | `materials-m12-1` slides 12, 20, 23 (tracing tables with columns `i`, parameters, output, plus the "מסך הרצה" screen) | Ministry draws the trace table with a variable column per variable and a cumulative output column; repo traces are already tables (OK) but have no cumulative output column | Reuse the slide 20 layout in the 5.1 running-total trace; no extra minutes | 0 |
| U5-11 | nice | counters, max, accumulator are Unit 7 (7.1, 7.2) | `classwork-m12-4-4ec331.md` Q1, Q3 (counts, total), Q4 (`count_red` with `while`); `ocr-m12-5.md` (max with class number); `ocr-m12-3.md` slide 3-4 (counts per category) | Ministry teaches counter / accumulator / max inside the `for` meeting; PDF order (Chapter 7 after 5) puts them later, so the repo order is PDF-correct but delays exam-style loops | No change in U5; make sure the 7.1/7.2 checkpoints reuse the 12.4 and 12.5 items (record in `audit-u7`). Optional: 12.4 Q4 as a `while` counter in 5.3 (6 min, in place of part of the digit challenge) | 0 |
| U5-12 | nice | `unit-strategy.md`, `m*-lesson-notes.md` citations | PDF p.3-4, p.11-12 | Verified correct: hours table on p.12 (2 + 6 h, 1 + 7 h), goals on p.11, Turtle row on p.4 ("הוראת ביצוע חוזר באמצעות Turtle"). The README minutes (45 + 315 = 360) and slide counts (20/17/20/18) match. No citation errors in Unit 5 | None | 0 |

Checked and fine: 5.4 Checkpoint B answers (`**|` x3 and 6 stars; `range(10, 0, -3)` gives 10, 7, 4, 1; rolling 6, 12, 24); 5.2 spiral end point (100, 80) facing down and the 144-degree star (checked by hand); 5.3 `rover_trips()` table (85, 70, 55, 40, 25, 10, six trips); `range` boundary starters; PDF goals 3, 4, 7, 8 (stop condition, correctness, difference, stop depending on a variable) are covered by 5.3.

## Time budget effect (inside 360 min)

| Add | min | Funded by | min |
|---|---:|---|---:|
| `+=` (5.1, 5.3) | 5 | 5.1 challenge `times_table` 10 -> 6 (it is optional); 5.3 exit check wording | 5 |
| `end` demo (5.2) | 5 | 5.2 star challenge 8 -> 4; spiral 13 -> 12 | 5 |
| `for` + `if %` (5.2) | 8 | 5.2 polygon 16 -> 12; 5.2 doc/save 3 -> 2; 5.2 countdown 8 -> 6 | 7 (+1 from exit check) |
| Classification (5.3) + equivalence (5.4 CP-B) | 6 | 5.4 flower 12 -> 4 (demo only) | 6 |
| `digit_sum()` (5.3) | 8 | 5.3 password 10 -> 8, rover_trips 8 -> 6, doc 3 -> 2 (+3 from sentinel demo) | 8 |
| Super Python (5.4) | 12 | 5.4 star patterns 10 -> 6, flower remaining 4 -> 0, nesting guided 5 min cut | 12 |
| **Total** | **44** | | **44** |

Not everything fits without cutting the flower and shortening several optional challenges. Priority order if the teacher wants less: U5-01 (5), U5-02 (5), U5-03 (8), U5-05 (6); then U5-04 and Super Python become homework (0 class min). These are teacher decisions because the lessons are approved.

## Meeting 18 (exam prep: conditions and loops)

Ministry: `materials-m18-1-88ee0a.md` (deck, 42 slides, 12 exam exercises with solutions), `classwork-m18-2-41ab22.md` (the same 12 exercises as the submission sheet, titled 19.2 inside), `classwork-m18-3-875584.md` (worksheet 2, three more exercises, titled 19.3 inside), H5P "practice #2" (`links.md` row 18.4, external, not verified), Master Python quizzes 18.5-18.7 (names only). The deck says one lesson including practice; notes say "solve on paper, no running". Slide 39 points to 19.3/19.4 and slide 40 to 18.3/18.4: source numbering is inconsistent; the folder numbers are used here.

Repo status: there is no exam-prep meeting. The only matching material is the 4.3 and 5.4 checkpoints. The year has 31 meetings needed and 26 available by end of April (`course-map.md` "Deadline and pace"), so a 90-min meeting 18 cannot be added; python-a.pdf gives no hours for exam prep.

Coverage of the 12 + 3 items by what the repo teaches today:

| Item (ministry file) | Skill | Answerable from repo now? | Gap |
|---|---|---|---|
| 18.1 #1 order two numbers, 7 programs | compare, assign, swap by arithmetic, wrong-code diagnosis | partial | swap via `a = a + b` trick not taught (Unit 3 has no swap); items א, ב, ד, ה, ו, ז are fine |
| #2 input for Yes / No | compound `and`/`or`, parentheses | partial | reverse-reasoning type (U4-06) |
| #3 evaluate with `a=10, b=15, c=0` | `%`, `//`, `and`/`or` | no | `%` and `//` inside conditions (U4-04) |
| #4, #5, #7 loop output with `if %` | `for`, `range`, step, `or`/`and` | partial | `for` + `if %` (U5-03) |
| #6 sum of odd numbers, state the purpose | accumulator, `+=` | partial | `+=` (U5-01); purpose wording is a new question type |
| #8 fill missing range arguments and while update | `range`, `while` update | partial | reverse-engineering type; `end=" "` (U5-02) |
| #9 match equivalent loops | for/while equivalence | no | U5-05 |
| #10 outputs incl. `i += 1`, `x -= 1`, `print(i, x)` after the loop | `while`, `+=`, final values | partial | `+=` (U5-01) |
| #11 perfect number | `while`, `%`, accumulator | no | divisor loop; optional, advanced |
| #12 ID digit positions | `for` + `% 10`, `// 10`, flag `found` | no | digit loop, flag pattern; optional, advanced (string variant uses Unit 6) |
| 18.3 #1 six even/odd solutions | compound, nested, `elif` | partial | needs `elif` (U4-01) |
| 18.3 #2 `range(-5, 0, 1)` output; `for ... else` | negative start, `for/else` | partial | `for ... else` is not taught anywhere in the extracts I read (m7-9, m12, m13, m18, formula sheet); do not adopt item 2b without confirming it is in scope |
| 18.3 #3 reverse number (`while`, `% 10`, `// 10`) | digit loop | no | U5-04 |

Findings for meeting 18:

| id | sev | repo location | ministry source | what differs | proposed fix | min |
|---|---|---|---|---|---|---:|
| M18-01 | should | no slot; `course-map.md`; `traceability.md` row 18 ("4.3, 5.4 checkpoints", partial) | `materials-m18-1` slides 1-3, 40-42 | The ministry has a dedicated 90-min exam-prep lesson on conditions and loops; the repo has none and no spare minutes. Hours authority (PDF) gives it zero hours | Do not add a meeting. Make 4.3 CP-B and 5.4 CP-B written, no-run, 18.1-style items (the ministry says solve on paper without running); assign 18.1 and 18.2 as homework after Unit 5 and again before the exam; record the decision in `traceability.md` section 4. If the schedule gap (`course-map.md`) later yields a free meeting, use it for 18.1 | 0 |
| M18-02 | should | 4.3 CP-B, 5.4 CP-B | `materials-m18-1` ex #2, #4, #8, #9, #10 | Repo checkpoint B items are trace-this-code only; the exam mixes five question types (trace, find input, fill the blank, match equivalent, state the purpose) | Add one item of each new type to the two CP-Bs (about 4 min each, funded in U4/U5 time tables above) | 0 |
| M18-03 | should | all of Units 4-5 | `materials-m18-1` ex #1, #3, #11, #12; `classwork-m18-3` #3 | Items needing swap, `%`/`//` in conditions and digit loops are not answerable (table above) | Do not assign those until U4-04 and U5-04 land; mark #11, #12 and 18.3 #3 as optional challenge | 0 |
| M18-04 | nice | n/a | `materials-m18-1` slide 33 (ex #8 ג); slide 37 (ex #12); `materials-m12-1` slide 39 (7-boom) | Three ministry solutions are wrong (verified by running them): see Defects | Fix before reuse | 0 |
| M18-05 | nice | n/a | `links.md` rows 18.4, 8.4, 16.4 (H5P); 18.5-18.7 Master Python (names only) | H5P/YouTube items cannot be reviewed or adopted offline; the Master Python quizzes have no text in the import | Optional links only after the teacher confirms they work | 0 |

Ministry defects found (do not copy verbatim; each reproduced by running the code):
- `materials-m18-1` slide 33 (solution 8 ג): `range (6,1,-1)` prints 6 5 4 3 2, but the required output is `6 4 2`; the exercise on slide 22 and `classwork-m12-7` Q1 #3 imply `range(6, 1, -2)`.
- `materials-m18-1` slide 37 (ex #12 `find_location`): `range(0,10)` with `print(index ...)` prints `0 2 3` for 334429969 and 9, not the stated `1 3 4`, and prints `9` for digit 0 in a 9-digit ID (a leading zero is counted). `range(1, 10)` gives `1 3 4`; the string solution on slide 38 is right.
- `materials-m12-1` slide 39 (7-boom): `number / 10 == 7` is true only for 70; 71, 72, 73, 74, 75, 76, 78, 79 are not printed (77 passes by `% 10 == 7`). Use `number // 10 == 7`.
- Minor: `classwork-m12-7` heading text describes `while` loops, but items are `for` loops; `materials-m13-1` slide 15 is marked "partial solution"; `materials-m09-1` slide 13 `nummber` typos (U4).

## Ministry exercises to adopt

Marker: חובה = in the ministry's submission list / "להגשה"; רשות = optional or bonus; exam = מפמ"ר style.

| Exercise | Ministry file and slide | Status | Where in the repo | Note |
|---|---|---|---|---|
| "Cheers" x3; loop counter 0..3 with tracing table | `materials-m12-1` slides 9-12 | חובה (12.2) | 5.1 warm-up | Repo warm-up is already similar; reuse the tracing table (slide 12) |
| Stars (one per line, then one line with `end`); numbers with commas | `materials-m12-1` slides 13-20 | חובה | 5.2 `end` demo (U5-02) | `print_star(num)` uses a parameter: adapt with `input()` |
| Sequence between two numbers; sum of a series; evens / odds 0-100 | `materials-m12-1` slides 22-30 | חובה | 5.2 tasks (adapt: no params/`return`) | Slide 25 solution uses `return`: print instead until Unit 8 |
| Average of 10 numbers, three equivalent `range` forms | `materials-m12-1` slides 31-34 | חובה | 5.1 or 5.2 homework | Good "same output" lesson for U5-05 |
| Countdown 10 to 1 with commas | `materials-m12-1` slides 36-37 | חובה | already `countdown()` in 5.2 | Add `end=","` |
| 7-boom | `materials-m12-1` slides 38-39; `classwork-m12-2-6f9e4c.md` #12 | חובה | 5.2 (U5-03) | Fix the `/ 10` bug |
| Same or different: `for`+`if %` vs `range` step | `materials-m12-1` slides 40-42 | in-class | 5.2 (U5-03) | Answers: same output |
| 13 `for` output snippets | `classwork-m12-7-6bdc55.md` Q1 | חובה (12.6) | 5.2 homework, 5.4 CP-B | #9 has a syntax glitch in the import; use cleaned copies |
| Count pairs with equal parity (fill-in) | `classwork-m12-7` Q2 | חובה | after counters (U7) or homework | |
| T-shirt counts and total; grade bonus rule; 10 students | `classwork-m12-4-4ec331.md` Q1-Q3 | חובה (12.3) | 5.4 homework (counters and two `if`s; `elif` optional) | Scale 30 to 5 students |
| Count red beads with `while` (fill-in) | `classwork-m12-4` Q4 | חובה | 5.3 (optional counter, U5-11) | |
| Super Python scores, `elif` ranges, counts, average of mushrooms | `ocr-m12-3.md` slides 2-4 | guided video 12.3 | 5.4 main task (U5-06) | Needs U4-01; ranges 90-100, 78-89, 55-77, below 55 |
| Beach cleanup: heaviest bag and its class | `ocr-m12-5.md` slide 2 | guided video 12.5 | Unit 7.2 (max) | |
| Series with `while` and `for`; descending; multiplication table | `materials-m13-1` slides 10-13; `classwork-m13-2-8204a6.md` | חובה (13.2) | 5.3 homework | Multiplication table is already 5.1 challenge |
| Average until 0 or negative (guard division by zero) | `materials-m13-1` slides 14-15 | חובה | 5.3 extra | Source solution is partial; finish with `if count > 0` |
| Names until a blank, count them; password | `materials-m13-1` slides 16-17 | חובה | password is 5.3 Task 1 | |
| Valid three-digit input with `or` | `materials-m13-1` slides 21-22 | in-class | 5.3 input-until-valid variant | |
| Exactly 3 even numbers (fill-in) | `materials-m13-1` slide 23 | חובה | 5.3 homework | Counter in `while` |
| Endless-loop fixes and predictions; counting up and down | `materials-m13-1` slides 25-34 | in-class | 5.3 (U5-05) | |
| Finite or endless? (5 + 5 snippets) and outputs | `classwork-m13-4-acd0a1.md` Q1-Q4 | חובה (13.3) | 5.3 / 5.4 CP-B (U5-05) | |
| Equivalent loops (match for with while) | `ocr-m13-3.md` slide 3; `materials-m18-1` ex #9 | guided video 13.3; exam | 5.4 CP-B (U5-05) | OCR table cut off after row 4 |
| Digit sum with `while` | `ocr-m13-5.md` slide 2 | guided video 13.5 (part A) | 5.3 challenge (U5-04) | Task says "return": print instead |
| Exam set of 12 items; second worksheet | `materials-m18-1`, `classwork-m18-2-41ab22.md`, `classwork-m18-3-875584.md` | exam / חובה (18.2, 18.3) | homework, 4.3 / 5.4 CP-B (M18-01..03) | Skip `for ... else` and the three defective solutions |
