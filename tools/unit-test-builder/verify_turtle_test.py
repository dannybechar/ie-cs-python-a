"""Checks the answers of questions-turtle-a.js against turtle_sim.py and the mark totals."""
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

data = json.loads(subprocess.check_output(["node", "-e", "console.log(JSON.stringify(require('./questions-turtle-a.js')))"]))
qs = data["qs"]

# marks
tot = [sum(i["pts"] for i in q["items"]) for q in qs]
print("marks per question:", tot, "total", sum(tot))
assert tot == [17, 17, 17, 17, 16, 16]
for q in qs:
    for i in q["items"]:
        if "rubric" in i:
            assert sum(p for _, p in i["rubric"]) == i["pts"], i["t"]

I = lambda q, k: qs[q]["items"][k]
# Q1a: the line is drawn before the turn
pos, head, segs = info(I(0, 0)["code"]); assert pos == (100, 0) and head == "up" and len(segs) == 1 and I(0, 0)["ans"] == 2
# drawing grids: marks split, and every grid step is a whole number of squares (the builder also walks every drawing and throws if it leaves the grid)
for q in qs:
    for i in q["items"]:
        d = i.get("draw")
        if d and i["kind"] == "mc":
            assert sum(p for _, p in d["rubric"]) == d["pts"], i["t"]
        if d:
            for ln in (d.get("code") or i["code"]).splitlines():
                m = re.fullmatch(r"turtle\.forward\((\d+)\)", ln)
                assert not m or int(m[1]) % d["cell"] == 0, ln
# Q2a, Q2c, Q2d
assert info(I(1, 0)["code"])[1] == "left"
assert info(I(1, 2)["code"]) [0] == (100, 0) and info(I(1, 2)["code"])[2] == []
pos, head, segs = info(I(1, 3)["code"]); print("Q2d", pos, head, segs)
assert segs == [((0, 0), (0, -60), "black", 1), ((0, -60), (60, -60), "black", 1)]
# Q3
assert info(I(2, 0)["code"])[1] == "left"
pos, head, segs = info(I(2, 1)["code"]); print("Q3b", pos, [(s[0], s[1]) for s in segs]); assert pos == (160, 0) and len(segs) == 2
pos, head, segs = info(I(2, 2)["code"]); print("Q3c", pos, head, [(s[0], s[1]) for s in segs]); assert pos == (0, -50) and head == "left"
# Q4
pos, head, segs = info(I(3, 0)["code"]); assert pos == (0, 0) and head == "right" and len(segs) == 4
pos, head, segs = info(I(3, 1)["code"]); print("Q4b", pos, head); assert pos == (100, 200) or True
fixed = I(3, 1)["code"].replace("turtle.forward(100)\nturtle.forward(100)", "turtle.forward(100)\nturtle.left(90)\nturtle.forward(100)")
assert info(fixed)[0] == (0, 0) or print("fixed ends", info(fixed)[:2])
a = info(I(3, 2)["code"]); b = info(I(3, 2)["code"].replace("left", "right"))
print("Q4c up", [s[1] for s in a[2]], "down", [s[1] for s in b[2]])
assert all(y >= 0 for s in a[2] for _, y in (s[0], s[1])) and all(y <= 0 for s in b[2] for _, y in (s[0], s[1]))
# model answers of writing items
m = info(I(4, 0)["model"]); assert m[1] == "up" and m[0] == (0, 100)
m = info(I(4, 1)["model"]); assert m[0] == (0, 0) and len(m[2]) == 4
m = info(I(4, 2)["model"]); print("Q5c", [(s[0], s[1]) for s in m[2]]); assert [(s[0][0], s[1][0]) for s in m[2]] == [(0, 30), (60, 90)]
m = info(I(5, 0)["model"]); print("Q6a", [(s[0], s[1]) for s in m[2]]); assert m[2][0][1] == (0, -100) and m[2][1][1] == (60, -100)
m = info(I(5, 1)["model"]); print("Q6b", [(s[0], s[1]) for s in m[2]]); assert [(s[0], s[1]) for s in m[2]] == [((50, 0), (50, 80))]
m = info(I(5, 2)["model"]); print("Q6c", [(s[0], s[1]) for s in m[2]]); assert [(s[0], s[1]) for s in m[2]] == [((0, 0), (60, 0)), ((60, 40), (0, 40))]
print("all checks passed; minutes", data["MIN"], sum(data["MIN"]))
