# Standards

[Table of contents](../../CONTENTS.md) · [Repository home](../../README.md)

Governing rules for the whole repository. They are summarised here and kept where they were written; nothing was moved.

| Standard | Where it lives |
|---|---|
| Content authority: the ministry Classroom program decides topics, order of constructs, terminology and exercises; `python-a.pdf` decides official hours; a deliberate school deviation is an approved deviation in `traceability.md` | [`docs/ministry-program/README.md`](../ministry-program/README.md), [`traceability.md`](../ministry-program/traceability.md) |
| Year-wide pedagogy: phases, assessment, enrichment, exit profile | [`docs/annual-strategy.md`](../annual-strategy.md) |
| Naming rule: **Unit {U}.{M} — {unit name}**, theme only as a subtitle; Hebrew **יחידה {U}.{M} – {שם}** | [`README.md`](../../README.md#repository-conventions) |
| Code conventions: every `.py` compiles; `_Starter` / `_Reference`; no version suffixes | [`README.md`](../../README.md#repository-conventions) |
| Hebrew in Markdown: start each line with a Hebrew word, code in fenced blocks, tables and lists in `<div dir="rtl">` | [`README.md`](../../README.md#repository-conventions) |
| Time budget: every lesson states Duration and Structure; unit minutes stay within official minutes (1 academic hour = 45 min) | [`course-map.md`](../../course-map.md) |
| Unit layout and teacher-only rule | [`units/README.md`](../../units/README.md) |

## Lesson deck standard (HTML)

Every lesson page `lessons/L<NN>-<slug>.md` has a generated `L<NN>-<slug>.html` beside it (same stem).

- One self-contained file: inline CSS and JavaScript, no external fonts, scripts or images; works offline from a double-click.
- One idea per slide (split at each `##` heading); Previous and Next buttons; keyboard navigation (in these right-to-left decks the left arrow, space and Page Down go forward, the right arrow and Page Up go back).
- Readable in light and dark (`prefers-color-scheme`) and on a phone (no horizontal scrolling); printing gives one slide per page.
- Student-safe: built only from the student lesson page, never from `teacher/`; any section headed Solution, Answer, Key or Teacher (also in Hebrew) is dropped.
- Start with `<!doctype html>`, `<meta charset="utf-8">` and a viewport meta; the `<title>` is the lesson's title.
- No PDF or PowerPoint is *produced* for lessons. The NotebookLM slide decks are existing approved Hebrew PDFs kept in `lessons/L<NN>-<slug>/slides-he.pdf`; the patch workflow is in [`tools/deck-patch-kit/`](../../tools/deck-patch-kit/README.md).

GitHub shows `.html` files as source, not as a rendered page: open a downloaded copy in a browser.
