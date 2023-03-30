"""
33. Search in Rotated Sorted Array
(Medium complexity)

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lf, rg = 0, len(nums)-1

        while lf < rg:
            mid = (lf + rg) // 2

            if nums[lf] <= nums[mid]:
                if nums[lf] <= target <= nums[mid]:
                    rg = mid
                else:
                    lf = mid + 1
            else:
                if nums[mid] < target <= nums[rg]:
                    lf = mid + 1
                else:
                    rg = mid

        return lf if target == nums[lf] else -1



