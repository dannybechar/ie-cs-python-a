# Unit 5 — Repetition and Loops

**8h = 2 Theory + 6 Labs = 4 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 5. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 4 meetings built and approved by the teacher; text materials aligned with the ministry program in Phase 5 (decks not yet updated, see below). Inspired by the teacher's raw decks (`unit5_meeting1–4`).

**Phase 5 (2026-11-13):** minute plans still sum to 90 per meeting (45 / 45 for 5.1 and 5.3, 0 / 90 for 5.2 and 5.4). Slide decks and PDFs are unchanged; the new blocks (`+=`, `end`, `for`+`if %`, finite/endless, `digit_sum`, Super Python, new checkpoint B items) still need deck slides.

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.12. Minutes = hours × 45.
Status: ✅ approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| ביצוע חוזר לשם מה? — why repetition | 1 | 0 | 45 | 5.1 (45 T) | ✅ |
| ביצוע חוזר מוגבל מראש, מותנה — bounded and conditional loops | 1 | 6 | 315 | 5.1 (45 P), 5.2 (90 P), 5.3 (45 T + 45 P), 5.4 (90 P) | ✅ |
| **Total** | **2** | **6** | **360** | | |

Also listed for this chapter in the program overview (p.3–5):

- Rolling repeated execution (ביצוע חוזר מתגלגל) → 5.4 Super Python: a `for` loop with a rolling `elif` condition (the folder's meaning of "rolling", Phase 5) ✅; the carried-value trace stays as a tracing exercise
- Loops using Turtle → 5.2 (polygons, spiral, star) ✅; the 5.4 flower is an optional take-home
- `+=` / `-=` → recognition in 5.1 and 5.3 (ministry decks and exam items use them) ✅
- `print(..., end=" ")` (attribute תכונה) → 5.2 ✅
- `for` + `if` with `%`, finite/endless loops, digit sum (`% 10`, `// 10`) → 5.2, 5.3 ✅
- Equivalent for/while loops, exam-style items (ministry meeting 18) → 5.4 checkpoint B + homework ✅

## Unit 5.1 — Knowledge + Lab: for and range
- why repetition; pseudo-code "repeat n times".
- `for` + `range(n)` and `range(start, stop)`; stop is excluded.
- loop variable; trace tables; running total.

## Unit 5.2 — Lab + Lab: range with a step and Turtle
- `end=" "` / `end=","`: one line of output.
- `for` + `if` with `%` compared with a `range` step; 7-boom.
- `range(start, stop, step)`; counting down with a negative step.
- regular polygons (`360 / n`), a square spiral, a star.

## Unit 5.3 — Knowledge + Lab: while
- start value, condition, update; the final `False` check.
- endless loops; input until valid; sentinel value.
- finite or endless? classification of snippets.
- for vs while; correctness.
- digit sum with `% 10` and `// 10` (challenge).

## Unit 5.4 — Lab + Lab: loops inside loops + checkpoint
- nested loops, star patterns with `end=""`.
- Super Python: a `for` loop over 10 scores with an `elif` chain (rolling condition), counts and an average.
- checkpoint: practical (a `for` program and a `while` program) + theory in exam style (trace, round count, equivalent loops, purpose, fill the blank, finite or endless).
- homework: ministry exam-prep sets 18.1 / 18.2 on paper (see `teacher/L04-loops-inside-loops-notes.md` section 9).

### Scope decisions
- The meetings follow the teacher's raw decks (for → range + Turtle → while → nested). 5.1 and 5.3 carry the 90 theory minutes.
- `+=` / `-=` are adopted as **shorthand for recognition** (teacher ruling, 2026-11-13): introduced in 5.1, the long form `x = x + 1` stays the main form students write; allowed in Units 5–9. This is an approved deviation from the repo's earlier ban; the ministry decks and exam items use `+=`.
- `elif` (Unit 4.3) may be used from 5.4 on; "rolling" (מתגלגל) means the `elif` chain, as in the ministry folder. The earlier "value carries over from round to round" reading is no longer called rolling.
- Turtle stays in the Unit 2 style (`turtle.forward`, `turtle.right`); the raw 3×3 grid (`backward`) was dropped. The exam turtle dialect (`wn`, `pen`, `mainloop`) is a Unit 2 translation drill, reused in Units 6 and 9.
- `print(..., end="")` is taught in 5.2 (one line of output) and reused for star patterns in 5.4. Nested loops are repo-only (not named in the program): a short demo plus star patterns; the flower is optional.
- The ministry says "פעולה" for a function, "תכונה" for `end`, "תנאי עצירה" for the stop condition; the briefs give both words.
- Digit extraction (`% 10`, `// 10`) comes from Unit 4; `digit_sum()` prints its result (return comes in Unit 8).
- Not in class (take-home pack [`exercises/Extra_Practice_Unit5.md`](exercises/Extra_Practice_Unit5.md)): counters/averages over several inputs, the three-digit input check, perfect number, reverse a number, the finite/endless worksheet. `for ... else` is not taught (not in the course or the program extracts).

## Exit criteria
The student identifies when a loop is required, chooses the appropriate
type, traces execution, and explains the stop condition.

## Enrichment
- high-ceiling pattern/challenge using existing control structures.
