# Unit 6.3 — Strings

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Cutting the Message — Slicing (Mission 17)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit6_meeting3_slicing_v3.pptx` (`word[2]` vs `word[2:5]`, the `computer` examples table, predictions on `Python` and `abcdefgh`, omitted bounds, step and reverse, the trace table, first/last three letters, the `word[1:4]` fix-it, palindrome kept, now optional; a hidden-message task added for the step; Phase 5 added negative bounds from the ministry meeting 15 deck and exam-prep items)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 6.1 | `str` → quotes → empty string → `len` → indexes → `IndexError` | 45 / 45 |
| 6.2 | `+` and `*` on strings vs numbers → `in` → a `for` loop over characters | 0 / 90 |
| **6.3 (this)** | **slicing `[start:end:step]` → omitted bounds → step → reverse** | 45 / 45 |
| 6.4 | string operations (`upper` … `replace`), Turtle `write`, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.13–14) | Covered here |
|---|---|
| 6. Slicing by range: start, end, step | ✅ slides 2–11, Tasks 1–5 |
| Negative start/end (`word[-3:]`, `word[:-1]`, `word[2:-2]`) — ministry meeting 15 and the exam-prep set (U6-01) | ✅ guided 34–40, Tasks 2 and 4 |
| Concept: `[start:end:step]` | ✅ |
| Teaching: basic manipulations on strings | ✅ Tasks 2–4 |

Official topic and minutes: "slicing" — 45 theory + 45 of its 135 practice minutes (the rest in 6.4).

### Link to Unit 5
Slicing follows the same rule as `range(start, stop, step)`: start included, end not included. Say it out loud — students already know it.

### Negative bounds (Phase 5)
Negative start/end are taught as the same rule as negative indexes from 6.1: `-n` means `len(word) - n`, so `word[-3:]` equals `word[len(word) - 3:]` (show both once). The step `-1` and the bound `-1` are different things — name the difference.

### Terminology bridge
The exam calls the three parts **start — מאיפה, end — עד איפה (לא כולל), step — קפיצה**. Use "קפיצה (step)" in class.

### Not in this meeting
The ministry "hidden word from indexes" class game (deck #5) and the 15.2 slicing worksheet items are in the take-home pack (`exercises/Strings_Extra_Practice.md`).

---

## 3. Lesson Goal

**A slice takes the characters from start up to — but not including — end, jumping by step.**

---

## 4. Core Mental Models

- **Like `range`:** `word[1:4]` takes indexes 1, 2, 3.
- **Missing start = from the beginning; missing end = to the end.**
- **Step 2 = every second character; step −1 = backwards.**
- **A slice is a new string;** the original does not change.
- **Negative bounds count from the end:** `word[-3:]` is the last three characters, `word[:-1]` is everything except the last, `word[2:-2]` cuts two from each side.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 17 |
| 1–5 | **Warm-up:** `word = "computer"` — what is the difference between `word[2]` and `word[2:5]`? |
| 5–7 | Answer: `m` (one character) vs `mpu` (a new string) |
| 7–14 | `text[start:end:step]`; the `computer` table: `[0:3]` com, `[3:6]` put, `[1:7:2]` opt |
| 14–17 | **Predict:** `word = "Python"` — `word[0:2]`, `word[2:6]`, `word[1:5]` |
| 17–18 | Answer: `Py`, `thon`, `ytho` |
| 18–22 | Omitted bounds: `word[:3]` com, `word[3:]` puter, `word[:]` computer |
| 22–28 | Step: `"0123456789"[0:10:2]` 02468, `[1:10:2]` 13579; `"Python"[::-1]` nohtyP |
| 28–32 | **Predict:** `text = "abcdefgh"` — `text[::2]`, `text[1::3]`, `text[::-2]` |
| 32–34 | Answer: `aceg`, `beh`, `hfdb` |
| 34–40 | **Negative bounds:** `text[-3:]` fgh, `text[:-1]` abcdefg, `text[2:-2]` cdef, `text[-4:-1]` efg; `-n` means `len(text) - n`; **predict** `text[-2:]`, `text[1:-1]` → gh, bcdefg |
| 40–44 | Trace table: start / end / step / result for three slices of `abcdefgh` (one has a negative bound) |
| 44–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Slicing_Starter.py`](exercises/Slicing_Starter.py). Reference: [`Slicing_Reference.py`](solutions/Slicing_Reference.py).

## 45–50 — Task 1: fix the slice

```python
# Task 1: this should print the letters
# at indexes 1 to 4 (bcde).
# Fix the slice.
word = "abcdefgh"
print(word[1:4])
```

It prints `bcd`: end is not included. Fix: `word[1:5]` → `bcde`.

## 50–60 — Task 2: `ends()`

Read a word; print its first three and last three letters, the last three with `word[-3:]`. Test `planet` → `pla`, `net`.

## 60–68 — Task 3: `decode()`

`secret = "xPxyxtxhxoxn"` — the message hides in every second letter, starting at index 1. `secret[1::2]` → `Python`.

## 68–76 — Task 4: `trim()`

Read a word; print it without its first and last character (`word[1:-1]`). Test `planet` → `lane`; `[x]` → empty line.

## 76–82 — Task 5 (optional): `palindrome()`

Read a word; compare it with `word[::-1]`. Tests: `level` → `Palindrome`, `rover` → `Not palindrome`. This is the first task to drop when time is short; the minutes then go to Tasks 2–4.

## 82–85 — Document and save

Save As `G7_U6_M3_Slicing_<Name>.py`.

## 85–90 — Exit check

1. Is end included in a slice? (no)
2. What does `word[:3]` take? (indexes 0 to 2 — the first three characters)
3. How do you reverse a string? (`word[::-1]`)
4. What does `word[-3:]` take? (the last three characters)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `word[1:4]` includes index 4 | End is not included — like `range` |
| `word[3:]` starts at the 3rd letter | It starts at index 3, the 4th letter |
| A slice changes the word | It makes a new string |
| `word[::-1]` needs start and end | Omitted bounds work in both directions |
| `word[-3:]` takes three characters from the start | A negative bound counts from the end: the last three |
| `word[:-1]` is empty or reversed | It stops before the last character: everything except the last |
| the step `-1` and the bound `-1` are the same | Different roles: a step is the direction and jump, a bound is a position |

---

# 8. Assessment Evidence (formative)

- Slice predictions and the trace table
- Task 1 fix explained with "end is not included"
- `trim()` and `ends()` with negative bounds
- `palindrome()` (optional) tested with `level` and `rover`
- Exit check
