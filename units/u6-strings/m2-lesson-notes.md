# Unit 6.2 — Strings

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Building Messages — `+`, `*`, `in` and a Loop over Characters (Mission 16)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (31 min guided practice, then 59 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit6_meeting2_string_operators.pptx` (`"Py" + "thon"` warm-up, full name with a space, `"-" * 10`, `in` and capital letters, the `A12B` prediction, the operators table, `for char in word`, counting `a` in `banana`, the password check kept; `count_a += 1` replaced by `count = count + 1`; a numbers-vs-strings comparison added, as the official teaching methods ask)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 6.1 | `str` → quotes → empty string → `len` → indexes → `IndexError` | 45 / 45 |
| **6.2 (this)** | **`+` and `*` on strings vs numbers → `in` → a `for` loop over characters** | 0 / 90 |
| 6.3 | slicing `[start:end:step]` → omitted bounds → step → reverse | 45 / 45 |
| 6.4 | string operations (`upper` … `replace`), Turtle `write`, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.13–14) | Covered here |
|---|---|
| 2. The concatenation operator `+` | ✅ slides 2–5, Task 1 |
| 3. The repetition operator `*` | ✅ slides 5–6, Task 1b |
| 4. The membership operator `in` | ✅ slides 6–8, Task 3 |
| Teaching: `+` and `*` depend on the types — on two numbers they add and multiply | ✅ slide 5, warm-up bug |
| Teaching: basic manipulations on strings | ✅ Tasks 1–3 |

Official topic and minutes: "operators on strings" — 90 practice.

### Deliberate exclusions
No `+=`. `count()` is not used yet (6.4) — the counter loop comes first, so students see what `count` does for them.

---

## 3. Lesson Goal

**The same operator does different work on different types: `5 + 5` is 10, but `"5" + "5"` is `"55"`.**

---

## 4. Core Mental Models

- **`+` joins, it does not add spaces:** `"Dana" + "Levi"` → `DanaLevi`; add `" "` yourself.
- **`*` repeats:** `"ha" * 3` → `hahaha`.
- **`in` asks a yes/no question** and returns `True` or `False`; capitals matter.
- **`for char in word`** gives one character per round, in order.

---

# 5. First 31 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 16 |
| 1–4 | **Warm-up:** `word = "Py" + "thon"` — what is printed, and what is `len(word)`? |
| 4–6 | Answer: `Python`, 6 |
| 6–10 | `+`: `first + " " + last` → `Dana Levi`; without the space → `DanaLevi` |
| 10–15 | Numbers vs strings table: `5 + 5`, `"5" + "5"`, `3 * 4`, `"3" * 4`, `"ha" * 3` |
| 15–20 | `*` and `in`: `"-" * 10`; `"science" in text` → `True`, `"art" in text` → `False` |
| 20–23 | **Predict:** `code = "A12B"` — `"12" in code`, `"a" in code`, `"B" in code`, `"" in code` |
| 23–25 | Answer: `True`, `False`, `True`, `True` |
| 25–30 | `for char in "code"` → `c o d e`, one character per round |
| 30–31 | Lab missions |

---

# 6. Lab — 59 Minutes

Starter: [`Operators_Starter.py`](Operators_Starter.py). Reference: [`Operators_Reference.py`](Operators_Reference.py).

## 31–37 — Warm-up: why 23?

```python
# Warm-up: 2 + 3 should be 5.
# Why does it print 23?
a = input("First number: ")
b = input("Second number: ")
print("Sum:", a + b)
```

`input` returns strings, so `+` joins them. Fix: `int(input(...))` → `Sum: 5`.

## 40–54 — Task 1: `greeting()` and `banner()`

`greeting()`: read first and last name → `Hello Dana Levi`. `banner()`: read a word and frame it:

```text
*********
* Rover *
*********
```

The frame line is `"*" * (len(word) + 4)`.

## 54–68 — Task 2: `count_letter()`

Read a word and a letter; count with a loop, a condition and a counter (`count = count + 1`). Test `banana`, `a` → `a appears 3 times`.

## 68–82 — Task 3: `password_check()`

Read a password; print `Contains !` and `Contains 7` for each rule that holds, and `Strong password` when both hold (`and` from 4.3). Tests: `hello!`, `abc7`, `go!7`.

## 82–85 — Document and save

Save As `G7_U6_M2_Operators_<Name>.py`.

## 85–90 — Exit check

1. What do `"5" + "5"` and `5 + 5` give? (`55` and `10`)
2. What does `in` return? (`True` or `False`)
3. What does `"ab" * 2` print? (`abab`)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `"5" + "5"` is 10 | Strings join: `55` |
| `+` adds a space | Only if you add `" "` |
| `"a" in "Apple"` is `True` | Capitals matter: `False` |
| `"3" * 4` is 12 | A string times a number repeats: `3333` |
| The loop gives indexes | `for char in word` gives the characters themselves |

---

# 8. Assessment Evidence (formative)

- `in` predictions
- Warm-up bug explained (types decide what `+` does)
- `count_letter()` tested with `banana`
- Exit check
