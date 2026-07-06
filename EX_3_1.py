import numpy as np

# Array Attributes
arr = np.array([[1, 2, 3], [4, 2, 5]])
print(f"Type: {type(arr)} | Dimensions: {arr.ndim} | Shape: {arr.shape} | Size: {arr.size}")

# Slicing Matrix Columns/Rows
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print("\nOriginal Array:\n", a)
print("Row 1 onwards:\n", a[1:])
print("Second Column:", a[:, 1])
print("Second Row:", a[1, :])