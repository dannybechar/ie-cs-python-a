# [Template] 9.2 _ תרגול לפיצוח _ דף עבודה _ פעולות המחזירות ערך.docx

Source: `Classwork/10.4 _ תרגול לפיצוח - דף עבודה/[Template] 9.2 _ תרגול לפיצוח _ דף עבודה _ פעולות המחזירות ערך.docx`

,

דף עבודה | פעולות המחזירות ערך(בדף זה 11 שאלות)1

1

לפניכם פעולה.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def even(num):

  if num % 2 == 0:

    return True

  else:

    return False

קריאה לפעולה

הערך המתקבל

print(even(12))

print(even(5))

print(even(3))

print(even(44))

2

2

לפניכם פעולה.

 מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def power(num1, num2):

  return num1 ** num2

קריאה לפעולה

הערך המתקבל

print(power(2, 3))

print(power(-2, 3))

print(power(4, 3))

print(power(5, 2))

3

3

לפניכם פעולה.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def repeat(word, count):

  return word * count

קריאה לפעולה

הערך המתקבל

print(repeat(“2”, 3))

print(repeat(“Hi”, 5)

print(repeat(“Python”, 4))

print(repeat(“*”, 2))

4

4

לפניכם פעולה.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def factorial(num1):

ans=1

for i in range(1, num1+1):

ans = i*ans

return ans

קריאה לפעולה

הערך המתקבל

print(factorial(5))

print(factorial(3))

print(factorial(2))

print(factorial(1))

5

5

לפניכם פעולה.

 מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def bus(num_of_passengers):

  if num_of_passengers > 10 and num_of_passengers < 60:

    return "Go"

  else:

    return "Stay"

קריאה לפעולה

הערך המתקבל

print(bus(45))

print(bus(60))

print(bus(11))

print(bus(80))

6

6

לפניכם פעולה.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def revenue(rev_per_hour, hours_per_day):

  return rev_per_hour * hours_per_day * 365

קריאה לפעולה

הערך המתקבל

print(revenue(100, 30))

print(revenue(200, 50))

print(revenue(1000, 400))

print(revenue(300, 200))

7

7

לפניכם פעולה.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:(ייתכן פלט עשרוני מטיפוס float).

def velocity(distance, time):

  return float(distance / time)

קריאה לפעולה

הערך המתקבל

print(velocity(50, 25))

print(velocity(100, 20))

print(velocity(200, 40))

print(velocity(150, 2))

8

8

לפניכם פעולה.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def average(grade1, grade2):

  return (grade1 + grade2)//2

קריאה לפעולה

הערך המתקבל

print(average(100, 90))

print(average(75, 88))

print(average(60, 79))

print(average(85, 90))

9

9

לפניכם פעולה.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def mod(num1, num2):

  return num1 % num2

קריאה לפעולה

הערך המתקבל

print(mod(10, 3))

print(mod(10, 5))

print(mod(15, 4))

print(mod(21, 2))

10

10

בעלי חנות פרחים בודקים בכל יום א' מהו המלאי שנותר להם. הם מחשבים את כמות הפרחים בתחילת השבוע הקודם ומפחיתים את הכמות שנמכרה.

num_flowers - משתנה המייצג את כמות הפרחים במלאי בתחילת השבוע הקודם.sold_last_week - משתנה המייצג את כמות הפרחים שנמכרה עד תום השבוע הקודם.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def flower_shop_inventory(num_flowers, sold_last_week):

  return num_flowers - sold_last_week  

קריאה לפעולה

הערך המתקבל

print(flower_shop_inventory(1000, 300))

print(flower_shop_inventory(400, 100))

print(flower_shop_inventory(100, 45))

print(flower_shop_inventory(500, 200))

11

11

לפניכם פעולה.

מלאו בטבלה את הערך המתקבל לאחר קריאה לפעולה:

def guess_game(num1, num2):

  if num1 > num2:

    return "Too low"

  elif num1 < num2:

   return "Too high"

  else:

    return "You got it!"

קריאה לפעולה

הערך המתקבל

print(guess_game(8, 3))

print(guess_game(3, 8))

print(guess_game(5, 4))

print(guess_game(10, 2))
