"""
2542. Maximum Subsequence Score
(Easy complexity)

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [0] * (rowIndex + 1)
        row[0] = 1

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row
