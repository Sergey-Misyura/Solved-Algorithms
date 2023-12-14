"""
2482. Difference Between Ones and Zeros in Row and Column
(Medium complexity)

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.
"""

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        len_rows = len(grid)
        len_cols = len(grid[0])

        transp_grid = list(zip(*grid))

        diff_rows = [2*sum(row)-len_cols for row in grid]
        diff_cols = [2*sum(col)-len_rows for col in transp_grid]

        return [[col + row for col in diff_cols] for row in diff_rows]