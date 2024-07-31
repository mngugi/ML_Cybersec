import numpy as np

# Define the matrix
matrix_x = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
])

# Calculate the determinant
determinant = np.linalg.det(matrix_x)
determinant
