"""
1155. Number of Dice Rolls With Target Sum
(Medium complexity)

You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 10**9 + 7.
"""


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (n + 1) for _ in range(target + 1)]
        for i in range(1, k + 1):
            if i <= target:
                dp[i][1] = 1
            else:
                break
        for j in range(2, n + 1):
            for i in range(j, target + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] - dp[i - min(i - 1, k) - 1][j - 1]

        return dp[target][n] % (10 ** 9 + 7)