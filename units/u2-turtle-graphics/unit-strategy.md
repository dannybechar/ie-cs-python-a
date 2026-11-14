# Unit 2 — Turtle & Graphics

**6h = 1 Theory + 5 Labs = 3 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 2. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete and approved — all 3 meetings built, 270 minutes (45 theory / 225 practice). See [README.md](README.md).
**Phase 5 (ministry alignment, 2026-11-13):** the unit was already taught, so the missing ministry content sits in a separate 45-minute **addendum session** ([`L04-coordinates-and-exam-notation-notes.md`](teacher/L04-coordinates-and-exam-notation-notes.md)) outside the three taught minute plans and outside the official 270 minutes. The three taught plans are unchanged (each still 90). Tests are unchanged.

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.7. Minutes = hours × 45.
Status: ✅ built · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| הכרת הספרייה turtle — the turtle library | 1 | 1 | 90 | m1 | ✅ |
| יצירת משטח עבודה וסמן — work surface and pen | 0 | 1 | 45 | m1, m2 | ✅ |
| הוראות תנועה, מיקום ושינוי כיוון — movement, position, direction | 0 | 2 | 90 | m1, practiced in m3; **position (coordinates, `goto`, `setx`, `sety`, `position`) in the addendum** | ✅ movement and direction · ✅ position (addendum) |
| שינוי מאפייני דמות — changing shape attributes | 0 | 1 | 45 | m2, practiced in m3 | ✅ |
| **Total** | **1** | **5** | **270** | | |

## Unit 2.1 — Knowledge + Lab
- import / basic Turtle environment.
- `Screen` and turtle.
- movement, direction, angle, distance.
- first geometric output.

## Unit 2.2 — Lab + Lab
- pen / turtle attributes.
- visibility, stamp, color, size where relevant.
- build geometric figures from sequential instructions.
- emphasize documentation and readable code.

## Unit 2.3 — Lab + Lab
- integrated geometric challenge.
- changing parameters and predicting the effect.
- practical micro-assessment: create a required shape from specifications.

## Addendum session (45 min, taught classes)
- coordinates, quadrants, `goto`, `setx`/`sety`, `position()`, jumping with `penup`/`pendown` (D5, finding U2-02; 15 min with the warm-up).
- short names `fd lt rt bk pu pd` as reading only, and `backward` (U2-03); `color()` next to `pencolor()` (U2-04); fill and `turtlesize` (U2-05); optional types-of-angles task (U2-08).
- 10-minute translation drill to the exam notation (`wn = turtle.Screen()`, `pen = turtle.Turtle()`, `wn.mainloop()`; D3, U2-01), reused in the Unit 6 and Unit 9 checkpoints.
- Terminology bridge: "פעולה" is the exam word for a command or function; the four ministry groups of turtle actions (relative movement, styling, position, pen) appear in the lab briefs.

## Approved deviations (teacher rulings 2026-11-13)
- **Module-level turtle** (`turtle.forward`, `turtle.done()`) stays the teaching style in Units 2–9. The ministry decks and the exam use `wn = turtle.Screen()`, `pen = turtle.Turtle()`, `pen.forward(...)`, `wn.mainloop()`. Mitigation: the addendum translation drill (10 min), repeated in the Unit 6 and Unit 9 checkpoints.
- Unit order stays as in the PDF (turtle first, no loops, input or `if` inside Unit 2), so ministry tasks that need `input()` or `elif` are not used here.

## Scope decisions
- The taught meetings 2.1–2.3 keep their exclusions (`goto`, `backward`, fill, `color` etc. are not in the 90-minute plans); the addendum adds them. Earlier statements that coordinates are "not in scope" are replaced by this section.
- Take-home: extras 01–11 (nine of the ten originals use `goto`, so they follow the addendum).
- Not adopted: ministry task 14 #7 (polygon generator with input and `elif`, Unit 8/9 material) and the pentagon (more than 8 instructions, left to Unit 5).

## Enrichment
- richer geometric scenes/patterns.
- no Classes or advanced new syntax.
