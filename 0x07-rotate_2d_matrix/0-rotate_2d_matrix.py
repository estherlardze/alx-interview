#!/usr/bin/python3

rotated_matrix = [] # Initialize a new matrix

def rotate_2d_matrix(matrix):
  rotated_matrix = list(zip(*matrix[::-1]))
  
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

