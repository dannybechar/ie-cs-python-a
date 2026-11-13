# 8.3 _ פייתון א _ תרגול לפיצוח - דף עבודה _ תנאי מורכב.docx

Source: `Classwork/8.3 _ תרגול לפיצוח - דף עבודה/8.3 _ פייתון א _ תרגול לפיצוח - דף עבודה _ תנאי מורכב.docx`

תרגול בנושא ביטויים מורכבים

שאלה 1

בכל אחד מהתנאים הבאים, סמנו True (אמת) או False (שקר) עבור התנאים המוצגים:

False

True

3 < 5 and 9 > 10

8 < 7 or 16 > 15

4 <= 3 and 2 == 2

10 <= 10 or 5 != 5

12 < 10 and 5 >= 3

9 != 9 and 6 > 5

(3 > 5 and 9 < 10) or (6 == 6)

(4 < 2 and 8 > 7) or (5 < 5)

(7 > 6 and 12 < 11) and (8 > 8)

(not(2 < 1) and 6 > 5) or not(5 != 10)

שאלה 2

סמנו בעזרת לחצן "צבע סימון", אם תוצאת הביטוי היא True או False:

- print(4 < 2 and 8 > 7)True / False

- print(5 < 4 or 11 > 10)True / False

- print(9 < 8 and 15 > 14)True / False

- print(6 < 5 and 13 > 12)True / False

- print(1 < 0 and 4 > 3)True / False

- print(8 < 7 or 16 > 15)True / False

- print(10 < 9 and 20 > 19)True / False

- print((4 < 2 and 8 > 7) or not(5 == 5))True / False

- print((not(2 < 1) and 6 > 5) or not(10 == 10))True / False

- print((not(9 > 8) and not(15 < 14)) or (11 < 11))True / False

- print((8 > 7 or not(16 < 15)) or (14 == 14))True / False

- print((not(10 < 9) and 20 > 19) or not(15 == 15))True / False

שאלות לתרגול נוסף

שאלה 3

כתבו תוכנית הקולטת סכום כסף שנחסך ומספר חודשי חיסכון. אם הסכום הנחסך  עולה על 4,000 ש"ח, או שתקופת החיסכון  עולה על 10 חודשים, הדפיסו הודעה שאתם יכולים לקנות מחשב נייד.

העתיקו את הקישור לפתרון, או הגישו את הפתרון כקובץ. 

saved_amount = float(input("Enter the amount of money saved: "))

months = 

if _________ > 4000 or _________ > 10:

    print("You can buy a laptop!")

שאלה 4

כתבו תוכנית הקולטת את גובהו וגילו של אדם. אם האדם גבוה  מ-130 ס"מ, וגם גילו מעל 13 שנה, הוציאו הודעה שהוא יכול לנסוע ברכבת ההרים.

השלימו, הריצו והעתיקו את הפתרון

height = int(input("Enter the person's height: "))

age = int(input("Enter the person's age: "))

if   ___________  and _____________:

    print("You can go on the roller coaster!")

else:

     print( ____________________________)

שאלה 5

נבחן יהיה זכאי לקבל רישיון נהיגה, אם הוא מקיים שלושה תנאים:

- גילו מעל 17 שנה, 

- הוא עבר בהצלחה את מבחן התאוריה 

- עבר בהצלחה את מבחן הנהיגה המעשי. 

כתבו פעולה שתקלוט את שלושת המדדים הנ"ל ותדפיס הודעה מתאימה: האם זכאי לרשיון או לא זכאי לרשיון נהיגה. 

השלימו, הריצו והעתיקו את הפתרון

def ex5():

    age = int(input("Enter the age of the applicant: "))

    theory_test = input("Has the applicant passed the theory test? (y/n): ")

    driving_test = input("Has the applicant passed the driving test? (y/n): ")

    if  ______________  and ______________  and ________________ :

          print (“זכאי לרשיון נהיגה”)

    else:

          print(“אינו זכאי לרשיון נהיגה)

ex5()

דף עבודה בנושא תנאים ותנאים מורכבים

שאלה 1

בכל אחד מהתנאים הבאים, סמנו True (אמת) או False (שקר) עבור התנאים המוצגים:

False

True

3 < 5 and 9 > 10

8 < 7 or 16 > 15

4 <= 3 and 2 == 2

10 <= 10 or 5 != 5

12 < 10 and 5 >= 3

9 != 9 and 6 > 5

(3 > 5 and 9 < 10) or (6 == 6)

(4 < 2 and 8 > 7) or (5 < 5)

(7 > 6 and 12 < 11) and (8 > 8)

(not(2 < 1) and 6 > 5) or not(5 != 10)

שאלה 2

סמנו בעזרת לחצן "צבע סימון", אם תוצאת הביטוי היא True או False:

- print(4 < 2 and 8 > 7)True / False

- print(5 < 4 or 11 > 10)True / False

- print(9 < 8 and 15 > 14)True / False

- print(6 < 5 and 13 > 12)True / False

- print(1 < 0 and 4 > 3)True / False

- print(8 < 7 or 16 > 15)True / False

- print(10 < 9 and 20 > 19)True / False

- print((4 < 2 and 8 > 7) or not(5 == 5))True / False

- print((not(2 < 1) and 6 > 5) or not(10 == 10))True / False

- print((not(9 > 8) and not(15 < 14)) or (11 < 11))True / False

- print((8 > 7 or not(16 < 15)) or (14 == 14))True / False

- print((not(10 < 9) and 20 > 19) or not(15 == 15))True / False

כתיבת תוכניות - רשות

- כתבו תוכנית הקולטת סכום כסף שנחסך ומספר חודשי חיסכון. אם הסכום הנחסך עולה על 4,000 ש"ח, או שתקופת החיסכון  עולה על 10 חודשים, הדפיסו הודעה שאתם יכולים לקנות מחשב נייד.

- כתבו תוכנית הקולטת את נפח הזיכרון הפנוי בתיקיית התמונות. אם הערך הנקלט הוא פחות מ-2 מגה, הוציאו הודעה שלא נשאר מקום בזיכרון, וצריך למחוק תמונות.

- כתבו תוכנית הקולטת את גובהו וגילו של אדם. אם האדם גבוהמ-130 ס"מ, וגם גילו מעל 13 שנה, הוציאו הודעה שהוא יכול לנסוע ברכבת ההרים.

- נבחן יהיה זכאי לקבל רישיון נהיגה, אם הוא מקיים שלושה תנאים: גילו מעל 17 שנה, הוא עבר בהצלחה את מבחן התאוריה ואת מבחן הנהיגה המעשי. כתבו תוכנית שבה תקבלו כקלט את שלושת המדדים הנ"ל. אם הנבחן אינו זכאי לרשיון נהיגה, הדפיסו את הסיבה הרלוונטית. כתבו תוכנית המממשת את קטע הקוד בהתאם לאילוצים.

פתרונות אפשריים לשאלות הפתוחות:

פתרון תרגיל 1

saved_amount = float(input("Enter the amount of money saved: "))

months = int(input("Enter the number of saving months: "))

if saved_amount > 4000 or months > 10:

    print("You can buy a laptop!")

פתרון תרגיל 2

free_space = float(input("Enter the free space in the picture folder (in megabytes): "))

if free_space < 2:

    print("Out of space! Delete some pictures.")

פתרון תרגיל 3

height = int(input("Enter the person's height: "))

age = int(input("Enter the person's age: "))

if height > 130 and age > 13:

    print("You can go on the roller coaster!")

פתרון תרגיל 4

age = int(input("Enter the age of the applicant: "))

has_passed_theory_test = input("Has the applicant passed the theory test? (yes/no): ").lower()

has_passed_driving_test = input("Has the applicant passed the driving test? (yes/no): ").lower()

if age <= 17:

    print("Applicant is not eligible for a driving license due to age.")

elif has_passed_theory_test != 'yes':

    print("Applicant is not eligible for a driving license as they have not passed the theory test.")

elif has_passed_driving_test != 'yes':

    print("Applicant is not eligible for a driving license as they have not passed the driving test.")

else:

    print("Applicant is eligible for a driving license. Congratulations!")

()lower פעולה זו מאפשרת להציג מחרוזת באותיות קטנות. נרחיב על כך בהמשך לימודינו.
