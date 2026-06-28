fruit = ["apple", "banana", "mango", "orange", "pineapple"]

for i in fruit:
    print(f"{i}")



n = int(input("\nEnter a number to countdown from: "))
print(f"Counting down from {n}:")
count = n
while count >= 0:
    print(f"{count}")
    count -= 1
print("Time up")



base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))

result = 1
for i in range(exp):
    result = result * base

print("Answer:", base, "^", exp, "=", result)


total = 0
for num in range(2, 1000):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        total = total + num

print("Sum of all prime numbers below 1000:", total)



N = int(input("Enter a number N: "))

a = 0
b = 1

print("Fibonacci numbers below", N, ":")

while a < N:
    print(a)
    next = a + b
    a = b
    b = next