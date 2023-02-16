#!/usr/bin/python3

 def rotate_2d_matrix(self, matrix: List[List[int]]) -> None:
        def transpose(A):
            R, C = len(A), len(A[0])
            T = [[None] * R for _ in range(C)]
            for r in range(R):
                for c in range(C):
                    T[c][r] = A[r][c]
            return T       
        
        matrix[:] = transpose(matrix)
        for r in range(len(matrix)):
            matrix[r] = matrix[r][::-1]
