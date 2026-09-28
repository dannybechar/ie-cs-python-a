# Unit 8 — Functions with Parameters

**8h = 2 Theory + 6 Labs = 4 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 8. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 4 meetings built and approved by the teacher. Inspired by the teacher's raw decks (`unit8_meeting1–4`).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.17. Minutes = hours × 45.
Status: ✅ approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| פונקציה — לשם מה? — why functions | 1 | 0 | 45 | 8.1 (45 T) | ✅ |
| פונקציה בלי פרמטר/ים — function without parameters | 0 | 3 | 135 | 8.1 (45 P), 8.2 (90 P) | ✅ |
| פונקציה עם פרמטר/ים — function with parameters | 1 | 3 | 180 | 8.3 (45 T + 45 P), 8.4 (90 P) | ✅ |
| **Total** | **2** | **6** | **360** | | |

Also listed for this chapter in the program overview (p.3–5) and goals (p.17):

- Scope: local variables and `global` (goal 3) → 8.4 ✅
- Functions with and without parameters using Turtle, with a `global` variable (teaching method 5) → 8.1–8.4, 8.4 spiral and checkpoint ✅

## Unit 8.1 — Knowledge + Lab: why functions
- reuse, one place to fix, testing parts; definition vs call; order of execution; `main()`; no return value.

## Unit 8.2 — Lab + Lab: functions without parameters
- split a program with `main()`; input inside a function; Turtle drawing functions (a house).

## Unit 8.3 — Knowledge + Lab: parameters
- parameter vs argument; several parameters and their order; parameter vs input; Turtle sizes.

## Unit 8.4 — Lab + Lab: scope + checkpoint
- local variables, reading an outside variable, `global`; a Turtle spiral with shared state.
- checkpoint: practical (`draw_square(size)` with a global counter, `show_line(symbol, amount)`) + theory on paper.

### Scope decisions
- The meetings follow the teacher's raw decks (why → without parameters → with parameters → scope).
- Students have written one function per task since Unit 1, so 8.1 names the reasons rather than introducing `def`.
- No `return` (Python A functions do not return values), no `+=`.
- Turtle stays in the Unit 2 style (`turtle.forward`, `turtle.right`).

## Depth boundary
Core functions **do not return values** in Grade 7 Python A.

## Enrichment
- larger decomposition and reuse.
- do not introduce `return` as a new core topic.
