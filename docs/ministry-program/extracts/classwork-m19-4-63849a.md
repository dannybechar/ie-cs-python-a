# [Template] 19.4 _ תרגול לפיצוח - דף עבודה.docx

Source: `Classwork/19.4 _ תרגול לפיצוח - דף עבודה/[Template] 19.4 _ תרגול לפיצוח - דף עבודה.docx`

שיעור 19 | תרגול לפיצוח - דף עבודה

שאלה 1

לפניכם מחרוזת. עבור כל אחד מהפקודות בטבלה, רשמו מה הפלט המתקבל עבור המחרוזת.

my_string = ‘The Matrix’

פקודה

פלט

print(my_string[5])

print(len(my_string))

print(my_string[-5])

print(my_string[ : : 3])

print(my_string[5 : -4])

print(my_string[ : ])

שאלה 2

חברת סרטים קיבלה תסריט ארוך, שנכתב כך שבין כל אות לאות יש רווחים מיותרים. החברה מבקשת לתקן את התסריט, ולבטל את הרווחים המיותרים במהירות. מתכנתי החברה כתבו תוכנית המקבלת מחרוזת, ומדפיסה מחרוזת חדשה ללא רווחים.

א. השלימו את החלקים החסרים בקוד שלפניכם:

- def remove_spaces(my_string):

- my_new_string = בחרו

- for בחרו in my_string:

- if ot != ' ':

- my_new_string = my_new_string + בחרו

- בחרו(my_new_string)

- בחרו("T h e  L o r d  o f  t h e  R i n g s :  T h e  R e t u r n  o f  t h e  K i n g ")

ב. אחת המתכנתות הציעה את הקוד שלפניכם. 

- def remove_spacesB(my_string):

-    my_new_string = ''

-    for i in range(len(my_string)):

-        if not (my_string[i] == ' '):

-            my_new_string = my_new_string + my_string[i]

- print(my_new_string)

- remove_spacesB("T h e  L o r d  o f  t h e  R i n g s :  T h e  R e t u r n  o f  t h e  K i n g ")

האם הפלט יהיה זהה או שונה? נמקו את תשובתכם.

ג. מבין קטעי הקוד שלפניכם, בחרו את הקוד המונה את מספר המופעים של המילה 'The':

my_string = ‘TheLordoftheRings:TheReturnoftheKing’

- my_string.count('The')

- my_string.lower('The')

- my_string.upper('The')

- my_string.index('The')

תשובה: בחרו את התשובה הנכונה

ד. מבין קטעי הקוד שלפניכם, בחרו את הקוד שבודק אם תת-המחרוזת 'Return' מופיעה במחרוזת my_string.

my_string = ‘TheLordoftheRings:TheReturnoftheKing’

- 'Return' not in my_string

- my_string in 'Return'

- 'Return' in my_string

- my_string.in('Return')

תשובה: בחרו את התשובה הנכונה

ה. איתן הציע שיפור לקוד. הוא כתב פעולה בשם fix_spaces.

- def fix_spaces(text):

-   fixed_text = text.replace(' '*2, '#')

-   fixed_text = fixed_text.replace(' ', '')

-   fixed_text = fixed_text.replace('#', ' ')

-    print(fixed_text)

my_string = "T h e  L o r d  o f  t h e  R i n g s :  T h e  R e t u r n  o f  t h e  K i n g"

fix_spaces(my_string)

ענו נכון / לא נכון:

- בשורה 2, מחליפים רווחים כפולים בתו '#'בחרו 

- בשורה 3, מחליפים רווח אחד בשני רווחיםבחרו 

- בשורה 4, מחליפים את התו '#'ברווח אחדבחרו 

- הפתרון המתקבל הוא: The Lord of the Rings: The Return of the King. בחרו 

שאלה 3

חברת אבטחת מידע פיתחה קוד שמטרתו לחולל סיסמאות חזקות. מחולל הסיסמאות יוצר סיסמה באורך 8 תווים. התווים הם מסוג ספרה. אם תיבחר הספרה '0', היא תוחלף בתו '#'.

א. השלימו את הקוד שלפניכם:

- import random

- def password_creator():

-    בחרו = ''

-    for i in range(בחרו):

-        item = random.randint(בחרו)

-        if item == 0:

-            my_password = my_password + בחרו

-        else:

-            my_password = בחרו + str(item)

-    print(בחרו)

- password_creator()

ב. איזה פלט יתקבל עבור הקלטים הבאים?

קלט (אקראי) משמאל לימין 

פלט

23404045

23401148

שאלה 4

ברישום לאפליקציה יש להוסיף את כתובת המייל של הנרשמים. כדי למנוע תקלות יש לבדוק את תקינות המייל.

לפניכם תוכנית. קראו את התוכנית וענו על השאלות.

- def check_mail(mail_address):

-    if (' ' not in mail_address) and ('@' in mail_address) and ('.' in mail_address):

-        print('Cleared')

-    else:

-        print('Not cleared')

- check_mail('donald_duck@gmail.com')

- check_mail('spong bob#gmail_com')

מה הפלט המתקבל בתום הרצת התוכנית, עבור:

שורה 6: ________________________________________

שורה 7: ________________________________________

שאלה 5

לפניכם הפעולה correct_sentence_case המקבלת משפט באנגלית. הפעולה תתקן את המשפט, כך שבתחילת כל משפט, וגם לאחר נקודה, תופיע אות גדולה.

- def correct_sentence_case(text):

-    corrected_text = ""

-    capitalize_next = True

-    for char in text:

-        if capitalize_next and char.isalpha():

-           corrected_text += char.upper()

-           capitalize_next = False

-        else:

-            corrected_text += char

-        if char == ' . ':

-            capitalize_next = True

-    print(corrected_text)

- my_string = "it is sunny outside. let's go to the sea."

- correct_sentence_case(my_string)

א. לפניכם אלגוריתם מילולי. השלימו את החסר:

- בשורה 2, יוצרים מחרוזת בחרו בשם corrected_text, שתאחסן את התוצאה המתוקנת.

- בשורה 3, תפקידו של המשתנה  בחרו לבדוק אם צריך להגדיל את האות הבאה.

- הלולאה מבצעת את הפעולות הבאות, על כל תו במחרוזת המקורית:

- אם התו הראשון המתקבל הוא אות, הופכים אותו ל בחרו ומוסיפים ל בחרו .

- אחרת, מוסיפים אותו למחרוזת המתוקנת.

- אם התו הנוכחי הוא  בחרו , יש להגדיל את  בחרו .

- בשורה 12,  בחרו את המחרוזת ה בחרו .

- בשורה 14, קוראים לפעולה  בחרו .

ב. רשמו את הפלט לאחר ההרצה, עבר המחרוזת בשורה 13:

_________________________________________________

שאלה 6

לפניכם רמזים. עליכם לגלות מה המחרוזת המתקבלת:

my_string = '_____________________'

hint1 = my_string[4:10]

hint2 = "wheels" in my_string

hint3 = my_string.index('the')

hint4 = my_string.index('bus')

hint5 = my_string[ : 3]

hint6 = len(my_string)

hint7 = my_string.count(‘ ‘)

print(hint1, hint2, hint3, hint4, hint5, hint6, hint7)

פלט:wheels True 14 18 The 36 4

שאלה 7

לפניכם המחרוזת:

my_string = ‘* *** ***** ******** ********** ************ ****************’

א. לפניכם תוכנית שסורקת את המחרוזת, כך שכל רצף של כוכביות יודפס בשורה נפרדת.

- current_sequence = ''

- for ot in my_string:

-     if ot == '*':

-         current_sequence += ot

-     elif ot == ' ':

-         if current_sequence:

-             print(current_sequence)

-             current_sequence = ''

- if current_sequence:

-     print(current_sequence)

מה הפלט המתקבל בתום ההרצה?

ב. שאלת אתגר: מה מבצעת הפקודה split? _______________________________

my_string = '* *** ***** ******** ********** ************ ****************'

star_sequences = my_string.split()

for sequence in star_sequences:

    print(sequence)

שאלות הרחבה והעמקה 

שאלה 8

כתבו פעולה המקבלת שתי מחרוזות, ובודקת אם מחרוזת אחת מכילה את השנייה. יש להדפיס הודעה מתאימה.

העתיקו את הקישור לפתרון. 

שאלה 9

כתבו פעולה המחזירה "אמת", אם התו הראשון שווה לתו האחרון במחרוזת המתקבלת מהמשתמש.

העתיקו את הקישור לפתרון. 

שאלה 10

א. כתבו פעולה המקבלת מחרוזת, ומחזירה מחרוזת חדשה, שכל תו בה מופיע פעמיים. יש להסיר את תווי הרווח.

הפעולה תדפיס את המחרוזת החדשה.

לדוגמה: עבור המחרוזת 'ab c de', תודפס המחרוזת 'aabbccddee'.

העתיקו את הקישור לפתרון. 

ב. כתבו פעולה המקבלת מחרוזת, ומחזירה מחרוזת חדשה, שכל תו בה מופיע פעמיים. הפעם יש להשאיר את תווי הרווח, אך לא להכפיל אותם.

לדוגמה: עבור המחרוזת 'ab c de', תודפס המחרוזת 'aabb cc ddee'.

העתיקו את הקישור לפתרון. 
