# includes code for B2.1 and B2.2

import numpy as np
from scipy import linalg

# Get the flow numbers as input values
flow1 = float(input("Enter Flow 1: "))
flow2 = float(input("Enter Flow 2: "))
flow3 = float(input("Enter Flow 3: "))
flow4 = float(input("Enter Flow 4: "))

# Create the augmented matrix
augmented_matrix = np.array([[1, 0, 0, 0, flow1],
                             [0, 1, 0, 0, flow2],
                             [0, 0, 1, 0, flow3],
                             [0, 0, 0, 1, flow4]])

# Display the augmented matrix without periods
print("The augmented matrix is:")
np.set_printoptions(formatter={'float': '{: 0.0f}'.format})
print(augmented_matrix)

# Split the augmented matrix into the coefficient matrix and the constant vector
coefficient_matrix = augmented_matrix[:, :-1]
constant_vector = augmented_matrix[:, -1]

# Use the Gauss-Jordan elimination method to solve the system
result_matrix = linalg.solve(coefficient_matrix, constant_vector)

# Output the resulting matrix without periods
print("\nThe resulting matrix is:")
np.set_printoptions(formatter={'float': '{: 0.0f}'.format})
print(result_matrix)
