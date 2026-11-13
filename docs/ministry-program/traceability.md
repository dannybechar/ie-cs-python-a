# Traceability: ministry Classroom program → repo meetings

Status: **preliminary** (written 2026-11-13 from the folder's lesson-component lists and a grep of the repo; every row is confirmed or corrected by the Phase 3 audits `audit-u*.md`). Folder meeting numbers are the authoritative ones (see README). Hours come from `course-map.md` (python-a.pdf), never from the folder.

Status key: ✅ covered · 🔶 partial · ❌ missing in repo · ➕ extra in repo (not in folder) · ⚖️ deviation to decide in the Phase 4 review.

## 1. Folder meeting → repo meeting

| Folder | Topic and key constructs (folder) | Repo meeting(s) | Status | Notes to verify |
|---:|---|---|---|---|
| 0 | Intro, Classroom setup, mood task; mentions the Ministry exam | 0.1 Environment Setup | 🔶 | Repo has no Classroom workflow or exam framing slide |
| 1 | Algorithm, `print`, newline, spacing, comments | 1.1 | ✅ | Folder task 4 is mandatory; repo adds first function |
| 2 | Variables: naming rules, assignment, multiple assignment, types, swap | 3.1 | ✅ | Check multiple assignment, swap, tracing of variables (video 2.4) |
| 3 | `input`, `int(input())`, conversion | 3.1, 3.2 | ✅ | |
| 4 | Functions A: `def`, call | 1.1, 8.1, 8.2 | ⚖️ | Order: folder teaches functions at meeting 4, repo at Unit 8 |
| 5 | Arithmetic operators, tracing table (טבלת מעקב) | 3.2 | 🔶 | Check tracing table format |
| 6 | `/`, `//`, `%` (modulo as remainder/clock) | 3.2, 4.2 (digits) | ✅ (Phase 5) | `//` and `%` appear in a single Unit 3 file; folder gives modulo a whole meeting plus a test |
| 7 | Simple `if`, boolean expressions | 4.1, 4.2 | ✅ | Folder 7.3 is "alternative assessment" |
| 8 | Compound condition `and`, `or`, `not` | 4.1, 4.3 | ✅ (`not` adopted, Phase 5) | Repo unit-strategy: `not` not taught (not in PDF list); folder teaches it |
| 9 | Nested `if` and `elif` chains | 4.3 | ✅ (`elif` adopted, Phase 5) | Repo: one-level nesting, `elif` optional; no `elif` in any repo code |
| 10 | Functions B: parameters, `return` | 8.1–8.4 | ✅ parameters; `return` as return-lite in 8.3 (approved deviation) | No `return` in any repo `.py`; folder teaches functions returning values |
| 11 | Turtle A: `import turtle`, `forward`, `left`, shape/color | 2.1–2.3 | ⚖️ | Repo teaches turtle first (Unit 2); folder at meeting 11 after conditions |
| 12 | `for … in range`, `print(..., end="")`, max-search pattern | 5.1, 5.2, 5.4 | ✅ | `end=` appears in only 2 repo files |
| 13 | `while`, infinite loops, equivalent loops, digit sum | 5.3, 5.4 | 🔶 | Check digit-sum and equivalent-loop tasks |
| 14 | Turtle B: axes, `goto`, `setx`, `sety` | 2.x, 9.3 | 🔶 | Check coordinate system treatment in Unit 2 |
| 15 | Strings: indexing, slicing (incl. jump), `+`, `*` | 6.1–6.3 | ✅ | |
| 16 | `random`, counter, accumulator, global variable, time loops | 7.1–7.3, 8.4 | ✅ | Folder also asks for peer review, edge cases, input validation |
| 17 | Exam prep: variables, operators and conditions (deck "משתנים ותנאים"; next lesson is conditions and loops) | none | ❌ | No dedicated exam-prep meeting; time budget is 60 h, see Phase 4 |
| 18 | Exam prep: conditions and loops | 4.3, 5.4 checkpoints | 🔶 | |
| 19 | Exam prep: strings and turtle; formula sheet (19.2/20.5) | 6.4 checkpoint | ❌ | Formula sheet (דף עזר לתלמיד, Python 3) not used anywhere in the repo |
| 20 | Mouse and keyboard events, three game worksheets | 9.1–9.6 | ✅ | |

## 2. Repo content with no folder counterpart

| Repo | Content | Status |
|---|---|---|
| 0.1 | School-added environment setup (outside the 60 h) | ➕ |
| 4.x | Truth tables | ➕ (verify against PDF) |
| 5.2, 6.4, 7.3 | Turtle polygons/spiral/star, `write`, random walk | ➕ (verify against the folder's turtle command list) |
| 9.5 | `ontimer`, animation, bounce | ➕ (folder meeting 20 covers only mouse and keyboard) |
| 9.x | Python C enrichment | ➕ optional |
| Unit tests | Unit 2 Forms A/B, written test | ➕ (folder has none) |

## 3. Cross-cutting differences (need a decision in Phase 4)

1. **Order of constructs.** Folder: variables → input → functions A → operators → modulo → conditions → functions B → turtle A → for → while → turtle B → strings → counter/random → exam prep → events. Repo (PDF order): turtle → variables/input/arithmetic → conditions → loops → strings → algorithmic patterns → functions → events. The units 0–2 are already taught turtle-first.
2. **Constructs the folder teaches that the repo does not:** modulo and floor division as a topic, `not`, `elif`, `return`, tracing tables, `print(..., end="")` as a pattern, exam-prep meetings, formula sheet.
3. **Time.** The folder has 21 × 90 min = 1,890 min (inference, no hours stated) versus the repo's 2,700 min; adding modulo, `return`, `elif`, `not` and exam prep must fit inside the existing per-unit minutes.
4. **Exercises and assessment.** Folder items (submission sheets, worksheets, H5P, Master Python, past-exam questions) are not mirrored; Phase 3 lists which to adopt as exercises.

## 4. Approved deviations

Phase 4 rulings, 2026-11-13 (teacher), see `audit-summary.md` for evidence:

| Id | Ruling |
|---|---|
| D1 | Adopt `elif` (rolling condition is in python-a.pdf p.4): ~10 min in 4.3; remove the "not official" statements. |
| D4 | Adopt `not` (~5 min) and `+=` as shorthand (~5 min); remove the bans in Units 5 and 7. |
| D2 | **Return-lite** in 8.3 (~20 min, zero net time); checkpoint A stays return-free. Approved deviation from python-a.pdf p.17 (functions that do not return a value remain the assessed form). |
| D3 | Add a ~10 min translation drill to the exam turtle dialect (`wn = turtle.Screen()`, `pen = turtle.Turtle()`, `mainloop`); module-level turtle stays the teaching style in Units 2-9 (**approved deviation**). |
| D5 | Add the coordinates / `goto` / `setx` / `sety` block (~8-10 min) to Unit 2 (addendum for taught classes). |
| D10 | Keep the repo unit order (PDF order; Units 0-2 taught) (**approved deviation** from the folder order). |
| Phase 5 scope | All blocking + should findings, Units 3-9 first, then Units 0-2 as addenda; one commit per unit; teacher approves each unit before the next. 'Nice' findings only when free. |
| Open | D6-D9, D11 follow the audit recommendations unless the teacher says otherwise while reviewing each unit. |


## 5. Phase 5 status (2026-11-13)

| Unit | Status | Hosted here | Deferred / open |
|---|---|---|---|
| 0-1 | Notes and code aligned; addenda for the taught classes | algorithm concept, `
` `	`, business-card task | deck sidecar text (U1-09); rewrite of EnvironmentCheck in ministry template where noted |
| 2 | Addendum (45 min, outside official minutes) | coordinates, `goto`, exam-dialect drill | tests untouched; D3 module-level style recorded as approved deviation |
| 3 | Done (commit 426f25d) | `**`, swap, self-update, multiple assignment, conversion | digit split moved to Unit 4; formula-sheet tour and take-home pack deferred |
| 4 | Done | `elif`, `not`, max of two, digit extraction, meeting-17 items | max of three (take-home E14); 7.6 flow charts (not in import) |
| 5 | Done | `+=`, `end=`, for+if `%`, digit_sum, finite/endless loops, Super Python with `elif`, meeting 18 conversion | `for...else` not taught; H5P/Master Python not reviewable offline |
| 6 | Done | negative indexes, string-building loop, exam dialect in checkpoint, meeting 19 homework | turtle half of meeting 19 |
| 7 | Done | `+=` / `elif` allowed, sentinel/validation, `survey()` fix, 16.3 Q3 as checkpoint | pattern-ID checkpoint item dropped |
| 8 | Done | return-lite (approved deviation), bridges פעולה/פרמטר, `+=` line | optional OCR of the decks (U8-15) |
| 9 | Done | object-style turtle bridge (approved deviation), meeting-19 exam question as 9.6 checkpoint B | key-name test, 20.2 digit circles, 9.5 timer exam question |

Decks and printed sheets: see `deck-sheet-backlog.md`. Meeting 17-19 exam prep: no meeting added; converted into checkpoints and homework.
