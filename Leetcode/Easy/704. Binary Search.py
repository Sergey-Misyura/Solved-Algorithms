"""
704. Binary Search
(Easy complexity)

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            curr = (left + right) //2
            if nums[curr] == target: return curr
            elif nums[curr] > target: right = curr -1
            elif nums[curr] < target: left = curr +1

        return -1