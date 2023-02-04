"""
283. Move Zeroes
(Easy complexity)

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0

        for curr in range(len(nums)):
            if nums[curr]!=0:
                nums[non_zero_idx], nums[curr] = nums[curr], nums[non_zero_idx]
                non_zero_idx+=1