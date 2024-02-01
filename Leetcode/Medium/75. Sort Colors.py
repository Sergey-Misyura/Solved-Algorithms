"""
75. Sort Colors
(Medium complexity)

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lf, mid, rg = 0, 0, len(nums)-1
        while mid <= rg:
            if nums[mid] == 0:
                nums[lf], nums[mid] = nums[mid], nums[lf]
                lf += 1; mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[rg], nums[mid] = nums[mid], nums[rg]
                rg -= 1