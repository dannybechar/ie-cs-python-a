# Unit 9.2 — Event-Driven Programming

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Click the Rover — `onclick`, x and y, State between Clicks (Mission 27)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit9_meeting2_turtle_click_final.pptx` (the listener warm-up, a click changes the color, clicking outside the rover, `stamp` on a click, the blue/orange toggle and its trace, the size toggle with `big = not big`, the code checklist kept; the two-turtle slide dropped, because the course uses one turtle; `+=` replaced)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | why event-driven: event → listener → response; the event loop; first click | 45 / 45 |
| **9.2 (this)** | **clicking the rover: `turtle.onclick`, x and y, state kept between clicks** | 45 / 45 |
| 9.3 | clicking the screen: `turtle.onscreenclick`, `goto`, stamps, a click counter | 0 / 90 |
| 9.4 | keyboard: `turtle.listen`, `turtle.onkey`, four directions, borders | 45 / 45 |
| 9.5 | animation with a timer: `turtle.ontimer`, speed, bounce, stop and start | 45 / 45 |
| 9.6 | final project: a game with keys, a click and a timer; unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.18–19) | Covered here |
|---|---|
| 1. Know and implement a mouse click on a character | ✅ all tasks |
| Teaching: register a character with a listener for a mouse click | ✅ |

Official topic and minutes: "mouse click events" — 45 theory + 45 practice.

---

## 3. Lesson Goal

**`turtle.onclick` responds only to a click on the rover; a variable that must survive between clicks lives outside the function and is changed with `global`.**

---

## 4. Core Mental Models

- **The signature:** a click response always has `(x, y)`, even if it does not use them.
- **Only the rover:** a click on an empty part of the window does nothing (that is 9.3).
- **State:** `current`, `big` or a counter is kept outside the function; the response reads and changes it with `global` (Unit 8.4).
- **`big = not big`** flips a Boolean (Unit 4).

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 27 |
| 1–4 | **Warm-up:** which line registers the listener, and which keeps the window listening? |
| 4–6 | Answer: `turtle.onclick(...)` registers; `turtle.done()` keeps listening |
| 6–13 | A click changes the color: `change_color(x, y)` |
| 13–17 | **Try it:** click the rover, then an empty spot — what happens? |
| 17–19 | Answer: only a click on the rover is caught |
| 19–25 | Using x and y: print them, `stamp()` |
| 25–32 | State between clicks: `current = "blue"`, `global current`, toggle |
| 32–36 | **Trace:** three clicks from `blue` |
| 36–38 | Answer: orange, blue, orange |
| 38–44 | `big = not big` and `shapesize`; code checklist: `(x, y)`, the name without `()`, `turtle.done()` at the end |
| 44–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`TurtleClick_Starter.py`](TurtleClick_Starter.py). Reference: [`TurtleClick_Reference.py`](TurtleClick_Reference.py).

## 45–51 — Warm-up: an error at the click

```python
# Warm-up: click the rover. It should turn red. Why is there an error?
import turtle


def change_color():
    turtle.color("red")


turtle.shape("turtle")
turtle.onclick(change_color)
turtle.done()
```

At the click: `TypeError: change_color() takes 0 positional arguments but 2 were given`. Fix: `def change_color(x, y):`.

## 51–61 — Task 1: `toggle_color(x, y)`

Blue ↔ orange on every click, with `global current`.

## 61–71 — Task 2: `toggle_size(x, y)`

`big = not big`; `shapesize(3)` or `shapesize(1)`.

## 71–82 — Task 3 (challenge): `step_forward(x, y)`

Every click moves the rover 40; after 5 clicks it prints `Arrived` and stops moving (a counter and a condition).

## 82–85 — Document and save

Save As `G7_U9_M2_TurtleClick_<Name>.py`.

## 85–90 — Exit check

1. What does `turtle.onclick` respond to? (a click on the rover)
2. Why does the response get x and y? (the click event sends its coordinates)
3. When is `global` needed? (to change an outside variable inside the response)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A click anywhere triggers `turtle.onclick` | Only a click on the rover |
| The toggle variable can live inside the function | It would start again at every click |
| Without `(x, y)` the function still works | Python sends two values: `TypeError` |

---

# 8. Assessment Evidence (formative)

- Toggle trace
- The warm-up `TypeError` explained
- Exit check
