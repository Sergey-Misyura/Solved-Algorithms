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
        non_zero_idx = 0  # индекс числа не 0
        for curr in range(len(nums)):  # проходим по массиву
            if nums[curr]!=0:  # переставляем каждое не 0 число в место по индексу non_zero_idx, в итоге 0 окажутся в конце
                nums[non_zero_idx], nums[curr] = nums[curr], nums[non_zero_idx]
                non_zero_idx+=1