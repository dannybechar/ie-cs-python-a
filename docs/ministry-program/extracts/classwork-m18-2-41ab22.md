# [Template] 19.2 _ פייתון א _ תרגול לפיצוח.docx

Source: `Classwork/18.2 _ הגשת משימות/[Template] 19.2 _ פייתון א _ תרגול לפיצוח.docx`

שיעור 19 | תרגול לפיצוח

תרגיל #1 

המורה נתנה לתלמידיה את המשימה הבאה:

"כתבו תוכנית הקולטת שני מספרים שלמים ומדפיסה אותם לפי הסדר, מהקטן לגדול."

התלמידים כתבו פתרונות שונים.

ציינו עבור כל קטע קוד, האם הוא עונה על הדרישה: כן או לא?

אם קטע הקוד אינו עונה על הדרישה, הסבירו את תשובתכם.

הניחו כי בראש כל תוכנית נכתבו שתי שורות הקוד הבאות:

num1 = int (input ('Enter an integer number'))

num2 = int (input ('Enter an integer number'))

סעיף

קוד בשפת python

 האם קטע הקוד עונה על הדרישה: כן/לא?

הסבר

א

min = num1

max = num2

print(num1, num2)

ב

if num1 < num2:

  print(num1, num2)

else:

  print(num2, num1)

ג

if num1 > num2:

  num1 = num1 + num2

  num2 = num1 - num2

  num1 = num1 - num2

print(num1, num2)

ד

if num1 < num2:

   min = num1

   max = num2

else:

   min = num2

   max = num1

print(min, max)

ה

print(num1, num2)

if num2 < num1:

  print(num2, num1)

ו

if num1 > num2:

  num1 = num2

  num2 = num1

print(num1, num2)

ז

if num1 < num2:

  min = num1

else:

  min = num2

print(min, num1+num2-min)

תרגיל #2 

לפניכם טבלה ובה שני קטעי קוד.

עבור כל קטע קוד, תנו דוגמה לקלט שיציג Yes ודוגמה לקלט שיציג No.

סעיף

קוד בשפת python

דוגמה לקלט שיציג Yes

דוגמה לקלט שיציג No

א

num1 = int(input(“Enter first number”))

num2 = int(input(“Enter second number”))

if num1 > 10 and num2 <= 5:

    print(“Yes”)

else:

    print(“No”)

ב

num1 = int(input(“Enter first number”))

num2 = int(input(“Enter second number”))

if (num1 > 6 or num2 <= 5) and num1 == num2:

    print(“Yes”)

else:

    print(“No”)

תרגיל #3 

נתונים שלושה משתנים a, b, c בעלי הערכים הבאים:

a=10, b=15, c=0

חשבו את ערכו של כל אחד מהביטויים בטבלה, וכתבו את הערך בעמודה הריקה.

סעיף

ביטוי בוליאני

ערך הביטוי True/Flase

א

a >= b  or b ==c

ב

a % 5 == 0 and b // 5 > c

ג

a < 0  or ( b == c  + 15 and a >= c)

ד

a % 2 == c % 2 and b % 3 > a % 3

ה

a != b and b != c

תרגיל #4 

לפניכם טבלה ובה ארבעה קטעי קוד.

עבור כל קטע קוד, כתבו בעמודה הריקה מה הפלט המתקבל.

סעיף

קוד בשפת python

הפלט המתקבל

א

for i in range(10):

    if i%3 == 0:

        print(i)

ב

for i in range(10):

    if i%2 == 0 or i%3 == 0:

        print(i)

ג

for i in range(3, 20, 3):

    print(i)

ד

for i in range(30, 0, -5):

    print(i)

תרגיל #5 

לפניכם טבלה ובה שני קטעי קוד.

עבור כל קטע קוד, כתבו בעמודה הריקה מה הפלט המתקבל.

סעיף

קוד בשפת python

הפלט המתקבל

א

for num in range(1, 11):

   if num % 2 == 0:

       print(num)

ב

for num in range(1, 101):

   if num % 3 == 0 and num % 5 == 0:

       print(num)

תרגיל #6 

א. כתבו בעמודה הריקה מה הפלט המתקבל.

ב. מה מטרת קטע הקוד?

קוד בשפת python

הפלט המתקבל

total_odd = 0

for num in range(1, 11):

   if num % 2 != 0:

       total_odd += num

print( total_odd)

תרגיל #7 

א. כתבו בעמודה הריקה מה הפלט המתקבל.

ב. מה מטרת קטע הקוד?

קוד בשפת python

הפלט המתקבל

for num in range(1, 11):

   if num % 2 == 0:

       print(num)

for num in range(10, 0, -1):

   if num % 2 != 0:

       print(num)

תרגיל #8 

בטבלה שלפניכם ארבעה קטעי קוד, והפלט שיתקבל מהרצת קטעי הקוד.

כל קטע קוד מכיל לולאה.

השלימו את החלקים הקחסרים בכל קטע קוד כדי שיתקבל הפלט הנתון.

סעיף

קוד בשפת python

הפלט המתקבל

א

for item in range(____):

    print(item + 1, end=" ")

1 2 3

ב

for item in range (___,___):

    print(item)

3

4

ג

for item in range (6,____ ,____):

    print(item,end=" ")

6 4 2

ד

i=12

while i < ____ :

    i = i + ____

    print(i)

13

14

15

תרגיל #9 

לפניכם שני טורים של קטעי קוד שבכל אחד מהם מבוצעת לולאה. התאימו בין זוגות של לולאות תואמות, כך שבשתי הלולאות יתקבל פלט זהה. 

לדוגמה: שתי הלולאות הבאות תואמות, כי הפלט שלהן זהה: 10 9 8 7 6 5

for item in range(6):

    print(item+5, end=" ")

for item in range(5,11):

    print(item, end=" ")

טור ב

טור א

- for item in range(1, 12):      print(item)

- i = 1while i < 10:      print(i)      i = i + 2

- i = 1while i <= 10:      print(i * 3)      i = i + 1

- for item in range (-5, 6):     print(item + 6)

- i = 8while i > 0:      print(i * 2)      i = i - 2

- i = 1while i <= 30:      if i % 3 == 0:          print(i)       i = i + 1

- for item in range (-4, 5, 2):      print(item + 5)

- for i in range(16, 3, -4):      print(i)

תרגיל #10 

לפניכם טבלה ובה ארבעה קטעי קוד.

עבור כל קטע קוד, כתבו בעמודה הריקה מה הפלט המתקבל.

סעיף

קוד בשפת python

הפלט המתקבל

א

i = 1

while i < 4:

    print(“wow”)

    i += 1

ב

for item in range (6):

    if item % 2 == 1:

       print(item * item)

ג

for item in range (9, 0, -3):

    print (item)

ד

x = 5

i = 1

while i < 4 :

    x -= 1

    i += 1

print (i, x)

תרגיל #11 

מספר מושלם הוא מספר השווה לסכום כל מחלקיו (לא כולל המספר עצמו). 

(לדוגמה: המספר 28 הוא מספר מושלם, כי הוא שווה לסכום כל מחלקיו: 28=1+2+4+7+14)

מחלק הוא מספר המחלק את המספר המחולק עם שארית אפס. 

(לדוגמה: 4 הוא מחלק של 24, אך לא של 23.)

א. לפי ההגדרה לעיל, האם 6 הוא מספר מושלם? אם כן, הציגו ביטוי מתמטי שמראה זאת, כמו בדוגמה.אם לא, הסבירו מדוע.

ב. לפניכם קטע קוד הקולט מספר מהמשתמש, ובודק אם הוא מספר מושלם. השלימו את הקטע. 

def perfect_number():

 num = int(input("Please enter a number:"))

 sum = (1)______ 

 x = 1

 while x < num:

if (2)___ :

sum = sum + (3)_________ 

x=(4)_______

 if (5) _______:

print("Perfect number ")

 else:

print("Not perfect number ")

perfect_number()

תרגיל #12 

קטע הקוד שלפניכם קולט מספר תעודת זהות בן 9 ספרות (number_id), וספרה נוספת(digit), ומדפיס את כל המיקומים במספר ת.ז. שהספרה digit מופיעה בהם (מימין לשמאל).

 אם הספרה לא מופיעה במספר, הפעולה תדפיס 1-. 

דוגמאות: עבור ת.ז. 334429969, והספרה 9, יודפסו המיקומים הבאים: 1 3 4. 

עבור ת.ז. 123457899, והספרה 6, יודפס 1-, כי הספרה 6 לא קיימת במספר ת.ז.

השלימו את הקטע על מנת שיבצע את הנדרש.

def find_location (): 

id_number = int(input("Please enter ID number:")) 

digit = int(input("Please enter a digit:")) 

found = False 

for index in range((1)_______,(2)_______): 

if (3)__________________: 

print((4)____________) 

found = (5)_____________ 

id_number = (6)_______________ 

if found == False: 

print((7)__________) 

find_location() 
