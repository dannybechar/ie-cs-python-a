# Unit 6.4 — Strings

## Grade 7 / Python A · Lesson Strategy v1
### Topic: Text Tools — String Operations, Turtle `write` and the Unit Checkpoint (Mission 18)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab with the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the teacher's draft `unit6_meeting4_string_methods_v3.pptx` (slicing warm-up, `upper`/`lower` and input cleanup, `count` and `find`, the `mississippi` prediction, the operations table, `startswith`/`endswith` file check, `isalpha`/`isnumeric`, `replace` phone task, Turtle `write`, the sentence report kept; the report became checkpoint A and a paper checkpoint B was added; Phase 5: negative indexes back in, `isdigit`, `index`, optional parameters, the exam turtle dialect in the checkpoint, checkpoint B re-cut as the ministry six-row table)  
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
| 7. Key operations: `find`, `upper`, `lower`, `count`, `startswith`, `endswith`, `isalpha`, `isnumeric` (taught as `isdigit`, see below), `replace` | ✅ slides 4–8, Task 1, checkpoint |
| Also on the exam formula sheet: `index`, and the optional parameters of `find`/`count`/`startswith`/`endswith`/`replace` (U6-06, U6-07) | ✅ guided 8–24, Task 1 |
| Teaching: writing with Turtle (`write`) | ✅ slide 9, a 4-minute demo (Task 2); `write` is a PDF goal, not on the exam sheet (U6-14) |
| Exam turtle dialect (`wn = turtle.Screen()`, `pen = turtle.Turtle()`, `wn.mainloop()`), drilled in Unit 2 and reused here (ruling 5) | ✅ Task 3 |
| Assessment (theory): a problem solved with string operators and operations | ✅ checkpoint B |
| Assessment (practical): code that reads a string and processes it | ✅ checkpoint A1 `text_report()`, A2 `code_check()` |

With this meeting Unit 6 uses exactly its 360 official minutes (90 theory / 270 practice).

### Source interpretation
The official hours table has no separate line for the string operations (goal 7); they are practised here inside the slicing practice hours, together with slicing in the warm-up and checkpoint B. The practical assessment asks for "a function that receives a string **or** code that reads a string"; functions with parameters come in Unit 8, so checkpoint A uses `input`.

### `isdigit` and `isnumeric`
`python-a.pdf` names `isnumeric`; the ministry deck and exam-prep use `isdigit`. On digits they give the same result. Teach `isdigit` as the main name and say "`isnumeric` is the name in the program booklet; it works the same on digits". Add `islower` / `isupper` in one line. None of the three is on the exam formula sheet, so an exam item that uses them defines them.

### Formula sheet (U6-11)
Print the strings and turtle sections of the ministry formula sheet (folder meeting 19.2 = 20.5) and let the students use **only that sheet** in checkpoint B. The brief's own cheat sheet marks the items that are not on the exam sheet (`isalpha`, `isdigit`, `write`). Say once: the sheet has more than we learn, so ignore lists and queue.

### Terminology bridge
A function we write is a **פעולה** in the exam; the string methods (`find`, `upper`…) are also called "פעולות". Say it once on the glossary line.

### Homework: exam-prep pack
There is no spare meeting for ministry meeting 19 (exam prep: strings and turtle). The strings half is homework: `exercises/Strings_Extra_Practice.md`, section A (ministry worksheet 19.4, questions 1–7 mandatory, 8–10 optional, with "print" instead of "return" until 8.3). The first 10 minutes of Unit 7.1 review it (the coordinator carries this into the Unit 7 notes).

### Deliberate exclusions
No `split`, `strip` or f-strings. `str(...)` was taught in 3.1 and 6.2; Turtle still writes `"Hello " + name.upper()`. `chr` / `ord` are in the take-home pack only.

---

## 3. Lesson Goal

**String operations answer questions about a text (`count`, `find`, `startswith`, `isnumeric`) or return a changed copy (`upper`, `lower`, `replace`) — the original never changes.**

---

## 4. Core Mental Models

- **Dot notation:** `text.upper()` — the operation belongs to the string.
- **A new copy:** `text.upper()` does not change `text` unless you assign it.
- **`find` gives the first index, or −1** when there is no match.
- **`index` is `find` that crashes:** `"banana".find("z")` is −1, `"banana".index("z")` is a `ValueError`.
- **Optional parameters:** a second number says where to start (`find("a", 2)`, `startswith("list", 4)`); `replace` takes a third number: how many replacements.
- **Yes/no operations** (`startswith`, `endswith`, `isalpha`, `isdigit`) return `True`/`False` and fit straight into `if`.

---

# 5. First 30 Minutes — Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: Mission 18 |
| 1–4 | **Warm-up:** `text = "Strings"` — `text[:3]`, `text[-3:]`, `text[::-1]`; answers `Str`, `ngs`, `sgnirtS` |
| 4–8 | `upper` / `lower`: `"PyThOn"` → `PYTHON`, `python`; `print(text)` still `PyThOn` |
| 8–14 | `count`, `find` and `index` on `banana`: 3, 2, 2, −1; `"banana".find("z")` is −1 but `"banana".index("z")` is an error; optional parameter: `find("a", 2)` → 3 |
| 14–17 | **Predict and answer:** `mississippi` — `count("s")`, `count("iss")`, `find("sip")`, `find("z")` → 4, 2, 6, −1 |
| 17–24 | Yes/no and replace table: `startswith`, `endswith` (with a start: `"playlist".startswith("list", 4)` → `True`), `isalpha`, `isdigit` (`isnumeric` in the booklet, `islower` / `isupper` in one line), `replace("a", "o", 2)` |
| 24–29 | Turtle `write` demo (4 min): `turtle.write("Hello " + name, align="center", font=("Arial", 24, "normal"))`; then one minute: the same line in the exam dialect on the board, `pen.write(...)` |
| 29–30 | Lab missions |

---

# 6. Lab — 60 Minutes

Starter: [`Methods_Starter.py`](../exercises/Methods_Starter.py). Reference: [`Methods_Reference.py`](solutions/Methods_Reference.py).

## 30–33 — Warm-up: why Rejected?

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

## 33–42 — Task 1: `file_check()` and `hide_phone()`

`file_check()` (5 min): `Python file` if the name ends with `.py`, also `.PY` (`lower()` first). `hide_phone()` (4 min): `050-123-4567` → `050*123*4567`; then predict `phone.replace("-", "*", 1)` → `050*123-4567`.

## 42–46 — Task 2: `name_card()` (Turtle demo)

Read a name and write `Hello` + the name in capitals in the middle of the screen, in blue, without the turtle shape. A short task, not graded.

## 46–50 — Task 3: the same card in the exam dialect

The teacher shows `name_card()` as the exam writes it (`wn = turtle.Screen()`, `pen = turtle.Turtle()`, `pen.write(...)`, `wn.mainloop()`); the students translate their own Task 2 using the Unit 2 translation drill (module-level `turtle.xxx(...)` becomes `pen.xxx(...)`, `turtle.done()` becomes `wn.mainloop()`).

## 50–68 — Checkpoint A (practical, alone)

- **A1 — `text_report()`:** read a sentence and print its length, how many `a` (capital or small), the index of the first space, whether it starts with `H`, its last character (`text[-1]`) and the sentence in capitals. Test `Hello Mars and Saturn` → 21, 3, 5, `True`, `n`, `HELLO MARS AND SATURN`.
- **A2 — `code_check()`:** a student code is valid when it is 6 digits (`isdigit()` and `len(code) == 6`). Tests: `123456` Valid, `12a456` Invalid, `12345` Invalid.

## 68–78 — Checkpoint B (theory, on paper, no running, with the exam formula sheet only)

`text = "rover-42"` — fill the table, one row each:

| command | output |
|---|---|
| `len(text)` | |
| `text[-1]` | |
| `text[:5]` | |
| `text[2:-2]` | |
| `text[::2]` | |
| `text.find("-")` | |

7. `text.count("r")`, `"Rover" in text`, `"-" not in text`
8. `"ab" + "c" * 3`, and `str(5) + "5"` compared with `5 + 5`

## 78–82 — Checkpoint B answers

`8`, `2`, `rover`, `ver-`, `rvr4`, `5`. 7. 2, `False`, `False`. 8. `abccc`; `55` and `10`.

## 82–84 — Document and save

Save As `G7_U6_M4_Methods_<Name>.py`.

## 84–87 — Exit check

1. What does `find` return when there is no match? (−1) And `index`? (an error)
2. What is the difference between `isalpha` and `isdigit`? (letters only / digits only)
3. Does `replace` change the original string? (no — it returns a new string)

## 87–90 — Homework hand-out

Hand out the exam-prep pack (`Strings_Extra_Practice.md`, section A) and the printed formula sheet; explain that Unit 7.1 opens with a 10-minute review.

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
| `"banana".index("z")` is −1 | `index` crashes; only `find` returns −1 |
| `isdigit` and `isnumeric` are different tools | Same result on digits; `isdigit` is the name in the ministry exam-prep |
| `write` needs `t = turtle.Turtle()` | Not in the course style: `turtle.write(...)`. The exam writes `pen.write(...)`, the same command on a named turtle |

---

# 8. Assessment Evidence

- Warm-up and `mississippi` predictions (formative)
- **Checkpoint A** (practical): `text_report()` and `code_check()`
- **Checkpoint B** (theoretical): the six-row output table (index, negative index, slice, step, `find`), operations, `str()` and operators on strings vs numbers
- Exit check
