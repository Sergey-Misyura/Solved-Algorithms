"""
368. Largest Divisible Subset
(Medium complexity)

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.
"""


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums) == 0:
            return []
        ans = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(ans[i]) < len(ans[j]) + 1:
                    ans[i] = ans[j] + [nums[i]]

        return max(ans, key=len)

