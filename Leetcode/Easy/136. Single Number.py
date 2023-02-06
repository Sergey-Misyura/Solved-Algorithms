"""
136. Single Number
(Easy complexity)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        single_dict={}
        for num in nums:
            if num in single_dict:
                single_dict.pop(num)
            else:
                single_dict[num]=1
        
        return single_dict.popitem()[0]