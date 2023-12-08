"""
1685. Sum of Absolute Differences in a Sorted Array
(Medium complexity)

You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
"""


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        cur_sum = sum([abs(n - nums[0]) for n in nums])
        ans[0] = cur_sum

        cur = 1
        next_cur = cur + 1
        while cur < len(nums):
            next_cur = cur + 1
            while next_cur < len(nums) and nums[next_cur] == nums[cur]:
                next_cur += 1

            diff = nums[cur] - nums[cur - 1]
            cur_sum += diff*cur - diff*(len(nums)-cur)
            for _ in range(next_cur - cur):
                ans[cur] = cur_sum
                cur += 1

        return ans