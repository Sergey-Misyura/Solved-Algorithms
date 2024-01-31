"""
53. Maximum Subarray
(Medium complexity)

Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum
