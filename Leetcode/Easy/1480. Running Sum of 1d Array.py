"""
1480. Running Sum of 1d Array
(Easy complexity)

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_ = 0
        nums_sum = []
        for num in nums:
            sum_ = num+sum_
            nums_sum.append(sum_)
        return nums_sum 