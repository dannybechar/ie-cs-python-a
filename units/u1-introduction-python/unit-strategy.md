# Unit 1 — Introduction to Python

**2h = 1 Theory + 1 Lab = one double meeting**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 1. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Ministry source:** the ministry's meeting 1 (`materials-m01-1-b6cfe9.md`, `classwork-m01-2-98da55.md`) opens with the algorithm concept, teaches `\n` and `\t`, and has one mandatory task (the business card). Its `def`/call part is in ministry meeting 4. See [`audit-u0-u1.md`](../../docs/ministry-program/audit-u0-u1.md) and [`traceability.md`](../../docs/ministry-program/traceability.md).

**Build status:** ✅ complete — [Unit 1.1 — Introduction to Python](README.md). Taught classes: the missed items are in [`teacher/L01-my-first-program-addendum-he.md`](teacher/L01-my-first-program-addendum-he.md).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.6. Minutes = hours × 45.
Status: ✅ built · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| הכרת סביבת העבודה — getting to know the working environment | 1 | 1 | 90 | m1 (install and tour: [Unit 0](../u0-environment-setup), outside the 60 h) | ✅ |
| **Total** | **1** | **1** | **90** | | |

Also listed for this chapter in the program overview (p.3–5):

- The algorithm concept (python-a.pdf goal 7) → m1 ✅ (added; addendum for taught classes)
- Simple output (`print`), with `\n` and `\t` → m1 ✅
- Compound output (הוראות פלט מורכבות — several values in one `print`) → [Unit 3.1](../u3-variables-io-arithmetic/teacher/L01-the-rovers-memory-notes.md) ✅
- Conventions: documentation, indentation → m1 ✅; file names → Unit 0 ✅
- Function (פונקציה / פעולה) structure and call; function with no parameters and no return value → m1 ✅

## 45 minutes — knowledge delivery
- What an algorithm is, and what a program is, as a sequence of instructions.
- Opening a file, running, saving — as the lab routine only. Installing the environment and learning its parts is done in [Unit 0](../u0-environment-setup).
- `print()`.
- Reading error messages (`NameError`, `SyntaxError`, `IndentationError`).
- Instruction count and the meaning of execution order.
- Comments using `#`; single or double quotes in strings.
- Escape sequences `\n` and `\t` (5 min, in the lab half of the timeline).
- A function (פונקציה, in the ministry's word פעולה) with no parameters and no return value.
- `define → call → execute`; a call before the `def` gives `NameError`.
- read → predict → run.

## 45 minutes — lab
Following the class deck ([`lessons/L01-my-first-program/slides-he.pdf`](lessons/L01-my-first-program/slides-he.pdf), slides 14–20):
1. Inside or outside? — indentation decides what belongs to the function.
2. The dragon story — trace the order when definitions and calls are mixed.
3. Launch challenge — turn `rocket.py` into a `launch()` function, step by step (steps 1–4 in class).
4. `\n` and `\t` — a 5-minute demo and task.
5. Exit mission — `introduce_me()`, after writing its steps in words, with a written output prediction.
6. Save under a new name.
Homework: launch challenge steps 5–6 and the business card (mandatory, ministry task 4).

## Exit criteria
The student can: `Open → Read → Predict → Modify → Run → Check → Comment → Save`.
