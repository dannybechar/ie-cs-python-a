# Grade 7 — Python A

This repository is the source of truth for working examples and teaching
resources for the Grade 7 Python A course, built directly against the
Israeli Ministry of Education's official Python A program
([`docs/ministry-source/python-a.pdf`](docs/ministry-source/python-a.pdf)).

## Current build status

**All 30 official double meetings are built and approved by the teacher** (Units 1–9), plus the school-added Unit 0,
and every meeting has its Hebrew slide deck. See [`course-map.md`](course-map.md) for the unit-by-unit
breakdown, the schedule and the pace check, and each unit's `unit-strategy.md` for its official scope.

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
  ministry-source/          — the official ministry PDFs this course answers to
  reviews/                  — external lesson reviews, one folder per review
tools/
  deck-patch-kit/           — scripts for reviewing and patching the NotebookLM slide decks
units/
  u{N}-{official-unit-slug}/
    README.md               — index of the unit's meetings and their files
    unit-strategy.md        — that unit's official scope + meeting breakdown
    m{K}-lesson-notes.md    — teacher: minute-by-minute plan for meeting K
    m{K}-slides-he.pdf      — teacher: Hebrew slide deck (NotebookLM, patched)
    m{K}-lab-brief-he.md    — student: Hebrew lab brief
    m{K}-exit-check-he.*    — exit check, where one exists
    *_Starter.py / *_Reference.py — lab code for the unit's meetings
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
  meeting's `m{K}-lesson-notes.md`), `_Reference` is the model solution.
- All of a unit's files sit flat in the unit folder; the `m{K}-` prefix
  says which meeting a file belongs to.
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
  committed as `m{K}-slides-he.pdf`.
- Hebrew in Markdown: start every Hebrew line with a Hebrew word (GitHub
  picks each paragraph's direction from its first letter). Put code in
  fenced blocks. Wrap tables and numbered/bulleted lists in
  `<div dir="rtl">` … `</div>` with blank lines inside, since GitHub
  doesn't set their direction automatically.
- Generated files (`__pycache__/`, etc.) are not committed.
- Never commit student information, passwords, tokens, or private school data.

## Course workflow

1. Open the unit folder under `units/`; its `README.md` lists each meeting's files.
2. Read `m{K}-lesson-notes.md` for the full 90-minute lesson plan.
3. Run the `_Starter` / `_Reference` scripts and confirm they behave as documented.
4. Compare against `m{K}-lab-brief-he.md` and the exit check.
5. Commit only after the example has been verified.

## Slide decks

Every meeting's deck is made in NotebookLM from its lesson notes and lab brief,
then checked slide by slide against the lesson notes and the `_Reference` code,
patched where needed, and committed as `m{K}-slides-he.pdf`. The tools and the
list of recurring NotebookLM problems are in [`tools/deck-patch-kit/`](tools/deck-patch-kit/README.md).
To change a deck, regenerate or edit it outside the repo and replace the PDF.
