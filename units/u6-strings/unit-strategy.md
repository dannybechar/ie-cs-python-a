# Unit 6 — Strings

**8h = 2 Theory + 6 Labs = 4 double meetings**
Source: [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) Unit 6. Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 4 meetings built and approved by the teacher. Inspired by the teacher's raw decks (`unit6_meeting1–4`).

## Official topics and hours

From the Chapter hours table in [`python-a.pdf`](../../docs/ministry-source/python-a.pdf) p.14. Minutes = hours × 45.
Status: ✅ approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry) | Theory h | Practice h | Minutes | Planned in | Status |
|---|---:|---:|---:|---|---|
| טיפוס נתונים str — the str type | 1 | 1 | 90 | 6.1 (45 T + 45 P) | ✅ |
| אופרטורים על מחרוזות — string operators | 0 | 2 | 90 | 6.2 (90 P) | ✅ |
| פעולת חיתוך — slicing | 1 | 3 | 180 | 6.3 (45 T + 45 P), 6.4 (90 P) | ✅ |
| **Total** | **2** | **6** | **360** | | |

Also listed for this chapter in the program overview (p.3–5) and goals (p.13):

- Empty string, `len`, indexes, including negative indexes (ministry meeting 15) → 6.1 ✅
- `+`, `*`, `in`, `not in`; `+` and `*` on numbers vs strings (teaching method 3); `str()`; building a new string in a loop → 6.2 ✅
- Key operations `find`, `upper`, `lower`, `count`, `startswith`, `endswith`, `isalpha`, `isnumeric` (taught as `isdigit`, same result on digits), `replace` (goal 7) → 6.4 ✅; also `index` and the optional parameters (ministry formula sheet) → 6.4 ✅
- Writing strings with Turtle (`write`) → 6.4, a 4-minute demo ✅
- Exam turtle dialect (`wn = turtle.Screen()`, `pen = turtle.Turtle()`, `wn.mainloop()`), drilled in Unit 2 → used in the 6.4 checkpoint ✅
- Not in this unit (ministry meeting 19 exam prep): the strings half is homework (`exercises/Strings_Extra_Practice.md`), the turtle half belongs to the turtle units

## Unit 6.1 — Knowledge + Lab: str, len and indexes
- `str`, quotes, the empty string (review of Unit 3 types).
- `len`; indexes from 0; the last index `len(word) - 1`; negative indexes (`word[-1]`, the second row of the index map); `IndexError`.

## Unit 6.2 — Lab + Lab: operators
- `+` and `*` on strings vs numbers; `str()`; `in` and `not in`.
- `for char in word`; counting with a counter; building a new string (`result = ""`, `result = result + char`; `+=` recognised).

## Unit 6.3 — Knowledge + Lab: slicing
- `[start:end:step]`, leaving out start or end, step, `[::-1]`, negative start/end (`[-3:]`, `[:-1]`, `[2:-2]`).

## Unit 6.4 — Lab + Lab: string operations + checkpoint
- the key operations, `index`, the optional parameters; `turtle.write` as a short demo and its exam-dialect form.
- checkpoint: practical (`text_report()`, `code_check()`) + theory on paper with the exam formula sheet (a six-row output table, operations, `str()`, operators).

### Scope decisions
- The meetings follow the teacher's raw decks (str → operators → slicing → operations). 6.1 and 6.3 carry the 90 theory minutes.
- The string operations have no separate line in the official hours table; they are practised in 6.4, inside the slicing practice hours.
- Negative indexes and negative slice bounds are taught (Phase 5, ministry meeting 15 and the exam-prep set use them). `len(word) - 1` is taught first and stays the link to `len`; `word[-1]` follows in 6.1 and `word[-3:]` in 6.3.
- Every meeting is full at 90 minutes; each addition is paid inside the same meeting (see the minute tables in the lesson notes): `banner()` is optional, the 6.1 `len` prediction and the 6.3 trace table are shorter, the `write` task is a demo, `palindrome()` is the first task to drop.
- `+=`: recognition only (introduced in 5.1); the long form `result = result + char` stays the main form. `not` and `not in` were taught in Unit 4 and are used here.
- Turtle: module-level `turtle.write` and `turtle.done()` stay the teaching style (approved deviation). The exam dialect (`wn`, `pen`, `wn.mainloop()`) is taught by the Unit 2 translation drill and used once in the 6.4 checkpoint.
- Terminology bridge: a function we write is a **פעולה** in the exam; `*` on strings is "כפל מחרוזות", `+` is "שרשור מחרוזות", the third slice part is "קפיצה (step)".
- `isdigit` is the main name (ministry exam-prep); `isnumeric` is the name in `python-a.pdf` and behaves the same on digits. Neither is on the exam formula sheet.
- The exam formula sheet (folder 19.2 = 20.5) is printed and used alone in checkpoint B. Commands that are not on it (`isalpha`, `isdigit`, `write`, `done`) are marked in the brief and not used in exam-style items without a definition.
- Ministry meeting 19 has no meeting of its own: the strings half is homework (`exercises/Strings_Extra_Practice.md`, section A) with a 10-minute review at the start of 7.1; the turtle half belongs to the turtle units.
- The practical assessment uses `input` rather than a function with a parameter (parameters come in Unit 8). Ministry items that ask to "return" are written with `print` until return-lite in 8.3 (approved deviation from the PDF, the PDF assesses functions that return nothing).

## Exit criteria
The student can access characters, slice a string, use key operations, and
solve a text-processing problem.

## Enrichment
- more complex text-processing tasks with the same tools.
