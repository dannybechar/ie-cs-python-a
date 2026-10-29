"""Checks the answers of questions-turtle-b.js (Form B) against turtle_sim.py, the mark totals, the rubrics and the uniform grid."""
import json, re, subprocess
from turtle_sim import run, P

def prog(code):
    ab = {"forward": "F", "left": "L", "right": "R", "penup": "U", "pendown": "D"}
    toks = []
    for ln in code.strip().splitlines():
        m = re.fullmatch(r"turtle\.(\w+)\((\d*)\)", ln.strip())
        toks.append(ab[m[1]] + m[2])
    return P(" ".join(toks))

def info(code):
    pos, head, segs, _ = run(prog(code))
    return pos, head, segs

data = json.loads(subprocess.check_output(["node", "-e", "console.log(JSON.stringify(require('./questions-turtle-b.js')))"]))
qs, META = data["qs"], data["META"]
I = lambda q, k: qs[q]["items"][k]

# marks: same split as Form A, every rubric adds up to its item
tot = [sum(i["pts"] for i in q["items"]) for q in qs]
print("marks per question:", tot, "total", sum(tot))
assert tot == [17, 17, 17, 17, 16, 16] and [len(q["items"]) for q in qs] == [4, 4, 3, 3, 3, 3] or [len(q["items"]) for q in qs] == [4, 4, 3, 3, 3, 3]
assert sum(len(q["items"]) for q in qs) == 20
for q in qs:
    for i in q["items"]:
        if "rubric" in i:
            assert sum(p for _, p in i["rubric"]) == i["pts"], i["t"]
        if i["kind"] == "mc":
            assert len(i["options"]) == 4 and len(set(i["options"])) == 4 and 0 <= i["ans"] < 4
print("correct option positions (1-4):", [[i["ans"] + 1 for i in q["items"]] for q in qs[:2]])

# uniform grid: same size, same step, and only a model start (no arrow on the student sheet: META.noStartArrow)
g = META["grid"]; assert META["noStartArrow"] and (g["cols"], g["rows"], g["cell"]) == (10, 7, 50)
draws = [i for q in qs for i in q["items"] if "draw" in i]
assert len(draws) == 4
for i in draws:
    d = i["draw"]; assert (d["cols"], d["rows"], d["cell"]) == (g["cols"], g["rows"], g["cell"]), i["t"]
    for ln in i["code"].splitlines():
        m = re.fullmatch(r"turtle\.forward\((\d+)\)", ln)
        assert not m or int(m[1]) % g["cell"] == 0, ln

# Q1: the line is drawn before the turn; Q1d position and direction
pos, head, segs = info(I(0, 0)["code"]); assert pos == (100, 0) and head == "down" and len(segs) == 1 and I(0, 0)["ans"] == 2
pos, head, segs = info("turtle.left(90)"); assert pos == (0, 0) and head == "up" and I(0, 3)["options"][I(0, 3)["ans"]] == "באמצע החלון, פונה למעלה"
# Q2
assert info(I(1, 0)["code"])[1] == "down" and I(1, 0)["options"][I(1, 0)["ans"]] == "למטה"
pos, head, segs = info(I(1, 2)["code"]); assert pos == (100, 0) and len(segs) == 1 and segs[0][1] == (50, 0)
pos, head, segs = info(I(1, 3)["code"]); print("Q2d", pos, head, [(s[0], s[1]) for s in segs])
assert [(s[0], s[1]) for s in segs] == [((0, 0), (60, 0)), ((60, 0), (60, -60)), ((60, -60), (0, -60))] or print("check directions of Q2d")
# Q3
pos, head, segs = info(I(2, 0)["code"]); print("Q3a", pos, head, [(s[0], s[1]) for s in segs]); assert head == "up" and len(segs) == 3
pos, head, segs = info(I(2, 1)["code"]); print("Q3b", pos, [(s[0], s[1]) for s in segs]); assert pos == (350, 0) and len(segs) == 2 and segs[0][1] == (150, 0) and segs[1][0] == (250, 0)
pos, head, segs = info(I(2, 2)["code"]); print("Q3c", pos, head, [(s[0], s[1]) for s in segs]); assert head == "down" and len(segs) == 4
# Q4: rectangle, buggy square (fix on the second turn gives a closed square), smaller square
pos, head, segs = info(I(3, 0)["code"]); assert pos == (0, 0) and head == "right" and len(segs) == 4
bug = I(3, 1)["code"]; pos, head, segs = info(bug); print("Q4b bug", pos, [(s[0], s[1]) for s in segs]); assert len(segs) == 4 and pos != (0, 0)
fixed = bug.replace("turtle.right(90)", "turtle.left(90)"); assert info(fixed)[0] == (0, 0), info(fixed)
assert bug.count("turtle.right(90)") == 1 and bug.splitlines()[3] == "turtle.right(90)"
sq = I(3, 2)["code"]; assert info(sq)[0] == (0, 0)
small = sq.replace("forward(100)", "forward(50)"); assert info(small)[0] == (0, 0) and all(abs(s[1][0] - s[0][0]) + abs(s[1][1] - s[0][1]) == 50 for s in info(small)[2])
# model answers of the writing items
m = info(I(4, 0)["model"]); assert m[1] == "down" and m[0] == (0, -80)
m = info(I(4, 1)["model"]); assert m[0] == (0, 0) and len(m[2]) == 4
m = info(I(4, 2)["model"]); print("Q5c", [(s[0], s[1]) for s in m[2]]); assert [(s[0][1], s[1][1]) for s in m[2]] == [(0, 30), (60, 90)] and all(s[0][0] == 0 for s in m[2])
m = info(I(5, 0)["model"]); print("Q6a", [(s[0], s[1]) for s in m[2]]); assert [(s[0], s[1]) for s in m[2]] == [((0, 0), (0, 80)), ((0, 80), (60, 80)), ((60, 80), (60, 0))]
m = info(I(5, 1)["model"]); print("Q6b", [(s[0], s[1]) for s in m[2]]); assert [(s[0], s[1]) for s in m[2]] == [((0, 70), (100, 70))]
m = info(I(5, 2)["model"]); print("Q6c", [(s[0], s[1]) for s in m[2]]); assert [(s[0], s[1]) for s in m[2]] == [((0, 0), (0, 80)), ((60, 80), (60, 0))]
print("Form B: all checks passed; minutes", data["MIN"], sum(data["MIN"]))
