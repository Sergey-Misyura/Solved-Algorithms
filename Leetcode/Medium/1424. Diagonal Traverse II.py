"""
1424. Diagonal Traverse II
(Medium complexity)

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
"""

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                if len(ans) <= i + j:
                    ans.append([])
                ans[i + j].append(a)
        return [a for r in res for a in reversed(r)]