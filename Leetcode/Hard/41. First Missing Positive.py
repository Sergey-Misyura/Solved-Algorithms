"""
41. First Missing Positive
(Hard complexity)

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            if abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1