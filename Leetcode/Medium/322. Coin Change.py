"""
322. Coin Change
(Medium complexity)

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [float('inf')] * amount
        for cur_sum in range(1, amount + 1):
            for coin in coins:
                if cur_sum - coin >= 0:
                    dp[cur_sum] = min(dp[cur_sum], dp[cur_sum - coin] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]
