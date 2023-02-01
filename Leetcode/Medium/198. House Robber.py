"""
198. House Robber 
(Medium complexity)

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing 
each of them is that adjacent houses have security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        sum_max = [0] * n
        sum_max[0] = nums[0]

        if (n > 1): sum_max[1] = max(nums[0], nums[1])

        for i in range(2, n):
            sum_max[i] = max(sum_max[i-1], sum_max[i-2] + nums[i])
    
        return sum_max[-1]