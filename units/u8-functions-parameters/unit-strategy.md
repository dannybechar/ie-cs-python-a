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
| *Not in python-a.pdf:* a function that returns a value (return-lite, ministry meeting 10) | 0 | 0 | 0 net (20 min of 8.3) | 8.3 (10 T + 10 P), checkpoint B Q4 | ✅ approved deviation D2 |
| **Total** | **2** | **6** | **360** | | |

Also listed for this chapter in the program overview (p.3–5) and goals (p.17):

- Scope: local variables and `global` (goal 3) → 8.4 ✅
- `+=` as recognition (shorthand for `x = x + 1`, introduced in 5.1) → shown once in 8.4 ✅
- `elif` (taught in 4.3) → used in `sign_text` in 8.3 ✅
- Functions with and without parameters using Turtle, with a `global` variable (teaching method 5) → 8.1–8.4, 8.4 spiral and checkpoint ✅

## Unit 8.1 — Knowledge + Lab: why functions
- reuse, one place to fix, testing parts; definition vs call; order of execution; `main()`; functions that act (print or draw); the word "פעולה" = "פונקציה".
- no `return` yet: every function here acts; return arrives in 8.3.

## Unit 8.2 — Lab + Lab: functions without parameters
- split a program with `main()` (and the module-level call style of the ministry); input inside a function; Turtle drawing functions (a house).
- ministry 4.3 arithmetic-in-a-function practice: trace warm-up (`78.0`, `//`, `/`), `rectangle()`, `pool()`; `draw_door()` is take-home.

## Unit 8.3 — Knowledge + Lab: parameters
- parameter vs argument ("פרמטר" / "ערך" in exam wording); several parameters and their order; parameter vs input (inside, or read outside and passed in); `pool(times, price)`; Turtle sizes.
- **return-lite** (20 min): `add(x, y)` returns, `print` shows and `return` hands back, nested calls, `absolute_value`, `sign_text`; one simple value per function.

## Unit 8.4 — Lab + Lab: scope + checkpoint
- local variables, reading an outside variable, `global` (ministry 16.1 `score` riddle); `+=` recognition; a bridge from Unit 5: `sum_numbers(num1, num2)`; a Turtle spiral with shared state.
- checkpoint: practical (`draw_square(size)` with a global counter, `show_line(symbol, amount)`; no `return`, as the PDF assessment says) + theory on paper (including a return trace).

### Scope decisions
- The meetings follow the teacher's raw decks (why → without parameters → with parameters → scope).
- Students have written one function per task since Unit 1, so 8.1 names the reasons rather than introducing `def`.
- **Return-lite adopted (teacher ruling D2, `traceability.md` section 4):** ministry meeting 10 teaches `return` and the ministry's worked solutions in meetings 8, 12, 13 and 16 use it. It is taught only in 8.3 (20 min, zero net time), for one simple value. python-a.pdf p.17 (goals 1-2, assessment item 2) speaks of functions that return no value; that is **an approved deviation**, and the practical assessment (checkpoint A) stays return-free.
- `+=` is allowed as recognition (ruling D4): long form `x = x + 1` stays the main form.
- `elif` is available (taught in 4.3, ruling D1).
- Terminology: the course says "פונקציה" (as python-a.pdf); ministry materials say "פעולה" and call both parameter and argument "פרמטר" / "ערך". Bridge lines are in 8.1 and 8.3.
- `main()` is kept as a name we choose; the ministry style (call at module level) is shown in 8.2 and 8.3.
- Turtle stays in the Unit 2 module-level style (`turtle.forward`, `turtle.right`), and `turtle.done()` sits at the end of the program ("`done()` = `mainloop()`", the exam word). The exam dialect (`wn = turtle.Screen()`, `pen = turtle.Turtle()`) is practised in Units 2, 6 and 9, not here.
- The ministry's own sizing of functions is larger (4 to 5 double meetings); nothing is added: the 20 min of return-lite and the 4.3 tasks are swaps inside existing meetings, and the rest goes to take-home (`exercises/Extra_Practice_U8.md`).
- Core and optional ("רשות") tasks are marked in each lab brief.

## Depth boundary
Functions return **one simple value** (a number or a string) and nothing else: no several return values, no `return` in a search loop, no `None` discussion. Practical checkpoint tasks use functions that return nothing.

## Enrichment
- larger decomposition and reuse.
- take-home pack: `exercises/Extra_Practice_U8.md` (ministry 4.3 and 10.2 / 10.4 items, `draw_door`, `draw_rectangle`, digit functions with `//` and `%`).
- deferred: H5P 10.5 / 10.6 and "Master Python" 4.4 / 10.3 links (content not extractable) as optional homework links.
