# Unit 9.6 — Event-Driven Programming

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Mission Game — Keys, a Click and a Timer, and the Final Checkpoint (Mission 31)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (20 min guided practice, then 70 min project lab with the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit9_meeting6_event_game_final.pptx` (planning the game by events, the shared state, arrow moves that check a hit, the hit check and score, placing the target with a click, the countdown timer, blocking moves after the end, registering everything at the end, peer testing kept; the target is a red dot at `target_x, target_y` instead of a second turtle, a new target place is drawn with `random.randint` from Unit 7, and `+=` / `-=` replaced)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | why event-driven: event → listener → response; the event loop; first click | 45 / 45 |
| 9.2 | clicking the rover: `turtle.onclick`, x and y, state kept between clicks | 45 / 45 |
| 9.3 | clicking the screen: `turtle.onscreenclick`, `goto`, stamps, a click counter | 0 / 90 |
| 9.4 | keyboard: `turtle.listen`, `turtle.onkey`, four directions, borders | 45 / 45 |
| 9.5 | animation with a timer: `turtle.ontimer`, speed, bounce, stop and start | 45 / 45 |
| **9.6 (this)** | **final project: a game with keys, a click and a timer; unit checkpoint** | 0 / 90 |

This meeting closes Unit 9 — and the course — with its **checkpoint** (practical + theoretical), as the official assessment asks.

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.18–19) | Covered here |
|---|---|
| Keyboard events (practice) | ✅ Steps 1, 4 (45 practice) |
| Animation with a timer (practice) | ✅ Steps 3, 4 (45 practice) |
| Assessment (practical): a game or animation with event-driven programming | ✅ checkpoint A: the game |
| Assessment (theory): follow a problem and identify the event type it needs | ✅ checkpoint B |

With this meeting Unit 9 uses exactly its 540 official minutes (180 theory / 360 practice).

---

## 3. Lesson Goal

**A game is a set of events, each with its response, sharing a few variables: the score, the time and whether the game is running.**

---

## 4. Core Mental Models

| Event | Listener | Response | Changes |
|---|---|---|---|
| arrow key | `turtle.onkey` | `move_up()` … | the rover's place, `score` |
| click on the screen | `turtle.onscreenclick` | `place_target(x, y)` | `target_x`, `target_y` |
| one second passed | `turtle.ontimer` | `tick()` | `time_left`, `running` |

- **Order of the program:** variables → functions → register every listener → start the timer → `turtle.done()`.
- **After the game:** every move checks `running`.

---

# 5. First 20 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 31 |
| 1–5 | **Warm-up:** plan the game — a keyboard event, a mouse event and a timer event, each with its response |
| 5–7 | Answer (table above) |
| 7–12 | The skeleton: shared variables, `draw_target()`, `check_hit()` |
| 12–16 | `tick()`: one second less, schedule the next tick; at 0 → `running = False`, `Game over` |
| 16–19 | Registering at the end: four `onkey`, one `onscreenclick`, `tick()`, `turtle.done()` |
| 19–20 | Project steps and checkpoint |

---

# 6. Project Lab — 70 Minutes

Starter: [`Game_Starter.py`](Game_Starter.py) (Left and Right already work). Reference: [`Game_Reference.py`](Game_Reference.py).

## 20–58 — Checkpoint A (practical, in pairs, each student saves a copy)

1. **Step 1:** `move_up()` and `move_down()`, connected to the arrows; each move calls `check_hit()`.
2. **Step 2:** `place_target(x, y)` — a click on the screen moves the target.
3. **Step 3:** `tick()` — a 30-second countdown that ends with `Game over` and the score.
4. **Step 4:** after `Game over` the rover does not move (`if running:` in every move).

## 58–66 — Peer testing

Test another pair's game: every arrow, a click, a hit (the score grows, the target moves), the time running out, a move after the end.

## 66–78 — Checkpoint B (theory, on paper, no running)

1. Which event and which listener: pressing an arrow · clicking a point · every second?
2. `time_left = 3`, then `tick()` — what is printed?

```python
def tick():
    global time_left
    if time_left > 0:
        time_left = time_left - 1
        print("Time:", time_left)
        turtle.ontimer(tick, 1000)
    else:
        print("Game over")
```

3. What is wrong in `turtle.onkey(move_up(), "Up")`?
4. Why does `place_target(x, y)` have parameters and `move_up()` does not?

## 78–82 — Checkpoint B answers

1. `turtle.onkey` · `turtle.onscreenclick` · `turtle.ontimer`. 2. `Time: 2`, `Time: 1`, `Time: 0`, `Game over`. 3. The parentheses run the function now; pass the name. 4. A click sends x and y; a key sends nothing.

## 82–85 — Document and save

Save As `G7_U9_M6_Game_<Name>.py`.

## 85–90 — Exit check

1. Which event triggers each response in your game? (keyboard, mouse or timer)
2. Which information is kept between events? (score, time, running, the target's place)
3. What starts the timer chain? (the first call to `tick()`)

### Tool Note – Thonny
Click the Turtle window before using the arrows. The Shell shows `Score:` and `Time:` while the game runs.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Registering listeners inside a response | Register everything once, at the end of the program |
| `tick()` repeats by itself | It schedules itself only while time is left |
| The game stops by itself at 0 | Only if the moves check `running` |

---

# 8. Assessment Evidence

- **Checkpoint A** (practical): the game — keyboard, mouse and timer events with shared state
- **Checkpoint B** (theoretical): event type identification, timer trace, the parentheses bug, handler signatures
- Peer test and exit check
