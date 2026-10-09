# Task: review two versions of a multiple-choice test

You are an experienced Python teacher and an expert in middle-school education (grades 7-8, ages 12-14), and you also know good test-design practice. Review the work below critically and honestly. Do not flatter. Do not modify any files; just answer with the report.

## Context
- Course: "Python A", Unit 2 "Turtle & Graphics", three 90-minute meetings (2.1, 2.2, 2.3). The ground truth of what was taught and practised in the lab is in `lesson-2.1-notes.md`, `lesson-2.2-notes.md`, `lesson-2.3-notes.md`. The students saw Hebrew slides based on these notes. Unit 2 deliberately excludes loops, variables, input, goto/backward/coordinates, and parameters of our own functions.
- Test requirements from the teacher: multiple choice for grades 7 and 8; NO trick questions, only honest questions and answers that check that the student listened in class and did the required lab work; it must take 45 minutes; only 1-2 students in a class should score above 90%.
- Files: `Version_A_student_test.md` + `Version_A_answer_key.md`, and `Version_B_student_test.md` + `Version_B_answer_key.md`. They are Hebrew (right-to-left) with English code. The files are exported text, so judge content and wording, not visual layout (the real documents are Word/PDF with code boxes). 25 questions each, 4 points per question, 4 options, answer letters are Hebrew letters (א ב ג ד = A B C D).
- The answer key claims difficulty levels (A easy / B medium / C hard) and an expected class average of about 70, and about 38 minutes of solving time for a good student.

## What to do
1. VERIFY EVERY ANSWER. For each of the 50 questions, work out the correct answer yourself (you may write and run a tiny Python simulation of turtle movement in a scratch file: start at (0,0) heading right; left = counter-clockwise; right = clockwise; penup/pendown/pencolor/pensize/stamp; Python turtle conventions). Report any question where your answer differs from the key, where 0 or 2+ options are defensible, or where the code or wording is ambiguous.
2. CHECK FAIRNESS against the lesson notes: is every question answerable from what was actually taught/practised? Flag anything outside scope, any hidden trick, or any distractor that is unfairly close to the right answer.
3. CHECK AGE/LANGUAGE: Hebrew wording clarity for 12-14 year olds, typos, grammar, confusing phrasing, code readability.
4. CHECK TIME AND DIFFICULTY DESIGN: can a typical grade 7-8 student finish 25 questions in 45 minutes? Is the claimed difficulty split realistic, and is the "only 1-2 students above 90%" goal plausible? Say what you would change.
5. COMPARE A AND B: are they equivalent in coverage and difficulty? Any question pair that is too similar or unbalanced?
6. Give a prioritised list of concrete fixes (version, question number, what to change, suggested replacement wording where useful).

## Output format
A Markdown report in English (Hebrew only when quoting the test). Sections: Summary verdict (3-5 lines); Answer verification table (version, Q#, key letter, your letter, OK/PROBLEM); Problems found (ordered by severity); Fairness and scope; Language and clarity; Timing and difficulty; Version A vs B; Recommended fixes. Be specific and concise.
