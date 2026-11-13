# Unit 7 — Algorithmic Problems

**6h = 1 Theory + 5 Labs = 3 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 7. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 3 meetings built and approved by the teacher. Inspired by the teacher's raw decks (`unit7_meeting1–3`).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.15. Minutes = hours × 45.
Status: ✅ approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| מונה — counter | 0 | 2 | 90 | 7.1 (90 P) | ✅ |
| צובר — accumulator | 0 | 1 | 45 | 7.2 (45 P) | ✅ |
| מספר אקראי — random number | 1 | 2 | 135 | 7.3 (45 T + 45 P); the second practice hour was moved to min/max in 7.2 (approved, see below) | ✅ |
| **Total** | **1** | **5** | **270** | | |

Also listed for this chapter in the program overview (p.3–5) and goals (p.15):

- **Minimum / maximum** — official goals 3 and 5, but the hours table has no line for them → 7.2 (45 P) ✅
- Algorithmic problems using Turtle → 7.3 (random walk with a counter and an accumulator) ✅

**Hours decision (approved by the teacher):** 7.2 spends 45 practice minutes on minimum and maximum, so random numbers get 45 theory + 45 practice (90 minutes in total, not 135) and min/max gets 45. The unit total (270) and its theory/practice split still match; only the per-row allocation differs from the table above.

## Unit 7.1 — Lab + Lab: the counter
- start at 0 before the loop, add 1 inside an `if`, print after the loop; the success-circle planning questions.
- `count += 1` as a recognition-only shorthand (**קידום**, "כתיבה מקוצרת").
- two and three counters; `elif` for three classes (coins); `count = 1` vs `count = count + 1`.
- a survey with an invalid-answer branch (three counters add up to 8).

## Unit 7.2 — Lab + Lab: accumulator, minimum, maximum
- accumulator; average = accumulator ÷ counter; `total += value` as a shorthand.
- counter and accumulator in a `while` loop with a sentinel (donations).
- minimum / maximum starting from the first value; why not 0.
- closing note: `max(a, b, c)`, `min(...)` and `text.count(ch)` exist.

## Unit 7.3 — Knowledge + Lab: random numbers + checkpoint
- `random.randint(a, b)` (both bounds included), `random.randrange(a, b)` (end excluded) and `random.random()` (formula sheet), two dice and doubles, guessing game, simulation.
- Turtle random walk.
- checkpoint: practical (`dice_stats()`, `guess_game()`) + theory on paper (trace, `randint` / `randrange` range, two fragments of the ministry past-exam question 16.3 Q3, why a maximum starts with the first value).

### Scope decisions
- The meetings follow the teacher's raw decks (counter → accumulator and min/max → random).
- **No Python lists:** the raw decks loop over lists (`[4, 12, 18]`, `numbers[0]`), which are not part of Python A. The data comes from `range`, `input`, strings (Unit 6) or `randint`.
- **`+=` is allowed (teacher ruling D4, Phase 4):** introduced in 5.1 as recognition and shown again here after the long form (7.1, 7.2). The long form `x = x + 1` stays the main form for writing; reading tasks and checkpoints may use `+=`. (The earlier ban is removed.)
- **`elif` is allowed (ruling D1):** taught in 4.3 and used here for the three-way coin counter and the survey. Minimum and maximum still use two separate `if`s, on purpose.
- `min()`, `max()` and `.count()` are not used in the tasks (the patterns are written by hand, PDF goal 5); 7.2 names them in a 2-minute closing note, because the exam formula sheet has them.
- Turtle stays in the Unit 2 style (`turtle.forward`, `turtle.right`); module-level turtle is the approved deviation from the exam dialect (see `docs/ministry-program/traceability.md` section 4).
- Counters and accumulators are practised with `for` (known length) and with `while` and a sentinel (donations, 7.2; guessing game, 7.3).
- Pass mark 55 and range 55–80 follow the ministry items (U7-09).
- No `return`: the ministry two-dice summary task counts doubles inline. Return-lite arrives in 8.3; `global` stays in 8.4 (approved order deviation, U7-07).
- Terminology bridges: **קידום** next to "עדכון" for the counter; "פונקציה (בבחינה: פעולה)".

### Minute plans (each meeting sums to 90)

| Meeting | Split | Main blocks |
|---|---|---|
| 7.1 | 30 guided + 60 lab (0 / 90) | counter 7 · `+=` 3 · trace 5 · coins with `elif` 7 · warm-up 9 · `passed_count` 14 · `survey` (3 counters) 17 · `count_digits` 11 · save 3 · exit 6 |
| 7.2 | 35 guided + 55 lab (0 / 90) | trace 6 · `+=` 2 · average 5 · prediction 2 · maximum 7 · `maximum = 0` 5 · warm-up 6 · `donations` (`while`) 15 · `min_max` 12 · `temperatures` 16 · shortcut note 2 · save 1 · exit 3 |
| 7.3 | 45 knowledge + 45 lab (45 / 45) | table incl. `randrange`, `random.random()` 10 · choose 6 · double dice 6 · guessing game 7 · simulation 5 · prediction 3 · `random_walk` 12 · checkpoint A 16 · checkpoint B 8 + 3 · save 2 · exit 4 |

Full tables are in each lesson note. Decks, lab sheets and PDFs were not rebuilt: the new items are shown live (see the "Deck" paragraph in each lesson note).

### Deferred and take-home
- [`exercises/Extra_Practice_he.md`](exercises/Extra_Practice_he.md): 18 take-home exercises with source references (flags, card game, storage space, beach cleaning, technicians, hiring, time loops 16.5, random grades, fragments B and D of 16.3 Q3, random walk with `goto`, escape-room lock, primes, `for` to `while`). Zero class minutes. Ministry defects in 16.3 Q4 and Q5 (`work =+1`, the name clash with `def work()`, `range(9)`, the typo `mange`) are not copied.
- Not in Unit 7: the gcd task needs `return` (8.3); the `global` riddle (8.4); the H5P time-loop part A has no readable content.

## Exit criteria
The student does not only use syntax but identifies the algorithmic
pattern suited to the problem.

## Enrichment
- high-ceiling algorithm challenges: primes (16.6 #7, #8), `for` to `while` (#10), the escape-room lock (16.3 Q5), all in the take-home pack.
- enrichment should deepen reasoning rather than introduce unrelated syntax.
