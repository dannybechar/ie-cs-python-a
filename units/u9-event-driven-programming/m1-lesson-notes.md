# Unit 9.1 — Event-Driven Programming

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover Waits for Orders — Event, Listener, Response (Mission 26)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit9_meeting1_event_driven_intro_final.pptx` (events in a game, sequential vs event program, event → listener → response, the event loop, the first click, the `onclick(say_hello())` bug, the x and y parameters kept; `screen = turtle.Screen()` / `player = turtle.Turtle()` replaced by the course style `turtle.onclick(...)`, `turtle.done()`)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **9.1 (this)** | **why event-driven: event → listener → response; the event loop; first click** | 45 / 45 |
| 9.2 | clicking the rover: `turtle.onclick`, x and y, state kept between clicks | 45 / 45 |
| 9.3 | clicking the screen: `turtle.onscreenclick`, `goto`, stamps, a click counter | 0 / 90 |
| 9.4 | keyboard: `turtle.listen`, `turtle.onkey`, four directions, borders | 45 / 45 |
| 9.5 | animation with a timer: `turtle.ontimer`, speed, bounce, stop and start | 45 / 45 |
| 9.6 | final project: a game with keys, a click and a timer; unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 9 (python-a.pdf p.18–19):

| Official goal / concept | Covered here |
|---|---|
| Why event-driven programming? | ✅ slides 2–8 (45 theory) |
| Concepts: event, listener, calling a function as a response | ✅ |
| 1. Mouse click on a character (first look) | ✅ slides 9–12, lab |

Official topics and minutes: "why event-driven" — 45 theory; "mouse click events" — 45 practice.

### Deliberate exclusions
No `turtle.Screen()` / `turtle.Turtle()` objects: the whole unit uses the module functions students know from Unit 2 (`turtle.onclick`, `turtle.onscreenclick`, `turtle.onkey`, `turtle.listen`, `turtle.ontimer`, `turtle.done`).

---

## 3. Lesson Goal

**In an event-driven program the user decides what happens next: an event happens, a listener notices it, and a response function runs.**

---

## 4. Core Mental Models

```python
import turtle


def say_hello(x, y):         # the response function
    print("Hello")


turtle.shape("turtle")
turtle.onclick(say_hello)    # the listener: "when the rover is clicked, run say_hello"
turtle.done()                # the event loop: keep the window open and listening
```

- **Sequential program:** lines run in a fixed order, top to bottom.
- **Event-driven program:** the order depends on what the user does.
- **Give the name, not a call:** `turtle.onclick(say_hello)` — with `()` the function runs now, not at the click.
- **A click sends x and y**, so a click response has two parameters (Unit 8).

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 26 |
| 1–5 | **Warm-up:** list events in a game you know: a click, a key, time passing, a touch |
| 5–7 | Answer: an event happens while the program runs; the program waits for it and responds |
| 7–13 | Sequential program (`print`, `input`, `print`) vs a game — who decides the order? |
| 13–19 | Event → listener → response |
| 19–23 | **Students sort:** a click · `turtle.onclick` · `change_color` |
| 23–25 | Answer: the event · the listener · the response |
| 25–31 | The event loop: `turtle.done()` keeps the window open and listening |
| 31–37 | The first click: `turtle.onclick(say_hello)`; `say_hello(x, y)` |
| 37–41 | **Predict:** `turtle.onclick(say_hello)` or `turtle.onclick(say_hello())`? |
| 41–44 | Answer: the name, no parentheses — `()` runs it immediately |
| 44–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Events_Starter.py`](Events_Starter.py). Reference: [`Events_Reference.py`](Events_Reference.py).

## 45–51 — Warm-up: it crashes before anyone clicks

```python
# Warm-up: the program crashes before anyone clicks. Why?
import turtle


def say_hello(x, y):
    print("Hello")


turtle.shape("turtle")
turtle.onclick(say_hello())
turtle.done()
```

`TypeError: say_hello() missing 2 required positional arguments` — the parentheses call the function now, with no x and y. Fix: `turtle.onclick(say_hello)`.

## 51–61 — Task 1: `report_click(x, y)`

Print `Clicked` and the two coordinates.

## 61–71 — Task 2: `turn_and_move(x, y)`

Every click on the rover: `right(90)`, `forward(50)`. After four clicks it is back where it started.

## 71–82 — Task 3 (challenge): `count_click(x, y)`

A `global` counter (Unit 8.4) that prints `Clicks: 1`, `Clicks: 2`, … — the value is kept between events.

## 82–85 — Document and save

Save As `G7_U9_M1_Events_<Name>.py`.

## 85–90 — Exit check

1. What is an event? (something that happens while the program runs)
2. What does a listener do? (it notices the event and calls the response)
3. Why pass the function's name without parentheses? (with them it runs now, not at the event)

### Tool Note – Thonny
A response function's error appears in the Shell only when the event happens. Close the Turtle window to end the program.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The program runs once and ends | `turtle.done()` keeps it waiting for events |
| `onclick(say_hello())` | The name only: `onclick(say_hello)` |
| A click response needs no parameters | A click sends x and y |
| The listener runs the function immediately | It runs it only when the event happens |

---

# 8. Assessment Evidence (formative)

- Sorting event / listener / response
- The parentheses bug explained
- Exit check
