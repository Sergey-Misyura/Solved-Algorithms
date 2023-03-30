"""
74. Search a 2D Matrix
(Medium complexity)

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lf, rg = 0, rows*cols-1
        while lf < rg:
            mid = (lf+rg)//2
            if matrix[mid//cols][mid % cols] < target:
                lf = mid+1
            else:
                rg = mid
        return matrix[lf//cols][lf % cols] == target

