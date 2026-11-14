# Working rules for the assistant

Read [`README.md`](README.md) (conventions) and [`CONTENTS.md`](CONTENTS.md) first. Course status: [`course-map.md`](course-map.md) and [`class-progress.md`](class-progress.md).

## Repository structure for units
- Every unit lives in `units/<id>-<name>/` with the layout in `units/README.md`: an entry page `README.md`, `background-paper.md`, `unit-plan.md`, `lessons/`, `assessment/`, `teacher/`, `feedback/`.
- Every lesson is delivered as `.html` AS WELL AS `.md` (same stem, same folder). No PDF or PowerPoint. The Markdown is the source of truth; the HTML is one self-contained, student-safe, printable slide file.
- Obtain or write the background paper before drafting a unit's lessons.
- Whenever a unit gains or changes material, update its row in `CONTENTS.md` and its entry page. Do not link planned material that does not exist.
- Teacher-only files (keys, audits) go in `teacher/`, never in `lessons/` or `assessment/`.
- Before finishing, run the link and anchor checks from the structure instructions and report any failure.

## How this repo applies it
- The lesson page `lessons/L<NN>-<slug>.md` is the Hebrew student lab brief. The teacher's minute-by-minute plan is `teacher/L<NN>-<slug>-notes.md`. Solutions are in `teacher/solutions/`.
- This repo has no `feedback/` folder (reviews live in `docs/reviews/`) and no `optional-java/`. The existing NotebookLM slide PDFs are kept as `lessons/L<NN>-<slug>/slides-he.pdf`; do not produce new PDFs or PowerPoints for lessons.
- Rebuild the HTML decks with `python tools/lesson-decks/build_decks.py` (needs `pip install -r tools/lesson-decks/requirements.txt`); `--check` verifies they are up to date.
- Repository consistency check: `python -I tools/check-repo.py`.
- Do not push unless the owner says to.
