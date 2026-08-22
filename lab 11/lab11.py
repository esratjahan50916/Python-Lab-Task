import numpy as np

# Problem 1

arr = np.array([12, 5, 8, 1, 19, 3])
k = 3
sorted_arr = np.sort(arr)
k_smallest = sorted_arr[:k]
print(f"{k} smallest values:", k_smallest)

# Problem 2

arr = np.array([1, 3, 5, 3, 7, 3, 9])
item = 3
n = 2
positions = np.where(arr == item)[0]
if len(positions) >= n:
    print(f"The {n}th occurrence of {item} is at index:", positions[n-1])
else:
    print("Item does not repeat that many times")

# Problem 3

mat = np.array([[1, 2, 3],
                 [4, 5, 6]])
column_sums = np.sum(mat, axis=0)
row_sums = np.sum(mat, axis=1)
print("Column sums:", column_sums)
print("Row sums:", row_sums)

# Problem 4

x = np.array([10, 20, 30])
y = np.array([1, 2, 3])
print("Addition:", np.add(x, y))
print("Subtraction:", np.subtract(x, y))
print("Multiplication:", np.multiply(x, y))
print("Division:", np.divide(x, y))

# Problem 5

arr = np.array([2, 4, 7, 11])
print("Sum:", np.sum(arr))
print("Product:", np.prod(arr))
print("Difference between consecutive elements:", np.diff(arr))
