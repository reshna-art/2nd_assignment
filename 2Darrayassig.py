import numpy as np

# Create two 2D arrays
matrix1 = np.array([[1, 2, 3], 
                    [4, 5, 6]])
matrix2 = np.array([[7, 8], 
                    [9, 10], 
                    [11, 12]])

# Perform matrix multiplication
result = np.dot(matrix1, matrix2)

# Print the matrices and the result
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nResult of Matrix Multiplication:")
print(result)