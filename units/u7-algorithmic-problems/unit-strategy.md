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
| מספר אקראי — random number | 1 | 2 | 135 | 7.3 (45 T + 45 P); 7.2 (45 P, see below) | ✅ |
| **Total** | **1** | **5** | **270** | | |

Also listed for this chapter in the program overview (p.3–5) and goals (p.15):

- **Minimum / maximum** — official goals 3 and 5, but the hours table has no line for them → 7.2 (45 P) ✅
- Algorithmic problems using Turtle → 7.3 (random walk with a counter and an accumulator) ✅

**Hours decision (approved by the teacher):** 7.2 spends 45 practice minutes on minimum and maximum, so random numbers get 45 theory + 45 practice instead of 45 + 90. The unit total (270) and its theory/practice split still match.

## Unit 7.1 — Lab + Lab: the counter
- start at 0 before the loop, add 1 inside an `if`, print after the loop.
- two counters; `count = 1` vs `count = count + 1`.

## Unit 7.2 — Lab + Lab: accumulator, minimum, maximum
- accumulator; average = accumulator ÷ counter.
- minimum / maximum starting from the first value; why not 0.

## Unit 7.3 — Knowledge + Lab: random numbers + checkpoint
- `random.randint(a, b)` (both bounds included), dice, guessing game, simulation.
- Turtle random walk.
- checkpoint: practical (`dice_stats()`, `guess_game()`) + theory on paper (trace, `randint` range, pattern identification).

### Scope decisions
- The meetings follow the teacher's raw decks (counter → accumulator and min/max → random).
- **No Python lists:** the raw decks loop over lists (`[4, 12, 18]`, `numbers[0]`), which are not part of Python A. The data comes from `range`, `input`, strings (Unit 6) or `randint`.
- No `+=`; no `min()`, `max()` or `.count()` — the patterns are written by hand.
- Turtle stays in the Unit 2 style (`turtle.forward`, `turtle.right`).

## Exit criteria
The student does not only use syntax but identifies the algorithmic
pattern suited to the problem.

## Enrichment
- high-ceiling algorithm challenges.
- enrichment should deepen reasoning rather than introduce unrelated syntax.
