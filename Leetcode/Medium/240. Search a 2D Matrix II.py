"""
240. Search a 2D Matrix II
(Medium complexity)

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        cur_i, cur_j = m - 1, 0

        while cur_i >= 0 and cur_j < n:
            if target < matrix[cur_i][cur_j]:
                cur_i -= 1
            elif target > matrix[cur_i][cur_j]:
                cur_j += 1
            else:
                return True

        return False
