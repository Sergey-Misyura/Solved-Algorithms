"""
1980. Find Unique Binary String
(Medium complexity)

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
"""


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""

        for digit in range(len(nums)):
            if nums[digit][digit] == '0':
                ans += '1'
            else:
                ans += '0'

        return ans