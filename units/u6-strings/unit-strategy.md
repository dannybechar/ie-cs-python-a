# Unit 6 — Strings

**8h = 2 Theory + 6 Labs = 4 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 6. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 complete — all 4 meetings built, awaiting approval. Inspired by the teacher's raw decks (`unit6_meeting1–4`).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.14. Minutes = hours × 45.
Status: ✅ approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| טיפוס נתונים str — the str type | 1 | 1 | 90 | 6.1 (45 T + 45 P) | 🔶 |
| אופרטורים על מחרוזות — string operators | 0 | 2 | 90 | 6.2 (90 P) | 🔶 |
| פעולת חיתוך — slicing | 1 | 3 | 180 | 6.3 (45 T + 45 P), 6.4 (90 P) | 🔶 |
| **Total** | **2** | **6** | **360** | | |

Also listed for this chapter in the program overview (p.3–5) and goals (p.13):

- Empty string, `len`, indexes → 6.1 🔶
- `+`, `*`, `in`; `+` and `*` on numbers vs strings (teaching method 3) → 6.2 🔶
- Key operations `find`, `upper`, `lower`, `count`, `startswith`, `endswith`, `isalpha`, `isnumeric`, `replace` (goal 7) → 6.4 🔶
- Writing strings with Turtle (`write`) → 6.4 🔶

## Unit 6.1 — Knowledge + Lab: str, len and indexes
- `str`, quotes, the empty string (review of Unit 3 types).
- `len`; indexes from 0; the last index `len(word) - 1`; `IndexError`.

## Unit 6.2 — Lab + Lab: operators
- `+` and `*` on strings vs numbers; `in`.
- `for char in word`; counting with a counter.

## Unit 6.3 — Knowledge + Lab: slicing
- `[start:end:step]`, leaving out start or end, step, `[::-1]`.

## Unit 6.4 — Lab + Lab: string operations + checkpoint
- the nine key operations; `turtle.write`.
- checkpoint: practical (`text_report()`, `code_check()`) + theory on paper (index, slice, operations, operators).

### Scope decisions
- The meetings follow the teacher's raw decks (str → operators → slicing → operations). 6.1 and 6.3 carry the 90 theory minutes.
- The string operations have no separate line in the official hours table; they are practised in 6.4, inside the slicing practice hours.
- No negative indexes: the last character is `word[len(word) - 1]`, the last three `word[len(word) - 3:]`. Only the step may be negative.
- No `+=`; Turtle stays in the Unit 2 style (`turtle.write`, never `t = turtle.Turtle()`).
- The practical assessment uses `input` rather than a function with a parameter (parameters come in Unit 8).

## Exit criteria
The student can access characters, slice a string, use key operations, and
solve a text-processing problem.

## Enrichment
- more complex text-processing tasks with the same tools.
