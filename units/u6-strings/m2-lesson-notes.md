# Unit 6.2 — Strings

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Building Messages — `+`, `*`, `in` and a Loop over Characters (Mission 16)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (31 min guided practice, then 59 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit6_meeting2_string_operators.pptx` (`"Py" + "thon"` warm-up, full name with a space, `"-" * 10`, `in` and capital letters, the `A12B` prediction, the operators table, `for char in word`, counting `a` in `banana`, the password check kept; `count_a += 1` replaced by `count = count + 1`; a numbers-vs-strings comparison added, as the official teaching methods ask; Phase 5 added `str()`, `not in`, building a new string in a loop (ministry meeting 19) and made `banner()` optional)  
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
| 3. The repetition operator `*` | ✅ slides 5–6, Task 3 `stars()`, optional `banner()` |
| 4. The membership operator `in` | ✅ slides 6–8, Tasks 4–5 |
| Teaching: `+` and `*` depend on the types — on two numbers they add and multiply | ✅ slide 5, warm-up bug |
| Teaching: basic manipulations on strings | ✅ Tasks 1–5 |
| Building a new string in a loop (`result = ""`, then `result = result + char`) — the main pattern of the ministry exam-prep questions (U6-02) | ✅ guided 25–30, Tasks 1, 3 |
| `str()` to turn a number into text (`str(5) + "5"`, `len(str(n))`) — the formula sheet lists it (U6-04) | ✅ guided 8–14, exit check |
| `not in` and `not` as "the opposite" (taught in Unit 4, used here) (U6-08) | ✅ guided 14–18, Task 4 |

Official topic and minutes: "operators on strings" — 90 practice.

### `+=` (Phase 5 ruling)
`+=` was introduced as recognition in 5.1 (`x += 1` means `x = x + 1`). Here say it once when the string is built: `result += char` means `result = result + char`. Students keep writing the long form; they must be able to read the short one, because ministry exam items use it.

### Terminology bridge
"שכפול" for `*` is called **כפל מחרוזות** in the exam, `+` is **שרשור מחרוזות**; a function we write is a **פעולה** in the exam. The brief carries one glossary line.

### Deliberate exclusions
`count()` is not used yet (6.4) — the counter loop comes first, so students see what `count` does for them. `banner()` is now an optional challenge (zero class minutes). The skip-string (`range(0, len(text), 3)`, ministry deck #3), the e-mail variants and the ministry worksheet 19.4 are in the take-home pack (`exercises/Strings_Extra_Practice.md`).

---

## 3. Lesson Goal

**The same operator does different work on different types: `5 + 5` is 10, but `"5" + "5"` is `"55"`.**

---

## 4. Core Mental Models

- **`+` joins, it does not add spaces:** `"Dana" + "Levi"` → `DanaLevi`; add `" "` yourself.
- **`*` repeats:** `"ha" * 3` → `hahaha`.
- **`in` asks a yes/no question** and returns `True` or `False`; capitals matter.
- **`for char in word`** gives one character per round, in order.
- **Build a string like a counter:** a counter starts at `0` and adds; a text starts at `""` and joins: `result = result + char`. The empty string is "nothing yet".
- **`not in` and `not`** turn the answer around: `"@" not in mail` is `True` when there is no `@`.

---

# 5. First 31 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 16 |
| 1–4 | **Warm-up:** `word = "Py" + "thon"` — what is printed, and what is `len(word)`? |
| 4–5 | Answer: `Python`, 6 |
| 5–8 | `+`: `first + " " + last` → `Dana Levi`; without the space → `DanaLevi` |
| 8–14 | Numbers vs strings table: `5 + 5`, `"5" + "5"`, `3 * 4`, `"3" * 4`, `"ha" * 3` — and `str()`: `str(5) + "5"` → `55`, `len(str(2026))` → 4 |
| 14–18 | `*`, `in` and `not in`: `"-" * 10`; `"science" in text` → `True`, `"art" in text` → `False`, `"art" not in text` → `True` |
| 18–21 | **Predict and answer:** `code = "A12B"` — `"12" in code`, `"a" in code`, `"B" in code`, `"" in code` → `True`, `False`, `True`, `True` |
| 21–25 | `for char in "code"` → `c o d e`, one character per round |
| 25–30 | **Building a string:** `result = ""`, then `for char in text:` `result = result + char`; keep only some characters (skip the spaces); compare with the counter that starts at `0`; say `result += char` means the same |
| 30–31 | Lab missions |

---

# 6. Lab — 59 Minutes

Starter: [`Operators_Starter.py`](exercises/Operators_Starter.py). Reference: [`Operators_Reference.py`](solutions/Operators_Reference.py).

## 31–36 — Warm-up: why 23?

```python
# Warm-up: 2 + 3 should be 5.
# Why does it print 23?
a = input("First number: ")
b = input("Second number: ")
print("Sum:", a + b)
```

`input` returns strings, so `+` joins them. Fix: `int(input(...))` → `Sum: 5`.

## 36–47 — Task 1: `greeting()` and `remove_spaces()`

`greeting()` (3 min): read first and last name → `Hello Dana Levi`. `remove_spaces()` (8 min): read a sentence and build a new one without the spaces (`result = ""`, `for char in text`, keep the character when it is not a space). Test `a b  c` → `abc`.

## 47–56 — Task 2: `count_letter()`

Read a word and a letter; count with a loop, a condition and a counter (`count = count + 1`). Test `banana`, `a` → `a appears 3 times`.

## 56–66 — Task 3: `stars()`

Read a word and build a new string: every letter at an even index becomes `*`, the others stay. Use `for i in range(len(text)):`, `i % 2 == 0` (from 3.2) and `text[i]`. Test `rover` → `*o*e*`.

## 66–75 — Task 4: `check_mail()`

Read an address; it is valid when it has no space and it has an `@` (`" " not in mail and "@" in mail`). Tests: `dana@mail.com` Valid, `dana mail.com` Invalid, `danamail.com` Invalid.

## 75–83 — Task 5: `password_check()`

Read a password; print `Contains !` and `Contains 7` for each rule that holds, and `Strong password` when both hold (`and` from 4.3). Tests: `hello!`, `abc7`, `go!7`.

*Optional challenges (zero class minutes, for fast finishers or homework):* `banner()` — frame a word in stars (`"*" * (len(word) + 4)`); `every_third()` — build a string from every third letter with `range(0, len(text), 3)`.

## 83–85 — Document and save

Save As `G7_U6_M2_Operators_<Name>.py`.

## 85–90 — Exit check

1. What do `"5" + "5"` and `5 + 5` give? (`55` and `10`)
2. What does `in` return? (`True` or `False`)
3. What does `"ab" * 2` print? (`abab`)
4. What does `str(5) + "5"` give? (`55`)
5. A loop builds a text; what is the starting value of `result`? (`""`)

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `"5" + "5"` is 10 | Strings join: `55` |
| `+` adds a space | Only if you add `" "` |
| `"a" in "Apple"` is `True` | Capitals matter: `False` |
| `"3" * 4` is 12 | A string times a number repeats: `3333` |
| The loop gives indexes | `for char in word` gives the characters themselves |
| `result = ""` then `result` stays empty | The loop must assign: `result = result + char` |
| `result` starts at `0` like a counter | A text starts at `""`; `0 + "a"` is an error |
| `"@" not in mail` means the mail has an `@` | `not in` is the opposite: no `@` |
| `str(5)` changes the number 5 | It returns a new string; `5` is still a number |

---

# 8. Assessment Evidence (formative)

- `in` predictions
- Warm-up bug explained (types decide what `+` does)
- `remove_spaces()` and `stars()` tested (string built in a loop)
- `count_letter()` tested with `banana`
- Exit check
