"""
54. Spiral Matrix
(Medium complexity)

Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
