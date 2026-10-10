# Warm-up: count the negative numbers. Find two bugs.
negative_count = 1
for i in range(4):
    number = int(input("Number: "))
    if number < 0:
        negative_count = 1
print("Negative:", negative_count)
