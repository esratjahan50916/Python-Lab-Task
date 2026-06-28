#Problem 1

string = "hello .py"

words = string.split()
result = ""

for word in words:
    rev = ""
    for i in range(len(word) - 1, -1, -1):
        rev = rev + word[i]
    result = result + rev + " "

result = result.strip()
print(result)

#Problem 3

numbers = [34, -7, 89, 12, 56, 3, 100, 45]

max = numbers[0]
min = numbers[0]

for i in numbers:
    if i > max:
        max = i
    if i < min:
        min = i

print("List    :", numbers)
print("Maximum :", max)
print("Minimum :", min)

#Problem 4

numbers = [10, 25, 38, 49, 56, 72, 89]

target = int(input("Enter the number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(target, "found at index", i)
        found = True
        break

if found == False:
    print(target, "not found")

#problem 5

sampleList = [10, 20, 30, 20, 50]

print("Sample List:", sampleList)

for i in range(len(sampleList)):
    if sampleList[i] == 20:
        sampleList[i] = 200

print("Result :", sampleList)

#Problem 6

original = [10, 20, 30, 20, 50]

newlist = []

for item in original:
    if item not in newlist:
        newlist.append(item)

print("Original:", original)
print("List without duplicates:", newlist)

#problem 7

myList = ['aca', 'xyz', 'aba', '1221']

count = 0

for word in myList:
    if len(word) >= 2:                  
        if word[0] == word[-1]:          
            count = count + 1

print("Sample List :", myList)
print("Count       :", count)
