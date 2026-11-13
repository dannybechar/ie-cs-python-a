# Ministry Python-A program (source of truth for content)

Origin (not committed): `C:\Users\Guitar\Workspace\classroom-downloader\downloads\פייתון_א` — 84 files (51 docx, 32 pptx, links.md), the Ministry of Education's Google Classroom program for Python A, grades 7–8.

## Precedence
1. **This program (folder)** decides content: topics, order of constructs, terminology, exercises, exam-style questions.
2. **`docs/ministry-source/python-a.pdf`** (and the circular/clarifications PDFs) decides official hours.
3. Repo lesson material (`units/`, decks, tests) follows 1 and 2. A deliberate school choice that differs must be recorded as an *approved deviation* in `traceability.md`.

## Contents
- `manifest.md` / `manifest.json` — one row per source file with extraction status. Regenerate:
  `python -I tools/ministry-import/extract.py "<origin>" docs/ministry-program`
- `extracts/` — text of each docx/pptx (slide text + speaker notes), named `<area>-m<meeting>[-<component>]-<hash>.md`.
- `traceability.md`, `audit-u*.md` — added in later phases.

## Reading the source correctly
- The program has 21 meetings (0–20); each is a Classroom lesson with components `N.1` deck, `N.2` submission sheet, `N.3+` worksheets / H5P / "Master Python" quizzes, last = "סיכום בקטנה" summary.
- **The folder number is authoritative.** About 20 Classwork files carry a different number inside the file (e.g. folder `2.2` holds a file numbered `3.2`; folder `12.2` holds `16.2`); some headers say the wrong lesson.
- Teacher copies `3.0`, `6.0`, `13.0` (marked "leave as draft") differ from the student decks `3.1`, `6.1`, `13.1`; `5.0` and `7.0` have no student version.
- Image-only decks (no extractable text, 5 files): `9.4 elif`, `12.3`, `12.5`, `13.3`, `13.5` — need a visual/OCR pass.
- H5P, YouTube and "Master Python" items exist only as links (`links.md`) or component names; link labels use yet another numbering.
- The folder states no total hours, no week schedule and has no test files; exam prep is meetings 17–19.
