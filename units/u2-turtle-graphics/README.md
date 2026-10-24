# Unit 2 — Turtle & Graphics

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

6 academic hours = 3 meetings = 270 minutes (45 theory / 225 practice).

## Meetings and materials

| Meeting | Type | File | What it is |
|---|---|---|---|
| **Unit** | Strategy | [`unit-strategy.md`](unit-strategy.md) | Official scope, topics, hours and the meeting breakdown |
| **2.1** First Moves | Lesson | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan: human-turtle hook, turning, square, lab (staircase, triangle, letter if time) |
|  | Exercise | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
|  | Exercise | [`TurtleFirstMoves_Starter.py`](exercises/TurtleFirstMoves_Starter.py) | Starter file |
|  | Exercise | [`TurtleFirstMoves_Reference.py`](solutions/TurtleFirstMoves_Reference.py) | Solutions, one function per task |
|  | Lesson | [`m1-slides-he.pdf`](m1-slides-he.pdf) | Hebrew slides (23 slides, rover theme, made in NotebookLM; slides 8, 12, 14, 17, 19 corrected and exit check 22–23 added) |
| **2.2** Pen, Appearance and Stamps | Lesson | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan: three short demos, each followed by a task; one function per task |
|  | Exercise | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
|  | Exercise | [`TurtlePenStamp_Starter.py`](exercises/TurtlePenStamp_Starter.py) | Starter file (warm-up as a function) |
|  | Exercise | [`TurtlePenStamp_Reference.py`](solutions/TurtlePenStamp_Reference.py) | Solutions, one function per task |
|  | Lesson | [`m2-slides-he.pdf`](m2-slides-he.pdf) | Hebrew slides (15 slides, made in NotebookLM; slides 2, 6, 10, 15 corrected) |
| **2.3** Geometry Challenge | Lesson | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan |
|  | Lesson | [`m3-slides-he.pdf`](m3-slides-he.pdf) | Hebrew slides (18 slides, rover theme, made in NotebookLM; slides 8, 9, 17 corrected) |
|  | Exercise | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
|  | Exercise | [`m3-exit-check-he.png`](m3-exit-check-he.png) | Exit check |
|  | Exercise | [`GeometryChallenge_Starter.py`](exercises/GeometryChallenge_Starter.py) | Starter file |
|  | Exercise | [`GeometryAssessment_Reference.py`](solutions/GeometryAssessment_Reference.py) | Assessment solution |
| **Extra** 10 turtle exercises | Exercise | [`exercises/`](exercises) | Ten starter files (01 ThickRedRectangle … 10 WelcomeSign): a comment header with the task, and an empty body to fill; see [below](#unit-2-extra-practice--10-turtle-exercises) |
|  | Exercise | [`solutions/`](solutions) | The ten complete solutions, same file names; the header explains what each one practices |
| **Test** Forms A and B | Test | [`u2-test-a-students-he.pdf`](u2-test-a-students-he.pdf), [`u2-test-b-students-he.pdf`](u2-test-b-students-he.pdf) | 45-minute multiple-choice test sheets (Word sources: [A](u2-test-a-students-he.docx), [B](u2-test-b-students-he.docx)) |
|  | Test | [`u2-test-a-key-he.pdf`](u2-test-a-key-he.pdf), [`u2-test-b-key-he.pdf`](u2-test-b-key-he.pdf) | Answer keys and blueprints ([A](u2-test-a-key-he.docx), [B](u2-test-b-key-he.docx)); details [below](#unit-2-test) |
| **Test** written, basics | Test | [`u2-turtle-test-a-students-he.pdf`](u2-turtle-test-a-students-he.pdf) | 60-minute written test on forward/left/right/penup/pendown only (Word source: [docx](u2-turtle-test-a-students-he.docx)) |
|  | Test | [`u2-turtle-test-a-key-he.pdf`](u2-turtle-test-a-key-he.pdf) | Key with rubric and sample solutions ([docx](u2-turtle-test-a-key-he.docx)); details [below](#unit-2-written-test) |

## Unit 2 extra practice — 10 turtle exercises

Ten short exercises (the solutions are 17–20 lines of code each, no functions, loops or variables) for after the three meetings or as homework. Each file starts with a comment block that says what the exercise draws and what it practices. Difficulty is about "a rectangle in different colors and pen thicknesses", widened step by step: filled shapes, `dot`, `bgcolor`, `circle`, `write`.

The files: 01 ThickRedRectangle · 02 FourColorFrame · 03 FilledBlueRectangle · 04 TrafficLight · 05 HouseWithRedRoof · 06 ThreeColorRibbons · 07 GoldenStarInNightSky · 08 ConcentricColorRings · 09 SnowmanFromDots · 10 WelcomeSign.

## Unit 2 test

A 45-minute multiple-choice test for grades 7 and 8 covering all three meetings (25 questions, 4 points each). It checks that students listened in class and did the lab work: honest questions only, no tricks. Two parallel forms with different questions, each with a teacher key. The key lists difficulty (7 easy / 12 medium / 6 hard), topic and a short explanation per question. Expected class average is about 70, with very few students above 90; these are estimates, so adjust after the first class (see the key).

Built from the question data in [`tools/unit-test-builder/`](../../tools/unit-test-builder/README.md); reviewed by ChatGPT, see [`docs/reviews/unit2-test/`](../../docs/reviews/unit2-test/REVIEW-FOLLOWUP.md).

## Unit 2 written test

A 60-minute paper test (Form A only) on the five basic commands: `forward`, `left`, `right`, `penup`, `pendown`. Six questions worth 17/17/17/17/16/16 = 100 points, about 10 minutes each: two multiple choice, two code analysis, two write-the-code. Every lettered sub-question brings its own code or start state, so a mistake in one does not cost the next. The instructions page includes hints. Writing and analysis items have a partial-credit rubric in the key. Time per question is an estimate for an average student, not measured.

Built from [`tools/unit-test-builder/`](../../tools/unit-test-builder/README.md) (`questions-turtle-a.js`, `build-written.js`); answers checked with `verify_turtle_test.py`.
