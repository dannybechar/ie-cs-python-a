# Unit 6.3 — Strings

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Cutting the Message — Slicing (Mission 17)

**Status:** Draft, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit6_meeting3_slicing_v3.pptx` (`word[2]` vs `word[2:5]`, the `computer` examples table, predictions on `Python` and `abcdefgh`, omitted bounds, step and reverse, the trace table, first/last three letters, the `word[1:4]` fix-it, palindrome kept; a hidden-message task added for the step)  
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
| 6. Slicing by range: start, end, step | ✅ slides 2–11, Tasks 1–4 |
| Concept: `[start:end:step]` | ✅ |
| Teaching: basic manipulations on strings | ✅ Tasks 2–4 |

Official topic and minutes: "slicing" — 45 theory + 45 of its 135 practice minutes (the rest in 6.4).

### Link to Unit 5
Slicing follows the same rule as `range(start, stop, step)`: start included, end not included. Say it out loud — students already know it.

### Deliberate exclusions
No negative start/end indexes (`word[-3:]`); the last three letters are `word[len(word) - 3:]`. The only negative number is the step `-1` (and `-2`) for reading backwards.

---

## 3. Lesson Goal

**A slice takes the characters from start up to — but not including — end, jumping by step.**

---

## 4. Core Mental Models

- **Like `range`:** `word[1:4]` takes indexes 1, 2, 3.
- **Missing start = from the beginning; missing end = to the end.**
- **Step 2 = every second character; step −1 = backwards.**
- **A slice is a new string;** the original does not change.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 17 |
| 1–5 | **Warm-up:** `word = "computer"` — what is the difference between `word[2]` and `word[2:5]`? |
| 5–7 | Answer: `m` (one character) vs `mpu` (a new string) |
| 7–14 | `text[start:end:step]`; the `computer` table: `[0:3]` com, `[3:6]` put, `[1:7:2]` opt |
| 14–18 | **Predict:** `word = "Python"` — `word[0:2]`, `word[2:6]`, `word[1:5]` |
| 18–20 | Answer: `Py`, `thon`, `ytho` |
| 20–26 | Omitted bounds: `word[:3]` com, `word[3:]` puter, `word[:]` computer |
| 26–32 | Step: `"0123456789"[0:10:2]` 02468, `[1:10:2]` 13579; `"Python"[::-1]` nohtyP |
| 32–36 | **Predict:** `text = "abcdefgh"` — `text[::2]`, `text[1::3]`, `text[::-2]` |
| 36–38 | Answer: `aceg`, `beh`, `hfdb` |
| 38–44 | Trace table: start / end / step / result for four slices of `abcdefgh` |
| 44–45 | Lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Slicing_Starter.py`](Slicing_Starter.py). Reference: [`Slicing_Reference.py`](Slicing_Reference.py).

## 45–52 — Task 1: fix the slice

```python
# Task 1: this should print the letters
# at indexes 1 to 4 (bcde).
# Fix the slice.
word = "abcdefgh"
print(word[1:4])
```

It prints `bcd`: end is not included. Fix: `word[1:5]` → `bcde`.

## 52–62 — Task 2: `ends()`

Read a word; print its first three and last three letters. Test `planet` → `pla`, `net`.

## 62–72 — Task 3: `decode()`

`secret = "xPxyxtxhxoxn"` — the message hides in every second letter, starting at index 1. `secret[1::2]` → `Python`.

## 72–82 — Task 4: `palindrome()`

Read a word; compare it with `word[::-1]`. Tests: `level` → `Palindrome`, `rover` → `Not palindrome`.

## 82–85 — Document and save

Save As `G7_U6_M3_Slicing_<Name>.py`.

## 85–90 — Exit check

1. Is end included in a slice? (no)
2. What does `word[:3]` take? (indexes 0 to 2 — the first three characters)
3. How do you reverse a string? (`word[::-1]`)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `word[1:4]` includes index 4 | End is not included — like `range` |
| `word[3:]` starts at the 3rd letter | It starts at index 3, the 4th letter |
| A slice changes the word | It makes a new string |
| `word[::-1]` needs start and end | Omitted bounds work in both directions |

---

# 8. Assessment Evidence (formative)

- Slice predictions and the trace table
- Task 1 fix explained with "end is not included"
- `palindrome()` tested with `level` and `rover`
- Exit check
