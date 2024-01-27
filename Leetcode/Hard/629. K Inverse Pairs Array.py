"""
629. K Inverse Pairs Array
(Hard complexity)

For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 10**9 + 7.
"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1

        mod = 10 ** 9 + 7
        dp = [0] + [1] * (k + 1)
        for cur_n in range(2, n + 1):
            second_dp = [0]
            for cur_k in range(k + 1):
                cur_count = dp[cur_k + 1]
                if cur_k >= cur_n:
                    cur_count -= dp[cur_k - cur_n + 1]
                second_dp.append((second_dp[-1] + cur_count) % mod)
            dp = second_dp

        return (dp[k + 1] - dp[k]) % mod

