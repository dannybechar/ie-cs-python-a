# Unit 9 — Event-Driven Programming

**12h = 4 Theory + 8 Labs = 6 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 9. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 complete — all 6 meetings built, awaiting approval. Inspired by the teacher's raw decks (`unit9_meeting1–6`).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.19. Minutes = hours × 45.
Status: ✅ approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| תכנות מונחה אירועים — לשם מה? — why event-driven | 1 | 0 | 45 | 9.1 (45 T) | 🔶 |
| אירוע לחיצת עכבר: הגדרת אירוע ורישום דמות ומסך — mouse click events | 1 | 4 | 225 | 9.1 (45 P), 9.2 (45 T + 45 P), 9.3 (90 P) | 🔶 |
| אירוע לחיצת מקש מקלדת: הגדרת אירוע ורישום — keyboard events | 1 | 2 | 135 | 9.4 (45 T + 45 P), 9.6 (45 P) | 🔶 |
| מימוש אנימציה (בשילוב טיימר) — animation with a timer | 1 | 2 | 135 | 9.5 (45 T + 45 P), 9.6 (45 P) | 🔶 |
| **Total** | **4** | **8** | **540** | | |

## Unit 9.1 — Knowledge + Lab: why event-driven
- sequential vs event-driven; event → listener → response; `turtle.done()` as the event loop; the first `turtle.onclick`.

## Unit 9.2 — Knowledge + Lab: clicking the rover
- `turtle.onclick`, the `(x, y)` signature, state kept between clicks with `global`.

## Unit 9.3 — Lab + Lab: clicking the screen
- `turtle.onscreenclick`, coordinate signs, `goto`, stamps, a click counter.

## Unit 9.4 — Knowledge + Lab: keyboard
- `turtle.listen`, `turtle.onkey`, key names, four directions, borders.

## Unit 9.5 — Knowledge + Lab: animation with a timer
- a step function and `turtle.ontimer`; distance per step vs time between steps; bounce; stop and start.

## Unit 9.6 — Lab + Lab: the final game + checkpoint
- a game with keyboard, mouse and timer events sharing score, time and `running`.
- checkpoint: practical (the game) + theory on paper (event types, a timer trace, the parentheses bug).

### Scope decisions
- The meetings follow the teacher's raw decks (intro → rover click → screen click → keys → timer → game).
- **One turtle, module functions:** the raw decks create `screen = turtle.Screen()` and several `turtle.Turtle()` objects. The course keeps the Unit 2 style: `turtle.onclick` (a click on the rover — the Ministry's "character"), `turtle.onscreenclick` (the screen), `turtle.onkey`, `turtle.listen`, `turtle.ontimer`, `turtle.done()`. The game's target is a red dot at `target_x, target_y`, not a second turtle.
- **"wait":** the Ministry text names a waiting action `wait`; Python's turtle has none, so the timer event `turtle.ontimer` is used (it waits without freezing the window).
- `goto` and coordinates appear for the first time in 9.3 (needed for screen clicks).
- No `+=` / `-=`.

## Exit criteria
The student builds an interactive program that responds to at least user
events and explains the relationship: `event → listener → function/action`.

## Enrichment from Python C
Appropriate selective extensions: richer mouse events such as `ondrag`,
timer-oriented behavior, audio, more complex games.
