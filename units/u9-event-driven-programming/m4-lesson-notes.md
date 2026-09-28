# Unit 9.4 — Event-Driven Programming

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Drive with the Arrows — Keyboard Events (Mission 29)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit9_meeting4_keyboard_events_final.pptx` (which signature fits a key, `listen` and `onkey`, three checks when a key does not respond, four directions, borders, the pen toggle on space, reaching a target kept; `screen.` replaced by the module functions; the target drawn as a dot instead of a second turtle)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | why event-driven: event → listener → response; the event loop; first click | 45 / 45 |
| 9.2 | clicking the rover: `turtle.onclick`, x and y, state kept between clicks | 45 / 45 |
| 9.3 | clicking the screen: `turtle.onscreenclick`, `goto`, stamps, a click counter | 0 / 90 |
| **9.4 (this)** | **keyboard: `turtle.listen`, `turtle.onkey`, four directions, borders** | 45 / 45 |
| 9.5 | animation with a timer: `turtle.ontimer`, speed, bounce, stop and start | 45 / 45 |
| 9.6 | final project: a game with keys, a click and a timer; unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.18–19) | Covered here |
|---|---|
| 3. Know and implement key presses | ✅ all tasks |
| Concepts: keyboard event `onkey`, registering a listener `listen` | ✅ |

Official topic and minutes: "keyboard events" — 45 theory + 45 of its 90 practice minutes (the rest in 9.6).

---

## 3. Lesson Goal

**`turtle.listen()` turns on listening to the keyboard; `turtle.onkey(function, "Up")` connects a key to a response.**

---

## 4. Core Mental Models

- **A key sends no x and y:** a key response has no parameters.
- **Three checks when a key does nothing:** `turtle.listen()` is there · the key name is exact (`"Up"`, `"space"`) · the function name has no `()`.
- **Move on one axis:** `sety(ycor() + 20)` or `setx(xcor() - 20)`.
- **Check before moving:** compute the new x, move only if it is inside the border.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 29 |
| 1–5 | **Warm-up:** `def up():` or `def up(x, y):` for a key? Why? |
| 5–7 | Answer: `def up():` — a key sends no coordinates |
| 7–15 | `turtle.listen()` and `turtle.onkey(up, "Up")` |
| 15–19 | Three checks when a key does not respond |
| 19–26 | Four directions: `up`, `down`, `left`, `right` with `sety` / `setx` |
| 26–30 | **Students:** write the four `onkey` lines |
| 30–32 | Answer |
| 32–37 | Borders: `new_x = turtle.xcor() + 20`, move only if `new_x <= 200` |
| 37–41 | **Students:** the condition for the left side (−200) |
| 41–43 | Answer: `if new_x >= -200:` |
| 43–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Keys_Starter.py`](Keys_Starter.py). Reference: [`Keys_Reference.py`](Keys_Reference.py).

## 45–50 — Warm-up: nothing happens

```python
# Warm-up: press the Up arrow. Why does nothing happen?
import turtle


def up():
    turtle.sety(turtle.ycor() + 20)


turtle.shape("turtle")
turtle.onkey(up, "Up")
turtle.done()
```

`turtle.listen()` is missing, so the window does not listen to the keyboard. (Click the window first so it has the focus.)

## 50–62 — Task 1: four directions, with borders

`up`, `down`, `left`, `right`; left and right stay between −200 and 200.

## 62–70 — Task 2: `toggle_pen()`

Space switches between drawing and moving without drawing: `pen_on = not pen_on`.

## 70–82 — Task 3 (challenge): reach the target

A red dot at (160, 100); after every move check `turtle.distance(160, 100) < 20` and print `Win`.

## 82–85 — Document and save

Save As `G7_U9_M4_Keys_<Name>.py`.

## 85–90 — Exit check

1. What does `turtle.listen()` do? (turns on listening to the keyboard)
2. How do we connect a key to a function? (`turtle.onkey(function, "key")`)
3. Why does a key response not need x and y? (a key event sends no coordinates)

### Tool Note – Thonny
Click the Turtle window once so the keys reach it, not the editor.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `onkey` works by itself | Only after `turtle.listen()` |
| `"up"` is the same as `"Up"` | Key names are exact |
| Move, then check the border | Check the new x first, then move |

---

# 8. Assessment Evidence (formative)

- The three checks
- Border condition for the left side
- Exit check
