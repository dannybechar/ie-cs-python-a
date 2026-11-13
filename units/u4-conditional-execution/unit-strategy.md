# Unit 4 — Conditional Execution

**6h = 2 Theory + 4 Labs = 3 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 4. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md). Ministry content check: [`../../docs/ministry-program/audit-u4.md`](../../docs/ministry-program/audit-u4.md).

**Build status:** ✅ complete — all 3 meetings built and approved by the teacher; Phase 5 alignment with the ministry program applied (rolling condition `elif`, `not`, digits, max of two, exam items). Inspired by the teacher's raw decks (`chapter4_session1–3`).

The three meeting decks (`m1–m3-slides-he.pdf`) are from before Phase 5 and are pending a patch (see the README).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.10 (hours) and the program overview p.3–4 (topic list). Minutes = hours × 45.
Status: ✅ built and approved · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| ביטויים בוליאניים — boolean expressions | 1 | 2 | 135 | m1 (45 T + 45 P), m3 (45 P) | ✅ m1 + m3 |
| משפטי תנאי — conditional statements | 1 | 2 | 135 | m2 (45 T + 45 P), m3 (45 P) | ✅ m2 + m3 |
| **Total** | **2** | **4** | **270** | | |

Also listed for this chapter: the overview (p.3–4) lists logical conditions, simple and compound conditions (`and`, `or`), the rolling conditional statement and conditions with Turtle; goal 2 on p.10 adds nesting at one level.

| Concept | Source | Planned in |
|---|---|---|
| Logical (boolean) conditions | p.3–4, p.10 | m1 ✅ |
| Simple condition (`if`, `if/else`) | p.3–4, p.10 goal 1 | m2 ✅ |
| Compound condition (`and`, `or`) | p.3–4, p.10 goal 2 | m1 expressions, m3 inside `if` ✅ |
| Nested conditional (one level) | p.10 goal 2 | m3 ✅ |
| **Rolling conditional (`elif`)** — משפט ביצוע מותנה מתגלגל | p.4 | m3 ✅ (10 min, added in Phase 5) |
| Conditions with Turtle — הוראת תנאים באמצעות Turtle | p.4 | m3 ✅ |

Beyond the PDF list, taken from the ministry Classroom folder (meetings 7–9, exam preparation 17–18): `not` (m1, 5 min), digit extraction with `// 10` and `% 10` (m2, 3 min; deferred from Unit 3), the larger of two numbers (m2), exam-style tracing items (m1 warm-up, m3 checkpoint B).

## Unit 4.1 — Knowledge + Lab: the rover's sensors
- comparison operators `== != > < >= <=` (אופרטורי יחס), `=` vs `==`.
- results are `bool`; storing them in variables; string equality.
- `and`, `or`, `not` (קשרים לוגיים) and their truth tables; a condition from a truth table.
- order: arithmetic → comparison → `not` → `and` → `or`.
- lab: trace (two predicts), sensor check, fix `input` vs number, truth tables both ways.

## Unit 4.2 — Knowledge + Lab: if and if/else
- `if`: condition, colon, indented body; a false condition skips the body.
- `if/else`: exactly one branch runs.
- even/odd with `%` (and odd with `not`), pass/fail, the `>=` boundary.
- the two digits of a two-digit number with `// 10` and `% 10`.
- simple input filter: valid / invalid (no re-asking).
- common errors: `=` in a condition, missing colon, missing indentation.
- lab: the larger of two numbers; challenge: even number → sum of digits, odd → product.

## Unit 4.3 — Lab + Lab: compound, nested and rolling conditions, Turtle
- `and` / `or` inside `if`.
- one-level nesting; the rule that an `else` belongs to the nearest `if` at the same indentation; when a compound condition can replace nesting.
- the rolling condition `if` / `elif` / `else` (תנאי מתגלגל): first true wins, order matters, chain vs separate `if`s.
- the four kinds of condition: simple, compound, nested, rolling.
- conditions with Turtle (module-level `turtle.*` calls only; three outcomes: square, triangle, unknown shape).
- practical checkpoint A and tracing checkpoint B (exam-style: a nested `if` inside an `elif` chain, expressions with `%` and `//`).

### Scope decisions
- `elif` (rolling condition) **is** in the program: python-a.pdf p.4 lists it, the ministry folder teaches it and the exam formula sheet contains it. Taught in 4.3 (10 min); Units 5–9 may use it (teacher ruling, Phase 4).
- `not` is taught in 4.1 (5 min), beyond the PDF list, from the ministry folder (teacher ruling D4).
- Digit extraction (`// 10`, `% 10`) is taught in 4.2 (3 min), deferred from Unit 3 (audit U3-01 → U4-04).
- Nesting stays at one level in the core; three-level nesting is an optional take-home item.
- Turtle stays with the Unit 2 style (`turtle.forward`, `turtle.left`); no `t = turtle.Turtle()` or `setheading`. The exam dialect is practised in Units 2, 6 and 9 (approved deviation D3).
- Terminology bridges: "פונקציה (בבחינה: פעולה)", אופרטור יחס, קשר לוגי, and the four condition kinds פשוט / מורכב / מקונן / מתגלגל.
- Unit order is kept as in the PDF (boolean expressions first with no `if`, then `if`); the ministry folder goes simple `if/else` first (approved deviation D10, audit U4-09).

### Time ledger (Phase 5, per meeting, all sums stay 90)
| Meeting | Added | Funded by |
|---|---|---|
| 4.1 (45 T / 45 P) | `not` 5 | strings −2, order −2, transition −1 (theory); the 3-min counter predict fits in the 7-min warm-up |
| 4.2 (45 T / 45 P) | digits 3 (theory); max of two 5 + digits challenge 5 replaces the discount task (practice) | warm-up −1, transition −1, errors −1 (theory); lab warm-up −2, ScoreBug −2, doc −1 (practice) |
| 4.3 (0 / 90) | `elif` 10, association rule 2 | guided 27→37 (compare −1, transition −1); lab: Task 1 10→7 (nested version folded into the demo), Task 2 15→13, checkpoint B 13→12, doc 4→2, exit 6→4 |

Take-home pack (0 class minutes): [`exercises/Extra_Practice.md`](exercises/Extra_Practice.md).

## Exit criteria
The student can formulate a condition, trace which branch was chosen, and
write a solution with a simple, compound or rolling (`elif`) condition.

## Enrichment
- more demanding decision problems without introducing new syntax (the take-home pack).
