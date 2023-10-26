"""
823. Binary Trees With Factors
(Medium complexity)

Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
"""

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}

        for num in arr:
            dp[num] = 1

        for index, first in enumerate(arr):
            for second in arr[0:index]:
                div, rem = divmod(first, second)
                if not rem and div in dp:
                    dp[first] += dp[second]* dp[div]

        return sum(dp.values()) % (10**9+7)