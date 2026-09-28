# Deck patch kit

Tools for reviewing and patching the Hebrew slide decks that NotebookLM generates for this course.
Teacher-facing material lives in `units/`; this folder is only for maintaining the decks.

Requirements: Python 3 with `pymupdf`, `pillow`, `numpy`, `opencv-python`, `python-bidi`; Windows fonts Segoe UI and Consolas.

## Review and patch one deck

1. Copy `common.py` and `heb.py` to a scratch folder and work there.
2. Render the newest PDF in Downloads: `render(pdf, D)` (D is a short tag such as `84` for Unit 8.4).
3. **Check the title slide first** — the newest PDF may be a different meeting than the one asked for.
4. Check every slide against `Downloads/unit<U>-m<M>-slides/1-source-slide-content.md`
   (or, when that folder is gone, the lesson notes and the `_Reference` code): use `sheet()` for overviews, then crop suspicious lines at full size.
5. Write `p<D>.py` (`from common import *`) that patches only real errors, `save(D, p, im)` each page, then `build(D, '', N)`.
6. Copy `new_<D>.pdf` to `units/<unit dir>/m<M>-slides-he.pdf` and to `Downloads/python-a/unit U.M - <English unit name>.pdf`;
   update the unit README row and the `course-map.md` meeting log; commit and push.

## Recurring NotebookLM problems

- Hebrew lines that mix in code come out garbled (flipped parentheses, doubled or made-up words). Rebuild them with `parts()` in on-screen order.
- The footer sits under the Gemini watermark (bottom right). Redraw it to the left or centered.
- Table columns in left-to-right order. Swap the column strips when the widths match.
- Pictures that contradict the code (3D houses, nested squares, a wrong windmill, a zigzag `goto`, a closed shape for an open path). Redraw the flat Turtle result.
- A challenge-task slide that shows the full (sometimes wrong) solution. Keep only the function header.
- Minus signs dropped from answers (`-5`, `-6`), and "X" written on the vertical axis. Check every number and axis label.
- Decorative code from outside the course (pygame, JavaScript) in the background. Remove it.
- Timer badges with a stray colon or without the number.
- Hints or picture text that give away the answer on a question-only slide. Remove them.
- A "bug" slide where NotebookLM silently fixed the bug. Restore the bug.
- Missing timers on student-activity slides. Copy the deck's own timer badge.

## Preparing a NotebookLM folder

`mkinstr.make(...)` writes `0-START-HERE-instructions.md` (Hebrew output language, the exact NAMING block, slide count,
code and table rules, check list). Each `Downloads/unit<U>-m<M>-slides/` folder also gets `1-source-slide-content.md`
(every slide spelled out, minutes summing to 90) and the meeting's lesson notes and Hebrew lab brief.
