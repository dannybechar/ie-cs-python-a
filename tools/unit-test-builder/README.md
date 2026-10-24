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
| `questions-turtle-a.js` | 6 questions with items: MC, open answer, grid drawing, code writing; marks, model answers, rubric |
| `build-written.js` | `node build-written.js out` writes `u2-turtle-test-a-students-he.docx` and `-key-he.docx` |
| `verify_turtle_test.py` | `python verify_turtle_test.py` checks every snippet answer with `turtle_sim.py` and the mark totals |

