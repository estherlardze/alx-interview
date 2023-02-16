#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """

    n = len(matrix)   # first the matrix is tranposed
    for i in range(0, n):
      for j in range(i, i):
        matrix[i][j] = matrix[j][i]
  

          for i in range(n/2): # swapping rows and columns
            for j in range(n):
              matrix[i][j], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[i][j]

