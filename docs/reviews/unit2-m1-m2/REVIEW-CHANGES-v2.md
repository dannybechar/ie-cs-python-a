# Changes after review round 1

Numbers match the review's findings. All code was re-run in Python 3.14 after the changes.

| # | Finding | Change | Files |
|---|---|---|---|
| 1 | `color_square()` reference didn't hide the turtle | Added `turtle.hideturtle()` at the end (checked: turtle hidden, back at start, facing right) | `TurtlePenStamp_Reference.py` |
| 2 | Task D output depends on earlier tasks' settings | Task D is its own function and the only active call, so each run starts fresh and `1 / 8 / black` is deterministic. Added the question "why black, when Task B used orange?" | `m2-lesson-notes.md`, `m2-lab-brief-he.md` |
| 3 | "Combine everything into one file" leaks state | New rule, carried from Unit 1: **one function per task, one active call, the rest as comments.** The starter now contains `warm_up()` as a function and its call; every task reference is a function | `TurtlePenStamp_Starter.py`, `m2-lesson-notes.md`, `m2-lab-brief-he.md` |
| 4 | "After a closed shape it turned 360" is too broad | Narrowed to "in our square and triangle, to finish facing the same direction, all turns together are 360°", with a note not to generalize | `m1-lesson-notes.md` |
| 5 | M1 lab overpacked | Triangle moved before the letter (60–72, 12 min). Letter is the flexible "if time" block (72–82). Priority table added: starter, staircase, triangle, save are must-do | `m1-lesson-notes.md`, `m1-lab-brief-he.md` |
| 6 | Common-errors section too long | Cut to 4 minutes (32–36): `Forward` as the main example, `"100"` flashed without reading its message. Freed time goes to the pre-lab buffer (36–45) | `m1-lesson-notes.md` |
| 7 | Purpose of documentation not checked | Added a 30-second question at 7–14: "אם אני פותח את הקובץ שלכם בעוד חודש — למה השורה שמתחילה ב-`#` יכולה לעזור לי?" | `m1-lesson-notes.md` |
| 8 | `showturtle()` not practiced | Demo 2 asks "איך לדעתכם נחזיר אותו?"; the brief has everyone add `hideturtle()`, run, then add `showturtle()`, run | `m2-lesson-notes.md`, `m2-lab-brief-he.md` |
| 9 | "מחזירה" suggests return values | Replaced with the Ministry terms **מעדכנת / מאחזרת**, and "כשיש ערך בסוגריים — משנים. כשהסוגריים ריקים — שואלים מה הערך עכשיו" | `m2-lesson-notes.md`, `m2-lab-brief-he.md` |
| 10 | "אבני דרך" means milestones | Renamed to **אבני קפיצה** | `m2-lab-brief-he.md`, `m2-lesson-notes.md` |
| 11 | Triangle question ambiguous | Now "כדי שהצב יסיים כשהוא שוב מסתכל ימינה, כמה מעלות הוא צריך להסתובב בסך הכול?" then "360° ÷ 3 פינות = ?" | `m1-lab-brief-he.md`, `m1-lesson-notes.md` |
| 12–13 | Keep M2 structure and scope | No change | — |
