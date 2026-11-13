# [Template] 16.3 _ פייתון א _ תרגול לפיצוח - דף עבודה - מונה צובר ומספר אקראי.docx

Source: `Classwork/16.3 _ תרגול לפיצוח - דף עבודה - מונה צובר ומספר אקראי/[Template] 16.3 _ פייתון א _ תרגול לפיצוח - דף עבודה - מונה צובר ומספר אקראי.docx`

תרגול לפיצוח - דף עבודה - מונה צובר ומספר אקראי

שאלה 1לפניכם קטע תוכנית שמטרתו למנות את כמות סוגי הדגלים בים במהלך 30 יום. 

השלימו את החסר בקטע שלפניכם: (תוכלו לכתוב את מספר הפקודה מהתרמילון במקום הקטעים החסרים)

(01) count_red = 0(02) count_white = 0(03) count_black = 0(04)(05) for i in range(_____):(06)    color = input("Enter color : ")(07)     if color.lower() == _________(08)        ______________(09)    elif color.lower() == "white":(10)        count_white += 1(11)     ____________(12)       count_black += 1 (01)   (13) print(count_red, _________, count_black)

תרמילון:

1.  30

2.  count_white

3.  :else

4.      :"red"

5.  count_red += 1

שאלה 2

לפניכם קטע תוכנית המונה כמות תיקונים לטכנאי, השלימו את החסר: (תוכלו לכתוב את מספר הפקודה במקום הקטעים החסרים)

(01) employee_num = _______(input("Enter num of employees"))(02) total = 0(03) for i in range(___________):

(04)   _____________= int(input("Enter number of fixes "))(05)   if number_fix > _______:(06)       print("Bonus")

(07)     total = _____________________(08) print(total)

השלימו את החסר מהתרמילון שלפניכם:

1. number_fix

2.  total + number_fix

3. employee_num

4. 25

5. int

שאלה 3 - ממבחן מפמ"ר

המטרה של כל קטע קוד היא לקלוט 10 ציונים, למנות ולהדפיס את כמות הציונים הגבוהים

מ 55 אך קטנים מ 80 .

עבור רצף הציונים הבא : 76 84, 80, 57, 77, 90, 68, 74, 100, 55,  יודפס 5 .

ציין עבור כל קטע קוד האם הוא מבצע את הנדרש בשאלה. 

אם לא, הסבר כיצד ניתן לתקן את הקוד כך שיבצע את הנדרש. 

קטע א: 

(01) count = 0 

(02) for item in range (10): 

(03)          grade = int(input("Please enter a grade:")) 

(04)          if grade > 55 and grade < 80: 

(05)                  count = count + 1 

(06) print(count)

האם הקוד מבצע את הנדרש? ________________

אם כן, הסבירו. אם לא, הציעו דרך לתקן את הקוד. 

קטע ב: 

(01) count = 0 

(02) for item in range (10): 

(03)           grade = int(input("Please enter a grade:")) 

(04)           if grade > 55 or grade < 80: 

(05)                      count = count + 1 

(06) print(count)

האם הקוד מבצע את הנדרש? _______

אם כן, הסבירו. אם לא, הציעו דרך לתקן את הקוד. 

קטע ג: 

(01) count = 0 

(02) index = 0 

(03) while index < 10: 

(04)          grade = int(input("Please enter a grade : ")) 

(05)          if grade > 55 and grade < 80: 

(06)                        count = count + 1 

(07) print(count)

האם הקוד מבצע את הנדרש? _____________

אם כן, הסבירו. אם לא, הציעו דרך לתקן את הקוד. 

קטע ד: 

(01) count = 0 

(02) index = 10 

(03) while index > 0: 

(04)            grade = int(input("Please enter a grade : ")) 

(05)            if grade > 55 and grade < 80: 

(06)                     print(count + 1) 

(07)             index = index - 1 

(08) print(count)

האם הקוד מבצע את הנדרש? ______

אם כן, הסבירו. אם לא, הציעו דרך לתקן את הקוד. 

תרגיל 4 

קבלה לעבודה

לפניכם תוכנית שתקלוט לכל אחד מ- 100 המועמדים את מספר שנות הלימוד האקדמיות שלו ואת מספר שנות הוותק שלו. 

התוכנית תמנה את מספר המועמדים המתאימים לתפקיד בכיר, ותציג מספר זה כפלט. הערה: הניחו כי המספרים הנקלטים שלמים והקלט תקין

לפניכם מקרא משתנים:

noth = 0 #not hired

work = 0 #worker

manage = 0 #manager

sel = 0

def work()

for i in range(100):

 imp = int(input(“Years of employment : ")) 

 _______ = int(input(“Years of study : "))

 sel = _____________

 if______________:

   ______________

   noth = noth + 1

 elif sel>=8 and sel<=15:

   print("Hired to work")

   work =+1

 elif sel >= 16:

   print(“Hired to manager")

   ____________

print(noth, work, manage)

work()

השלימו את החסר מהתרמילון שלפניכם:

- mange =+1

- print("Not haired")

- study 

- imp * study

- sel<=7

תרגיל 5 

עליכם לפתוח מנעול חדר הבריחה  בעל 3 ספרות. באמצעות בחירה מבין הספרות  0 עד 9 עם חזרות.

לפניכם תוכנית הבודקת האם פיצחתם את הקוד ואתם יכולים לצאת מחדר הבריחה.

הערה: הניחו כי המספרים הנקלטים שלמים והקלט תקין

sod = "574"

new_sod = " "

alert = "Locked"

ans = True

count = 0 

i=0

while(ans):

count = count + 1

if count == 5:

print(alert)ans = False

elif count < 5:

for j in range(9): 

for k in range(9):

new_sod = str(i)+str(j)+str(k)

if(sod == new_sod):

alert = "Get in "

ans = False

print(alert, new_sod, sod)

א. ענו על השאלות שלפניכם:

- יתן לנסות לפצח את הקוד 5  פעמים             

- המשתנה count צובר             

- המשתנה count מונה כניסות             

- הלולאה תסתיים כאשר ans == False             

- המשתנה ans אותחל בערך True             

- בקוד אין לולאות מקוננות             

ב. עדכנו את הקוד כך שמספר הניחושים יהיה 3.

ג. אתגר: עדכנו את הקוד כך שניתן לנחש מבין הספרות 1 עד 9 ללא חזרות.
