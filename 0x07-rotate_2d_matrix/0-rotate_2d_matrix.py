#!/usr/bin/python3

rotated_matrix = [] # Initialize a new matrix

def rotate_2d_matrix(matrix):
  rotated_matrix = list(zip(*matrix[::-1]))

