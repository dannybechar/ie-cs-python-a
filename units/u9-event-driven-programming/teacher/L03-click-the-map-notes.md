# Unit 9.3 — Event-Driven Programming

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Click the Map — Screen Clicks and Coordinates (Mission 28)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit9_meeting3_screen_click_final.pptx` (rover vs screen click, the quadrant signs, `goto` the click, `penup`, a stamp on each click, color by `y`, a click counter, stop after five, edge testing kept; `screen.onclick` replaced by the module function `turtle.onscreenclick`, with the exam's `wn.onclick` named as the same call; `+=` shown only as recognition; the ministry's `btn=` buttons and four-quarter colours adopted)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | why event-driven: event → listener → response; the event loop; first click | 45 / 45 |
| 9.2 | clicking the rover: `turtle.onclick`, x and y, state kept between clicks | 45 / 45 |
| **9.3 (this)** | **clicking the screen: `turtle.onscreenclick`, `goto`, stamps, a click counter** | 0 / 90 |
| 9.4 | keyboard: `turtle.listen`, `turtle.onkey`, four directions, borders | 45 / 45 |
| 9.5 | animation with a timer: `turtle.ontimer`, speed, bounce, stop and start | 45 / 45 |
| 9.6 | final project: a game with keys, a click and a timer; unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.18–19) | Covered here |
|---|---|
| 2. Know and implement a mouse click on the screen | ✅ all tasks |
| Mouse buttons (`btn=1`, `btn=3`) and the character vs the screen click (ministry 20.3 task 6) | ✅ Task 3 |
| Teaching: register the screen with a listener for a mouse click | ✅ |

Official topic and minutes: "mouse click events" — 90 practice. With 9.1 and 9.2 this completes the topic's 225 minutes (45 theory / 180 practice).

### New Turtle tools
`goto(x, y)` and the coordinate system (0, 0 in the middle) are taught in the Unit 2 addendum (`units/u2-turtle-graphics/teacher/L04-coordinates-and-exam-notation-notes.md`) and are applied here: a screen click gives a point, so the rover needs to go to it. If a class skipped the addendum, spend 3 minutes on the axes first.

---

## 3. Lesson Goal

**`turtle.onscreenclick` responds to a click anywhere in the window and sends the point that was clicked.**

---

## 4. Core Mental Models

- **Rover vs screen:** `turtle.onclick` — a click on the rover; `turtle.onscreenclick` — a click anywhere.
- **Signs:** right of the middle x > 0, left x < 0; above y > 0, below y < 0.
- **`goto(x, y)` draws a line** unless the pen is up.
- **Exam name:** the exam writes `wn.onclick(f)` for what we write `turtle.onscreenclick(f)`; a click on the character is `player.onclick(f)` (9.2).
- **A click on the rover is also a click on the screen.** To tell them apart, register them on different mouse buttons: `turtle.onclick(grow, btn=1)` (left, the default) and `turtle.onscreenclick(shrink, btn=3)` (right).

---

# 5. First 30 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 28 |
| 1–4 | **Warm-up:** `turtle.onclick` or `turtle.onscreenclick` — which click does each catch? |
| 4–6 | Answer: a click on the rover / a click anywhere; the exam writes the second one `wn.onclick(f)` — the same call |
| 6–11 | `report(x, y)` with `turtle.onscreenclick` |
| 11–15 | **Students:** the signs of x and y in each quarter of the window |
| 15–17 | Answer (table) |
| 17–23 | `goto(x, y)`: each click becomes a new destination |
| 23–29 | A stamp at the click; a click counter with `global` |
| 29–30 | Lab missions |

---

# 6. Lab — 60 Minutes

Starter: [`ScreenClick_Starter.py`](../exercises/ScreenClick_Starter.py). Reference: [`ScreenClick_Reference.py`](solutions/ScreenClick_Reference.py).

## 30–38 — Warm-up: a line instead of a jump

```python
# Warm-up: the rover should jump to the click without drawing a line. Fix it.
import turtle


def move_to(x, y):
    turtle.goto(x, y)


turtle.shape("turtle")
turtle.onscreenclick(move_to)
turtle.done()
```

Fix: `penup()` before `goto`, `pendown()` after.

## 38–52 — Task 1: `mark(x, y)`

A stamp at every click, coloured by the quarter of the window (ministry 20.3 task 3): `x >= 0 and y >= 0` red; `x >= 0 and y < 0` blue; `x < 0 and y >= 0` green; otherwise yellow. Use `and` with `elif` (Unit 4.3).

## 52–66 — Task 2: `mark_five(x, y)`

Only 5 stamps; after that every click prints `Finished`. Test clicks on the axes and at the edges too.

## 66–80 — Task 3 (challenge): grow and shrink (ministry 20.3 task 6)

A click **on the rover** makes it bigger (`size` + 1, then `shapesize(size)`); a click **elsewhere** makes it smaller (never below 1). Both functions need `global size`. Because a click on the rover also counts as a screen click, register them on different buttons: `turtle.onclick(grow, btn=1)` and `turtle.onscreenclick(shrink, btn=3)` (on a Mac the right button may be `btn=2`). Reference: `task_3()`.

Take-home: `connect(x, y)` — `goto` with the pen down and `dot(10, "orange")`; here the line from the warm-up is the goal (`task_3_home()`).

## 80–83 — Document and save

Save As `G7_U9_M3_ScreenClick_<Name>.py`.

## 83–90 — Exit check

1. What is the difference between `turtle.onclick` and `turtle.onscreenclick`? (where the click is caught; the exam calls the second one `wn.onclick`)
2. What do x and y hold? (the point that was clicked)
3. How do we count clicks? (a `global` counter updated in the response)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| (0, 0) is the top-left corner | In Turtle it is the middle |
| `goto` jumps without drawing | Only with the pen up |
| The counter can start at 0 inside the response | It would reset at every click |
| A click on the rover is not a screen click | It is both; split the two listeners by mouse button |

---

# 8. Assessment Evidence (formative)

- Quadrant signs and the four-quarter colours
- `mark_five()` tested at the edges and after 5 clicks
- Exit check
