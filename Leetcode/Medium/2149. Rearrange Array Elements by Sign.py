"""
2149. Rearrange Array Elements by Sign
(Medium complexity)

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            elif num < 0:
                ans[neg] = num
                neg += 2

        return ans



