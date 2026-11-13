"""Repo consistency check. Usage:  python -I tools/check-repo.py   (run from the repo root)

Errors (exit 1):  Reference .py that does not compile; a meeting without notes / lab brief / deck;
                  course-map meeting log not 31 rows of 90 min; manifest rows whose extract is missing.
Warnings:         Starter .py that does not compile (some are broken on purpose); lesson notes without a
                  recognisable Duration line.
Nothing is written to disk (compile() only, no __pycache__).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors, warnings = [], []


def check_python():
    n = 0
    for f in sorted((ROOT / "units").rglob("*.py")):
        n += 1
        try:
            compile(f.read_text(encoding="utf-8"), str(f), "exec")
        except SyntaxError as e:
            msg = "%s: %s (line %s)" % (f.relative_to(ROOT).as_posix(), e.msg, e.lineno)
            (warnings if "_Starter" in f.name or f.parent.name == "exercises" else errors).append("python: " + msg)
    return n


def check_meetings():
    n = 0
    for unit in sorted((ROOT / "units").glob("u[0-9]*")):
        notes = sorted(unit.glob("m*-lesson-notes.md"))
        if not notes:
            errors.append("%s: no lesson notes" % unit.name)
        for note in notes:
            k = re.match(r"m(\d+)-", note.name).group(1)
            n += 1
            for need in ("m%s-lab-brief-he.md" % k, "m%s-slides-he.pdf" % k):
                if not (unit / need).exists():
                    errors.append("%s: missing %s" % (unit.name, need))
            if not re.search(r"(?i)duration", note.read_text(encoding="utf-8")):
                warnings.append("%s/%s: no Duration line" % (unit.name, note.name))
    return n


def check_course_map(meetings):
    text = (ROOT / "course-map.md").read_text(encoding="utf-8")
    log = text.split("## Meeting log", 1)[1].split("\n## ", 1)[0]
    rows = re.findall(r"^\|\s*(\d)\s*\|\s*([\d.]+)[^|]*\|\s*(\d+)\s*\|", log, re.M)
    if len(rows) != meetings:
        errors.append("course-map: %d meeting-log rows, %d meetings built" % (len(rows), meetings))
    bad = [r[1] for r in rows if r[2] != "90"]
    if bad:
        errors.append("course-map: meetings not 90 min: %s" % ", ".join(bad))
    return len(rows)


def check_manifest():
    mf = ROOT / "docs" / "ministry-program" / "manifest.json"
    if not mf.exists():
        errors.append("manifest.json missing")
        return 0
    rows = json.loads(mf.read_text(encoding="utf-8"))
    for r in rows:
        if r.get("extract") and not (mf.parent / r["extract"]).exists():
            errors.append("manifest: missing extract %s" % r["extract"])
        if r["status"] not in ("ok", "ocr"):
            errors.append("manifest: %s has status %s" % (r["name"], r["status"]))
    return len(rows)


if __name__ == "__main__":
    py = check_python()
    meetings = check_meetings()
    rows = check_course_map(meetings)
    files = check_manifest()
    print("python files: %d | meetings: %d | course-map rows: %d | manifest files: %d" % (py, meetings, rows, files))
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    sys.exit(1 if errors else 0)
