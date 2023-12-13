"""
1582. Special Positions in a Binary Matrix
(Easy complexity)

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
"""


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        transp_mat = list(zip(*mat))

        sum_mat = [sum(row) for row in mat]
        rows = [i for i, sm in enumerate(sum_mat) if sm == 1]
        sum_transp_mat = [sum(row) for row in transp_mat]
        cols = [i for i, sm in enumerate(sum_transp_mat) if sm == 1]

        return sum([mat[i][j] for i in rows for j in cols])
