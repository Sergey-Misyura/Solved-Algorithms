"""
1464. Maximum Product of Two Elements in an Array
(Easy complexity)

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = -1
        for n in nums:
            if n >= m2:
                m1 = m2
                m2 = n
            else:
                m1 = max(m1, n)

        return (m1-1)*(m2-1)