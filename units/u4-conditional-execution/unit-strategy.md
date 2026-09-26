# Unit 4 — Conditional Execution

**6h = 2 Theory + 4 Labs = 3 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 4. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ⚠️ partial — Meeting 1 built (🔶 awaiting approval); Meetings 2–3 planned. Inspired by the teacher's raw decks (`chapter4_session1–3`).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.10. Minutes = hours × 45.
Status: ✅ built · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| ביטויים בוליאניים — boolean expressions | 1 | 2 | 135 | m1 (45 T + 45 P), m3 (45 P) | 🔶 m1 built |
| משפטי תנאי — conditional statements | 1 | 2 | 135 | m2 (45 T + 45 P), m3 (45 P) | ⏳ |
| **Total** | **2** | **4** | **270** | | |

Also listed for this chapter in the program overview (p.3–5):

- Nested conditionals (one level) → m3 ⏳
- Conditions using Turtle → m3 ⏳

## Meeting 1 — Knowledge + Lab: the rover's sensors
- comparison operators `== != > < >= <=`, `=` vs `==`.
- results are `bool`; storing them in variables; string equality.
- `and`, `or` and their truth tables; a condition from a truth table.
- order: arithmetic → comparison → `and` → `or`.
- lab: trace, sensor check, fix `input` vs number, truth tables both ways.

## Meeting 2 — Knowledge + Lab: if and if/else
- `if`: condition, colon, indented body; a false condition skips the body.
- `if/else`: exactly one branch runs.
- even/odd with `%`, pass/fail, the `>=` boundary.
- simple input filter: valid / invalid (no re-asking).
- common errors: `=` in a condition, missing colon, missing indentation.

## Meeting 3 — Lab + Lab: compound conditions, nesting, Turtle
- `and` / `or` inside `if`.
- one-level nesting; when a compound condition can replace it.
- conditions with Turtle (module-level `turtle.*` calls only).
- integrated problems + practical and tracing checkpoint.

### Scope decisions
- `elif` is **not** in the official concept list (simple condition, one-level nesting) — optional extension only.
- `not` is not in the official concept list — not taught.
- Turtle stays with the Unit 2 style (`turtle.forward`, `turtle.left`); no `t = turtle.Turtle()` or `setheading`.

## Exit criteria
The student can formulate a condition, trace which branch was chosen, and
write a solution with a simple/compound condition.

## Enrichment
- more demanding decision problems without introducing new syntax.
