import numpy as np

# Problem 1

a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print("Original:", a)
print("Reshaped:\n", b)

# Problem 2

arr = np.array([5, 12, 8, 12, 20])
value_to_find = 12
result = np.where(arr == value_to_find)
print("Value found at index(es):", result[0])

# Problem 3

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
even_numbers = arr[arr % 2 == 0]
print("Even numbers:", even_numbers)

# Problem 4

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 9, 3, 8, 5])
positions = np.where(a == b)
print("Matching positions:", positions[0])

# Problem 5

arr = np.array([3, -2, 7, -5, 0, -1])
arr[arr < 0] = 0
print("After replacing negatives:", arr)
