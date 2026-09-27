# Unit 6.4 — Strings

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Text Tools — String Operations, Turtle `write` and the Unit Checkpoint (Mission 18)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab with the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit6_meeting4_string_methods_v3.pptx` (slicing warm-up, `upper`/`lower` and input cleanup, `count` and `find`, the `mississippi` prediction, the operations table, `startswith`/`endswith` file check, `isalpha`/`isnumeric`, `replace` phone task, Turtle `write`, the sentence report kept; `text[-3:]` replaced by `text[len(text) - 3:]`, `t = turtle.Turtle()` replaced by the Unit 2 style; the report became checkpoint A and a paper checkpoint B was added)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 6.1 | `str` → quotes → empty string → `len` → indexes → `IndexError` | 45 / 45 |
| 6.2 | `+` and `*` on strings vs numbers → `in` → a `for` loop over characters | 0 / 90 |
| 6.3 | slicing `[start:end:step]` → omitted bounds → step → reverse | 45 / 45 |
| **6.4 (this)** | **string operations → Turtle `write` → checkpoint** | 0 / 90 |

This meeting closes Unit 6 and holds its **checkpoint** (practical + theoretical), as the official assessment asks.

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-a.pdf p.13–14) | Covered here |
|---|---|
| 7. Key operations: `find`, `upper`, `lower`, `count`, `startswith`, `endswith`, `isalpha`, `isnumeric`, `replace` | ✅ slides 4–8, Task 1, checkpoint |
| Teaching: writing with Turtle (`write`) | ✅ slide 9, Task 2 |
| Assessment (theory): a problem solved with string operators and operations | ✅ checkpoint B |
| Assessment (practical): code that reads a string and processes it | ✅ checkpoint A1 `text_report()`, A2 `code_check()` |

With this meeting Unit 6 uses exactly its 360 official minutes (90 theory / 270 practice).

### Source interpretation
The official hours table has no separate line for the string operations (goal 7); they are practised here inside the slicing practice hours, together with slicing in the warm-up and checkpoint B. The practical assessment asks for "a function that receives a string **or** code that reads a string"; functions with parameters come in Unit 8, so checkpoint A uses `input`.

### Deliberate exclusions
No negative indexes, no `split`, `strip` or f-strings. `str(...)` is not needed: Turtle writes `"Hello " + name.upper()`.

---

## 3. Lesson Goal

**String operations answer questions about a text (`count`, `find`, `startswith`, `isnumeric`) or return a changed copy (`upper`, `lower`, `replace`) — the original never changes.**

---

## 4. Core Mental Models

- **Dot notation:** `text.upper()` — the operation belongs to the string.
- **A new copy:** `text.upper()` does not change `text` unless you assign it.
- **`find` gives the first index, or −1** when there is no match.
- **Yes/no operations** (`startswith`, `endswith`, `isalpha`, `isnumeric`) return `True`/`False` and fit straight into `if`.

---

# 5. First 30 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 18 |
| 1–4 | **Warm-up:** `text = "Strings"` — `text[:3]`, `text[len(text) - 3:]`, `text[::-1]` |
| 4–6 | Answer: `Str`, `ngs`, `sgnirtS` |
| 6–10 | `upper` / `lower`: `"PyThOn"` → `PYTHON`, `python`; `print(text)` still `PyThOn` |
| 10–15 | `count` / `find` on `banana`: 3, 2, 2, −1 |
| 15–18 | **Predict:** `mississippi` — `count("s")`, `count("iss")`, `find("sip")`, `find("z")` |
| 18–20 | Answer: 4, 2, 6, −1 |
| 20–25 | Yes/no and replace table: `startswith`, `endswith`, `isalpha`, `isnumeric`, `replace` |
| 25–29 | Turtle `write`: `turtle.write("Hello " + name, align="center", font=("Arial", 24, "normal"))` |
| 29–30 | Lab missions |

---

# 6. Lab — 60 Minutes

Starter: [`Methods_Starter.py`](Methods_Starter.py). Reference: [`Methods_Reference.py`](Methods_Reference.py).

## 30–34 — Warm-up: why Rejected?

```python
# Warm-up: the user types Yes,
# but the program says Rejected. Why?
answer = input("Answer: ")
if answer == "yes":
    print("Accepted")
else:
    print("Rejected")
```

`"Yes" == "yes"` is `False` (capitals matter, from 4.1). Fix: `input("Answer: ").lower()`.

## 36–46 — Task 1: `file_check()` and `hide_phone()`

`file_check()`: `Python file` if the name ends with `.py`, also `.PY` (`lower()` first). `hide_phone()`: `050-123-4567` → `050*123*4567`.

## 46–54 — Task 2: `name_card()` (Turtle)

Read a name and write `Hello` + the name in capitals in the middle of the screen, in blue, without the turtle shape.

## 54–72 — Checkpoint A (practical, alone)

- **A1 — `text_report()`:** read a sentence and print its length, how many `a` (capital or small), the index of the first space, whether it starts with `H`, and the sentence in capitals. Test `Hello Mars and Saturn` → 21, 3, 5, `True`, `HELLO MARS AND SATURN`.
- **A2 — `code_check()`:** a student code is valid when it is 6 digits (`isnumeric()` and `len(code) == 6`). Tests: `123456` Valid, `12a456` Invalid, `12345` Invalid.

## 72–82 — Checkpoint B (theory, on paper, no running)

`text = "rover-42"`

1. `len(text)`, `text[0]`, `text[len(text) - 1]`
2. `text[:5]`, `text[6:]`, `text[::2]`
3. `text.find("-")`, `text.count("r")`, `"Rover" in text`
4. `"ab" + "c" * 3`, and `"5" + "5"` compared with `5 + 5`

## 82–85 — Checkpoint B answers

1. 8, `r`, `2`. 2. `rover`, `42`, `rvr4`. 3. 5, 2, `False`. 4. `abccc`; `55` and `10`.

## 85–87 — Document and save

Save As `G7_U6_M4_Methods_<Name>.py`.

## 87–90 — Exit check

1. What does `find` return when there is no match? (−1)
2. What is the difference between `isalpha` and `isnumeric`? (letters only / digits only)
3. Does `replace` change the original string? (no — it returns a new string)

### Tool Note – Thonny
Close the Turtle window before the next run.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `text.upper()` changes `text` | It returns a copy; assign it if you need it |
| `find` returns `False` when missing | It returns −1 |
| `count("a")` counts `A` too | Capitals matter — use `lower()` first |
| `"A12".isalpha()` is `True` | Every character must be a letter |
| `write` needs `t = turtle.Turtle()` | The course writes `turtle.write(...)` |

---

# 8. Assessment Evidence

- Warm-up and `mississippi` predictions (formative)
- **Checkpoint A** (practical): `text_report()` and `code_check()`
- **Checkpoint B** (theoretical): index, slice, operations, operators on strings vs numbers
- Exit check
