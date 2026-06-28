x = 10
y = 20
print(f"Before swap: x = {x} y = {y}")
x, y = y, x
print(f"After swap:  x = {x} y = {y}")

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance = d = {d}")


n = int(input("Enter a number : "))

if n % 2 == 0:
   print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")


c = input("Enter a charecter : ")
vowel = "aeiouAEIOU"
if c in vowel:
    print(f"{c} is a vowel.")
else:
    print(f"{c} is not a vowel.")


mark = float(input("Enter your mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark. Enter a value between 0 and 100.")
elif mark >= 90:
    print(f"Marks: {mark} = Grade: A+ (GPA: 4.00)")
elif mark >= 85:
    print(f"Marks: {mark} = Grade:A  (GPA: 4.00)")
elif mark >= 80:
    print(f"Marks: {mark} = Grade:A- (GPA: 3.70)")
elif mark >= 75:
    print(f"Marks: {mark} = Grade: B+ (GPA: 3.30)")
elif mark >= 70:
    print(f"Marks: {mark} = Grade:B  (GPA: 3.00)")
elif mark >= 65:
    print(f"Marks: {mark} = Grade: B- (GPA: 2.70)")
elif mark >= 60:
    print(f"Marks: {mark} = Grade:C+ (GPA: 2.30)")
elif mark >= 55:
    print(f"Marks: {mark} = Grade:C  (GPA: 2.00)")
elif mark >= 50:
    print(f"Marks: {mark} = Grade: C- (GPA: 1.70)")
elif mark >= 45:
    print(f"Marks: {mark} = Grade: D+ (GPA: 1.30)")
elif mark >= 40:
    print(f"Marks: {mark} = Grade: D  (GPA: 1.00)")
else:
    print(f"Marks: {mark} = Grade:F  (GPA: 0.00)")

