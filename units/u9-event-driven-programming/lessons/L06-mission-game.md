# יחידה 9.6 – תכנות מונחה אירועים

כיתה ז׳ · Python A · **משחק המשימה: מקשים, לחיצה וטיימר — נקודת ביקורת מסכמת**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> משחק הוא אוסף של אירועים, לכל אחד תגובה, והם חולקים כמה משתנים: הניקוד, הזמן, והאם המשחק פעיל.

## דף עזר

| אירוע | מאזין | תגובה | מה משתנה |
|---|---|---|---|
| חץ במקלדת | `turtle.onkey` | `move_up()` … | מקום הצב, `score` |
| לחיצה על המסך | `turtle.onscreenclick` | `place_target(x, y)` | `target_x`, `target_y` |
| עברה שנייה | `turtle.ontimer` | `tick()` | `time_left`, `running` |

<div dir="rtl">

- סדר התוכנית: משתנים ← פונקציות ← רישום כל המאזינים ← הפעלת הטיימר ← `turtle.done()`.
- אחרי סוף המשחק: כל תזוזה בודקת את `running`.
- דף העזר של הבחינה כולל `dot(size)`, `xcor()`, `ycor()`, `goto`, `onclick`, `onkeypress`, `mainloop`. הפקודות `distance` ו-`clear` במשחק שלנו אינן בדף העזר.

</div>

## 1. נקודת ביקורת א׳: המשחק (בזוגות, כל אחד שומר עותק)

פתחו את `Game_Starter.py`. החצים שמאלה וימינה כבר עובדים.

<div dir="rtl">

1. **שלב 1:** כתבו `move_up()` ו-`move_down()` וחברו אותן לחצים. כל תזוזה מזמנת את `check_hit()`.
2. **שלב 2:** כתבו `place_target(x, y)` — לחיצה על המסך מעבירה את המטרה.
3. **שלב 3:** כתבו `tick()` — ספירה לאחור של 30 שניות, שמסתיימת ב-`Game over` ובניקוד.
4. **שלב 4:** אחרי `Game over` הצב לא זז (`if running:` בכל תזוזה).

</div>

## 2. בדיקת עמיתים

בדקו משחק של זוג אחר: כל החצים, לחיצה, פגיעה (הניקוד עולה, המטרה עוברת), סוף הזמן, וניסיון לזוז אחרי הסוף.

## 3. נקודת ביקורת ב׳ (על דף, בלי להריץ)

```python
def tick():
    global time_left
    if time_left > 0:
        time_left = time_left - 1
        print("Time:", time_left)
        turtle.ontimer(tick, 1000)
    else:
        print("Game over")
```

<div dir="rtl">

1. איזה אירוע ואיזה מאזין: לחיצה על חץ · לחיצה על נקודה · כל שנייה?
2. `time_left = 3`, ואז `tick()`. מה יודפס?
3. התוכנית של עדי (בסגנון הבחינה), בהמשך: כל לחיצה מציירת ריבוע במקום הלחיצה, באדום ובכחול לסירוגין (הלחיצה הראשונה אדומה), וצלע כל ריבוע גדולה ב-2 מהקודם. השלימו את החסר.
4. למה ל-`place_target(x, y)` יש פרמטרים, ול-`move_up()` אין?

</div>

```python
import turtle


def do_it(x, y):
    global click_num
    global size
    player.penup()
    player.goto(x, y)
    player.shapesize(size)
    if ______ % 2 == 0:
        player.color("____")
    else:
        player.color("____")
    player.stamp()
    click_num = ______ + ____
    size = ______ + ____


tw = turtle.Screen()
click_num = 0
size = 2
player = turtle.Turtle()
player.shape("square")
tw.onclick(do_it)
turtle.mainloop()
```

## 4. מתעדים ושומרים

מעל כל פונקציה — הערה.

שומרים: `File › Save As` ← `G7_U9_M6_Game_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. איזה אירוע מפעיל כל תגובה במשחק שלכם?
2. איזה מידע נשמר בין האירועים?
3. מה מתחיל את שרשרת הטיימר?

</div>
