#Problem 1

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

d3 = {}

for i in d1:
    d3[i] = d1[i]

for i in d2:
    if i in d3:
        d3[i] = d3[i] + d2[i]
    else:
        d3[i] = d2[i]

print(f"Counter({d3})")

#Problem 2

original = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

frequency = {}

for i in original:
    value = original[i]
    if value in frequency:
        frequency[value] = frequency[value] + 1
    else:
        frequency[value] = 1

print("Original Dictionary:", original)
print("Frequency of values:", frequency)

#Problem 3

def isPalindrome(s):
    s = s.lower()

    rev = ""
    for i in range(len(s) - 1, -1, -1):
        rev = rev + s[i]

    if s == rev:
        return True
    else:
        return False

#Problem 4


word = input("Enter a string: ")

if isPalindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


def uniqueList(lst):
    newList = []

    for item in lst:
        if item not in newList:
            newList.append(item)

    return newList


sample = [1, 2, 3, 3, 3, 3, 4, 5]

print("Original List:", sample)
print("Unique List  :", uniqueList(sample))

#Problem 5

def countElements(lst):
    counts = {}

    for i in lst:
        if i in counts:
            counts[i] = counts[i] + 1
        else:
            counts[i] = 1

    for i in counts:
        print(i, "=>", counts[i])


sample = [10, 20, 30, 30, 30, 30, 20, 40]

print("Sample List:", sample)
countElements(sample)

#Problem 6

startsWith = lambda string, prefix: string[:len(prefix)] == prefix

string = input("Enter the main string: ")
prefix = input("Enter the prefix to check: ")

result = startsWith(string, prefix)

if result == True:
    print(string, "starts with", prefix)
else:
    print(string, "does noy start with", prefix)
