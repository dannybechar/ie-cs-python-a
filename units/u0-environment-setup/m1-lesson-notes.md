# G7 Unit 0 Meeting 1 Lesson Strategy v1

## Grade 7 / Python A
### Unit 0 — Environment Setup
### Meeting 1 — Install, Check, Save

**Status:** Draft for review  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (one short explanation at the start)  
**Current tool:** Thonny 5.0.0, which includes Python 3.14 (versions current in September 2026)  
**Tool-dependence rule:** This is the one lesson that is about the tool itself. Keep the concepts (Python vs. tool, course folder, file naming, save/reopen) in separate sections from the Thonny steps, so that if the IDE changes, only the **Tool Note – Thonny** sections need replacing.

---

## 1. Lesson Goal

Every student leaves with a working setup:

**Install → Open → Check → Save → Reopen**

and knows that Thonny is the tool, while Python is the language they will learn.

---

## 2. Student-Facing Objectives

Students should be able to:

1. Explain in one sentence the difference between Python and Thonny.
2. Download software from the official site only.
3. Install Thonny and open it from the Start menu.
4. Name the parts of the Thonny window: editor, Shell, Run, Stop.
5. Save files in the course folder, using the file-naming rules.
6. Run the check file and read its result.
7. Close Thonny, reopen it and find a saved file.

---

## 3. Before the Lesson — Teacher Checklist

Do this on one lab PC, **logged in as a student account**, at least a few days before the lesson.

| Check | Why it matters | If it fails |
|---|---|---|
| The student account can open https://thonny.org and download the installer | Students install it themselves | Put the installer on a shared drive or USB stick instead |
| The installer runs **without admin rights** (Thonny installs into the user's own folder by default) | Lab PCs usually block admin installs | Use the **portable** version (zip), or ask IT to install Thonny for all users before the lesson |
| Windows SmartScreen or school security software doesn't block the installer | This is the most common failure on school PCs | Ask IT to allow it, or pre-install |
| Files saved in the planned course folder **are still there after a restart** | Many labs reset PCs on reboot (e.g. "Deep Freeze") | Choose a different location: network drive, USB stick or cloud drive |
| The lab PCs are Intel/AMD, not Arm | There are separate installers | Use the Arm installer on Arm (e.g. Snapdragon) machines |

**Decide before the lesson:** where the course folder lives (see section 7). The lab brief says `Documents\G7-Python`. If you choose somewhere else, change that line in the brief.

**Prepare:** copy `EnvironmentCheck.py` to where students can get it (shared drive, class site or USB stick).

---

## 4. Core Model

### Python vs. Thonny

> **Python is the language. Thonny is the tool we write it in and run it from.**

Thonny comes with Python inside it, so installing Thonny installs both.
This is the correction for the Unit 1 misconception "IDE = Python".

### Files live in folders, not "in Thonny"

A program is a file with a `.py` ending, saved in a folder. Thonny only opens it.

### File-naming rules

- English letters, numbers and `_` only. No spaces, no Hebrew.
- Always ends in `.py`.
- **Never** name a file after something Python already has: not `turtle.py`, `random.py` or `math.py`.
  Python would open the student's file instead of the real one, and Turtle programs stop working.
- The course pattern: `G7_U<unit>_<Topic>_<Name>.py`, e.g. `G7_U0_Check_Dana.py`.

---

## 5. Lesson Flow

## 0–5 min — Hook

Run `EnvironmentCheck.py` on the projector: the `OK` lines appear and the Turtle window draws a square with "Ready!".

Say: **By the end of today, your computer will do exactly this.**

---

## 5–12 min — What We Need

Teach only:

> **Python is the language. Thonny is the tool we write it in and run it from.**

Ask: **If we changed the tool next year, would the Python code change?** Expected answer: no.

---

## 12–17 min — Safe Downloading

- Only from the official site: **thonny.org**. Check the address bar.
- Don't click advertisement "Download" buttons on other sites.
- Windows may show a warning ("Windows protected your PC"). Follow the teacher's instruction, don't click through on your own.

---

## 17–35 min — Guided Install (everyone together)

### Tool Note – Thonny

1. At thonny.org, choose the **Windows installer** (Intel/AMD, x64 file).
2. Run the downloaded file. If Windows warns about it, wait for the teacher.
3. Keep the default options. **Don't** choose "Run as Administrator"; the default install goes into the student's own folder.
4. At the end, open Thonny from the Start menu.
5. On first launch, if Thonny asks for language and initial settings: **English** and **Standard**.

Students who finish early help a neighbor **with words only, not the mouse**.

---

## 35–45 min — Tour of Thonny

### Tool Note – Thonny

| Part | What it's for |
|---|---|
| Editor (top) | Where the program file is written |
| Shell (bottom) | Where the output appears |
| Run (green ▶, or F5) | Runs the file in the editor |
| Stop (red ■) | Stops a running program |
| View → Files | Shows the folders on the computer |

Keep it short. Students will use these parts every lesson from Unit 1 onward.

---

## 45–55 min — Course Folder

1. Create the course folder (default: `Documents\G7-Python`).
2. Copy `EnvironmentCheck.py` into it.
3. Go over the file-naming rules (section 4).

---

## 55–65 min — Environment Check

Students open `EnvironmentCheck.py` in Thonny and run it.

Expected result in the Shell:

```text
Python version: 3.14.x
OK   Python 3
OK   math
OK   random
OK   turtle
Opening the drawing window...
All done. Close the drawing window to finish.
```

A drawing window opens with a blue square and "Ready!". Students close the drawing window when done.

Say: **You don't need to understand this code yet. By the end of the year you will be able to write all of it.**

---

## 65–75 min — Save As, Close, Reopen

### Tool Note – Thonny

1. File → Save As → in the course folder, name it `G7_U0_Check_<Name>.py`.
2. Close Thonny completely.
3. Open Thonny again, then File → Open → the course folder → the file.
4. Run it again.

This proves the file was really saved where the student thinks it was.

---

## 75–82 min — Installing at Home

The Ministry program expects students to be able to install the environment themselves (Chapter 1, goal 1).

Homework: install Thonny at home in the same way, then run `EnvironmentCheck.py` there.

- Mac and Linux installers are also on thonny.org.
- A student with no computer at home tells the teacher privately. Don't ask about this in front of the class.

---

## 82–87 min — Exit Check

The teacher walks around with the class list. Each student shows:

1. Thonny open.
2. `G7_U0_Check_<Name>.py` in the course folder.
3. The check output with every line `OK`.

Then asks one student out of every few: **What is the difference between Python and Thonny?**

---

## 87–90 min — Buffer

Troubleshooting for students who are still installing.

---

## 6. Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| "Windows protected your PC" | SmartScreen doesn't know the installer | "More info" → "Run anyway", only if school policy allows it. Otherwise use the portable version or IT |
| Installer blocked completely | School security policy | Portable version from a shared drive, or IT pre-install |
| `PROBLEM   turtle is missing` | Python installed without Tk (usually a separate Python, not Thonny's) | Make sure Thonny uses its own built-in Python: Tools → Options → Interpreter |
| `AttributeError` or strange errors when using turtle | A student file is named `turtle.py` | Rename that file |
| The drawing window doesn't appear | It opened behind Thonny | Look at the taskbar and bring it forward |
| Can't find the saved file | Saved somewhere else | View → Files, or File → Save As again into the course folder |
| The file disappeared after a restart | The lab PC resets on reboot | Change the course folder location (section 3) |

---

## 7. Course Folder Options

| Option | Good | Watch out |
|---|---|---|
| `Documents\G7-Python` on the lab PC | Simplest | Lost if the PC resets, and students don't always sit at the same PC |
| School network drive | Follows the student to any PC | Needs IT setup; check it works from Thonny's Open dialog |
| USB stick | Also works at home | Gets lost or forgotten |
| Cloud drive (OneDrive / Google Drive folder) | Works at home too | Needs the sync app on lab PCs |

---

## 8. Misconception Risks

### Thonny is Python
Correction: Python is the language. Thonny is one tool for writing it; others exist.

### Files are saved "in Thonny"
Correction: files are saved in a folder. The save/reopen step is there to prove it.

### Any "Download" button is fine
Correction: only from the official site. Check the address bar.

---

## 9. Assessment Evidence

- Thonny installed and opened by the student
- `EnvironmentCheck.py` output with every line `OK`, and the Turtle drawing
- `G7_U0_Check_<Name>.py` saved in the course folder and reopened
- An oral one-sentence answer: Python vs. Thonny

No grade. This is a readiness check for Unit 1.
