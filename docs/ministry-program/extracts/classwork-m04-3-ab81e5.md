# 4.3 _ תרגול לפיצוח _ דף פעולות חלק א' _ פעולות.docx

Source: `Classwork/4.3 _ תרגול לפיצוח - דף עבודה/4.3 _ תרגול לפיצוח _ דף פעולות חלק א' _ פעולות.docx`

שיעור 4 | תרגול לפיצוח | דף עבודה - פעולה חלק א'

הניחו בכל אחד מהתרגילים שלפניכם שהקלט תקין.

תרגיל 1

עבור כל אחת מהפעולות בטבלה רשמו מהו הפלט המתקבל:

סעיף

פעולה

פלט

א

def ex1():

       num = 34

       a = num + 10

       b = num / 10

       print(b * 10 + a)

ex1()

ב

def ex2():

       a = 10

       b = 30

       c = 20

       print(a + b * c)

ex2()

ג

def ex3():

       a = 5

       b = 2

       c = 10

       print(a * b + c)

ex3()

ד

def ex4():

       a = 3

       b = 2

       c = 1

       print(a + 2 * b + 3 * c)

ex4()

ה

def ex5():

       a = 10

       b = 30

       c = 20

       print((a + b) // c)

ex5()

ו

def ex6():

       a = 10

       b = 30

       print( (b + a) / (b - a) )

ex6()

תרגיל 2לפניכם פעולה הקולטת לשני משתנים שונים את כמות מגשי הפיצה ומחיר הפיצה. הפעולה מחשבת ומדפיסה על העלות הכוללת לתשלום.

השלימו את החסר בקוד שלפניכם (היעזרו בתרמילון):

def calculate_pizza_order():

    # קבלת קלט מהמשתמש

    num_pizzas = int(input("Enter the number of pizzas: "))

   price_per_pizza= float(input("Enter the price per pizza: "))

    # חישוב המחיר הכולל

    total_price = num_pizzas * price_per_pizza

    # הצגת התוצאה

    print("The total price for pizzas is: ",total_price , "nis")

# קריאה לפעולה

calculate_pizza_order()

תרמילון:

int(input("Enter the number of pizzas: "))

price_per_pizza

total_price

תרגיל 3

לפניכם פעולה המציגה מידע על בית ספר:

def school_info():

    school_name = "ABC High School"

    address = "123 Main St, Anytown"

    principal = "Mrs. Smith"

    print("School: ", school_name)

    print("Address: ",  address)

    print("Principal: ",principal)

# קריאה לפעולה

school_info()

א. סמנו (ע"י הדגשה) את התשובה הנכונה ביותר: 

כדי לקלוט את שם בית הספר עלינו לרשום את הפקודה הבאה:

- input("Enter school name: ")

- int(input("Enter school name: "))

- float(input("Enter school name: "))

- print("Enter school name: ")

ב. סמנו את התשובה הנכונה ביותר: 

שם הפעולה הוא:

- school_info

- principal 

-  school_name

- def

ג. עדכנו את הפעולה כך שתקלוט מהמשתמש את המידע ותדפיס הודעה מתאימה.

הדביקו את הקוד או קישור לקוד

תרגיל 4

כתבו פעולה בשם ()rectangle הקולטת למשתנים a  ו b ערכי מספרים המציינים אורך צלעות מלבן. על הפעולה לחשב ולהדפיס את שטח המלבן.

הדביקו את הקוד או קישור לקוד

תרגיל 5

כתבו פעולה בשם ()pool, הקולטת לשני משתנים את כמות הפעמים שאנו מתכוונים להגיע לבריכה (times) ואת מחיר הכניסה (price).הפעולת תחשב ותדפיס את המחיר הכולל לתשלום.הדביקו את הקוד או קישור לקוד 

תרגיל 6

כתבו פעולה בשם ()super. הפעולה תקלוט ערכים ל 2 משתנים. 

במחיר לתשלום תתקבל הנחה של 10%.

bottle #כמות בקבוקי שתייה

price #מחיר בקבוק שתייה אחד

הפעולה תחשב ותדפיס את המחיר לתשלום עבור מספר בקבוקי השתייה לפני ההנחה ואחרי ההנחה. יש להדפיס את המחירים בתוספת הודעה מתאימה.

הדביקו את הקוד או קישור לקוד
