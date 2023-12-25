"""
73. Set Matrix Zeroes
(Medium complexity)

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = first_col_zero = False
        rows = len(matrix)
        cols = len(matrix[0])

        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
