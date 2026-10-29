# Unit test builder

Generates the Hebrew multiple-choice Unit 2 tests (student sheet + teacher key, Word) from plain question data.

| File | What it is |
|---|---|
| `questions-a.js` | Form A: 25 questions, with answers, difficulty, topic and a one-line explanation |
| `questions-b.js` | Form B: 25 different questions on the same blueprint |
| `build.js` | Builds the two `.docx` files for one form (right-to-left Hebrew, code in boxes) |
| `turtle_sim.py` | Small turtle simulator; every code-tracing answer was checked with it |

## Build

```
npm install docx@9          # once, in this folder (node_modules is not committed)
node build.js out           # Form A -> out/u2-test-a-students-he.docx, out/u2-test-a-key-he.docx
QFILE=./questions-b.js VER=B node build.js out    # Form B -> u2-test-b-*.docx
```

Convert to PDF with LibreOffice (`soffice --headless --convert-to pdf out/*.docx`) and look at every page before using it.

## Editing questions

- `«…»` in a question marks inline code. Options are `correct` + `wrong` (position set by `keyPlan` at the bottom) or `fixed` in display order with `ans`.
- Keep the answer letters balanced and avoid runs of the same letter; the build prints nothing about it, so check with `node -e "console.log(require('./questions-a.js').q.map(x=>'אבגד'[x.answer]).join(' '))"`.
- Tracing questions: verify the answer with `turtle_sim.py` before changing code in a question.
- The committed PDFs and `.docx` files in `units/u2-turtle-graphics/` are the current output; rebuild and replace them after any edit.

## Written turtle-basics test

| File | What it is |
|---|---|
| `questions-turtle-a.js` | 6 questions with items: MC, open answer, grid drawing, code writing; marks, model answers, rubric. An item with `draw: {cols, rows, start, cell}` gets a code box (right) and an empty grid (left) with a start arrow; the key shows the solved grid |
| `build-written.js` | `node build-written.js out` writes `u2-turtle-test-a-students-he.docx` and `-key-he.docx` |
| `verify_turtle_test.py` | `python verify_turtle_test.py` checks every snippet answer with `turtle_sim.py` and the mark totals |


### First sitting (Grade 8, 29 Oct 2026, 36 students)

Aggregates only; individual grades and feedback papers are kept outside the repository (student data). Graded from the handwritten scans with the rubric in `questions-turtle-a.js` (a model read the handwriting; unclear items were re-examined and decided best-effort).
Mean 94.6 · median 95.5 · range 74–100 · 11 students scored 100. The hardest item was 1א (22% scored zero).

**Two rubric lines were fixed after the sitting (29 Oct 2026)**

- 4ב "explains what happens" earned 0 for all 36 students and 4ג "the first line does not change" earned full marks for only 8 of 36, because the question text asked for neither. For the first sitting both lines were credited to everyone. The questions now ask for them: 4ב adds "ומה קורה בציור בגלל החסר?" and 4ג adds "ציינו גם מה נשאר זהה". Rubric lines and points are unchanged, the test is still 7 pages, and the estimate is still about 62 minutes.
- The test was easy for this class (mean 94.6), so it separates weak students but not strong ones.
