# Unit 5 — Repetition and Loops

**8h = 2 Theory + 6 Labs = 4 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 5. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 4 meetings built and approved by the teacher. Inspired by the teacher's raw decks (`unit5_meeting1–4`).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.12. Minutes = hours × 45.
Status: ✅ approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| ביצוע חוזר לשם מה? — why repetition | 1 | 0 | 45 | 5.1 (45 T) | ✅ |
| ביצוע חוזר מוגבל מראש, מותנה — bounded and conditional loops | 1 | 6 | 315 | 5.1 (45 P), 5.2 (90 P), 5.3 (45 T + 45 P), 5.4 (90 P) | ✅ |
| **Total** | **2** | **6** | **360** | | |

Also listed for this chapter in the program overview (p.3–5):

- Rolling repeated execution (ביצוע חוזר מתגלגל) → 5.4 (tracing) ✅
- Loops using Turtle → 5.2 (polygons, spiral, star), 5.4 (flower) ✅

## Unit 5.1 — Knowledge + Lab: for and range
- why repetition; pseudo-code "repeat n times".
- `for` + `range(n)` and `range(start, stop)`; stop is excluded.
- loop variable; trace tables; running total.

## Unit 5.2 — Lab + Lab: range with a step and Turtle
- `range(start, stop, step)`; counting down with a negative step.
- regular polygons (`360 / n`), a square spiral, a star.

## Unit 5.3 — Knowledge + Lab: while
- start value, condition, update; the final `False` check.
- endless loops; input until valid; sentinel value.
- for vs while; correctness.

## Unit 5.4 — Lab + Lab: loops inside loops + checkpoint
- nested loops, star patterns with `end=""`, a Turtle flower.
- rolling repeated execution (tracing).
- checkpoint: practical (a `for` program and a `while` program) + theory (trace, round count, loop type).

### Scope decisions
- The meetings follow the teacher's raw decks (for → range + Turtle → while → nested). 5.1 and 5.3 carry the 90 theory minutes.
- `+=` / `-=` are not used — the course keeps `x = x + 1`.
- Turtle stays in the Unit 2 style (`turtle.forward`, `turtle.right`); the raw 3×3 grid (`backward`) was dropped.
- Nested loops and `print(..., end="")` appear in 5.4 only (official teaching: shapes and in-depth practice).

## Exit criteria
The student identifies when a loop is required, chooses the appropriate
type, traces execution, and explains the stop condition.

## Enrichment
- high-ceiling pattern/challenge using existing control structures.
