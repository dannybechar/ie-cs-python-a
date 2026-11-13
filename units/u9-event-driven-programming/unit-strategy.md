# Unit 9 — Event-Driven Programming

**12h = 4 Theory + 8 Labs = 6 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 9. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 6 meetings built and approved by the teacher. Inspired by the teacher's raw decks (`unit9_meeting1–6`).
**Ministry alignment (Phase 5, unit 9):** text materials aligned with the ministry Classroom folder (meeting 20 and exam-style material from meeting 19); see [`audit-u9.md`](../../docs/ministry-program/audit-u9.md). Decks and the unit's printed sheets were not changed (see the list at the end).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.19. Minutes = hours × 45.
Status: ✅ approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| תכנות מונחה אירועים — לשם מה? — why event-driven | 1 | 0 | 45 | 9.1 (45 T) | ✅ |
| אירוע לחיצת עכבר: הגדרת אירוע ורישום דמות ומסך — mouse click events | 1 | 4 | 225 | 9.1 (45 P), 9.2 (45 T + 45 P), 9.3 (90 P) | ✅ |
| אירוע לחיצת מקש מקלדת: הגדרת אירוע ורישום — keyboard events | 1 | 2 | 135 | 9.4 (45 T + 45 P), 9.6 (45 P) | ✅ |
| מימוש אנימציה (בשילוב טיימר) — animation with a timer | 1 | 2 | 135 | 9.5 (45 T + 45 P), 9.6 (45 P) | ✅ |
| **Total** | **4** | **8** | **540** | | |

## Unit 9.1 — Knowledge + Lab: why event-driven
- sequential vs event-driven; event → listener → response; `turtle.done()` as the event loop; the first `turtle.onclick`.

## Unit 9.2 — Knowledge + Lab: clicking the rover
- `turtle.onclick`, the `(x, y)` signature, state kept between clicks with `global`; `%` for even/odd clicks and `+=` as recognition; challenge: translating a click program from module style to the exam's object style (8 min).

## Unit 9.3 — Lab + Lab: clicking the screen
- `turtle.onscreenclick` (the exam's `wn.onclick`), coordinate signs, `goto`, stamps coloured by the four quarters (`and`, `elif`), a click counter; challenge: grow on a click on the rover, shrink on a click elsewhere, split by mouse button (`btn=1`, `btn=3`).

## Unit 9.4 — Knowledge + Lab: keyboard
- `turtle.listen`, `turtle.onkey`, key names, four directions, borders; the exam's `onkeypress` / `onkeyrelease`; exit check: the ministry's four `onkeypress` blanks.

## Unit 9.5 — Knowledge + Lab: animation with a timer
- a step function and `turtle.ontimer`; distance per step vs time between steps; bounce; stop and start.

## Unit 9.6 — Lab + Lab: the final game + checkpoint
- a game with keyboard, mouse and timer events sharing score, time and `running`.
- checkpoint: practical (the game) + theory on paper (event types, a timer trace, an exam-style completion question in object style, handler signatures).

### Scope decisions
- The meetings follow the teacher's raw decks (intro → rover click → screen click → keys → timer → game).
- **One turtle, module functions — with a bridge to the exam style (approved deviation, traceability section 4):** the raw decks and the ministry's exam aid create `wn = turtle.Screen()` and `player = turtle.Turtle()`. The course teaches the Unit 2 style: `turtle.onclick` (a click on the rover — the ministry's "character", הדמות), `turtle.onscreenclick` (the screen), `turtle.onkey`, `turtle.listen`, `turtle.ontimer`, `turtle.done()`. The exam style is bridged, not taught separately: `done()` = `mainloop()` (9.1), an 8-minute translation task module to object style (9.2), `wn.onclick` = `turtle.onscreenclick` (9.3), `onkeypress` (9.4), and an exam-style question in object style in Checkpoint B (9.6). The game's target is a red dot at `target_x, target_y`, not a second turtle.
- **Constructs allowed here, with their home unit:** `not` (Unit 4), `elif` (4.3), `%` (Unit 3), `+=` as recognition only (5.1; the long form stays the main form). Ministry words: פעולה = function, פרמטר = parameter, דמות = the turtle that listens.
- **"wait":** the Ministry text names a waiting action `wait`; Python's turtle has none, so the timer event `turtle.ontimer` is used (it waits without freezing the window).
- `goto` and coordinates are taught in the Unit 2 addendum and applied in 9.3 (screen clicks); if a class skipped the addendum, add a 3-minute axes recap to 9.3.
- **Not taught (not in the ministry folder or the classroom time):** ministry pong code (`screen.tracer`, `screen.update`, `while True`, turtle attributes such as `ball.dx`, f-strings), `*=`, `ondrag`, audio. Pong is an optional take-home extension (see `exercises/ExtraPractice_Unit9.md`).
- **If the schedule is cut (audit U9-14):** protect in this order 9.1, 9.2, 9.3, 9.6, 9.4; 9.5 is the first to compress, because the ministry folder and its exam-style question contain no timer (python-a.pdf still requires it; open question for the teacher or the ministry). The decision stays with the teacher.

## Exit criteria
The student builds an interactive program that responds to at least two kinds
of user events (for example a mouse click and a key press) and explains the
relationship: `event → listener → function/action`.

## Enrichment from Python C
Appropriate selective extensions (Extension Bank): richer mouse events such as
`ondrag`, audio, more complex games (for example the ministry's pong with a
timer). Timer-based animation is core in 9.5, not enrichment.

## Ministry folder anchors (meeting 20)

| Ministry item | Used in |
|---|---|
| 20.3 tasks 1–2 (move to the click, stamp) | 9.3 warm-up and `mark_five` |
| 20.3 task 3 (colour by quarter, `elif`) | 9.3 Task 1 |
| 20.3 task 4 (`counter % 3`), task 5 (random size) | take-home pack |
| 20.3 task 6 (`btn=1` / `btn=3`) | 9.3 Task 3 |
| 20.4 task 2 part A (four `onkeypress` blanks) | 9.4 exit check |
| 20.4 task 2 part B (true/false), parts C–E (pong), task 1 variations | take-home pack |
| m19 slide 22 (Adi's squares, `%`) | 9.6 Checkpoint B question 3 |
| m20 exam aid (`wn.onclick`, `wn.onkeypress`, `mainloop`) | the object-style bridge, 9.1–9.6 |

## Deferred (not done in this pass)
- Decks 9.1–9.6 and any lab sheet: slides still show the earlier wording (see the coordinator's list).
- m19 slides 21 and 23–24 (read turtle code and draw it; match code to shapes): take-home pack, also a Unit 2 audit item.
- Digits 1–9 with `circle(r, extent)` (20.2): optional take-home, no circle completions.
- Uppercase key name `"A"` (m20.1 slide 12): not adopted until tested on the classroom machines.
