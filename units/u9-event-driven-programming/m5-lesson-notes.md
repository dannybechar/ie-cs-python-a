# Unit 9.5 — Event-Driven Programming

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover Moves by Itself — Animation with a Timer (Mission 30)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit9_meeting5_timer_animation_final_v7.pptx` (animation as small changes, a step function, the repeating timer, 50 vs 200 milliseconds, distance per step vs time between steps, bounce with `dx = -dx` and its trace, stop with space and start with s kept; `screen.ontimer` replaced by the module function `turtle.ontimer`; an `ontimer(animate(), 50)` bug added)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | why event-driven: event → listener → response; the event loop; first click | 45 / 45 |
| 9.2 | clicking the rover: `turtle.onclick`, x and y, state kept between clicks | 45 / 45 |
| 9.3 | clicking the screen: `turtle.onscreenclick`, `goto`, stamps, a click counter | 0 / 90 |
| 9.4 | keyboard: `turtle.listen`, `turtle.onkey`, four directions, borders | 45 / 45 |
| **9.5 (this)** | **animation with a timer: `turtle.ontimer`, speed, bounce, stop and start** | 45 / 45 |
| 9.6 | final project: a game with keys, a click and a timer; unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.18–19) | Covered here |
|---|---|
| Teaching: an animation combined with a waiting action | ✅ all tasks |
| Concept: waiting (the Ministry names it `wait`) | ✅ `turtle.ontimer(function, milliseconds)` |

Official topic and minutes: "animation with a timer" — 45 theory + 45 of its 90 practice minutes (the rest in 9.6).

### Source interpretation
The Ministry text names the waiting action `wait`. Python's turtle has no `wait`; the timer event `turtle.ontimer` schedules the next step without freezing the window, so key and click events keep working during the animation.

---

## 3. Lesson Goal

**An animation is many small changes: a step function moves a little and asks the timer to call it again in a few milliseconds.**

---

## 4. Core Mental Models

```python
def animate():
    turtle.forward(5)                # one small change
    turtle.ontimer(animate, 50)      # call me again in 50 milliseconds


animate()                            # the first call starts the chain
turtle.done()
```

- **Distance per step** decides how far; **time between steps** decides how often.
- **Bounce:** at the border `dx = -dx` flips the direction.
- **Stop:** a `running` flag — when it is `False`, the step does not schedule the next one.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 30 |
| 1–5 | **Warm-up:** how do many small, fast changes look like motion? |
| 5–7 | Answer: change a little, show it, wait, repeat |
| 7–15 | The step function and `turtle.ontimer(animate, 50)`; the first call starts it |
| 15–19 | **Predict:** 50 → 200 milliseconds |
| 19–21 | Answer: fewer steps per second — slower |
| 21–26 | Two ways to double the speed: `speed` 5 → 10 or 50 → 25 milliseconds |
| 26–33 | Bounce: `dx = 5`, `setx(xcor() + dx)`, flip at ±200 |
| 33–37 | **Trace:** `dx` before and after passing the right border |
| 37–39 | Answer: 5 → −5; the next steps go left |
| 39–44 | Stop with space: the `running` flag |
| 44–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Timer_Starter.py`](Timer_Starter.py). Reference: [`Timer_Reference.py`](Timer_Reference.py).

## 45–52 — Warm-up: RecursionError

```python
# Warm-up: the rover should move 5 steps every 50 milliseconds.
# The program crashes with RecursionError. Why?
import turtle


def animate():
    turtle.forward(5)
    turtle.ontimer(animate(), 50)


turtle.shape("turtle")
animate()
turtle.done()
```

`animate()` calls itself immediately, again and again, without waiting. Fix: `turtle.ontimer(animate, 50)` — the name, like `onclick` and `onkey`.

## 52–66 — Task 1: `bounce()`

Move with `dx`; flip at −200 and 200.

## 66–80 — Task 2: stop and start

Space → `stop()`; `s` → `start()`, which starts a new chain only if the animation is stopped (otherwise two chains would run and the rover would move twice as fast).

## 80–83 — Document and save

Save As `G7_U9_M5_Timer_<Name>.py`.

## 83–90 — Exit check

1. What does `turtle.ontimer` do? (it schedules a function to run after some milliseconds)
2. What is the difference between the distance per step and the timer's time? (how far / how often)
3. How do we stop a chain of timer calls? (a state variable: stop scheduling the next step)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `ontimer` repeats by itself | Each step schedules the next one |
| `ontimer(animate(), 50)` | The name, no parentheses |
| A bigger number is faster | A bigger time is slower |
| Pressing `s` twice is harmless | It would start two chains — check `running` first |

---

# 8. Assessment Evidence (formative)

- Speed predictions and the `dx` trace
- The RecursionError explained
- Exit check
