"""
3. Longest Substring Without Repeating Characters
(Medium complexity)

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        output = float('inf')

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s

                output = min(output, s, key=lambda x: abs(target - x))

        return output


