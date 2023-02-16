#!/usr/bin/python3

# Initialize a new matrix
rotated_matrix = []

def rotate_2d_matrix(matrix):
  for i in range(0, len(matrix)):
    for j in range(i, len(matrix)):
      matrix[i][j] = matrix[j][i]
  

    for i in range(N/2):
      for j in range(N):
        matrix[i][j], matrix[j][len(matrix)-1-i] = matrix[j][len(matrix)-1-i], matrix[i][j]

rotate_2d_matrix(matrix):
