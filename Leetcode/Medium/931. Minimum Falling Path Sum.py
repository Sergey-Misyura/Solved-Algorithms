"""
931. Minimum Falling Path Sum
(Medium complexity)

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)."""


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        lf, rg = 0, 0

        for row in range(1, rows):
            for col in range(cols):
                if col == 0:
                    lf, rg = 0, 2
                else:
                    lf = 1
                    rg = 1 if col == cols - 1 else 2

                # cell value + min of prev row 2 or 3 cells
                matrix[row][col] = matrix[row][col] + min(matrix[row - 1][col - lf:col + rg])

        return min(matrix[-1])