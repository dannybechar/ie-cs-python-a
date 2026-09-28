# Unit 9.3 — Event-Driven Programming

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Click the Map — Screen Clicks and Coordinates (Mission 28)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit9_meeting3_screen_click_final.pptx` (rover vs screen click, the quadrant signs, `goto` the click, `penup`, a stamp on each click, color by `y`, a click counter, stop after five, edge testing kept; `screen.onclick` replaced by the module function `turtle.onscreenclick`; `+=` replaced)  
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
| Teaching: register the screen with a listener for a mouse click | ✅ |

Official topic and minutes: "mouse click events" — 90 practice. With 9.1 and 9.2 this completes the topic's 225 minutes (45 theory / 180 practice).

### New Turtle tools
`goto(x, y)` and the coordinate system (0, 0 in the middle) appear here for the first time: a screen click gives a point, so the rover needs to go to it.

---

## 3. Lesson Goal

**`turtle.onscreenclick` responds to a click anywhere in the window and sends the point that was clicked.**

---

## 4. Core Mental Models

- **Rover vs screen:** `turtle.onclick` — a click on the rover; `turtle.onscreenclick` — a click anywhere.
- **Signs:** right of the middle x > 0, left x < 0; above y > 0, below y < 0.
- **`goto(x, y)` draws a line** unless the pen is up.

---

# 5. First 30 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 28 |
| 1–4 | **Warm-up:** `turtle.onclick` or `turtle.onscreenclick` — which click does each catch? |
| 4–6 | Answer: a click on the rover / a click anywhere |
| 6–11 | `report(x, y)` with `turtle.onscreenclick` |
| 11–15 | **Students:** the signs of x and y in each quarter of the window |
| 15–17 | Answer (table) |
| 17–23 | `goto(x, y)`: each click becomes a new destination |
| 23–29 | A stamp at the click; a click counter with `global` |
| 29–30 | Lab missions |

---

# 6. Lab — 60 Minutes

Starter: [`ScreenClick_Starter.py`](ScreenClick_Starter.py). Reference: [`ScreenClick_Reference.py`](ScreenClick_Reference.py).

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

A stamp at every click: blue above the middle (`y > 0`), red below.

## 52–66 — Task 2: `mark_five(x, y)`

Only 5 stamps; after that every click prints `Finished`. Test clicks on the axes and at the edges too.

## 66–80 — Task 3 (challenge): `connect(x, y)`

Connect the dots: `goto` with the pen down and `dot(10, "orange")` — here the line from the warm-up is the goal.

## 80–83 — Document and save

Save As `G7_U9_M3_ScreenClick_<Name>.py`.

## 83–90 — Exit check

1. What is the difference between `turtle.onclick` and `turtle.onscreenclick`? (where the click is caught)
2. What do x and y hold? (the point that was clicked)
3. How do we count clicks? (a `global` counter updated in the response)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| (0, 0) is the top-left corner | In Turtle it is the middle |
| `goto` jumps without drawing | Only with the pen up |
| The counter can start at 0 inside the response | It would reset at every click |

---

# 8. Assessment Evidence (formative)

- Quadrant signs
- `mark_five()` tested at the edges and after 5 clicks
- Exit check
