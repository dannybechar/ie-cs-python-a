# Grade 7 — Python A

This repository is the source of truth for working examples and teaching
resources for the Grade 7 Python A course, built directly against the
Israeli Ministry of Education's official Python A program.

**Start here: [Table of contents (ordered unit material)](CONTENTS.md)**

- [`CONTENTS.md`](CONTENTS.md): every unit in teaching order, with its lessons
- [`units/`](units/README.md): one folder per unit (layout and rules)
- [`docs/standards/`](docs/standards/README.md): governing standards for this repository
- [`course-map.md`](course-map.md), [`class-progress.md`](class-progress.md), [`tools/`](tools)

**Source-of-truth precedence** (see [`docs/ministry-program/README.md`](docs/ministry-program/README.md)):
Status 2026-11-13: all units' notes, briefs and code are aligned with it (see [`docs/ministry-program/audit-summary.md`](docs/ministry-program/audit-summary.md)); the slide decks and printed lab sheets are not yet, see [`deck-sheet-backlog.md`](docs/ministry-program/deck-sheet-backlog.md).

1. the ministry Classroom program (21 meetings, 84 files; indexed and extracted in [`docs/ministry-program/`](docs/ministry-program)) decides **content**: topics, order of constructs, terminology, exercises;
2. [`docs/ministry-source/python-a.pdf`](docs/ministry-source/python-a.pdf) decides official **hours**;
3. everything in `units/` follows 1 and 2; a deliberate school deviation is recorded as an approved deviation in `docs/ministry-program/traceability.md`.

## Current build status

**All 30 official double meetings are built and approved by the teacher** (Units 1–9), plus the school-added Unit 0,
and every meeting has its Hebrew slide deck. See [`course-map.md`](course-map.md) for the unit-by-unit
breakdown, the schedule and the pace check, and each unit's `unit-strategy.md` for its official scope.
Where the two classes (Grade 7 and Grade 8) actually are in the course: [`class-progress.md`](class-progress.md).

- [Unit 0 — Environment Setup](units/u0-environment-setup) — school addition, outside the official 30 meetings; complete (1/1 meeting)
- [Unit 1 — Introduction to Python](units/u1-introduction-python) — complete (1/1 meeting)
- [Unit 2 — Turtle & Graphics](units/u2-turtle-graphics) — complete (3/3 meetings)
- [Unit 3 — Variables, Input/Output & Arithmetic](units/u3-variables-io-arithmetic) — complete (2/2 meetings)
- [Unit 4 — Conditional Execution](units/u4-conditional-execution) — complete (3/3 meetings)
- [Unit 5 — Repetition and Loops](units/u5-loops) — complete (4/4 meetings)
- [Unit 6 — Strings](units/u6-strings) — complete (4/4 meetings)
- [Unit 7 — Algorithmic Problems](units/u7-algorithmic-problems) — complete (3/3 meetings)
- [Unit 8 — Functions with Parameters](units/u8-functions-parameters) — complete (4/4 meetings)
- [Unit 9 — Event-Driven Programming](units/u9-event-driven-programming) — complete (6/6 meetings)

## Repository layout

```
docs/
  annual-strategy.md        — year-wide pedagogical strategy (phases, assessment, enrichment, exit profile)
  annual-work-plan-he.docx  — official annual work plan (Hebrew)
  ministry-source/          — the official ministry PDFs this course answers to (hours, circulars)
  ministry-program/         — the ministry Classroom program: manifest, text extracts, traceability and per-unit audits (content authority)
  reviews/                  — external lesson reviews, one folder per review
tools/
  deck-patch-kit/           — scripts for reviewing and patching the NotebookLM slide decks
  ministry-import/          — extract.py: rebuilds docs/ministry-program/ from the ministry download folder
  check-repo.py             — consistency check (Python compiles, every lesson has notes/page/HTML/deck, course-map rows, manifest); run `python -I tools/check-repo.py`
  lesson-decks/             — build_decks.py: generates the HTML deck beside every lesson page
  lab-sheet-builder/        — builds the printable Unit 3 lab sheets and key
  unit-test-builder/        — question data and builder for the Hebrew unit tests (Unit 2 so far)
units/
  README.md                       — layout and rules for units
  u{N}-{official-unit-slug}/
    README.md                     — unit entry page: links to everything in the unit
    unit-strategy.md              — the unit's official scope + meeting breakdown
    unit-plan.md                  — lesson sequence, minutes, status
    background-paper.md           — teacher's background paper (not yet added for any unit)
    lessons/L{NN}-{slug}.md       — student: Hebrew lab brief, the lesson page (NN = meeting number in the unit)
    lessons/L{NN}-{slug}.html     — student: generated one-file slide deck (tools/lesson-decks)
    lessons/L{NN}-{slug}/         — student: slides-he.pdf (NotebookLM, patched), lab sheets, exit check
    exercises/                    — student code: *_Starter.py files for the lab tasks (Unit 2 also has the extra exercises)
    assessment/                   — student test sheets (Unit 2 so far)
    teacher/                      — TEACHER-ONLY: L{NN}-{slug}-notes.md, solutions/ (*_Reference.py), answer keys, run of show
```

## Repository conventions

- **Naming rule:** a meeting is named by its curriculum unit, as
  **Unit {U}.{M} — {unit name}** (e.g. *Unit 4.1 — Conditional Execution*);
  in Hebrew, **יחידה {U}.{M} – {שם היחידה}** (e.g. *יחידה 4.1 – ביצוע מותנה*).
  Unit names follow the Ministry program (`python-a.pdf`); Unit 0 is the
  school-added Environment Setup (סביבת עבודה). A lesson's theme or topic
  (e.g. "The Rover's Sensors") appears only as a subtitle, never as its name.
  This applies to headings, the course map, lab briefs, slide titles and
  footers, and NotebookLM notebook names.
- Every `.py` example must compile cleanly before it's committed.
- Code files use `_Starter` / `_Reference` — `_Starter` is the student's
  starting point (may contain an intentional bug, documented in that
  meeting's `teacher/L{NN}-{slug}-notes.md`), `_Reference` is the model solution.
- Unit layout: see [`units/README.md`](units/README.md). Student material is in `lessons/`, `exercises/` and
  `assessment/`; teacher-only files (notes, solutions, keys) are in `teacher/` and never in a student folder.
- Every lesson's notes state its **Duration** and **Structure**. When a
  meeting is added or retimed, log it in [`course-map.md`](course-map.md)
  and keep each unit's planned minutes within its official minutes
  (1 academic hour = 45 minutes).
- No version suffixes in filenames — git history is the version record.
- Hebrew-facing files (decks, lab briefs, exit checks) keep an explicit
  `-he` suffix since directory names are English.
- Markdown is the source format for lesson notes, lab briefs and plans, so
  everything renders on GitHub. Exceptions: original ministry documents stay
  in their original format, and slide decks are made in NotebookLM and
  committed as `lessons/L{NN}-{slug}/slides-he.pdf`.
- Hebrew in Markdown: start every Hebrew line with a Hebrew word (GitHub
  picks each paragraph's direction from its first letter). Put code in
  fenced blocks. Wrap tables and numbered/bulleted lists in
  `<div dir="rtl">` … `</div>` with blank lines inside, since GitHub
  doesn't set their direction automatically.
- Generated files (`__pycache__/`, etc.) are not committed.
- Never commit student information, passwords, tokens, or private school data.

## Course workflow

1. Open the unit folder under `units/` (start from [`CONTENTS.md`](CONTENTS.md)); its `README.md` lists each lesson's files.
2. Read `teacher/L{NN}-{slug}-notes.md` for the full 90-minute lesson plan.
3. Run the `_Starter` / `_Reference` scripts and confirm they behave as documented.
4. Compare against the lesson page `lessons/L{NN}-{slug}.md` and the exit check.
5. Commit only after the example has been verified.

## Slide decks

Every meeting's deck is made in NotebookLM from its lesson notes and lab brief,
then checked slide by slide against the lesson notes and the `_Reference` code,
patched where needed, and committed as `lessons/L{NN}-{slug}/slides-he.pdf`.
Every lesson page also has a generated `.html` deck beside it (see [`tools/lesson-decks/`](tools/lesson-decks/README.md)). The tools and the
list of recurring NotebookLM problems are in [`tools/deck-patch-kit/`](tools/deck-patch-kit/README.md).
To change a deck, regenerate or edit it outside the repo and replace the PDF.
