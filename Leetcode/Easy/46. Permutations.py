"""
46. Permutations
(Medium complexity)

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[num] + sec for i, num in enumerate(nums)
                for sec in self.permute(nums[:i] + nums[i + 1:])] or [[]]