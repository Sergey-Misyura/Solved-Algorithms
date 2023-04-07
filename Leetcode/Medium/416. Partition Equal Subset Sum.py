"""
416. Partition Equal Subset Sum
(Medium complexity)

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)
        if s % 2 == 1:
            return False

        s //= 2
        dp = [True] + [False] * s

        for x in nums:

            dp = [dp[s_cur] or (s_cur >= x and dp[s_cur - x]) for s_cur in range(s + 1)]
            if dp[s]:
                return True

        return False
