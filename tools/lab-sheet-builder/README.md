# Lab sheet builder

`build_u3_labs.py <output folder>` builds the printable Unit 3 lab sheets (A4, Hebrew, right to left, black and white, one sheet both sides, 45 minutes each) and a one-page teacher key, using headless Edge and PyMuPDF. The script fails if a student sheet grows beyond two pages. Edit it with the Edit/Write tools, not shell heredocs (Hebrew gets mangled). The sheets follow the Unit 3 slide decks and use the starters in `units/u3-variables-io-arithmetic/exercises/`.

## Worksheet standard (the teacher's rules, for every worksheet)

- Two question types only: **run** (run the code, write what was printed, explain why) and **code** (write the code that does X).
- Every question is a pair of equal-height boxes: the **code is always in the left box** (given code, or an empty box where the student writes code), and the **answer box is on the right** with printed prompts (what was printed, explain why) and blank space. No ruled lines.
- Helpers in the script: `qrow(left, right)`, `code(text)`, `empty(height)`, `ans(label, height)`.
