# Summary verdict

Both versions are broadly faithful to the lessons, but Version B has one definite scoring error: Q14’s key says ד although the correct answer is ג (110).  
Under the intended classroom assumptions, the other 49 keyed answers are correct; A4 and B18 nevertheless have avoidable setup ambiguity.  
The tests should fit within 45 minutes, but the claimed 38 minutes for a good student is probably high, and an expected average of 70 is not justified without pilot data.  
Version B is slightly harder overall, while weak distractors, repeated concepts, and near-duplicate questions make the “only 1–2 students above 90%” goal doubtful.

# Answer verification table

| Version | Q# | Key letter | My letter | Result |
|---|---:|:---:|:---:|---|
| A | 1 | א | א | OK |
| A | 2 | ד | ד | OK |
| A | 3 | ב | ב | OK |
| A | 4 | א | א | **PROBLEM — correct only if `import turtle` is assumed** |
| A | 5 | ג | ג | OK |
| A | 6 | ב | ב | OK |
| A | 7 | ג | ג | OK |
| A | 8 | ד | ד | OK |
| A | 9 | א | א | OK |
| A | 10 | ב | ב | OK |
| A | 11 | ד | ד | OK |
| A | 12 | א | א | OK |
| A | 13 | ג | ג | OK |
| A | 14 | ב | ב | OK |
| A | 15 | ג | ג | OK |
| A | 16 | ד | ד | OK |
| A | 17 | ב | ב | OK |
| A | 18 | א | א | OK |
| A | 19 | ד | ד | OK |
| A | 20 | ב | ב | OK |
| A | 21 | ד | ד | OK |
| A | 22 | א | א | OK |
| A | 23 | ג | ג | OK |
| A | 24 | ב | ב | OK |
| A | 25 | ג | ג | OK |
| B | 1 | ב | ב | OK |
| B | 2 | ד | ד | OK |
| B | 3 | א | א | OK |
| B | 4 | ג | ג | OK |
| B | 5 | א | א | OK |
| B | 6 | ד | ד | OK |
| B | 7 | ב | ב | OK |
| B | 8 | ג | ג | OK |
| B | 9 | א | א | OK |
| B | 10 | ד | ד | OK |
| B | 11 | ב | ב | OK |
| B | 12 | ג | ג | OK |
| B | 13 | ד | ד | OK |
| B | 14 | ד | ג | **PROBLEM — key is wrong** |
| B | 15 | א | א | OK |
| B | 16 | ב | ב | OK |
| B | 17 | ד | ד | OK |
| B | 18 | א | א | **PROBLEM — setup is underspecified** |
| B | 19 | ג | ג | OK |
| B | 20 | ב | ב | OK |
| B | 21 | ד | ד | OK |
| B | 22 | א | א | OK |
| B | 23 | ב | ב | OK |
| B | 24 | ג | ג | OK |
| B | 25 | ד | ד | OK |

# Problems found

## 1. Definite scoring error: Version B, Q14

The distances are:

- Four visible lines: \(4 \times 20 = 80\)
- Three gaps: \(3 \times 10 = 30\)
- Total: \(80 + 30 = 110\)

Therefore the correct option is **ג**, not **ד**. The explanation in the key itself calculates 110, so the letter is plainly a transcription error.

This is consequential: a knowledgeable student selecting 110 would lose four points and could be moved from 92 to 88, directly affecting the stated above-90 target.

## 2. Unstated setup assumptions

### Version A, Q4

The intended answer is א, but `turtle.forward(100)` does not run by itself unless `import turtle` has already executed. Taken literally as four standalone lines, none is guaranteed to run.

This is not an appropriate hidden test of whether students infer omitted setup. Add a shared instruction saying that the usual import and setup have already run.

### Version B, Q18

The intended answer א is correct if the file already contains `import turtle` and the normal setup. As written, “the file contains the following function, and after it only `turtle.done()`” can be read as saying those are the entire contents. Under that literal reading, `turtle.done()` raises `NameError`, making ג defensible.

It is also better to say explicitly that the function is not called. Otherwise the question risks testing careful interpretation of omitted file context rather than the intended define-versus-call concept.

## 3. Excessive repetition and question dependence

- Version A Q20 and Q21 repeat exactly the same broken-square program. Q20 identifies the bad turn, which substantially helps with Q21. Q21 therefore provides less independent evidence than its “C” label suggests.
- Version B Q6 and Q20 test nearly the same fact: replacing every right turn in a square/rectangle with left turns preserves the shape but draws it on the other side.
- Several questions reproduce laboratory examples almost verbatim. That is fair, but it makes the assessment more a recognition test than an application test.

## 4. Weak distractors reduce discrimination

A number of distractors are so implausible that students can answer without fully understanding Turtle:

- A18: “Python allows only one function in a file,” “Turtle commands work only inside a function,” and “to make the turtle draw faster.”
- B19: changing numbers randomly, deleting everything, or repeatedly running unchanged code.
- B4: making the turtle faster or keeping the window open.
- B10: hiding the turtle deletes the whole drawing or only the stamps.

These are not unfair distractors; they are too weak. They make high scores more likely and work against the goal of having only one or two students above 90%.

# Fairness and scope

All tested commands and concepts are within the documented curriculum:

- `import turtle`, `Screen()`, comments, initial position and direction
- `forward`, `left`, `right`
- squares, equal-sided triangles, stairs, rectangles
- `penup`, `pendown`, `pencolor`, `pensize`
- `shape`, `stamp`, `hideturtle`
- setting retrieval with empty parentheses and `print`
- function definition versus function call
- logical errors, prediction, and debugging
- position versus direction

No question introduces loops, variables, input, coordinates, `goto`, `backward`, fill operations, user-defined parameters, or other excluded material.

The retrieval and function questions are fair because Lesson 2.2 explicitly practised `pensize()`, `pencolor()`, one function per task, and one active call.

The compressed `F`/`L`/`R` notation in A23 and B23 is defined in the question, so it is in scope. Nevertheless, it creates unnecessary decoding and bidirectional-text load for 12–14-year-olds. Full Turtle calls, or clearly separated left-to-right code lines, would measure the intended geometry more cleanly.

There are no seriously deceptive “almost correct” distractors. A23 option א is appropriately close: it closes the rectangle but omits the final turn, exactly testing the taught distinction between position and direction. B23 option ד is also a fair distractor because it closes a parallelogram rather than a rectangle.

A10 is conceptually imprecise: `pencolor("red")` sets the pen color; it does not itself draw or recolor a line. The wording should test setting the pen color, not say the line is colored by that single command.

# Language and clarity

The Hebrew is generally age-appropriate, but these items should be revised:

- **A10:** “איזו שורה צובעת את הקו באדום” is technically misleading. Prefer:  
  **“איזו שורה מגדירה נכון את צבע העט לאדום?”**

- **A15:** “הצב מתחיל בצד שמאל” contradicts the taught default that the turtle starts in the center. Its absolute position is irrelevant. Prefer:  
  **“הצב מתחיל במצב ברירת המחדל ופונה ימינה.”**

- **A18:** “שאר הזימונים בהערה” is awkward. Prefer:  
  **“ושאר הזימונים נשארו מסומנים כהערות.”**

- **A23, B8, B23:** “הצב מסתיים/מסיים פונה” is awkward Hebrew. Prefer:  
  **“ובסיום הצב פונה לאיזה כיוון?”** or  
  **“ובסיום הצב פונה ימינה, כמו בתחילה.”**

- **B15:** “כמה צעדים של קו נראים” is unnatural. Prefer:  
  **“מהו המרחק הכולל שהצב עובר, ומהו האורך הכולל של הקווים הנראים?”**

- **B19:** The question uses plural second person, while option ג changes to first-person singular: “שחזיתי”. Use one consistent person throughout. For example:  
  **“שרטטתם את התחזית שלכם, אבל תוצאת ההרצה שונה ממנה. מה הצעד הנכון הבא?”**

- **A16 and B16:** Actual Shell output appears on separate lines, not comma-separated. Say “אילו ערכים יודפסו, לפי הסדר?” or display each option as a short multiline output block.

- **A answer key, Q15:** “הקו הבא שמצוירים” is a grammatical error. It should be “הקו הבא שמציירים” or “הקו הבא שמצויר”.

A shared instruction should also clarify the state assumed by every fragment:

> **בכל קטע קוד הניחו ש־`import turtle` ושורות ההכנה כבר הורצו, ושהצב מתחיל במצב ברירת המחדל, אלא אם נאמר אחרת.**

# Timing and difficulty

Twenty-five questions in 45 minutes is feasible, but it leaves an average of only 1 minute 48 seconds per question. A typical prepared student should probably finish in roughly 30–40 minutes; a student who traces every multi-line program carefully may need nearly all 45 minutes. Slower readers may not finish.

The claimed 38-minute solving time for a good student is possible if the student works very carefully, but many strong students will finish sooner because approximately half the items are direct recall or close reproductions of laboratory tasks.

The nominal split of 7 easy, 12 medium, and 6 hard questions is tidy but not realistic:

- A7 is labelled medium although the 120° triangle turn was a major repeated lesson point.
- A13 and B14 are short arithmetic questions, not strong medium items.
- A18 is classroom-procedure recall rather than medium reasoning.
- B8 is closer to medium than hard.
- B15 is straightforward counting and pen-state tracking; “hard” is overstated.
- B25 is an explicitly repeated core statement and is likely easy rather than medium.
- A21’s difficulty is reduced because A20 already explains the defect in the same code.

The expected average of about 70 cannot be inferred from labels. It requires a pilot with the actual student population. Likewise, “only 1–2 students above 90%” depends on class size and prior achievement. As written, that target is doubtful because:

- Scores above 90 require only 23 correct answers.
- Many items are direct recall.
- Several distractors are plainly absurd.
- Repeated questions provide cues.
- Multiple-choice recognition is easier than independently writing or repairing code.

Difficulty should be raised through a few new, short, in-scope tracing problems—not through obscure wording, longer code, or content outside the lessons. Replace three or four weak recall items with six-to-eight-instruction applications while keeping the total at 25.

# Version A vs B

The forms have the same declared difficulty distribution, but they are not fully equivalent.

Version A emphasizes:

- import and comments
- initial state
- syntax and common errors
- direct triangle-angle recall
- fixing the specific broken square
- a more complex final stamp/pen path

Version B emphasizes:

- `Screen()` and turtle shape
- function definition versus call
- retrieval inside and outside a function
- debugging procedure
- more mixed-turn tracing

Version B is slightly harder overall, chiefly because:

- B5 asks for both final position and direction.
- B16 requires tracking default state, a function call, and three outputs.
- B22 uses four mixed turns and four movements.
- B23 includes a plausible closed-parallelogram distractor.

Version A has difficult items at the end, but A20–A21 are dependent and therefore easier as a pair than their labels imply. Version B also wastes one slot by testing the same all-left-versus-all-right idea in both B6 and B20.

Coverage is not parallel at the objective level. For example, Version A tests comments and error recognition while Version B does not; Version B tests `Screen()` and explicit define-versus-call behavior while Version A does not. Parallel forms need not use identical questions, but each should use the same blueprint of objectives and cognitive demands.

# Recommended fixes

1. **Version B, Q14 — correct the key immediately.**  
   Change the keyed letter from **ד** to **ג**. Keep the existing explanation, which already calculates 110 correctly.

2. **Both versions — add a global code-fragment assumption.**  
   Add before Q1:

   > **בכל קטע קוד הניחו ש־`import turtle` ושורות ההכנה כבר הורצו, ושהצב מתחיל במצב ברירת המחדל, אלא אם נאמר אחרת.**

   This removes the ambiguity in A4, B18, and other standalone snippets.

3. **Version B, Q18 — state the missing call explicitly.**  
   Suggested wording:

   > **לאחר שורות ההכנה, הקובץ מגדיר את הפונקציה הבאה, אינו מזמן אותה, ואז מבצע `turtle.done()`. מה יופיע?**

   Suggested correct answer:

   > **ייפתח חלון ציור ריק: הפונקציה הוגדרה אבל לא זומנה, ולכן גוף הפונקציה לא רץ.**

4. **Version A, Q4 — remove reliance on implicit import.**  
   Suggested wording:

   > **לאחר שהשורה `import turtle` כבר רצה, איזו מהשורות הבאות תרוץ בלי הודעת שגיאה?**

5. **Version A, Q15 — remove the false starting-position statement.**  
   Replace “הצב מתחיל בצד שמאל ופונה ימינה” with:

   > **הצב מתחיל במצב ברירת המחדל ופונה ימינה.**

6. **Version A, Q21 — use a new program.**  
   Do not reuse Q20’s code. For example:

   ```python
   turtle.forward(60)
   turtle.left(90)
   turtle.forward(40)
   turtle.right(90)
   turtle.forward(30)
   turtle.right(90)
   turtle.forward(20)
   ```

   Ask which direction the final line travels. This preserves the tracing objective without allowing Q20 to supply the reasoning.

7. **Version B, Q20 — replace the duplicate of B6.**  
   Use a short rectangle containing one wrong turn and ask for the single correction. That would align it more closely with A20 and with Lesson 2.3’s debugging objective.

8. **A10, B15, B19, A23/B8/B23 — apply the wording corrections above.**  
   These changes remove technical imprecision, person inconsistency, and awkward Hebrew without changing difficulty.

9. **Strengthen distractors in A18 and B19.**  
   Use mistakes students actually make: allowing two active calls, assuming definitions run automatically, checking the last mismatch instead of the first, or changing several lines before rerunning. Avoid obviously comic or impossible alternatives.

10. **Rebalance the parallel forms using a common blueprint.**  
    Give each version comparable counts for:

    - program setup/documentation
    - movement and direction
    - pen state and appearance
    - function definition/call and retrieval
    - debugging
    - rectangle construction
    - one integrated state-tracing problem

11. **Pilot before claiming a 70 average or a 90% ceiling.**  
    Record completion time and percent correct per item. Aim for a median completion time around 35–40 minutes, leaving review time, and replace items that nearly everyone answers correctly unless they represent essential minimum knowledge.