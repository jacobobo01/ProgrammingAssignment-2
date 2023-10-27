import numpy as np

# Define the invertible matrix A
A = np.array([
    [1, -1, -1, 1],
    [2, -3, -5, 4],
    [-2, -1, -2, 2],
    [3, -3, -1, 2]
])

# Define the inverse of matrix A
B = np.array([
    [84, 112, 119, 32, 32, 45, 52],
    [104, 97, 111, 105, 78, 50, 0],
    [101, 115, 114, 115, 67, 48, 0],
    [32, 115, 100, 58, 83, 49, 0]
])

# Read the message to be encrypted from the text file
with open("input-A21.txt", "r") as file:
    message = file.read().strip()

# Convert the message to lowercase and remove any spaces or special characters
message = ''.join(filter(str.isalpha, message.lower()))

# Convert the message into a matrix of numbers
char_to_num = {char: ord(char) - 96 for char in "abcdefghijklmnopqrstuvwxyz"}
matrix_B = []
for char in message:
    matrix_B.append(char_to_num[char])

# Convert matrix B to a 4x4 matrix
while len(matrix_B) % 4 != 0:
    matrix_B.append(0)
matrix_B = np.array(matrix_B).reshape(-1, 4)

# Calculate the cipher matrix C using matrix B and A
matrix_C = np.dot(matrix_B, A) % 26

# Display the matrices B and C
print("Matrix B (plaintext):")
print(matrix_B)
print("\nMatrix C (cipher):")
print(matrix_C)
