"""
300. Longest Increasing Subsequence
(Medium complexity)

Given an integer array nums, return the length of the longest strictly increasing
subsequence.
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub_nums = []
        for num in nums:
            if len(sub_nums) == 0 or sub_nums[-1] < num:
                sub_nums.append(num)
            else:
                idx = bisect_left(sub_nums, num)
                sub_nums[idx] = num

        return len(sub_nums)

