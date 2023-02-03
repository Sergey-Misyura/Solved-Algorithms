"""
189. Rotate Array 
(Medium complexity)

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        
        l_num, r_num = 0, k-1
        while l_num < r_num:
            nums[l_num], nums[r_num] = nums[r_num], nums[l_num]
            l_num += 1
            r_num -= 1
            
        l_num, r_num = k, len(nums) - 1
        while l_num < r_num:
            nums[l_num], nums[r_num] = nums[r_num], nums[l_num]
            l_num += 1
            r_num -= 1