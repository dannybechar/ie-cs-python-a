# Unit 6.1 — Strings

## Grade 7 / Python A · Lesson Strategy v1
### Topic: The Rover's Message — Strings, `len` and Indexes (Mission 15)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit6_meeting1_strings_and_indexes.pptx` and the ministry meeting 15 deck (second numbering row, negative indexes added in Phase 5; which values are strings, quotes, empty string, `len` predictions, index map of `Python`, `len(word) - 1`, `IndexError`, initials task, `banana` trace kept; the types-prediction slides shortened because Unit 3 already taught `type()`)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **6.1 (this)** | **`str` → quotes → empty string → `len` → indexes → `IndexError`** | 45 / 45 |
| 6.2 | `+` and `*` on strings vs numbers → `in` → a `for` loop over characters | 0 / 90 |
| 6.3 | slicing `[start:end:step]` → omitted bounds → step → reverse | 45 / 45 |
| 6.4 | string operations (`upper` … `replace`), Turtle `write`, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

From the Ministry program, Chapter 6 (python-a.pdf p.13–14):

| Official goal / concept | Covered here |
|---|---|
| 1. Assign string values to a variable | ✅ slides 4–5, all tasks |
| 5. Position index `[ ]`, the character at an index, and `len` | ✅ slides 5–11, Tasks 1–3 |
| Positions counted from the end (negative indexes, ministry meeting 15) | ✅ second row of the index map, Tasks 2–3 (Phase 5, U6-01) |
| Concepts: the `str` type, the empty string, access by position | ✅ |
| Teaching: `str` is a compound type with built-in operations | ✅ slide 4 ("a string is a sequence of characters") |

Official topic and minutes: "the `str` type" — 45 theory + 45 practice.

### Negative indexes (Phase 5)
Negative indexes are taught here as a **second numbering of the same string**. Teach `word[len(word) - 1]` first (it keeps the link to `len`), then show `word[-1]` as the short form of the same thing: index `-n` means `len(word) - n`. The ministry exam-prep items use them heavily (`string[-3]`, `title[-2]`, `text[-1]`).

### Terminology bridge
Say once: a function we write is called **פעולה** in the exam; `len` is also a "פעולה". We keep saying "פונקציה" in class and name both words on the glossary line of the brief.

### Not in this meeting
Operators (6.2), slicing (6.3) and string operations (6.4) come later. The ministry "hidden word from indexes" game (deck #5) and the folder 15.2 worksheet are in the take-home pack (`exercises/Strings_Extra_Practice.md`), zero class minutes.

---

## 3. Lesson Goal

**A string is a sequence of characters: `len` counts them, and the index of the first one is 0.**

---

## 4. Student-Facing Objectives

1. Tell a string from a number: anything in quotes is a `str`, even `"25"` and `""`.
2. Find the length of a string with `len` — spaces and signs count.
3. Read the character at an index; the first index is 0.
4. Reach the last character with `len(word) - 1`.
5. Explain `IndexError`: the index is outside the string.

---

## 5. Core Mental Models

- **Index map:** for `"Python"` the indexes are 0 1 2 3 4 5 — length 6, last index 5.
- **Length vs last index:** the last index is always `len(word) - 1`.
- **Two rows on the index map:** for `"Python"` the second row is -6 -5 -4 -3 -2 -1; `word[-1]` is the last character, and `-n` means `len(word) - n`.
- **Empty string `""`:** a valid string with 0 characters.
- **`input` returns a string** (from Unit 3), so `name[0]` works on what the user types.

---

# 6. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 15 |
| 1–5 | **Warm-up:** which are strings — `25`, `"25"`, `"Python"`, `""`? |
| 5–7 | Answer: `"25"`, `"Python"` and `""` are `str`; `25` is `int` |
| 7–13 | The `str` type: `city = "Haifa"`, `print(type(city))` → `<class 'str'>`; `"I'm learning Python"` |
| 13–19 | Empty string and `len`: `len("")` → 0, `len("Python")` → 6 |
| 19–22 | **Predict and answer:** `len("cat")`, `len("a b")`, `len("")`, `len("Hi!")` → 3, 3, 0, 3 — the space is a character |
| 22–28 | Indexes: `word[0]` → P, `word[1]` → y, `word[5]` → n; the index map; last index = length − 1 |
| 28–31 | **Predict:** `word[2]`, `word[4]`, `word[len(word) - 1]` |
| 31–33 | Answer: t, o, n |
| 33–39 | **Negative indexes:** the second row of the map (−6 … −1); `word[-1]` → n, `word[-2]` → o, `word[-1]` is the same character as `word[len(word) - 1]`; **predict** `word[-3]`, `word[-6]` → h, P |
| 39–42 | `IndexError`: `"cat"[3]` and `"cat"[-4]` — valid indexes are 0 to 2, or −1 to −3 |
| 42–44 | `input` returns a string: `name[0]`, `name[-1]` |
| 44–45 | Lab missions |

---

# 7. Second 45 Minutes — Lab

Starter: [`Strings_Starter.py`](../exercises/Strings_Starter.py). Reference: [`Strings_Reference.py`](solutions/Strings_Reference.py).

## 45–50 — Warm-up: why does it crash?

```python
# Warm-up: this should print the last letter. Why does it crash?
word = "rover"
print(word[len(word)])
```

Predict, run → `IndexError: string index out of range`. `len(word)` is 5, but the last index is 4. Fix: `word[len(word) - 1]` → `r`.

## 52–60 — Task 1: `initials()`

Read a first name and a last name; print the first letter of each. Test: `Dana`, `Levi` → `D L`.

## 60–72 — Task 2: `word_info()`

Read a word; print `Length:`, `First:` and `Last:` (with `len(word) - 1`). Then print `Last (short):` with `word[-1]` and check that both agree. Test `banana` → 6, `b`, `a`, `a`.

## 72–82 — Task 3 (challenge): `index_map()`

Read a word; print every index, the same position counted from the end (`i - len(word)`) and the character, using `for i in range(len(word)):` from Unit 5. Test `cat` → `0 -3 c`, `1 -2 a`, `2 -1 t`.

## 82–87 — Document, save and exit check

Save As `G7_U6_M1_Strings_<Name>.py`. Exit check (answers 87–90):

1. What is the length of `"a b"`? (3)
2. What is the first index? (0)
3. How do you reach the last index? (`len(text) - 1`)
4. What does `text[-1]` give? (the last character)

### Tool Note – Thonny
The error message names the line. Read the last line of the red message: `IndexError: string index out of range`.

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| The first index is 1 | It is 0 |
| The last index equals the length | It is `len(word) - 1` |
| A space is not a character | It is: `len("a b")` is 3 |
| `""` is not a string | It is the empty string, length 0 |
| `"25"` is a number | It is text; `int("25")` makes a number |
| `word[-1]` is the first character (or an error) | Negative numbers count from the end; `-1` is the last character |
| The second row starts at `-0` | `-1` is the last character; there is no `-0` |

---

# 9. Assessment Evidence (formative)

- Predictions (`len`, indexes)
- Warm-up crash explained and fixed
- Negative-index predictions (`word[-3]`, `word[-6]`)
- `word_info()` tested with `banana`
- Exit check
