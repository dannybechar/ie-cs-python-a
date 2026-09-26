# G7 Unit 1 Lesson Strategy v4

## Grade 7 / Python A
### Unit 1 — Introduction to Python

**Status:** Approved baseline after external review  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Current tool assumption:** Thonny  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Unit Scope

Core content only:

- the open → run → save as routine, using the environment set up in [Unit 0](../u0-environment-setup) (installing and touring the tool is not repeated here)
- sequential instructions
- `print()`
- comments using `#`
- function with no parameters and no return value
- define → call → execute
- predict output before running

Do not introduce variables, `input()`, arithmetic, conditions, loops, parameters, `return`, formal scope, or advanced IDE features.

---

## 2. Lesson Goal

By the end of the lesson, students should be able to use this workflow independently:

**Open → Read → Predict → Run → Check → Modify → Comment → Save**

Thonny is the current implementation tool, not the learning goal.

---

## 3. Student-Facing Objectives

Students should be able to:

1. Explain that a program is a sequence of instructions.
2. Predict the output of short `print()` sequences.
3. Explain that execution order matters.
4. Use `#` to add a comment.
5. Distinguish defining a function from calling it.
6. Write/use a simple no-parameter, no-return function.
7. Open, run, modify, and save a Python file.
8. Compare predicted output with actual output and explain a mismatch.

---

## 4. Core Model

### Sequential execution
Python executes instructions in order.

### Output
`print()` displays output.

### Comments
A line beginning with `#` is documentation for people reading the code and is not executed as a Python instruction.

### Functions
Use only:

**Define → Call → Execute**

- Define: describe what the function does.
- Call: ask Python to perform it.
- Execute: the instructions inside the function run.

Beginner-safe indentation wording:

> **All lines that belong to the function are indented and line up the same way.**

Do not teach parameters, arguments, return values, scope, or formal modularity here.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

## 0–5 min — Hook: Predict Before Run

```python
print("Good morning")
print("Welcome to Python")
print("Ready!")
```

Ask: **What do you think will appear on the screen?**

Predict → run → compare.

---

## 5–12 min — A Program as a Sequence of Instructions

Compare:

```python
print("A")
print("B")
print("C")
```

with:

```python
print("C")
print("A")
print("B")
```

Ask whether the result is the same and why.

Core message:

> **Python executes instructions in order.**

---

## 12–17 min — `print()`

Give the name to the operation already observed:

```python
print("Hello")
```

Explain only:

> `print()` displays output.

Use clear string examples with **double quotes consistently throughout Unit 1**.

---

## 17–22 min — Comments

```python
# This program prints a greeting
print("Hello")
```

Ask which line will appear in the output.

Core message:

> A comment is written for people reading the code. Python does not execute it as an instruction.

---

## 22–31 min — First Function

```python
def say_hello():
    print("Hello")
    print("Welcome")
```

Ask: **If we run this now, what will be printed?**

Expected insight: **nothing from the function yet.**

Then add:

```python
say_hello()
```

Teach only:

**Define → Call → Execute**

Do not make indentation a separate conceptual topic here.

---

## 31–38 min — Integrated Trace

```python
print("Start")

def say_hello():
    print("Hello")
    print("Welcome")

print("Ready")
say_hello()
print("End")
```

Students predict exact output before running.

Expected:

```text
Start
Ready
Hello
Welcome
End
```

During debrief, add the beginner-safe indentation sentence:

> **All lines that belong to the function are indented and line up the same way.**

---

## 38–41 min — Transition to Lab

Show:

**Open → Read → Predict → Run → Check → Modify → Comment → Save**

Explain that the lab will use this exact workflow.

---

## 41–45 min — Floating Buffer

Protected buffer for:

- questions
- logging in / opening Thonny
- moving into independent work
- small delays from the first half

Do not fill this time with additional content if the class is on schedule.

---

# 6. Second 45 Minutes — Lab

Use one starter file throughout.

## Starter filename

`G7_U1_FirstProgram_Starter.py`

---

## 45–49 min — Open

Students open the starter file but do **not** run it yet.

### Tool Note – Thonny

- Open: `File → Open`
- Run: `Run → Run current script`
- Save As: `File → Save As`
- After typing `:` and pressing Enter, Thonny normally indents the next line automatically.

These instructions are tool-specific and must remain isolated from the conceptual task.

---

## 49–56 min — Read → Predict → Run → Check

Students read the whole starter, including the function definition, and predict the exact output **before the first run**.

Then run and compare.

---

## 56–62 min — Modify

Students modify the three opening `print()` lines so they show:

- their name
- something they like
- one short sentence of their choice

Use double quotes in all examples.

---

## 62–66 min — Order Challenge

Students change the order of two lines.

Before running, they predict the new output order.

---

## 66–70 min — Documentation

Students add:

```python
# My first Python program
```

and one additional comment explaining part of the program.

---

## 70–77 min — Function Scaffold

The starter already contains this scaffold:

```python
def introduce_me():
    print("FIRST LINE")
    print("SECOND LINE")
```

Students:

1. replace the placeholder text with two personal lines
2. delete the original three opening `print()` statements
3. add the function call:

```python
introduce_me()
```

4. run the program and check that the function prints the two chosen lines

The structure is scaffolded to reduce indentation errors on the first Python lesson.

---

## 77–83 min — Final Predict Challenge — Protected Time

This block is non-negotiable assessment time.

Students arrange the file into:

```python
# My first Python program

print("Start")

# This function prints two facts about me
def introduce_me():
    print("My name is ...")
    print("I like ...")

print("Ready")
introduce_me()
print("End")
```

Before running, students write the exact predicted output.

Then run and compare.

Ask 2–3 students orally:

> **Why did the lines inside `introduce_me()` not run when Python reached the function definition?**

---

## 83–86 min — Save As

Save using:

`G7_U1_FirstProgram_<Name>.py`

Example:

`G7_U1_FirstProgram_Dana.py`

---

## 86–90 min — Buffer / Optional Exit Check

Use this time for:

- troubleshooting
- oral explanation
- optional exit check if time remains

Optional code:

```python
print("A")

def message():
    print("B")
    print("C")

print("D")
message()
```

Expected output:

```text
A
D
B
C
```

---

# 7. Misconception Risks

### Function runs when defined
Correction: definition describes the function; the body runs when the function is called.

### Comments appear in output
Correction: comments are for people; `print()` produces visible output.

### Program order does not matter
Correction: repeatedly predict and verify changed order.

### IDE = Python
Correction: Thonny is the current tool; Python code is the lesson focus.

### Indentation is decorative
Correction: all lines belonging to the function are indented and line up the same way.

---

# 8. Assessment Evidence

Primary evidence:

- output prediction
- comparison of prediction with actual output
- correct modification of `print()` statements
- correct comments
- correct use of the provided function scaffold and call
- Save As
- oral explanation of definition vs call

Do not use a vocabulary quiz as the main assessment.

---

# 9. IDE Portability Rule

### IDE-neutral

- Python code
- tasks
- prediction questions
- conceptual explanations
- lab sequence
- assessment
- filenames

### Tool-specific

- screenshots
- menu names
- button locations
- open/run/save instructions
- auto-indent behavior

Every tool-specific item must be labeled:

**Tool Note – Thonny**

If the IDE changes, only these notes/screenshots should need replacement.
