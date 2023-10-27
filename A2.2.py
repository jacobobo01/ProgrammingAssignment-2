import numpy as np

# Define the inverse of matrix A as the cipher matrix
A_inverse = np.array([
    [0, 1, 1, 0],
    [22, 21, 7, 8],
    [4, 5, 3, 4],
    [17, 18, 13, 15]
])

# Read the linear sequence of numbers from the text file
with open("input-A22.txt", "r") as file:
    sequence = list(map(int, file.read().split()))

# Pad the sequence with zeros to ensure it can be reshaped into a 4 x n matrix
while len(sequence) % 4 != 0:
    sequence.append(0)

# Convert the sequence into a 4 x n matrix of numbers
n = len(sequence) // 4
matrix_C = np.array(sequence).reshape(4, n)

# Decrypt the matrix C by multiplying it with the inverse of matrix A
matrix_B = np.dot(A_inverse, matrix_C) % 26

# Convert the matrix B to the original plaintext message
num_to_char = {i: chr(97 + i) for i in range(26)}
plaintext = ''
for col in range(matrix_B.shape[1]):
    for row in range(matrix_B.shape[0]):
        plaintext += num_to_char[matrix_B[row][col]]

# Display the original plaintext message
print("Original plaintext message:")
print(plaintext)
