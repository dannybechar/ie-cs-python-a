# Audit: Unit 3 (variables, input/output, arithmetic) and ministry exam-prep meeting 17

Audited 2026-11-13. Repo: `units/u3-variables-io-arithmetic` (`unit-strategy.md`, `README.md`, `m1-lesson-notes.md`, `m2-lesson-notes.md`, both lab briefs, both lab sheets and key, `exercises/`, `solutions/`, two decks). Ministry sources: folder meeting 2 (`extracts/materials-m02-1-11fbda.md`, `classwork-m02-2-aaf70a.md`, `classwork-m02-3-1d5f67.md`), meeting 3 (`materials-m03-1-abe48a.md`, teacher copy `materials-m03-0-e4efc2.md`, `classwork-m03-2-784e0e.md`, `classwork-m03-3-6805c6.md`), meeting 4 (`materials-m04-1-8172ae.md`, only the `def`/call part), meeting 5 (`materials-m05-1-1d21fa.md`, `classwork-m05-2-8a08ce.md`, `classwork-m05-4-bf00c5.md`), meeting 6 (`materials-m06-1-462ca0.md`, `classwork-m06-2-3916b6.md`, `classwork-m06-4-705ec5.md`), meeting 17 (`materials-m17-1-fe65ee.md`, `classwork-m17-2-baa948.md`, `classwork-m17-3-48c5d5.md`), the formula sheet (`materials-m19-2-5389b6.md`) and the teacher notes (`materials-misc-7fa1b5.md`). Hours authority: `docs/ministry-source/python-a.pdf` Chapter 3 (p.8).

## Verdict

1. Unit 3 covers the ministry's meetings 2 and 3 well (variables, types, `type()`, `input`, `int`/`float` conversion, friendly output, trace tables, a variable driving the turtle). The structure and every minute table in both notes add up to 90.
2. The ministry spends **four meetings** (2, 3, 5, 6) on this material; the PDF gives Unit 3 only 4 hours = 180 minutes. The biggest content gaps are **modulo as a topic (digit extraction `//10`, `%10` appears nowhere in the repo)**, **swap with a temporary variable and self-update `x = x + 1`**, the operator `**`, multiple assignment, and the formula-sheet items `math`, `str()`, `abs`, `max`, `min`.
3. Meeting 17 (exam prep) has no home in the repo. Its trace and boolean exercises mostly fit Units 3 and 4 as warm-ups or homework; its fifth exercise needs an **`elif` chain with nesting**, which the repo explicitly does not teach (`units/u4-conditional-execution/unit-strategy.md`). That is the one item I would call blocking for exam readiness, and the decision belongs to the Unit 4 audit.
4. Time: 3.1 and 3.2 have no free minutes. About 27 minutes of proposed content: 17 fit in class by 17 minutes of trims and the removal of one duplicate (the 3.2 Turtle bridge); the other 10 (digit split, formula-sheet tour) go to a take-home pack (like the Unit 2 extras) or Unit 4 warm-ups. The protected Packing Calculator is never touched.
5. Terminology: the repo omits the formal operator names ("מנה שלמה / חילוק שלמים", "מודולו") and the word "פלט ידידותי" in the Hebrew sheets; the ministry says "פעולה" where the repo says "פונקציה"; "float" is "עשרוני" (repo, PDF) but "מספר ממשי" in the ministry table.

Coverage note: the two decks have no text layer (22 pages each, matches `README.md`); the lab-sheet PDFs extract in a scrambled right-to-left order, so I audited them by their code and by `u3-lab-sheets-key-he.pdf` code lines, not by Hebrew text. Not read: H5P and "Master Python" items (links only), 6.4 exercises 1, 2 and 5 (tables lost in extraction), 17.2/17.3 trace exercises #1-#3 (code was in images).

## Findings

| id | severity | repo location | ministry source | what differs | proposed fix | est. min |
|---|---|---|---|---|---|---:|
| U3-01 | should | `m2-lesson-notes.md` 20-36 min and 79-87 (packs only); `m2-lab-brief-he.md` helper table; grep of all `units/` finds no `// 10` or `% 10` | `materials-m06-1-462ca0.md` slides 4-9 (rowers and boats 16/19 with 4 seats), 14-17 (presents for 5 children), 18-21 (`% 2`: even/odd), 22-25 (`57//10` = tens digit, `57%10` = units digit; three-digit discussion `num//10%10` against `num%100//10`), 29-32 (flowers, library shelves, bus seats), 34-35 (clock enrichment); `classwork-m06-4-705ec5.md` exercises 3-6; teacher note in `materials-misc-7fa1b5.md` ("very important: exercise 6, splitting a number into digits, run it step by step") | The ministry gives modulo a whole meeting; the repo has one concrete model (17 stickers, 5 per pack) and one task. Digit extraction, the standard exam pattern (it returns in meeting 13, digit sum), is absent; `% 2` appears only later in 4.2. | Add a two-digit digit-split task (units, tens, sum) as the 3.2 fast-finisher or in-class if time allows; add the clock/day-of-week cycle as one slide. Do not add the three-digit version in class; it goes to the take-home pack. | 7 |
| U3-02 | should | `m2-lesson-notes.md` section 5 ("exponentiation as required syntax" excluded) and 5-13 min ("Do not add exponentiation"); `m2-lab-brief-he.md` helper table has six operators | `materials-m05-1-1d21fa.md` slides 5 and 7 (`**` taught with `+ - * / //`); `classwork-m02-3-1d5f67.md` exercise 2 (`print(num1**num2)`, note "order of operations is kept"); `classwork-m03-3-6805c6.md` exercise 2 (`pi*(r**2)`); formula sheet "אופרטורים חשבוניים" lists `+ - * / ** // %` | The exam sheet and three ministry worksheets use `**`; the repo bans it and gives no precedence demo. | Add a row to the helper table, a 3-minute demo (`2**8`, `5**2`, and `2 + 3*4` against `(2 + 3)*4`, with `**` before `*`). | 3 |
| U3-03 | should | `m1-lesson-notes.md` 12-17 min (reassignment `fuel = 80; fuel = 50` only); `m2-lesson-notes.md` 13-20 (store a result); no `temp`, no `x = x + 1` in any unit before 5.1 (`u5-loops/m1-lab-brief-he.md` line 23 is the first) | `materials-m05-1-1d21fa.md` slides 18-20 (trace table with a `temp` column: swap `num1`, `num2`), 16-17 ("same or different": `total = total + num1`); `classwork-m05-4-bf00c5.md` exercise 4 (swap, four input pairs), 9, 10; `materials-m17-1-fe65ee.md` slides 4-6 (`num1 = num2`, `num2 = num1`; `counter = counter + 1`); `links.md` (YouTube "tracing variables, swap", guided practice 2.4) | Two core ideas are missing: a value can be copied through a third variable, and a variable can be updated from itself (`x = x + 1`, right side first). Both are exam staples (17.1 exercises 2 and 3). The ministry plants the right-side-first model through swap before loops. | Add the swap trace (5 minutes: predict `num1 = num2; num2 = num1`, then fix with `temp`) and one line `score = score + 1` in the existing 3.2 "store the result" trace (2 minutes). | 7 |
| U3-04 | should | `m1-lesson-notes.md` 12-17 min and 5-12 min | `materials-m02-1-11fbda.md` slides 12-13 ("השמה מרובה": several variables in one line; the 2.2 submission sheet `classwork-m02-2-aaf70a.md` lists it as its own task); `materials-m05-1-1d21fa.md` slide 17 (`num1, num2, num3, total = 10, 2, 5, 0`) | Multiple assignment is a named topic and is used in later ministry code. The repo never shows `a, b = 1, 2`. | One 2-minute example in the reassignment block, with the trace table (two columns change in one row). Note that the ministry's own task 2 ("multiple assignment") actually defines two separate variables on two lines; use the one-line form. | 2 |
| U3-05 | should | `m1-lesson-notes.md` 5-12 min (five names, legal-or-not round) | `materials-m02-1-11fbda.md` slide 8 (five naming rules; law "חוק בל יעבור" against convention "מוסכמה"; Latin letters; no special characters `! # ?`; no reserved words; meaningful name) with teacher note; `materials-misc-7fa1b5.md` ("Master Python" key: 9 legal/illegal items) | The repo shows five examples but never says "reserved word" (for example `if`, `for`), special characters, or the law/convention distinction (a program with a bad convention still runs). | Extend the round by two names (`my-fuel`, `for`) and the two Hebrew labels חוק / מוסכמה. | 2 |
| U3-06 | should | `m1-lesson-notes.md` 32-40 min (only `int(input())` and `float(input())`); `m2-lesson-notes.md` | `materials-m03-1-abe48a.md` slides 12-15 (conversion table incl. `bool(input())`: any text is `True`, empty is `False`); `materials-m17-1-fe65ee.md` slide 7 and solution slide 18 (`float(number_int)`: 34 becomes 34.0, with the exam question "what is the purpose of the code?"); formula sheet "המרה": `var = int(var)`, `var = float(var)`, `var = str(var)` | The repo only converts at the moment of input. Converting a stored variable, and `str()`, are not shown; the "purpose of the code" question type is not practised. | Add 3 minutes after the `ValueError` demo: `x = 7; y = float(x); print(y, type(y))`, then `str(5) + "!"`; add one "what is the purpose?" prompt. `bool(input())` is optional (nice). | 3 |
| U3-07 | should | `m2-lesson-notes.md` section 2 "Source interpretation - `math`" and decision 8 | PDF Ch.3 goal 4 ("basic calculations using the `math` library on input values"); formula sheet "פעולות שימושיות מתוך ספריות": `import math`, `abs`, `max`, `min`, `math.sqrt`, plus `random` | The repo decided not to teach `math` because no function was named. The ministry lessons (meetings 2-6) do not teach it either, but the exam sheet does list `abs`, `max`, `min`, `math.sqrt`, so the stated reason ("if later materials specify functions, insert") is now answered. | Do not add a lesson. Add a 3-minute "formula sheet tour" at the end of 3.2 or in exam prep: `import math`, `math.sqrt(16)`, `abs(-3)`, `max(3, 9)`; update the note in section 2. | 3 |
| U3-08 | should | `m2-lab-brief-he.md` helper table, `m1-lab-brief-he.md`, `m2-lesson-notes.md` section 6; decks | `materials-m05-1-1d21fa.md` slide 5 (names: "חילוק", "חלוקת שלמים", "חזקה"); `materials-m06-1-462ca0.md` slides 9-10, 37-38 ("מנה שלמה", "שארית החלוקה", "מודולו"); PDF overview p.3 ("אופרטור מנה (//) ושארית חלוקה (%)") | Repo names: "כמה קבוצות שלמות" for `//`, "שארית" for `%`. The formal names the exam uses ("מנה שלמה"/"חלוקת שלמים", "שארית חלוקה"/"מודולו") never appear. | Add the formal names in brackets in the helper table and on the `//` and `%` slides (deck patch at next rebuild). | 0 |
| U3-09 | nice | Hebrew briefs and sheets | `materials-m02-1-11fbda.md` slides 9, 14-16 and `materials-m03-1-abe48a.md`: "פקודת השמה", "הצבה", "פקודת קלט", "המרת משתנים", "פקודת טיפוס משתנה", types "מספר שלם / מספר ממשי / מחרוזת / בוליאני"; `materials-m17-1-fe65ee.md` solution: "מספר עשרוני" | The repo's float name is "עשרוני" (also the PDF's word); the ministry table says "ממשי" but its own 17.1 solution says "עשרוני". "טבלת מעקב" is used by both (repo: `m1-lab-brief-he.md` line 5 only; the notes use English "trace table"). Friendly/intermediate output ("פלט ידידותי / פלט ביניים") are PDF concepts used only in English in the notes. | Write "עשרוני (ממשי)" once; put "טבלת מעקב", "פלט ידידותי", "פלט ביניים" on the slides. | 0 |
| U3-10 | nice | `m1-lesson-notes.md` 25-32 min (friendly output) | `materials-m03-1-abe48a.md` slides 7-8 and worksheet `classwork-m03-3-6805c6.md` exercise 1 (`print(num, end=" ")`, trace table with an output column) | `end=` is first used in 5.4. The ministry teaches it in meeting 3 and tests it in the worksheet. | Mention `end=" "` in 3.1 friendly output only if time allows; otherwise move to 5.1. | 2 |
| U3-11 | nice | `m2-lesson-notes.md` first and second 45 min | `materials-m05-1-1d21fa.md` slides 8-15 (every task written as `def ...():` and a call; teacher note: "students solve with a function that takes no parameters and prints") | 3.1 follows "one function per task"; 3.2 and `Packing_Reference.py` are flat scripts. Inconsistent inside the unit; the ministry style is functions. | Wrap the packing calculator in `def packing():` (and the starter likewise); 0 extra minutes. | 0 |
| U3-12 | nice | `m1-lesson-notes.md` 72-82 and `m2-lesson-notes.md` 41-44 | n/a (repo-internal) | Duplicate: 3.1 Task 3 (`side` drives the square) and the 3.2 "Bridge Back to Turtle" show the same idea twice. | Delete the 3.2 bridge (3 minutes); keep 3.1 Task 3. | -3 |
| U3-13 | nice | `exercises/` and `solutions/`, `README.md` | n/a (repo-internal) | Pairs are uneven: `Variables_Starter.py` is only the rover warm-up, `Variables_Reference.py` holds the three function tasks (no starters) and not the warm-up; `Arithmetic_Starter.py` (four operators) has no reference; `Packing_Reference.py` has no starter. The lab sheets (`m1-lab-sheet-he.pdf`, `m2-lab-sheet-he.pdf`) contain extra questions not in the notes' timelines (for example the `a + b` on two input strings giving 125 on sheet 2, which previews string `+` taught in 6.2; ministry slide 17 of meeting 2 shows the same `num2 + num2`). | Either add `Packing_Starter.py` and `Arithmetic_Reference.py`, or state the pairing in `README.md`; add the sheet questions to the minute plan. | 0 |
| U3-14 | nice | `unit-strategy.md`, `m1-lesson-notes.md` section 2 | n/a | Page citations verified: Chapter 3 with its hours table is on PDF page 8. `unit-strategy.md` says "p.8" for the table: correct. The overview is p.3-5: correct. | None. | 0 |

## Unit 3 time ledger (item 5)

Official: 4 hours = 180 min (45 theory / 135 practice); repo: 90 + 90. Both meeting timelines sum to exactly 45 + 45 (checked line by line).

| Change | Meeting | + min | Funded by (- min) |
|---|---|---:|---|
| U3-04 multiple assignment, U3-05 two extra names | 3.1 | 4 | card sort 7 to 5 cards (2), types detective 4th question dropped to the sheet (2) |
| U3-06 casting stored variables, `str()`, "purpose" | 3.1 | 3 | "document and save" 4 to 2 (2), exit-check overlap with the trace (1) |
| U3-12 delete the Turtle bridge | 3.2 | -3 | frees 3 |
| U3-02 `**` and precedence | 3.2 | 3 | the 3 minutes above |
| U3-03 swap and self-update | 3.2 | 7 | open/read/predict 9 to 6 (3), "change inputs" and "make interactive" merged 12 to 8 (4) |
| U3-01 digit split task | 3.2 | 7 | does **not** fit; moves to the take-home pack or a Unit 4 warm-up (4.1 or 4.2, 7 minutes) |
| U3-07 formula-sheet tour | exam prep | 3 | does not fit in Unit 3; exam-prep recap |

Rule: the Packing Calculator (79-87 min in 3.2) and the 3.1 trace tables stay untouched. Items that do not fit go to a "Unit 3 extra practice" pack of ten exercises built from the ministry worksheets, the same device as the ten Unit 2 extras (zero class minutes).

## Constructs: repo against ministry (item 1)

| Construct | Ministry meeting | Repo | Status |
|---|---|---|---|
| variable, assignment, naming | 2 | 3.1 | covered; reserved words and law/convention missing (U3-05) |
| multiple assignment | 2 | none | gap (U3-04) |
| types int/float/str/bool, `type()` | 2 | 3.1 | covered |
| `print` with commas | 2 | 3.1 | covered |
| `input`, `int(input())`, `float(input())` | 3 | 3.1 | covered; `bool(...)`, `str(...)`, conversion of a stored variable missing (U3-06) |
| `end=" "` | 3 | 5.4 | later (U3-10) |
| `+ - * /` | 5 | 3.2 | covered |
| `**` | 5 | none | gap (U3-02) |
| `//` and `%` | 5 and 6 | 3.2 (one model) | partial (U3-01) |
| swap with `temp`, tracing table with a `temp` column | 5 | none | gap (U3-03) |
| tracing table | 5 (named "טבלת מעקב": one column per variable plus an output column, first row = names) | 3.1 and 3.2 (same layout) | covered |
| shorthand assignment (`+= -= *= /= //= %= **=`) | 5, labelled "enrichment"; also on the formula sheet | none; `+=` banned through Unit 7 | decision needed (below) |
| relational operators, `print(a == b)` | 5 (slides 28-32) | 4.1 | later (fine) |
| functions around tasks | 4 and on | 3.1 per task; 3.2 flat | inconsistent (U3-11) |

Shorthand assignment: the ministry labels it enrichment, the formula sheet lists it, and the ministry loop meetings use `+=` (counts in `classwork-m13-4`, `materials-m12-1`, `materials-m16-1`). The repo bans `+=` in Units 6 and 7 notes (a deliberate choice recorded in the raw-deck conversion rule). Recommendation: keep writing `total = total + x` in lessons, but add a 3-minute "read-only" slide (`x += 2` means `x = x + 2`) at the end of 5.1 so the exam notation is recognised; record this as an approved deviation. Not part of Unit 3 minutes.

## Things the repo uses before the ministry introduces them (item 4)

- `import turtle` and `turtle.forward(side)` inside Unit 3 tasks (ministry: turtle at meeting 11, after conditions).
- `ValueError` shown on purpose (the ministry says "assume the input is valid" on 3.3 and slide 16 of 3.1).
- `float`/`int` printed by `type(age)` inside the same `print` (aligned with ministry slide 16 of meeting 2).

## Meeting 17 (exam prep) against the repo

Source: `materials-m17-1-fe65ee.md` (deck title "משתנים ותנאים", the file name and `traceability.md` say "משתנים ואופרטורים"; the deck's own topic list (slide 3) and closing slide (13) say variables, operators and **conditions**). The unit is "one lesson" with no stated minutes. Format: solve on paper without running, then show student solutions, then the teacher's solution (slides 14-19).

| Ministry exercise | What it tests | Repo coverage | Where it fits | Min |
|---|---|---|---|---:|
| 17.1 #1 trace `num1 = 5; num2 = num1 + 1; num1 = num2` (output 6, 6) | reassignment trace | 3.1 trace tables | 3.2 trace challenge or exit check | 3 |
| #2 `num1 = 3; num2 = 10; num1 = num2; num2 = num1` (output 10, 10) | assignment direction, the swap trap | none (U3-03) | the swap block in 3.2 | 3 |
| #3 `counter = 0; print(counter == 5); counter = counter + 1; print("Hello!")` | boolean print, self-update | `==` in 4.1; `x = x + 1` first in 5.1 (U3-03) | add to 4.1 warm-up after U3-03 | 3 |
| #4 `float(int(input()))` with input 34, "what is the purpose of the code?" | conversion, purpose question | partial (U3-06) | 3.1 conversion block | 3 |
| #5 and 17.3 #5 gift chain: `if / elif amount < 400: if ... elif ... else / elif ... else` plus match-the-ranges table | nested `if` inside an `elif` chain, boundaries | **none: the repo does not teach `elif`** (`unit-strategy.md` of Unit 4: "elif is not in the official concept list"); nesting is taught one level only | Unit 4.3 checkpoint, **requires teaching `elif`** (see below) | 15 |
| 17.3 #4 five Boolean expressions for `a = 10, b = 15, c = 0` mixing `%`, `//`, `and`, `or`, parentheses, `!=` | precedence and operator reading | 4.1 covers `and`/`or` and precedence; `//` and `%` inside conditions only in 4.2 even/odd | 4.1 lab or 4.3 checkpoint | 7 |
| 17.2/17.3 trace #1-#3 | tracing | code not in the extracts (images) | n/a | n/a |

Findings from this section:

| id | severity | repo location | ministry source | what differs | proposed fix | est. min |
|---|---|---|---|---|---|---:|
| U3-15 | blocking (fix lives in Unit 4) | `units/u4-conditional-execution/unit-strategy.md` "Scope decisions" (`elif` optional, `not` not taught); `traceability.md` rows 8-9 | `materials-m17-1-fe65ee.md` slides 9-11 and 15-19 and `classwork-m17-3-48c5d5.md` exercise 5: both exam-prep exercises on conditions are `elif` chains with a nested `if`; teacher doc `materials-misc-7fa1b5.md` (meeting 9 is "תנאי מקונן", meeting 14 task 7 asks for "תנאי מתגלגל"); formula sheet (`if / elif / else` template) | The ministry's own exam-prep material and formula sheet use `elif`; the repo cannot do these exercises. The PDF Ch.4 text lists nesting at one level and Boolean connectives and does not name `elif`; the ministry decides content. | In the Unit 4 audit: teach `elif` (about 10 minutes in 4.2, as the third form of `if`) and use 17.1 #5 as the 4.3 checkpoint; or record `elif` as a deviation with the exam risk stated. | 10-15 (Unit 4) |
| U3-16 | should | no repo file | `materials-m17-1-fe65ee.md` slides 4-7 and `classwork-m17-2-baa948.md`, `classwork-m17-3-48c5d5.md` | The repo has no exam-style practice sheet: no "trace without running", no "what is the purpose of the code", no "fill the table for these inputs". | Build one A4 exam-style tracing sheet from 17.1 #1-#4 and 17.3 #4 for the Unit 3 close (homework) and keep #5 for Unit 4. | 0 in class |
| U3-17 | should | `traceability.md` row 17 | meeting 17 deck slides 1, 3, 13 | Row 17 says "variables and operators"; the deck covers variables, operators and conditions, and its "next lesson" is conditions and loops (meeting 18). | Correct the row text. | 0 |

## Ministry exercises to adopt (with source)

The ministry marks nothing mandatory or optional in the Unit 3 area except "enrichment" (העשרה) on shorthand assignment (meeting 5 slides 21-24, "5 on 5" challenge marked "אתגר") and the clock slides of meeting 6 (slides 34-35, marked "העשרה"). Everything else is practice; all submissions are by link or screenshot. Adopt as follows.

| Ministry item | File and place | Adopt as | Min |
|---|---|---|---:|
| Interview program: five questions, then print all answers | `materials-m03-1-abe48a.md` slides 18-19 (task 4, 15 min) | optional replacement for the 3.1 "types detective" if the class is strong; otherwise the take-home pack | 0 |
| Four variables: name, surname, age (`int`), height (`float`) | slide 16 (task 3); note on privacy ("avoid publishing personal details") | already covered by `types_detective()`; add the privacy sentence | 1 |
| Match code to output (6 snippets, order of operations, string `+`) | `classwork-m02-3-1d5f67.md` exercise 2 | 3.1 warm-up or take-home | 5 |
| Reassignment trace `num1 = 8; num2 = 2; ...` | exercise 10 | 3.1/3.2 trace extra | 4 |
| Predict outputs of `/`, `//`, `**`, `"sponge " + "bob"`, `type(...)` of `34.5 // 10` (a float) | `classwork-m05-4-bf00c5.md` exercise 1 | 3.2 warm-up table | 5 |
| Swap with four input pairs (trace table) | exercise 4 | the swap block (U3-03) | 5 |
| Price and quantity word problems (phone plan, avatars, printing, bakery, surprises) | exercises 2, 3, 5, 6, 7, 8 | take-home pack | 0 |
| Pizza orders; "third magic" (x2, x5, divide by the number, minus 7 gives 3, with a trace table); "5 on 5" | `materials-m05-1-1d21fa.md` slides 14-15, 25-26, 23-24 | fast-finisher in 3.2 (the magic task is a good trace) | 0 |
| Same or different: `(n1+n2)//n3` against `(n1+n2)/n3`; accumulate against one expression | slides 16-17 | 3.2 predict slide | 3 |
| Circle perimeter and area; triangle and square perimeter | `classwork-m03-3-6805c6.md` exercise 2 | take-home | 0 |
| Rowers and boats; presents; digit extraction; flowers; shelves; buses | `materials-m06-1-462ca0.md` slides 4-9, 14-17, 22-25, 29-32 | digit split in the take-home pack (U3-01) | 7 |
| Remainder matching table; `20//6 + 14%7` style expressions | `classwork-m06-4-705ec5.md` exercises 3, 4 | take-home | 0 |
| Exam-style tracing and Boolean table | meeting 17 (above) | U3-16 | 0 |

## Ministry source defects found (do not copy)

- `materials-m05-1-1d21fa.md` slide 9 solution prints `mod` but defines `mod1` (NameError); slides 9 and 12 name variables `sum` and `pow`, which hide built-ins; slide 26 prints `3.0`, not `3`, because `/` returns a float, while the slide says the result is 3; slide 15 menu prints a bottle at 10 but the code charges 13.
- `classwork-m02-3-1d5f67.md` exercise 3 contains `pint(` for `print(`; `classwork-m03-3-6805c6.md` exercises 7 and 8 collect a passport number and a credit-card number (use invented data).
- `classwork-m05-4-bf00c5.md` exercise 10 wraps `input` text in `int("...")`, which raises `ValueError`; exercise 3 has `def ex3()` with no colon.
- `materials-m17-1-fe65ee.md` slide 11: five gifts are listed but the range table has four rows; amounts 101-249 get the stationery gift with no matching row. `classwork-m17-3-48c5d5.md` exercise 4 writes `a > = c` and "Flase".
- `materials-m03-1-abe48a.md` slide 15 (`bool(input())`) states only "any value is read as True; with no input the result is False". Correct, but it needs one explicit example that a typed "False" still converts to `True` (non-empty text); the extract does not show the result table row by row, so I did not verify the individual rows.
