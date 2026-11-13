# [Template] 15.2 _ פייתון א - תרגול לפיצוח - דף עבודה מחרוזות.docx

Source: `Classwork/15.2 _ תרגול לפיצוח - דף עבודה/[Template] 15.2 _ פייתון א - תרגול לפיצוח - דף עבודה מחרוזות.docx`

15.2 | תרגול לפיצוח - דף עבודה 

מחרוזות Strings 

מחרוזת = רצף של תווים במחשב

האופרטורים חיבור (+) וכפל (*) 

האופרטורים חיבור (+) וכפל (*) 

שאלה 1

א. הקלידו את הקוד הבא וכתבו את הפלט המתקבל:text1 = "I like to play, "text2 = "piano"text3 = "guitar"print (text1 +  text2)  print (text1 +  text3)print( text3 * 2)print (text2 * 3)

text1 = "I like to play, "

text2 = "piano"

text3 = "guitar"

print (text1 +  text2)  

print (text1 +  text3)

print( text3 * 2)

print (text2 * 3)

ב. מה משמעות הסימן +  בין שתי מחרוזות?

ג. מה משמעות הסימן * בין מספר שלם למחרוזת?

שאלה 2 א. הקלידו את הקוד הבא וכתבו את הפלט המתקבל:num1 = "123"num2 = "45"num3 = "7"print (num1 + num2)print (num2 + num3)print (num2 * 4)print (num3 * 9)

num1 = "123"

num2 = "45"

num3 = "7"

print (num1 + num2)

print (num2 + num3)

print (num2 * 4)

print (num3 * 9)

ב. השתמשו באופרטורים +,* ובמשתנים num2, num3 וצרו את הפלט  457457457. ההוראה תהיה: 

אורך הטקסט | len

אורך הטקסט | len

שאלה 3

א. הקלידו את הקוד הבא וכתבו את הפלט המתקבל:text1 = "I like to play, "text2 = "piano"text3 = “guitar”print ( len(text1)  )print ( len(text2)  )print ( len(text2 + text3)  )print ( len (text3 + text2) )

text1 = "I like to play, "

text2 = "piano"

text3 = “guitar”

print ( len(text1)  )

print ( len(text2)  )

print ( len(text2 + text3)  )

print ( len (text3 + text2) )

ב. מה מבצעת הפעולה len?

המרה | str| int

המרה | str| int

שאלה 4לפניכם קטע ובו שני משתנים.

num_1 מקבל את המחרוזת 123, ו-num_2  מקבל מספר שלם 451.num_1 = "123"num_2 = 451print (num_1)print (int(num_1))print (num_1+str(num_2))print (int(num_1)+num_2)word = num_1+str(num_2)print (word[-4])

num_1 = "123"

num_2 = 451

print (num_1)

print (int(num_1))

print (num_1+str(num_2))

print (int(num_1)+num_2)

word = num_1+str(num_2)

print (word[-4])

א. הקלידו את שורות הקוד וכתבו את הפלט המתקבל.

ב. מה מבצעת ההוראה ()int?

ג. מה מבצעת ההוראה ()str?

טבלת ASCII

טבלת ASCII

שאלה 5 

חפשו ברשת והגדירו בקצרה מהי טבלת ASCII.

שאלה 6הקלידו את שורות הקוד הבאות וכתבו לצד כל שורה את הפלט המתקבל.

________________________________print (chr(112))  print (chr(105)) print (chr(97))  print (chr(110) )print (chr(111))  print (ord("p"))	print (ord("i"))	print (ord("a"))	print (ord("n"))	print (ord("o"))	

print (chr(112))  

print (chr(105)) 

print (chr(97))  

print (chr(110) )

print (chr(111))  

print (ord("p"))	

print (ord("i"))	

print (ord("a"))	

print (ord("n"))	

print (ord("o"))	

________________________________

________________________________

________________________________

________________________________

________________________________

________________________________

________________________________

________________________________

________________________________

שאלה 7 הגדירו קטע קוד שמטרתו הדפסת שמכם בקוד ASCII.

שאלה 8 א. מה מבצעת הפעולה chr?

ב. מה מבצעת הפעולה ord?

index [ ]

index [ ]

שאלה 9הקלידו את שורות הקוד הבאות וכתבו לצד כל שורה את הפלט המתקבל:word = "piano"	print (word[0])print (word[1])	print (word[4])	print (word[-1])	print (word[-2])print (word[-3])print (word[-4])	

word = "piano"	

print (word[0])

print (word[1])	

print (word[4])	

print (word[-1])	

print (word[-2])

print (word[-3])

print (word[-4])	

___________________________

___________________________

___________________________

___________________________

___________________________

___________________________

___________________________

___________________________

שאלה 10הקלידו את הפעולה הבאה:  ([print(word[5

מהו הפלט המתקבל? מדוע?

שאלה 11

לפניכם טבלה בת שני טורים: פלט והפעולה בפייתון. 

עבור משתנה number, לכל ערך פלט המתבקש בטבלה, יש להגדיר 2 הוראות פלט אפשריות (לדוגמה, הדפסת המספר 5). 

number ="12345"

הפלט

הפעולה בפייתון

5

print (number[4] )

print (number[-1] )

4

3

2

1

חיתוך Slicing

חיתוך Slicing

text[start :end: jump]

text[start :end: jump]

שאלה 12הקלידו את הפעולות בטבלה ורשמו את הפלט המתקבל עבור משתנה text.

  text = "I like to play drums"

הפלט

הפעולה בפייתון

print (text[2:6] )

print (text[6: ] )

print( text[ :15] )

drums

to play

print( text[2:20:2 ])

print( text[1:15:3] )

print( text[ : :-1] )

Ikoar

Ko

print (text[-10:-6])

print (text[-20:-14])

print (text[-20:-14:2])

שאלה 13הקלידו את הפעולות בטבלה ורשמו את הפלט המתקבל  עבור משתנה number.

  number = "572483291"

הפלט 

הפעולה בפייתון

572

print (number[0:3] )

print (number[-9:-6] )

483

291

52821

42

789

הפעולה in

הפעולה in

שאלה 14א. הקלידו את שורות הקוד הבאות וכתבו את הפלט המתקבל:print ('a' in 'jerusalem')print ('x' in 'jerusalem')print ('2' in str(12345) )print ('9' in str(12345) )

print ('a' in 'jerusalem')

print ('x' in 'jerusalem')

print ('2' in str(12345) )

print ('9' in str(12345) )

ב. מה מבצעת הפעולה in?

ג. כתבו פעולה לבדיקה האם הספרות 9 או 3 מופיעות במספר:

הפעולה find

הפעולה find

שאלה 15א. הקלידו את שורות הקוד הבאות וכתבו את הפלט המתקבל:text = "I LIKE TO PLAY DRUMS"print (text.find('L') )print (text.find('LIKE') )print (text.find('PIANO') )print (text.find('L',3) )print (text.find('L',12) )

text = "I LIKE TO PLAY DRUMS"

print (text.find('L') )

print (text.find('LIKE') )

print (text.find('PIANO') )

print (text.find('L',3) )

print (text.find('L',12) )

ב. מה מבצעת הפעולה (find(str,begin,end?

שאלה 16

כתבו פעולה המקבלת מחרוזת. 

אם המחרוזת מכילה את המילה war, יש להחליפה במילה flower. 

הפעולות ()lower() | upper 

הפעולות ()lower() | upper 

שאלה 17א. הקלידו את שורות הקוד הבאות וכתבו את הפלט המתקבל:print ("piano".upper() )print ("DRUMS".lower() )print( "Piano And Drums".upper() )

print ("piano".upper() )

print ("DRUMS".lower() )

print( "Piano And Drums".upper() )

ב. השלימו: 

מה מבצעת כל אחת מהפעולות הבאות?upper __________________________________________________________

lower __________________________________________________________

שאלה 18 כתבו פעולה המקבלת מחרוזת. על הפעולה להחזיר True, אם המחרוזת מכילה את המילים “yes” או “YES”. בכל מקרה אחר, הפעולה תחזיר False. השתמשו בפעולות upper/ lower.

endwith/ startswith()

endwith/ startswith()

שאלה 19

א. הקלידו את שורות הקוד הבאות וכתבו את הפלט המתקבל:text = "I like to play drums"print (text.startswith('I like') )print (text.startswith( 'play', 10, 17 ) )print (text.startswith( 'to play', 10, 17 ) )

text = "I like to play drums"

print (text.startswith('I like') )

print (text.startswith( 'play', 10, 17 ) )

print (text.startswith( 'to play', 10, 17 ) )

ב. הסבירו בקצרה את מבנה הפעולות הבאות ומטרתן: 

startswith(str,begin,end) 

endswith(str,begin,end) 

replace

replace

שאלה 20עיינו בקישור הבא.

הסבירו את מבנה הפעולה ומטרתה: ( replace(old,new,max  

שאלה 21כתבו פעולה המקבלת מחרוזת. על הפעולה להחליף את התו | בתווים we ב-3 הפעמים הראשונות שבהן הוא מופיע. 

count

count

שאלה 22

העתיקו את שורות הקוד הבאות וכתבו את הפלט המתקבל:text = "I like to play guitar and piano and drums"print (text.count("and") )print (text.count("and",25) )print (text.count ("play") )print (text.count("books") )

text = "I like to play guitar and piano and drums"

print (text.count("and") )

print (text.count("and",25) )

print (text.count ("play") )

print (text.count("books") )

שאלה 23הסבירו את מבנה ההוראה ומטרתה:  (count(str,begin,end

שאלה 24כתבו פעולה המקבלת מחרוזת. על הפעולה למנות ולהחזיר כמה פעמים מופיע רצף התווים "the" במחרוזת. 

לחקור ברשת

לחקור ברשת

שאלה 25

לכל אחת מהפעולות הבאות, הסבירו בקצרה מה הפעולה מבצעת, ותנו דוגמה הממחישה את מטרת הפעולה: 

מה מבצעת הפעולה ודוגמה

הפעולה בפייתון

text.index(str)

text.isdigit()

text.isalpha()

text.islower()

text.isdigit()

text.isupper()

 שאלה 26 

 לפניכם קטע קוד:

א. מה מבצע הקוד?

ב. מה מבצעת הפעולה ( 'message.encode('text? 

ג. מה מבצעת הפעולה ( 'message.b64decode('text? 
