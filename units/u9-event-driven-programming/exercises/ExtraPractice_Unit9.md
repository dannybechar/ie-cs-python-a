# Unit 9 — Extra practice (take-home, zero class minutes)

For students who finish early or want more. No solutions here; the teacher's answers for the class tasks are in `solutions/`.
Source references point to the ministry Classroom folder (`docs/ministry-program/extracts/`). The ministry's code is only a source of ideas: write your own solutions.

Use the style you prefer (module style from the lessons or the exam's object style); try each exercise once in each style.

## Mouse (after 9.2 and 9.3)

1. **Step forward.** Each click on the rover moves it 40; after 5 clicks it prints `Arrived` and stops moving. (Lab 9.2, former Task 3.)
2. **Connect the dots.** Each click on the screen draws a line from the last point and a small orange dot. (Lab 9.3, former Task 3.)
3. **Three colours in turn.** A click on the screen stamps a circle at the click. The circles are blue, red, green, blue, red, green, and so on. Use a counter and `%`. (ministry 20.3 task 4)
4. **Random size.** A click on the rover changes its size to a random number from 1 to 6. (ministry 20.3 task 5; needs `import random`)
5. **Stamp variations.** Use the quarter-colour program from 9.3, and add a `stamp()` of the rover's shape, a thicker pen, or a different shape for each quarter. (ministry 20.3 tasks 2–3)
6. **Digits on click.** You are given two functions, `draw_one()` and `draw_two()`, that draw the digits 1 and 2. A left click draws the next digit at the click. (ministry 20.2, the last task; only the click part, not the circles)

## Keyboard (after 9.4)

7. **Four arrows with a trail.** Move the turtle with four arrow keys, and add `pendown`, a `stamp` or a different colour for each direction. (ministry 20.4 task 1, part D)
8. **Key down, key up.** The turtle draws while the space bar is held and stops when it is let go (`onkeypress` and `onkeyrelease`).
9. **A letter key.** Add a letter key (a lower-case letter) that stamps. Check on your computer what happens with a capital letter.

## Animation and the whole game (after 9.5)

10. **True or false.** Mark each statement as true or false and fix the false ones. (ministry 20.4 task 2, part B)
    - The line `ball.dx *= -1` changes the direction of the ball (`*=` means `ball.dx = ball.dx * -1`).
    - The condition `ball.xcor() > 390` keeps the ball inside the screen.
    - The line `score_b += 1` counts the number of moves.
    - The call `ball.setx(...)` sets the x place where the ball is.
11. **Pong with a timer.** Two paddles moved by keys (`w`/`s` and the up/down arrows) and a ball that bounces off the top and bottom borders. Use `ontimer` for the ball's steps. Extension: score, ball speed, colours. (ministry 20.4 task 2, parts C–E; the ministry's version uses a `while True` loop, which we do not use)
12. **Your own game.** Choose three events (a click, a key, a timer) and design a small game around them. The ministry mentions sharing such games in competitions and festivals.

## Exam-style reading (turtle part of the exam)

13. **Draw what the code draws.** Read short turtle programs (`left`, `forward`, a grid of 40-step squares) and draw the path on a grid. (ministry m19 slides 21 and 25)
14. **Match code to shapes.** Four code fragments with `for` and `range`, four shapes: match them. (ministry m19 slides 23–24)
15. **Another squares question.** Change Adi's program (Checkpoint B, question 3) so that the squares alternate between three colours. What must change in the condition?
