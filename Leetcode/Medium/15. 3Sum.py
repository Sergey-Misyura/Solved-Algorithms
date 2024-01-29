"""
15. 3Sum
(Medium complexity)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        nums = [float('-inf')] + nums
        n = len(nums)

        for i in range(1, n - 2):
            if nums[i] == nums[i - 1]:
                continue
            lf, rg = i + 1, n - 1
            while lf < rg:
                sum_ = nums[i] + nums[lf] + nums[rg]
                if sum_ < 0:
                    lf += 1
                elif sum_ > 0:
                    rg -= 1
                else:
                    ans.add((nums[i], nums[lf], nums[rg]))
                    while lf < rg and nums[lf] == nums[lf + 1]:
                        lf += 1
                    while lf < rg and nums[rg] == nums[rg - 1]:
                        rg -= 1
                    lf += 1
                    rg -= 1

        return ans
