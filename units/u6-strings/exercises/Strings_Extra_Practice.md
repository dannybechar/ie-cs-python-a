# Unit 6 — Take-home pack: extra practice (strings)

Zero class minutes. Homework and enrichment, solutions-free. Source: the ministry Classroom folder, meeting 15 (strings) and meeting 19 (exam prep: strings and turtle). The statements below are re-written for the course style (no lists, `print` instead of `return` until 8.3, `isdigit` defined where used).

Use the printed exam formula sheet (folder 19.2 = 20.5, strings and turtle sections) for every item. Items that use a command that is not on the sheet say so.

## A. Exam-prep homework (assigned at the end of 6.4; reviewed for 10 minutes at the start of Unit 7.1)

Source: `classwork-m19-4-63849a.md` (submission sheet 19.4). Questions 1–7 are mandatory in the ministry plan, 8–10 optional.

| # | Task | Source | Notes |
|---|---|---|---|
| A1 | Fill an output table of 6 commands on `'The Matrix'`: an index, `len`, a negative index, a slice with a negative bound, `[::2]`, `[:]` | 19.4 Q1 | negative indexes, 6.1 and 6.3 |
| A2 | Remove all spaces from a sentence, once with `for char in text` and once with `for index in range(len(text))`; then decide which of the listed checks is true for a text (`count`, `in`, `not in`, `index`) | 19.4 Q2 | string building (6.2). The ministry distractor `my_string.lower('The')` is invalid Python: do not copy it. A chained `replace` item (`fix_spaces`) is optional |
| A3 | Password generator: build a string of random digits, a `0` becomes `#` | 19.4 Q3 | needs `randint` from Unit 7; do it after 7.3 |
| A4 | E-mail checker: no space, has an `@` | 19.4 Q4 | `not in` and `in`; done in class as `check_mail()` |
| A5 | Capitalise the first letter after a full stop | 19.4 Q5 | the ministry text compares with `' . '` (spaces around the dot), which is never true for one character: use `'.'`. `isalpha` must be defined in the item. The ministry uses `+=`: read it, write `x = x + y` |
| A6 | Riddle: a series of hints solved with `index`, `count` and `in` | 19.4 Q6 | `index` from 6.4 |
| A7 | Star line from words (the second part, the `split` version, is a challenge: `split` is not taught) | 19.4 Q7 | only the non-`split` part |
| A8–A10 (optional) | Write your own: does the text contain a given character, are the first and last characters equal, double every letter | 19.4 Q8–Q10 | the ministry asks to "return"; write them with `print` until 8.3, then redo them with `return` (return-lite) |

## B. Strings worksheet (meeting 15.2)

Source: `classwork-m15-2-ec45c1.md`. Pick by topic.

| # | Task | Source | Topic |
|---|---|---|---|
| B1 | Predict the printed result of mixed `+`, `*` and `str()` lines | 15.2 Q2, Q4, Q14 | 6.2, `str()` |
| B2 | Print the same word forwards and backwards with positive and negative indexes | 15.2 Q4, Q9, Q11 | 6.1, 6.3 |
| B3 | Slices with negative bounds and a step on a long text (`[-10:-6]`, `[-20:-14:2]`) | 15.2 Q12, Q13 | 6.3 |
| B4 | `find` and `count` with a start index, `startswith` with a start, `replace` with a count | 15.2 Q15, Q19, Q21, Q22 | 6.4. In Q21 the character to replace is lost in the extraction: check the original worksheet before use |
| B5 | `isdigit`, `islower`, `isupper` on short strings | 15.2 Q25 | 6.4 |

## C. Class game and enrichment

- **Hidden word from indexes** (deck #5): a long text and a line such as `text[0:2] + text[4] + ... + text[-1]`; students find the word. Source: `materials-m19-1-b8b334.md` slide 10. Good negative-index practice, use as a warm-up if a lesson has a spare minute.
- **Skip string** (deck #3): build a string from every third character with `range(0, len(text), 3)`. Source: `materials-m19-1` slide 8. Also the optional `every_third()` of 6.2.
- **ASCII** (not in `python-a.pdf`, on the formula sheet): `ord("a")` → 97, `chr(97)` → `a`; print a name as codes. Source: `classwork-m15-2` Q5–Q8. Five minutes of enrichment at most.
- **Frame a word in stars**: the optional `banner()` of 6.2.

## D. Turtle half of the ministry exam prep (not in Unit 6)

The eight turtle items of meeting 19 (`materials-m19-1-b8b334.md` slides 20–30; submission sheet `classwork-m19-3-a0fd4a.md`) belong to the turtle units (2, 5, 9). They are listed in the coordinator's notes, not here.
