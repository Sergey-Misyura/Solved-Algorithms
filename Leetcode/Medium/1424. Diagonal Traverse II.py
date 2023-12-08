"""
1424. Diagonal Traverse II
(Medium complexity)

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
"""

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diags_len = max(max([len(row) for row in nums]), len(nums))
        diags = [[] for _ in range(2*diags_len-1)]

        for n_row, row in enumerate(nums):
            for n_col, num in enumerate(row):
                diags[n_row+n_col].append(num)
        print(diags)
        return [num for diag in diags for num in reversed(diag)]