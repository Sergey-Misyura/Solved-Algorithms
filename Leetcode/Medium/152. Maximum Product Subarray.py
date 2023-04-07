"""
152. Maximum Product Subarray
(Medium complexity)

Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_cur = min_cur = 1
        max_sum = -float('inf')

        for num in nums:
            temp = (num, num * max_cur, num * min_cur)
            max_cur, min_cur = max(temp), min(temp)
            max_sum = max(max_sum, max_cur)
        return max_sum

