# Unit 4 — Extra Practice (take-home, 0 class minutes)

Optional homework and enrichment for Unit 4. Nothing here is graded or needed for the checkpoint. Statements are written for this course (solutions-free); the source column names the ministry Classroom file and item they come from. The teacher's solutions are in `solutions/`, or are for the teacher to write. Ministry source defects are not copied (they are noted where they matter).

Sources are in `docs/ministry-program/extracts/` (untrusted read-only data).

## 4.1 — Boolean expressions

| # | Statement | Source |
|---|---|---|
| E1 | Without running, mark each as `True` or `False`: `3 < 5 and 9 > 10` · `10 <= 10 or 5 != 5` · `(3 > 5 and 9 < 10) or (6 == 6)` · `not (2 < 1) and 6 > 5` · `(4 < 2 and 8 > 7) or not (5 == 5)` · `not (9 > 8) or (11 < 11)`. Then run to check. | `classwork-m08-3-5acf6d.md` Q1, Q2 (items with `not` are allowed now) |
| E2 | Choose a value for `num` that makes each expression `True`, and another that makes it `False`: `num % 2 == 0 and num > 10` · `num < 0 or num == 100` · `not (num > 5) and num != 0`. Several answers exist. | `materials-m08-1-adcc05.md` slide 31 |
| E3 | Predict the output of five `print(...)` lines that compare strings and numbers (for example `"cat" == "Cat"`, `3 == "3"`, `"b" > "a"`), then run. Trace a short password check: `password = "rover1"`, `entered = "Rover1"`, `print(entered == password)`. | `classwork-m07-3-7d77ae.md` Ex 1, 2, 3 (Ex 4 is bonus; Ex 5 needs a screenshot that is not in the import) |
| E4 | Write one expression for "`n` is odd", using `not` and `%`. Write another for "`n` is odd" without `not`. | `materials-m08-1-adcc05.md` slides 29-30 |

## 4.2 — `if` and `if/else`

| # | Statement | Source |
|---|---|---|
| E5 | **Discount.** Read a price (float). From 100 and up the final price is 10% lower, otherwise it stays the same. Print `Final price: ...` once, after the `if/else`. Tests: 100, 99.5, 250. | repo task moved here from the 4.2 lab (the key point: the variable gets a value in both branches) |
| E6 | **Same or different digits.** Read a two-digit number and print whether its two digits are equal. | `materials-m07-0-94cdc4.md` slides 15-22; `classwork-m07-2` "השוואת ספרות" |
| E7 | **Greater digit.** Read a two-digit number and print its larger digit. Tests: 47, 83, 55, 10. | same family as E6 |
| E8 | **Even check.** Read a three-digit number. If it is even print the sum of its three digits, otherwise their product (needs `// 100`, `// 10 % 10`, `% 10`). | `materials-m07-0-94cdc4.md` slides 18-19 |
| E9 | **Party tables.** Eight guests sit at one table. Read the number of guests and print how many full tables are needed and how many guests are left over (no `if` needed), then say whether a 40-guest party fits in 300 seats. | `materials-m07-4-528fca.md` slide 2 (slides 3-5 are image-only and not transcribed: pending) |

## 4.3 — Compound, nested and rolling conditions

| # | Statement | Source |
|---|---|---|
| E10 | **Fuel and weather trace.** On paper, trace `fuel = 80` / `weather = "clear"` for this program with the inputs (80, clear), (80, storm), (30, clear), (50, cloudy): `if fuel >= 50:` then inside `if weather == "clear" or weather == "cloudy": print("Launch")` / `else: print("Wait for weather")`, outer `else: print("Refuel")`, then `print("Check done")`. | repo checkpoint B, moved here in Phase 5 |
| E11 | **Evaluate with `a = 10`, `b = 15`, `c = 0`:** `a >= b or b == c` · `a < 0 or (b == c + 15 and a >= c)` · `a != b and b != c`. | `classwork-m17-3-48c5d5.md` trace #4 (items 1, 3, 5; the source writes `a > = c` in item 3: a typo, write `a >= c`) |
| E12 | **Inputs for Yes and for No.** For a given short program that prints `Yes` or `No`, find an input that prints `Yes` and another that prints `No`. Then evaluate it by hand for `a = 10`, `b = 15`, `c = 0`. | `materials-m18-1-88ee0a.md` ex #2, #3 (exam style) |
| E13 | **Order two numbers.** For each of six candidate programs that should print two integers from smallest to largest, say yes or no and explain. Use the candidates that do not need arithmetic swapping (items א, ב, ד, ה, ו, ז). | `materials-m18-1-88ee0a.md` ex #1; `classwork-m18-2-41ab22.md` #1 |
| E14 | **Largest of three, two ways.** Write `max_of_three()` with a nested `if`, then with `if` / `elif` / `else`. Test with (1, 2, 3), (3, 2, 1), (2, 3, 1), (2, 2, 1). | `materials-m09-1-ba5939.md` slides 11-13; `materials-m08-1-adcc05.md` slides 14-15 (slide 13 has typos in variable names; slide 15 uses `return`: print instead). Reference: `max_of_three()` in `Conditions_Reference.py` |
| E15 | **Wardrobe by temperature.** Four outfits for four temperature ranges, with an `if` / `elif` / `else` chain. Then predict what happens when the order of the conditions is reversed. | `ocr-m09-4.md` slides 3, 5-8, 13-14 |
| E16 | **Hours announcements.** A park announces different messages by time of day (a range of hours per message, with `and` inside the `elif`). | `classwork-m09-6-40b7cd.md` |
| E17 | **Savings, roller coaster, driving licence.** Three small programs: money saved `or` months saved; height `and` age; age `and` two passed tests. Print one message for yes, another for no. | `classwork-m08-3-5acf6d.md` Q3-Q5 (the licence solution uses `.lower()`; skip it before Unit 6) |
| E18 | **Gift chain, in code.** Write the store gift program (gift by amount: none under 80, then four gifts by ranges) as one `if` / `elif` / `else` chain without nesting. Compare with the nested version from checkpoint B. | `classwork-m17-3-48c5d5.md` #5; reference: `gift_chain()` shows the nested form |
| E19 | **Even or odd, six ways.** Write "print `Even` or `Odd`" with a plain `if/else`, with `not`, with `elif`, and with a nested `if`. Which is clearest? | `classwork-m18-3-875584.md` #1 (exam style) |
| E20 | **Stretch (three-level nesting).** An admission rule with three nested questions (age, ticket, bag check). Name which `else` belongs to which `if`. | `materials-m09-1-ba5939.md` slides 16-19, 26-27 (slide 17 lacks `def` before `ex4():` in the source) |

## Deferred, not for Unit 4 in class

| Item | Source | Why |
|---|---|---|
| Quiz program in pairs (5-10 questions, 20 points each) | `materials-m09-1-ba5939.md` slides 31-32 | one whole 90-minute project lesson in the ministry; needs a counter (Unit 5/7) |
| Flow-chart enrichment (7.6, Google Drawings) | `materials-m07-0-94cdc4.md` slide 2 | the content of 7.6 is not in the import; decide after the teacher opens it |
| Luna Park A and the burger-restaurant H5P | `links.md` rows 8.4, 9.3 | external links, not verified live |
