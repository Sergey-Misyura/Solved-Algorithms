"""
1887. Reduction Operations to Make the Array Elements Equal
(Medium complexity)

Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.
"""


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                total += i + 1

        return total