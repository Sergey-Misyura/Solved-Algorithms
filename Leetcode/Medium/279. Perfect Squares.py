"""
279. Perfect Squares
(Medium complexity)

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""


class Solution:
    def numSquares(self, n):
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            cur_min = float('inf')
            j = 1
            while j * j <= i:
                cur_min = min(cur_min, dp[i - j * j] + 1)
                j += 1
            dp[i] = cur_min
        return dp[n]