# [Template] 19.3 _ פייתון א _ תרגול לפיצוח 2 - דף עבודה.docx

Source: `Classwork/18.3 _ תרגול לפיצוח #1 - דף עבודה/[Template] 19.3 _ פייתון א _ תרגול לפיצוח 2 - דף עבודה.docx`

שיעור 19 | תרגול לפיצוח - דף עבודה

תרגיל #1 

המורה נתנה לתלמידיה את המשימה הבאה:

"כתבו תוכנית הקולטת שני מספרים שלמים, ומדפיסה הודעה המציינת אם המספרים זוגיים או אי-זוגיים."

התלמידים כתבו פתרונות שונים.

ציינו עבור כל קטע קוד, האם הוא עונה על הדרישה: כן או לא?

אם קטע הקוד אינו עונה על הדרישה, הסבירו מדוע.

הניחו כי בראש כל תוכנית נכתבו שתי שורות הקוד הבאות:

num1 = int (input ('Enter an integer number'))

num2 = int (input ('Enter an integer number'))

סעיף

קוד בשפת python

 האם קטע הקוד עונה על הדרישה: כן/לא?

הסבר

א

if num1 % num2 == 0:

   print(num1, num2, "הם מספרים זוגיים")

else:

   print(num1, num2, "הם מספרים אי זוגיים")

ב

even = num1

odd = num2

print(num1, “”הוא מספר זוגי”)

print(num2, “”הוא מספר אי-זוגי”)

ג

if num1 % 2 == 0:

   print(num1, num2, "הם מספרים זוגיים")

else:

   print(num1, num2, "הם מספרים אי זוגיים")

ד

if num1 % 2 == 0 and num2 % 2 == 0:

   print(num1, num2, "הם מספרים זוגיים")

else:

   print(num1, num2, "הם מספרים אי זוגיים")

ה

if num1 % 2 == 0 and num2 % 2 == 0:

   print(num1, num2, "הם מספרים זוגיים")

elif num1 % 2 != 0 and num2 % 2 != 0:

   print(num1, num2, "הם מספרים אי זוגיים")

else:

   print("אחד מהמספרים זוגי והאחר אי זוגי")

ו

if num1 % 2 == 0:

   if num2 % 2 == 0:

       print(num1, num2, "הם מספרים זוגיים")

   else:

       print("אחד מהמספרים זוגי והאחר אי זוגי")

elif num1 % 2 != 0 and num2 % 2 != 0:

   print(num1, num2, "הם מספרים אי זוגיים")

else:

   print("אחד מהמספרים זוגי והאחר אי זוגי")

תרגיל #2 

לפניכם טבלה ובה שני קטעי קוד.

עבור כל קטע קוד, כתבו בעמודה הריקה מה הפלט המתקבל.

סעיף

קוד בשפת python

הפלט המתקבל

א

for i in range(-5, 0, 1):

   print(i)

ב

for i in range(5):

   print(i)

else:

   print("Done!")

תרגיל #3 

א.  כתבו בעמודה הריקה מה הפלט המתקבל.

ב. מה מטרת קטע הקוד?

קוד בשפת python

הפלט המתקבל

num = 98713

reverse_number = 0

while num > 0 :

   reminder = num % 10

   reverse_number = (reverse_number * 10) + reminder

   num = num // 10

print("Reverse number: ", reverse_number)
