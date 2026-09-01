# Grade 7 — Python A

This repository is the source of truth for working examples and teaching
resources for the Grade 7 Python A course, built directly against the
Israeli Ministry of Education's official Python A program
([`docs/ministry-source/python-a.pdf`](docs/ministry-source/python-a.pdf)).

## Current build status

**3 of 30 official double meetings are built**, spanning parts of 3 of the
9 official units. See [`course-map.md`](course-map.md) for the full
unit-by-unit breakdown, and each unit's `strategy/unit-strategy.md` for
what's built vs. still missing within that unit.

- [Unit 1 — Introduction to Python / Environment](units/u1-introduction-environment) — complete (1/1 meeting)
- [Unit 2 — Turtle & Graphics](units/u2-turtle-graphics) — partial (only Meeting 3, the geometry challenge/assessment)
- [Unit 3 — Variables, Input/Output & Arithmetic](units/u3-variables-io-arithmetic) — partial (only Meeting 2, input→calculation→output)
- Units 4–9 — not yet started

## Repository layout

```
docs/
  annual-strategy.md        — year-wide pedagogical strategy (phases, assessment, enrichment, exit profile)
  annual-work-plan-he.docx  — official annual work plan (Hebrew)
  ministry-source/          — the official ministry PDFs this course answers to
units/
  u{N}-{official-unit-slug}/
    strategy/unit-strategy.md   — that unit's official scope + meeting breakdown
    m{K}-{meeting-slug}/
      examples/    — Starter / Reference Python scripts
      teacher/     — Hebrew lesson deck + lesson notes
      student/     — Hebrew lab brief (docx + pdf)
      assessment/  — exit-check image, where one exists
```

## Repository conventions

- Every `.py` example must compile cleanly before it's committed.
- Code files use `_Starter` / `_Reference` — `_Starter` is the student's
  starting point (may contain an intentional bug, documented in that
  meeting's `teacher/lesson-notes.md`), `_Reference` is the model solution.
- No version suffixes in filenames — git history is the version record.
- Hebrew-facing files (decks, lab briefs, exit checks) keep an explicit
  `-he` suffix since directory names are English.
- Generated files (`__pycache__/`, etc.) are not committed.
- Never commit student information, passwords, tokens, or private school data.

## Course workflow

1. Open the meeting folder under `units/`.
2. Read `teacher/lesson-notes.md` for the full 90-minute lesson plan.
3. Run the `examples/` scripts and confirm they behave as documented.
4. Compare against `student/lab-brief-he.docx` and the exit check.
5. Commit only after the example has been verified.
