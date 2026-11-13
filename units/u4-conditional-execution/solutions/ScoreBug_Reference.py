# Unit 4.2 - reference for ScoreBug_Starter.py (the bug-fixing task).
# The four fixes, in the order Python reports them:
#   1. = became ==   2. colon after the condition
#   3. indented body of if   4. indented body of else
score = int(input("Score: "))
if score == 100:
    print("Perfect")
else:
    print("Not perfect")
